# LM Studio stateful-chat learning note

**Branch:** `learning/deployment-interface-d-prep-2026-10-17`
**Status:** learning supplement only; no main-branch transport or experiment change.
**Parent learning gates:** Q6-Q9 (stateless history/reference authority), with later relevance to Q10/Q13 (deployment/experiment identity).

## Why this matters

LM Studio's current native `/api/v1/chat` API supports stored chat threads. A response may return a `response_id`; a later request can pass it as `previous_response_id` to continue that server-managed conversation. `store=false` disables that storage for the request. LM Studio's `/v1/responses` endpoint also supports stateful continuation through `previous_response_id`.

This is directly relevant to UpgradePilot because the current Investigator qualification deliberately uses complete explicit stateless requests: no response ID, prior server conversation, hidden notebook or implicit chat history is allowed to become model context or evidence authority.

## Learning distinction to own at Q6-Q9

- **Current baseline:** UpgradePilot/Workspace owns durable investigation state; every model call explicitly presents the admissible task/history/evidence working set. Omitted evidence must be re-read. Delivered observations, not prior model-authored text or hidden server state, determine reference eligibility.
- **LM Studio stateful alternative:** LM Studio can retain a conversation thread and let a later request continue from a `previous_response_id` without resending all prior conversation text in the API request.
- **Important unknown:** stateful API convenience does not by itself establish what performance state is reused internally (for example KV-cache reuse), recovery guarantees, exact persisted representation, or compatibility with UpgradePilot's reference-authority/reproducibility requirements. Those must be measured/read from authoritative implementation/docs before any product claim.
- **Potential benefit:** smaller follow-up API payloads and possibly a cleaner/potentially faster continuation path if the runtime can reuse work; actual token accounting/performance must be measured rather than inferred from the presence of `response_id`.
- **Potential cost/risk:** part of the model-visible conversational state becomes server-managed instead of completely reconstructed by UpgradePilot, which can complicate exact replay, crash/restart recovery, branching, experiment fairness, omission semantics and proof that only currently authorized evidence remains usable.

## Future bounded comparison (not selected work)

If transport/performance becomes an explicit responsibility after the current qualification baseline is stable, compare the current explicit-stateless transport against a separately frozen LM Studio stateful transport. Keep Workspace as canonical evidence/state authority and measure at least:

1. exact model-visible history and reference eligibility;
2. recovery/replay after process/model/server restart;
3. branching semantics using response IDs;
4. prompt/input-token accounting and whether prior context is still charged/reprocessed;
5. time to first token, prompt-processing time, throughput and RAM/VRAM/KV behavior;
6. behavior when evidence is invalidated/omitted and must no longer authorize a citation;
7. Raw/Structured fairness and reproducibility;
8. failure behavior when a response/thread identifier is unavailable or stale.

A stateful success would be a different transport/deployment revision and must not retroactively relabel current r6 results. Do not adopt stateful storage merely because the API supports it; select it only if measured benefits justify the additional state/recovery/authority complexity.
