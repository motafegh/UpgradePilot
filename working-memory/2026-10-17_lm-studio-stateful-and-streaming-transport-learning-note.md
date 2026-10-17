# LM Studio stateful and streaming transport — learning note

**Branch:** `learning/deployment-interface-d-prep-2026-10-17`
**Date:** October 17, 2026
**Status:** temporary learning/research note only; not selected main-branch implementation work.

## Why this note exists

Current main qualification deliberately uses a complete explicit stateless request for every model prediction. While learning the current runtime boundary, Ali identified two current LM Studio REST capabilities that are directly relevant to future transport design:

1. **Stateful chats** through `/api/v1/chat`, `response_id`, and `previous_response_id`.
2. **Streaming events** through `/api/v1/chat` with `stream: true` and Server-Sent Events (SSE).

These capabilities must not be silently mixed into current r6/r7 evidence. They are alternative transport/runtime surfaces to understand and, if useful, evaluate under a separately selected/frozen responsibility.

## What main already does

Current `experiments/investigator_model_interface.py` intentionally supplies one fresh explicit history per prediction. It does not use response IDs, prior server conversation, or implicit chat history. Its pinned LM Studio SDK transport already uses a `PredictionStream` and intercepts incremental fragments. Visible fragments are persisted before final accumulation; reasoning-labelled fragments are filtered before persistence. Final success metadata is retained separately. This means UpgradePilot already has **streaming fragment retention**, but it is not the same API/transport as the newer REST `/api/v1/chat` SSE event taxonomy.

## LM Studio stateful-chat alternative

Current LM Studio documentation describes `/api/v1/chat` as stateful by default: a stored response can return a `response_id`, and a later request can pass `previous_response_id` to continue that conversation. `store: false` disables stored conversational continuation.

This is directly relevant to Q6-Q9 because it changes where conversational state is owned:

- current UpgradePilot baseline: Workspace/retained request-result history is canonical; every model request explicitly reconstructs its allowed working state;
- LM Studio stateful alternative: some conversational history is retained and reconstructed by LM Studio and referenced by an opaque response identifier.

Do not assume from `response_id` alone that a previous KV cache is physically retained/reused, that fewer prompt tokens are actually processed, or that TTFT necessarily improves. Those are separate empirical questions.

A future bounded comparison may be useful, but must preserve UpgradePilot's evidence-authority rules. Questions include invalidation/omission semantics, restart/recovery, reproducibility, branching, exact effective context, current-reference eligibility, Raw/Structured fairness, input-token accounting, TTFT and resource use.

## LM Studio REST streaming events

Current LM Studio documentation says `/api/v1/chat` with `stream: true` emits ordered SSE events beginning with `chat.start` and ending with `chat.end`. The current event taxonomy includes:

- model-load start/progress/end;
- prompt-processing start/progress/end;
- reasoning start/delta/end;
- tool-call start/arguments/success/failure;
- message start/delta/end;
- error;
- final `chat.end` with the aggregated result.

The documented final result can include model instance identity, output, token/timing statistics, and (when stored) a response ID. Current documentation examples expose fields such as input tokens, total output tokens, reasoning-output tokens, tokens/second and time-to-first-token.

### Relation to current UpgradePilot streaming

This is **related but not equivalent** to current main's SDK `PredictionStream` implementation:

- both provide incremental output before the final result;
- current main already retains visible partial output so a terminated prediction does not erase received visible evidence;
- current main explicitly filters reasoning fragments before persistence;
- REST SSE exposes richer typed lifecycle events, including prompt-processing, reasoning, native tool-call boundaries and explicit errors;
- switching from the pinned SDK channel to REST SSE would therefore be a transport revision, not a drop-in observability flag.

Potential value for a future experiment includes clearer TTFT/prompt-processing telemetry, explicit reasoning-event detection/counting when available, stronger interruption/error classification, and typed event boundaries. Potential risk includes accidentally changing native tool semantics, reasoning exposure/privacy, stored-conversation semantics, reference authority, applied configuration observability, or experimental comparability.

## Learning/experiment placement

Fold the concepts into the existing 20-question learning path rather than adding new top-level questions:

- **Q1/Q4:** distinguish SDK streaming from REST/SSE transport and understand prompt-processing/timing/resource observability.
- **Q5:** reasoning events are relevant to thinking-on/off behavior and generated-token accounting; hidden reasoning content must remain outside retained evidence unless governance explicitly changes.
- **Q6-Q9:** stateful `response_id` continuation versus complete explicit stateless history; authority/invalidation/recovery are central.
- **Q10/Q13:** changing transport from SDK stateless prediction to REST stateful/SSE is a material deployment/protocol revision and cannot be silently pooled with r6/r7.
- **Q14-Q16:** typed stream errors/reasoning events may improve failure classification, but do not turn transport telemetry into semantic evidence.

## Deferred bounded transport comparison

If a later responsibility selects it, compare the current explicit-stateless SDK baseline with one or more LM Studio REST alternatives while keeping model, task/evidence, sampler, context, reasoning policy and qualification semantics fixed as far as possible. Measure at minimum:

- exact input/output/reasoning token accounting available from each transport;
- TTFT and prompt-processing/generation timing;
- interruption/error retention;
- restart/recovery and branch behavior;
- effective evidence/reference authority after omission or invalidation;
- Raw/Structured fairness;
- RAM/VRAM/runtime state where observable;
- whether server-managed state actually reduces backend prompt work rather than merely shrinking the HTTP payload.

Do not activate this merely because the APIs exist. Current r6/r7 evidence retains its original transport identity.

## References to re-check when selected

- LM Studio Stateful Chats: `https://lmstudio.ai/docs/developer/rest/stateful-chats`
- LM Studio Streaming Events: `https://lmstudio.ai/docs/developer/rest/streaming-events`
- Current UpgradePilot binding: `experiments/investigator_model_interface.py`
- Current qualification protocol: `experiments/INVESTIGATOR_MODEL_INTERFACE_QUALIFICATION.md`

Because LM Studio APIs can evolve, re-read the current primary documentation at the time of any actual transport experiment rather than treating this October 17 note as a frozen external specification.
