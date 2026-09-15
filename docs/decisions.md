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
| D003 | — | proposed | Freeze the empirical protocol and its permitted claim before confirmatory runs. | Resolve through [study-specification issue #3](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/3); link the reviewed protocol revision and reviewer agreement. |
| D004 | 2026-09-15 | accepted | Draw selectively from Agent Assurance as a source of testable assumptions alongside independent literature, and front-load the semester's core work. Preserve student critique, null/adverse findings, and visible contribution evidence. | Repository owner explicitly requested this direction in the setup conversation on this date; [scope issue #11](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/11) records the implementation. The [source map](agent-assurance-bridge.md) pins and limits the borrowed concepts. This accepts the direction, not a frozen experimental protocol or model budget. |
| D005 | 2026-09-15 | proposed | Working targets: kickoff September 18; protocol September 25; empirical backend and practical gate October 2; dataset/analysis October 16; full draft October 23; final report/handoff November 6. | Implements D004 in the [semester plan](semester-plan.md#calendar-and-working-targets) and GitHub milestones, superseding D002's schedule. These are adjustable project targets, not official NYU deadlines or an assertion of instructor approval of each date. Access and feasibility are checked early; Study 1 remains subject to D003. |

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
