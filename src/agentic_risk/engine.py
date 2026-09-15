"""A scripted credit-limit pipeline; this is a mechanism check, not an LLM study."""

from __future__ import annotations

import csv
import hashlib
import itertools
import json
import platform
import random
import subprocess
import tomllib
from datetime import datetime, timezone
from pathlib import Path


AUTHORITY_LEVELS = ("recommend", "approve", "execute")
FAULTS = ("clean", "flip")
BACKEND = "scripted-v1"


def validate_config(config: dict) -> dict:
    """Reject ambiguous, unsupported, and duplicate experimental conditions."""
    required = {"experiment_id", "seed", "cases", "authority_levels", "verification", "faults", "scenario"}
    if set(config) != required:
        raise ValueError(f"Config keys must be exactly {sorted(required)}")
    if not isinstance(config["experiment_id"], str) or not config["experiment_id"].strip():
        raise ValueError("experiment_id must be a nonempty string")
    for key, minimum in (("seed", 0), ("cases", 2)):
        if type(config[key]) is not int or config[key] < minimum:
            raise ValueError(f"{key} must be an integer >= {minimum}")
    for key, choices, item_type in (
        ("authority_levels", AUTHORITY_LEVELS, str),
        ("verification", (False, True), bool),
        ("faults", FAULTS, str),
    ):
        values = config[key]
        if not isinstance(values, list) or not values:
            raise ValueError(f"{key} must be a nonempty list")
        if any(type(value) is not item_type or value not in choices for value in values):
            raise ValueError(f"{key} entries must be from {choices}")
        if len(values) != len(set(values)):
            raise ValueError(f"{key} must not contain duplicates")
    scenario = config["scenario"]
    if not isinstance(scenario, dict) or set(scenario) != {"current_limit", "reduced_limit"}:
        raise ValueError("scenario must contain current_limit and reduced_limit")
    if any(type(value) is not int for value in scenario.values()):
        raise ValueError("Limits must be integers in synthetic units")
    if not 0 < scenario["reduced_limit"] < scenario["current_limit"]:
        raise ValueError("Limits must satisfy 0 < reduced_limit < current_limit")
    return config


def load_config(path: str | Path) -> dict:
    return validate_config(tomllib.loads(Path(path).read_text(encoding="utf-8")))


def generate_cases(config: dict) -> list[dict]:
    """Pair conditions on seeded cases; low/high counts differ by at most one."""
    rng = random.Random(config["seed"])
    risks = ["low" if index % 2 == 0 else "high" for index in range(config["cases"])]
    rng.shuffle(risks)
    return [
        {
            "case_id": f"seed-{config['seed']}-case-{index:05d}",
            "true_risk": risk,
            "risk_score": round(rng.uniform(0.05, 0.45) if risk == "low" else rng.uniform(0.55, 0.95), 6),
            **config["scenario"],
        }
        for index, risk in enumerate(risks)
    ]


def policy(risk: str) -> str:
    if risk not in ("low", "high"):
        raise ValueError("Risk must be low or high")
    return "reduce_limit" if risk == "high" else "keep_limit"


def run_trial(case: dict, condition: dict, config: dict) -> dict:
    """Run four stages with truth available only to the evaluator and ideal verifier."""
    if set(condition) != {"authority", "verification", "fault"}:
        raise ValueError("A condition needs authority, verification, and fault")
    authority, verify, fault = (condition[key] for key in ("authority", "verification", "fault"))
    if authority not in AUTHORITY_LEVELS or type(verify) is not bool or fault not in FAULTS:
        raise ValueError("Unsupported experimental condition")
    expected = policy(case["true_risk"])
    observed = case["true_risk"]
    if fault == "flip":
        observed = "high" if observed == "low" else "low"
    recommendation = policy(observed)
    proposed_limit = case["reduced_limit"] if recommendation == "reduce_limit" else case["current_limit"]
    incorrect = recommendation != expected
    can_approve = authority in ("approve", "execute")
    can_execute = authority == "execute"
    rejected = can_execute and verify and incorrect
    executed = can_execute and not rejected
    final_limit = proposed_limit if executed else case["current_limit"]
    approved = {"decision": recommendation, "proposed_limit": proposed_limit}
    stages = [
        {
            "stage": "monitor", "status": "accepted",
            "input": {"observed_signal": observed},
            "output": {"risk_signal": observed},
        },
        {
            "stage": "analyze", "status": "accepted",
            "input": {"risk_signal": observed, "current_limit": case["current_limit"], "reduced_limit": case["reduced_limit"]},
            "output": {"recommendation": recommendation, "proposed_limit": proposed_limit},
        },
        {
            "stage": "approve", "status": "accepted" if can_approve else "blocked_by_authority",
            "input": {"recommendation": recommendation, "proposed_limit": proposed_limit},
            "output": {"approved_decision": recommendation, "approved_limit": proposed_limit} if can_approve else {},
        },
        {
            "stage": "execute",
            "status": "executed" if executed else "blocked_by_verification" if rejected else "blocked_by_authority" if can_approve else "not_reached",
            "input": approved if can_approve else {},
            "output": {"operation": recommendation, "final_limit": final_limit} if executed else {},
        },
    ]
    verification_trace = {
        "enabled": verify,
        "kind": "ideal_independent_truth_verifier",
        "status": "rejected" if rejected else "allowed" if can_execute and verify else "disabled" if not verify else "not_reached",
        "input": {"approved_decision": recommendation, "independent_true_risk": case["true_risk"]} if can_execute and verify else {},
        "output": {"allow": not incorrect, "expected_decision": expected} if can_execute and verify else {},
    }
    return {
        "schema_version": 1,
        "experiment_id": config["experiment_id"],
        "backend": BACKEND,
        "trial_id": f"{case['case_id']}--{authority}--v{int(verify)}--{fault}",
        "case_id": case["case_id"],
        "seed": config["seed"],
        "condition": dict(condition),
        "case": {key: case[key] for key in ("current_limit", "reduced_limit")},
        "fault_injection": {"kind": fault, "target": "monitor.input.observed_signal"},
        "evaluator": {
            "true_risk": case["true_risk"], "risk_score": case["risk_score"],
            "expected_decision": expected,
            "expected_final_limit": case["reduced_limit"] if expected == "reduce_limit" else case["current_limit"],
        },
        "stages": stages,
        "verification_trace": verification_trace,
        "incorrect_recommendation": incorrect,
        "incorrect_approval": incorrect if can_approve else None,
        "executed": executed,
        "erroneous_execution": executed and incorrect,
        "harmful_state_change": executed and incorrect and final_limit != case["current_limit"],
        "task_completion": executed if can_execute else None,
        "task_success": executed and not incorrect if can_execute else None,
        "propagation_depth": (4 if executed else 3 if can_approve else 2) if fault == "flip" else 0,
        "error_authority_reached": ("execute" if executed else "approve" if can_approve else "recommend") if incorrect else "none",
        "containment_point": "not_applicable" if fault == "clean" else "verification" if rejected else "authority_cap" if not can_execute else "none",
        "final_limit": final_limit,
    }


def summarize(trials: list[dict]) -> list[dict]:
    """Rates with no eligible denominator are None (empty fields in CSV)."""
    groups: dict[tuple, list[dict]] = {}
    for trial in trials:
        condition = trial["condition"]
        key = tuple(condition[name] for name in ("authority", "verification", "fault"))
        groups.setdefault(key, []).append(trial)
    rows = []
    for (authority, verification, fault), group in groups.items():
        n = len(group)
        approvals = sum(item["incorrect_approval"] is not None for item in group)
        executions = sum(item["executed"] for item in group)
        eligible = sum(item["task_completion"] is not None for item in group)
        count = lambda key: sum(item[key] is True for item in group)
        rate = lambda numerator, denominator: numerator / denominator if denominator else None
        recommendations_wrong = count("incorrect_recommendation")
        approvals_wrong = count("incorrect_approval")
        executions_wrong = count("erroneous_execution")
        harmful_changes = count("harmful_state_change")
        completions, successes = count("task_completion"), count("task_success")
        rows.append({
            "authority": authority, "verification": verification, "fault": fault,
            "n_trials": n, "n_recommendations": n,
            "n_incorrect_recommendations": recommendations_wrong,
            "incorrect_recommendation_rate": rate(recommendations_wrong, n),
            "n_approvals": approvals, "n_incorrect_approvals": approvals_wrong,
            "incorrect_approval_rate": rate(approvals_wrong, approvals),
            "n_executions": executions, "execution_rate_all_trials": rate(executions, n),
            "n_erroneous_executions": executions_wrong,
            "erroneous_execution_rate_all_trials": rate(executions_wrong, n),
            "erroneous_execution_rate_among_executed": rate(executions_wrong, executions),
            "n_harmful_state_changes": harmful_changes,
            "harmful_state_change_rate_all_trials": rate(harmful_changes, n),
            "harmful_state_change_rate_among_executed": rate(harmful_changes, executions),
            "n_task_eligible": eligible, "n_task_completions": completions, "n_task_successes": successes,
            "task_completion_rate": rate(completions, eligible), "task_success_rate": rate(successes, eligible),
            "mean_propagation_depth": sum(item["propagation_depth"] for item in group) / n,
            "n_stopped_by_verification": sum(item["containment_point"] == "verification" for item in group),
            "n_stopped_by_authority_cap": sum(item["containment_point"] == "authority_cap" for item in group),
        })
    return rows


def source_provenance() -> dict:
    """Hash package source even in a new repository without a first commit."""
    package = Path(__file__).resolve().parent
    digest = hashlib.sha256()
    files = []
    for path in sorted(package.rglob("*.py")):
        relative = path.relative_to(package.parent).as_posix()
        digest.update(relative.encode() + b"\0" + path.read_bytes() + b"\0")
        files.append(relative)
    return {"sha256": digest.hexdigest(), "files": files, "algorithm": "sha256(path + NUL + bytes + NUL), sorted paths relative to src"}


def git_provenance() -> dict:
    """Capture tracked and untracked state without changing the repository."""
    def git(*arguments: str) -> str | None:
        try:
            result = subprocess.run(
                ["git", *arguments], cwd=Path(__file__).resolve().parent,
                capture_output=True, text=True, check=False,
            )
            return result.stdout.rstrip("\n") if result.returncode == 0 else None
        except OSError:
            return None

    status = git("status", "--porcelain=v1", "--untracked-files=all")
    entries = status.splitlines() if status else []
    return {
        "commit": git("rev-parse", "HEAD"),
        "dirty": bool(entries) if status is not None else None,
        "tracked_dirty": any(not entry.startswith("?? ") for entry in entries) if status is not None else None,
        "untracked_files": [entry[3:] for entry in entries if entry.startswith("?? ")],
        "status_porcelain": entries,
        "available": status is not None,
    }


def run_experiment(config_path: str | Path, output_dir: str | Path) -> Path:
    """Write a complete paired run into a new directory; never overwrite a run."""
    config_bytes = Path(config_path).read_bytes()
    config = validate_config(tomllib.loads(config_bytes.decode("utf-8")))
    output = Path(output_dir)
    if output.exists():
        raise FileExistsError(f"Output already exists: {output}. Choose a new directory.")
    provenance = {"git": git_provenance(), "source": source_provenance()}
    cases = generate_cases(config)
    trials = [
        run_trial(case, {"authority": authority, "verification": verification, "fault": fault}, config)
        for authority, verification, fault in itertools.product(config["authority_levels"], config["verification"], config["faults"])
        for case in cases
    ]
    rows = summarize(trials)
    output.mkdir(parents=True, exist_ok=False)
    (output / "config.toml").write_bytes(config_bytes)
    with (output / "trials.jsonl").open("w", encoding="utf-8") as stream:
        for trial in trials:
            stream.write(json.dumps(trial, sort_keys=True, allow_nan=False) + "\n")
    with (output / "summary.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    manifest = {
        "schema_version": 1, "experiment_id": config["experiment_id"],
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "backend": BACKEND, "python_version": platform.python_version(),
        "python_implementation": platform.python_implementation(),
        "seed": config["seed"], "cases": len(cases), "conditions": len(rows), "trial_count": len(trials),
        "config_sha256": hashlib.sha256(config_bytes).hexdigest(),
        "verifier": "ideal_independent_truth_verifier_at_execution_boundary",
        "claim_scope": "Deterministic synthetic mechanism check; no LLM/model/API runs or empirical model-effect estimates.",
        **provenance,
        "artifacts": {
            name: {"sha256": hashlib.sha256((output / name).read_bytes()).hexdigest()}
            for name in ("config.toml", "trials.jsonl", "summary.csv")
        },
    }
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return output
