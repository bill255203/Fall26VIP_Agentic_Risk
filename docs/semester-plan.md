# Fall 2026 semester plan

This repository is the canonical workspace for the Fall 2026 Agentic Risk VIP.
The cohort will select one study and share one task queue and final report.
This document defines delivery gates; the [selection guide](studies/README.md)
explains how students choose the question, and the [research plan](research-plan.md)
defines research standards and the starter's claim limits.

**Kickoff: Friday, September 18, 2026.** No repository submission is due at kickoff.
The instructor introduces the project and demonstrates the starter; students have
until **September 25** for the first onboarding checkpoint. The [student guide](student-start.md)
explains individual tasks, the shared deliverables, where to submit work, and resources.

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

Access to data or models and the smallest feasibility check begin during the first
week after kickoff. Study settings and resources are frozen in M2; evaluation data/cases are
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
| **M1 — Onboard and reproduce** | After the first meeting, self-enroll through [#5](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/5), try the starter in [#1](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/1), and bring a question or setup blocker. Agree small reading, reproduction, and feasibility tasks across the cohort. | Introduction PRs and linked starter evidence from the active kickoff group; one shared reviewed trace walkthrough; recorded setup blockers with a help plan; named next-task owners. Students report blocked attempts honestly. Unresolved reproduction needs remain visible and the gate closes only when required evidence is reviewed. Late enrollment has an agreed individual onboarding target. |
| **M2 — Select a question and freeze protocol** | Pilot critique [#1](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/1), literature [#2](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/2), and one bounded reproduction [#6](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/6) inform [#3](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/3), which owns pre-selection feasibility probes, candidate comparison, selection, and protocol freeze. | Compare at most two developed proposals; record source evidence, reproduction/probe findings or concrete limitations, selection rationale, and method review. Freeze one feasible protocol with comparison, outcomes, labels/data, analysis, failure rules, access/resources, and claim limits; align study tasks with the decision. Neither candidate selection nor feasibility is assumed. |
| **M3 — Implement and validate** | After #3 selects a study and freezes its protocol, build and validate the smallest selected experiment or analysis pipeline in [#7](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/7). Reuse suitable probes from #3; #7 starts only after M2. If A is chosen, activate practical gate [#4](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/4) here. | End-to-end development evidence and analysis smoke; validated labels/outcomes, failure handling, provenance, and appropriate comparison. Freeze evaluation cases/data before confirmatory work. For A specifically: all four conditions, genuine model traces, source/answer separation, and isolated paired replay with the practical gate. |
| **M4 — Run and analyze** | Depends on M3 validation and the recorded M2 protocol. Collect or assemble the planned evidence and analyze it in [#8](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/8), retaining failures and exclusions. | Versioned records and accessible reviewed artifacts; counts, denominators, comparisons and uncertainty appropriate to the design; relevant utility/cost tradeoffs; protocol deviations linked and explained. A peer reproduces the analysis. |
| **M5 — Report and hand off** | Start a shared outline during onboarding and add evidence as it arrives. Complete the draft at the checkpoint below, then reproduce, review, revise, and hand off in [#9](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/9). | Report claims link to sources/results; source-author relationship and claim limits are disclosed; null/adverse findings retained; another analyst follows the handoff; open work has owners or explicit unassigned status; student credit is reviewed. |

Issue #4 has no delivery milestone while Candidate A is unselected. If A is
selected, its practical gate becomes required M3 work: an oracle-only comparison
cannot establish practical containment effectiveness. If another study is selected,
update #7/#8 and define only the implementation work that study needs. No candidate
is adopted automatically because it already has a document or issue.

## Calendar and working targets

NYU Tandon's published Fall 2026 calendar has classes from **September 2 through December 14**, reading day on **December 15**, and final exams **December 16–22**. Fall break is October 12, October 14 follows a Monday class schedule, and Thanksgiving recess is November 26–27. Source: [NYU Tandon School Calendar](https://engineering.nyu.edu/academics/registration/school-calendar), checked September 18, 2026.

**T = September 18, 2026**, the confirmed first cohort meeting. The dates below
apply the agreed offsets and are working project targets in New York local dates,
not grading deadlines or a newly prescribed submission time. GitHub milestones
use the same target dates. The instructor confirms course-specific requirements
and adjusts scope or targets if student availability or access requires it.

| Checkpoint | Work | Target from kickoff | 2026 target date |
| --- | --- | --- | --- |
| First meeting | Orientation, starter demo, interests, setup support, task allocation | T | September 18 |
| M1 — Onboard and reproduce | Introduction PR, starter attempt, shared trace walkthrough, blockers and small next tasks | T + 7 days (1 week) | September 25 |
| M2 — Select a question and freeze protocol | Focused reading, one shared bounded reproduction, feasibility, selection, and reviewed protocol | T + 21 days (3 weeks) | October 9 |
| M3 — Implement and validate | Smallest end-to-end selected experiment or analysis pipeline | T + 28 days (4 weeks) | October 16 |
| M4 — Run and analyze | Planned evidence and first complete analysis | T + 42 days (6 weeks) | October 30 |
| Full report draft | Assemble the evolving report for criticism and reproduction | T + 49 days (7 weeks) | November 6 |
| M5 — Report and hand off | Reviewed report, reproducible handoff, and contribution credit | T + 63 days (9 weeks) | November 20 |

The founding cohort has three weeks to form the research question: week 1 centers
on onboarding and pilot critique; week 2 on literature, bounded reproduction, and
exploration; week 3 on candidate formation, feasibility, selection, and protocol review.
Students take small complementary tasks rather than each completing a full literature
review, reproduction, and proposal. This gives emerging alternatives time to develop;
Candidate A's longer protocol is a teaching example, not an entry requirement.
This preserves time for implementation, experiments, and review after selection.
For a live-agent study, feasibility includes a genuine model development trace;
an existing-data study needs accessible data, usable labels, and an analysis probe.

All targets fall on Fridays and the core handoff precedes Thanksgiving recess.
The M3 week includes fall break on October 12 and the October 14 schedule change;
plan task capacity around them and raise blockers at the M2 review. If access or
availability makes the sequence infeasible, record a narrower scope or adjusted
targets in this plan and GitHub together. Use remaining term time for instructor-agreed
presentations, justified repairs, and review; presentation dates remain to be arranged.
No required work should be assigned during Thanksgiving recess or moved into exams.

## Passing each milestone

After kickoff, divide literature reading, candidate proposals, data/model feasibility,
reusable tooling, documentation, and onboarding across the cohort. Keep the
early paper reproduction bounded to a relevant result/component; do not wait for
an entire benchmark reimplementation before making a protocol decision. Record
infeasibility and choose a narrower reviewed target by M2 if needed.

Do not spend on model calls until access and a bounded smoke budget are agreed.
Development probes may precede the frozen protocol but stay labeled and
outside held-out confirmatory evidence. Final implementation conforms to M2;
confirmatory runs or analysis wait for validated M3 and frozen evaluation data. Each gate
closes only when linked evidence is reviewed. Dates alone never mark a task done.

Raise unresolved access, data, or scope issues during M1;
select a feasible study at M2. If a core dependency still cannot
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
