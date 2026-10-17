# LM Studio stateful-chat and SSE transport alternatives — deferred discovery

**Date:** October 17, 2026
**Status:** DEFERRED / NON-CONTROLLING discovery record
**Current-cycle effect:** none. Do not change the frozen/current Investigator qualification transport, r6/r7 execution, budgets, outcomes, or semantic-comparison activation because of this note.

## Why this record exists

During deployment/interface learning we identified two current LM Studio REST capabilities that are directly relevant to UpgradePilot's model-transport architecture and may deserve a bounded future comparison. They are recorded on `main` so a later builder/orientation session does not depend on the temporary learning branch or rediscover them from scratch.

Current qualification remains the explicitly reconstructed stateless SDK transport described by `experiments/investigator_model_interface.py` and `experiments/INVESTIGATOR_MODEL_INTERFACE_QUALIFICATION.md`. This note does not claim the alternatives are better and does not authorize migration.

## 1. Stateful chat threads

LM Studio documents `/api/v1/chat` as stateful by default. A response can return a `response_id`; a later request can supply `previous_response_id` so LM Studio manages prior conversation context instead of the client resending the full visible history. `store: false` disables stateful storage.

Source: https://lmstudio.ai/docs/developer/rest/stateful-chats

### Relevance to UpgradePilot

Potential benefit:

- smaller client request payloads and simpler conversation continuation;
- possible runtime/performance benefit, but **do not infer KV-cache reuse or lower prompt-token processing merely from `response_id` semantics**; that must be measured/verified separately.

Architecture questions that must be answered before adoption:

- What exact historical content remains available through a continued thread?
- Can old/omitted/invalidated evidence remain model-visible after Workspace no longer authorizes it?
- How would the current rule "omitted evidence must be re-read before it can grant reference authority" be preserved?
- What survives LM Studio/server/model restart, unload, eviction, or process loss?
- Can UpgradePilot reconstruct/audit the effective context from its own durable records without trusting opaque server state?
- How are branching, response/thread identity, failure recovery and retention represented durably?
- Does stateful continuation actually reduce measured prompt processing/TTFT or only reduce HTTP payload size?
- Can Raw/Structured treatment fairness and fresh-assignment isolation remain explicit and reproducible?

The durable Workspace/evidence authority must remain product-owned even if a future transport uses server-managed conversational state.

## 2. REST streaming events (SSE)

LM Studio documents `POST /api/v1/chat` with `stream: true` as Server-Sent Events (SSE). Current event types include lifecycle events for model loading, prompt processing, reasoning, tool calls, visible messages, errors and final aggregation (`chat.end`). `chat.end` includes the final result and statistics such as input/output/reasoning token counts, tokens per second and time to first token when reported.

Source: https://lmstudio.ai/docs/developer/rest/streaming-events

### Relation to what UpgradePilot already has

UpgradePilot already has streaming in the current SDK binding: `PredictionStream` receives fragments incrementally; visible fragments are retained before final completion; reasoning-labelled fragments are filtered before persistence; success metadata/usage are retained when available. Therefore SSE streaming is **not** a missing prerequisite for current qualification.

The REST SSE surface is nevertheless materially different because it exposes typed lifecycle events such as:

- `prompt_processing.start/progress/end`;
- `reasoning.start/delta/end`;
- `tool_call.start/arguments/success/failure`;
- `message.start/delta/end`;
- `error`;
- `chat.end`.

Potential future value:

- cleaner prompt-processing/TTFT observability;
- explicit reasoning-channel detection when validating thinking-on/off behavior;
- richer interruption/error diagnostics;
- possible independent cross-check of usage/timing metadata;
- explicit tool-event visibility if a future transport experiment deliberately evaluates LM Studio-native tool handling.

Do **not** equate LM Studio-native tool events with UpgradePilot's current closed Investigator tool protocol. Tool ownership/reference authority must be evaluated explicitly before any such migration.

## 3. Future bounded comparison, if selected

If transport/performance/observability later becomes an explicit responsibility, compare rather than silently replace:

1. current explicit stateless SDK `PredictionStream` baseline;
2. REST `/api/v1/chat` stateless mode (`store: false`) with SSE, if interface requirements can be represented equivalently;
3. REST stateful continuation with `response_id` / `previous_response_id`, only after authority/recovery semantics are designed.

Hold constant where possible: model asset, template, task/evidence inputs, tool/reference contract, context/output limits, sampler/reasoning settings and assignment identity. Measure at least:

- actual runtime input-token usage, not HTTP payload size alone;
- prompt-processing time and TTFT;
- generated throughput and total latency;
- RAM/VRAM/KV behavior where observable;
- restart/unload/recovery behavior;
- exact effective-history/audit reconstruction;
- evidence invalidation/omission/reference-authority behavior;
- interruption/error retention;
- Raw/Structured fairness and semantic/interface correctness guardrails.

Any transport change that materially changes effective history, tool behavior, reference authority, accounting or runtime semantics is a new/versioned deployment/protocol condition and must not be pooled blindly with r3/r4/r5/r6 or the current native-mode follow-up.

## 4. Trigger for revisiting

Revisit this note only when one of these becomes selected work:

- stateless history size/prefill latency becomes a demonstrated bottleneck;
- transport/recovery/auditability is being redesigned;
- richer runtime observability is required to discriminate a qualification failure;
- concurrent/long-lived Investigator sessions become a product requirement;
- a post-qualification runtime-performance characterization is explicitly planned.

Until then, preserve the established stateless qualification baseline and finish the currently selected work before introducing another transport dimension.
