# Choosing the semester study

**Current status: no empirical study has been selected or frozen.**
The code runs a scripted starter. [Candidate A: runtime containment](01-runtime-containment.md)
is a detailed proposal for student critique; its real-model experiment is not implemented.
[Issue #3](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/3) records the cohort's
selection and protocol review.

## What is open, and what is expected

The research territory is how risks arise, propagate, and can be understood or
controlled in agentic systems. Consequential decisions provide useful motivation;
the credit-limit setting is one available example. Students help choose the question,
environment, comparison, and tools from literature and early evidence.

The cohort will select **one bounded empirical study** and leave reusable methods,
evidence, analysis, and a report. A controlled replication, a control experiment,
or a study using existing genuine execution traces can fit. A live model backend
is needed only when the selected question requires new model runs. An attribution
study needs defensible labels and an attribution measure; a control study needs
both risk and useful-task outcomes. Every study needs a meaningful comparison.

Keep Candidate A available and consider **at most one developed alternative**
across the cohort. Reading can range more widely, but preparing many full proposals
would consume the experiment time. Agent Assurance, CAGE, and the benchmarks in
the [literature guide](../literature.md) are optional sources or tools. No named
framework or control is required by the program.

## Selection and protocol

1. **Explore and test feasibility from kickoff through M2.** Reproduce and critique
   the starter, read relevant primary sources, and attempt one bounded published
   reproduction. Divide that work between students. Small development probes or
   checks on existing data belong to [issue #3](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/3),
   alongside inputs from starter critique #1, literature #2, and bounded reproduction #6.
   A feasibility failure is useful evidence when its cause and implications are recorded.
   Use a declared development subset for feasibility probes and preserve held-out
   records for confirmatory analysis. If prior inspection prevents a clean holdout,
   disclose it and limit the affected conclusions to exploratory or replication
   findings; calling a study a replication does not remove that limitation.
2. **Compare the candidates in issue #3.** Use the short outline below. Select on
   importance, what prior work leaves unresolved, measurable outcomes, credible
   comparisons, accessible resources, and an end-to-end validation path by M3.
   A deliberate replication can be selected for its value without claiming novelty.
3. **Record one decision and freeze its protocol at M2.** The method
   lead records the rationale and review, with student research and engineering
   input. Link the chosen protocol revision and alternatives considered from the
   [decision log](../decisions.md). Candidate A needs the same review as any alternative;
   it is not selected automatically. Preserve reasons for rejecting or narrowing proposals.
4. **Align the work queue with the decision.** Update the semester plan and issues
   before committing to study-specific implementation. If A is selected, activate
   [gate issue #4](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/4) in M3.
   If another study is selected, keep #4 deferred and define only its needed tasks.
5. **Build and validate after protocol freeze.** [Issue #7](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/7)
   starts after #3 records the selected study and frozen protocol. Complete the smallest
   selected experiment or analysis pipeline by M3, reusing relevant feasibility work.
   Freeze its evaluation cases/data before confirmatory runs or analysis; keep
   development results separate.
   Changes after inspecting evaluation results must be recorded as amendments.

If no candidate is feasible, the method lead records a narrower study or revised
scope immediately. Neither the calendar nor a lack of alternatives makes a study
valid. An apparatus-only outcome is an explicit scope reduction, not a completed
empirical study. Resource access and any paid-call budget must be settled before use.

## Short proposal outline

Use one concise issue entry or document per candidate. Candidate A already has a
detailed document: it illustrates what a mature protocol can look like. Early student
proposals need only the five-part outline below; they do not need to match A's level
of detail to be considered. Compare candidates using this outline, then develop
the selected proposal into a full protocol. Critique and amend A without duplicating it.

| Item | What the cohort needs to know |
| --- | --- |
| Question | One answerable question, why it matters, and what result could change our view. |
| Prior work | Relevant primary sources, what is established, and the remaining uncertainty or replication purpose. |
| Smallest comparison | Conditions or baselines, what stays fixed, and the unit being compared. |
| Evidence and measures | Data/trace access, defensible truth or labels, primary outcome, useful-task or other relevant tradeoff, and claim limits. |
| Feasibility | Reproduction/probe evidence or concrete limitation, owners, access/resources, and the smallest M3 deliverable. |

The selected proposal becomes a reviewed protocol: specify the hypothesis or
analysis question, data/scenario construction, conditions, outcomes and denominators,
sample/repeat counts, inference target, analysis and uncertainty, failure/exclusion/
retry rules, stopping rule, resources, and provenance. Apply design-specific details
where relevant. Candidate A's four cells and utility tolerance belong to A; other
questions must justify their own measures and precision.

## Credit and continuity

Link source notes, critiques, reproduction attempts, proposals, selection rationale,
and substantive review in students’ [Individual tasks](../issue-workflow.md). A proposal
can be a valuable contribution even when it is rejected. Record who did what and
the evidence; reading volume, positive findings, or adoption of a proposal are not
contribution scores. Keep the [semester targets](../semester-plan.md#calendar-and-working-targets)
and one shared report as the delivery plan.
