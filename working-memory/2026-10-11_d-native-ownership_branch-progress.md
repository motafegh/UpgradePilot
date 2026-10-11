# D-native ownership — branch-local progress

**Date:** 2026-10-11
**Branch:** `learning/d-native-ownership-2026-10-10`
**Canonical cycle owner:** [Workspace native capture, reconstruction and durable publication — LbD cycle](2026-10-10_1552_workspace-native-capture-reconstruction-and-publication_lbd-cycle.md)
**Purpose:** temporary branch-local Phase-D progression while `main` continues durable-publication B in parallel.

This file is **not** a competing phase-status owner and does not create a new LbD cycle. Under the repository Smart Situational Override, the normal rule of progressively updating the single active cycle record is temporarily displaced because the learning branch and `main` are intentionally advancing in parallel and may both touch the canonical cycle record. Keeping the D-learning delta here avoids concurrent whole-file rewrites and merge loss. Before this branch is merged/rebased back, reconcile these findings into the canonical cycle record and then retire or preserve this note only as branch provenance as appropriate.

Procedural provenance: `UP-SKILL:upgradepilot-learning-by-doing`; `UP-SKILL:upgradepilot-working-memory`.

## Established ownership

- [x] **D1 — Why native recovery exists and where it stops.** Already recorded in the canonical cycle record before this branch split. Ali distinguished recovery from replay/fresh investigation/current continuation, correctly required unsupported old codec/schema/semantic versions to refuse instead of rerun, and kept exact-target recovery separate from later continuation authority.

- [x] **D2 — Actual source/control flow.** Ali traced and reasoned through the implemented path from normal owner results into `NativeInvestigationCapture`, explicit `not_evaluated` staging, the completion gate, sealing into `CapturedNativeBoundary`, `read_native_boundary`, and consumer-specific CI/Python reconstruction. Ownership demonstrated:
  - capture receives the actual objects produced by the normal investigation and must not reopen/reparse/re-evaluate them;
  - explicit `not_evaluated` distinguishes an operation that never ran from missing/corrupt retained material;
  - staged records do not imply a completed historical investigation; `complete()` is the current normal-orchestration sealing gate;
  - `read_native_boundary()` proves format/target/digest/reference closure, while consumer projections still decode supported families and validate owner/version/outcome/material relationships before exposing typed historical values;
  - recovery/projection does not grant replay, semantic re-evaluation, synthesis or continuation authority.

- [x] **D3 — The 11 native families and 18 declared edges.** Ali understands the families as retained responsibility/result groups and the edges as declared historical material dependencies rather than arbitrary graph bookkeeping. Ownership demonstrated:
  - CI/runtime results cannot be accepted merely because each payload has a valid digest; downstream results must remain bound to the exact retained investigation/CI material they claim to depend on;
  - Python target relevance needs both the upstream support-drop basis and the target-side Python declaration because relevance is a comparison of those two historical sides;
  - a digest proves byte integrity relative to the stored digest, not that independently valid records belong together historically;
  - Ali challenged an initially confusing example and correctly identified that normal encode→decode should preserve the same value. The clarified threat is an incoherent combination of individually valid records, not random codec mutation. Compact distinction: **codec correctness != graph coherence**.

## Useful clarification captured during D3

Current reconstruction does **not** manually serialize every UpgradePilot layer. It defines explicit fixed codecs/layouts for the selected native families; runtime encoding is automatic through those contracts. The current scope is the 11 native roots (with their reachable fixed layouts/variants), not the complete product. This clarification feeds later D6/D13/D14.

## Remaining formal D-native route

- [ ] **D4 — Trust vocabulary:** integrity vs coherence vs authenticity/admission vs freshness/current validity.
- [ ] **D5 — Capture vs storage/publication vs recovery responsibility.** Separate root-cause ownership from recovery refusal responsibility without duplicating every owner/evaluator.
- [ ] **D6 — Codec/version/provenance model.** Boundary format, family codec version, producer method identity and producer semantic version; unrelated unsupported-family behavior.
- [ ] **D7 — Boundary/representation validation.** Exact target, digest/reference closure, fixed layouts/variants, bounded JSON/resource limits and constructor-normalization refusal.
- [ ] **D8 — Structural/material binding vs semantic re-evaluation.** Use the real repaired binding cases and identify the line where validation would become replay/evaluation.
- [ ] **D9 — Outcome/lifecycle states.** `recorded`, `not_evaluated`, typed unavailable/problem results, unresolved, selector abstention, selected-but-unexecuted acquisition and coherent prefixes.
- [ ] **D10 — CI/runtime deep trace.** Dependency/source context → workflow/project inputs → CI coverage/correlation → runtime assessment/witness and proof limits.
- [ ] **D11 — Python-support deep trace.** Upstream authority/claim → pre-assessment → selection/abstention → target source/result → relevance → post-assessment.
- [ ] **D12 — Proof design.** Positive parity, valid-digest inconsistent-history controls, baseline-red, guarded fresh children, forbidden re-entry, unaffected projections and broader regressions.
- [ ] **D13 — Proof/non-proof and retained limitations.** Native-equivalent versus later obligations; missing producer semantic versions/call metadata/source content; no arbitrary checkpoint authentication, complete canonical recovery, continuation/replay/usefulness/power-loss claim.
- [ ] **D14 — Architecture/maintainability critique.** Shared validated historical Workspace/native graph or trusted core/IR pressure versus projection-local validation, without stealing domain semantic ownership.
- [ ] **D15 — Ownership synthesis.** Trace one CI/runtime and one Python-support case, explain integrity/coherence, exact-SHA limits, unsupported codec behavior, structural validation versus re-evaluation and critique the trusted-core/IR option.

## Current decision point

D1–D3 are meaningfully demonstrated. No technical contradiction has been found in the native reconstruction result during these learning steps. The next natural cluster is **D4 + D5**, because the questions already raised about digests, incoherent histories, capture/storage root causes and recovery refusal map directly onto the trust/responsibility vocabulary. D6/D7 should follow once that trust model is explicit; D8/D9 then apply it to concrete repaired cases and lifecycle states. D10–D13 deepen the two domain traces and proof boundaries, with D14/D15 reserved for architecture critique and synthesis.

Do not infer completion of any remaining item from this route. Each checkbox still requires meaningful interaction/ownership evidence before reconciliation into the canonical cycle record.
