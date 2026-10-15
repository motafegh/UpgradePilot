# Stage 3 deferred D learning — todo and progress

**Created:** 2026-10-15
**Parent cycle:** [Workspace lifecycle, host admission and material-basis validity](2026-10-13_2030_workspace-lifecycle-admission-and-material-basis_lbd-cycle.md)
**Status:** CLOSED — D1–D4 sufficiently learned for the parent Stage 3 responsibility on 2026-10-15. Both deferred A2 reasoning checks are resolved from Ali's own explanations. This closure does not reopen Stage 3 engineering B/Verification/E, expand product scope, or claim mastery beyond the responsibility described below.
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

- [x] **D3 — Generic host and intelligence/truth authority boundaries**
  - Trace the real Python-support caller through the generic host, then map S013–S016 onto a future Investigator.
  - Distinguish native/domain-owned `InvestigationNeed` and evaluation from attributed proposals, capability admission, observable use, procedural termination and unsupported adequacy.
  - Confirm that the Python path is the first caller/proof case, not host architecture or universal investigation policy.

- [x] **D4 — End-to-end Stage 3 ownership and proof boundary**
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

### D3 — 2026-10-15

1. **Evidence used** — the real Python-support caller in `investigation.py`, plus `workspace/lifecycle_host.py` paths for `add_purpose()`, `evaluate_native()`, `prepare_view()`, `record_use()`, `propose()`, `evaluate_proposal()`, `propose_stop()` and `terminate()`.
2. **Ali's explanation** — LLMs/agents may make proposals but do not have authority to turn those proposals into product truth or execution authority. The generic host is mainly an orchestration/coordination and lifecycle-authority mechanism; semantic/domain meaning remains with the qualified native/domain owners, which the host can invoke. A proposed stop concerns stopping that investigation activity and does not by itself establish that the overall investigation is successful or adequate.
3. **What it proves / does not prove** — A trusted `InvestigationNeed` is owner/admission-backed and is not equivalent to an LLM suggestion. A successful generic capability observation does not authorize the host to invent a domain conclusion; the native owner performs the interpretation/evaluation and the host retains it. The LLM may still propose strong statements such as “the upgrade is safe,” but without an admitted semantic/adequacy evaluator the retained truth is only an attributed proposal plus an `unsupported` evaluation outcome, not safety. `StoppingProposal`, procedural termination and investigation adequacy are separate states; even a completed run does not establish maintainer action permission.
4. **Open confusion or gap** — No material D3 gap remains. Refinement recorded: the boundary is not that an LLM is forbidden from uttering a decision-like statement; it is that such a statement remains a proposal unless the appropriate evaluator/synthesis owner establishes stronger meaning.
5. **Disposition** — D3 sufficiently learned for this responsibility. The Python-support path is understood as the first production caller/proof case of the generic host, not as the architecture or universal investigation policy. Continue to D4.

### D4 — 2026-10-15

1. **Evidence used** — the Stage 3 normal production flow in `investigation.py`; `workspace/native_capture.py` partial-versus-completed capture semantics; the generic host request/admission/intent/observation/native-evaluation path; immutable Workspace publication/reconstruction behavior; and the recorded Stage 3 implementation/verification repairs for pending-input identity refresh, installed-test child-environment isolation and rejection retention on the original request basis.
2. **Ali's explanation** — `partial_snapshot()` contains the coherent native material the investigation truthfully has up to that point; it is not one request record and it does not claim completion. The generic host owns request admission/execution/lifecycle handling, while the Python/domain owner owns the semantic interpretation and reassessment. Procedural `completed` means the normal run reached its completion point, not that investigation adequacy, upgrade safety or maintainer action permission was established. After restart, historical admissions are not executed again because recovery restores history while live admissions/current execution authority are cleared.
3. **What it proves / does not prove** — Stage 3 now connects partial native capture → owner-backed need → request/admission → durable intent → bounded observation/interruption → native reassessment → immutable Workspace successor → cold historical inspection without changing the ownership boundaries learned in D1–D3. Historical recovery proves inspectability of supported retained state, not continuation, retry or replay. The Stage 3 verification establishes the admitted generic-host/native path and its tested failure distinctions; it does not establish model usefulness, generic semantic/adequacy competence, exactly-once external effects, power-loss durability, full native-family/report migration, user-facing continuation or replay.
4. **Open confusion or gap** — No material Stage 3 ownership contradiction remains. Two wording refinements were resolved during the check: `partial_snapshot()` is the whole coherent unfinished native boundary rather than a request record, and a recovered `RequestAdmission(admitted)` is historical rather than current executable authority.
5. **Disposition** — D4 sufficiently learned. D1–D4 and both deferred A2 reasoning checks are complete for this Stage 3 responsibility; no learning finding requires reopening Stage 3 engineering proof or changing the current common-Investigator preparation responsibility.

## How we record progress

For each D step, append a short dated note containing:

1. **Evidence used** — exact source/test/case or verified behavior we examined.
2. **My explanation** — the concept in Ali's own words, not just agreement with the assistant.
3. **What it proves / does not prove** — especially authority, provenance, semantic and recovery limits.
4. **Open confusion or gap** — anything still unclear.
5. **Disposition** — learned sufficiently for this responsibility, needs another example, or material issue requiring reconciliation with the parent cycle/owner.

Passing tests or agreement with an explanation is not learner-ownership evidence by itself. A material learning finding that contradicts a Stage 3 engineering premise should be reconciled with the responsible plan/spec/source before proceeding as if the premise were settled.

## Coordination with the current engineering cycle

The active engineering continuation is the [Common Investigator native inputs/source interfaces cycle](2026-10-14_2345_common-investigator-inputs-and-source-interfaces_lbd-cycle.md). Its progression remains independently owned by that cycle. This completed Stage 3 D review found no contradiction requiring it to stop or reopen Stage 3 engineering. Any future finding that materially changes a Stage 3 premise still returns to the responsible owner rather than silently changing history.

## Completion condition

**Satisfied on 2026-10-15.** D1–D4 have evidence-backed notes, both deferred A2 reasoning checks were answered in Ali's own reasoning, no material contradiction remains undisposed, and the parent Stage 3 cycle can truthfully mark learner ownership closed without changing its already-verified engineering claims.