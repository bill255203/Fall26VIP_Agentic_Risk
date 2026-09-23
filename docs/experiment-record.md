# Experiment Record

An experiment is reproducible only when another contributor can identify the exact inputs, rerun the same procedure, reconstruct every reported denominator, and explain how the summary was derived. Keep one versioned record for each experiment batch and link it to its code, raw artifacts, and analysis.

## How to use this reference

This is a field guide, not another report to submit. Link the applicable record from
your pair case. For the scripted starter, keep the generated files and record your
command, source revision, result/error and interpretation in your task; do not fill
model/API fields that do not apply. For a trace study, record source IDs, selection,
labels and analysis instead of inventing model-call settings. Generated provenance
can be linked rather than copied into a second log.

Here, a **paired comparison** means matched experimental cases/conditions, not the
two student partners. Repeated messages and deterministic repetitions are not extra
independent samples.

## Required record

Complete these fields before or during execution, not from memory at the end.

### Identity and intent

- experiment and batch IDs;
- research question and hypotheses or quantities to estimate;
- pilot, apparatus validation, confirmatory study, or exploratory study;
- unit of analysis and planned conditions or comparison groups;
- primary and secondary outcomes, with formulas;
- exclusion, retry, and stopping rules;
- issue and pull-request links;
- selected protocol revision and the recorded selection decision, or the apparatus/pilot designation;
- source assumption, control, or literature claim; exact source revision; predicted evidence path where applicable; and the outcome that would challenge the claim.

### Exact implementation

- Git commit and whether tracked or untracked changes were present;
- exact run command and configuration file;
- dependency and runtime versions;
- model/provider identifier, revision when available, decoding settings, and seed behavior, or `not applicable` for a study of existing traces without new model calls;
- prompt/template files and versions or hashes;
- scenario, dataset, or trace-set version; selection and inclusion rules; fixture or label version; and ground-truth source;
- authority, action, and enforcement semantics where applicable;
- treatment, perturbation, exposure, control, evaluator, and labeling rules where applicable;
- actual timestamp and execution environment;
- known deviations from the plan.

Include a compact map of the selected study's evidence path: actors or sources, inputs, tools or transformations, permissions where relevant, memory or retained context, outputs, labels, and evaluation boundary. [Candidate A](studies/01-runtime-containment.md) contains one proposed role map and evidence-separation design; use it only if that candidate is selected. For a practical verifier, identify the independent evidence source and what it can observe, and keep evaluator answer labels inaccessible. For paired downstream comparisons, retain the shared upstream trace/request ID and record how each execution branch starts from an isolated state copy. For replications or existing-trace studies, record source revision, acquisition method, license or access constraint, sampling frame, integrity check, and any transformation from source records to analysis units.

Do not store credentials, private data, or secret values in a record or trace.

### Run accounting

For every attempted run or analyzed source record, retain:

- record or run ID, source or scenario ID, pairing or cluster ID where applicable, condition or exposure, and seed where applicable;
- ingestion or execution status: available or completed, failed, timed out, cancelled, or retried, as applicable;
- whether the run is included and, if excluded, the predeclared reason;
- proposed decision, authority attempt, enforcement result, control result, and observed or simulated action where applicable;
- expected decision, action, attribution, or other reference label, together with its source;
- trace and error-artifact locations.

A retry receives a new run ID and points to the original attempt. Never silently replace a failed run.

## Generated artifacts

The current pilot writes `config.toml`, `manifest.json`, `trials.jsonl`, and `summary.csv`. Each JSONL row contains one full trial plus its outcomes; there is no separate outcome-table file. The manifest records the scripted backend, seed, Python version, Git revision/dirty state, package-source hash, and artifact hashes. Preserve these logical layers when the selected study adds live calls, reuses a dataset, or analyzes existing traces:

For empirical work, retain the observable source material needed for the claim: exact assembled model inputs for live calls; dataset or trace identifiers and content snapshots for reused evidence; available tool schemas; calls and outputs; raw exposed responses; control, attribution, or evaluator outputs where applicable; and observed or simulated actions. Record redactions and unavailable fields explicitly. This adapts AT-01's observable-evidence practice; it is not a claim to capture hidden model reasoning or satisfy the whole control matrix. See [the source map](agent-assurance-bridge.md).

| Layer | Purpose | Interpretation |
| --- | --- | --- |
| Manifest/config snapshot | Records what was intended and what ran | Required to reconstruct the batch. |
| Per-run trace/events | Records inputs, messages, decisions, controls, and actions | Primary evidence for audit and re-analysis. Redact only by a documented rule. |
| Run-level outcome table | One row per analysis unit | Preferred input for statistical summaries. Agent messages are not independent trials. |
| Summary metrics | Counts and rates; later empirical studies may add intervals and plots | Derived convenience output; verify it against run-level data. |
| Logs/errors | Explains operational failures and retries | Operational failures are not task failures unless defined that way in advance. |

Generated files are not self-interpreting. Document schema version, units, allowed values, missing-value meaning, and the code that generated each derived artifact. Preserve raw traces even when a summary exists.

## Denominators and missing runs

Every reported rate must name both numerator and denominator. Include a count table before percentages:

```text
attempted | completed | eligible | excluded | missing | numerator
```

The current summary groups by authority, verification, and fault. Its rates are:

| Field | Numerator / denominator |
| --- | --- |
| `incorrect_recommendation_rate` | incorrect recommendations / all recommendations |
| `incorrect_approval_rate` | incorrect approvals / actual approvals |
| `execution_rate_all_trials` | executed operations / all trials in the cell |
| `erroneous_execution_rate_all_trials` | incorrect executed operations / all trials in the cell |
| `erroneous_execution_rate_among_executed` | incorrect executed operations / executed operations |
| `harmful_state_change_rate_all_trials` | incorrect executed operations that change the limit / all trials in the cell |
| `harmful_state_change_rate_among_executed` | incorrect executed operations that change the limit / executed operations |
| `task_completion_rate` | executed operations / execution-authorized trials |
| `task_success_rate` | correct executed operations / execution-authorized trials |

An executed `keep_limit` is an explicit operation, even though it leaves state unchanged. It is erroneous if the policy required `reduce_limit`. A block by the verifier prevents execution but does not repair or complete the task. Completion and success are therefore different measures.

The corresponding `n_...` columns expose every numerator and denominator. A zero denominator produces JSON `null` or an empty CSV cell, not zero. Lower-cap execution rates over all trials are structurally zero; their task rates are missing because they are ineligible. Analyze verification effectiveness within execution-authorized conditions rather than pooling caps.

`mean_propagation_depth` counts accepting stages starting with the monitor as stage 1, and is zero for clean inputs. `error_authority_reached` and `containment_point` are recorded per trial. The containment counts in the summary apply only to injected errors; clean authority gates are not labeled contained failures.

Do not include lower-cap runs in an execution-eligible denominator. Do not count event rows, agent turns, retries, or duplicated summaries as additional trials. Report missing and operationally failed runs separately; explain any sensitivity analysis that treats them as successes or failures. The scripted pilot aborts on a batch error; only an output directory containing its final `manifest.json` represents a complete batch.

## Scripted-pilot and Candidate A pairing

The clean and flipped versions of one base scenario are a pair. The same scenario should also appear under verification on/off and each authority cap. Keep all non-treatment settings identical when possible.

That matrix describes the scripted apparatus. If selected, Candidate A instead uses four primary cells (clean/corrupted × practical gate off/on), all execution-eligible. Replay each upstream candidate request through isolated gate branches with a shared pair ID; keep optional oracle references and non-executing cap checks outside its primary effect estimate. These four cells and a live backend are not general semester requirements. Each study uses its own recorded method and dated changes; confirmatory claims require prespecified rules. Neither matrix is a default assignment.

For the pilot or Candidate A, analyze within-scenario contrasts before aggregating:

1. verify that the clean run reaches the expected outcome;
2. measure how the flip changes the proposed decision and propagation path;
3. measure how verification changes the flipped outcome;
4. report authority-cap results as enforcement behavior and descriptive outcomes;
5. for empirical studies, aggregate matched-case effects with uncertainty that respects repeated observations from the same scenario; for the scripted pilot, report descriptive validation counts only.

For stochastic agents, repeat complete matched sets using declared seeds or replicate IDs. Treat runs sharing a scenario as clustered or repeated measurements. Do not treat each message or each condition from the same scenario as independent evidence. Other designs must name their analysis unit and dependence structure just as explicitly.

## Deterministic fixture caveat

A deterministic fixture is a development instrument. Repeating the identical fixture may confirm that code paths are stable, logs are complete, caps are enforced, and the oracle behaves as specified. Identical repetitions do not create new independent observations.

The seed shuffles low/high cases and generates auxiliary risk scores. Decisions use only the low/high label. The default 40 cases therefore exercise two behavioral templates; different scores and case IDs do not add independent decision mechanisms. No model, prompt, API call, confidence interval, or significance estimate is involved in this pilot.

Do not make behavioral, causal, population, model-robustness, or domain-general claims from the fixture. Such claims require distinct scenarios sampled or constructed under a documented protocol and, where relevant, genuine stochastic agent runs. Label fixture-only tables and plots as validation results.

## Minimum report

A completed report contains the question, design, evidence and condition counts, exclusions, record-level outcomes, the prespecified analysis, uncertainty appropriate to the evidence, usefulness or cost results where relevant, anomalies, negative results, limitations, and links to exact artifacts. It must distinguish observations from explanations and list the smallest next experiment that could resolve remaining uncertainty.
