# Agentic AI for Risk Management

## Risk Propagation and Assurance in Multi-Agent Systems

This is the **canonical repository for the Fall 2026 VIP: Agentic AI for Risk Management**. The cohort will identify and investigate one bounded question about risk in agentic systems, producing reusable evidence and a technical report. The plan, work queue, decisions, code, and student contribution records live here.

## Start here

**New student?** Follow the [student quick start](docs/student-start.md): clone the repo, run the pilot, and add your name through a first pull request. No advance registration of your GitHub username or repository invitation is needed for that path.

Then read the [selection guide](docs/studies/README.md) and choose a small current
task. Use the detailed methods and candidate documents as references for that work.

| Need | Authoritative location |
|---|---|
| Semester scope, deliverables, and dependencies | [Fall 2026 plan](docs/semester-plan.md) |
| Current work and completion status | [Issues](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues) and [milestones](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/milestones) |
| Student roster and individual work | [Contributors](CONTRIBUTORS.md) and [portfolio guide](docs/contributors/README.md) |
| First contribution and review process | [Contributing](CONTRIBUTING.md) |
| Research methods and claim limits | [Research plan](docs/research-plan.md) |
| How students choose the research question | [Study selection guide](docs/studies/README.md) |
| A worked proposal to critique | [Candidate A: runtime containment](docs/studies/01-runtime-containment.md) |
| Ideas borrowed from Agent Assurance | [Source-to-experiment map](docs/agent-assurance-bridge.md) |
| Accepted decisions and meeting actions | [Decision log](docs/decisions.md) and [meeting records](docs/meetings/README.md) |
| Semester outputs and continuity | [Reports and handoff](docs/reports/README.md) |

`main` is the current project record; branches and forks contain work in progress. Students add themselves to the roster, and task ownership is agreed in Issues. Course policies and grades remain with the course's official systems.

Chat, slides, notebooks, and external storage may support the work. Link their durable outputs from a reviewed issue or document here. Resolve changes to scope through a plan pull request and the decision log so there is one current plan.

## What is ready, and what students decide

| Item | Current status |
| --- | --- |
| Scripted credit-limit pilot | Runnable now, with tests and traces; no real model calls. |
| Candidate A: runtime containment | Proposed research design; not selected, frozen, or implemented. |
| Semester study | Students compare bounded proposals and select one with the method lead by September 25. |
| Empirical results and report | Still to be produced and reviewed; the starter's output is apparatus validation. |

Students begin by running and criticizing the pilot, reading primary research,
attempting one bounded reproduction, and proposing a feasible question. The
[selection guide](docs/studies/README.md) explains how this becomes one shared study.

## Research question

The program asks:

> How do risks arise and propagate in agentic systems, when do they become consequential, and how can they be understood or controlled?

The starter uses a synthetic financial-control workflow to make decisions and
consequences inspectable. Candidate A asks whether an evidence-checking gate reduces
incorrect actions while preserving correct task completion. The cohort may select
that study or one better-supported feasible alternative, including a controlled
replication or analysis of existing agent traces. The credit setting, gate, and
particular frameworks are choices to justify during selection.

## Research structure

```text
Explore and reproduce → select one question → freeze a protocol
                    → validate → collect/analyze evidence → report and hand off
```

[Agent Assurance](docs/agent-assurance-bridge.md) is one source of hypotheses and evidence practices. Students may support, qualify, or challenge its assumptions. The VIP's success is a defensible result and reproducible evidence, including a negative result.

The **currently runnable scripted pilot** varies three factors:

| Factor | Conditions |
|---|---|
| Input | clean, flipped signal |
| Authority cap | recommend, approve, execute |
| Verification | off, on |

The deterministic backend validates the experiment machinery and trace format.
Because lower authority caps cannot execute by construction, their execution rates
cannot establish a causal effect of authority on agent behavior. Its verifier reads
the expected answer, so it checks the control pathway rather than demonstrating
practical detection. These limitations are useful starting points for student critique.
See the [research plan](docs/research-plan.md) for methods and outcome definitions.

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

The Research and Data Science / Engineering subteams work on the same selected
study. Research owns questions, design, analysis, interpretation, and writing.
Engineering owns the data/trace pipeline, tooling, and reproducibility, plus agents
and controls where needed. Each issue should leave reusable evidence, code, data,
literature synthesis, or a documented research decision.

Start with the [cohort guide](docs/cohort-guide.md), record experiments using [the experiment record](docs/experiment-record.md), and review the current [literature map](docs/literature.md). Contributions follow [CONTRIBUTING.md](CONTRIBUTING.md).

The [semester task queue](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues)
targets onboarding and starter critique by **September 18**, selection and protocol
by **September 25**, the smallest validated selected study by **October 2**, dataset
and analysis by **October 16**, a full draft by **October 23**, and report/handoff by
**November 6**. These are working project targets in the [semester plan](docs/semester-plan.md#calendar-and-working-targets).
The rest of term provides review, presentation, and recovery time.

## Current scope

Keep one question, a meaningful comparison, measurable outcomes, and a feasible
evidence plan. Choose tools after choosing the question. Agent Assurance and the
external work in the literature guide supply ideas and reusable assets; they do
not prescribe the study. More models, controls, or frameworks require a clear
scientific purpose and an agreed scope change after selection.

Literature synthesis, pilot criticism, reproduction attempts, and well-supported
rejected proposals are visible contributions alongside code and results. Link them
from [student portfolios](docs/contributors/README.md), with each person's role.

The repository contains no production financial integration and should not contain personal, confidential, regulated, or proprietary data.
