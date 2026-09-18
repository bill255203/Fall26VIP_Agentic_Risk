# Group goals and individual tasks

**Two students can complete the same assignment independently. Each student uses
a separate Individual task linked to the same Group goal.** Each task has its own
owner, evidence, review, and completion status.

## Two kinds of issue

| Kind | Purpose | Who is assigned? | When is it closed? |
| --- | --- | --- | --- |
| **[Group]** / `group-goal` | The shared assignment or cohort outcome. See the complete task map below; #4 remains conditional. | At most one coordinator, named by a maintainer. Students join through their Individual tasks. | A maintainer checks the group's acceptance criteria and required student contributions. One student's completion does not close the group. |
| **[Individual]** / `individual-task` | One student's agreed work package under a Group goal. | Exactly one student owner before work begins; name helpers and a reviewer in the body. | The student's own acceptance criteria and evidence are reviewed. Other students' unfinished tasks do not hold this task open. |

A Group goal's assignee coordinates the shared work; they do not own everyone else's
contribution. An unassigned goal/task stays explicitly unassigned until a maintainer
confirms a person. No student roster or reviewer is assumed in advance.

## Complete task and assessment map

**Every student owns their work; no student completes every Group goal alone.**
Start with your onboarding task under #5 and starter task under #1. Agree later
work at the relevant checkpoint instead of creating the whole semester's tasks now.
An Individual task is a separate GitHub issue with a parent link, not a checkbox
inside someone else's issue. Native sub-issues are optional.

| Work / assessment | Parent goal or tracker | Who does it? | Checkpoint |
| --- | --- | --- | --- |
| Onboarding and profile (access/attribution; not a research score) | [#5](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/5) | Every student, own task and introduction PR | M1, September 25 |
| Starter attempt and critique | [#1](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/1) | Every student, own attempt/evidence | M1, September 25; Foundation evidence reviewed by M2 |
| Literature and bounded reproduction | [#2](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/2), [#6](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/6) | Divide scoped work across students; not every student does both | M2, October 9 |
| Candidate feasibility, question, and protocol | [#3](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/3) | Every student has an agreed design contribution; cohort selects one study | M2, October 9 |
| Research-question presentation — **10% shared** | [#21](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/21) | One cohort deck; every student has an agreed preparation/presentation role | M2, October 9, before #3 selection |
| Selected-study implementation and evidence | [#7](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/7), [#8](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/8); [#4](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/4) only if activated | Divide substantive work, each student accountable for their part | M3 October 16 / M4 October 30 |
| Final written report/reproducibility — **10% shared** | [#9](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/9) | One cohort report; divide writing, analysis, checking, and handoff | Draft November 6; M5 November 20 |
| Final presentation — **10% shared** | [#22](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/22) | One cohort deck; every student has an agreed preparation/presentation role | M5, November 20 |
| Individual contribution report — **10% individual** | [#23](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/23) | Every student writes their own report and opens their own report task | Draft November 6; M5 November 20 |
| Individual research work — **50% individual** | Own tasks under the research goals above | Every student: Foundation 10, Question 10, Execution 20, Synthesis 10; agree distinct outputs | Four stage checkpoints in the [rubric](grading-proposal.md#how-the-individual-50-maps-to-issues) |
| Collaboration/review — **10% individual** | Existing tasks, reviews, and portfolio; instructor checks in [#24](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/24) | Every student records useful reviews, communication, and follow-through | Ongoing; reviewed at checkpoints |
| Confirm policy, slots, scope reviews, and private assessment | [#24](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/24) | Instructor/maintainer; no student tasks under this administrative issue | M1 through announced assessment cutoff |

Milestones are **date-based collections and review gates**, not additional student
assignments. M1 groups #1/#5; M2 groups #2/#3/#6/#21; M3 uses #7 (and #4 only if
activated); M4 uses #8; M5 groups #9/#22/#23. #24 spans the semester and is tracked
through M5, with explicit earlier check-ins in its checklist. The November 6 draft
checkpoint is in #9/#23; it does not need a duplicate milestone issue.

Use one primary parent per Individual task. If your existing #3 task includes your
question-presentation role, #21 can link it; do not open a duplicate just to fill a
second list. The same applies to #9 work supporting #22. Each individual report has
its own task under #23 so its submission/review is visible separately; if one was
already opened under #9, update its parent and cross-link it instead of recreating it.
Routine review comments need no extra issue; a substantial planned review package
can be a task under the relevant research goal. Evidence may support different
assessment criteria, but the same output is not scored twice within the 50% work budget.

The [grading scheme](grading-proposal.md) remains tentative until instructor
confirmation. The **Group** label on #23 means collection/coordination, not a shared
report or shared grade. Keep all scores and private feedback out of GitHub.

## Same assignment, separate attempts

Example only; Student A and Student B below are not actual assignments:

```text
[Group] #1 — Reproduce and critique the scripted starter
  ├─ [Individual] Student A — My starter reproduction and critique
  │    owner: A; evidence: A's commands, output/error, and critique
  └─ [Individual] Student B — My starter reproduction and critique
       owner: B; evidence: B's commands, output/error, and critique
```

Both students may run the same configuration or study the same paper. They submit
their own attempt and explanation, and each task is reviewed separately. Agreement
between results is fine; a different answer or unique topic is not required. Mark
these tasks **Independent attempt** and link any sources or assistance used. Do not
close a second student's planned attempt as a duplicate merely because its topic matches.

The starter attempt is for every student. Other repeated work needs an agreed purpose,
such as an independent reproduction, comparison, or learning task; confirm it with
the maintainer before spending effort. Repeating a task does not earn automatic credit.

## Working together on one output

For a shared code change, dataset, analysis, or report, each student has their own
Individual task describing their part. Mark it **Contribution to shared work** and
link the other students' tasks. For example, under #7 one student owns case/label
construction and another owns runner implementation and tests.

Pair work can produce one shared artifact or PR. Each task identifies what its owner
actually contributed and links the common evidence. Credit both people where justified;
do not describe joint work as two independent attempts. Incidental help or a review
comment can be credited directly without creating another task. Use one task per
meaningful work package, not per commit, comment, or small edit.

## Student steps

1. Open the relevant **Group goal** and propose your specific deliverable in a comment.
2. Use **New issue → Individual task**. Title it `[Individual] YOUR-USERNAME — outcome`.
   Include the parent goal, your username, work mode, deliverable, done criteria,
   target/check-in, and proposed reviewer. A maintainer confirms scope and assignment.
3. Post your task link in a comment on the Group goal; a maintainer adds it to the
   **Individual tasks** section. An ordinary link is sufficient; native sub-issues
   are optional. The maintainer sets the
   milestone/workstream label; conditional work such as #4 remains deferred until selected.
4. Post your short weekly evidence/next-step/blocker update in **your task**. The
   coordinator summarizes group dependencies using links; no duplicate update is needed.
5. Link your PR or other evidence and request review. Use `Closes #YOUR_TASK_NUMBER`
   only when it finishes your task, and `Relates to #GROUP_NUMBER` for the Group goal
   (replace the placeholders with actual numbers). A joint PR may close multiple
   Individual tasks only when each one's criteria are independently checked.
6. Link the task/artifact in your portfolio, describing your actual contribution.
   Keep scores and private assessment feedback in the course's private channel.

**Onboarding follows the same rule:** open an Individual task under #5, then link
your roster/profile PR with `Closes #YOUR_TASK_NUMBER` and `Relates to #5`. Choose
Independent attempt, M1, and Documentation / onboarding; state “Onboarding” as the
component. Done means your roster/profile PR is reviewed and merged. No research
result is required for this task. If your introduction PR already exists or is
merged, link it as evidence; do not submit it again. For the starter reproduction,
use a separate Individual task under #1. If you already posted your starter
evidence in #1, link that comment from your task instead of copying or rerunning it.
Report setup trouble in #1 or your task without waiting for assignment.
The starter is already an agreed assignment; you can run it while the maintainer
sets GitHub fields. Scope confirmation for new work should not delay setup help.

## Closing and credit

The coordinator keeps required task links current. Before closing a Group goal,
the maintainer checks its agreed participant coverage and shared output; open required
tasks stay visible or are explicitly re-scoped with a reason. Optional tasks do not
hold the goal open. Late joiners receive an agreed task/target without reopening every
earlier goal. Preserve each student's evidence when ownership or scope changes.

Assignment or closure alone does not establish contribution quality or a grade.
Two students can each receive credit for their own sound work under one Group goal;
credit is not a pool divided among its contributors. The [tentative grading
scheme](grading-proposal.md) defines the four individual-work stages and assessment
criteria; include the agreed stage in your task objective. Grades remain private. See [contribution records](contributors/README.md)
and the [student guide](student-start.md) for attribution and the semester roadmap.
