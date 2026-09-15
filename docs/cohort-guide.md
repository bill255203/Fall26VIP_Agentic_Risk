# Cohort Guide

## One experiment, two teams

The Research and Data Science/Engineering teams share one research question, condition matrix, dataset, and final report. They have different responsibilities, but they are not separate projects.

| Research | Data Science / Engineering | Shared |
| --- | --- | --- |
| literature review; hypotheses; outcome definitions; analysis plan; interpretation; limitations; writing | experimental workflow; agents; fixtures; perturbations; controls; instrumentation; run tooling; tests | experiment design; trace schema; scenario review; result analysis; reproducibility; final claims |

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
- **Research synthesis:** literature notes, decisions, limitations, and manuscript-ready prose.

Presentations and notebooks are useful when they point to a durable source. They should not be the only surviving record.

## Definition of done

A task is done when another contributor can review and reuse its result.

For code or experiment work, that means:

- acceptance criteria pass;
- relevant tests or validation runs pass;
- the run command and configuration are recorded;
- outputs include IDs, ground truth, treatment values, statuses, and errors;
- generated artifacts and schemas are documented;
- assumptions and known limitations are explicit;
- the pull request has been reviewed.

For research or writing work, that means:

- claims are traceable to primary sources or repository evidence;
- hypotheses, outcomes, and denominators are precise;
- observations are separated from interpretation;
- contradictory and null results are retained;
- methodological implications are reflected in the experiment or opened as Issues;
- the pull request has been reviewed.

## Handoff

The cohort should leave a working starting point rather than a final presentation alone. Before handoff, provide:

- a tested setup and one-command path to the smallest working experiment;
- exact experiment records, configurations, prompts, scenario definitions, and code revision;
- raw traces, run-level outcomes, summaries, and a data dictionary;
- a report of findings, null results, exclusions, and claim limits;
- unresolved bugs and failed approaches with enough detail to avoid repetition;
- prioritized next questions and the evidence needed to answer each one;
- an updated literature map and contribution record.

A new contributor should be able to reproduce the pilot and identify the next research decision without relying on private messages or oral history.

## Credit and authorship

Discuss authorship expectations near the start of the work and revisit them as contributions change. Track contributions in pull requests and a shared record using the [CRediT contributor roles](https://credit.niso.org/), such as conceptualization, methodology, software, investigation, data curation, formal analysis, visualization, and writing.

Authorship decisions should reflect substantive contributions to the resulting work; enrollment, job title, or a single isolated task does not by itself determine authorship. Record contributions throughout the project so the discussion is transparent and based on evidence rather than memory.
