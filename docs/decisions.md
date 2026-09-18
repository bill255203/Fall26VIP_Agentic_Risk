# Decision log

Record decisions that change scope, method, resources, responsibilities, or
interpretation. Routine task progress belongs in issues. Link the issue or PR
that contains the reasoning and actual review; meeting discussion alone does
not establish approval.

Use `proposed`, `accepted`, `rejected`, or `superseded`. An accepted decision
needs the responsible reviewer's recorded agreement. Keep prior entries when
a decision changes and link the replacement. Dates are the decision dates,
not a planned completion schedule.

| ID | Date | Status | Decision | Basis / review record |
| --- | --- | --- | --- | --- |
| D001 | 2026-09-15 | accepted | Use `zhongnz/Fall26VIP_Agentic_Risk` as the canonical Fall 2026 VIP repository, with an explicit plan and visible student contributions. | Repository owner requested this direction in the setup conversation on this date. The [semester plan](semester-plan.md) implements the charter; this row does not assert instructor approval of an experimental protocol. |
| D002 | 2026-09-15 | superseded | Initial working checkpoints extended core work to the end of term. Retain the NYU Tandon calendar and self-enrollment approach; replace the checkpoint schedule with D005. | [Original schedule](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/blob/658b8e4390198975217dad3d2aaab4ee44ea7ad6/docs/semester-plan.md#calendar-and-working-targets). The owner subsequently requested front-loaded work and milestones; see D004 and [scope issue #11](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/11). |
| D003 | — | proposed | Select one empirical question and freeze its protocol and permitted claim before confirmatory runs or analysis. | Resolve through [selection and protocol issue #3](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/3); link the selected question, reviewed protocol revision, and reviewer agreement. No study is selected yet. |
| D004 | 2026-09-15 | accepted | Draw selectively from Agent Assurance as a source of testable assumptions alongside independent literature, and front-load the semester's core work. Preserve student critique, null/adverse findings, and visible contribution evidence. | Repository owner explicitly requested this direction in the setup conversation on this date; [scope issue #11](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/11) records the implementation. The [source map](agent-assurance-bridge.md) pins and limits the borrowed concepts. This accepts the direction, not a frozen experimental protocol or model budget. |
| D005 | 2026-09-15 | superseded | Front-loaded targets included a required empirical backend and practical gate by October 2. D007 retains the dates while making the selected study determine the implementation. | [Previous plan](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/blob/c440afea7943d88480cbaddc49e0d2558f4c4a32/docs/semester-plan.md#calendar-and-working-targets). D006 removes the implicit commitment to the containment proposal. |
| D006 | 2026-09-16 | accepted | Give students a bounded period to help choose the research question. Treat runtime containment as unselected Candidate A; compare at most two developed cohort proposals using literature, reproduction, and feasibility evidence. Preserve research standards, early evidence, and credit for exploration and reasoned rejections. | The owner agreed with the review and requested a consistent repository update; [scope issue #13](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/13) records this work. The [selection guide](studies/README.md#selection-and-protocol) implements the process. This accepts the process, not a candidate, protocol, or budget; D003 remains pending. |
| D007 | 2026-09-16 | superseded | Previous working targets: kickoff/critique September 18; selected question and protocol September 25; smallest validated selected study October 2; dataset/analysis October 16; full draft October 23; report/handoff November 6. | [Previous schedule](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/blob/15c88d004658bc4a2cea63a4b2d29d4b0b3b166f/docs/semester-plan.md#calendar-and-working-targets). The owner noted the cohort had not met and September 18 was too tight. Replaced by D008; these dates are historical, not active deadlines. |
| D008 | 2026-09-16 | superseded | Start the schedule from the first cohort meeting, with no required repository submission before it. Previous working targets from kickoff: M1 +7 days, M2 +14, M3 +21, M4 +35, full draft +42, M5 +56. D009 retains relative dates and full-week onboarding while extending research formation. | The owner confirmed that the meeting is not scheduled and explicitly requested relative dates; [scope issue #15](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/15) records the change. These offsets are historical; use the [current semester schedule](semester-plan.md#calendar-and-working-targets). D003's study selection remains pending. |
| D009 | 2026-09-16 | accepted | Put pre-selection feasibility in #3 and make #7 strictly post-selection. Allow three weeks for founding-cohort research formation: working targets are M1 +7 days, M2 +21, M3 +28, M4 +42, draft +49, M5 +63. Move later targets by one week to preserve experiment and review time. Compare concise candidate outlines; A illustrates a mature protocol. | The owner supplied a kickoff review identifying the circular #3/#7 dependency and recommending consideration of a third formation week. This update adopts that working window within the existing relative-date plan. [Issue #3](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/3) owns feasibility and selection; no extra student task is added. At this decision, calendar dates were unset pending kickoff; D010 records the confirmed date. Offsets remain adjustable project targets, not instructor approval of a protocol or budget. D003 remains pending. |
| D010 | 2026-09-18 | accepted | Set kickoff to September 18, 2026 and apply D009 offsets: M1 September 25, M2 October 9, M3 October 16, M4 October 30, draft November 6, M5 November 20. Publish a student roadmap covering individual actions, shared deliverables, submission locations, weekly review, and resources. | The owner confirmed the first meeting is September 18 and requested clear student instructions and resource locations. [Onboarding issue #5](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/5) coordinates kickoff work. The published Tandon calendar was checked; dates are project targets, with course-specific requirements and availability for the instructor to confirm. This records the scheduled kickoff, not attendance, completed student work, or protocol approval; D003 remains pending. |
| D011 | 2026-09-18 | accepted | Use Group goals for cohort outcomes and separate Individual tasks for each student's meaningful work package. Independent attempts at the same assignment have separate tasks, evidence, and completion states. Joint work links each student's task to shared artifacts; intro-only PRs keep the #5 shortcut. | The owner requested an unambiguous issue structure, including two students completing the same assignment individually. The [issue workflow](issue-workflow.md) defines the operating rules. Existing #1–#9 remain Group goals with the same dependencies and dates; grading weights in draft PR #19 are not adopted by this workflow update. |
| D012 | 2026-09-18 | accepted | Publish the tentative 70% individual / 30% group working scheme and align student instructions, portfolio/report templates, #3/#9, and milestones. Individual work uses four stage budgets (10/10/20/10); add two group presentations and individual contribution reports. | The owner requested 70/30, issue-based individual assessment, reports and presentations, then explicitly requested completion and merge of all PRs. [PR #19](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/pull/19) implements this direction. This accepts publication of a tentative working plan, not formal instructor approval of grading policy, presentation slots, or submission arrangements. D003 remains pending. |

## New entry template

```markdown
### DNNN — Short decision title

- Date: YYYY-MM-DD (leave pending while proposed)
- Status: proposed
- Owner / required reviewer:
- Question and options:
- Decision and rationale:
- Evidence / issue / PR links:
- Impact on scope, protocol, artifacts, resources, or credit:
- Review record: (link recorded agreement before marking accepted)
- Supersedes / follow-up:
```

Protocol amendments must identify the original revision, affected runs, and
whether the change happened before or after inspecting results.
