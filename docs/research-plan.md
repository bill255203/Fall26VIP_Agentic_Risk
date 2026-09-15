# Research Plan

## North Star

The program asks:

> How do failures propagate through agentic AI systems, when do they become consequential, and which assurance controls contain them?

Keep the project hierarchy explicit:

1. **Agent Assurance** is the broader research program: evidence that an agentic system remains acceptably controlled despite failures, uncertainty, and delegated autonomy.
2. **Risk propagation** is the central research problem.
3. **The VIP cohort** is the vehicle for producing cumulative evidence, code, traces, and writing.
4. **A simulated financial-control workflow** is the first experimental environment. It gives actions clear consequences without using real accounts, money, or production systems.

A useful conceptual chain is:

> Failure → Propagation → Authority boundary → Consequence → Control

The first cohort should build a small experimental apparatus, not a general platform. Its contribution is a reproducible method and careful pilot evidence.

## Common research cycle

Every study follows the same cycle:

| Stage | Required question or action |
| --- | --- |
| **Define** | State one falsifiable question, hypotheses, unit of analysis, outcomes, and exclusions before running the study. |
| **Baseline** | Run the unchanged workflow against known ground truth. |
| **Perturb** | Change one declared input or mechanism. |
| **Observe** | Preserve the full trace needed to locate propagation, decisions, and interventions. |
| **Control** | Add one assurance mechanism with a precise, testable rule. |
| **Compare** | Use the same scenarios and declared analysis across conditions. Report counts and uncertainty, not just examples. |
| **Generalize** | State only what the design supports, identify limitations, and propose the next test. |

## First pilot

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

## A later empirical study of authority

Treat a causal authority study as a separate experiment after the apparatus works. It should:

1. define whether the target is the effect of authority on reasoning, proposed decisions, or realized consequences;
2. randomly assign the authority treatment within a shared set of scenarios;
3. hold prompts, information, model settings, tools, and controls fixed except for the treatment;
4. collect a common pre-enforcement decision outcome in every condition so comparison is not determined by the cap;
5. use multiple independent scenarios and, for stochastic agents, declared repeated seeds;
6. analyze paired or blocked comparisons by scenario and report uncertainty;
7. distinguish behavioral effects from the mechanical protection supplied by enforcement.

This design can test a causal claim. The first pilot should be described as apparatus and enforcement validation.

## Semester delivery

The [Fall 2026 semester plan](semester-plan.md) is the single operational plan for milestones, dates, owners, dependencies, and delivery evidence. This document defines the scientific method. A technical report and reproducible evidence are semester outputs; publication depends on the findings.

## Claim discipline

Do not claim that the cohort discovered multi-agent propagation, that finance alone creates novelty, or that one workflow establishes a universal Agent Assurance framework. Separate observed results from interpretation, and describe conclusions at the level supported by the scenarios, models, controls, and outcome definitions actually tested.
