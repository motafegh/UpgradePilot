# 04 — LM Studio Structured Output and Experimental Diagnostics

**Depth target:** understand the retained local-model transport, its diagnostic evidence, and why transport success did not justify normal runtime adoption.

**Read with:**

- [`../../src/upgradepilot/llm_extractor.py`](../../src/upgradepilot/llm_extractor.py)
- [`../../tests/test_llm_extractor.py`](../../tests/test_llm_extractor.py)
- [`../../scripts/evaluate_python_support_models.py`](../../scripts/evaluate_python_support_models.py)
- [`../../m2-s02-attributed-claim-decision-effects.json`](../../m2-s02-attributed-claim-decision-effects.json)

## 1. Current status

`LMStudioPythonSupportExtractor` remains implemented and tested, but neither tested local deployment is accepted as the normal M2 extractor.

Its current value is:

- a real OpenAI-compatible local transport example;
- a reproducible experimental provider;
- a source of preserved negative evaluation evidence;
- a future comparison point if learned extraction is reconsidered.

Implemented does not mean adopted.

## 2. Runtime settings

```python
@dataclass(frozen=True)
class LLMExtractorSettings:
    base_url: str
    model: str
    timeout_seconds: float = 60.0
    max_tokens: int = 512
    seed: int = 0
```

Environment variables can supply these values. Required model identity and positive numeric limits are validated before a request.

The recorded seed improves reproducibility evidence, but does not guarantee identical behavior across model files, quantizations, hardware, LM Studio versions, or inference implementations.

## 3. Request boundary

The extractor calls an OpenAI-compatible chat completion with:

```text
model
temperature = 0
seed
max_tokens
system + user messages
response_format = json_schema
```

The release-note text is wrapped in `<release_notes>` tags and explicitly described as untrusted data.

Prompt wording is a behavioral request, not a security boundary. The models still produced instruction-shaped and category errors.

## 4. Structured output

The model schema permits exactly:

```json
{
  "claims": [
    {
      "change": "added | dropped",
      "python_version": "string",
      "source_quote": "string"
    }
  ],
  "unresolved": ["string"]
}
```

The schema does not permit:

- authority;
- evidence state;
- policy outcome;
- merge approval;
- tool calls;
- arbitrary extra fields.

This is valuable representation control. It does not prove semantic correctness.

## 5. Pydantic parsing

```python
CandidateExtractionResult.model_validate_json(content, strict=True)
```

Possible outcomes:

- schema-valid candidate result;
- empty-output error;
- malformed/schema-invalid output error;
- request-level error.

Even a schema-valid result remains untrusted until the application applies mechanical grounding and authority.

## 6. Diagnostics

`LLMResponseDiagnostics` preserves:

```text
raw_output
finish_reason
prompt_tokens
completion_tokens
reasoning_tokens
total_tokens
```

This allowed the project to distinguish:

- token truncation from semantic failure;
- request failure from malformed output;
- fast model behavior from correct behavior;
- reasoning-token use from total completion size.

The malformed-output preview is bounded to avoid dumping unlimited model text into an error message.

## 7. Token-budget failure example

Gemma initially produced truncated JSON under a low completion ceiling because its reported reasoning tokens consumed much of the completion budget.

At a higher ceiling, the JSON completed successfully.

This corrected one diagnosis:

```text
malformed JSON at low budget
→ transport/output-budget failure
```

But later complete responses still contained wrong semantic claims:

```text
finish_reason = stop
valid JSON
wrong meaning
```

Increasing tokens solved the first problem, not the second.

## 8. Warm-up and deployment metadata

The evaluator:

- reuses one client per model;
- can run one unscored warm-up;
- records metadata before and after warm-up;
- saves model architecture, quantization, context, load state, timestamps, configuration, and per-case output where available.

This matters because the compared deployments were not equivalent:

- Gemma used a Q4_K_M 4-bit file;
- Qwen3 used a Q6_K 6-bit file.

The results therefore compare the actual local deployments, not perfectly controlled model architectures.

## 9. What the model can and cannot do

The current extractor receives text and returns JSON.

It has no direct access to:

- shell commands;
- filesystem;
- GitHub mutation;
- credentials;
- external tools;
- merge actions.

Its direct risks are therefore bounded mainly to:

- wrong extraction;
- latency/resource use;
- malformed output;
- contamination of later displayed free text;
- downstream decision effects permitted by application code.

Prompt injection does not magically create tool authority that the application never provided.

## 10. Final semantic evidence

Complete run:

| Deployment | Candidate/grounded correct | Decision-effect correct | Average latency |
|---|---:|---:|---:|
| Gemma | 9/14 | 11/14 | 3.163 s |
| Qwen3 | 8/14 | 10/14 | 0.749 s |

Both produced repeated material false dropped-support claims. Valid JSON, deterministic sampling settings, and fast latency did not compensate for unacceptable decision effects.

## 11. Failure localization

| Symptom | Likely category |
|---|---|
| Endpoint timeout | Transport/runtime |
| Empty message | Response contract |
| Truncated JSON with `finish_reason=length` | Completion budget |
| Unsupported enum value | Schema/model output |
| Correct JSON, wrong claim | Model semantics |
| Correct candidate, quote absent from source | Grounding failure |
| Correct claim, excessive policy effect | Authority/decision policy |

Do not change the prompt when the failure is an evidence-reference invariant. Do not change the validator when the model simply interpreted the sentence incorrectly.

## 12. Why the extractor stays in the repository

Retaining rejected experimental code is justified because it provides:

- reproducible negative evidence;
- a transport reference for later comparative work;
- tests for strict structured-output behavior;
- preserved diagnostics and deployment metadata;
- an explicit reversal path if future models materially improve.

It must remain clearly labeled experimental so presence in `src/` is not mistaken for normal product adoption.

## Ownership check

1. What does JSON Schema prove?
2. What does `finish_reason="stop"` rule out, and what does it not rule out?
3. Why does seed 0 not prove universal determinism?
4. Why is comparing Q4 Gemma and Q6 Qwen a deployment comparison rather than a clean architecture benchmark?
5. Why was the faster Qwen deployment still rejected?
6. Which fields are application-assigned and absent from the model schema?
