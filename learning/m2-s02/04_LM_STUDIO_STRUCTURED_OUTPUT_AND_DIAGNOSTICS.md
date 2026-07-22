# 04 — LM Studio, Structured Output, and Diagnostics

**Depth target:** implementation understanding of both local model request boundaries and current reproducibility evidence.

**Read with:**

- [`../../src/upgradepilot/llm_extractor.py`](../../src/upgradepilot/llm_extractor.py)
- [`../../src/upgradepilot/llm_input_risk_detector.py`](../../src/upgradepilot/llm_input_risk_detector.py)
- [`../../tests/test_llm_extractor.py`](../../tests/test_llm_extractor.py)
- [`../../tests/test_llm_input_risk_detector.py`](../../tests/test_llm_input_risk_detector.py)
- [`../../scripts/evaluate_python_support_models.py`](../../scripts/evaluate_python_support_models.py)

## 1. Two separate model responsibilities

The current normal proceed path can make two LM Studio calls:

```text
input-risk detector
→ semantic extractor
```

They share transport settings but use different prompts, JSON Schemas, output contracts, and provenance identities.

| Boundary | Candidate output | Trusted decision it cannot make |
|---|---|---|
| Input-risk detector | `CandidateInputRiskAssessment` | proceed/quarantine |
| Semantic extractor | `CandidateExtractionResult` | accepted fact or final recommendation |

Both outputs remain untrusted after schema parsing.

## 2. OpenAI-compatible local transport

The project uses the `openai` Python client against LM Studio's local OpenAI-compatible endpoint.

```python
OpenAI(
    base_url=settings.base_url,
    api_key="lm-studio",
    timeout=settings.timeout_seconds,
)
```

The library is a transport adapter. The configured base URL determines where requests go.

Current default endpoint:

```text
http://localhost:12345/v1
```

## 3. Shared settings

`LLMExtractorSettings` contains:

```python
base_url
model
timeout_seconds
max_tokens
seed
```

Environment variables:

| Variable | Purpose |
|---|---|
| `UPGRADEPILOT_LLM_BASE_URL` | Local OpenAI-compatible endpoint |
| `UPGRADEPILOT_LLM_MODEL` | Exact model identity; required |
| `UPGRADEPILOT_LLM_TIMEOUT` | Request timeout |
| `UPGRADEPILOT_LLM_MAX_TOKENS` | Completion budget |
| `UPGRADEPILOT_LLM_SEED` | Recorded request seed; default `0` |
| `UPGRADEPILOT_LLM_RESPONSE_FORMAT` | Must be `json_schema` when explicitly set |

Settings validate required model identity, numeric values, non-empty base URL, positive timeout/token limits, and supported response format.

## 4. Temperature and seed

Both model calls send:

```python
temperature=0
seed=settings.seed
```

### Temperature zero

Requests low-variation generation.

### Seed

Provides a recorded sampling input and is included in extractor/detector provenance:

```text
lm-studio:<model>:json_schema:seed=0
lm-studio:<model>:input-risk-json-schema:seed=0
```

Accurate claim:

> The seed improves traceability and supports local repeatability checks.

Inaccurate claim:

> The seed guarantees identical behavior across every runtime, backend, quantization, or model revision.

The observed seeded run produced identical raw outputs across three repetitions for each local deployment. That is local evidence, not universal determinism.

## 5. Semantic extractor request

The semantic extractor asks for explicit Python runtime-support changes.

Important request fields:

```python
model=settings.model
temperature=0
seed=settings.seed
max_tokens=settings.max_tokens
messages=(system_prompt, user_text)
response_format=json_schema
```

The user text is wrapped in `<release_notes>` and says embedded instructions are data.

Prompt guidance reduces ambiguity but did not prevent both measured models from following several embedded directives.

## 6. Risk detector request

The risk detector asks for instruction-like manipulation signals.

Its input is wrapped in `<untrusted_text>`, and its schema requires:

```json
{
  "risk_level": "none_detected | suspicious | high",
  "signals": [
    {
      "signal_type": "...",
      "source_quote": "...",
      "explanation": "..."
    }
  ],
  "unresolved": []
}
```

This constrains shape and vocabulary. It cannot prove that a manipulation was detected or absent.

## 7. What JSON Schema proves

JSON Schema can constrain:

- object/array shape;
- required fields;
- allowed field names;
- field types;
- bounded enumerations;
- rejection of unknown properties.

It cannot prove:

- source quote grounding;
- risk-classification correctness;
- semantic direction correctness;
- absence of prompt injection;
- safety of the evidence;
- authority to proceed, accept, or recommend.

Structured output is a data-format control, not a truth mechanism.

## 8. Completion budget and reasoning tokens

`max_tokens` bounds the completion. For some models, reported reasoning tokens are included inside the completion count.

The earlier Gemma output stopped mid-JSON at a 200-token ceiling. Diagnostics showed:

```text
finish_reason=length
completion_tokens=200
reasoning_tokens=149
```

Increasing the bounded ceiling produced complete output. The failure was token exhaustion, not demonstrated JSON-Schema incompatibility.

A healthy example with 507 total tokens meant:

```text
262 prompt + 245 completion = 507 total
```

The 172 reasoning tokens were part of the 245 completion tokens, not an additional 172.

## 9. Diagnostics asymmetry

The semantic extractor currently preserves richer response diagnostics:

```python
raw_output
finish_reason
prompt_tokens
completion_tokens
reasoning_tokens
total_tokens
```

The risk detector currently preserves bounded raw output only when malformed output raises `InputRiskDetectionError`; it does not expose the same full diagnostics object.

This is an implementation difference to recognize, not hide.

## 10. Error boundaries

### Semantic extractor

Raises `LLMExtractionError` for:

- request failure;
- missing/empty message content;
- malformed or schema-invalid candidate data.

Available diagnostics are attached when possible.

### Risk detector

Raises `InputRiskDetectionError` for:

- request failure;
- empty output;
- malformed/schema-invalid assessment.

The orchestration service converts this specific detector error into explicit quarantine evidence.

Therefore the same transport-style failure has different application treatment:

```text
risk detector failure → quarantine before extraction
semantic extractor failure after proceed → extraction error
```

## 11. Fake-client tests

Both model-boundary test files inject fake OpenAI-compatible clients.

They prove request construction and parsing without:

- network access;
- loaded models;
- GPU/runtime variability;
- slow inference.

Semantic-extractor tests inspect model, temperature, token limit, response format, diagnostics, and malformed output.

Risk-detector tests inspect temperature, seed, response format, input wrapper, request error wrapping, and malformed assessment output.

These tests do not measure real model semantics.

## 12. Seeded semantic evaluator improvements

The semantic evaluator now:

- creates one extractor/client per model rather than per case;
- sends one recorded seed with every request;
- performs one harmless unscored warm-up by default;
- captures LM Studio model metadata before and after warm-up;
- records quantization, architecture, capabilities, context length, and loaded instances when available;
- saves configuration, model runs, summaries, and per-case results in one self-describing JSON report.

### Why reuse one client?

It avoids repeatedly constructing the transport boundary and better represents one loaded local deployment over the scored run.

### Why warm up?

The first request may include model loading and cold-start cost. An unscored warm-up separates that cost from warm scored latency.

### Why capture metadata?

Model names alone do not fully describe local deployments. Quantization and loaded state can materially affect latency, memory use, and comparability.

The observed Gemma and Qwen files used different quantizations, so their results are deployment comparisons, not controlled architecture benchmarks.

## 13. Predict before checking

### A — Same seed, different quantization

Can the results be described as a controlled model-architecture comparison?

<details>
<summary>Expected answer</summary>

No. They compare the actual local deployments, which differ in quantization and potentially other runtime factors.
</details>

### B — Warm-up takes 12 seconds, scored average is 0.7 seconds

<details>
<summary>Expected answer</summary>

The warm-up likely includes loading/cold-start overhead. It is unscored and should be reported separately from warm case latency.
</details>

### C — Valid detector JSON says `none_detected` for an attack

<details>
<summary>Expected answer</summary>

The model boundary succeeded structurally but failed semantically. Deterministic risk validation cannot invent the missing signal if the candidate is internally consistent, so the route may proceed.
</details>

### D — Risk-detector JSON truncates on an attack

<details>
<summary>Expected answer</summary>

The detector raises `InputRiskDetectionError`; normal orchestration quarantines. The model evaluation should still record a detector/output failure rather than claim a clean semantic detection.
</details>

## 14. Current depth boundary

### Required now

- explain both prompts/schemas and their different responsibilities;
- explain settings, seed, temperature, and provenance IDs;
- explain JSON Schema limits;
- diagnose token exhaustion from diagnostics;
- distinguish cold warm-up from scored latency;
- explain model metadata and quantization caveats;
- explain the different treatment of detector and extractor failures.

### Deferred

- serving-engine internals;
- controlled cross-quantization benchmarking;
- GPU optimization;
- cloud provider abstraction;
- model fine-tuning;
- production deployment and observability.

## 15. Ownership checkpoint

Explain without reading:

1. why the same settings class can support two different model responsibilities;
2. what the seed establishes and does not establish;
3. why JSON Schema does not create trusted output;
4. how reasoning tokens caused the earlier truncation diagnosis;
5. why warm-up and metadata were added;
6. how risk-detector failure treatment differs from semantic-extractor failure treatment.
