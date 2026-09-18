# Semester report and handoff

Maintain one evolving report at `fall-2026.md`. Start its selection record,
source map, provisional method notes, and contribution section during M1. Add
the selected question and frozen protocol after the M2 decision, then
add actual evidence as it arrives. The [semester schedule](../semester-plan.md#calendar-and-working-targets)
sets the draft and M5 handoff checkpoints from the first cohort meeting. The outline
is shared cohort work started after kickoff; nothing is due before students meet.
Link supporting analyses and figures. This directory currently defines the
report structure and does not contain study findings.

The question remains open until the cohort completes the
[selection and protocol process](../studies/README.md#selection-and-protocol).
The deterministic starter is runnable infrastructure, while
[Candidate A](../studies/01-runtime-containment.md) is an unselected proposal.
Use candidate-specific concepts only if the selected question and evidence make
them applicable.

## Presentations and individual reports

The cohort prepares **one research-question presentation for October 9 (M2)**,
before selection/protocol freeze, and **one final presentation for November 20 (M5)**.
These are working targets; the instructor confirms actual slots and submission details.
Save reviewed slides or an accessible export/link here. Coordinate the question
presentation in [#21](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/21) and the final presentation in [#22](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/22); cross-link
their reviewed outputs from #3 and #9, respectively. Record each student's preparation/presentation role and supporting work.
The [tentative grading scheme](../grading-proposal.md#two-group-presentations-and-the-written-report)
explains the content and criteria.

Each student also writes an [individual contribution report](../contributors/_individual-report-template.md)
in `docs/contributors/YOUR-USERNAME.md`, linking existing tasks and PRs: draft November 6, final November 20. Link it from their
own Individual report task under [#23](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/23). The shared technical report, two shared presentations,
and each student's report are distinct outputs. Reuse evidence links instead of
copying logs; slides do not replace the written reports.

## Shared technical report outline

Use the following outline. Fill sections with observed evidence; mark anything
pending explicitly instead of supplying illustrative results as findings.

```markdown
# Fall 2026 Agentic Risk VIP report

## Summary
Question, study status, and conclusions supported by the evidence.

## Research question and related work
Selected question, alternatives considered, selection rationale, primary
sources, hypotheses or analysis questions, contribution, and claim limits.
Include the evidence and feasibility check behind the choice and the group's
relationship to Agent Assurance where applicable.

## Method
Frozen protocol revision; study materials or data and their provenance;
systems and settings; variables, interventions, and comparators where
applicable; outcomes; units and denominators; exclusions,
analysis, and resource use.

## Validation
Feasibility checks, apparatus tests, reproduction checks, and smoke runs as
applicable, clearly distinguished from the evidence used for final claims.

## Results
Artifact and analysis links, counts and denominators, appropriate uncertainty,
comparisons appropriate to the selected design, failures, and null findings.

## Interpretation and limitations
Observed results versus interpretation; protocol deviations and the claims the
selected design supports. For each tested assumption or research objective:
evidence that supports, qualifies, or challenges it; alternative explanations;
limits on describing affiliated-cohort work as independent or external review.

## Contributions
Student names/handles, contribution roles, and links to attributable evidence.
Include only actual contributors and reviewed evidence. Credit sourced
exploration, critique, reproduction attempts, and reasoned proposal rejections
where they informed selection or the selected study. Review contributions with
the participants before finalizing credit.

## Reproduction and handoff
Applicable setup, retrieval, or run instructions; code, protocol, data, and
configuration revisions; artifact locations and provenance; analysis or
source-to-claim verification; known issues; prioritized next work and ownership
or explicit unassigned status.

## References
Primary-source citations and links to repository evidence.
```

Before M5 closes, a contributor other than the original author or implementer
reproduces the empirical analysis from the handoff and links their result.
Record any access requirements for empirical reruns, while
keeping reviewed artifacts available for analysis without making new paid
calls. Keep large artifacts according to
[the results policy](../../results/README.md).

Report credit follows [the cohort guide](../cohort-guide.md) and
[CONTRIBUTING.md](../../CONTRIBUTING.md). Preserve student-authored contributions
and review evidence; authorship of a potential paper is a separate documented
discussion, not automatically assigned by enrollment or commit count.
