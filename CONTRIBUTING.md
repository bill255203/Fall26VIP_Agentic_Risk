# Contributing

This is the canonical Fall 2026 VIP workspace. New students begin with the
[student guide](docs/student-start.md). Orientation and setup support begin at the
September 18 kickoff, with onboarding targeted for September 25; no repository submission
is due at kickoff. The [semester plan](docs/semester-plan.md) and [selection guide](docs/studies/README.md)
support the tasks agreed after kickoff. No empirical study has been selected yet.

## Your first contribution

1. Follow the [student quick start](docs/student-start.md) after kickoff, with setup help as needed. Advance preparation is optional.
2. Use your own GitHub account. With repository write access, create a branch here; otherwise fork the repository and open a pull request back to this repository's `main`.
3. Follow the [enrollment guide](docs/contributors/README.md#first-contribution) to add your public roster entry. No personal profile file is required. Share only your preferred display name and GitHub username.
4. Open your own Individual task under #5, then submit the introduction PR with `Closes #YOUR_TASK_NUMBER` and `Relates to #5` (use your actual task number). No completed research result is required. A maintainer reviews onboarding and can arrange repository access separately.
5. Choose a Group goal in the current milestone and open an **Individual task** for your own work. A maintainer confirms scope and your assignment. Follow [the issue guide](docs/issue-workflow.md): two students attempting the same assignment use two tasks under the same goal.

## Workflow

Use the same task/PR workflow for onboarding and later work. An introduction PR
needs a roster change, a short introduction, its Individual task link, and
`Relates to #5`; it can omit the research interpretation and full evidence/role table.

1. Start from an Individual task with one student owner, a parent Group goal, a milestone or candidate/backlog status, acceptance criteria, and planned evidence. Name collaborators and reviewer separately. The Group goal's assignee coordinates the group; each Individual task's sole assignee owns that student's work. Introduction tasks use #5 as their parent; the [task map](docs/issue-workflow.md#complete-task-and-assessment-map) covers all deliverables and grading components.
2. Create a short-lived branch from current `main`, such as `work/12-trace-analysis`. Do not work directly on `main`.
3. Make one focused change and document assumptions. Link deliverables and substantive reviews in your Individual task. Keep the evidence there; no separate contribution log is required.
4. For code or experiment changes, run `python -m unittest discover -s tests -v` plus the relevant experiment. For documents, check references, links, and claims. CI runs for every pull request.
5. Open a pull request with its issue, milestone, evidence, and a brief attribution statement where needed. For shared work, identify each person’s part and link their tasks. No duplicate portfolio update is required.
6. Obtain review from someone other than the author. A contributor from the other subteam should review methodological changes. Resolve review discussions and pass CI before merging.
7. Merge with a **merge commit** to preserve individual commit authors. Use `Closes #123` for a completed Individual task and `Relates to #456` for its Group goal, substituting actual numbers. One student's PR does not close the Group goal. A joint PR closes each student's task only after that task's own criteria are checked.

For each active Individual task, post one short weekly update: evidence produced, next step, and blocker or decision needed. The coordinator links these updates from the Group goal as needed. Keep work status in Issues and pull requests; milestone completion records delivery. Use the [meeting guide](docs/meetings/README.md) to capture decisions and assign follow-up actions.

Organize work as `To Do`, `In Progress`, `Review`, and `Done` if a Project board is enabled. Issues and pull requests are sufficient to start. An issue should have at least one of these labels:

- `research`: literature, hypotheses, design, analysis, or writing;
- `engineering`: experimental environment or instrumentation;
- `experiment`: a configured, executed, or analyzed study;
- `bug`: behavior that contradicts the documented design;
- `documentation`: onboarding, contribution reports, presentations, or administrative documentation.

Issues marked `stretch` are optional extensions and stay outside delivery milestones until adopted through a scope decision. Finish required milestone work before starting them. A change in research scope, planned outcomes, resources, or success criteria needs a linked plan-change issue and reviewed update to the semester plan/decision log.

Issues marked `candidate` are conditional on the study-selection decision in #3.
They have no delivery milestone until selected. The selected study's necessary
tasks become required work; other candidates stay deferred. Sourced exploration,
reproduction attempts, and selection rationale are M2 work and count as contributions
even when a proposed direction is rejected.

## Make your contributions visible

The [roster](CONTRIBUTORS.md) identifies students and their GitHub accounts; Individual tasks and linked PRs record their work. Literature synthesis, experiment design, reproductions, datasets, analysis, validation, writing, reviews, and presentations all count as visible work when they link to an inspectable artifact. Commit counts and lines of code are not measures of research value or a grading rubric.

Use a commit email associated with your own GitHub account; GitHub's private `noreply` address works. Configure it for this checkout, rather than using a shared team identity. Copy the exact address from your GitHub email settings; do not guess it or put private addresses in the roster. GitHub also has [other conditions for profile contributions](https://docs.github.com/en/account-and-profile/how-tos/contribution-settings/troubleshooting-missing-contributions), including the branch and repository relationship. Task evidence and substantive review links capture work that a commit graph cannot express.

For work jointly authored in one commit, use `Co-authored-by` trailers with each person's chosen account-associated address. Confirm the credit with them first. See [GitHub's co-author instructions](https://docs.github.com/en/pull-requests/how-tos/commit-changes/creating-a-commit-with-multiple-authors). Link reviews and other contributions in the relevant tasks even when they do not justify commit co-authorship.

Keep original authors when integrating student changes. If a maintainer must cherry-pick or import work, preserve author metadata and link the original PR. Do not replace students' work with a maintainer-authored aggregate commit. If tools materially assisted the work, describe their role and what the contributor verified; credit named people only for their actual work.

## Repository review settings

`main` requires a pull request, one approving review, resolved conversations, and passing `test (3.11)` and `test (3.13)` CI checks. New commits dismiss stale approvals. Force pushes and branch deletion are disabled. The repository uses merge commits and disables squash/rebase merging to preserve the original contribution history.

Changes to workflow configuration and core research/semester policy require a code-owner review. The initial code owner is the repository owner, `@zhongnz`; update `.github/CODEOWNERS` through review when actual maintainers are appointed. No student access or role is assumed from appearing in the public roster.

The repository owner retains GitHub's administrator bypass for bootstrap or recovery while the cohort is being onboarded. Ordinary student work follows the review path. Document any exceptional bypass and its reason in the relevant issue or pull request.

## Experiment changes

A research result is reviewable only when another person can identify exactly what produced it. Include:

- the research question and hypothesis or quantity to estimate;
- the treatment, evidence groups, or comparison, including what stays fixed;
- defensible reference labels and any fault/perturbation definition where applicable;
- configuration, code revision, source data/trace revisions, and transformations;
- backend, model, prompts, sampling parameters, and seeds for new model runs;
- source records or trial traces and analysis with explicit units and denominators;
- negative results, limitations, and known threats to validity.

Do not describe deterministic fixture runs as LLM evidence. Do not treat an ideal verifier with direct access to truth as a deployable control. See [the experiment record](docs/experiment-record.md) before interpreting results.

## Code changes

- Keep the core experiment readable before adding abstractions.
- Add a focused test for behavior that could change a research conclusion or corrupt provenance.
- Never commit credentials, API keys, local `.env` files, or generated caches.
- Use synthetic or approved public data only. Do not commit personal, confidential, regulated, or proprietary data.
- Avoid adding services, frameworks, or dependencies until a concrete experiment requires them.

## Durable handoff

An issue is done when its code or document is reviewed, its validation is recorded, and its result can be located without private context. At the end of a research package, update the open questions and preserve the configuration, code, traces, findings, limitations, and next hypotheses.

Discuss authorship expectations before manuscript work begins. Use plain role descriptions in tasks and the final report’s contribution summary. CRediT labels are optional; see the [cohort guide](docs/cohort-guide.md#credit-and-authorship).
