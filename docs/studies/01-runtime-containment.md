# Candidate A: runtime containment

> **Optional advanced example (September 23 update).** A pair may adapt this design
> with peer feedback. It is not the cohort assignment, a selected study, or the
> expected detail of a beginner outline. Use the [pair case guide](README.md) and
> current schedule; no platform or backend is implemented by this document.

**Status: unselected and unimplemented candidate protocol.** This maintainer-authored
proposal is a starting point for student critique under the [selection process](README.md#selection-and-protocol).
The executable code implements only the scripted pilot in `experiments/pilot.toml`.

This advanced protocol does not add an instructor sign-off requirement. A pair can
narrow or adapt it with peer feedback and dated method notes. Its prespecification
requirements apply to the confirmatory claims below; simpler exploratory work
should state its own narrower question and limits.

If a pair adopts Candidate A, its model/backend choice, resource limits, scenario
set, repetitions, and analysis thresholds must be reviewed and frozen in
its Pair case issue before confirmatory runs (registered through #3).
Its detail illustrates what a mature protocol can look like. Early student ideas
need only the [five-part candidate outline](README.md#short-proposal-outline), not a
protocol of comparable length; selection assesses the question and evidence.

## The question and the possible answers

> In an execution-capable multi-agent workflow, does a gate that checks independent evidence reduce incorrect actions under a corrupted upstream summary, while preserving correct task completion on clean inputs?

This would test one runtime containment package. Delegated authority defines where a recommendation becomes an action. Authority would be held constant in the primary comparison, so both conditions could complete the same tasks. Permission does not establish correctness: an authorized request can still be wrong.

- **H1 — containment:** on faulted inputs, the practical gate reduces erroneous execution per assigned trial relative to no gate.
- **H2 — utility:** on clean inputs, task-success loss from the gate is no larger than a prespecified tolerance, `delta`. The working proposal is 5 percentage points; the reviewed protocol must justify and freeze the tolerance and the precision needed to assess it.

Define clean loss as `task_success_off - task_success_on`. To support H2, a prespecified one-sided 95% upper confidence bound for that loss must fall below `delta`; otherwise report H2 as unresolved or contradicted as the evidence warrants. Choose a method valid for the paired, clustered design before running, including rare-event and zero-loss cases. A naive bootstrap with no observed losses can produce a misleading zero-width interval. Repeated calls on a few cases cannot substitute for enough distinct cases; assess whether the budget can resolve the proposed tolerance during the M3 plan review.

Report effect sizes and uncertainty. A wide interval is inconclusive, not proof of no effect. Useful outcomes include risk reduction with acceptable utility, risk reduction with excessive blocking, no detectable benefit, or worse performance. These findings concern the tested mechanism, scenarios, and model only.

## The smallest experiment

Use the existing synthetic credit-limit setting: keep a limit or reduce it according to a stated synthetic policy. Replace scripted decision behavior with one selected model used in fixed roles. Keep execution in a deterministic local tool stub; no external account or action is involved.

Create distinct synthetic case documents with known facts and an evaluator-only expected decision. Include cases requiring reduction and cases requiring no change, with documented difficulty and boundary cases. A seeded shuffle of the current low/high labels is not a new scenario set.

For each base case, supply a clean upstream summary and a paired version with one declared decision-relevant assertion corrupted. Keep all other facts and documents fixed. The independent evidence document comes from a separately constructed, uncorrupted source in the fixture. Its format must not expose an answer label. Ordinary decision agents see the upstream summary; the practical verifier additionally sees this source document and the proposed action. Only the evaluator and optional ideal oracle receive the expected decision directly.

Before model runs, check that exactly the intended assertion changes, that its corrupted value would imply a different decision if accepted under the stated policy, and that both error directions are represented. Preserve cases where downstream agents nevertheless reach the correct answer; do not force propagation to obtain an interesting trace.

The first fault is a factual/semantic error, not a prompt-injection attack. Claims about adversarial instructions, shared memory, asynchronous actions, or exfiltration require later experiments.

### Architecture and authority map

| Role | Inputs / tools | Authority | Memory, outputs, and outbound capability |
|---|---|---|---|
| Monitor | Selected case summary | Read and forward | Per-trial state only; passes the summary to analysis; no outbound access. |
| Analysis | Summary and synthetic decision policy | Recommend an action | Emits recommendation and exposed rationale/response; cannot change state. |
| Approval | Recommendation and the fixed policy context | Form an execution request | Emits the same structured request type in every condition; cannot change state. |
| Practical verifier, when enabled | Request, policy, independent source document | Allow or block this request | Separate invocation/context; no shared conversational memory or evaluator labels; emits a structured decision. |
| Executor | Structured request and gate result, when applicable | Apply `keep_limit` or `reduce_limit` to local state | Deterministic stub; records attempt, enforcement, result, and final state; no network egress. |

Record the actual prompts, tool schemas, role implementation, and any deviation from this map when freezing the protocol. Sharing a base model does not make the verifier independent in its errors; here “independent” describes the supplied evidence and separated context.

### Predicted path, before observing results

```text
corrupted summary → monitor → recommendation → approval request
                                                   ↓
                          no gate OR independent-evidence gate
                                                   ↓
                                      simulated execution
```

Prediction: an upstream factual error can induce an incorrect request; the verifier may interrupt it before execution. A correct downstream agent may already contain the error without the gate. Measure both possibilities. Gate failures can come from misreading evidence, trusting the bad summary, or rejecting correct requests. Record those as candidate explanations; a trace alone does not establish causal attribution.

## Conditions and pairing

| Input | No practical gate | Practical evidence gate |
|---|---|---|
| Clean summary | Baseline usefulness and natural error | Utility and unnecessary blocking |
| Corrupted summary | Error propagation without intervention | Containment effect and remaining failures |

These four cells form the primary study. Use the same base cases, upstream model outputs, and structured candidate requests across gate conditions by producing the upstream trace once per case/input/replicate and replaying it through each branch in an isolated state copy. Randomize execution order and record a shared pair ID. This isolates the downstream control-package comparison; it does not measure how agents change their behavior when they know a gate exists.

Pair clean and corrupted inputs on base case and replicate as well; those upstream model calls may differ. Keep model versions, ordinary-role prompts, tool availability, policy, and sampling settings fixed. The optional ideal oracle is a calibration reference kept outside the primary four-cell effect estimate. Recommendation/approval-only caps remain enforcement checks and are never pooled into the execution-eligible denominator.

The gate adds evidence and a model invocation. An effect is attributable to that complete package, not separately to extra compute, evidence independence, or authentication strength. A same-source reviewer ablation is a possible later extension.

Because this gate only blocks an unchanged request, it cannot introduce a new incorrect action in an otherwise identical replay. Reduced error alone is therefore insufficient: assess which wrong requests it stops together with the correct work it blocks. An always-block policy would also reduce errors, but would fail the required task-utility assessment. Do not equate consequence with mutation: an explicit incorrect `keep_limit` operation is an erroneous execution even though state does not change; harmful state change remains a separate, narrower outcome.

## Outcomes and analysis

Use the current [outcome definitions](../research-plan.md#outcomes) where applicable and explicitly version new empirical fields.

| Outcome | Definition / denominator |
|---|---|
| Primary: erroneous execution | Wrong executed decision / all assigned trials in the condition, including explicit incorrect `keep_limit` operations. |
| Required utility: task success | Correctly executed policy decision / all assigned execution-eligible trials; a blocked request does not complete the task. |
| Unnecessary blocking | Gate blocks a correct candidate request / correct candidate requests presented to the gate; report clean and faulted inputs separately. Undefined when no correct request exists. |
| Gate miss rate | Gate allows an incorrect candidate request / incorrect candidate requests presented to it. Undefined when no incorrect request exists. |
| Supporting evidence | Incorrect recommendations/approvals, attempted vs realized actions, propagation depth/authority reached, containment point, harmful state changes, and operational failures. |

Report gate-on minus gate-off paired differences and counts. H1 estimates the gate-package effect under corrupted input; it does not by itself prove that corruption caused each wrong decision. Report the paired clean/fault contrast descriptively unless a separate corruption-effect or interaction hypothesis and appropriate assignment/sampling are preregistered.

Define the inference target during the M3 plan review. For a fixed hand-authored benchmark, report paired effects on that set and avoid population claims. For inference to a synthetic scenario population, define its construction/sampling distribution, draw distinct cases under that protocol, and account for scenario clustering. If using a paired bootstrap, resample entire base-case clusters containing both inputs, both gate branches, and all replicates; assess small-sample and boundary behavior before relying on it. Freeze case counts, replicates, confidence methods, pairing keys, and stopping rules. Do not count messages as samples or add runs because a desired result has not appeared.

Retain cases on which the clean baseline fails. Do not filter evaluation cases or tune prompts based on held-out results. Use separate development cases for smoke tests; freeze the evaluation set and its version before confirmatory runs. If the sample cannot resolve the utility tolerance, report the uncertainty rather than declaring H2 passed.

Malformed responses, missing evidence, and timeouts must be visible. The proposed gate fails closed on malformed/missing verdicts: execution is blocked and task success is false, with the operational cause recorded separately. A failed request is not evidence of semantic detection. Keep the full assigned-trial denominator, expose missing outcomes, and report a sensitivity analysis where missing outcomes could change the conclusion. Retry rules must not silently substitute successful attempts.

## Evaluate the candidate, then deliver if selected

Steps 1–2 inform selection. Steps 3–5 apply only if Candidate A is selected.
All checkpoints use the [semester schedule measured from kickoff](../semester-plan.md#calendar-and-working-targets):

1. **M1:** try and critique the starter after the first meeting, raise setup/access blockers, and share small reading and feasibility tasks relevant to this proposal.
2. **M2:** propose the pair case and inspect access/feasibility. Record an access failure as a limitation, not an assumed future solution.
3. **M3:** present the case and feasibility evidence. If adopted, review and freeze its hypotheses, utility tolerance, model/settings/resources, scenarios, failures, pairing and analysis. Demonstrate all four conditions, the practical gate, source/answer separation and isolated replay; freeze evaluation data before final runs. Narrow scope with the reviewer if infeasible.
4. **M4:** preserve the planned dataset and first complete paired analysis, including null findings and utility costs.
5. **Report draft checkpoint, then M5:** assemble a full draft, reproduce, review, revise, and hand off; reserve the remaining term for presentations and justified repairs.

These are working project targets, not NYU course deadlines. See the [semester plan](../semester-plan.md) for gate ownership and dependencies. A late student can join an active task without restarting the cohort's sequence.

## Relationship to Agent Assurance

[The source map](../agent-assurance-bridge.md) motivates authority-boundary questions from IA-02/IA-03, the narrow containment assumption from CF-01, and evidence capture from AT-01. Candidate A would not implement an authentication-strength experiment, assess all 26 controls, or certify a framework. If selected, it could support, qualify, or challenge a specific assumption; relevant academic work and contrary findings carry equal weight.
