# Agentic AI for Risk Management

## Risk Propagation and Assurance in Multi-Agent Systems

This is the **canonical repository for the Fall 2026 VIP: Agentic AI for Risk Management**. The accepted semester plan, work queue, research decisions, code, experiments, reports, and student contribution records live here. `main` contains the reviewed project record; branches and forks are work in progress.

## Start here

**New student?** Follow the [student quick start](docs/student-start.md): clone the repo, run the pilot, and add your name through a first pull request. No advance registration of your GitHub username or repository invitation is needed for that path.

| Need | Authoritative location |
|---|---|
| Semester scope, deliverables, and dependencies | [Fall 2026 plan](docs/semester-plan.md) |
| Current work and completion status | [Issues](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues) and [milestones](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/milestones) |
| Student roster and individual work | [Contributors](CONTRIBUTORS.md) and [portfolio guide](docs/contributors/README.md) |
| First contribution and review process | [Contributing](CONTRIBUTING.md) |
| Research methods and claim limits | [Research plan](docs/research-plan.md) |
| First empirical question, conditions, and measures | [Study 1: runtime containment](docs/studies/01-runtime-containment.md) |
| Ideas borrowed from Agent Assurance | [Source-to-experiment map](docs/agent-assurance-bridge.md) |
| Accepted decisions and meeting actions | [Decision log](docs/decisions.md) and [meeting records](docs/meetings/README.md) |
| Semester outputs and continuity | [Reports and handoff](docs/reports/README.md) |

The starter apparatus is available; cohort deliverables are complete only when the linked evidence has been reviewed. The [semester plan](docs/semester-plan.md#calendar-and-working-targets) has working milestone dates aligned with NYU Tandon's Fall 2026 calendar. Students add themselves to the roster, and task ownership is agreed in Issues. Course policies and grades remain with the course's official systems.

Chat, slides, notebooks, and external storage may support the work. Link their durable outputs from a reviewed issue or document here. Resolve changes to scope through a plan pull request and the decision log so there is one current plan.

## Research question

The program asks:

> How do failures propagate through agentic AI systems, when do they become consequential because of delegated authority, and which assurance controls reduce or contain that transition?

The first cohort starts with one small, synthetic financial-control workflow. The initial empirical question is whether a gate that checks independent evidence reduces incorrect actions under a corrupted upstream summary, while preserving useful task completion. All actions are simulated.

The current code is a deterministic apparatus for checking traces, permissions, and measurements. [Study 1](docs/studies/01-runtime-containment.md) describes the next step: one real model backend, paired clean/corrupted cases, and a practical gate on/off. That empirical study is proposed and still needs implementation and a frozen protocol; the starter's output is not a model finding.

## Research structure

```text
Question → testable hypothesis → controlled experiment → evidence → revised claim

Sources: academic literature + selected Agent Assurance assumptions
First study: corrupted summary → agent decisions → execution boundary
Comparison: practical evidence gate off/on, with clean-input utility checks
```

[Agent Assurance](docs/agent-assurance-bridge.md) is one source of hypotheses and evidence practices. Students may support, qualify, or challenge its assumptions. The VIP's success is a defensible result and reproducible evidence, including a negative result.

Every study follows the same cycle:

**Define → Baseline → Perturb → Observe → Control → Compare → Generalize**

The **currently runnable scripted pilot** varies three factors:

| Factor | Conditions |
|---|---|
| Input | clean, flipped signal |
| Authority cap | recommend, approve, execute |
| Verification | off, on |

The deterministic backend validates the experiment machinery and trace format. Its output is fixture evidence, not an empirical result about LLM agents. The authority caps also validate permission enforcement; because lower-cap conditions cannot execute by construction, their execution rates cannot establish a causal effect of authority. See [the research plan](docs/research-plan.md) for the empirical study that should follow.

## Run the pilot

Python 3.11 or later is required. The initial harness has no runtime dependencies.

```bash
git clone https://github.com/zhongnz/Fall26VIP_Agentic_Risk.git
cd Fall26VIP_Agentic_Risk
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python -m agentic_risk \
  --config experiments/pilot.toml \
  --output results/local/pilot
```

If you already cloned the repository, start with the virtual-environment command. On Windows, use `py -3 -m venv .venv` and activate with `.venv\Scripts\Activate.ps1` in PowerShell. To run directly from a checkout without installation on macOS/Linux, prefix the run and test commands with `PYTHONPATH=src`.

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

The [semester task queue](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues) follows five front-loaded milestones: onboarding by **September 18**, protocol by **September 25**, validated empirical workflow and practical gate by **October 2**, first complete dataset/analysis by **October 16**, and report/handoff by **November 6**, with a full draft by **October 23**. These are working project targets; the rest of the term provides review, presentation, and recovery time.

## Current scope

The first research package is deliberately narrow: one workflow, one known information fault, one model backend, one practical containment gate, and auditable safety/utility measurements. The ideal oracle and authority caps remain apparatus checks. Memory poisoning, full toxic-flow/exfiltration experiments, authentication-strength comparisons, and trace-attribution studies are later candidates selected from evidence.

The repository contains no production financial integration and should not contain personal, confidential, regulated, or proprietary data.
