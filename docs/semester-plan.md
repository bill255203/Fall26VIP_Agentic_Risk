# Fall 2026 semester plan

**Current approach, September 23:** one bounded case study per pair, with common
teaching resources and cross-pair review. This replaces the earlier plan to select
one cohort-wide experiment. Existing student contributions remain valid evidence.

## Semester outcome and scope

Each pair investigates **one business workflow, one risk question, and one possible
improvement**. Produce a sourced case description, a reviewed evidence plan, a small
empirical investigation, and a report with reproducible evidence and limitations.
A controlled experiment, deliberate replication, or systematic analysis of genuine
agent traces can qualify. A hypothetical risk narrative or scripted demonstration
alone does not establish empirical findings.

Ground the business use case in public policies, documented processes, or other
approved sources. Distinguish the real-world motivation from the simulated or
observational evidence actually studied. No company integration is required.

The cohort shares concepts, a guided example, a small reading core, compatible
reporting practices, reusable tools, and peer review. Pairs choose their own bounded
questions; they need not compete for one winning proposal. Agent Assurance and
external benchmarks are optional sources, not required frameworks to implement.

## Calendar and working targets

Kickoff: **September 18, 2026**. These New York local dates are **working project
targets**, not official submission cutoffs or confirmed presentation slots. The
instructor confirms course policy and adjusts scope for preparation, access, and
availability. Late joiners agree individual targets; no work is due before joining.

| Checkpoint | Target | What is expected |
| --- | --- | --- |
| **M1 — Onboard and understand** | **September 25** | Roster PR, starter attempt or recorded blocker, guided trace discussion, and one observation/question per student. |
| **M2 — Propose pair cases** | **October 9** | Confirm partners, register one Pair case, complete its short outline, assign individual contributions, and agree a feasible evidence route with a reviewer. This is a scope check, not a full finished protocol. |
| **M3 — Present cases and validate plans** | **October 16** | Each pair presents its question, business motivation, reading, evidence plan, and a small feasibility result or diagnosed limitation. Reviewer approves the revised plan and validation before final evidence work. |
| **M4 — Analyze first evidence** | **October 30** | Each pair produces a first complete analysis with counts, failures, relevant risk/utility tradeoffs, and limitations. |
| **Full draft checkpoint** | **November 6** | Pair report and individual contribution report drafts for feedback. |
| **M5 — Report and hand off** | **November 20** | Reviewed pair report/evidence, final pair presentation, individual reports, and a peer check of the handoff. |

Dates stay front-loaded while moving the former October 9 question presentation to
October 16 for guided case development. This is a proposed midterm-period slot;
actual slots remain for the instructor to confirm. The October 16 week includes the
previously noted Tandon fall-break/schedule changes; reduce workload or adjust the
slot if needed. Consult the [NYU Tandon calendar](https://engineering.nyu.edu/academics/registration/school-calendar)
and course announcements. Preserve remaining term time for agreed review and repairs;
do not create new required work during recess or exams.

## Milestones and dependencies

Each pair progresses on its own reviewed evidence. One pair's blocker does not
prevent another pair from proceeding. A cohort collection issue remains open until
all required pairs are covered, but its closure is not a prerequisite for a ready pair.

- **M1:** shared onboarding #5 and starter #1; pair formation can follow.
- **M2:** #3 registers Pair case issues. Each pair uses the [short outline](studies/README.md#short-proposal-outline).
- **M3:** #21 collects midterm decks and feedback; #7 collects validation links. Each
  pair records its approved plan revision, reviewer, data/access, and development
  check in its own case issue. Freeze evaluation data/rules before final analysis.
- **M4:** #8 collects first-analysis links. Preserve failures and deviations; counts
  and uncertainty must match the units of evidence. Do not treat repeated messages
  or repeated deterministic runs as independent observations.
- **M5:** #9 collects pair reports/handoffs, #22 final decks/discussion, and #23
  individual reports. Required outputs are reviewed separately.

Exploratory probes may precede plan approval and must be labeled exploratory.
Changes after inspecting evaluation data are recorded, with their effect on claims.
The instructor narrows scope when access or setup fails. Existing-trace analysis
requires actual accessible traces, usable labels, and a meaningful comparison;
it is not an automatic fallback based on the scripted starter.

## Instructor preparation and support

Track the teaching package in **#6** and assessment arrangements in **#24**.
Before assigning an external platform, the instructor/maintainer must:

1. Test a pinned version and a small task subset; record installation and runtime.
2. Provide exact instructions, a guided example, and permitted saved executions with
   provenance. Clearly distinguish genuine model traces from scripted fixtures.
3. Arrange model access and a bounded budget if paid runs are needed. Students are
   not expected to buy access or commit API keys.
4. Explain the workflow and one paper in plain language; offer setup help.
5. Demonstrate that another person can run or analyze the example. If not, select a
   narrower supported route before requiring it of students.

The existing starter is ready; the external-platform package is **pending**, not
implemented or funded. Tau-bench is a candidate for a text-based business example;
AgentDojo is an alternative for injection-focused questions. No integration of
multiple frameworks is required. See [resources](literature.md).

## Assessment and reports

Proposed **70% individual / 30% pair**:

- Individual: work **50** (Foundation 10, Question 10, Execution 20, Synthesis 10),
  collaboration/review **10**, contribution report **10**.
- Pair: midterm case/question presentation **10**, final report and evidence **20**.
- Final pair presentation remains a required communication/handoff activity, with
  feedback but **no separate grade weight** in this proposal.

The instructor must confirm this revised breakdown before applying it. See the
[grading proposal](grading-proposal.md); an issue closure is not a grade. Keep marks
and private feedback outside GitHub. The final report is shared within the pair,
not graded across the entire cohort.

## Responsibility and student visibility

Each pair shares responsibility for its case and rotates research/technical roles
where practical. Each student owns a reviewable contribution in all four stages;
agree scope suited to enrolled commitment and experience. There are no permanent
Research versus Engineering subteams. Both partners explain the evidence and method.
The instructor confirms pair membership, scope, reviewers, access, and assessments.
No partner or reviewer is assigned without agreement.

Use [Pair cases and Individual tasks](issue-workflow.md). Record work once in Issues
and PRs; no weekly slide deck, portfolio table, or separate activity log is required.
Existing #28/#30 and PR #29 remain valid onboarding/starter records.

## Weekly rhythm

The [weekly student goals](student-start.md#weekly-goals) elaborate this schedule.
Each student posts a short evidence/next-step/blocker update in their active task.
Use cohort meetings for a trace discussion, a useful finding, blockers, and feedback
across pairs. Reuse tasks across weeks. Agree a small next deliverable and offer help
before adding scope. Weekly targets do not add graded submissions or assumed hours.

## Changes and definition of done

Use a reviewed PR and [decision log](decisions.md) for program changes; case-specific
amendments stay in the pair's document and issue, preserving prior versions and
identifying affected evidence. A pair finishes when its reviewed report, evidence,
individual tasks, presentation, and handoff are linked. Unfinished work stays visible.
The cohort leaves an index of pair reports and reusable assets, not an extra combined
research paper. See [reports](reports/README.md).
