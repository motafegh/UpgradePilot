# Stage 3 deferred D learning — todo and progress

**Created:** 2026-10-15
**Parent cycle:** [Workspace lifecycle, host admission and material-basis validity](2026-10-13_2030_workspace-lifecycle-admission-and-material-basis_lbd-cycle.md)
**Status:** ACTIVE learning companion for the parent cycle's explicitly deferred D/learner-ownership work. It does not reopen Stage 3 engineering B/Verification/E, change product scope, or claim mastery.
**Purpose:** consolidate the verified Stage 3 result through real UpgradePilot code/tests and Product Simulation cases, record our reasoning, and surface any material contradiction back to the responsible owner before claiming learner ownership.

## Minimal learning plan

Follow these steps in order unless evidence gives a reason to change the sequence.

- [x] **D1 — Original basis vs current material validity vs current execution authority**
  - Use the real `material_validity.py`/host behavior plus S013/S016-style cases.
  - Be able to explain why a lifecycle record keeps its historical basis, why unrelated same-target progress may remain valid, why material/target/scope/method changes may make current use stale/unsupported, and why evidential validity still does not grant execution authority.
  - Resolve the parent cycle's first deferred A2 reasoning check.

- [x] **D2 — Published intent vs known non-execution vs unknown completion vs retry authority**
  - Use the real repository-read path, interruption/lost-acknowledgement controls and recovery behavior.
  - Be able to distinguish `intent_recorded`, `not_started`, completion unknown and completed observation/problem, and explain why none of these automatically grants retry authority.
  - Resolve the parent cycle's second deferred A2 reasoning check.

- [ ] **D3 — Generic host and intelligence/truth authority boundaries**
  - Trace the real Python-support caller through the generic host, then map S013–S016 onto a future Investigator.
  - Distinguish native/domain-owned `InvestigationNeed` and evaluation from attributed proposals, capability admission, observable use, procedural termination and unsupported adequacy.
  - Confirm that the Python path is the first caller/proof case, not host architecture or universal investigation policy.

- [ ] **D4 — End-to-end Stage 3 ownership and proof boundary**
  - Reconstruct one complete normal flow from native partial capture → need/request/admission → published intent → observation/problem → native reassessment → immutable Workspace successor → cold historical inspection.
  - Review partial capture, immutable closure, schema/version compatibility and the implementation failures/repairs discovered during verification.
  - State clearly what Stage 3 proves and does not prove: no model usefulness, generic semantic/adequacy competence, replay, exactly-once effects, power-loss guarantee, full native-family/report migration or user-facing continuation.

## Progress notes

### D1 — 2026-10-15

1. **Evidence used** — `workspace/material_validity.py`, the host's `current_validity()` and `_execution_refusal()` paths, plus the verified same-target/unrelated-vs-material-change controls discussed in the parent cycle.
2. **Ali's explanation** — For a request created at R5, unrelated later progress does not make it stale when target/scope/method/capability and actual dependencies are unchanged. If execution authority is removed, the historical/current material can remain valid while the action is not authorized. If a native premise the request actually depends on changes, current use becomes stale.
3. **What it proves / does not prove** — Original basis remains historical and is never rewritten to the newest revision. Material validity answers present usability, not execution permission. Current authority is a separate present-time host decision. A stale material basis also blocks execution even when authority otherwise exists.
4. **Open confusion or gap** — No material conceptual gap remains for D1. Code-level expectation clarified: learn the small decision logic inside the relevant functions, not merely their names and not every implementation line.
5. **Disposition** — D1 sufficiently learned for this responsibility; first deferred A2 reasoning check resolved. Continue to D2.

### D2 — 2026-10-15

1. **Evidence used** — `workspace/lifecycle_records.py`, `workspace/lifecycle_host.py` (`execute_admission()`, `_publish()`, `attempt_completion()` and retry refusal), the repository-read adapter's completed `problem` result path, and host-integration tests for failed intent publication, authority withdrawal after intent, unknown completion, lost acknowledgement and duplicate execution refusal.
2. **Ali's explanation** — If intent publication fails before being established, the provider is not entered and the host must not continue automatically. If intent is recorded but authority disappears before the provider call, the attempt is `not_started`. If the provider is entered and an unexpected error occurs without a retained observation, completion is unknown and automatic retry is unsafe. A bounded provider/acquisition problem returned by the adapter is still a completed observation, not unknown completion.
3. **What it proves / does not prove** — Published intent is a durable pre-interaction fact, not evidence of completion. `not_started` requires positive retained evidence that the external call was not entered. Unknown completion preserves ambiguity instead of converting an exception into non-execution. A completed `problem` observation proves only that the admitted capability returned that bounded result. Any previous attempt blocks automatic retry; historical admission/intent do not restore live execution permission.
4. **Open confusion or gap** — No material D2 gap remains. Useful cross-domain analogy recorded: the ordering is CEI-like (`check` current authority/material → durably record internal intent → external interaction), but unlike Solidity CEI it is not primarily a reentrancy pattern and does not provide one-transaction atomic rollback across SQLite and an external provider. The durable intent/observation/interruption model exists because those systems can fail independently and leave ambiguous completion.
5. **Disposition** — D2 sufficiently learned for this responsibility; second deferred A2 reasoning check resolved. Continue to D3.

## How we record progress

For each D step, append a short dated note containing:

1. **Evidence used** — exact source/test/case or verified behavior we examined.
2. **My explanation** — the concept in Ali's own words, not just agreement with the assistant.
3. **What it proves / does not prove** — especially authority, provenance, semantic and recovery limits.
4. **Open confusion or gap** — anything still unclear.
5. **Disposition** — learned sufficiently for this responsibility, needs another example, or material issue requiring reconciliation with the parent cycle/owner.

Passing tests or agreement with an explanation is not learner-ownership evidence by itself. A material learning finding that contradicts a Stage 3 engineering premise should be reconciled with the responsible plan/spec/source before proceeding as if the premise were settled.

## Coordination with the current engineering cycle

The active engineering continuation is the [Common Investigator native inputs/source interfaces cycle](2026-10-14_2345_common-investigator-inputs-and-source-interfaces_lbd-cycle.md). Its A/B progression may continue independently under its own gates. This D companion should inform that work when relevant, but ordinary pending learning does not block it. If our learning reveals a real contradiction affecting the new cycle's assumptions, surface it before the affected Build decision.

## Completion condition

This companion is complete when D1–D4 have evidence-backed notes, both deferred A2 reasoning checks have been answered in Ali's own reasoning, any material gaps have an explicit repair/defer disposition, and we can truthfully update the parent cycle's learner-ownership status without changing its already-verified engineering claims.