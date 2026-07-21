# M2-S02 LLM Extraction Session

**Status:** Paused after first working vertical slice; model selection unresolved  
**Date:** 2026-07-22  
**Owner:** Ali Rajabi  
**Controlling plan:** `../plans/M2_S02_KNOWN_TEXT_SEMANTIC_EXTRACTION_PLAN.md`

## Session outcome

Establish the first real known-text semantic-extraction path for Python runtime-support changes using Ali's existing LM Studio setup, while preserving a deterministic trusted boundary and the existing deterministic recommendation policy.

The implemented path is:

```text
accepted release-note evidence
→ local LM Studio model
→ untrusted structured candidate facts
→ deterministic validation and grounding
→ trusted Python-support facts or explicit unresolved/rejected result
→ existing deterministic decision rule
```

The first real vertical slice works. A production model and final response-format method are not yet selected.

## Accepted method direction

Use the Sentinel-proven local connection pattern in a smaller UpgradePilot-specific form:

- LM Studio provides the local OpenAI-compatible endpoint;
- configuration comes from environment variables rather than hardcoded host or model values;
- one bounded chat/instruct model performs natural-language extraction;
- temperature is zero or effectively deterministic;
- timeout and output-token limits are explicit;
- model output remains untrusted until deterministic validation succeeds;
- the LLM does not make the final recommendation;
- no LangChain, LangGraph, agents, RAG, embeddings, or model-routing framework is added for this responsibility.

## Implemented source

- `src/upgradepilot/extraction.py`
  - `CandidatePythonSupportChange`
  - `CandidateExtractionResult`
  - `ExtractedPythonSupportChange`
  - `ExtractionResult`
  - `PythonSupportExtractionService`
  - conversion from accepted extracted facts to existing decision facts
- `src/upgradepilot/extraction_validation.py`
  - accepted evidence and evidence-kind checks
  - Python major.minor validation
  - exact quote grounding
  - version-in-quote validation
  - duplicate and contradiction handling
- `src/upgradepilot/llm_extractor.py`
  - direct OpenAI-compatible LM Studio client
  - environment-backed base URL, model, timeout, output limit, and response-format setting
  - bounded malformed-output preview
- `scripts/evaluate_python_support_models.py`
  - repeated semantic proof set
  - per-case progress, latency, failures, validation errors, and JSON result output
  - stops a model after request-level failure

No broad framework was added.

## Verified runtime

LM Studio is reachable at:

```text
http://localhost:12345/v1
```

The server exposed multiple local models including:

- `qwen2.5-0.5b-instruct`
- `qwen2.5-coder-0.5b-instruct`
- `ministral-3-3b-instruct-2512`
- `gemma-4-e2b-it`
- `qwen3-4b-instruct-2507`
- larger models not yet justified for this bounded task

After repairing JSON-array to strict-tuple validation at the JSON boundary, local checks reached:

```text
50 tests passed
compileall passed
```

## Real vertical-slice proof

Using `qwen3-4b-instruct-2507` and the real service path:

```text
"Soup Sieve 2.8 drops Python 3.8 support."
→ candidate dropped Python 3.8 with exact source quote
→ accepted grounded fact attached to release-notes-001
→ PythonSupportChange conversion
→ evaluate_decision(...)
→ run_targeted_checks
```

Observed decision reason:

```text
PYTHON_SUPPORT_DROP_UNRESOLVED
```

The model did not select the decision or targeted checks.

## Semantic proof set

The current evaluation cases cover:

- explicit drop;
- paraphrased drop;
- explicit addition;
- deprecation only;
- possible future removal;
- continued support;
- irrelevant text;
- embedded instruction attempting to invent a fact;
- multiple explicit facts.

False positives on abstention cases are treated as more serious than ordinary misses.

## Model evidence

### `qwen2.5-0.5b-instruct`

Result: `2/9` passed.

Material failures included:

- wrong direction for paraphrased drop;
- deprecation treated as an addition;
- future removal treated as an addition;
- continued support treated as an addition;
- malformed or request-level failures on abstention cases.

Disposition: rejected for this responsibility.

### `qwen2.5-coder-0.5b-instruct`

Result: `2/9` passed.

Material failures were similar, including unsafe false positives and malformed/ungrounded candidates.

Disposition: rejected for this responsibility.

### `qwen3-4b-instruct-2507`

Result: `6/9` passed, average observed latency about `3.463s` over nine cases.

Passed:

- explicit drop;
- paraphrased drop;
- explicit addition;
- future-removal abstention;
- irrelevant text;
- multiple facts.

Failed:

- deprecation interpreted as dropped;
- continued support interpreted as added;
- embedded instruction interpreted as a real drop.

Disposition: useful transport/vertical-slice reference, not acceptable for production selection.

### `gemma-4-e2b-it`

Under `json_schema`, the first explicit-drop request returned truncated output:

```text
{ "facts": [
```

This is a structured-output compatibility or truncation failure. It does not establish semantic failure.

A `json_object` compatibility option was then added, but the actual LM Studio endpoint rejected it:

```text
HTTP 400
'response_format.type' must be 'json_schema' or 'text'
```

Disposition: unresolved. The current runtime supports `json_schema` or `text`, not `json_object`.

### `ministral-3-3b-instruct-2512`

The model appeared to stall under the schema-constrained request path. The evaluator originally hid progress by collecting all cases before printing; this was repaired. Ministral remains unqualified and is no longer a default candidate.

## Observed repairs

1. JSON output arrays were parsed into Python lists and rejected by strict tuple contracts. Repaired by validating directly from JSON with `model_validate_json(..., strict=True)`.
2. Malformed-output errors originally hid the model response. Added a bounded raw-output preview.
3. The evaluator originally appeared frozen because it printed after all cases. Changed to print before and after each case, use shorter defaults, and stop after request-level failure.
4. A `json_object` compatibility assumption proved false for the actual LM Studio API. This option must be removed, revised, or explicitly treated as unsupported before the client is finalized.

## Current understanding boundary

Established at implementation depth:

- raw text, candidate output, trusted fact, and decision are separate states;
- JSON Schema constrains shape but cannot prove meaning;
- exact quote grounding prevents invented supporting text but does not prove correct direction;
- deterministic validation controls admission to trusted facts;
- semantic variation tests are required to evaluate the model;
- transport compatibility, structured-output compliance, and semantic accuracy are separate gates.

Not established yet:

- an acceptable smallest model;
- a final prompt/method robust to negation, deprecation, continued support, and embedded instructions;
- whether Gemma should be tested through `text` mode with strict post-parse validation;
- whether any current local small model meets the production gate.

## Next continuation point

Do not add broader architecture. Continue with the smallest diagnostic step:

1. remove or correct the unsupported `json_object` method;
2. decide whether `text` mode plus strict local parsing is justified for Gemma;
3. harden the extraction method against the three observed 4B false-positive classes;
4. rerun the exact same proof set;
5. test additional small models only when their transport method is valid;
6. select no production model unless critical abstention cases pass;
7. rerun the complete repository checks after any client correction.

## Assistance and ownership

- Ali identified the original manual semantic gap.
- Ali selected local LM Studio and directed the comparison toward smaller models appropriate to the bounded task.
- Ali supplied and ran all real local commands, surfaced the tuple/JSON failure, verified the end-to-end path, challenged misleading model-failure interpretation, and chose to pause for an accurate memory update.
- The implementation, tests, evaluator, and records are substantially AI-generated under Ali direction.
- Final model and method selection remain open.

## Forbidden expansion

Do not add merely for architectural appearance:

- LangChain or LangGraph;
- autonomous agents or tool-selection loops;
- RAG, embeddings, vector databases, or graphs;
- live GitHub, PyPI, or web acquisition;
- model fine-tuning or a training corpus;
- multiple-provider abstraction;
- cloud deployment, persistence, queues, services, or workflow engines;
- LLM-controlled final recommendations;
- broad semantic routing across every release-note category;
- a universal compatibility ontology.
