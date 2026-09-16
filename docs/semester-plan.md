# Fall 2026 semester plan

This repository is the canonical workspace for the Fall 2026 Agentic Risk VIP.
The cohort will select one study and share one task queue and final report.
This document defines delivery gates; the [selection guide](studies/README.md)
explains how students choose the question, and the [research plan](research-plan.md)
defines research standards and the starter's claim limits.

## Semester outcome and scope

The core outcome is one bounded empirical investigation of agentic risk, with a
reviewed protocol, reusable evidence and analysis, a technical report, and a usable
handoff. Students help form the question through literature, critique, and a small
reproduction. A controlled replication or analysis of existing genuine agent traces
can meet this outcome when it has a meaningful comparison and defensible measures.

**No empirical study is selected yet.** The runnable scripted pilot teaches the
experimental method and validates the machinery. [Candidate A: runtime containment](studies/01-runtime-containment.md)
proposes a real-model workflow and practical evidence gate; it is one option.
Compare it with at most one developed cohort alternative and select one study in M2.
The [selection guide](studies/README.md#selection-and-protocol) defines the process.

What stays fixed is research quality: precise questions, relevant prior work,
appropriate comparisons and outcome labels, reproducible analysis, honest claim
limits, visible student contributions, and early evidence. A control study reports
both risk and useful-task outcomes. Other questions justify their own primary
measure and relevant tradeoffs. The domain, control, model/backend, and framework
remain choices to justify rather than universal requirements.

Access to data or models and the smallest feasibility check begin in the first
week. Study settings and resources are frozen in M2; evaluation data/cases are
frozen before confirmatory work. This plan does not authorize spending or claim
that access has been arranged. Existing artifacts can support feasibility without
new paid calls when suitable for the question.

[Agent Assurance](agent-assurance-bridge.md) and the [literature](literature.md)
supply hypotheses and methods. No named framework is mandatory. After selection,
additional questions, models, controls, or environments are stretch work requiring
an agreed scope change. Novelty and publication depend on evidence and are not
promised semester deliverables.

## Milestones and dependencies

GitHub [milestones](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/milestones)
and [issues](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues) are the live
work queue. Use these exact milestone titles. Dates below are working project
targets; a milestone passes only when its evidence is reviewed, regardless of
the calendar date.

| Milestone | Work and dependencies | Evidence required to pass the gate |
| --- | --- | --- |
| **M1 — Onboard and reproduce** | Self-enroll through [#5](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/5), reproduce and critique the starter in [#1](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/1), and claim a first task. Begin literature, data/model-access checks, and the report outline in parallel. | Reproduction commands, environment, commit, artifact checks, and a reviewed contribution from the active kickoff group; critique of what the starter establishes; named owners; early access/setup blockers. Late enrollment does not restart the cohort schedule. |
| **M2 — Select a question and freeze protocol** | Literature [#2](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/2), one bounded reproduction [#6](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/6), and feasibility checks inform selection [#3](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/3), alongside onboarding. | Compare at most two developed proposals; record source evidence, reproduction/probe findings or concrete limitations, selection rationale, and method review. Freeze one feasible protocol with comparison, outcomes, labels/data, analysis, failure rules, access/resources, and claim limits; align study tasks with the decision. Neither candidate selection nor feasibility is assumed. |
| **M3 — Implement and validate** | Build the smallest selected experiment or analysis pipeline in [#7](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/7). Reusable feasibility work starts before M2; final behavior follows the selected protocol. If A is chosen, activate practical gate [#4](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/4) here. | End-to-end development evidence and analysis smoke; validated labels/outcomes, failure handling, provenance, and appropriate comparison. Freeze evaluation cases/data before confirmatory work. For A specifically: all four conditions, genuine model traces, source/answer separation, and isolated paired replay with the practical gate. |
| **M4 — Run and analyze** | Depends on M3 validation and the recorded M2 protocol. Collect or assemble the planned evidence and analyze it in [#8](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/8), retaining failures and exclusions. | Versioned records and accessible reviewed artifacts; counts, denominators, comparisons and uncertainty appropriate to the design; relevant utility/cost tradeoffs; protocol deviations linked and explained. A peer reproduces the analysis. |
| **M5 — Report and hand off** | Draft the report from M1; add evidence as it arrives. Complete draft by October 23, then reproduce, review, revise, and hand off in [#9](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/9). | Report claims link to sources/results; source-author relationship and claim limits are disclosed; null/adverse findings retained; another analyst follows the handoff; open work has owners or explicit unassigned status; student credit is reviewed. |

Issue #4 has no delivery milestone while Candidate A is unselected. If A is
selected, its practical gate becomes required M3 work: an oracle-only comparison
cannot establish practical containment effectiveness. If another study is selected,
update #7/#8 and define only the implementation work that study needs. No candidate
is adopted automatically because it already has a document or issue.

## Calendar and working targets

NYU Tandon's published Fall 2026 calendar has classes from **September 2 through December 14**, reading day on **December 15**, and final exams **December 16–22**. Fall break is October 12, October 14 follows a Monday class schedule, and Thanksgiving recess is November 26–27. Source: [NYU Tandon School Calendar](https://engineering.nyu.edu/academics/registration/school-calendar), checked September 15, 2026.

The targets below organize this repository's work from its September 15 setup. They are proposed project checkpoints, not published NYU course deadlines. Instructor deadlines take precedence; update this plan and the matching GitHub milestone together when dates change.

| Milestone | Working window | Target date |
| --- | --- | --- |
| M1 — Onboard and reproduce | September 15–18 | September 18 |
| M2 — Select a question and freeze protocol | September 15–25, alongside onboarding | September 25 |
| M3 — Implement and validate | September 15–October 2; early feasibility, then integration | October 2 |
| M4 — Run and analyze | October 5–16 | October 16 |
| M5 — Report and hand off | Outline from September 18; complete draft October 23; revise and reproduce | November 6 |

The critical early outputs are feasibility evidence and a selected protocol by
September 25, the smallest validated selected study by October 2, and a dataset
with analysis by October 16. For a live-agent study, feasibility includes a genuine
model development trace; an existing-data study instead needs accessible data,
usable labels, and an analysis probe. Use the period after the October 23 full draft
for criticism, reproduction, and correction.

November 9–December 14 is buffer for presentations, onboarding late contributors into bounded work, justified repairs, and a small follow-up selected from results. No core build or dataset is scheduled for that buffer. Avoid required work during Thanksgiving recess; finish all course obligations by the instructor's actual deadline.

## Passing each milestone

Literature reading, candidate proposals, data/model feasibility, reusable tooling,
documentation, and onboarding begin together. Keep the
early paper reproduction bounded to a relevant result/component; do not wait for
an entire benchmark reimplementation before making a protocol decision. Record
infeasibility and choose a narrower reviewed target by M2 if needed.

Do not spend on model calls until access and a bounded smoke budget are agreed.
Development probes may precede the frozen protocol but stay labeled and
outside held-out confirmatory evidence. Final implementation conforms to M2;
confirmatory runs or analysis wait for validated M3 and frozen evaluation data. Each gate
closes only when linked evidence is reviewed. Dates alone never mark a task done.

Raise unresolved access, data, or scope issues at the September 18 check-in;
select a feasible study by September 25. If a core dependency still cannot
be met, record a method-lead scope decision immediately. An apparatus-only
deliverable is a documented reduction in scope, not a completed empirical study.

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
