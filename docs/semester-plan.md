# Fall 2026 semester plan

This repository is the canonical workspace for the Fall 2026 Agentic Risk VIP.
The cohort shares one study, one task queue, and one final report. This document
defines delivery gates; the [research plan](research-plan.md) defines the
scientific question, apparatus, measures, and limits on claims.

## Semester outcome and scope

The core outcome is a reproducible study of one simulated workflow with known
ground truth, a declared information fault, explicit authority boundaries, and
one assurance control. Deliver working code, a reviewed protocol, recorded
empirical trials, analysis, a technical report, and a usable handoff.

The scripted pilot is the starting apparatus. Its deterministic output validates
the machinery; it does not satisfy the empirical-study requirement. The study
needs at least one empirical agent backend selected after the protocol is
reviewed, with enough recorded provenance to inspect the observed behavior.
Model access, spending limits, and a feasible run count must be settled before
implementation or paid runs depend on them. No model budget is assumed here.
This plan itself does not authorize spending.

Core scope includes one workflow, one fault mechanism, one empirical backend,
the existing oracle control as an explicitly idealized comparison, clean and
perturbed conditions, utility measures, and reproducibility. A causal claim
about authority requires the separate design described in the research plan;
it is not an automatic consequence of varying authority caps.

Stretch work includes a practical verifier using independent evidence, multiple
models, additional fault mechanisms, extra domains, or a publication submission.
Start stretch work only after core dependencies are secure. Novelty and
publication depend on evidence and are not promised semester deliverables.

## Milestones and dependencies

GitHub [milestones](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/milestones)
and [issues](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues) are the live
work queue. Use these exact milestone titles. Dates below are working project
targets; a milestone passes only when its evidence is reviewed, regardless of
the calendar date.

| Milestone | Work and dependencies | Evidence required to pass the gate |
| --- | --- | --- |
| **M1 — Onboard and reproduce** | Self-enroll through [#5](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/5), reproduce the starter in [#1](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/1), and claim a first task. | Reproduction commands, environment, commit, artifact checks, and a reviewed contribution from each active student; setup gaps captured as issues. |
| **M2 — Review evidence and freeze protocol** | Depends on M1 apparatus understanding. Literature [#2](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/2) selects a reproduction [#6](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/6); both inform protocol [#3](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/3). Choose a feasible empirical backend and resolve access/resources. | Linked primary sources and reproduction lessons; one question and explicit claim boundary; frozen protocol revision with scenario selection, treatment assignment, outcomes/denominators, repeats, analysis, exclusions, stopping rules, backend settings, and run budget. Method lead records review. |
| **M3 — Implement and validate** | Depends on the M2 protocol. Implement and validate the minimum empirical backend, traces, and analysis in [#7](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/7). | Passing relevant tests; inspected smoke traces; treatment and authority checks; correct clean-run behavior; documented errors/retries and resource use; reproducible analysis from a small artifact set. Research and Engineering review implementation against the protocol. |
| **M4 — Run and analyze** | Depends on M3 validation and the recorded M2 protocol. Execute and analyze the study in [#8](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/8), retaining failures and exclusions. | Versioned experiment records and manifests; accessible reviewed artifacts; counts, denominators, paired comparisons and uncertainty appropriate to the design; utility alongside containment; protocol deviations linked and explained. A peer reproduces the analysis. |
| **M5 — Report and hand off** | Depends on M4 evidence. Consolidate one report, student credit, reproduction instructions, and next steps in [#9](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/9). | Report claims link to sources and results; limitations and null findings are retained; another contributor follows the handoff successfully; open work has owners or explicit unassigned status; student credit is reviewed against linked contributions. |

Practical verifier [#4](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/4) stays in the `stretch` backlog without a delivery milestone. Adopt it through a reviewed scope decision after the core implementation is feasible; optional work does not distort the completion status of required milestones.

## Calendar and working targets

NYU Tandon's published Fall 2026 calendar has classes from **September 2 through December 14**, reading day on **December 15**, and final exams **December 16–22**. Fall break is October 12, October 14 follows a Monday class schedule, and Thanksgiving recess is November 26–27. Source: [NYU Tandon School Calendar](https://engineering.nyu.edu/academics/registration/school-calendar), checked September 15, 2026.

The targets below organize this repository's work from its September 15 setup. They are proposed project checkpoints, not published NYU course deadlines. Instructor deadlines take precedence; update this plan and the matching GitHub milestone together when dates change.

| Milestone | Working window | Target date |
| --- | --- | --- |
| M1 — Onboard and reproduce | September 15–25 | September 25 |
| M2 — Review evidence and freeze protocol | September 28–October 9 | October 9 |
| M3 — Implement and validate | October 13–30 | October 30 |
| M4 — Run and analyze | November 2–20 | November 20 |
| M5 — Report and hand off | November 23–December 14 | December 14 |

Use November 23–25 for the report outline and evidence review, then resume after Thanksgiving. Complete the handoff by the last day of classes so the plan does not add project delivery during exams. A late-joining student starts with the same short onboarding path and a scoped task in the current milestone.

## Passing each milestone

Literature reading, documentation, and contributor onboarding may run in parallel.
Protocol-sensitive implementation waits for M2. Confirmatory runs wait for M3;
exploratory smoke runs must be labeled as such and must not quietly enter the
final study. Each gate closes only when its evidence is linked from the relevant
issues and reviewed. The method lead confirms scientific gates; maintainers
confirm repository and reproducibility checks. These are required reviews, not
reviews this document asserts have happened.

If empirical access or another core dependency cannot be resolved, open a scope
decision issue and revise this plan with instructor/method-lead review. An
apparatus-only deliverable must be named as a reduced outcome, with the reason
recorded; it must not be described as a completed empirical study.

## Responsibility and student visibility

| Role | Accountability |
| --- | --- |
| Instructor / method lead | Confirm roster, calendar, scientific scope, access/resources, protocol, changes to claims, and gate reviews. Assign people to these responsibilities in the task queue; no names are assumed here. |
| Research | Literature evidence, question and protocol, scenario rationale, analysis, interpretation, and report. |
| Engineering | Workflow/backend, instrumentation, controls, test coverage, run tooling, artifact provenance, and reproducibility. |
| Every student | Own a scoped issue, update its evidence and blockers, submit attributable work, review peer work, and keep contribution records current. |

Students may work across roles. Each task has one accountable issue owner and
names collaborators and reviewers. Research and Engineering review together
when a change affects treatment, measures, traces, or interpretation. Contributions
can be code, research synthesis, validation, analysis, documentation, or review;
link the actual artifact and describe the student's role. Follow
[CONTRIBUTING.md](../CONTRIBUTING.md) and the [cohort guide](cohort-guide.md) for
the contribution record and review workflow. Commit totals and lines of code
are not measures of research contribution.

## Weekly rhythm

1. Before the cohort meeting, each active owner updates their issue with work
   completed, evidence links, blockers, and the next concrete step.
2. At the meeting, inspect progress against the current gate, resolve cross-team
   dependencies, and choose achievable next tasks. Keep concise
   [meeting notes](meetings/README.md) with decisions and action owners.
3. During the week, submit small linked pull requests and review peer work.
   Update contribution evidence when a PR or other durable artifact is ready.
4. At the end of the cycle, link accepted evidence to the milestone issues and
   record consequential decisions in the [decision log](decisions.md).

A Project board can be a view of the issues; it does not replace them. The
milestone and issue records remain usable without a board.

## Changes and definition of done

A scope or method change starts with an issue explaining the reason, impact on
claims, affected tasks, and resource implications. Link a PR updating the plan
and, when relevant, the protocol. Record the decision and reviewer after review.
Changes after data collection begins must preserve the original protocol and
identify affected runs and analyses. Do not silently rewrite planned outcomes
after seeing results.

An issue is done when its acceptance criteria are supported by linked, reusable
evidence, the appropriate reviewer has reviewed it, and the contribution record
identifies participants and roles. Open follow-ups explicitly. A milestone is
done when its required gate evidence is complete; optional stretch work does
not hold the core gate open.

The semester ends with the [single report and handoff package](reports/README.md).
Any unfinished goal stays visible as an issue with its current state and next
action so the next cohort can continue from evidence.
