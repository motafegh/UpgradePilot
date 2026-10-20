# Stage 3 architecture and end-to-end evidence-flow audit

**Date:** 2026-10-20  
**Status:** CLOSED — architecture/source-flow classified; no migration Build authorized  
**Mode:** cross-responsibility Repository Audit  
**Branch:** `audit/project-wide-system-audit-2026-10-20`  
**Main base reconciled:** `a1c291c6cf9238493eeb666b184192ed178b90f1`  
**Program:** [Project-wide technical audit and correction program](../plans/PROJECT_WIDE_TECHNICAL_AUDIT_AND_CORRECTION_PROGRAM_PLAN.md)  
**Prior result:** [AUDIT-014](../audits/2026-10-20_AUDIT-014_product-value-and-evaluation-sequencing.md)  
**Durable result:** [AUDIT-015](../audits/2026-10-20_AUDIT-015_workspace-authority-and-consumer-cutover.md)

## Audit-program cadence

`reconcile → audit/classify → verify → record → fix/route when justified → continue`

No separate D/E learning ceremony is required for this audit slice.

## 1. Question answered

Stage 3 traced the actual normal product path and compared it with ADR-0012/0013 and the Workspace migration plan.

Primary trace:

```text
public PR acquisition
→ shared native producers/evaluators
├→ NativeInvestigationCapture → Workspace host/revision
└→ orchestration-local PublicPullRequestInvestigation
      → maintainer-action synthesis
      → report projection
      → CLI/save/open
```

## 2. Main result

The Workspace architecture itself remains sound. The current implementation does **not** rerun the same domain evaluations to create a second semantic truth system: capture records the same native producer values, and admitted native reconstruction is offline decoding/binding validation.

But the replacement migration is still incomplete:

- the legacy result is assembled directly from local producer values, not reconstructed from Workspace;
- synthesis and report still consume the legacy result directly;
- Workspace codecs cover an initial CI/runtime/Python-support closure, not every fact currently used by report/synthesis;
- CLI normal output therefore remains legacy-consumer driven while carrying a Workspace revision alongside;
- durable Workspace recovery is not the default CLI path yet.

This state is explicitly anticipated by the Workspace implementation plan, so it is migration debt/proof gap rather than an ADR violation.

## 3. Classified findings

- **F1 — P1 migration blocker:** direct synthesis/report cutover is not complete. Do not claim the complete normal product is Workspace-canonical yet.
- **F2 — P1 before default cutover:** Workspace family coverage is narrower than the current report responsibility. Missing families/material must be captured/reconstructed or the product scope deliberately narrowed by its owner.
- **F3 — P2:** overlapping legacy/Workspace values share one producer but are not structurally one-way. A future edit can drift unless parity tests/ledger catch it; retire the parallel path rather than growing permanent parity machinery.
- **F4 — RETAIN:** native processing is not duplicated for Workspace; capture/reconstruction authority separation is good.
- **F5 — RETAIN with scope:** `prepare_dependency_ci_workspace` is an explicit partial bootstrap reusing the same shared owners, not a separate semantic implementation. Keep it bounded to a real consumer.
- **F6 — RETAIN:** saved-report reopening, Workspace recovery and deterministic replay remain correctly distinct.
- **F7 — P2 staged limitation:** normal CLI does not yet provide durable Workspace recovery/continuation; this is acceptable only while documentation remains truthful about the incomplete gate.
- **F8 — P3 clarity:** “canonical” language should stay scoped to admitted Workspace families/lifecycle until full consumer cutover.

## 4. Proof reviewed

Current tests strongly establish the admitted Workspace subset:

- normal selected-read/reassessment goes through host admission/attempt/observation/evaluation;
- `result.workspace_revision == host.current` in the normal integration proof;
- fresh-process readers reconstruct CI/Python native values without provider/model/evaluator calls;
- store/backup/interruption/lifecycle controls are substantial;
- consumer access distinguishes availability, delivery, observed use, citation and semantic support.

Current report tests independently protect the legacy input path and its evidence/unknown/action semantics.

What is intentionally not yet proven is complete report/synthesis parity from Workspace across all current evidence families followed by legacy retirement.

## 5. Architectural disposition

Retain ADR-0012/0013. Do not introduce another generic truth/evidence framework and do not remove `PublicPullRequestInvestigation` prematurely.

Remaining migration closure should stay:

```text
complete legacy-field/material-family ledger
→ add only missing owner-specific capture/reconstruction required by current consumers
→ prove normal/recovered semantic parity
→ cut synthesis to Workspace-native/retained conclusion input
→ cut report/CLI to explicit Workspace projections
→ retain legacy bridge only for a named compatibility/proof caller
→ retire obsolete snapshot plumbing
```

The highest-value immediate preparation is the exact **legacy-field → native family/material → consumer → migration disposition** ledger, not another abstraction.

## 6. Handoff

Stage 3 closes without source refactoring.

**Next program stage:** Stage 4 — tests, proof, reproducibility and operational integrity.

Stage 4 should use the migration findings to determine:

- whether transitional dual-surface parity is sufficiently protected today;
- which current tests uniquely prove architecture versus duplicated implementation shape;
- the minimum proof set needed before direct Workspace consumer cutover;
- canonical hosted CI/branch-protection gap from AUDIT-013;
- Python support declaration versus actual proof;
- fresh-install/CLI/package/recovery/replay proof distinctions.

`UP-SKILL:upgradepilot-repository-audit`
