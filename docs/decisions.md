# Decision log

Record substantial program decisions and their reasoning here. Routine adjustments
belong in the affected issue. Instructor direction can be given in a course
announcement or discussion; maintainers record it and synchronize the guides.
This log does not create an approval process. Distinguish actual decisions from
suggestions, and preserve dated method changes that affect research claims.

Current direction: **D017** (pair cases), **D018** (75/25 grading), **D019** (flexible workflow) and **D020** (shared propagation theme). Earlier entries record the historical plan; references
to one cohort study or D003 pending selection are superseded as specified below.

Use `proposed`, `accepted`, `rejected`, or `superseded`. An accepted decision
records who made it and the source of that direction. Keep prior entries when
a decision changes and link the replacement. Dates are the decision dates,
not a planned completion schedule.

| ID | Date | Status | Decision | Basis / review record |
| --- | --- | --- | --- | --- |
| D001 | 2026-09-15 | accepted | Use `zhongnz/Fall26VIP_Agentic_Risk` as the canonical Fall 2026 VIP repository, with an explicit plan and visible student contributions. | Repository owner requested this direction in the setup conversation on this date. The [semester plan](semester-plan.md) implements the charter; this row does not assert instructor approval of an experimental protocol. |
| D002 | 2026-09-15 | superseded | Initial working checkpoints extended core work to the end of term. Retain the NYU Tandon calendar and self-enrollment approach; replace the checkpoint schedule with D005. | [Original schedule](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/blob/658b8e4390198975217dad3d2aaab4ee44ea7ad6/docs/semester-plan.md#calendar-and-working-targets). The owner subsequently requested front-loaded work and milestones; see D004 and [scope issue #11](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/11). |
| D003 | — | superseded | Select one empirical question and freeze its protocol and permitted claim before confirmatory runs or analysis. | Resolve through [selection and protocol issue #3](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/3); link the selected question, reviewed protocol revision, and reviewer agreement. Replaced by pair-specific plan reviews in D017; this cohort selection was never completed. |
| D004 | 2026-09-15 | accepted | Draw selectively from Agent Assurance as a source of testable assumptions alongside independent literature, and front-load the semester's core work. Preserve student critique, null/adverse findings, and visible contribution evidence. | Repository owner explicitly requested this direction in the setup conversation on this date; [scope issue #11](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/11) records the implementation. The [source map](agent-assurance-bridge.md) pins and limits the borrowed concepts. This accepts the direction, not a frozen experimental protocol or model budget. |
| D005 | 2026-09-15 | superseded | Front-loaded targets included a required empirical backend and practical gate by October 2. D007 retains the dates while making the selected study determine the implementation. | [Previous plan](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/blob/c440afea7943d88480cbaddc49e0d2558f4c4a32/docs/semester-plan.md#calendar-and-working-targets). D006 removes the implicit commitment to the containment proposal. |
| D006 | 2026-09-16 | accepted | Give students a bounded period to help choose the research question. Treat runtime containment as unselected Candidate A; compare at most two developed cohort proposals using literature, reproduction, and feasibility evidence. Preserve research standards, early evidence, and credit for exploration and reasoned rejections. | The owner agreed with the review and requested a consistent repository update; [scope issue #13](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/13) records this work. The [selection guide](studies/README.md#selection-and-protocol) implements the process. This accepts the process, not a candidate, protocol, or budget; D003 remains pending. |
| D007 | 2026-09-16 | superseded | Previous working targets: kickoff/critique September 18; selected question and protocol September 25; smallest validated selected study October 2; dataset/analysis October 16; full draft October 23; report/handoff November 6. | [Previous schedule](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/blob/15c88d004658bc4a2cea63a4b2d29d4b0b3b166f/docs/semester-plan.md#calendar-and-working-targets). The owner noted the cohort had not met and September 18 was too tight. Replaced by D008; these dates are historical, not active deadlines. |
| D008 | 2026-09-16 | superseded | Start the schedule from the first cohort meeting, with no required repository submission before it. Previous working targets from kickoff: M1 +7 days, M2 +14, M3 +21, M4 +35, full draft +42, M5 +56. D009 retains relative dates and full-week onboarding while extending research formation. | The owner confirmed that the meeting is not scheduled and explicitly requested relative dates; [scope issue #15](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/15) records the change. These offsets are historical; use the [current semester schedule](semester-plan.md#calendar-and-working-targets). D003's study selection remains pending. |
| D009 | 2026-09-16 | accepted | Put pre-selection feasibility in #3 and make #7 strictly post-selection. Allow three weeks for founding-cohort research formation: working targets are M1 +7 days, M2 +21, M3 +28, M4 +42, draft +49, M5 +63. Move later targets by one week to preserve experiment and review time. Compare concise candidate outlines; A illustrates a mature protocol. | The owner supplied a kickoff review identifying the circular #3/#7 dependency and recommending consideration of a third formation week. This update adopts that working window within the existing relative-date plan. [Issue #3](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/3) owns feasibility and selection; no extra student task is added. At this decision, calendar dates were unset pending kickoff; D010 records the confirmed date. Offsets remain adjustable project targets, not instructor approval of a protocol or budget. D003 remains pending. |
| D010 | 2026-09-18 | accepted | Set kickoff to September 18, 2026 and apply D009 offsets: M1 September 25, M2 October 9, M3 October 16, M4 October 30, draft November 6, M5 November 20. Publish a student roadmap covering individual actions, shared deliverables, submission locations, weekly review, and resources. | The owner confirmed the first meeting is September 18 and requested clear student instructions and resource locations. [Onboarding issue #5](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/5) coordinates kickoff work. The published Tandon calendar was checked; dates are project targets, with course-specific requirements and availability for the instructor to confirm. This records the scheduled kickoff, not attendance, completed student work, or protocol approval; D003 remains pending. |
| D011 | 2026-09-18 | accepted | Use Group goals for cohort outcomes and separate Individual tasks for each student's meaningful work package. Independent attempts at the same assignment have separate tasks, evidence, and completion states. Joint work links each student's task to shared artifacts; intro-only PRs keep the #5 shortcut. | The owner requested an unambiguous issue structure, including two students completing the same assignment individually. The [issue workflow](issue-workflow.md) defines the operating rules. Existing #1–#9 remain Group goals with the same dependencies and dates; grading weights in draft PR #19 are not adopted by this workflow update. |
| D012 | 2026-09-18 | accepted | Publish the tentative 70% individual / 30% group working scheme and align student instructions, portfolio/report templates, #3/#9, and milestones. Individual work uses four stage budgets (10/10/20/10); add two group presentations and individual contribution reports. | The owner requested 70/30, issue-based individual assessment, reports and presentations, then explicitly requested completion and merge of all PRs. [PR #19](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/pull/19) implements this direction. This accepts publication of a tentative working plan, not formal instructor approval of grading policy, presentation slots, or submission arrangements. D003 remains pending. |
| D013 | 2026-09-18 | accepted | Apply one Individual-task rule to onboarding and research work. Give the two presentations and individual report collection dedicated Group goals; publish a complete task/assessment map and an instructor checkpoint tracker. | The owner questioned the #5 exception and missing visible assessment issues. This removes D011's introduction-only shortcut while preserving its separate ownership/evidence rule. New goals [#21](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/21), [#22](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/22), [#23](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/23) and instructor tracker [#24](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/24) make existing deliverables visible; grading weights, dates, and pending study selection are unchanged. Existing evidence is linked rather than resubmitted. |
| D014 | 2026-09-18 | accepted | Use Individual tasks and linked PRs as the ongoing contribution record. Keep a simple roster, the individual contribution report, and the final group credit summary; remove routine portfolio tables and mandatory CRediT labeling. | The owner approved simplifying duplicate contribution records. Onboarding now requires a roster-entry PR, not a personal profile file. Students create individual reports at the draft checkpoint using existing task/PR evidence; preserve any earlier records. The tentative 70/30 scheme, report’s 10%, issue ownership, and project dates stay unchanged. |
| D015 | 2026-09-18 | accepted | Describe multiple students independently completing the same agreed assignment, with one task per student and no two-student limit. Document actual access/main protection, the fork-first student workflow, trusted reviewer onboarding, and the owner bootstrap exception. | The owner requested access-management guidance and corrected the participant wording. The [access guide](access-management.md) records the September 18 API audit; this update grants no new access and does not change protection settings. Enable administrator enforcement after an eligible independent reviewer and appropriate code-owner coverage are in place. |
| D016 | 2026-09-21 | accepted | Add nine weekly student goals from kickoff through M5, with individual evidence, shared outcomes, and existing parent issues. Use intermediate weeks for exploration, early evidence checks, and review; reuse ongoing tasks and keep the existing milestone dates and grading scheme. | The owner requested weekly goals for the student guide and roadmap. The [weekly goals](student-start.md#weekly-goals) elaborate the canonical semester plan without adding weekly graded submissions, new tracking issues, assumed meeting times, or claims of completed student work. Prerequisite gates and instructor-agreed scope adjustments still apply. |

## D017 — Pair case studies with guided empirical work

- Date: 2026-09-23
- Status: accepted (repository working direction; grading remains tentative)
- Basis: the owner requested that the repository reflect the discussed pair-based,
  beginner-supported approach following Prof. Aboussalah's proposal.
- Decision: one bounded business case per pair; shared teaching resources and
  cross-pair review; one Pair case issue plus one-owner Individual tasks. Preserve
  existing student work. Instructor prepares/tests the external platform example;
  none is adopted or funded by this update.
- Schedule: retain Sep 25, Oct 9, Oct 16, Oct 30, Nov 6 and Nov 20 targets. M2 is
  the case outline; M3 includes the midterm presentation and reviewed evidence plan.
- Historical tentative assessment (replaced by D018): retain individual 50/10/10; propose pair midterm 10 and
  report/evidence 20. Final presentation remains required with feedback, no separate
  weight. Formal instructor confirmation and presentation slots remain pending.
- Supersedes: D003's pending cohort selection; the single-study/two-subteam aspects
  of D006/D009; the cohort-wide shared grading split of D012; and D016's old weekly
  outputs. Retains D010 dates, individual attribution and no-duplicate-log principles.
- Implementation/review record: [PR #32](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/pull/32) records validation and the documented owner bootstrap merge exception.
  Pair-specific plan approvals are recorded separately, not inferred from this decision.

## D018 — Increase individual grading to 75% and align the working guides

- Date: 2026-09-23
- Status: accepted for the repository proposal; formal course confirmation remains pending
- Basis: the owner explicitly requested 75% individual / 25% pair and a thorough
  review of coherence, correctness and structure.
- Decision: individual work 55 (Foundation 10, Question 10, Execution 25, Synthesis 10),
  collaboration 10, individual report 10; pair midterm 10 and final report/evidence 15.
  Move five points from the integrated pair report to individual execution evidence.
  Final presentation stays required with feedback and no separate grade weight.
- Preserve: D017 pair-case approach, dates, credit for existing work, and one evidence
  record per task. Do not apply new grading retrospectively without announced policy.
- Coherence fixes: clarify study-plan/task/merge review responsibilities, collection
  issue links, prior-inspected evidence, platform support status and beginner setup.
  Keep the grading proposal and semester plan authoritative for weights and dates.
- Implementation/review record: [PR #33](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/pull/33) records the audit, validation and owner bootstrap merge exception.
  Checked documents, live issue/milestone descriptions, source references, protection
  settings and the scripted starter. External-platform preparation remains pending.
- Supersedes: the weight/rubric portions of D012 and D017 only; retain those entries
  as historical records, not current student instructions.

## D019 — Flexible, student-owned work with adaptable course direction

- Date: 2026-09-23
- Status: accepted (repository working direction; course grading remains tentative)
- Basis: the owner requested a logical, professional structure that allows the
  instructor to adapt freely without an administrative or preparation burden.
- Decision: partners register their case, own the working method and proceed with
  peer checks. Remove mandatory instructor/mentor plan approvals. Keep methods,
  changes, evidence and claim limits explicit; prespecify confirmatory tests.
- Resources: the starter/walkthrough is available. #6 becomes optional shared
  examples and setup help, not an instructor obligation to build a platform by M2.
- Adaptation: instructor announcements/discussions can change direction, scope,
  timing, pairings and activities. Maintainers record a short note and synchronize
  affected guidance; the course does not wait for a PR. #24 becomes course notes,
  not a checkpoint-by-checkpoint instructor checklist.
- Preserve: 75/25 proposal, visible personal contributions, pair/individual reports,
  current dates as adjustable targets, fair announced assessment and main protection.
- Supersedes: instructor sign-off and mandatory teaching-package provisions in
  D017/D018 and the administrative checklist aspect of D013. No faculty approval,
  new pair assignment, platform access or funding is asserted.
- Implementation/review record: [PR #35](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/pull/35),
  including validation and the documented owner bootstrap merge exception.

## D020 — Risk propagation and containment as the shared theme

- Date: 2026-09-23
- Status: accepted (repository research direction)
- Basis: after discussing that the pair-case framing had broadened to agentic
  risk generally, the owner proposed adopting risk propagation as the theme.
- Decision: each pair connects a business case to an error/input origin, possible
  propagation path, consequence and possible control, then studies one bounded
  question about that path. These prompts fit the existing outline and report.
- Scientific scope: one agent can qualify; propagation, correction, containment,
  no observed propagation and insufficient evidence must be distinguished. No
  required multi-agent architecture, injected fault or successful control result.
  Trace observations alone do not establish an intervention's causal effectiveness.
- Preserve: D019 instructor flexibility, student-owned work and peer feedback;
  the 75/25 proposal, dates, individual reports, existing contributions and normal
  repository review. No new deliverable, approval gate or grading component.
- Refines: the broad risk-question framing in D017; the cohort shares a research
  theme while pairs retain their own business cases and methods.
- Implementation/review record: [PR #36](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/pull/36),
  including validation and the documented owner bootstrap merge exception.

## New entry template

```markdown
### DNNN — Short decision title

- Date: YYYY-MM-DD (leave pending while proposed)
- Status: proposed
- Decision-maker / participants:
- Question and options:
- Decision and rationale:
- Evidence / issue / PR links:
- Impact on scope, protocol, artifacts, resources, or credit:
- Decision source: (link the actual direction before marking accepted)
- Supersedes / follow-up:
```

Protocol amendments must identify the original revision, affected runs, and
whether the change happened before or after inspecting results.
