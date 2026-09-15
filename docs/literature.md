# Literature Starting Point

This is a seed list, not a completed literature review. The links below point to the primary arXiv records. Descriptions are deliberately limited to what the papers say they contribute; students should read and assess the methods before relying on any result.

## Start with the first question

For [Study 1](studies/01-runtime-containment.md), review propagation, executable-action outcomes, runtime containment, and safety/utility tradeoffs. Use the [Agent Assurance source map](agent-assurance-bridge.md) to select testable assumptions from its pinned control matrix. Read IA-02, IA-03, CF-01, and AT-01 first; their literal scopes are narrower or different from some proposed VIP adaptations.

Treat this methodology as one source alongside independent papers. Record which claim the first experiment could falsify and what alternative explanations remain. Time-box the initial review and reproduction selection to the September 25 protocol checkpoint; continue expanding the literature while feasible implementation proceeds. A full reproduction of an unrelated benchmark is not a prerequisite for the first experiment.

## Multi-agent adversarial risk and propagation

### [TAMAS: Benchmarking Adversarial Risks in Multi-Agent LLM Systems](https://arxiv.org/abs/2511.05269) — arXiv:2511.05269

TAMAS presents a benchmark for adversarial robustness in multi-agent LLM systems. Its abstract describes five scenarios, 300 adversarial instances across six attack types and 211 tools, 100 harmless tasks, ten backbone models, and three interaction configurations. It also proposes an Effective Robustness Score intended to combine safety and task effectiveness.

**Why it matters here:** it provides relevant benchmark structure, adversarial baselines, and an explicit safety–utility tradeoff. It also means that “multi-agent systems can propagate adversarial failures” should not be presented as this project’s novelty.

### [ACIArena: Toward Unified Evaluation for Agent Cascading Injection](https://arxiv.org/abs/2604.07775) — arXiv:2604.07775

ACIArena studies cascading injection across external inputs, agent profiles, and inter-agent messages, with several attack goals and multi-agent implementations. The authors report that topology alone does not explain robustness, and that role design, interaction controls, and transfer across settings matter.

**Why it matters here:** it is directly related to cascading failure and control evaluation. The cohort should compare its threat model and outcome definitions with ACIArena rather than claim cascading injection is unstudied.

## Failure attribution and observability

### [Seeing the Whole Elephant: A Benchmark for Failure Attribution in LLM-based Multi-Agent Systems](https://arxiv.org/abs/2604.22708) — arXiv:2604.22708

This paper introduces TraceElephant, a benchmark for failure attribution using full execution traces and reproducible environments. The authors compare full-trace and partial-observation settings and report substantially better attribution when inputs and context are retained.

**Why it matters here:** it motivates keeping complete, structured execution evidence instead of final outputs alone. It studies attribution; our initial pilot uses known injected faults and should not imply that logging by itself solves automated attribution.

### [Which Agent Causes Task Failures and When? On Automated Failure Attribution of LLM Multi-Agent Systems](https://arxiv.org/abs/2505.00212) — arXiv:2505.00212

This work formulates automated failure attribution and introduces the Who&When dataset, built from failure logs with labels for responsible agents and decisive error steps. Its reported benchmark results show that locating the responsible step remains difficult even when methods can sometimes identify the agent.

**Why it matters here:** it offers task definitions, annotations, baselines, and cautions for any later attribution study. The first pilot knows where it injects a fault; that is ground truth for propagation measurement, not evidence that the system can infer responsibility in an unknown incident.

## How to use this list

The first cohort should make the literature review an explicit research deliverable. For each relevant paper, record:

- the research question, threat or failure model, system boundary, and unit of analysis;
- datasets, models, agent frameworks, controls, baselines, and outcome denominators;
- whether code, data, prompts, and traces are available and reproducible;
- what the evidence directly supports and what the discussion only proposes;
- similarities to and differences from consequence-aware propagation across authority boundaries;
- one concrete implication for this project’s experiment design.

Then broaden the search systematically across multi-agent safety, cascading failures and prompt injection, delegated authorization and capability control, runtime verification, operational risk, failure attribution, trace observability, and safety–utility evaluation. Record search sources, query strings, inclusion criteria, and the version of each reviewed paper.

Related work does not establish this project’s novelty. Only a documented review can show which questions are already answered, which methods can be reused, and where a defensible gap may remain. Until that review is complete, describe the project as investigating consequence-aware propagation and controls, not as the first work to do so.
