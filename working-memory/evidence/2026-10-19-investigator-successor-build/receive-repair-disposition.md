# Receive/control repairs and the observed runtime resource boundary

October19,2026. Implementation revisions: `855d6e49`, then `9f4a5df4`.
Owner: [the same Build cycle](../../2026-10-19_investigator-successor-build_lbd-cycle.md), under [the amended successor plan](../../../plans/INVESTIGATOR_RUN_CONTROL_COMPLETION_AND_CAPABILITY_DIAGNOSTIC_PLAN.md).

Ali directed fixing reasonable blockers and continuing instead of ending after each diagnosis. The receive-ownership defect, signal-handoff race and terminal-metadata retention defect are repaired and verified. The work progressed through actual runtime qualification and a real report-canary attempt. That canary reached its declared deadline without output under the resource-constrained placement, so no semantic case ran. The remaining constraint requires available GPU resources or a separately selected execution capacity; it is not evidence of semantic inadequacy.

## Delivered behavior and why it matters

The pinned SDK creates an asynchronous queue-get future for each synchronous receive. Our earlier signal deadline abandoned that future, allowing it to consume the terminal cancellation reply while drain saw only channel closure. The new per-prediction receiver retains exactly one future until endpoint processing acknowledges its message. A blocked or already-completed receive remains recoverable after interruption. It uses the same SDK queue, task manager, protocol handler and cancellation sender; no SDK files/globals, transport, dependency or worker process were changed.

A second race appeared in the repair tests: masking OS signals on the main thread did not prevent CPython handling a process signal delivered through the SDK's background thread. A fragment could be delivered twice. The final implementation defers the Python control handlers during the short local delivery/acknowledgment step and restores all timer/interrupt/exit handlers on every path. Blocking queue/network waits remain interruptible. Finalization uses its own absolute deadline, independent of the probe's one-second SDK idle setting. Event-kind and receive-ownership counts are retained without event payloads or hidden reasoning.

The actual repaired cancellation probe confirms terminal success, retained-future reuse, stopped receiver, channel release and owned model/client cleanup. Its terminal stats expose only `stopReason: userStopped`; numeric token counts remain unknown. The original cohort correctly failed its accounting gate. The proof contract was then prospectively separated: those isolated control facts support the unchanged receive/cancellation mechanism, while every fresh report still requires complete numeric usage and exact prompt/configuration/instance correspondence. A new client/owned model is required after the failed probe; no unknown-usage object or batch is resumed.

The next real call also exposed why metadata must be retained before validating its counters. That order is repaired for interrupted and complete returns. The report-canary cancellation now preserves the actual metadata even though its counters are absent. All16 requested settings and the exact model instance match in the retained terminal packet; thinking is off. No missing count is invented or replaced with a reservation.

## Observed progression

| Evidence horizon | Result | What it establishes |
| --- | --- | --- |
| Original diagnostic-r1 at `c4c833e6` | Cancellation requested; no terminal receipt; unknown usage | Original failed control gate; five roles withheld |
| Repaired diagnostic-r2 at `855d6e49` | Terminal success, receiver stopped/channel released; stats only `userStopped`; cleanup confirmed | Receive/cancellation repair observed; original numeric-usage gate still failed |
| Runtime-r6, zero generation | Ratio0.45 requested;5 GPU layers observed instead of22; rejected and cleaned up | Actual placement drift; no prediction or executable freeze |
| Runtime-r7, zero generation | Explicit ratio0.10 and5 GPU layers match; all complete inputs fit; cleanup confirmed | New resource point's identity/fit, not report qualification |
| Diagnostic-r3 at `9f4a5df4` | Report canary reaches its actual deadline, no visible output; terminal/metadata/cleanup retained | Actual runtime/latency failure; four semantic cases unattempted |

The [initial diagnosis](diagnostic-disposition.md), [receive-repair proof](receive-repair-proof.json), [exact repaired control result](isolated-control-result.json), [prospective five-role proof](isolated-cohort-proof.json), [failed placement disposition](resource-placement-disposition.json), [matching activation](isolated-cohort-activation.json) and [actual report-canary result](resource-canary-result.json) preserve these distinct outcomes. They are not pooled into a successful cohort or silently relabelled as passes.

## Resource point and actual report-canary result

The original36,864-context request inherited GPU ratio0.45 with22 offloaded layers. Runtime-r6 exposed that the same request could produce only5 layers under current resource pressure; strict identity validation rejected it. After unload, Windows GPU telemetry showed about6,767/8,192MiB used and1,252MiB free, with no llama backend. Rather than silently accept adaptive placement, the plan prospectively selected ratio0.10/5 layers, a fresh owned identifier and actual profile/freeze. Model assets, sampler, context,8,192 output reserve, cache/template, complete cases and20 review obligations were preserved. No semantic output informed the selection.

Runtime-r7 freeze `0067f9884cc44c8a3175d5beb40787f055f123c59256a1f4c169acc10fad4145` binds observed profile `96ec429f20eadb69764b41e34b75de52b29602ff710cb330779f9081791afd50` and explicit effective roles/ceilings. It measured canary3270, HTTPX22415, newer consumer7862, glyphsLib25476 and older consumer7885 input tokens; the unused cancellation-role fit was3276. All fit their original role caps with zero omitted events. r10 preserves every stable material inventory/reference count and76/23/61/23-unit maximum-reference completion path.

The new report cohort has five roles, at most73,096 input/40,960 generated tokens,322 admission units,310 finalization seconds and the unchanged4,200 prediction/4,800 batch ceiling. The external cancellation slot cannot be transferred. The fresh canary's actual callback counted3269 input tokens. It reached a299.820701-second allowance at299.821152 prediction seconds, with11 prompt-progress events and no fragment events or visible bytes. The deadline is measured by the monotonic controller, not inferred from file age. Its finalization confirms cancellation success, one pending-future reuse, all12 messages acknowledged, receiver stopped and channel released; model unload/client release confirm afterward.

The terminal stats again contain only `userStopped`, so this is an unknown-usage failed attempt. Four cases remain unattempted. The canary's complete original output does not exist, and it cannot qualify the report interface or receive a semantic judgment. The repaired observability does preserve its terminal metadata and demonstrates zero mismatches across all16 requested settings and the exact instance. Numeric prompt/generation consumption remains unknown.

Across diagnostic-r1/r2/r3, three calls were attempted, all numeric usage unknown. Conservative reservations total12,288 input/24,576 generated tokens. The known-token subtotal0/0 is a sum across zero known-usage calls, not zero actual consumption. No semantic assignment was attempted or reviewed. No report repair, semantic feedback, selective retry or original-matrix continuation occurred.

## Resource evidence and limits

During the canary, a sampled Windows backend working set was8600MiB and physical RAM free was28889/65260MiB. A GPU snapshot reported100% utilization,7613MiB used and106.75W. After cleanup, Windows GPU Process Memory counters showed the unrelated `sp26-cod` process holding5314MiB dedicated memory. These observations explain why available GPU capacity needs attention; they do not independently attribute latency, measure final prompt-progress fraction or establish model token throughput. Process listings alone reported memory unavailable, so the dedicated-memory counter was checked separately. No full process command line or ephemeral backend credential was emitted or retained.

[Historical timing context](runtime-timing-context.json) records a prior Gemma12 qualification report at22 GPU layers/32,768 context:4086 input,847 generated tokens,145.001880 seconds recorded elapsed, and6.902262 seconds server-reported time to first token. This is historical evidence, not a fresh benchmark or controlled comparison with the new36,864-context report-only task. It supports restoring a previously qualified resource point as a candidate; it does not prove a specific application's causal share of the current delay or guarantee latency for the larger cases.

The smallest useful runtime follow-up is to make GPU resources available, explicitly select/requalify the intended placement and run a freshly bounded report-canary/four-case cohort. Exact identity and full input fit must still pass, and any additional attempt ceiling must be declared before dispatch. Raising timeouts, shrinking material or trying another model is not an established remedy. No further prediction was performed after the failed canary.

Resource availability was requested asynchronously while source/evidence verification continued. Stopping or suspending another application's workload is outside this project's authorized software repair; no such action was taken. If that workload remains active, preserve this runtime limitation rather than manufacture an answer-quality conclusion or continue an uncontrolled timeout/configuration loop.

## Verification, preservation and learning

Fresh proof comprises173 focused control/model/report-only/runner/seam tests and65 nearest Workspace tests,238 distinct. New cases cover the actual SDK queue-factory shape, interrupted blocked receive, already-dequeued terminal, continuous fragments exactly once, SIGINT/SIGTERM handoff, delayed/missing terminal, finite silent cancellation and handler restoration. Additional tests protect metadata retention despite missing counters, isolated-control artifact/source/cleanup binding and the fresh five-role strict-usage path. The preliminary OS-masking failure and a misplaced test assertion were corrected and recorded. These tests do not establish semantic adequacy or production adoption.

Exact source horizons are preserved: committed855d6e49 sources for runtime-r5/diagnostic-r2,9f4a5df4 for runtime-r7/diagnostic-r3, and all10 exact hash-verified sources for failed runtime-r6. Earlier roots and completed indexes are unchanged. The [new retention summary](receive-repair-retention.json) binds owner-only new preparations, runtime/control/attempt evidence and source/review snapshots; directories0700 and files0600. This is local retention, not off-machine backup or a full model/runtime archive.

The useful learning is now concrete: owning a foreground channel does not own its pending background receive; preserving a terminal packet does not guarantee numeric usage; and fitting context does not establish runtime feasibility under a changed resource point. The controller can terminate and account conservatively while the model capability question remains unanswered. Learner ownership is unassessed. The cycle stays at its unresolved runtime verification gate; D/E and semantic acceptance are not claimed complete.
