# Activated supplied-evidence diagnostic: cancellation gate failure

Date: October 19, 2026. Execution/source horizon: `c4c833e6` on main.
Owner: [the same Build cycle](../../2026-10-19_investigator-successor-build_lbd-cycle.md), under [the successor plan](../../../plans/INVESTIGATOR_RUN_CONTROL_COMPLETION_AND_CAPABILITY_DIAGNOSTIC_PLAN.md).

The activated cohort is **incomplete and inconclusive**. Its first cancellation probe attempted one prediction, reached the declared monotonic deadline, requested cancellation and released the channel, but received no terminal response or usage. The runner withheld the report/reference canary and all four semantic cases. Owned model unload and SDK client cleanup confirmed afterward. No retry, report repair, additional model, resumed slot or semantic verdict followed.

Offline inspection found a concrete receive-ownership defect at the boundary between our signal deadline and the pinned SDK. A local counterexample using the exact installed SDK reproduces the lost terminal reply and observed channel-end error. This is a sufficient failure mechanism, not a captured reconstruction of the live server's messages. The old run's usage remains unknown.

## Exact execution and resource disposition

[The activation record](diagnostic-activation.json) binds Ali's directed continuation, source/SDK hashes, the six fixed roles and ceilings. It activated runtime-r4 freeze `a94101982226436f6ef993c80af041e2b425994aaa13afcbddd95714f65f8b42`, observed profile `7c43296f207f324725ee094a232206f57f2eb972df52224f8640f883742b5efd`, r7 preparation and the unchanged reviewer-only protocol. The selected point is Gemma12 at 36,864 context / 8,192 generation; this is the previously measured capacity point, with no new configuration change.

The fresh execution retained its exact freeze, backend/template observation, reference map, preliminary reservation, actual callback request/rendering, pre-dispatch attempt, receipt, visible fragment file, failed trial result, whole-cohort summary and both cleanup receipts. Existing admission rechecked source/SDK/profile/assets/input/reviewer identity; owned load validation and fresh probe fit passed before dispatch. No new complete terminal configuration receipt exists for the attempted prediction.

[The exact safe result](diagnostic-result.json) binds all 15 retained execution files by hash. The private execution root is `/home/motafeq/.local/share/upgradepilot/investigator-runs/supplied-evidence-2026-10-19-diagnostic-r1`.

| Role | Observed result | Semantic assessment |
| --- | --- | --- |
| Cancellation probe | One attempted prediction; deadline/cancellation requested; terminal/usage missing | Non-semantic probe; qualification failed |
| Report/reference canary | Unattempted after the hard gate | Not evaluated |
| HTTPX PR context | Unattempted | No report to review |
| Captured newer consumer | Unattempted | No report to review |
| glyphsLib PR context | Unattempted | No report to review |
| Captured older consumer | Unattempted | No report to review |

The one-second probe recorded prediction elapsed **1.000142099 seconds**. Reaching this deadline was intentional; a deadline exception alone was not its pass criterion. Passing also required an actual terminal protocol/configuration/usage receipt and channel release. The receipt records cancellation requested, channel released, terminal not received, and prediction-protocol quiescence unconfirmed. Its secondary problem is `ValueError: prediction channel ended without a terminal response`; cancel/drain/release took approximately **0.006032 seconds**, so the observed failure was not a 50-second drain timeout. Zero visible bytes and no complete response were retained.

The cohort summary records **one unknown-usage attempt, zero known-usage attempts, 12 admission units, 1.000142099 prediction seconds and 0.953319488 finalization seconds**, with batch elapsed **2.011390457 seconds**. The token fields `input: 0` and `generated: 0` are sums across zero known-usage calls, **not actual zero consumption**. The conservative role reservation remains **4,096 input / 8,192 generated tokens**. The callback's exact input reservation was 3,281; neither reservation is measured server usage. At most this one admitted request was dispatched, with no authorized retries; actual token consumption cannot be reconstructed from elapsed time or empty visible output.

Preliminary probe rendering counted 3,279 tokens; the fresh callback request counted 3,281, both within 4,096. They are separate preparation/packing observations with fresh budget/time metadata. This difference is not evidence of a measured prompt-usage mismatch: no terminal prompt-token count exists to compare. The retained request hash, packed-input hash, rendered hash and fragment hash agree with their receipt/attempt bindings, and the actual request omitted no events.

Owned cleanup subsequently confirms unloading identifier `up-supplied-capacity-gemma12-36864-v1`, no remaining loaded identifiers at that check, and client release. Those later receipts establish cleanup separately. They neither supply missing prediction usage nor retrospectively change the terminal-protocol quiescence field or qualify the probe.

## Receive-ownership finding

The failure crosses three owners:

1. [Our controller](../../../experiments/investigator_run_control.py) interrupts a blocking synchronous receive with a distinct `PredictionDeadlineExceeded`, retains the primary failure, then sends cancellation and begins a new bounded drain on the same channel.
2. Installed SDK 1.5.0 `AsyncWebsocketHandler._rx_queue_get_threadsafe` submits `rx_queue.get()` to its background event loop and waits on the returned future. It cancels that future only when `SyncFutureTimeout` is raised. Our custom deadline exception, `KeyboardInterrupt` and handled exit are outside that catch. An interrupted foreground wait can therefore leave its background queue consumer pending.
3. `SyncChannel.rx_stream` starts another queue get during drain. The abandoned first consumer can take the next terminal event; the new consumer then takes `channelClose`, which `ChannelHandler.handle_rx_message` maps to end-of-stream. No terminal success reaches `CapturedEndpoint`, so its scalar metadata capture never runs and our controller correctly records a missing-terminal failure.

The SDK's `ChatResponseEndpoint` explicitly supports a `success` event after cancellation carrying stats and configuration; cancellation therefore does not inherently mean there can be no terminal receipt. Conversely, channel closure alone supplies no usage. The retained live receipt cannot distinguish an absent server success from a success consumed by an abandoned receiver. We did not retain the abandoned future or raw channel event sequence from that run; do not claim either server behavior as an observed fact.

[The offline reproduction script](analyze-cancellation-queue.py) uses the exact hash-verified installed SDK queue getter and `SyncChannel`, a local asyncio queue/background loop, and an explicitly synthetic endpoint. It constructs no client, websocket or model and sends no inference. [Its retained differential result](diagnostic-queue-analysis.json) demonstrates:

| Local case | Background receive outcome | Terminal delivered to foreground endpoint |
| --- | --- | --- |
| Ordinary terminal success | First receive returns synthetic success | Yes |
| Our monotonic interruption, then synthetic success + channel close | Abandoned first receive takes success; new receive takes closure | No; same missing-terminal secondary error as the real probe |
| SDK idle timeout, then the same synthetic replies | SDK cancels first receive; new receive takes success | Yes; primary idle failure remains a failure |

This local result proves an ownership defect that exists with the selected code and SDK, even when a server would provide a terminal reply. It does not prove the real server emitted that reply, establish actual usage, or qualify the runtime cancellation path. The synthetic terminal carries no real model/configuration/usage evidence.

## Why prior green tests were insufficient

The installed-SDK test in [the control tests](../../../experiments/tests/test_investigator_run_control.py) uses one persistent `Future` as its getter. The interrupted wait and drain read the same future, so its synthetic success remains available. Real SDK queue reads create a new asynchronous queue-get future on each invocation. The test established signal interruption and same-channel cancel wiring while omitting the asynchronous receive-ownership behavior that matters here. The generic missing-terminal test correctly proves conservative failure reporting, but cannot qualify the missing queue layer.

The distinct deadline exception still avoids the SDK's timeout relabeling; that earlier correction remains valid. The later finding shows its adjacent cancellation semantics also needed inspection. **227 passing tests** are the preceding implementation/profile/fit horizon's mechanical proof, not fresh proof of successful real cancellation. A fresh focused rerun still passes all **10 existing control tests** with the exact SDK selected, while the new three-case offline differential exposes the omitted queue behavior. Those 10 overlap the earlier suite, not 10 additional distinct tests. Executable experiment/product source and the pinned SDK were not changed or tested as a repair in this increment.

## Consequence and bounded repair target

The capability question remains unanswered: zero of four semantic cases ran, zero reports can be source-reviewed, and all 20 frozen reviewer obligations are unreached. This neither establishes semantic inadequacy nor removes the earlier independently observed semantic/navigation defects. Actual complete-input fit remains valid evidence at its recorded point, while end-to-end diagnostic readiness failed at control/accounting.

The smallest useful follow-up is a **receive-ownership repair**, proved offline before another load or prediction. It should satisfy this contract: interruption cannot leave an unowned pending receive that consumes the terminal event, and terminal events already dequeued during an interruption race remain recoverable exactly once. Merely calling `future.cancel()` is not sufficient proof for the race in which a receive has already completed. Preserve primary failures, known-versus-reserved accounting, same-channel cancellation, finite drain/release and owned cleanup.

Compare an experiment-owned interruption-safe receive boundary with the existing simpler baseline before choosing its implementation. Do not globally monkeypatch the SDK, change its installed files, replace the transport, add a worker/dependency or upgrade the SDK without a justified decision. A worker is warranted only if the local boundary cannot establish ownership; killing a worker still does not prove server cancellation. Fixing this specific defect does not automatically settle every SDK/background-thread signal interaction.

Required discriminating proof includes the actual queue getter's blocked wait, a terminal arriving around interruption/cancellation, a receive already completed at interruption, continuous fragments, missing terminal, handled interruption/exit, bounded drain/release and unknown-usage withholding. A follow-up runtime record should retain a minimal allowlisted event/receive lifecycle (event types and ownership transitions, without hidden reasoning or credentials), enough to distinguish missing server completion from client receive loss. Do not preserve arbitrary raw event payloads.

The repair must also separate finalization's absolute deadline from the inherited one-second prediction idle timeout: the current SDK idle setting remains in force during drain. That is a source-visible limitation for a delayed cancellation reply, **not this run's observed cause**, whose channel ended within milliseconds. It belongs to the same receive/drain proof rather than a separate model-quality tuning loop.

Do not lengthen the one-second probe to hide the defect, weaken unknown usage into acceptance, relabel unload as a usage receipt, or spend the five unused slots. Any source change invalidates this freeze's source identity. A later runtime qualification needs a freshly bound preparation/profile/fit/freeze, explicit finite probe/cost consequences and matching activation; the old failed cohort remains immutable. This disposition specifies a reviewable repair target, not an implemented repair or a new inference authorization.

## Retention, verification and proof limits

[The completed retention summary](diagnostic-retention.json) binds 42 owner-only execution/disposition files / 765,036 bytes, excluding its index, and revalidation of all 400 files in four prior completed indexes. Earlier failures, profile/fit records and original interrupted matrix remain unchanged. The already-indexed disposition draft had a prose count of16 execution files; the exact inventory has15, corrected here without rewriting that draft or the correct index. Local retention is not off-machine backup or a complete model/runtime archive.

Verification checks the source/SDK/freeze/reviewer identity, current r7 preparation/freeze admission, all retained request/receipt/hash relationships, exact attempted/unattempted denominator, resource/reservation arithmetic, cleanup evidence, local three-case queue reproduction, source snapshot correspondence, analysis syntax, 10 existing control tests, Markdown links and focused diff. No new full test-suite pass or semantic review is claimed. Learner ownership and cycle E closure remain pending in their normal owners; no product acceptance, autonomous discovery repair or original-matrix continuation follows.

Reproduce the offline evidence from repository root:

```sh
PYTHONPATH=src:. .venv/bin/python working-memory/evidence/2026-10-19-investigator-successor-build/analyze-cancellation-queue.py --sdk-site /home/motafeq/.local/share/upgradepilot/investigator-runs/deployment-interface-2026-10-16-r1/sdk-1.5.0/lib/python3.12/site-packages --diagnostic-root /home/motafeq/.local/share/upgradepilot/investigator-runs/supplied-evidence-2026-10-19-diagnostic-r1
```

Source hashes must still match the failed activation. After a later repair, use its retained matching source horizon; do not edit the old activation or treat an expected source-drift refusal as permission to bypass admission.
