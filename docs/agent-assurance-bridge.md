# Agent Assurance as a research source

The VIP studies agentic risk and assurance through bounded business case studies, one per pair. Agent Assurance supplies candidate assumptions, threat patterns, controls, and evidence practices alongside independent academic literature; it does not select the semester question. A result may support an assumption, narrow its applicability, or challenge it. Completing the methodology's institutional templates is not a semester deliverable.

## Version inspected

This map summarizes and adapts [Fengze Zhong's Agent Assurance repository](https://github.com/zhongnz/agent_assurance/tree/4c23d50cdc416586c389cca3ee4499ce45e7c621), commit `4c23d50cdc416586c389cca3ee4499ce45e7c621` (repository version v0.8.30), inspected September 15, 2026. Its [license](https://github.com/zhongnz/agent_assurance/blob/4c23d50cdc416586c389cca3ee4499ce45e7c621/LICENSE) is CC BY 4.0. The research interpretations below are VIP adaptations, not claims established by the source.

The pinned [control matrix](https://github.com/zhongnz/agent_assurance/blob/4c23d50cdc416586c389cca3ee4499ce45e7c621/paper/control_matrix.md) contains 26 controls. [Minimum Viable Assurance](https://github.com/zhongnz/agent_assurance/blob/4c23d50cdc416586c389cca3ee4499ce45e7c621/MINIMUM_VIABLE_ASSURANCE.md) selects ten; IA-03, MC-01, TF-01, ZC-01, and AT-01 are in that subset, while IA-02, CF-01, MC-02, IC-01, and AT-03 are outside it. MVA is an institutional adoption sequence, not the VIP syllabus.

## Examples relevant to Candidate A

| Source control and exact title | Useful VIP question or practice | Limit of the connection |
|---|---|---|
| **IA-02 — Service-account authority limitation** | Record which component may request or execute each action; test enforcement of those permissions. | IA-02 is specifically about service accounts, which the local stub does not instantiate. Generic caps are related mechanism checks, not an IA-02 implementation. |
| **IA-03 — Authentication strength for high-authority actions** | Identify the action boundary at which stronger authorization may be warranted. | The source specifies authentication strength. Our proposed evidence verifier does not manipulate authentication or test IA-03 in full. |
| **CF-01 — Failure-domain isolation and cascade prevention** | Test whether one intervention prevents a local information error from becoming an incorrect simulated action. | One gate tests a narrow containment assumption, not every isolation, circuit-breaker, or recovery requirement. |
| **AT-01 — Runtime evidence capture** | Preserve observable inputs, messages, tool definitions/calls/results, model responses, and final actions so traces can be audited. | Logging is a method requirement here; attribution accuracy is a separate future experiment. Capture exposed outputs only, not unavailable internal reasoning. |

[Candidate A](studies/01-runtime-containment.md) proposes a practical containment package with authority held constant. It is unselected and receives the same review as any other proposed pair case under the [study-selection process](studies/README.md#selection-and-protocol). If selected, its design is more precise than describing a recommendation-only agent's inability to execute as proof of a control's effectiveness.

## Other candidate directions

| Source concept | Bounded question or experiment |
|---|---|
| **MC-01 — Retrieval-context integrity; MC-02 — Memory-poisoning detection and response** | Corrupt one retrieval item or memory entry; compare how source verification or memory isolation affects propagation and useful task completion. |
| **IC-01 — Inter-agent message authentication and policy enforcement** | Manipulate sender identity or permitted message/action classes. Semantic contamination alone does not test message authentication. |
| **TF-01 — Toxic-flow analysis of authorised tool inventory** | Predict paths from untrusted input through privileged-data access to egress, then probe whether they occur and where a gate interrupts them. Any formal node-type system would be a VIP extension to the source's static analysis. |
| **ZC-01 — Asynchronous-processing risk gating** | In a background/queue-driven workflow, test gates on outbound invocations caused by untrusted content. The synchronous pilot does not meet this control's specific setting. |
| **LT-01 — Lethal trifecta architectural review; LT-02 — Egress-channel inventory and control** | Vary sensitive-data access and egress routes in a synthetic sandbox and measure unauthorized disclosure, alongside legitimate task outcomes. |
| **AT-03 — Evidence-store reconstruction queryability**, with AT-01 | Test reconstruction by session ID, output, network anomaly, or input pattern, measuring completeness and latency without custom per-query code. An evidence-view attribution comparison is a distinct AT-01-inspired study with blinded labels and attribution accuracy. |

These are research directions, not a syllabus, a promise to implement each control, or a fixed sequence for future cohorts. Each pair develops a bounded outline and evidence plan using the adjustable [semester targets](semester-plan.md#calendar-and-working-targets). Any proposal still needs primary literature, accessible evidence, clear measures and a recorded method. Prespecify evaluation rules for confirmatory claims; routine refinements need a dated note, not instructor sign-off.

## Three small artifacts to borrow

Combine the following in the pair's [case document](studies/_case-template.md); do not create three extra required reports. Start with a simple workflow sketch and add detail only as needed.

1. **Architecture and authority map.** One table of roles, inputs, tools, permissions, memory, outputs, and outbound capability. Adapt the [agent inventory](https://github.com/zhongnz/agent_assurance/blob/4c23d50cdc416586c389cca3ee4499ce45e7c621/assurance_kit/agent_inventory_template.md) to the experiment rather than collecting institutional governance fields.
2. **Predicted propagation path.** Before running, name the injected fault, expected downstream path, intervention point, and assumptions that could fail. The [toxic-flow template](https://github.com/zhongnz/agent_assurance/blob/4c23d50cdc416586c389cca3ee4499ce45e7c621/assurance_kit/toxic_flow_analysis_template.md) informs this practice. Its specific toxic flows require privileged-data access and egress: Candidate A would test a propagation path, not exfiltration or a full TF-01 assessment.
3. **Evidence map.** Link each proposed claim to the needed fields in the trace and analysis. Adapt the [capture checklist](https://github.com/zhongnz/agent_assurance/blob/4c23d50cdc416586c389cca3ee4499ce45e7c621/assurance_kit/evidence_capture_checklist.md); distinguish missing evidence from evidence that no failure occurred.

Candidate A's inventory and predicted path live in its proposal; another selected study should create only the compact artifacts its claim needs. The run record uses [experiment-record.md](experiment-record.md). Students do not need nine separate assurance documents.

Authority permits an action; it does not establish that the action is correct. Likewise, consequence is broader than state mutation: an incorrect no-op, omission, or decision to retain the current state may still be consequential. Preserve those distinctions when turning any source control into an empirical outcome.

## Research independence and feedback

The pinned [overview](https://github.com/zhongnz/agent_assurance/blob/4c23d50cdc416586c389cca3ee4499ce45e7c621/OVERVIEW.md) describes a preliminary methodology with structured self-review and pending external review. The VIP can supply new empirical scrutiny, but an affiliated cohort is not automatically an external or independent validation body.

State the relationship to the methodology's author in reports. Predeclare hypotheses and outcomes, preserve null/adverse findings, use independent literature and baselines, and seek review from someone outside the design team where feasible. A second analyst in the same cohort provides a reproduction check, not external peer review.

For each finding, record **source assumption → experiment → observed result → scope/limitations → suggested revision**. Feed supported findings back through an attributed report or separately authorized upstream contribution. No VIP result certifies the methodology, proves regulatory compliance, or requires the source project to accept a revision.
