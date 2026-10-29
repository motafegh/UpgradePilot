# Active Audits

This folder is the **active lifecycle index** for validated audit findings selected as inputs to the current engineering responsibility.

Canonical audit records remain at stable paths directly under `audits/`. Existing audits contain relative references written from that location, so lifecycle classification is represented here instead of physically relocating those files and silently breaking their reproducibility links.

Current active audits:

- [ACTIVE — AUDIT-013 — Experiment architecture, lifecycle and dependency boundaries](../2026-10-29_AUDIT-013_experiment-architecture-lifecycle-and-dependency-boundaries.md)
  - selection basis: Ali identified increasing reuse of older experiment modules by newer source/API experiments and selected an experiment-subsystem audit/repair responsibility after closure of the source-correspondence increment.
  - execution boundary: the implementing assistant must first perform an independent current-source inventory/import/lifecycle/frozen-evidence analysis and explicitly confirm, narrow, contradict or supersede AUDIT-013's initial observations before selecting repairs. The audit does not pre-authorize a mass folder move, historical evidence rewrite, experiment-to-product promotion or semantic/product behavior change. Organization/API-boundary repairs follow only from that reconstructed evidence; `../../MEMORY.md` remains the live continuation owner.

- [ACTIVE — AUDIT-012 — Whole-project value, capability and delivery](../2026-10-22_AUDIT-012_whole-project-value-capability-and-delivery.md)
  - selection basis: Ali accepted the next-investment reassessment and selected assistant-performed source-aware report review. Findings about value, source reachability, study scope and coordination inform bounded milestone design under the [direction plan](../../plans/PRODUCT_DIRECTION_AND_MAINTAINER_UTILITY_INVESTIGATION_PLAN.md) and [report plan](../../plans/MAINTAINER_REPORT_PRESERVATION_AND_USEFULNESS_EVALUATION_PLAN.md). This selection does not activate every audit recommendation, independent study, source Build, model inference or third capture. `../../MEMORY.md` alone owns live selection.

- [ACTIVE — AUDIT-011 — Investigator Experiment Validity, Bottlenecks and Useful Progress](../2026-10-18_AUDIT-011_investigator-experiment-validity-and-progress.md)
  - selection basis: Ali accepted the audit/amendment review and authorized writing the bounded successor plan, including the refinement that fixed-packet interpretation need not await a general adaptive discovery-budget implementation.
  - execution owner: [Investigator Run Control, Completion and Capability Diagnostic Plan](../../plans/INVESTIGATOR_RUN_CONTROL_COMPLETION_AND_CAPABILITY_DIAGNOSTIC_PLAN.md). Audit findings are selected planning inputs; this lifecycle entry grants no Build, model loading, inference, automatic navigation repair or product adoption. Original incomplete semantic evidence and its separate D/E boundary remain intact; `../../MEMORY.md` owns exact continuation.

- [ACTIVE — AUDIT-010 — Hybrid Investigation Architecture Compatibility and Interface Delta](../2026-10-07_AUDIT-010_hybrid-investigation-architecture-compatibility.md)
  - selection basis: Ali proposes a bounded workspace/Investigator-interface design responsibility following the completed interpretation-only research result at `74835751`.
  - execution owner: [Investigation Workspace and Investigator-interface Design Plan](../../plans/INVESTIGATION_WORKSPACE_AND_INVESTIGATOR_INTERFACE_DESIGN_PLAN.md); `../../MEMORY.md` alone owns the cycle phase and continuation.
  - selected input is the composition/update/proposal-admission delta. The original October7 review predates subsequent Workspace design, native implementation and Investigator experiment integration; its old non-selections are historical, not statements that those later responsibilities remain unselected. Accepted methods live in ADR-0012/0013, implementation truth in source/tests, and exact continuation in `../../MEMORY.md`. The original audit/proof cutoff remains unchanged; no new semantic/utility/action acceptance follows from the integration.

- [ACTIVE — AUDIT-009 — Post-Runtime-State Delta Readiness Audit](../2026-10-02_AUDIT-009_post-runtime-state-delta-readiness.md)
  - selection basis: Ali requested a full post-runtime-state delta audit and then authorized reconciliation of stale current-facing records before the next action-relative reachability comparison.
  - execution owners: `../../plans/END_TO_END_PRODUCT_FLOW_LEARNING_AND_EVIDENCE_TO_ACTION_EXECUTION_PLAN.md` and its parent `../../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`; `../../MEMORY.md` alone owns the exact live slice.
  - historical coordination boundary (2026-10-02): Runtime Dependency-State Cycle1 closure and Product Verification#17 were the review's evidence horizon. Later direction/report/Workspace work has its own owners and proof; the old next-action wording does not select current work. Retain the audit's runtime/action distinction as review input without authorizing runtime expansion, AI activation or a new action permission.

AUDIT-008 has been moved to ABSORBED because AUDIT-009 and the completed F3/F4/F9/F11/F6 records now carry its current conclusions forward. AUDIT-008 remains the historical baseline and source of finding provenance. AUDIT-005 remains SCHEDULED and is not the selected current engineering workstream.

Active audits remain **non-controlling evidence**. The active plan, specifications/ADRs where applicable, source/tests, and `MEMORY.md` own execution, stable decisions, behavior, and live continuation.

When an active audit is dispositioned, remove it from this index and add it to the appropriate lifecycle index under `../scheduled/`, `../deferred/`, or `../absorbed/` with an updated title and explicit rationale under `audits/LIFECYCLE.md`.
