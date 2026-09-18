# Agentic AI for Risk Management

## Risk Propagation and Assurance in Multi-Agent Systems

This is the **canonical repository for the Fall 2026 VIP: Agentic AI for Risk Management**. The cohort will identify and investigate one bounded question about risk in agentic systems, producing reusable evidence and a technical report. The plan, work queue, decisions, code, and student contribution records live here.

## Start here

**First meeting: Friday, September 18, 2026. First student checkpoint: September 25.**
Kickoff covers the project, a starter demonstration, and setup help. No repository
submission is due at kickoff.

Start with the [student guide](docs/student-start.md): it explains **what to do at
each stage, where to submit work, and how to get help**. By September 25, open an
introduction PR, try the starter and record the result or setup error, and bring one
question and an agreed small next task. No advance username list or invitation is needed.

Then read the [short proposal outline](docs/studies/README.md#short-proposal-outline)
and choose an assigned source from the [literature and research resources](docs/literature.md).
Reading is divided across the cohort; detailed methods and candidate protocols are
references for your task. Use the [dated semester schedule](docs/semester-plan.md#calendar-and-working-targets)
and [student roadmap](docs/student-start.md#throughout-the-project) throughout the project.

## Resources and where work lives

| Need | Authoritative location |
|---|---|
| Semester scope, deliverables, and dependencies | [Fall 2026 plan](docs/semester-plan.md) |
| Current work and completion status | [Issues](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues) and [milestones](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/milestones) |
| Two students doing the same assignment; ownership and completion | [Group goals and individual tasks](docs/issue-workflow.md): one Group goal, a separate task per student |
| Student roster and individual work | [Contributors](CONTRIBUTORS.md) and [portfolio guide](docs/contributors/README.md) |
| First contribution and review process | [Contributing](CONTRIBUTING.md) |
| Papers, benchmarks, datasets, and evaluation tools | [Literature and resource guide](docs/literature.md), including propagation, containment, and failure attribution |
| Research methods and claim limits | [Research plan](docs/research-plan.md) |
| How students choose the research question | [Study selection guide](docs/studies/README.md) |
| A worked proposal to critique | [Candidate A: runtime containment](docs/studies/01-runtime-containment.md) |
| Ideas borrowed from Agent Assurance | [Source-to-experiment map](docs/agent-assurance-bridge.md) |
| Runnable starter, configuration, and checks | [Run commands](#run-the-pilot), [source code](src/agentic_risk/), [pilot configuration](experiments/pilot.toml), and [tests](tests/) |
| How to record experiments and store evidence | [Experiment record](docs/experiment-record.md) and [results policy](results/README.md) |
| Accepted decisions and meeting actions | [Decision log](docs/decisions.md) and [meeting records](docs/meetings/README.md) |
| Semester outputs and continuity | [Reports and handoff](docs/reports/README.md) |

`main` is the current project record; branches and forks contain work in progress. Students add themselves to the roster, and task ownership is agreed in Issues. Course policies and grades remain with the course's official systems.

Chat, slides, notebooks, and external storage may support the work. Link their durable outputs from a reviewed issue or document here. Resolve changes to scope through a plan pull request and the decision log so there is one current plan.

## What is ready, and what students decide

| Item | Current status |
| --- | --- |
| Scripted credit-limit pilot | Runnable now, with tests and traces; no real model calls. |
| Candidate A: runtime containment | Proposed research design; not selected, frozen, or implemented. |
| Semester study | Students compare bounded proposals and select one with the method lead at M2, after onboarding and feasibility work. |
| Empirical results and report | Still to be produced and reviewed; the starter's output is apparatus validation. |

After orientation, students share the work of running and criticizing the pilot,
reading primary research, attempting one bounded reproduction, and proposing a
feasible question. The
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
starts from **September 18**, with a full week for onboarding.
The [semester plan](docs/semester-plan.md#calendar-and-working-targets) is the single
schedule for selection, validation, evidence, draft, and handoff. Its dates are
working project targets; course policies and any formal submission times come from the instructor.

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
