# Contributing

This repository supports cumulative research across VIP cohorts. Keep each contribution small enough to review and complete enough for the next cohort to reproduce.

## Workflow

1. Start from a GitHub issue with a clear question or deliverable.
2. Create a short-lived branch from `main`.
3. Make one focused change and document assumptions.
4. Run `python -m unittest discover -s tests -v`.
5. Open a pull request and link the issue.
6. Address review, then merge only when the acceptance criteria are met.

Organize work as `To Do`, `In Progress`, `Review`, and `Done` if a Project board is enabled. Issues and pull requests are sufficient to start. An issue should have at least one of these labels:

- `research`: literature, hypotheses, design, analysis, or writing;
- `engineering`: experimental environment or instrumentation;
- `experiment`: a configured, executed, or analyzed study;
- `bug`: behavior that contradicts the documented design.

## Experiment changes

A research result is reviewable only when another person can identify exactly what produced it. Include:

- the research question and falsifiable hypothesis;
- the changed and held-constant variables;
- ground truth and fault definition;
- configuration and code revision;
- backend, model, prompts, sampling parameters, and seeds when applicable;
- raw trial traces and an analysis with explicit denominators;
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

Discuss authorship expectations before manuscript work begins. Track contributions using the CRediT roles described in the [cohort guide](docs/cohort-guide.md).
