# Research Plan

## North Star

The program asks:

> How do risks arise and propagate in agentic AI systems, when do they become consequential, and how can they be understood or controlled?

The VIP is an empirical research project on agentic risk and assurance. A simulated financial-control workflow is the starter environment, giving decisions observable consequences. Academic literature and selected [Agent Assurance concepts](agent-assurance-bridge.md) supply hypotheses and methods. Neither source predetermines the question or findings or requires the cohort to validate an entire framework.

A useful conceptual chain is:

> Failure → Propagation → Authority boundary → Consequence → Control

The first cohort's contribution is one bounded, reproducible study with clear methods, data, conclusions, and limitations. The cohort helps select that study through a short, evidence-producing discovery period rather than receiving a predetermined paper question.

## Selecting the first empirical study

The cohort will select one study by **September 25** using the [study-selection and protocol process](studies/README.md#selection-and-protocol). Consider no more than two serious cohort candidate proposals. Each candidate must identify a testable question or deliberate replication purpose, relevant primary literature, a feasible empirical design, needed access and resources, measurable outcomes, and a credible path to the October 2 validation gate. A bounded replication, a controlled experiment, an analysis of existing genuine traces, or an attribution study can qualify when its question and evidence fit the program.

[Candidate A: runtime containment](studies/01-runtime-containment.md) is a worked starting proposal, not the selected semester study. It asks whether independent-evidence gating reduces incorrect actions under corrupted input without unacceptable loss of clean task completion. Its detail makes it useful for critique and feasibility testing; it receives the same review of novelty or replication value, evidence, access, and schedule as any other candidate.

The scripted pilot remains common setup evidence. It gives every candidate a concrete apparatus to reproduce and criticize, but the selected study may adapt it, replace parts of it, reuse an established research asset, or analyze a suitable genuine trace set. If no candidate is viable by September 25, the method lead records a narrower scope decision; no candidate becomes selected merely because it is already documented.

1. **Explore and critique.** Read primary literature, inspect relevant datasets or systems, and question the scripted pilot's assumptions.
2. **Reproduce or probe feasibility.** Reproduce the starter and one bounded external result or component, or run another small feasibility check that directly informs a candidate.
3. **Select and freeze one study.** Record the question, hypotheses or estimands, evidence source, units, comparisons, outcomes, resources, exclusions, failure handling, and analysis before confirmatory work.
4. **Produce and inspect evidence.** Preserve the observable inputs, outputs, decisions, failures, labels, and provenance needed for the selected claim. Analyze adverse outcomes beside usefulness or other relevant costs.
5. **Report the finding and its limits.** Explain whether the evidence supports, qualifies, or challenges the tested claim. Keep method critique, negative results, and next questions visible.

If Candidate A is selected, its first empirical effect is the effect of the **configured control package**, with authority held constant. Its practical gate, live backend, and fixed four-cell comparison are Candidate A requirements, not program-wide requirements. A different selected study must provide equally explicit claim boundaries and a design appropriate to its question.

## Common research cycle

Every study follows the same cycle:

| Stage | Required question or action |
| --- | --- |
| **Define** | State one answerable question, prespecified hypotheses or estimands, unit of analysis, outcomes, and exclusions before running the study. |
| **Evidence base** | Establish the baseline, source dataset, trace sample, or prior result against which the question will be assessed. |
| **Vary or classify** | Apply a declared treatment or perturbation, or define a reproducible exposure, label, or comparison in existing evidence. |
| **Observe** | Preserve the traces, records, labels, and provenance needed to locate outcomes and support re-analysis. |
| **Test or analyze** | Apply the prespecified control, replication, attribution, or analysis procedure appropriate to the question. |
| **Compare** | Use the declared units and analysis across conditions or evidence groups. Report counts and uncertainty, not just examples. |
| **Generalize** | State only what the design supports, identify limitations, and propose the next test. |

## Current scripted pilot

Use a deterministic, simulated credit-limit decision with explicit ground truth. The workflow passes a signal through monitoring, analysis, approval, and execution roles. “Execution” applies an explicit `reduce_limit` or `keep_limit` operation to simulated state. Keeping the limit unchanged is a decision too: it is incorrect when the ground-truth policy requires a reduction.

The pilot crosses three factors:

| Factor | Levels |
| --- | --- |
| Authority cap | `recommend`, `approve`, `execute` |
| Oracle verification | `off`, `on` |
| Input condition | `clean`, `flip` |

This is a 3 × 2 × 2 design with 12 cells. A `flip` replaces the correct input signal with a known incorrect value while leaving the scenario and expected decision unchanged. Oracle verification consults fixture ground truth immediately before execution and either permits or blocks the proposed operation. It blocks an incorrect proposal without repairing the decision or completing the task. Calling it an oracle is deliberate: it validates the control pathway, not the realism of a deployable verifier.

Run every base scenario in every condition. Preserve the scenario ID, treatment assignment, authority attempt, enforcement decision, proposed decision, final action, and control result. Clean and flipped versions of the same base scenario form a pair.

### What this pilot can establish

The authority caps are an enforcement test. They can show whether the system prevents an agent from crossing a configured boundary and can describe outcomes under each allowed action set.

They **cannot establish that greater delegated authority causes worse reasoning or a higher underlying tendency to fail**. Execution is impossible under lower caps by construction, so a lower consequential-action rate there is partly mechanical. Comparisons across caps must be labeled descriptive. Do not present them as a causal authority effect.

Likewise, a deterministic fixture validates plumbing, logging, expected decisions, perturbation, and control enforcement. It does not provide independent repeated evidence about real agent behavior.

### Outcomes

Predeclare the exact numerator, denominator, and eligible conditions for each outcome.

**Primary outcome**

- **Erroneous execution rate:** executed decisions that disagree with the ground-truth policy divided by all trials in that condition (`erroneous_execution_rate_all_trials`). This includes both unnecessary reductions and incorrect decisions to keep a limit unchanged. Report clean and flip conditions separately, and use the `execute` conditions to assess the verifier. Lower-cap zeroes are structural enforcement results. Also report the conditional rate among executed operations, with a missing value when none executed.

**Secondary outcomes**

- **Propagation depth:** number of stages that accept the corrupted input or a decision derived from it: monitor = 1, analysis = 2, approval = 3, execution = 4. Clean runs have depth 0. The metric counts the injected origin as stage 1; blocked stages do not add depth.
- **Error authority reached:** highest boundary crossed by an incorrect decision (`none`, `recommend`, `approve`, or `execute`), distinct from the configured authority cap.
- **Harmful state change:** an incorrect executed decision that changes the limit. This narrower measure excludes incorrect keep decisions and is reported separately from erroneous execution.
- **Incorrect recommendations and approvals:** record errors at the common recommendation stage and, where permitted, the approval stage.
- **Containment point:** verification, authority cap, or none for flipped inputs; not applicable to clean inputs.
- **Task completion and success:** completion means an operation executed; success means it executed the correct decision. Both use all execution-authorized trials as the denominator and are missing under lower caps. A rejected wrong decision is contained but does not complete the task.

Inspect clean execution-enabled runs for unnecessary blocking and verify that no realized approval or execution exceeds its authority cap. Tests cover these enforcement invariants. These checks, together with clean task-success rates, expose a control that simply blocks everything. The fixture does not measure latency or cost.

Safety results must be read beside utility. A control that blocks every action may reduce harmful execution while also making the workflow useless.

## Requirements for a causal authority study

A candidate that tests authority causally must treat it as a separate experiment rather than infer it from the scripted caps. It should:

1. define whether the target is the effect of authority on reasoning, proposed decisions, or realized consequences;
2. randomly assign the authority treatment within a shared set of scenarios;
3. hold prompts, information, model settings, tools, and controls fixed except for the treatment;
4. collect a common pre-enforcement decision outcome in every condition so comparison is not determined by the cap;
5. use multiple independent scenarios and, for stochastic agents, declared repeated seeds;
6. analyze paired or blocked comparisons by scenario and report uncertainty;
7. distinguish behavioral effects from the mechanical protection supplied by enforcement.

Those requirements are necessary before making a causal authority claim. The current scripted pilot is apparatus and enforcement validation. Candidate A would estimate a containment-control effect under fixed authority if the cohort selects and freezes it.

## Semester delivery

The [Fall 2026 semester plan](semester-plan.md) is the single operational plan for milestones, dates, owners, dependencies, and delivery evidence. This document defines the scientific method. A technical report and reproducible evidence are semester outputs; publication depends on the findings.

## Claim discipline

Do not claim that the cohort discovered multi-agent propagation, that finance alone creates novelty, or that one workflow establishes a universal Agent Assurance framework. Separate observed results from interpretation, and describe conclusions at the level supported by the scenarios, models, controls, and outcome definitions actually tested.

Keep permission, correctness, mutation, and consequence distinct. An authorized action can still be wrong. An explicit wrong no-op, omission, or decision to preserve state can be consequential even though it is not a state mutation; report harmful state change as a narrower outcome where useful.

Disclose the research group's relationship to Agent Assurance. An affiliated cohort's experiments can scrutinize assumptions but are not automatically external validation or peer review. A static risk path is a hypothesis about possible propagation, not proof of actual traversal. See the [source map](agent-assurance-bridge.md) for exact control meanings and limitations.
