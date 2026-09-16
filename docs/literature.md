# Literature Starting Point

This is a seed list, not a completed literature review. The links below point to the primary arXiv records. Descriptions are deliberately limited to what the papers say they contribute; students should read and assess the methods before relying on any result.

## Start by choosing a question

Use the [selection guide](studies/README.md) to compare at most two developed cohort proposals at M2, on the [schedule measured from kickoff](semester-plan.md#calendar-and-working-targets). Divide focused reading/reproduction tasks after the first meeting; nobody needs to survey every resource below. Select sources because they inform a question, baseline, or feasibility decision. Record contrary findings and the work's actual limits.

For [Candidate A](studies/01-runtime-containment.md), begin with propagation, consequential actions, practical containment, and safety/utility tradeoffs. The [Agent Assurance source map](agent-assurance-bridge.md) identifies related assumptions in IA-02/IA-03/CF-01 and the AT-01 evidence practice. Their literal scopes differ from parts of this adaptation. Other questions should choose their own relevant sources.

Time-box one bounded published reproduction so it can inform the selection. Record infeasibility rather than turning a full benchmark reimplementation into a prerequisite. Continue the literature review after choosing the study; evidence of an overlap or flaw can justify a recorded protocol amendment.

## Additional resources to evaluate selectively

These references serve different purposes. Reading a paper, reusing its data,
running its code, and adopting a framework are separate decisions. No row is a
mandatory integration or an established result about our own study.

| Resource | Why inspect it | Scope to keep clear |
| --- | --- | --- |
| [SABER: Small Actions, Big Errors](https://arxiv.org/abs/2512.07850) | Studies state-changing actions and combines targeted verification, reflection, and context management. Relevant prior work for any claim about safeguards at action boundaries. | Its observations and combined intervention do not establish our proposed gate's effect. A consequential error can also be an incorrect no-change decision. |
| [AgentDojo](https://agentdojo.spylab.ai/) | Reusable prompt-injection tasks, attacks, defenses, and a candidate for one small reproduction. | Prompt injection is a different fault mechanism from Candidate A's factual corruption; transferring a task or metric needs justification. |
| [Inspect AI](https://inspect.aisi.org.uk/) | Evaluation infrastructure with datasets, agents, tools, scorers, and logs; consider it if it reduces work for the selected study. | It is infrastructure, not evidence of novelty or a required replacement for the starter. |
| [CAGE](https://github.com/google/cybernetic-agent-governance-engine) | An architectural reference for execution mediation and other runtime controls. A bounded mechanism could inform a question or comparator. | A control-boundary invariant does not demonstrate practical detection or utility. Full integration, formal models, or richer routing need a selected scientific purpose. |

Use exact paper/code/data revisions in a reproduction. Check actual access, setup,
licensing, and resource requirements before selecting a dependency. A reused
benchmark can support independent research when the question and interpretation
are clear; a fresh framework implementation is not itself an academic contribution.

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
- similarities to and differences from the candidate question and proposed comparison;
- one concrete implication for this project’s experiment design.

Then broaden the search systematically across multi-agent safety, cascading failures and prompt injection, delegated authorization and capability control, runtime verification, operational risk, failure attribution, trace observability, and safety–utility evaluation. Record search sources, query strings, inclusion criteria, and the version of each reviewed paper.

Related work does not establish this project's novelty. A documented review helps
show what is answered, which methods can be reused, and where a defensible gap may
remain. A deliberate replication is also a valid choice when its purpose is clear.
Describe the selected study at the level its actual evidence supports.
