# Pair cases, cohort goals, and Individual tasks

**One shared case per pair; one owner per Individual task.** Issues and PRs are the
contribution record. Do not create an issue for every meeting, comment, or weekly update.

## Which issue do I create?

| Issue type | Purpose | Ownership and completion |
| --- | --- | --- |
| **Pair case** | One pair's workflow, question, plan, report links, and milestone checklist for the semester. Create after partners agree; register its link in [#3](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/3). | Names both partners and a reviewer. Both may be assigned. Stays open until the case outputs are reviewed. Assignment alone does not allocate individual credit. |
| **Individual task** | One student's meaningful contribution or independent attempt. | Exactly one student owner; separate evidence and review. Name collaborators separately. |
| **Group goal** | Existing cohort onboarding, shared resources, or collection of outputs across pairs. | Maintainer coordinates required coverage; it is not a single research project or cohort-wide grade. |
| **Instructor task** | Teaching setup, access/budget, assessment and support. | Instructor/maintainer owns it. Students are not automatically responsible for preparing the platform. |

GitHub calls the templates **Pair case**, **Individual task**, and **Group goal (maintainer)**.
The parent is an issue link in the form; native GitHub sub-issues or a Project board
are optional. No multi-select enrollment field is needed. Multiple assignees on a
pair issue identify partners; personal credit still comes from one-owner tasks.

## Simple student workflow

1. Onboard with your Individual task under [#5](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/5) and starter task under [#1](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/1).
2. When partners are confirmed, **one partner** opens **New issue → Pair case**,
   names both partners, and links it in [#3](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/3). A maintainer confirms membership, reviewer,
   and scope. Choose a stable short slug such as `retail-refunds`.
3. Each partner opens **Individual tasks** under that Pair case for their meaningful
   work. Include stage, deliverable, done criteria, target, and reviewer. Reuse a task
   across weeks; no minimum number of tasks is required.
4. Link the artifact and review in the Individual task. Update the Pair case with
   links to its outputs; cohort collection goals link those same outputs.
5. A PR uses `Closes #YOUR_INDIVIDUAL_TASK` only when complete and `Relates to
   #YOUR_PAIR_CASE`. A joint PR may close multiple personal tasks after each is
   checked. It must not automatically close the pair or a cohort collection goal.
6. Write your individual report under [#23](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/23) and link it from the Pair case as well.

A task has **one primary parent**. Related goals may link it without requiring a
second task. Shared resource work can belong directly to [#2](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/2), [#6](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/6), or [#7](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/7) when agreed;
link it from the benefiting pair. Assignees/labels/milestones can be set by a
maintainer; missing edit permissions do not prevent starting agreed work.

## Multiple students doing the same assignment

Any number of students may independently do the same agreed assignment. Each uses
a separate Individual task under the same parent, with their own evidence and review.
They can each earn full individual credit; credit is not divided between assignees.
For example, starter critiques from several students belong under [#1](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/1).

Partners doing joint work choose **Contribution to shared work**, describe their
actual parts, and link each other's tasks. They may use the same code, table, or PR.
Do not describe a joint artifact as independent results. A planned replication by
another pair needs an agreed purpose; there is no requirement that every topic differ.

## Complete task and assessment map

Cohort issues are retained to keep existing links and show coverage. Students do
**not** open tasks under every row. Most research work belongs under the Pair case.

| Work / output | Primary student task parent | Cohort coordination / target | Proposed assessment |
| --- | --- | --- | --- |
| Roster and onboarding | [#5](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/5) | [#5](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/5); M1 Sep 25 | Access/attribution; setup alone is not research credit |
| Starter attempt and critique | [#1](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/1) | [#1](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/1); M1 Sep 25 | Foundation evidence |
| Reading / business workflow | Pair case (or [#2](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/2) for shared resources) | [#2](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/2) resources; M2 Oct 9 | Foundation 10 |
| Question and evidence plan | Pair case | [#3](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/3) case registry; outline M2, reviewed plan M3 Oct 16 | Question 10 |
| Guided platform / trace package | Instructor [#6](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/6); agreed student help may have a task under [#6](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/6) | [#6](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/6) before requiring platform use | Student credit only for actual agreed work |
| Feasibility and execution | Pair case | [#7](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/7) validation; M3 then M4 | Execution 25 |
| Analysis | Pair case | [#8](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/8) first analysis; M4 Oct 30 | Execution or Synthesis; distinct outputs, no double counting |
| Midterm case/question presentation | Pair case; reuse design task if it covers the role | [#21](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/21) collects each pair's deck/feedback; M3 Oct 16 | Pair 10 |
| Final report and reproducible evidence | Pair case | [#9](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/9); draft Nov 6, final M5 Nov 20 | Synthesis 10 individually; integrated pair package 15 |
| Final presentation | Pair case; reuse report task if it covers the role | [#22](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/22); M5 Nov 20 | Required, feedback only; no separate weight |
| Individual contribution report | [#23](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/23); cross-link Pair case | [#23](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/23); draft Nov 6, final Nov 20 | Individual 10 |
| Collaboration and substantive peer review | Existing relevant task; substantial review package may have its own task | Ongoing, with cross-pair review before M5 | Individual 10 |
| Course policy, support, private assessment | Instructor [#24](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/24); students do not open tasks for course administration | Checkpoints through official cutoff | Private instructor assessment |
| Candidate A practical gate | Pair case only if explicitly adopted; related [#4](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/4) | [#4](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/4) deferred, no delivery milestone | Optional scope; no additional points |

The [grading proposal](grading-proposal.md) defines the rubric and stage boundaries.
The two assessments of individual contribution and integrated pair output serve
different purposes; closing issues does not award points.

## Who reviews what?

- **Personal task:** an agreed reviewer other than its owner checks the evidence;
  a partner can provide this review. A substantial cross-pair review is useful too.
- **Study plan and method changes:** the instructor or a designated method mentor
  records approval. Partner agreement alone does not approve the final evidence plan.
- **Final handoff:** another pair or an instructor checks the analysis/source trail.
- **PR merge:** an eligible GitHub reviewer approves according to [access rules](access-management.md).
  Peer feedback and study-plan approval do not automatically grant merge permissions.
- **Grades:** the instructor assesses evidence privately using announced policy.

## Milestones, review, and closing

Each Individual task uses the milestone for its next agreed output. A semester-long
Pair case uses M5 and keeps its M2–M5 checklist in the body; do not create five
separate pair issues. Cohort collectors use their relevant milestone. Milestones
organize work, not new assignments.

A reviewer checks a student's evidence separately from the pair's overall progress.
The pair may proceed after its own plan/validation review without waiting for the
cohort's [#3](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/3)/#7 to close. A maintainer closes collection goals only after every required
participant/pair is covered or an explicit scope adjustment is recorded.

Use one short weekly update in each active task: evidence, next step, blocker. Keep
completed links visible. No duplicate portfolio, public gradebook, or weekly report.
When a partner or dependency blocks progress, preserve the existing work and agree
an alternative scope with the instructor. Late joiners get agreed targets.

## Transition from the previous plan

Existing student [#28](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/28), [#30](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/30), and PR [#29](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/pull/29) remain valid. Do not rewrite student-authored
records or require resubmission. Existing research tasks can be re-parented by agreement,
with a note and original evidence retained. Previous cohort goals become coordination
and output collections; [#4](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/4) stays optional. No pair membership or completed result is
inferred from an old assignment. Confirm partners in [#3](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/3) before creating a Pair case.
