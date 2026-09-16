# Student quick start

You can read and clone this public repository immediately. To contribute, use your own GitHub account; your first pull request adds you to the visible roster. A pull request (PR) is a proposed change that someone else reviews before it joins the shared project.

## Before and after the first meeting

Before the first meeting, browsing the README or trying the starter is optional.
There is no repository submission due before we meet. The kickoff includes a project
introduction, a starter demonstration, and a check of students' Git/Python experience,
interests, and access needs. Setup support is part of onboarding.

Your first-week checklist, with a full week after kickoff:

- Open an introduction PR with your roster row and profile, following steps 2–3.
- Try the starter in step 1 and save the result or exact setup error for help.
- Bring one observation or question, and agree on one small next task.

The cohort shares the later literature and reproduction work; each student starts
with a scoped task. The [semester plan](semester-plan.md#calendar-and-working-targets)
sets the milestones from kickoff, while the [selection guide](studies/README.md)
explains how the cohort chooses its study.

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

Use the [portfolio template](contributors/_template.md) to create `docs/contributors/YOUR-USERNAME.md`. Fill in your public display name, GitHub link, and interests. Add your row to [CONTRIBUTORS.md](../CONTRIBUTORS.md). Your username alone is enough as a display name. Your first PR can just introduce you; no research result is required.

Before committing, set your Git author name and account-associated email in this repository. A GitHub `noreply` address keeps your email private; copy the exact value from your account's email settings. See [the attribution guide](../CONTRIBUTING.md#make-your-contributions-visible).

Replace the placeholders before running:

```bash
git config user.name "Your preferred public name"
git config user.email "YOUR-EXACT-GITHUB-NOREPLY-ADDRESS"
```

```bash
git add CONTRIBUTORS.md docs/contributors/YOUR-USERNAME.md
git commit -m "Add my Fall 2026 contributor profile"
git push -u fork onboarding/YOUR-USERNAME
```

If Git asks you to authenticate, use GitHub Desktop's sign-in or GitHub CLI's `gh auth login`. The [GitHub authentication guide](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github) covers the available methods.

## 3. Open a pull request

GitHub shows a **Compare & pull request** link after you push. Choose **base repository** `zhongnz/Fall26VIP_Agentic_Risk`, **base** `main`, and your fork/branch as the source. Describe what you changed, name the current milestone (**M1** during kickoff), and link the [onboarding issue](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/5) with `Relates to #5`. Do not close the whole cohort's onboarding issue for one person's enrollment. If you cannot edit GitHub's milestone or assignee fields, put the information in the PR description and a maintainer will set them.

A maintainer reviews the PR. If they request edits, make another commit on the same branch and push it; the PR updates automatically. CI for a first-time fork contributor may wait for a maintainer to approve running it. Once merged, your roster/profile and original commit appear in the canonical repository.

For a documentation-only first contribution, you can also use GitHub's browser editor in your fork: create the profile, edit the roster, then open a PR. GitHub Desktop is another option if you prefer a graphical Git interface.

## 4. Pick a small task and keep the evidence

Choose a task in the current [milestone](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/milestones). Start with a scoped part of reproducing the pilot, exploring or critiquing a proposed question, checking a source or feasibility assumption, a test, or a documentation improvement. Identify yourself and collaborators in its issue and agree the deliverable with a maintainer. Research and writing are visible contributions too.

Follow the [selection and protocol guide](studies/README.md#selection-and-protocol).
Reading, critique, and feasibility checks lead to the M2 review of at most two
developed cohort proposals. Candidate A may be selected, revised, or rejected;
other feasible agentic-risk questions can qualify.

A sourced exploration, substantive critique, bounded reproduction attempt, or
reasoned rejection is useful work when linked to evidence. If you join later,
use the same onboarding path and agree an individual setup target with a maintainer
while taking a bounded current task. The cohort's [schedule](semester-plan.md#calendar-and-working-targets)
continues; new students are not expected to complete work before joining.

Add one short portfolio row for each meaningful outcome, linked to its issue, PR, review, or artifact. Those links show the actual review status; you do not need a second progress log. For shared work, say who did what. The [portfolio guide](contributors/README.md) has examples.

Before starting the next branch, update from the official repository with a clean working tree:

```bash
git switch main
git pull --ff-only origin main
git switch -c work/ISSUE-NUMBER-short-description
```

Replace `ISSUE-NUMBER-short-description` with the task number and a few words. Push future work to `fork` and open PRs back to the official `main` in the same way. The [semester plan](semester-plan.md) explains what the cohort is delivering and when; [CONTRIBUTING.md](../CONTRIBUTING.md) covers the full review process.
