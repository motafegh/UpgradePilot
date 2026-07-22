# 03 — LM Studio, Structured Output, and Diagnostics

**Depth target:** implementation understanding of the local model request/response boundary.

**Read with:**

- [`../../src/upgradepilot/llm_extractor.py`](../../src/upgradepilot/llm_extractor.py)
- [`../../tests/test_llm_extractor.py`](../../tests/test_llm_extractor.py)
- [`../../pyproject.toml`](../../pyproject.toml)

## 1. The extractor's exact role

`LMStudioPythonSupportExtractor` sends known release-note text to one local model and asks for schema-valid candidate facts.

Its output is still untrusted:

```text
release-note text
→ LM Studio request
→ JSON response
→ Pydantic candidate contract
→ CandidateExtractionResult
```

The extractor does **not**:

- decide whether the candidate is trusted;
- attach evidence identity to a trusted fact;
- choose `run_targeted_checks` or `abstain`;
- prove that the model understood the sentence correctly.

Those responsibilities belong to later deterministic layers.

## 2. What “OpenAI-compatible” means here

LM Studio exposes a local HTTP API whose request shape is compatible with the OpenAI Python client used by the project.

The repository therefore uses:

```python
from openai import OpenAI
```

with a local base URL:

```python
OpenAI(
    base_url=settings.base_url,
    api_key="lm-studio",
    timeout=settings.timeout_seconds,
)
```

The client library is used as a transport adapter. Requests go to the configured LM Studio endpoint, not automatically to a cloud provider.

The placeholder API key satisfies the client interface; the current local LM Studio endpoint does not use it as a real external credential.

## 3. Runtime settings

`LLMExtractorSettings` holds the model request configuration.

| Environment variable | Purpose | Current default/requirement |
|---|---|---|
| `UPGRADEPILOT_LLM_BASE_URL` | OpenAI-compatible endpoint | `http://localhost:12345/v1` |
| `UPGRADEPILOT_LLM_MODEL` | Exact model identity | Required |
| `UPGRADEPILOT_LLM_TIMEOUT` | Per-request timeout in seconds | `60.0` in the client settings |
| `UPGRADEPILOT_LLM_MAX_TOKENS` | Completion budget | `512` |
| `UPGRADEPILOT_LLM_RESPONSE_FORMAT` | Optional compatibility check | Must be `json_schema` when set |

`from_environment()` strips whitespace, parses numeric values, and rejects:

- a missing model identity;
- an empty base URL;
- non-numeric limits;
- zero or negative limits;
- stale unsupported response formats such as `json_object`.

This keeps configuration outside source code while still validating it before a request.

## 4. The request construction

The key call is:

```python
response = self._client.chat.completions.create(
    model=self.settings.model,
    temperature=0,
    max_tokens=self.settings.max_tokens,
    messages=(...),
    response_format=_response_format(),
)
```

### `model`

Selects the exact model exposed by LM Studio.

The model name is also included in:

```python
extractor_id = f"lm-studio:{settings.model}:json_schema"
```

This gives accepted facts transformation provenance.

### `temperature=0`

Requests low-variation generation.

It may improve repeatability, but it does not prove deterministic or stable semantic behavior across:

- repeated requests;
- runtime versions;
- model revisions;
- hardware/backends;
- changed prompts or token budgets.

That is why repeated live evaluation remains necessary.

### `max_tokens`

Bounds the model's completion budget.

In the observed Gemma failure, reasoning tokens consumed much of a 200-token completion ceiling. The model began correct JSON but stopped with `finish_reason="length"` before completing it.

Increasing the budget allowed a complete response. The lesson was:

> Partial structured output must be diagnosed using finish reason and token usage, not immediately labeled model/schema incompatibility.

### `messages`

The system prompt defines the bounded semantic category and exclusions. The user message wraps the source text in:

```text
<release_notes>
...
</release_notes>
```

and explicitly says embedded instructions are data, not commands.

This is useful prompt guidance, but it is not the trusted security boundary. Both Gemma and Qwen3 still followed several embedded directives.

## 5. The JSON Schema response format

`_candidate_json_schema()` requires one object with exactly:

```json
{
  "facts": [
    {
      "change": "added | dropped",
      "python_version": "string",
      "source_quote": "string"
    }
  ],
  "unresolved": ["string"]
}
```

Important schema controls:

- top-level object required;
- `facts` and `unresolved` required;
- unknown fields forbidden through `additionalProperties: false`;
- `change` restricted to `added` or `dropped`;
- every fact requires all three fields.

### What JSON Schema proves

It can constrain:

- shape;
- required fields;
- allowed field names;
- basic value categories;
- the allowed vocabulary for `change`.

### What JSON Schema cannot prove

It cannot prove:

- the quote actually occurs in the source;
- the Python version occurs in the quote;
- `dropped` is the correct interpretation;
- the source sentence is an assertion rather than an instruction;
- the text describes actual removal rather than deprecation;
- the model abstained safely.

A perfectly schema-valid answer can still be semantically wrong.

## 6. Response parsing

After the request, the extractor reads:

```python
content = response.choices[0].message.content
```

It then:

1. collects diagnostics;
2. rejects missing or empty content;
3. validates the raw JSON string using `CandidateExtractionResult.model_validate_json(..., strict=True)`;
4. returns candidates plus diagnostics when requested.

The ordinary `extract()` method returns only candidates:

```python
return self.extract_with_diagnostics(text).candidates
```

The evaluator uses `extract_with_diagnostics()` because model comparison needs runtime evidence as well as candidate facts.

## 7. Diagnostics

`LLMResponseDiagnostics` preserves:

```python
raw_output
finish_reason
prompt_tokens
completion_tokens
reasoning_tokens
total_tokens
```

These fields help distinguish different failures.

| Observation | Possible interpretation |
|---|---|
| `finish_reason="length"` and output ends mid-JSON | Completion ceiling exhausted |
| Empty output with completion tokens consumed | Model/runtime produced no usable message content |
| Complete JSON but invalid field value | Schema/Pydantic rejection |
| Valid candidates but wrong meaning | Model semantic error |
| Large latency followed by request exception | Runtime, model load, timeout, or endpoint failure |

Diagnostics are evidence for diagnosis. They are not themselves trusted semantic facts.

## 8. Error boundary

The extractor raises `LLMExtractionError` for model-call and model-output failures.

### Request failure

Examples:

- endpoint unavailable;
- timeout;
- server error;
- client exception.

The original exception is preserved as the cause:

```python
raise LLMExtractionError(...) from exc
```

### No usable message content

The response object exists but does not contain accessible message content.

### Empty content

The message content is missing or only whitespace. Available diagnostics are attached to the error.

### Malformed candidate data

The content is not valid against `CandidateExtractionResult`. A bounded single-line preview is included for debugging, and diagnostics remain attached.

The preview is limited to avoid dumping arbitrarily large model output into an error.

## 9. Why the tests use a fake client

`tests/test_llm_extractor.py` defines `_FakeClient` and `_FakeCompletions`.

The fake:

- returns a controlled response or raises a controlled error;
- records the arguments supplied to `create()`;
- requires no network or loaded model;
- makes the tests deterministic and fast.

The tests can therefore prove that the code:

- uses the configured model;
- uses temperature zero;
- forwards the token limit;
- requests `json_schema`;
- includes the release-note wrapper;
- preserves diagnostics;
- rejects empty input before any request;
- wraps endpoint failures;
- rejects malformed or schema-invalid JSON.

They do not prove that a real Qwen or Gemma model follows the prompt correctly.

## 10. Predict before checking

### Case A

The model returns:

```json
{
  "facts": [
    {
      "change": "removed-later",
      "python_version": "3.8",
      "source_quote": "Python 3.8 may be removed later."
    }
  ],
  "unresolved": []
}
```

What happens?

<details>
<summary>Check the answer</summary>

`model_validate_json()` rejects the response because `removed-later` is outside the allowed `change` enum/Literal. The extractor raises `LLMExtractionError` for malformed candidate extraction data. The deterministic extraction validator is not called.
</details>

### Case B

The model returns schema-valid JSON claiming `dropped` for a deprecation sentence.

<details>
<summary>Check the answer</summary>

The extractor successfully returns a `CandidateExtractionResult`. The later deterministic validator must reject the candidate as non-effective support context. This is a semantic admission failure, not a transport/schema failure.
</details>

### Case C

The output begins valid JSON but stops halfway, with `finish_reason="length"`.

<details>
<summary>Check the answer</summary>

The extractor cannot construct a candidate result and raises `LLMExtractionError`. The diagnostics suggest token-budget exhaustion. The discriminating next check is an adequate bounded completion ceiling, not immediately rewriting the schema or changing architecture.
</details>

## 11. Security, privacy, and scope

Current properties:

- model execution is local through LM Studio;
- release-note text remains untrusted content;
- no credentials are embedded in source;
- the model cannot directly produce a trusted fact;
- the model cannot select the final decision;
- timeout and completion budgets are bounded;
- there is no agent loop, tool execution, RAG, model router, or cloud provider abstraction.

Current limitations:

- local execution does not make the model instruction-safe;
- prompt wording is not a security proof;
- model/runtime versions affect reproducibility;
- live evaluation is required to characterize behavior;
- an endpoint failure currently becomes an extraction error rather than an accepted unresolved fact.

## 12. Current depth boundary

### Required now

- locate every environment setting;
- explain the request fields and their purpose;
- explain schema correctness versus semantic correctness;
- use diagnostics to distinguish truncation from incompatibility;
- explain the fake-client test strategy;
- identify where `LLMExtractionError` is raised.

### Deferred

- serving-engine internals;
- GPU backend optimization;
- broad provider abstraction;
- model fine-tuning;
- advanced prompt-security research;
- cloud deployment and operational scaling.

## 13. Ownership checkpoint

Explain without reading:

1. why the project uses the OpenAI client with LM Studio;
2. why `temperature=0` does not establish full determinism;
3. what JSON Schema proves and does not prove;
4. why Gemma's truncated output was initially misdiagnosed;
5. which diagnostics distinguish token exhaustion from semantic error;
6. why unit tests use a fake client while the evaluator uses real models.
