# Investigator successor Build evidence

Owner: [Build cycle](../../2026-10-19_investigator-successor-build_lbd-cycle.md).
Scope: offline implementation proof under the [successor plan](../../../plans/INVESTIGATOR_RUN_CONTROL_COMPLETION_AND_CAPABILITY_DIAGNOSTIC_PLAN.md).

[Initial control proof](control-proof.json) records the first202 passing checks at `07e0a28b`. [Final Build proof](build-proof.json) records158 focused/control/report-only/runner/seam tests and65 nearest Workspace controls (223 distinct tests across this Build), current source hashes and limitations. The optional preserved SDK was selected for actual queue/cancel/timeout-restoration tests without a model server. Product source is unchanged; no dependency was installed.

**Readiness remains WITHHELD.** One real zero-generation runtime preflight loaded the intended Gemma12 point and stopped at the complete HTTPX packet exceeding16,000 input tokens. No prediction was attempted, no executable freeze was written, and owned unload/client release were confirmed. Exact rejected count/rendering was not retained by that initial preflight; only16,000 < tokens ≤24,320 is established from its passed context-reserve check and failed input-cap check. The remaining three semantic roles were unmeasured. [Runtime disposition](runtime-fit-disposition.json) preserves this limited negative evidence and its original source hashes. It is neither a semantic failure nor completed interface qualification.

The corrected preflight retains intent/current identity and every full packed/rendered measurement before disposition, including an over-context input. It measures all independent roles within one bounded preparation, then withholds the freeze if any cap/context gate fails. It shares no model output or review feedback across cases. These repairs passed deterministic tests; **the corrected preflight was not rerun against the backend**, and no cap increase or additional runtime attempt was selected.

## Packet and retention evidence

[Offline packet feasibility](offline-packet-feasibility.json) binds current-source preparation r5 and all four maximum-reference scripted publications/terminations:

| Packet | Trusted reads | Eligible references | Admission units through termination |
| --- | ---: | ---: | ---: |
| HTTPX PR context | 13 | 16 | 76 |
| Newer captured consumer | 3 | 3 | 23 |
| glyphsLib PR context | 10 | 13 | 61 |
| Older captured consumer | 3 | 3 | 23 |

The original12-read/12-reference/68-unit draft could not preserve the complete HTTPX recipe. The plan's prospective correction is13 reads/16 references/76 units per case; four cases plus two18-unit probes total340 units. Calls remain at most6, aggregate inputs72,192 and generation49,152; total batch4,800 seconds and preparation1,200 seconds. This is fixed report-only capacity, not a repair or resume of the original autonomous matrix.

[Static byte accounting](offline-byte-profile.json) records model-facing user-presentation bytes and source/native/schema components. It excludes actual tokenizer/chat-template/model-budget measurement and uses r5 host IDs. It is not a token estimate, an ablation result or permission to remove material. It helps localize the next packet/allowance investigation without another runtime call.

[Retention summary](private-retention-summary.json) binds200 owner-only files /3,146,996 bytes across the five immutable offline preparation snapshots, separate20-obligation reviewer protocol, failed runtime and its exact pre-repair source/disposition archive, excluding the aggregate index itself. Directories are0700 and files0600. These are local retention checks, not off-machine backup or a full model/runtime archive. Only r5 passes current preparation-source admission; older snapshots intentionally retain their old source horizon. Original prior experiment roots are untouched.

## Implementation route and operation boundaries

- [Run control](../../../experiments/investigator_run_control.py): same-thread monotonic deadlines, bounded cancel/drain/release, handled interruption and distinct requested/confirmed states.
- [Model boundary](../../../experiments/investigator_model_interface.py): complete request measurement, strict usage/settings/instance checks, immutable attempt/reservation evidence and failure-preserving finalization. `pack_complete` never removes required events; prediction still refuses an oversized input.
- [Report-only composition](../../../experiments/investigator_supplied_evidence.py): actual Workspace deliveries, honest trusted-preparation attribution, protected terminal capacity and one unmodified report attempt.
- [Recipes](../../../experiments/investigator_supplied_evidence_packets.json) and [offline preparation](../../../experiments/prepare_investigator_supplied_evidence.py): real selected source/native inventories, fresh reference IDs, maximum-reference feasibility and immutable retention checks. Reviewer files are outside the allowlisted packet construction.
- [Runtime/cohort runner](../../../experiments/run_investigator_supplied_evidence.py): `prepare-runtime` loads only the intended point and never predicts; `execute` needs an actual verified freeze plus its explicit matching activation hash. There is currently no executable freeze. The first cancellation probe is required; unknown usage or a hard failure withholds all later slots, with no retry/resume or semantic grading.

Six attempts reserve up to50 seconds each for shared transport/receipt/report/termination finalization; owned unload gets at most50 and client release10, retaining the360-second aggregate. Non-prediction RPC idle timeout is600 under the total deadlines; each prediction restores it after its own scoped allowance. Actual backend cancellation still needs the activated probe.

The next bounded responsibility is a versioned measurement-only packet/allowance disposition under the corrected code, before deciding on any token budget or presentation change. Do not spend unused inference slots, infer acceptance from a successful subset, or turn this failed readiness gate into a model-capability verdict. Canonical D/E and learner ownership remain pending in the cycle record.

## Reproduction of mechanical checks

Reproduction (run from repository root):

```sh
PYTHONPATH=src:.:/home/motafeq/.local/share/upgradepilot/investigator-runs/deployment-interface-2026-10-16-r1/sdk-1.5.0/lib/python3.12/site-packages .venv/bin/python -m unittest experiments.tests.test_investigator_run_control experiments.tests.test_investigator_model_interface experiments.tests.test_investigator_workspace_trial experiments.tests.test_investigator_supplied_evidence experiments.tests.test_investigator_supplied_evidence_runner experiments.tests.test_workspace_investigator_seam -q
PYTHONPATH=src:.:tests .venv/bin/python -m unittest test_workspace_consumer_access test_workspace_host_integration test_workspace_lifecycle_publication -q
```

The SDK path is the installed optional environment, not a new dependency. Without it, the SDK-specific queue/timeout proofs skip. These commands do not load models or request predictions. Scripted/fake-channel success does not qualify actual backend cancellation, real packet fit or semantic usefulness.
