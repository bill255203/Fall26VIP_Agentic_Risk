# Student guide: kickoff through handoff

You can read and clone this public repository immediately. To contribute, use your own GitHub account; your first pull request adds you to the visible roster. A pull request (PR) is a proposed change that someone else reviews before it joins the shared project.

Jump to: [setup](#1-clone-and-run) · [first contribution](#2-make-your-first-visible-contribution) ·
[weekly goals](#weekly-goals) · [weekly workflow](#every-week-work-share-evidence-and-get-review) ·
[resources](#resources-what-to-read-and-where-to-save-work).

You do not need write access to start: use your own fork and ask a maintainer to
set issue fields. Peer feedback is welcome; required merge approval comes from an
eligible reviewer. See [access and protection](access-management.md).

## First meeting: September 18, 2026

No repository submission is due at kickoff. The meeting includes a project
introduction, a starter demonstration, and a check of students' Git/Python experience,
interests, and access needs. Setup support is part of onboarding.

At the meeting, share an interest or question and any setup/access difficulty.
Agree with a maintainer on a small first task and who can help. The instructor
provides meeting logistics and course policies through the course's usual channels.

**By Friday, September 25 (M1), each student should:**

- Open your **Individual onboarding task** under #5, then an introduction PR with your roster row, following steps 2–3; link your task and [#5](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/5).
- Try the starter in step 1. Open an **Individual task** under [Group goal #1](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/1), with your command, result or exact setup error, and one observation/question. Link any evidence already posted in #1 instead of copying or rerunning it; remove private paths or credentials before posting. Setup help does not wait for assignment.
- Agree one small next task and record your name/handle and deliverable in your Individual task. If blocked, say what help you need so a maintainer can help or adjust your task.

The cohort shares the later literature and reproduction work; each student starts
with a scoped task. The [semester plan](semester-plan.md#calendar-and-working-targets)
sets the milestones from kickoff, while the [selection guide](studies/README.md)
explains how the cohort chooses its study.

**Multiple students may do the same assignment independently.** Each opens their own
Individual task under the same Group goal, with separate evidence and review.
Use [Group goals and individual tasks](issue-workflow.md) for examples and the
steps to claim work, including onboarding under #5. The [complete task map](issue-workflow.md#complete-task-and-assessment-map) identifies every deliverable, assessment component, parent issue, and checkpoint. You do not need a task under every Group goal.

## Your individual responsibilities and tentative grading

Use the [tentative 70% individual / 30% group scheme](grading-proposal.md) to plan
your work. The instructor confirms the final course policy and submission details.

- **50% individual work:** Foundation **10**, Question/protocol **10**, Execution
  **20**, and Synthesis/handoff **10**. Agree a substantive contribution in each
  stage through your own Individual tasks; include the stage in each task's objective.
  The [rubric](grading-proposal.md#one-scoring-rubric-applied-to-each-stage) assesses
  quality, reasoning, and evidence. More issues or commits do not earn more points.
- **10% individual collaboration/review:** keep agreed commitments, communicate
  blockers, and give useful, evidence-linked feedback.
- **10% individual contribution report:** explain your own responsibilities,
  decisions, evidence, collaboration, and learning. Write your report
  using the [report template](contributors/_individual-report-template.md);
  draft November 6, final November 20. No second weekly activity log is needed.
- **30% shared group work:** research-question presentation **10**, final written
  report/reproducibility **10**, and final presentation **10**. The whole cohort
  creates these outputs together; agree and record each student's part.

Multiple students doing the same assignment independently can each earn full individual
credit through separate tasks and evidence. Joint work must identify each person's
actual contribution. Grades and private feedback stay outside GitHub.

## Throughout the project

The dates below are **2026 working project targets** from the [canonical schedule](semester-plan.md#calendar-and-working-targets).
M1–M5 are shared checkpoints. A **protocol** is the agreed study plan: the question,
comparison, data, measures, and analysis. Freezing it means recording a reviewed
version before the evidence collection or analysis used for final claims.
Each student owns an agreed part of the shared work and reviews another contributor's
work as agreed with the task owner. The cohort produces one study and one report;
you are not expected to complete every row's deliverable alone. Issue numbers in
the tables below are Group goals: put personal work in your linked Individual task;
the group collects those links and produces the combined output.

### Weekly goals

Weeks below end on Fridays and count from the September 18 kickoff; **Week 1 ends
September 25**. No work was due at kickoff. Use the row for the current week to
agree your next achievable contribution with your reviewer. The dates are planning
targets, not additional weekly graded submissions or confirmed meeting times.

| Week ending / focus | Your individual goal and evidence | Shared cohort outcome / parent goals |
| --- | --- | --- |
| **Week 1 — September 25: onboard and critique (M1)** | Open your onboarding and starter tasks. Submit your roster PR; try the starter and link your command, result/error, and one observation or limitation. Agree one small next task and who can help. | Onboard in [#5](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/5); review a shared trace walkthrough and setup blockers in [#1](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/1). Assign initial reading/probe roles and someone to start the shared report outline in [#9](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/9). |
| **Week 2 — October 2: explore and test feasibility** | Complete an agreed reading, reproduction, or feasibility slice. Link sources/commands, a finding or diagnosed blocker, and what it means for a possible question. You do not need to do every type of task. | Combine literature notes in [#2](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/2), the bounded published reproduction in [#6](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/6), and candidate outlines/probes in [#3](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/3). Identify access gaps early; develop at most two candidate questions. |
| **Week 3 — October 9: compare, present, and select (M2)** | Finish your agreed design contribution: for example a candidate comparison, probe, metric definition, or analysis plan. Link the reasoning/evidence and prepare your part of the question presentation. Agree your selected-study execution task and reviewer. | Give one research-question presentation in [#21](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/21); then the cohort and method lead record one selected question and reviewed frozen protocol in [#3](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/3). Review Foundation and Question evidence. Feedback that prevents approval keeps the gate open. |
| **Week 4 — October 16: build and validate (M3)** | Once #3 is approved, implement or validate your scoped part—code, data, labels, scenarios, or analysis tooling. Link development checks, failures, and reproducible commands; report access/capacity blockers promptly. | Validate the smallest end-to-end selected study in [#7](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/7) and freeze evaluation data before confirmatory work. Activate [#4](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/4) only if Candidate A is selected. Plan around the existing fall-break/schedule-change caveat in the semester plan. |
| **Week 5 — October 23: produce and check early evidence** | After the M3 gate passes, complete an agreed first evidence batch or analysis slice. Link artifacts, provenance, counts, failures, and an early interpretation labeled provisional. If collection is blocked, agree a useful validation or analysis-preparation task. | In [#8](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/8), check that the protocol can produce interpretable evidence and that the analysis works; expose missing data, access, or quality problems while there is time to address them. Record any protocol amendment before affected work. |
| **Week 6 — October 30: complete planned evidence and analysis (M4)** | Finish your agreed Execution deliverable and address its review. Link the planned evidence, appropriate comparisons/uncertainty, failures, deviations, and limitations. Agree your remaining Synthesis contribution. | Complete the first full analysis in [#8](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/8) and have an assigned peer reproduce it. Identify which claims the evidence supports and which remain unresolved; carry those limits into the shared report. |
| **Week 7 — November 6: write the drafts** | Draft or review your assigned group-report section with evidence links. Draft your own individual contribution report under [#23](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/23), explaining your work, decisions, collaboration, and learning using existing tasks/PRs. | Assemble the full shared technical report in [#9](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/9); collect individual drafts in #23. Agree reviewers and preparation/presentation roles for the final shared presentation in [#22](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/22). |
| **Week 8 — November 13: reproduce, review, and revise** | Resolve feedback on your assigned work and individual report. Complete an agreed peer review or reproduction check, link the result or problem, and prepare your part of the final presentation. | Check the report's claims and handoff instructions in [#9](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/9), review individual reports in [#23](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/23), and rehearse the presentation in [#22](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/22). Record remaining corrections and owners. |
| **Week 9 — November 20: present and hand off (M5)** | Finalize your individual report and any agreed synthesis/handoff work; link the reviewed evidence in your task. Deliver your agreed presentation role, confirm accurate credit, and document unfinished work. | Finish the shared report/reproduction package in [#9](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/9), final presentation in [#22](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/22), and individual report collection in [#23](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/23). Review all required evidence before closing M5; a date alone does not complete a goal. |

**Use your existing task.** A task may span multiple weeks; update its next check-in
instead of opening another issue just because the week changed. Each student owns
their part, while the cohort divides the shared output. Research and Engineering
roles can both meet these goals; not everyone needs to code, reproduce every paper,
or write a separate slide deck.

If a prerequisite is unfinished, state the blocker and agree a smaller scope,
alternative useful task, or revised target with the method lead. Do not start
confirmatory evidence work before protocol approval, M3 validation, and the required
data freeze. Update the [canonical plan](semester-plan.md#calendar-and-working-targets)
and affected issues if a milestone changes. Late joiners agree a feasible individual
entry plan rather than being assigned every past week's work.

The question presentation targets **October 9** and the final presentation targets
**November 20**; the instructor confirms actual slots, length, and submission routes.
After handoff, use remaining term time for instructor-agreed review or repairs.
No required project work is scheduled during Thanksgiving recess, November 26–27. Raise a missed target or access
blocker in the relevant issue early; the method lead records any change to scope or dates.
Late joiners agree an individual onboarding target and join the current shared work.

## Every week: work, share evidence, and get review

1. **Agree the week's goal.** Use the weekly row and continue your existing Individual
   task, setting the next deliverable and check-in. Open a new task only for a new
   meaningful work package, with its Group goal, work mode, reviewer, and scope.
   A maintainer confirms assignment; you can comment even if you cannot assign yourself.
2. **Keep evidence.** Save source links, commands, findings, or exact errors as you work.
   Post one short weekly update in your task: **evidence produced; next step; blocker/help needed**.
   Link review feedback when relevant. A useful diagnosed blocker is honest progress;
   no extra weekly report, portfolio log, or new grading component is required.
   The coordinator summarizes group progress using links to the individual tasks.
3. **Submit for review.** Put a small code/document change in a PR linked to the issue.
   Address comments on the same branch; review a peer's work as agreed. A maintainer
   closes your task when its criteria are met and the Group goal when the required
   individual contributions and combined output are reviewed.
4. **Keep credit visible in the same task.** Identify your actual part, collaborators,
   and relevant review links alongside your evidence. No portfolio table or second
   weekly log is required. Use these links when writing your individual report.

For setup questions, comment in #1; for roster/PR help, use #5; for a research,
data, or model-access blocker, use your task issue (#3 before selection).
Include what you tried and the error or decision needed. Bring unresolved blockers
to the next meeting. Private information belongs in the instructor's course channel.

## Resources: what to read and where to save work

| Your task | Start here | Record the outcome here |
| --- | --- | --- |
| Understand the project and schedule | [README](../README.md), [semester plan](semester-plan.md), [cohort roles](cohort-guide.md) | Your task's issue; agreed changes in the [decision log](decisions.md). |
| Understand assessment and prepare your individual report | [Tentative grading scheme](grading-proposal.md), [rubric](grading-proposal.md#one-scoring-rubric-applied-to-each-stage), [report template](contributors/_individual-report-template.md) | Agree stages in your own tasks; link existing task/PR evidence; keep scores and private feedback in the course channel. |
| Claim work or attempt the same assignment as a classmate | [Group goals and individual tasks](issue-workflow.md) | Your own Individual task, linked to the parent Group goal; one student owner per task. |
| Set up Git/Python and run the starter | Steps 1–3 below and [run commands](../README.md#run-the-pilot) | #1 for commands/results/help; #5 for your intro PR. |
| Find papers, datasets, benchmarks, or tools | [Literature guide](literature.md): propagation and containment, failure attribution, AgentDojo, Inspect, CAGE, and other starting points | Short source-linked notes in #2; PRs to the literature guide for reviewed synthesis. Pick sources for your assigned question; this is not a mandatory reading list. |
| Propose a question or test feasibility | [Five-part outline](studies/README.md#short-proposal-outline), [Candidate A example](studies/01-runtime-containment.md), [Agent Assurance source map](agent-assurance-bridge.md) | #3 for proposals and probes; the selected protocol goes in `docs/studies/` through review. |
| Build, test, or analyze | [Code](../src/agentic_risk/), [configurations](../experiments/), [tests](../tests/), [research methods](research-plan.md), [experiment record](experiment-record.md) | PR linked to #7/#8, with exact commands and artifact links. The selected protocol determines the implementation. |
| Save data and results | [Results policy](../results/README.md) and [experiment record](experiment-record.md) | Generated runs stay in ignored `results/local/`. Share concise evidence in the issue; commit only reviewed snapshots or document an accessible approved storage location and revision. |
| Write, review, and hand off | [Report outline](reports/README.md), [meeting guide](meetings/README.md), [contribution guide](../CONTRIBUTING.md) | Report PRs in #9; actual meeting notes in `docs/meetings/`; evidence links in your Individual tasks; [individual reports](contributors/README.md) under #23. |

Resources linked from the literature guide are starting points to evaluate; access
to a particular dataset, service, or model is not assumed. The scripted starter needs
no API key. Agree any paid-model access and budget with the instructor before spending.

## 1. Clone and run

Install Git and Python 3.11 or later, then follow the [README run commands](../README.md#run-the-pilot). They clone the official repo, create an isolated Python environment, install the package, and run the pilot. No model account or API key is needed for the starter.

The checks should report 10 passing tests. The default pilot produces 480 scripted trials and 12 summary rows. Look at `results/local/pilot/summary.csv`, then read one trial from `trials.jsonl`. Local output stays on your computer; record a concise reproduction note when it becomes part of a task.

This runnable starter is a deterministic mechanism check that gives the cohort a shared setup and trace format. It does not choose the semester's research question. [Candidate A](studies/01-runtime-containment.md) is a proposed runtime-containment study, not an implemented or preselected continuation of the starter.

## 2. Make your first visible contribution

On [the repository page](https://github.com/zhongnz/Fall26VIP_Agentic_Risk), click **Fork** to create a working copy in your GitHub account. The official repository remains the shared destination for everyone's work. Forking lets you contribute before being invited as a collaborator.

In the clone you already made, replace `YOUR-USERNAME` with your own GitHub username:

```bash
git switch -c onboarding/YOUR-USERNAME
git remote add fork https://github.com/YOUR-USERNAME/Fall26VIP_Agentic_Risk.git
```

Add one row to [CONTRIBUTORS.md](../CONTRIBUTORS.md) with your preferred public
name and GitHub profile link, following the [enrollment guide](contributors/README.md#first-contribution).
Your username is enough as a display name. Your first PR only needs this roster
change; no personal profile file, report, or research result is required.

Before committing, set your Git author name and account-associated email in this repository. A GitHub `noreply` address keeps your email private; copy the exact value from your account's email settings. See [the attribution guide](../CONTRIBUTING.md#make-your-contributions-visible).

Replace the placeholders before running:

```bash
git config user.name "Your preferred public name"
git config user.email "YOUR-EXACT-GITHUB-NOREPLY-ADDRESS"
```

```bash
git add CONTRIBUTORS.md
git commit -m "Add my Fall 2026 roster entry"
git push -u fork onboarding/YOUR-USERNAME
```

If Git asks you to authenticate, use GitHub Desktop's sign-in or GitHub CLI's `gh auth login`. The [GitHub authentication guide](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github) covers the available methods.

## 3. Open a pull request

GitHub shows a **Compare & pull request** link after you push. Choose **base repository** `zhongnz/Fall26VIP_Agentic_Risk`, **base** `main`, and your fork/branch as the source. Describe what you changed, name the current milestone (**M1** during kickoff), and link the [onboarding issue](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/5) with `Relates to #5`, plus `Closes #YOUR_TASK_NUMBER` for your own completed onboarding task (replace with its actual number). Do not close the whole cohort's onboarding issue for one person's enrollment. If you cannot edit GitHub's milestone or assignee fields, put the information in the PR description and a maintainer will set them.

A maintainer reviews the PR. If they request edits, make another commit on the same branch and push it; the PR updates automatically. CI for a first-time fork contributor may wait for a maintainer to approve running it. Once merged, your roster entry and original commit appear in the canonical repository.

For a documentation-only first contribution, you can also use GitHub's browser editor in your fork: edit the roster, then open a PR. GitHub Desktop is another option if you prefer a graphical Git interface.

## 4. Pick a small task and keep the evidence

Choose a Group goal in the current [milestone](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/milestones), then use **New issue → Individual task** for your own deliverable. Follow [the issue guide](issue-workflow.md). Start with reproducing the pilot, exploring or critiquing a proposed question, checking a source or feasibility assumption, a test, or a documentation improvement. Name your own part and agree its scope with a maintainer. Research and writing are visible contributions too.

Follow the [selection and protocol guide](studies/README.md#selection-and-protocol).
Reading, critique, and feasibility checks lead to the M2 review of at most two
developed cohort proposals. Candidate A may be selected, revised, or rejected;
other feasible agentic-risk questions can qualify.

A sourced exploration, substantive critique, bounded reproduction attempt, or
reasoned rejection is useful work when linked to evidence. If you join later,
use the same onboarding path and agree an individual setup target with a maintainer
while taking a bounded current task. The cohort's [schedule](semester-plan.md#calendar-and-working-targets)
continues; new students are not expected to complete work before joining.

Keep evidence and review links in your Individual task. For shared work, say who
did what. At the report checkpoints, use those links to explain your contributions
in the [individual report](contributors/README.md#individual-contribution-report).
No separate ongoing contribution table is required.

Before starting the next branch, update from the official repository with a clean working tree:

```bash
git switch main
git pull --ff-only origin main
git switch -c work/ISSUE-NUMBER-short-description
```

Replace `ISSUE-NUMBER-short-description` with the task number and a few words. Push future work to `fork` and open PRs back to the official `main` in the same way. The [semester plan](semester-plan.md) explains what the cohort is delivering and when; [CONTRIBUTING.md](../CONTRIBUTING.md) covers the full review process.
