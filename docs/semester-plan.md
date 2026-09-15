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

The scripted pilot validates the machinery. [Study 1](studies/01-runtime-containment.md)
supplies a concrete proposed empirical path: one backend, clean/corrupted
summary pairs, and a practical independent-evidence gate off/on. All primary
conditions can execute; authority caps remain separate enforcement checks.
This keeps the effect from being predetermined by removing execution permission.

Core scope includes one workflow, one fault mechanism, one empirical backend,
one practical containment gate, safety and utility outcomes, and reproducibility.
The existing oracle remains an explicitly idealized reference. Selected
[Agent Assurance assumptions](agent-assurance-bridge.md) inform the study alongside
independent literature; testing one adaptation does not validate the whole matrix.

Backend feasibility, access, and a small smoke budget are resolved in the first
week while students refine the protocol. Full study settings and resources are
frozen in M2 before confirmatory runs. This plan does not authorize spending or
claim that model access has been arranged.

Stretch work includes additional verifier variants or ablations, multiple
models, new fault mechanisms, extra domains, full toxic-flow/egress evaluation,
trace-attribution comparisons, or a publication submission.
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
| **M1 — Onboard and reproduce** | Self-enroll through [#5](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/5), reproduce the starter in [#1](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/1), and claim a first task. Start literature, backend-access checks, and report outline in parallel. | Reproduction commands, environment, commit, artifact checks, and a reviewed contribution from the active kickoff group; named owners for research and engineering tasks; access/setup blockers raised early. Late enrollment does not restart the cohort schedule. |
| **M2 — Review evidence and freeze protocol** | Literature [#2](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/2), a bounded reproduction [#6](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/6), and feasibility work inform protocol [#3](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/3). They run alongside onboarding. | Pinned source assumptions and independent literature; reproduction result or explicit feasibility limitation; reviewed question, outcomes, utility tolerance, scenario construction plan, pairing, analysis, failure/retry rules, backend access/settings, and run budget. At least one genuine-model development trace if access is feasible; otherwise a recorded scope/access decision. |
| **M3 — Implement and validate** | Integrate core backend [#7](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/7) with the practical gate [#4](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/4). Adapter and trace work starts before M2; final study behavior must match the reviewed protocol. | Four primary conditions run end to end; genuine model inputs/outputs recorded; source evidence separated from evaluator labels; isolated paired replay; clean-task checks, failure handling, hashes, and analysis smoke validated. Freeze evaluation cases before confirmatory runs. |
| **M4 — Run and analyze** | Depends on M3 validation and the recorded M2 protocol. Execute and analyze the study in [#8](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/8), retaining failures and exclusions. | Versioned experiment records and manifests; accessible reviewed artifacts; counts, denominators, paired comparisons and uncertainty appropriate to the design; utility alongside containment; protocol deviations linked and explained. A peer reproduces the analysis. |
| **M5 — Report and hand off** | Draft the report from M1; add evidence as it arrives. Complete draft by October 23, then reproduce, review, revise, and hand off in [#9](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/9). | Report claims link to sources/results; source-author relationship and claim limits are disclosed; null/adverse findings retained; another analyst follows the handoff; open work has owners or explicit unassigned status; student credit is reviewed. |

One practical verifier is core because an oracle-only comparison cannot establish practical containment effectiveness. Additional variants remain optional and enter delivery milestones only through a scope decision.

## Calendar and working targets

NYU Tandon's published Fall 2026 calendar has classes from **September 2 through December 14**, reading day on **December 15**, and final exams **December 16–22**. Fall break is October 12, October 14 follows a Monday class schedule, and Thanksgiving recess is November 26–27. Source: [NYU Tandon School Calendar](https://engineering.nyu.edu/academics/registration/school-calendar), checked September 15, 2026.

The targets below organize this repository's work from its September 15 setup. They are proposed project checkpoints, not published NYU course deadlines. Instructor deadlines take precedence; update this plan and the matching GitHub milestone together when dates change.

| Milestone | Working window | Target date |
| --- | --- | --- |
| M1 — Onboard and reproduce | September 15–18 | September 18 |
| M2 — Review evidence and freeze protocol | September 15–25, alongside onboarding | September 25 |
| M3 — Implement and validate | September 15–October 2; early feasibility, then integration | October 2 |
| M4 — Run and analyze | October 5–16 | October 16 |
| M5 — Report and hand off | Outline from September 18; complete draft October 23; revise and reproduce | November 6 |

The critical front-loaded outputs are an empirical feasibility trace by September 25, a validated four-condition study by October 2, and a dataset with analysis by October 16. Use the period after the October 23 full draft for criticism, reproduction, and correction instead of starting the report near term end.

November 9–December 14 is buffer for presentations, onboarding late contributors into bounded work, justified repairs, and a small follow-up selected from results. No core build or dataset is scheduled for that buffer. Avoid required work during Thanksgiving recess; finish all course obligations by the instructor's actual deadline.

## Passing each milestone

Literature reading, protocol drafting, candidate-case writing, backend feasibility,
the evidence adapter, documentation, and onboarding begin together. Keep the
early paper reproduction bounded to a relevant result/component; do not wait for
an entire benchmark reimplementation before making a protocol decision. Record
infeasibility and choose a narrower reviewed target by M2 if needed.

Do not spend on model calls until access and a bounded smoke budget are agreed.
Development smoke runs may precede the frozen protocol but stay labeled and
outside held-out confirmatory evidence. Final implementation conforms to M2;
confirmatory runs wait for validated M3 and a frozen evaluation set. Each gate
closes only when linked evidence is reviewed. Dates alone never mark a task done.

Raise unresolved access, scenario, or scope issues at the September 18 check-in;
choose a feasible alternative by September 25. If a core dependency still cannot
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
