# Investigator successor — controlled report-only diagnostic Build

Date: October 19, 2026 (Asia/Tehran). Primary operation: Build / Implement.
Session status: ACTIVE. Starting revision: `2b1a8cde` on main.
Previous: [successor planning cycle](2026-10-18_investigator-successor-planning_lbd-cycle.md).
Owner: [successor plan](../plans/INVESTIGATOR_RUN_CONTROL_COMPLETION_AND_CAPABILITY_DIAGNOSTIC_PLAN.md).

## Authorization, cadence and scope

Ali requested fully building the plan and progressively recording/documenting necessary work. This selects the plan's implementation and offline preparation/proof responsibilities. Model loading, zero-generation runtime preparation and bounded inference activation remain distinct later gates; no real prediction is included in this Build. Preserve the untracked October 3 audit-cycle file and all original experiment retention roots.

Continuous-context adaptation: the normal A1/A2 dialogue stops would repeat the just-accepted audit/planning orientation despite Ali explicitly selecting full Build. Compress those stops into visible source-grounded explanation plus recorded decisions while progressing the authorized work. New mechanism concepts and trade-offs are explained before implementation; learner mastery is not inferred. Consequential scope/claim changes still return to their owner. D/E will preserve actual evidence and defer unassessed learner ownership rather than manufacture it.

## Cycle status

- A0 — DONE: live owners/plan/recent main and relevant source/tests reconciled; this single cycle record created. No intervening tracked changes.
- A1 — DONE at directed continuity depth: audit and successor plan remain the basis; original matrix is immutable and withheld.
- A2 — DONE at directed Build depth: synchronous main-thread deadline/cancel ownership and fixed-packet/non-semantic proof boundaries explained; learner mastery remains unassessed.
- B — CURRENT: controlled model boundary and interruption/terminal accounting implemented; report-only preparation/offline feasibility follows.
- Verification gate — PENDING: focused deterministic/installed-SDK controls, experiment integration and nearest Workspace tests.
- D — PENDING: evidence-backed changed flow, failures/corrections, proof limits and learner gaps.
- E — PENDING: truthful implementation handoff; later runtime/freeze/activation gates remain separate.
- C — CONTINUOUS: preserve meaningful decisions, evolution, verification and handoff here.

## Living orientation map

Existing flow: `StatelessInvestigatorModel` packs/measures → `SDKBinding.predict` → strict adapter/report admission; `run_scripted_trial` owns procedural charges/termination; comparison orchestrator owns the loaded model. Current gaps: SDK timeout is per-message inactivity, `except Exception` misses `KeyboardInterrupt`, and finalizer failures can mask the primary cause. A supplied-evidence diagnostic must use its own report-only composition without weakening the fresh-trial guard.

Expected result: finite monotonic prediction/cancel boundaries; known usage distinct from reserved unknown; primary/secondary failure preservation; real typed packet references; one report attempt whose complete capacity is proved before dispatch. Synthetic/scripted proof is mechanical evidence only. Actual backend cancellation, rendered token fit, capability and maintainer value remain unproved without later authorized execution.

## Progressive record

### A0/source reconciliation and mechanism selection

Read the Build/LbD/Working Memory procedures, plan, live MEMORY, environment/security and relevant Operating Guide/source-clarity rules. Installed optional SDK remains the preserved 1.5.0 copy. Its `SyncChannel.cancel` sends on the same synchronous channel; receive waits have per-message timeouts. `PredictionStream` unwinds/closes on exceptions, so draining after interruption needs explicit ownership of the channel rather than pretending stream exit yields a usage receipt.

Selected mechanism: same-thread synchronous SDK channel with temporary POSIX `ITIMER_REAL`/signal deadline under the main WSL Python thread, with monotonic deadline checks and bounded cancellation/drain. This refines the synchronous control candidate, avoids cross-thread SDK ownership and avoids a contained worker when the same-thread route can prove its boundary. Reject unsupported threads/platforms or an already-owned timer rather than disturb other timer owners. Prediction elapsed origin is dispatch entry; inactivity is separately bounded at the prediction allowance (normal prompt processing is not killed by an arbitrarily short idle timeout). Cancel/drain allowance is at most 60 seconds. Only an actual terminal protocol/usage receipt can establish completion; otherwise usage/quiescence remain unknown and block further prediction. Installed runtime transport still needs the plan's separately activated cancellation probe.

The necessary alternative was a worker with parent deadline. It would also need server cancellation/quiescence proof and adds process/IPC/ownership complexity; use it only if the synchronous deterministic/installed-source proof fails. No SDK/transport/dependency change is selected.

### Control implementation and discriminating failures

Added `experiments/investigator_run_control.py`: one main-thread monotonic deadline interrupts silence/continuous traffic, then cancel/drain/channel release share a bounded finalization period. SIGTERM becomes handled `SystemExit(143)` and KeyboardInterrupt remains an interruption. A late terminal success preserves its metadata without turning the elapsed violation into a successful report. An existing timer owner is refused.

`StatelessInvestigatorModel` now reserves immutable attempt evidence before dispatch; BaseException paths retain unknown versus actual scalar usage, original visible prefixes and separate secondary failures. Failed models block reuse even with known usage. Response validation/storage and attempt finalization share the remaining 60-second allowance after channel finalization. The scripted driver terminates on interruption, retains a result for orchestration and re-raises; terminal-publication failure no longer replaces the prediction cause. Comparison runtime cleanup is bounded and confirmed separately, without unloading an unowned instance. The new controller is part of prospective code hashes; old freezes/retention stay immutable and cannot pass as fresh admission.

The installed SDK test caught a real exception-class collision: its receive loop catches `concurrent.futures.TimeoutError`, the built-in TimeoutError alias, so inheriting our elapsed-deadline exception from TimeoutError hid the distinction as an SDK idle timeout. Use a distinct Exception subtype; actual preserved SDK queue waiting and same-channel cancellation now pass without network/inference. A test assertion also used the wrong existing result-field name and was corrected to `original_responses`.

Initial test invocations exposed checkout import conventions, not behavioral failures: use `PYTHONPATH=src:.` for experiment tests and add `tests` for product test modules that import sibling helpers. No environment/package installation was changed. Focused control/model/trial proof passes 62 tests with the preserved SDK explicitly on PYTHONPATH. The separately run seam family passes 74 tests; the first combined invocation had three product-module import errors, so those product families are rerun with the correct path. Ruff is absent from the existing project environment; no dependency was installed merely to obtain a formatter.

The final control increment adds the known-usage cancellation case: actual scalar spend remains known while a failed/late attempt blocks reuse and has no admitted visible response. Final control proof: 63 focused tests with installed SDK selected, 74 seam tests and 65 nearest Workspace controls pass (202 total), plus compile/diff checks. [Public evidence](evidence/2026-10-19-investigator-successor-build/README.md) binds commands, counts, source hashes and limitations. This remains an in-progress Build cycle; publication of the coherent control increment does not activate inference or claim the whole successor complete.

Procedural provenance: `UP-SKILL:upgradepilot-build-implement`; `UP-SKILL:upgradepilot-learning-by-doing`; `UP-SKILL:upgradepilot-working-memory`.
