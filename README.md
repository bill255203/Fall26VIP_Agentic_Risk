# Agentic AI for Risk Management

## Risk Propagation and Assurance in Multi-Agent Systems

This repository is the shared research workspace for a Vertically Integrated Project (VIP) on Agent Assurance. The program asks:

> How do failures propagate through agentic AI systems, when do they become consequential because of delegated authority, and which assurance controls prevent that transition?

The first cohort starts with one small, synthetic financial-control workflow. The software is an experimental apparatus: it creates known ground truth, injects a controlled information error, records what happens at each stage, and compares outcomes with and without a control. All actions are simulated.

## Research structure

```text
Agent Assurance
    └── risk propagation research question
        └── VIP as the experimental vehicle
            └── synthetic financial workflow as the first environment

signal (clean/flipped) → monitor → analyze/recommend → approve
                                                        ↓
                                             optional ideal verifier
                                                        ↓
                                              simulated execution
```

Every study follows the same cycle:

**Define → Baseline → Perturb → Observe → Control → Compare → Generalize**

The founding pilot varies three factors:

| Factor | Conditions |
|---|---|
| Input | clean, flipped signal |
| Authority cap | recommend, approve, execute |
| Verification | off, on |

The deterministic backend validates the experiment machinery and trace format. Its output is fixture evidence, not an empirical result about LLM agents. The authority caps also validate permission enforcement; because lower-cap conditions cannot execute by construction, their execution rates cannot establish a causal effect of authority. See [the research plan](docs/research-plan.md) for the empirical study that should follow.

## Run the pilot

Python 3.11 or later is required. The initial harness has no runtime dependencies.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python -m agentic_risk \
  --config experiments/pilot.toml \
  --output results/local/pilot
```

On Windows, activate with `.venv\Scripts\Activate.ps1` in PowerShell. To run directly from a checkout without installation on macOS/Linux, prefix the run and test commands with `PYTHONPATH=src`.

The output directory must be new. Each run creates:

- `trials.jsonl`: one complete, structured trace per trial;
- `summary.csv`: condition-level counts, denominators, and rates;
- `manifest.json`: configuration, source, environment, and artifact provenance;
- `config.toml`: the exact configuration used for the run.

Local artifacts are ignored by Git. Promote only reviewed, documented result snapshots into version control.

Run the checks with:

```bash
python -m unittest discover -s tests -v
```

## Repository map

```text
src/agentic_risk/     experiment engine and command-line entry point
experiments/          versioned experiment configurations
tests/                behavior and reproducibility checks
results/              policy for reviewed result snapshots
docs/                 research plan, cohort guide, records, and literature
.github/               issue, pull-request, and CI workflow templates
```

## Working as one cohort

The Research and Data Science / Engineering subteams work on the same experiment. Research owns questions, hypotheses, experimental design, analysis, and writing. Engineering owns the environment, agents, fault injection, controls, instrumentation, and reproducibility. Each issue should produce a durable academic asset: evidence, code, trace data, or literature synthesis.

Start with the [cohort guide](docs/cohort-guide.md), record experiments using [the experiment record](docs/experiment-record.md), and review the current [literature map](docs/literature.md). Contributions follow [CONTRIBUTING.md](CONTRIBUTING.md).

The [initial task queue](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues) starts with reproducing the pilot, mapping related work, specifying the empirical study, and evaluating verification using independent evidence.

## Current scope

The first research package is deliberately narrow: one workflow, one known information fault, authority boundary enforcement, one ideal control, and auditable measurements. Future work can replace scripted stages with recorded model calls, test realistic verifiers, add other fault mechanisms, and evaluate whether findings transfer across models, architectures, and domains.

The repository contains no production financial integration and should not contain personal, confidential, regulated, or proprietary data.
