# B2 Local LLM Semantic Extraction Re-evaluation Plan

**Status:** Position-neutral bounded plan  
**Owner:** Ali Rajabi  
**Parent responsibility:** [`B2_TRANSPARENT_DECISION_METHOD_PLAN.md`](B2_TRANSPARENT_DECISION_METHOD_PLAN.md)  
**Stable semantic boundary proposal:** [`../working-memory/2026-07-28_B2-upstream-semantic-boundary.md`](../working-memory/2026-07-28_B2-upstream-semantic-boundary.md)  
**Responsibility:** Determine whether a current local LM Studio GGUF deployment can produce trustworthy-enough bounded attributed upstream claims for the first B2 decision method, under deterministic validation and decision-effect limits.

## 1. Why this plan exists

UpgradePilot has already run a local-model semantic-extraction experiment. At historical revision `e7425dcfc20f093ac10c9a903f1c4ae50a8b2638`:

- `gemma-4-e2b-it` produced 9/14 clean candidate/grounded results and 11/14 correct decision effects;
- `qwen3-4b-instruct-2507` produced 8/14 clean candidate/grounded results and 10/14 correct decision effects;
- repeated material false dropped-support claims created unnecessary targeted-check outcomes;
- both deployments were rejected for normal extraction;
- strict JSON Schema, source quotation, provenance, model authority, diagnostics, and deterministic decision-effect limits were retained as useful evidence.

The current B2 responsibility is broader than the historical Python-support proof slice. It requires bounded attributed claims across:

```text
fix_or_remediation
compatibility_assurance
interface_or_behavior_change
support_boundary_change
```

A new local-model attempt is legitimate only as a re-evaluation against changed evidence, not as a restart that ignores the prior rejection.

## 2. Re-evaluation hypothesis

A current local GGUF deployment may outperform the rejected 2B/4B deployments if all of the following are true:

1. a materially stronger instruction-following model fits Ali's RTX 3070 Laptop GPU with 8 GB VRAM at a useful context length;
2. LM Studio's current JSON-Schema constrained generation is used directly;
3. the output contract preserves subject, direction/state, attributed meaning, explicit consumer action, source span, limitations, and unresolved/conflicting states;
4. release text remains untrusted data and the model receives no tools or decision authority;
5. deterministic validation rejects malformed, ungrounded, policy-producing, or source-mismatched output;
6. the deterministic decision layer limits the effect of model-derived claims;
7. representative semantic and decision-effect tests show material improvement over the prior rejected deployments.

Failure of this hypothesis is an acceptable result. The plan may close with local LLM extraction rejected or deferred again.

## 3. Method boundary

The candidate semantic path is:

```text
accepted exact GitHub Release body
→ local LM Studio structured extraction
→ untrusted candidate UpstreamClaimResult
→ deterministic schema validation
→ deterministic source-span grounding
→ model-derived attributed upstream claims
→ deterministic evidence-sufficiency evaluation
→ deterministic maintainer-action evaluation
```

The local model may extract candidate meaning only. It must not:

- select evidence authority;
- decide whether the external source is true;
- infer target-repository relevance without target evidence;
- choose evidence sufficiency or stopping;
- produce a maintainer action;
- claim compatibility, safety, or merge authorization beyond attributed source meaning;
- call tools, browse, read files, mutate repositories, or access credentials.

## 4. Transport and client comparison

Before implementation, compare the smallest credible transport options.

### Option A — direct HTTP with the existing `requests` dependency

Advantages:

- no new runtime dependency;
- complete visibility into request/response payloads;
- direct support for `/v1/chat/completions` and `response_format=json_schema`;
- easy preservation of status code, timing, raw body, and LM Studio response metadata.

Costs and risks:

- application code owns OpenAI-compatible payload construction and response parsing;
- compatibility changes must be handled locally.

### Option B — OpenAI Python client pointed at LM Studio

Advantages:

- previously proven against LM Studio in UpgradePilot and Sentinel-style local endpoints;
- typed client surface and familiar timeout handling;
- straightforward JSON-Schema request construction.

Costs and risks:

- adds a runtime dependency to the active clean B2 package;
- provider-compatible behavior can still differ from OpenAI-hosted behavior;
- the SDK does not solve semantic correctness or grounding.

### Option C — LM Studio Python SDK

Advantages:

- native model discovery and load-management capabilities;
- provider-specific access to current LM Studio features.

Costs and risks:

- adds a provider-specific dependency and tighter coupling;
- unnecessary if the first admitted responsibility only needs one chat-completion request.

### Option D — LangChain / agent framework

Disposition: reject for this bounded responsibility unless later evidence establishes a missing capability. It adds orchestration and dependency surface without improving the core schema, grounding, authority, or decision-effect problem.

No client or dependency is selected by this plan. A durable selection requires Ali approval and an ADR only if the commitment becomes cross-cutting.

## 5. Required local environment inventory

Before selecting a model or writing product integration, record:

1. LM Studio application/CLI version;
2. server status, port, bind behavior, and authentication state;
3. all downloaded LLM model keys, architectures, parameter sizes, quantizations, and disk sizes;
4. currently loaded model identifiers and load configuration;
5. NVIDIA GPU model, driver, total/free VRAM, and current processes;
6. Windows-to-WSL2 reachability and the exact base URL that works from the UpgradePilot environment;
7. Python version and current UpgradePilot environment;
8. candidate model memory estimates at proposed context lengths and GPU offload;
9. one structured-output smoke response and LM Studio model/server logs.

Do not record secrets, API tokens, unrelated model prompts, or private data.

## 6. Candidate deployment eligibility

A candidate deployment enters the scored experiment only when it:

- is a chat/instruct GGUF model, not an embedding model;
- exposes a stable model identifier through LM Studio;
- successfully completes a JSON-Schema structured-output smoke test;
- fits without system instability at the chosen context length;
- reports no truncation for the smoke schema;
- can run serially on the 8 GB RTX 3070 environment;
- has enough context for the admitted release-body input limit;
- is not one of the previously rejected deployments unless deliberately included as a historical control.

Prefer the strongest general instruction-following 7B–8B-class deployment already available locally. Do not assume a coder model is the best semantic extractor. Use `lms load --estimate-only` and observed behavior rather than parameter count alone.

## 7. Source-input boundary

The active GitHub release client permits a body much larger than a small local model can necessarily process. The semantic method must not silently truncate decision-relevant release text.

Before scoring models, freeze one of these bounded behaviors:

1. **supported complete-body limit:** accept only release bodies that fit the measured prompt/context budget; return explicit unsupported or unresolved behavior above the limit; or
2. **deterministic chunking:** split complete release text into traceable bounded chunks, extract per chunk, preserve spans, and deterministically aggregate claims and conflicts.

The first experiment should prefer the complete-body limit unless representative evidence proves chunking is required. The exact limit must be derived from the selected deployment's measured tokenizer/context behavior, not an arbitrary character count.

## 8. Proposed claim contract under evaluation

The candidate output must represent:

```text
UpstreamClaimResult
├── state
│   ├── resolved
│   ├── no_decision_relevant_claim
│   ├── unresolved
│   └── conflicting
├── source_identity
├── claims[]
│   ├── category
│   ├── subject
│   ├── change_state
│   ├── normalized_meaning
│   ├── required_action
│   ├── migration_summary
│   ├── source_span
│   └── limitations[]
└── unresolved_reasons[]
```

The exact Python representation is not selected here. The schema must prohibit maintainer actions, confidence-as-truth, safety conclusions, arbitrary authority, tool calls, and unknown fields.

## 9. Deterministic trusted-boundary controls

Deterministic code must validate at least:

- exact upstream source identity;
- allowed result state, claim category, and change state;
- required fields and no unknown fields;
- source span offsets or exact bounded quotation within the supplied release body;
- subject/version/direction consistency with the grounded span where mechanically testable;
- no maintainer action or safety conclusion in model output;
- no caller/model assignment of authority;
- preservation of multiple and contradictory claims;
- explicit unresolved behavior for malformed, ambiguous, unsupported, or ungrounded output;
- bounded raw-output and diagnostic preservation.

Mechanical grounding proves correspondence to source text. It does not prove source truth or semantic correctness.

## 10. Evaluation corpus

Freeze a small but representative corpus before scoring candidate deployments.

It must include:

1. same-meaning wording variation for all four claim categories;
2. changed direction/state, including added versus dropped, deprecated versus removed, and current versus future;
3. explicit negation and continued-support/unchanged controls;
4. multiple claims in one source;
5. no-decision-relevant-claim text;
6. ambiguous or incomplete text that must remain unresolved;
7. materially conflicting statements;
8. instruction-shaped untrusted text;
9. legitimate quoted instruction-like text that must not be automatically discarded;
10. malformed/ungrounded candidate-output controls;
11. exact historical S001, S002, and S004 upstream excerpts;
12. at least one longer realistic GitHub Release body within the admitted input limit.

Known fixtures are calibration cases and test oracles, not the implementation method.

## 11. Measurements

For every model, deployment, case, and repetition, record:

- model key, architecture, quantization, file size, context length, GPU offload, flash-attention state, and LM Studio/runtime version;
- prompt/schema identity and hash;
- seed, temperature, max output tokens, timeout, and non-streaming mode;
- raw candidate output;
- structured-output/schema result;
- grounded accepted claims;
- unresolved/conflicting result;
- false positive, false negative, wrong category, wrong subject, wrong direction/state, and ungrounded-claim counts;
- downstream decision-effect result under the bounded deterministic policy;
- finish reason, prompt/completion/reasoning token counts when available;
- first-token and total latency when available;
- failures, timeouts, GPU OOM, and model/server logs needed for diagnosis.

Run at least three scored repetitions for decision-critical cases. Temperature remains `0`; record the seed without claiming universal determinism.

## 12. Selection gate

A deployment may be proposed for product adoption only when all of the following hold on the frozen proof set:

1. every response either validates or degrades explicitly without creating trusted claims;
2. no model output creates a maintainer action or changes authority;
3. every accepted claim is grounded to the exact admitted source;
4. no decision-critical wrong direction/state, false compatibility assurance, or invented required migration survives validation;
5. decision-effect behavior is correct for every critical case and repetition;
6. same-meaning variations normalize equivalently within the supported boundary;
7. negation, deprecation/removal, future/current, added/dropped, ambiguity, and irrelevant text remain materially distinct;
8. untrusted embedded instructions cannot change policy or create an accepted unsupported claim;
9. latency and resource use are measured and operationally acceptable for one read-only maintainer decision run;
10. the method materially improves over the previously rejected deployments rather than merely reproducing JSON compliance.

Prefer explicit unresolved/abstention over guessing. A schema-valid but semantically wrong result is a failure.

## 13. Decision outcomes for this plan

The experiment must end in one of:

- **adopt candidate:** evidence supports a bounded local extractor; create the required ADR if the client/model/provider commitment is durable, then implement the minimum method;
- **retain as experiment:** useful capability exists but proof or operational quality is insufficient for normal runtime;
- **reject candidate deployment:** material semantic or decision-effect failures remain;
- **defer local LLM extraction:** available hardware/models cannot satisfy the boundary; continue deterministic decision support with semantic unresolved/abstention behavior;
- **reconsider method:** evidence shows a different source-input or interpretation architecture is required.

No adoption occurs merely because Ali has approved trying an LLM.

## 14. Execution sequence

1. Capture current local environment and model inventory.
2. Select at most three candidate deployments plus an optional rejected historical control.
3. Run memory estimates and freeze load configuration.
4. Prove WSL2 transport and one strict structured-output smoke request.
5. Freeze the semantic corpus, expected claims, and decision effects before scoring.
6. Implement only the smallest experiment harness needed to call candidates, validate output, and record diagnostics.
7. Run narrow deterministic harness tests.
8. Run candidate models serially with repeated critical cases.
9. Diagnose failures by transport, output budget, schema, semantics, grounding, authority, or decision effect.
10. Compare results against the historical rejected deployments.
11. Present the model/client/source-boundary decision to Ali.
12. Create an ADR and product implementation only after explicit adoption approval.

## 15. Stop line

Stop this plan when one evidence-backed adopt, retain-as-experiment, reject, defer, or reconsider-method decision is recorded.

Do not continue here into:

- LLM-controlled recommendation policy;
- agent frameworks, tool-calling loops, MCP, RAG, embeddings, vector stores, or multi-model debate;
- automatic model download without Ali's explicit approval;
- cloud model fallback;
- arbitrary release-document search;
- target-repository mutation;
- broad corpus training or fine-tuning;
- restoration or import of archived M2 source.

## 16. Proof and ownership

Ali should be able to explain:

- why the earlier local deployments were rejected;
- what JSON Schema guarantees and what it cannot guarantee;
- the difference between transport, schema, semantics, grounding, authority, and decision effect;
- why a local endpoint is still an untrusted model boundary;
- how WSL2 reaches LM Studio and why the base URL is configuration;
- why release text is untrusted but does not receive tool authority;
- how one candidate is selected, loaded, measured, rejected, or adopted;
- why the final maintainer action remains deterministic and human-bounded.
