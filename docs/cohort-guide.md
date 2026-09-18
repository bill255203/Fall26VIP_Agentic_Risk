# Cohort Guide

New students can start with the [quick start](student-start.md). The [semester plan](semester-plan.md) defines milestone targets and dependencies; [Contributors](../CONTRIBUTORS.md) links each student's visible work. This guide explains how the cohort chooses a study and works together.

## Select one study, then share it

The existing scripted pilot is a deterministic, runnable starter for setup, traces, and mechanism checks. It is not the selected empirical study. [Candidate A](studies/01-runtime-containment.md) is one unselected proposal built from that starting point; the selected study may instead address attribution, replication, another containment question, or a different feasible agentic-risk question.

The September 18 first meeting introduces the project and starter; no repository submission is
required beforehand. Students have until September 25 to introduce themselves,
try the starter, and raise setup questions. Divide focused reading, reproduction,
and feasibility checks across the cohort rather than assigning all of them to each student.

Use the [selection guide](studies/README.md#selection-and-protocol) to compare at
most two developed proposals and freeze one reviewed protocol at M2. Record the
selection rationale and reasoned rejections. The [semester schedule](semester-plan.md#calendar-and-working-targets)
sets dated targets from the confirmed September 18 kickoff. The [student roadmap](student-start.md#throughout-the-project)
shows what each student contributes, the shared outputs, and where to submit them;
its [resource directory](student-start.md#resources-what-to-read-and-where-to-save-work)
links the relevant guides, code, papers, and templates.

## Two teams, one selected study

After selection, the Research and Data Science/Engineering teams share one research question, protocol, evidence base, and final report. They have different responsibilities, but they are not separate projects.

| Research | Data Science / Engineering | Shared |
| --- | --- | --- |
| literature review; question and outcomes; analysis plan; interpretation; limitations; writing | data/trace pipeline; tooling; validation; provenance; agents and controls where needed | study design; labels and evidence review; result analysis; reproducibility; final claims |

Every research requirement must be implementable, and every implementation choice that affects a claim must be reviewed as part of the methodology.

## Lightweight GitHub workflow

Use [Group goals and Individual tasks](issue-workflow.md) as the work queue and
pull requests as the reviewable record. Two students can do the same assignment
independently using separate tasks under one goal, with separate evidence and reviews.

Introduction PRs use the shared onboarding issue #5 and the [quick start](student-start.md).
The workflow below applies to subsequent research, engineering, and writing tasks.

1. Create an Individual task under an existing Group goal, with one student owner, work mode, deliverable, acceptance criteria, and reviewer. For joint work, each student's task describes their own part and can link the same shared artifact.
2. Make a small branch and commit changes that address that Issue.
3. Open a pull request that links the Issue and states what changed, why it matters, and how it was checked.
4. Request review from the other team when a change affects hypotheses, data, traces, outcomes, controls, or interpretation.
5. Merge after the acceptance criteria and checks pass; close the completed Individual task. A maintainer closes the Group goal after its required contributions and combined output are reviewed. Record follow-up work as new tasks instead of hiding it in comments.

Issues and pull requests are sufficient to start. If a Project board is enabled, use `To Do → In Progress → Review → Done`. Useful labels include `research`, `engineering`, `experiment`, and `bug`.

## Durable assets

Prefer work that leaves one or more assets the next cohort can use:

- **Evidence:** versioned run-level results, uncertainty, and negative findings;
- **Code:** a reproducible workflow, tests, run commands, and analysis;
- **Data and traces:** documented schemas, provenance, ground truth, and permitted reuse;
- **Research synthesis:** sourced explorations, critiques, bounded reproduction attempts, reasoned proposal decisions, limitations, and manuscript-ready prose.

Presentations and notebooks are useful when they point to a durable source. They should not be the only surviving record.

## Definition of done

A task is done when another contributor can review and reuse its result.

For code or experiment work, that means:

- acceptance criteria pass;
- relevant tests or validation runs pass;
- the run command and configuration are recorded;
- outputs include source/unit IDs, reference labels and comparison values where applicable, statuses, and errors;
- generated artifacts and schemas are documented;
- assumptions and known limitations are explicit;
- the pull request has been reviewed.

For research or writing work, that means:

- claims are traceable to primary sources or repository evidence;
- questions, outcomes, and denominators are precise;
- observations are separated from interpretation;
- contradictory and null results are retained;
- methodological implications are reflected in the experiment or opened as Issues;
- the pull request has been reviewed.

## Handoff

The cohort should leave a working starting point rather than a final presentation alone. Before handoff, provide:

- tested setup and commands for the smallest selected experiment or analysis;
- exact study records, data/configuration/code revisions, and prompts/scenarios where applicable;
- source data/traces or documented access, unit-level outcomes, summaries, and a data dictionary;
- a report of findings, null results, exclusions, and claim limits;
- unresolved bugs and failed approaches with enough detail to avoid repetition;
- prioritized next questions and the evidence needed to answer each one;
- an updated literature map and contribution record.

A new contributor should be able to reproduce the pilot and identify the next research decision without relying on private messages or oral history.

## Credit and authorship

Discuss authorship expectations near the start of the work and revisit them as contributions change. Track contributions in pull requests and a shared record using the [CRediT contributor roles](https://credit.niso.org/), such as conceptualization, methodology, software, investigation, data curation, formal analysis, visualization, and writing. Sourced question exploration, substantive critique, reproduction attempts, and evidence-backed recommendations to reject a proposal can all be substantive contributions.

Authorship decisions should reflect substantive contributions to the resulting work; enrollment, job title, or a single isolated task does not by itself determine authorship. Record contributions throughout the project so the discussion is transparent and based on evidence rather than memory. Credit the useful outcome already produced; do not create extra work for rejected ideas or rank students by activity counts.
