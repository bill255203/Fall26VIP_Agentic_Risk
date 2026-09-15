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
| D002 | 2026-09-15 | proposed | Use the NYU Tandon Fall 2026 calendar and the semester plan's working checkpoint dates. Students self-enroll; named leads/reviewers and empirical resources are settled during M1/M2. | The owner confirmed the NYU fall semester and requested easy reading, cloning, and contribution without a supplied roster. [Official calendar](https://engineering.nyu.edu/academics/registration/school-calendar); [working targets](semester-plan.md#calendar-and-working-targets). Project checkpoint dates remain adjustable by the instructor; no model budget or student role is inferred. |
| D003 | — | proposed | Freeze the empirical protocol and its permitted claim before confirmatory runs. | Resolve through [study-specification issue #3](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/3); link the reviewed protocol revision and reviewer agreement. |

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
