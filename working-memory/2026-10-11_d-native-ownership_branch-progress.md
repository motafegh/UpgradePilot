# D-native ownership — branch provenance and reconciled route

**Date:** 2026-10-11; current-main reconciliation 2026-10-15
**Branch:** `learning/d-native-ownership-2026-10-10`
**Synchronized main horizon:** `f518597c63cf5574c9da9bff2557679c33603482`
**Verified product implementation horizon:** `9d39481933fa834af4a10b3f2758f1e079dfe178`
**Canonical cycle owner:** [Workspace native capture, reconstruction and durable publication — LbD cycle](2026-10-10_1552_workspace-native-capture-reconstruction-and-publication_lbd-cycle.md)

This note preserves branch provenance and navigation. [MEMORY.md](../MEMORY.md) owns the current main position; the canonical foundation cycle owns its phase progression and engineering proof. This branch remains the independent Stages 1–2 D/E learning continuation, not a second product workstream and not product proof.

## Parallel progression and reconciliation

The earlier branch-local-record exception avoided concurrent rewrites of the cycle record while native learning and main durable-publication engineering proceeded separately. Native D1 was already preserved before the split; commits `dc9f192c` and `ac2097fc` recorded D2/D3 and D4/D5 reasoning and corrections. Merge `e9a6160e` synchronized the branch with verified main. The record at `3c55da46` preserved D1–D7 coverage and regrouped remaining native topics around completed storage and combined engineering proof.

Ali then requested independent branch/main learning review and explicitly authorized incorporating the full recommendations and pushing this branch. Native ownership findings and the complete remaining route were reconciled into the [combined-D cycle section](2026-10-10_1552_workspace-native-capture-reconstruction-and-publication_lbd-cycle.md#combined-d-learning-route-and-parallel-ownership-reconciliation--2026-10-11). Earlier detailed branch records remain in Git ancestry and have not been discarded or rewritten.

## Learning evidence and coverage navigation

- [Recorded native D1–D7 coverage and evidence limits](2026-10-10_1552_workspace-native-capture-reconstruction-and-publication_lbd-cycle.md#native-ownership-carried-forward-without-restarting). D2–D5 preserve concrete reasoning; D6/D7 carry synchronized coverage marks with a concise evidence limitation, without inventing unseen learner answers.
- [Remaining route and depth](2026-10-10_1552_workspace-native-capture-reconstruction-and-publication_lbd-cycle.md#remaining-route-coverage-and-depth): historical material/outcomes, three durable-publication lessons, combined recovery, two domain traces/proof, limits/critique/synthesis. Former D8–D15 topics remain accounted for.
- [Storage audit cases and proof](2026-10-10_1552_workspace-native-capture-reconstruction-and-publication_lbd-cycle.md#block-4--durable-publication): absence/coherence, staged identity, retained A/B/C history, failed-create cleanup, shared missing-head classification and coherence before conflict.
- [Combined recovery](2026-10-10_1552_workspace-native-capture-reconstruction-and-publication_lbd-cycle.md#block-5--combined-durable-recovery).
- [Domain traces and evidence interpretation](2026-10-10_1552_workspace-native-capture-reconstruction-and-publication_lbd-cycle.md#block-6--domain-traces-and-proof-design), including fresh-child guards, installed execution, actual harness failures and temporary-evidence limits.
- [Claim limits and ownership synthesis](2026-10-10_1552_workspace-native-capture-reconstruction-and-publication_lbd-cycle.md#block-7--claim-limits-architecture-critique-and-ownership-synthesis), then [preservation and stop boundary](2026-10-10_1552_workspace-native-capture-reconstruction-and-publication_lbd-cycle.md#preservation-verification-and-stop-boundary).

Preserve D1–D7 without restarting. Product source/test proof remains owned by main; branch learning never upgrades an engineering claim by itself.

## Learning evidence after reconciliation — 2026-10-13

**Block 3 — Historical material and outcome meaning: completed with meaningful interaction.** This is evidence for later canonical reconciliation, not a second live checklist. Ali demonstrated the following distinctions against the synchronized implementation and storage repair history:

- Recovery may validate that a retained result is bound to its retained historical inputs, but must not rerun today's selector/evaluator to replace the historical owner conclusion.
- `target_python` with `outcome=recorded` and no retained source/result is contradictory and must refuse; the same empty representation with `outcome=not_evaluated` is a truthful unexecuted historical state.
- A recorded selector `None` is historical abstention, not missing selection and not permission for recovery to infer a new read merely because the pre-assessment was unresolved.
- A recorded target-Python selection followed by explicit `target_python=not_evaluated` is a coherent selected-but-unexecuted prefix; recovery preserves it rather than deciding whether execution should continue.
- Storage absence, missing selected revision, damaged lineage, writer conflict and acknowledgement uncertainty are different states. In the concrete repaired publication-order case, retained revisions with a missing head must classify as `invalid_checkpoint_storage` before ordinary predecessor-conflict handling; corruption must not masquerade as concurrency.

No technical contradiction was found. No product code/test/architecture change or new verification claim is implied by this learning record.

## Current-main architecture reconciliation — 2026-10-15

Main advanced materially after the earlier `f8047c5b` synchronization. Stage 3 is now implemented and verified at product horizon `9d394819`, while later main commits through `f518597c` are planning/learning records. The foundation concepts already learned remain valid, but the remaining route must use the current composed Workspace rather than teach the older native-only picture as current architecture.

Current additions that affect this learning route:

- `CheckpointRevision` now retains the native `CapturedNativeBoundary` plus optional `CapturedLifecycleHistory`. Native-only/schema-1 history preserves its old digest contract; composed history uses the versioned lifecycle digest. Missing lifecycle history is distinct from an explicitly empty retained lifecycle run.
- Publication lineage and present material validity are now concrete separate owners. `predecessor_id` answers which Workspace revision a publication extends; `material_validity.py` checks exact target/scope/method/capability and the transitive native material actually used. Revision inequality alone is not staleness.
- The generic synchronous lifecycle host is production code. It owns current admission, durable intent, observations/interruption handling, native-owner feedback and lifecycle orchestration; it does not own domain truth. The Python selected-read/reassessment path is the first production caller/proof case, not the universal architecture.
- Stage 3 has its own learning companion. At main `f518597c`, D1–D3 are complete and D4 remains pending. Do not duplicate those lessons here; use them only when they clarify a foundation boundary.
- The next engineering cycle, common Investigator native inputs/source interfaces, is independently at A2 pre-B. It does not become part of foundation D merely because it is current main work.

### Adjusted remaining foundation route

1. **Block 4 / Lesson 1 — durable identity and atomic publication: KEEP, CURRENT-MAIN FORM.** Continue `lineage_id` / `revision_id` / `predecessor_id`, immutable material versus mutable lineage head, record/payload/reference/revision membership and transaction ordering. Teach against the composed revision and explicitly contrast **publication predecessor** with **material basis/current validity**.
2. **Block 4 / Lesson 2 — storage failure and acknowledgement: KEEP.** Preserve absence/damage/conflict/unconfirmed-publication and staged-identity inspection. Stage 3's `intent_recorded` / `not_started` / unknown external completion states are a related but separately learned lifecycle responsibility; reference rather than reteach them.
3. **Block 4 / Lesson 3 — retention, backup and durability: KEEP + VERSION UPDATE.** Include lifecycle history, schema/version compatibility/refusal and missing-history versus empty-history meaning while retaining WAL/FULL, online backup and power-loss claim limits.
4. **Block 5 — combined recovery: UPDATE TO COMPOSED CHECKPOINT.** Reconstruct native plus retained lifecycle history where supported, while preserving historical inspection as non-executing. Avoid duplicating Stage 3 D4's end-to-end host ownership; refetch its state before teaching this block.
5. **Block 6 — domain traces/proof: REFRESH BEFORE TEACHING.** The Python path now traverses the generic host for selected repository read/reassessment. Re-fetch current source/tests and trace the actual present flow rather than teaching the pre-Stage-3 orchestration as current.
6. **Block 7 — claim limits/architecture critique: REWORK AGAINST IMPLEMENTED PRESSURE.** Generic host and material-validity separation are no longer hypothetical recommendations. Critique what remains duplicated/unsupported and the later family/consumer/continuation/semantic/usefulness boundaries instead.

### Immediate continuation

Resume Foundation Block 4 Lesson 1 after this synchronization. The next ownership distinction is:

```text
Workspace publication relationship:
    predecessor_id / lineage head

is separate from

current-use evidence relationship:
    original basis / exact transitive material / target / scope / method / capability
```

The first controls coherent history and competing writers. The second decides whether retained material is presently usable. Neither grants domain truth or current execution authority.

Before Blocks 5–7, re-fetch main because Stage 3 D4 and the common-Investigator preparation may advance independently.

Procedural provenance: earlier learning used `UP-SKILL:upgradepilot-learning-by-doing` and `UP-SKILL:upgradepilot-working-memory`; synchronization/review used `UP-SKILL:upgradepilot-repository-audit` and `UP-SKILL:upgradepilot-workstream-supervision`; this current-main reconciliation preserves those boundaries and does not create a second product plan.
