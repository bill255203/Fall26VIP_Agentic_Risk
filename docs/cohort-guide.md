# Cohort Guide

New students can start with the [quick start](student-start.md). The [semester plan](semester-plan.md) defines milestone targets and dependencies; [Contributors](../CONTRIBUTORS.md) links each student's visible work. This guide explains how the cohort chooses a study and works together.

## Select one study, then share it

The existing scripted pilot is a deterministic, runnable starter for setup, traces, and mechanism checks. It is not the selected empirical study. [Candidate A](studies/01-runtime-containment.md) is one unselected proposal built from that starting point; the selected study may instead address attribution, replication, another containment question, or a different feasible agentic-risk question.

Use the [selection and protocol guide](studies/README.md#selection-and-protocol) to keep the choice bounded. By **September 18**, finish onboarding and begin sourced critique, reproduction, and feasibility checks for at most two cohort-level proposals. Continue those checks through the selection review, select one question, and freeze its reviewed protocol by **September 25**. Record the reason for the choice and any reasoned rejection; a rejected proposal needs no replacement busywork.

The shared delivery targets remain: the smallest validated chosen study by **October 2**, evidence and analysis by **October 16**, a complete report draft by **October 23**, and reviewed handoff by **November 6**. These are working project targets from the semester plan.

## Two teams, one selected study

After selection, the Research and Data Science/Engineering teams share one research question, protocol, evidence base, and final report. They have different responsibilities, but they are not separate projects.

| Research | Data Science / Engineering | Shared |
| --- | --- | --- |
| literature review; question and outcomes; analysis plan; interpretation; limitations; writing | data/trace pipeline; tooling; validation; provenance; agents and controls where needed | study design; labels and evidence review; result analysis; reproducibility; final claims |

Every research requirement must be implementable, and every implementation choice that affects a claim must be reviewed as part of the methodology.

## Lightweight GitHub workflow

Use Issues as the work queue and pull requests as the reviewable record.

1. Create one focused Issue with a problem, owner, acceptance criteria, and relevant experiment or document.
2. Make a small branch and commit changes that address that Issue.
3. Open a pull request that links the Issue and states what changed, why it matters, and how it was checked.
4. Request review from the other team when a change affects hypotheses, data, traces, outcomes, controls, or interpretation.
5. Merge after the acceptance criteria and checks pass. Record follow-up work as new Issues instead of hiding it in comments.

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
