# UpgradePilot Current Memory

**Last updated:** 2026-07-22  
**Purpose:** Authoritative concise project-local continuation pointer. Source, tests, commands, outputs, and the current environment remain the authority for actual implementation behavior.

## Current responsibility

M2-S02 — known-text semantic extraction under [`plans/M2_S02_KNOWN_TEXT_SEMANTIC_EXTRACTION_PLAN.md`](plans/M2_S02_KNOWN_TEXT_SEMANTIC_EXTRACTION_PLAN.md).

The current working session is [`working-memory/2026-07-22_M2-S02_llm-extraction-session.md`](working-memory/2026-07-22_M2-S02_llm-extraction-session.md).

## Verified current implementation

The first complete Python-support extraction path now exists:

```text
accepted upstream release-note EvidenceItem
→ LM Studio OpenAI-compatible chat completion
→ CandidateExtractionResult
→ deterministic grounding validation
→ ExtractionResult with accepted_facts / unresolved / validation_errors
→ trusted PythonSupportChange facts
→ existing evaluate_decision(...)
```

Current modules:

- `src/upgradepilot/extraction.py` — candidate/trusted contracts, conversion to decision facts, and extraction orchestration;
- `src/upgradepilot/extraction_validation.py` — deterministic evidence, quote, version, duplicate, and contradiction checks;
- `src/upgradepilot/llm_extractor.py` — direct LM Studio client and environment-backed runtime settings;
- `scripts/evaluate_python_support_models.py` — repeatable semantic/model comparison;
- tests under `tests/` cover contracts, validation, client behavior, orchestration, and decision integration.

The ordinary path no longer requires callers to manually construct `PythonSupportChange` for the demonstrated Python-support case.

## Verified runtime evidence

- Reachable LM Studio base URL: `http://localhost:12345/v1`.
- Direct dependency: OpenAI-compatible Python client; no LangChain, LangGraph, agents, RAG, embeddings, or model router.
- Repository checks reached 50 passing tests after the JSON-array/strict-tuple boundary repair; compile checks also passed.
- Real end-to-end Soup Sieve proof succeeded with `qwen3-4b-instruct-2507`:

```text
"Soup Sieve 2.8 drops Python 3.8 support."
→ accepted dropped Python 3.8 fact
→ run_targeted_checks
```

The model supplied candidate meaning and exact quote. Trusted code attached evidence identity, validated grounding, converted the accepted fact, and retained deterministic control of the final decision.

## Model evaluation findings

No production model is selected yet.

### Rejected for this responsibility

- `qwen2.5-0.5b-instruct`: 2/9 semantic cases passed; produced unsafe false positives and malformed/ungrounded candidates.
- `qwen2.5-coder-0.5b-instruct`: 2/9 passed; similarly produced unsafe false positives.

These models are not merely less accurate. They confused deprecation, future removal, or continued support with actual support changes and are unsuitable for this trusted path.

### Reference result, not accepted

- `qwen3-4b-instruct-2507`: 6/9 passed.
- Correct on explicit drop, paraphrased drop, explicit addition, future-removal abstention, irrelevant text, and multiple facts.
- Failed by treating deprecation as dropped, continued support as added, and an embedded instruction as an actual drop.

It proves the transport and structured-output path, but its false-positive behavior is not acceptable for selection.

### Compatibility unresolved

- `gemma-4-e2b-it` under LM Studio `json_schema` began output with `{ "facts": [` and terminated before completing JSON. This is a structured-output compatibility/truncation failure, not enough evidence to judge semantic ability.
- A `json_object` experiment was added, but the current LM Studio endpoint rejects it with HTTP 400: `response_format.type` must be `json_schema` or `text`.
- Therefore the `json_object` compatibility path is not supported by the actual runtime and must not be treated as viable.
- `ministral-3-3b-instruct-2512` appeared to stall under the current schema-constrained request path and remains unqualified.

## Current trust boundary

- Raw evidence text, model candidate output, trusted extracted facts, and final decisions remain distinct.
- Structured output proves shape only; it does not prove semantic correctness.
- Exact quote grounding blocks invented text but does not independently verify whether `added` versus `dropped` was interpreted correctly.
- Model selection requires discriminating semantic cases, with false positives weighted more heavily than misses.
- The LLM never selects the final recommendation.

## Immediate continuation

Resume from model-method diagnosis, not from adding broader architecture:

1. remove or revise the unsupported `json_object` runtime option before presenting the client as final;
2. decide whether to test Gemma using LM Studio `text` mode plus strict post-parse validation, or defer Gemma as incompatible;
3. improve the extraction method against deprecation, continued support, and prompt-injection false positives;
4. rerun the same bounded proof set against the smallest credible model candidates;
5. select no model unless it passes the critical abstention cases;
6. record final model/method choice and remaining limitations in the working session.

Do not expand into agents, RAG, multiple providers, broad release-note ontologies, or LLM-controlled recommendations.

## Ownership boundary

- Ali identified that manually supplied semantic facts did not satisfy the product responsibility.
- Ali selected local LM Studio, directed testing of smaller models, challenged misleading benchmark interpretation, and stopped further implementation in favor of an accurate state record.
- The implementation and records are substantially AI-generated under Ali direction.
- Model selection and the final extraction method remain unresolved.

## Career boundary

Do not update Career for ordinary project progress, tests, commits, sub-gates, or continuation changes.

Ali explicitly initiates a Career review when he wants Career to inspect UpgradePilot and update coarse project state, capability assessment, workload/capacity, career role, strategy, or durable program commitments.

## Detailed evidence

Use:

- current source and tests;
- `plans/M2_S02_KNOWN_TEXT_SEMANTIC_EXTRACTION_PLAN.md`;
- `working-memory/2026-07-22_M2-S02_llm-extraction-session.md`;
- applicable specifications and ADRs;
- Git history and actual local command output.

Do not copy this continuation into README, `AGENTS.md`, specifications, ADRs, or Career.
