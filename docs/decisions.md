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
| D007 | 2026-09-16 | proposed | Working targets: kickoff/critique September 18; selected question and protocol September 25; smallest validated selected study October 2; dataset/analysis October 16; full draft October 23; report/handoff November 6. | Supersedes D005's study-specific milestone wording, retaining its dates. [Semester targets](semester-plan.md#calendar-and-working-targets) and live GitHub milestones agree. These remain adjustable project checkpoints, not official NYU deadlines; the method lead records a narrower scope if no study meets the feasibility bar. |

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
