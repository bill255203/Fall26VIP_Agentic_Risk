# Tentative grading and individual responsibility

**Status: proposal for discussion, September 18, 2026.** These weights and individual
report expectations are not yet adopted course policy. The instructor confirms and
announces the final scheme through the course's official channel before applying it.
The existing [project schedule](semester-plan.md#calendar-and-working-targets) continues.

## Proposed grade: 70% individual, 30% group

Here, **group** means the whole cohort's one selected study. Research and Engineering
contribute to the same group output. Each student receives their own individual marks
plus the same three shared assessment marks; students do not receive identical overall grades.

| Component | Weight | What is assessed | Evidence |
| --- | --- | --- | --- |
| Individual research or engineering work | **50%** | Quality and correctness (20); reasoning and value to the agreed research task (20); evidence, validation, and usability by others (10). | Owned deliverables, source notes, designs, code, data, analyses, writing, reproduction attempts, and their review. |
| Individual collaboration and review | **10%** | Reliable communication and follow-through on agreed responsibilities (5); useful peer review and help that improves the work (5). | Issue updates, substantive review comments, documented coordination, and resolved feedback. |
| Individual contribution report | **10%** | Accurate, specific attribution linked to evidence (5); explanation of decisions, limitations, learning, and next steps (5). | A short individual report using existing portfolio links. |
| Group research-question presentation | **10%** | Evidence-based comparison and rationale (5); a feasible, testable plan and useful responses to questions (5). | One cohort presentation comparing at most two candidates, source/probe evidence, and the recorded selection discussion. |
| Group final technical report and reproducibility | **10%** | Defensible method, analysis, and honest interpretation (5); a coherent written report and usable reproduction/handoff package (5). | The reviewed report, evidence, commands, and peer reproduction check. |
| Group final presentation | **10%** | Clear, evidence-backed explanation of the study and findings (5); understanding of limitations, responses to questions, and next steps (5). | One cohort presentation with links to the final report and artifacts. |
| **Total** | **100%** | **70 individual + 30 shared** | |

Each number in parentheses is a maximum number of percentage points toward the
course grade. For example, 43/50 for work, 8/10 for collaboration, 9/10 for the individual report,
and group marks of 8/10, 8/10, and 9/10 produce **85/100**. The instructor records grades privately;
letter-grade thresholds and other course policies are not defined by this proposal.

Artifact quality is assessed in the individual-work component; report marks assess
accurate attribution and the student's explanation of that work. The three group
components separately assess selection reasoning, the written evidence/handoff,
and the final presentation and discussion.

Assess the body of work against the student's agreed scope, not by averaging scores
for arbitrary numbers of issues. The instructor agrees a feasible, substantive scope
with each student and checks its adequacy at M2 and M3. Small setup tasks are a start;
they are not a substitute for sustained research contributions. Scope may be adjusted
for role, preparation, enrolled commitment, or access, with the reason recorded.

Literature, design, code, data, analysis, validation, and writing can all earn full
individual-work marks. Rigorous null results, failed reproductions with useful
diagnoses, and evidence-backed rejection of a proposal can also earn full marks.
Publication, positive findings, hours claimed, commit counts, issue counts, and lines
of code do not determine the grade. A merged PR is evidence of review, not an automatic
grade. Public evidence can support assessment without publishing marks or private feedback.

## Two group presentations and the written report

| Assessment | Proposed checkpoint | What the cohort presents or submits |
| --- | --- | --- |
| Research-question presentation | **October 9 (M2 review)**, before selection and protocol freeze | At most two candidate questions; why each matters; relevant literature and the uncertainty or replication purpose; reproduction/feasibility evidence; the smallest comparison and measures; access/resources; a recommendation and its tradeoffs. |
| Final technical report and reproducibility | **Draft November 6; reviewed package November 20 (M5)** | The question, method, evidence and analysis, limitations, contribution credits, and the commands/artifacts needed to reproduce the work. |
| Final presentation | **November 20 (M5)** | The selected question, what was done, the strongest evidence, what it supports, limitations and negative findings, and the next useful research step. Link the report and artifacts. |

These are proposed assessment targets aligned with the project schedule. The instructor
confirms presentation slots, length, and official submission arrangements. A practical
starting point is a 10-minute question presentation and a 15-minute final presentation,
each followed by discussion, adjusted to cohort size.

Prepare one shared deck for each occasion. At the question review, different students
can present the two candidate sections, then the cohort compares them together. The
method lead records the selection and reviewed protocol in #3 after considering the
presentation and discussion. The pitch is assessed on its reasoning and feasibility;
a candidate can earn strong credit even when it is not selected. If feedback requires
more protocol work, keep the gate open and record the necessary target adjustment.

For both presentations, name each student's agreed preparation/presentation role and
link their contribution. Students should be able to explain the work they contributed;
the instructor can distribute speaking and question-answering roles to fit the group.
The group receives the shared presentation mark, while each person's preparation,
analysis, review, and follow-through support their individual assessment. Neither
speaking longest nor being the coordinator confers ownership of the whole project.

Save reviewed slides or an accessible export/link in `docs/reports/`, with links from
#3 for the question presentation and #9 for the final presentation/report. The written
technical report and the individual contribution reports remain separate outputs;
slides do not replace either report. No additional weekly slide deck is needed.

## Two levels of issues

**Shared parent issue = what the cohort delivers. Individual task = who delivers which part.**

Keep the existing issues #1–#9 as the shared work queue; #4 remains conditional on
Candidate A selection. Multiple students may join a shared issue. Name one coordinator
to keep its contributor/task links and blockers current. Coordination alone does not
give that person credit for other students' work.

For each substantial, separable deliverable, use the existing **Research work item**
form to create a linked individual task with **one accountable owner**. A native
sub-issue or a normal issue with a parent link works. Give it the parent's milestone
when active; conditional tasks remain outside delivery milestones until selected.
List collaborators and a reviewer separately. Students can own several tasks over
the term; agree a manageable active workload rather than claiming many tasks at once.

For small work, use a named row in the shared issue instead of opening another issue:

| Contributor | Agreed deliverable | Target/check-in | Evidence or task link | Reviewer |
| --- | --- | --- | --- | --- |
| @student | A specific outcome, not just “help with research” | Agreed date | Link when available | @reviewer or awaiting assignment |

This is an illustrative row, not an actual student assignment. Both routes provide
the same individual accountability and assessment opportunity. Onboarding stays
simple: the existing introduction PR and starter comment are enough; students do
not need extra issues to repeat that record.

### How a student claims work

1. Comment on the relevant shared issue: **“I propose to deliver X by Y; evidence
   will be Z. I would like to work with …”**
2. A maintainer confirms the scope, named owner, collaborators, target/check-in, and
   reviewer. Before usernames are known, work remains explicitly unassigned.
3. Put the agreed responsibility in a named row or individual task. For an individual
   task, the sole assignee is its owner; list helpers and the reviewer in the body.
4. Link the PR or other artifact and explain who did what. Use `Closes #TASK` only
   when that entire task is complete; use `Relates to #PARENT` for the shared issue.
5. The reviewer checks the result against the agreed criteria. A maintainer closes
   the shared issue only when all required parts and the shared acceptance criteria
   are complete. Reassignment preserves the original contributor's evidence and credit.

GitHub supports [multiple assignees](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/assigning-issues-and-pull-requests-to-other-github-users).
For a shared issue, additional assignees may show participation, but the named
deliverables establish responsibility. Clicking several names is not a division of work.
Students without assignment permissions can comment; a maintainer sets the fields.

### What to put in an individual task

Use these fields in the existing issue form; no second task-management system is needed:

```markdown
Parent/shared issue: #...
Owner: @...
Collaborators and their distinct parts: ...
Reviewer: @... / awaiting assignment
Milestone and target/check-in: ...
My deliverable: ...
Done when: ...
Evidence to provide: ...
Dependencies or help needed: ...
```

Example under literature issue #2: one student owns a comparison of relevant papers,
another checks the selected paper's available data/code, and another reviews whether
the proposed metric supports the intended claim. Each has a distinct output and
evidence link. For pair programming or joint analysis, one task can name a lead and
describe both people's actual work; split it only when there are separable deliverables.

Shared artifacts may appear in several portfolios, with each person's contribution
identified. There is no automatic equal split of individual credit and no requirement
to invent contribution percentages. Credit is not a fixed pool: several people can
earn strong marks for different substantive contributions to the same artifact.

## Individual contribution report

Each student prepares **one short report**, about **1–2 pages plus evidence links**.
Length is a guide, not a scoring criterion. Use the
[individual report template](contributors/_individual-report-template.md).
Draft target: **November 6**; final target: **November 20**, aligned with the shared
report and handoff. These are proposed report targets, not new official due dates.
If the instructor assigns later assessed work, update the report before the announced
assessment cutoff rather than treating the early handoff as the end of all course work.

The report answers:

1. **What was I responsible for?** State agreed tasks and any reviewed scope changes.
2. **What did I personally produce or decide?** Link the existing portfolio evidence;
   distinguish your work from collaborators' work and disclose material tool assistance.
3. **How did it help the shared study?** Explain the result, decision, or reusable asset.
4. **How did I review and support others?** Link specific review or coordination evidence.
5. **What are the limits and next steps?** Discuss unsuccessful approaches, learning,
   unfinished work, and what another student needs to continue it.

To keep this easy, extend the existing `docs/contributors/YOUR-USERNAME.md` portfolio
with the report sections. Reuse its evidence table and replace its short “Semester
reflection” placeholder; do not maintain a second activity log or duplicate the group
report. The public version contains research contributions and evidence. The instructor
confirms the official submission route; marks, personal circumstances, and private
feedback stay in that channel.

## Fair assessment and a simple routine

- **Each week:** work on the agreed deliverable, post the existing short issue update,
  submit evidence for review, and add a portfolio row when a meaningful outcome is ready.
- **At M2 and M3:** the instructor checks each student's scope and evidence, identifies
  gaps early, and agrees any change. These are progress conversations, not new reports.
- **At the M2 review:** contribute to the research-question presentation and selection discussion.
- **At handoff:** submit the individual report and contribute to the group report and final presentation.
  The instructor assesses individual evidence separately from the shared project.

If a dependency or teammate blocks delivery, raise it in the issue and agree an
alternative deliverable or scope change. Assess the student's documented work and
response; another person's missing task does not automatically erase individual credit.
The 30% shared component still reflects the integrated outcomes. Any exceptional
adjustment is an instructor decision communicated under the adopted course policy.

Peer feedback can help verify attribution and collaboration; classmates do not assign
one another's grades. Resolve disputed credit using artifact history and a private
instructor discussion. Paper authorship remains a separate contribution-based decision.

## Adoption checklist for the instructor

Confirm the weights and criteria, the assessed period, presentation slots, official
report/slide submission route, and how extensions or adjustments follow course policy. Then announce the
adopted version and update the student guide, contribution template, selection issue
#3, and shared report issue #9 together. Until then, this document remains a proposal and the existing
student instructions and live issue assignments continue to apply.
