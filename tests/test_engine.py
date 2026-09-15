"""Behavioral checks for the synthetic experiment and its research artifacts."""

import copy
import csv
import hashlib
import itertools
import json
import tempfile
import tomllib
import unittest
from pathlib import Path
from unittest.mock import patch

from agentic_risk import engine


CONFIG_TEXT = """experiment_id = "test-credit-pilot"
seed = 123
cases = 4
authority_levels = ["recommend", "approve", "execute"]
verification = [false, true]
faults = ["clean", "flip"]

[scenario]
current_limit = 100
reduced_limit = 50
"""


class EngineTests(unittest.TestCase):
    def setUp(self):
        self.config = tomllib.loads(CONFIG_TEXT)

    def trial(self, risk, authority="execute", verification=False, fault="clean"):
        case = {
            "case_id": f"example-{risk}", "true_risk": risk,
            "risk_score": 0.2 if risk == "low" else 0.8,
            "current_limit": 100, "reduced_limit": 50,
        }
        condition = {"authority": authority, "verification": verification, "fault": fault}
        return engine.run_trial(case, condition, self.config)

    def test_authority_and_error_containment_across_all_conditions(self):
        # authority, verifier, fault, executes, accepted depth, error authority, containment
        expectations = [
            ("recommend", False, "clean", False, 0, "none", "not_applicable"),
            ("recommend", True, "clean", False, 0, "none", "not_applicable"),
            ("recommend", False, "flip", False, 2, "recommend", "authority_cap"),
            ("recommend", True, "flip", False, 2, "recommend", "authority_cap"),
            ("approve", False, "clean", False, 0, "none", "not_applicable"),
            ("approve", True, "clean", False, 0, "none", "not_applicable"),
            ("approve", False, "flip", False, 3, "approve", "authority_cap"),
            ("approve", True, "flip", False, 3, "approve", "authority_cap"),
            ("execute", False, "clean", True, 0, "none", "not_applicable"),
            ("execute", True, "clean", True, 0, "none", "not_applicable"),
            ("execute", False, "flip", True, 4, "execute", "none"),
            ("execute", True, "flip", False, 3, "approve", "verification"),
        ]
        for risk, row in itertools.product(("low", "high"), expectations):
            authority, verify, fault, executes, depth, reached, containment = row
            with self.subTest(risk=risk, authority=authority, verify=verify, fault=fault):
                trial = self.trial(risk, authority, verify, fault)
                self.assertEqual(
                    (trial["executed"], trial["propagation_depth"],
                     trial["error_authority_reached"], trial["containment_point"]),
                    (executes, depth, reached, containment),
                )
                self.assertIs(trial["incorrect_recommendation"], fault == "flip")
                self.assertIs(trial["incorrect_approval"], None if authority == "recommend" else fault == "flip")
                if authority != "execute":
                    self.assertEqual(trial["final_limit"], 100)
                    self.assertIsNone(trial["task_completion"])
                    self.assertIsNone(trial["task_success"])
                    self.assertFalse(trial["erroneous_execution"])
                    self.assertFalse(trial["harmful_state_change"])
                    self.assertEqual(trial["stages"][-1]["output"], {})

    def test_explicit_keep_and_reduce_operations_distinguish_omissions_from_changes(self):
        # risk, fault, operation, final limit, erroneous execution, harmful change
        cases = [
            ("low", "clean", "keep_limit", 100, False, False),
            ("high", "clean", "reduce_limit", 50, False, False),
            ("low", "flip", "reduce_limit", 50, True, True),
            ("high", "flip", "keep_limit", 100, True, False),
        ]
        for risk, fault, operation, limit, erroneous, harmful in cases:
            with self.subTest(risk=risk, fault=fault):
                trial = self.trial(risk, fault=fault)
                self.assertTrue(trial["executed"])
                self.assertTrue(trial["task_completion"])
                self.assertIs(trial["task_success"], not erroneous)
                self.assertEqual(trial["stages"][-1]["output"], {"operation": operation, "final_limit": limit})
                self.assertEqual(trial["final_limit"], limit)
                self.assertIs(trial["erroneous_execution"], erroneous)
                self.assertIs(trial["harmful_state_change"], harmful)

    def test_ideal_verifier_uses_independent_truth_at_execution_boundary(self):
        for risk, fault in itertools.product(("low", "high"), ("clean", "flip")):
            with self.subTest(risk=risk, fault=fault):
                trial = self.trial(risk, verification=True, fault=fault)
                verifier = trial["verification_trace"]
                self.assertEqual(verifier["input"]["independent_true_risk"], risk)
                self.assertEqual(verifier["status"], "allowed" if fault == "clean" else "rejected")
                self.assertIs(verifier["output"]["allow"], fault == "clean")
                self.assertEqual(trial["stages"][2]["status"], "accepted")
                self.assertIs(trial["task_completion"], fault == "clean")
                self.assertIs(trial["task_success"], fault == "clean")
                if fault == "flip":
                    self.assertEqual(trial["stages"][-1]["status"], "blocked_by_verification")
                    self.assertEqual(trial["stages"][-1]["output"], {})
                    self.assertEqual(trial["final_limit"], 100)
                    self.assertFalse(trial["erroneous_execution"])

    def test_ordinary_stage_views_do_not_receive_evaluator_truth(self):
        private_keys = {"true_risk", "independent_true_risk", "risk_score", "expected_decision", "expected_final_limit"}

        def check_view(value):
            if isinstance(value, dict):
                self.assertFalse(private_keys.intersection(value))
                for child in value.values():
                    check_view(child)
            elif isinstance(value, list):
                for child in value:
                    check_view(child)

        for risk, authority, verify, fault in itertools.product(
            ("low", "high"), engine.AUTHORITY_LEVELS, (False, True), engine.FAULTS
        ):
            trial = self.trial(risk, authority, verify, fault)
            self.assertEqual([stage["stage"] for stage in trial["stages"]], ["monitor", "analyze", "approve", "execute"])
            for stage in trial["stages"]:
                check_view(stage["input"])
                check_view(stage["output"])
            observed = trial["stages"][0]["input"]["observed_signal"]
            self.assertEqual(observed == risk, fault == "clean")
            if authority != "execute" or not verify:
                self.assertEqual(trial["verification_trace"]["input"], {})

    def test_summary_keeps_zero_rates_distinct_from_missing_denominators(self):
        trials = [
            self.trial(risk, authority, verify, fault)
            for authority, verify, fault, risk in itertools.product(
                engine.AUTHORITY_LEVELS, (False, True), engine.FAULTS, ("low", "high")
            )
        ]
        rows = engine.summarize(trials)
        self.assertEqual(len(rows), 12)
        for row in rows:
            with self.subTest(condition=(row["authority"], row["verification"], row["fault"])):
                self.assertEqual(row["n_trials"], 2)
                self.assertEqual(row["n_recommendations"], 2)
                if row["authority"] == "recommend":
                    self.assertEqual(row["n_approvals"], 0)
                    self.assertIsNone(row["incorrect_approval_rate"])
                if row["authority"] != "execute":
                    self.assertEqual(row["n_task_eligible"], 0)
                    self.assertIsNone(row["task_completion_rate"])
                    self.assertIsNone(row["task_success_rate"])
                if row["n_executions"] == 0:
                    self.assertEqual(row["execution_rate_all_trials"], 0)
                    self.assertEqual(row["erroneous_execution_rate_all_trials"], 0)
                    self.assertIsNone(row["erroneous_execution_rate_among_executed"])
                    self.assertIsNone(row["harmful_state_change_rate_among_executed"])
        unverified_flip = next(row for row in rows if row["authority"] == "execute" and not row["verification"] and row["fault"] == "flip")
        self.assertEqual(unverified_flip["n_executions"], 2)
        self.assertEqual(unverified_flip["n_erroneous_executions"], 2)
        self.assertEqual(unverified_flip["erroneous_execution_rate_all_trials"], 1)
        self.assertEqual(unverified_flip["erroneous_execution_rate_among_executed"], 1)
        self.assertEqual(unverified_flip["n_harmful_state_changes"], 1)
        self.assertEqual(unverified_flip["harmful_state_change_rate_among_executed"], 0.5)
        self.assertEqual(engine.summarize([]), [])

    def test_case_generation_is_seeded_and_contains_both_risk_classes(self):
        cases = engine.generate_cases(self.config)
        self.assertEqual(cases, engine.generate_cases(self.config))
        self.assertEqual({case["true_risk"] for case in cases}, {"low", "high"})
        self.assertEqual(len({case["case_id"] for case in cases}), self.config["cases"])
        for case in cases:
            self.assertEqual(case["risk_score"] < 0.5, case["true_risk"] == "low")
        changed_seed = {**self.config, "seed": self.config["seed"] + 1}
        self.assertNotEqual(
            [(case["true_risk"], case["risk_score"]) for case in cases],
            [(case["true_risk"], case["risk_score"]) for case in engine.generate_cases(changed_seed)],
        )

    def test_config_rejects_invalid_types_duplicates_unknowns_and_limits(self):
        invalid_updates = [
            {"seed": True}, {"seed": -1}, {"cases": True}, {"cases": 1}, {"cases": 2.5},
            {"experiment_id": " "}, {"authority_levels": ["execute", "execute"]},
            {"authority_levels": ["admin"]}, {"authority_levels": "execute"},
            {"verification": [0, 1]}, {"verification": [True, True]},
            {"faults": ["clean", "clean"]}, {"faults": ["unknown"]}, {"faults": []},
            {"scenario": {"current_limit": True, "reduced_limit": 50}},
            {"scenario": {"current_limit": 100, "reduced_limit": 0}},
            {"scenario": {"current_limit": 100, "reduced_limit": 100}},
            {"scenario": {"current_limit": 100}}, {"unknown": 1},
        ]
        for update in invalid_updates:
            with self.subTest(update=update):
                candidate = {**copy.deepcopy(self.config), **update}
                with self.assertRaises(ValueError):
                    engine.validate_config(candidate)
        missing_key = copy.deepcopy(self.config)
        del missing_key["seed"]
        with self.assertRaises(ValueError):
            engine.validate_config(missing_key)
        self.assertEqual(engine.validate_config(self.config), self.config)

    def test_outputs_are_paired_reproducible_and_hash_verified(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            config_path = root / "experiment.toml"
            config_path.write_text(CONFIG_TEXT, encoding="utf-8")
            self.assertEqual(engine.load_config(config_path), self.config)
            first = engine.run_experiment(config_path, root / "first")
            second = engine.run_experiment(config_path, root / "second")
            for name in ("config.toml", "trials.jsonl", "summary.csv"):
                self.assertEqual((first / name).read_bytes(), (second / name).read_bytes())
            self.assertEqual((first / "config.toml").read_bytes(), config_path.read_bytes())
            trials = [json.loads(line) for line in (first / "trials.jsonl").read_text().splitlines()]
            self.assertEqual(len(trials), 12 * self.config["cases"])
            self.assertEqual(len({trial["trial_id"] for trial in trials}), len(trials))
            groups = {}
            for trial in trials:
                key = tuple(trial["condition"][name] for name in ("authority", "verification", "fault"))
                groups.setdefault(key, []).append((trial["case_id"], trial["evaluator"], trial["case"]))
            self.assertEqual(set(groups), set(itertools.product(engine.AUTHORITY_LEVELS, (False, True), engine.FAULTS)))
            paired_cases = next(iter(groups.values()))
            self.assertEqual(len(paired_cases), self.config["cases"])
            for cases in groups.values():
                self.assertEqual(cases, paired_cases)
            manifests = [json.loads((path / "manifest.json").read_text()) for path in (first, second)]
            self.assertEqual(manifests[0]["artifacts"], manifests[1]["artifacts"])
            for path, manifest in zip((first, second), manifests):
                self.assertEqual(manifest["config_sha256"], hashlib.sha256(config_path.read_bytes()).hexdigest())
                self.assertEqual(manifest["backend"], "scripted-v1")
                self.assertEqual(manifest["trial_count"], len(trials))
                self.assertEqual(manifest["source"], engine.source_provenance())
                self.assertTrue({"commit", "dirty", "tracked_dirty", "untracked_files"} <= manifest["git"].keys())
                for name, metadata in manifest["artifacts"].items():
                    self.assertEqual(metadata["sha256"], hashlib.sha256((path / name).read_bytes()).hexdigest())
            with (first / "summary.csv").open(newline="", encoding="utf-8") as stream:
                rows = list(csv.DictReader(stream))
            self.assertEqual(len(rows), 12)
            for row in rows:
                if row["n_executions"] == "0":
                    self.assertEqual(row["erroneous_execution_rate_among_executed"], "")

    def test_source_fingerprint_changes_when_source_changes(self):
        with tempfile.TemporaryDirectory() as directory:
            package = Path(directory) / "agentic_risk"
            package.mkdir()
            module = package / "engine.py"
            module.write_text("value = 1\n", encoding="utf-8")
            (package / "__init__.py").write_text("", encoding="utf-8")
            with patch.object(engine, "__file__", str(module)):
                before = engine.source_provenance()
                self.assertEqual(before, engine.source_provenance())
                self.assertEqual(before["files"], ["agentic_risk/__init__.py", "agentic_risk/engine.py"])
                module.write_text("value = 2\n", encoding="utf-8")
                self.assertNotEqual(before["sha256"], engine.source_provenance()["sha256"])

    def test_overwrite_refusal_preserves_artifacts_and_invalid_config_creates_nothing(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            config_path = root / "experiment.toml"
            config_path.write_text(CONFIG_TEXT, encoding="utf-8")
            output = engine.run_experiment(config_path, root / "run")
            originals = {path.name: path.read_bytes() for path in output.iterdir()}
            with self.assertRaisesRegex(FileExistsError, "already exists"):
                engine.run_experiment(config_path, output)
            self.assertEqual(originals, {path.name: path.read_bytes() for path in output.iterdir()})
            config_path.write_text(CONFIG_TEXT.replace("cases = 4", "cases = true"), encoding="utf-8")
            invalid_output = root / "invalid-run"
            with self.assertRaises(ValueError):
                engine.run_experiment(config_path, invalid_output)
            self.assertFalse(invalid_output.exists())


if __name__ == "__main__":
    unittest.main()
