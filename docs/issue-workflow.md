# Group goals and individual tasks

**Two students can complete the same assignment independently. Each student uses
a separate Individual task linked to the same Group goal.** Each task has its own
owner, evidence, review, and completion status.

## Two kinds of issue

| Kind | Purpose | Who is assigned? | When is it closed? |
| --- | --- | --- | --- |
| **[Group]** / `group-goal` | The shared assignment or cohort outcome. Existing issues #1–#9 are Group goals; #4 remains conditional. | At most one coordinator, named by a maintainer. Students join through their Individual tasks. | A maintainer checks the group's acceptance criteria and required student contributions. One student's completion does not close the group. |
| **[Individual]** / `individual-task` | One student's agreed work package under a Group goal. | Exactly one student owner before work begins; name helpers and a reviewer in the body. | The student's own acceptance criteria and evidence are reviewed. Other students' unfinished tasks do not hold this task open. |

A Group goal's assignee coordinates the shared work; they do not own everyone else's
contribution. An unassigned goal/task stays explicitly unassigned until a maintainer
confirms a person. No student roster or reviewer is assumed in advance.

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

**Introduction-only PRs are the one onboarding exception:** add your roster/profile
and use `Relates to #5`; no separate Individual task is needed. For the starter
reproduction, use an Individual task under #1. If you already posted your starter
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
