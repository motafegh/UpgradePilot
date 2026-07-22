# 05 — Testing, Model Evaluation, and Diagnosis

**Depth target:** implementation understanding of the current test layers and the ability to interpret failures without mixing their meanings.

**Read with:**

- [`../../tests/test_extraction_validation.py`](../../tests/test_extraction_validation.py)
- [`../../tests/test_llm_extractor.py`](../../tests/test_llm_extractor.py)
- [`../../tests/test_extraction_service.py`](../../tests/test_extraction_service.py)
- [`../../scripts/evaluate_python_support_models.py`](../../scripts/evaluate_python_support_models.py)

## 1. Why one kind of test is not enough

M2-S02 contains several boundaries:

```text
contracts
→ LM Studio request/response
→ model candidate meaning
→ deterministic validation
→ orchestration
→ decision policy
```

A single end-to-end live-model run cannot localize all failures reliably. The repository therefore uses different test layers, each with a narrower question.

## 2. Layer map

| Layer | Main question | Real model required? |
|---|---|---:|
| Contract tests | Are allowed fields, values, and invariants enforced? | No |
| Validator unit tests | Is a supplied candidate admitted or rejected correctly? | No |
| LM Studio boundary tests | Is the request built and the response parsed correctly? | No; fake client |
| Orchestration/integration tests | Do extraction, validation, conversion, and decision compose correctly? | No; fake extractor |
| Live model evaluation | What candidate and trusted outcomes occur with actual local models? | Yes |

The layers complement each other. They are not competing versions of proof.

## 3. Arrange, Act, Assert

Most unit tests follow:

```text
Arrange
→ Act
→ Assert
```

### Arrange

Construct the evidence, candidate, fake client, fake extractor, or expected response.

### Act

Call one behavior such as:

```python
validate_python_support_extraction(...)
extractor.extract(...)
PythonSupportExtractionService(...).extract(...)
evaluate_decision(...)
```

### Assert

Verify observable output or error:

```python
self.assertEqual(result.accepted_facts, ())
self.assertEqual(result.validation_errors, (...,))
self.assertRaisesRegex(LLMExtractionError, "malformed")
```

A useful test name describes behavior, not implementation mechanics.

## 4. Validator unit tests

`test_extraction_validation.py` bypasses the model and constructs candidates directly.

Example responsibility:

```text
Given this evidence and this exact candidate,
will deterministic validation admit or reject it correctly?
```

Representative proof classes include:

- valid grounded candidate accepted;
- quote absent from source rejected;
- version absent from quote rejected;
- instruction-like context rejected;
- deprecation/future/continued support rejected;
- legitimate declarative `report` wording accepted;
- unrelated instruction on another line does not poison a valid line;
- ambiguous quote occurrence rejected;
- invalid version representation rejected;
- unresolved output preserved;
- duplicate candidate rejected;
- contradictory direction rejected;
- unsupported evidence kind rejected.

These tests prove deterministic code behavior for specified inputs. They do not measure whether a real model will generate those inputs.

## 5. LM Studio boundary tests

`test_llm_extractor.py` uses `_FakeClient`.

The fake client records request arguments and returns controlled response objects. This isolates the transport adapter from LM Studio availability and model variability.

The tests verify:

- environment settings are loaded and normalized;
- model identity is required;
- stale `json_object` configuration is rejected;
- non-positive limits are rejected;
- model, temperature, token limit, prompt wrapper, and response format are sent correctly;
- schema-valid JSON becomes an untrusted candidate result;
- diagnostics are preserved;
- no-fact output is preserved;
- empty source text is rejected before a request;
- endpoint exceptions are wrapped;
- malformed, empty, or schema-invalid output is rejected.

These tests prove the code's boundary behavior. They do not prove a model's semantic accuracy.

## 6. Orchestration and decision integration tests

`test_extraction_service.py` uses `_FakeExtractor` rather than a fake HTTP client.

That test starts one layer higher:

```text
controlled candidate extractor
→ PythonSupportExtractionService
→ validator
→ trusted conversion
→ evaluate_decision
```

The positive test proves the demonstrated vertical slice without model variability.

The negative test proves that an ungrounded candidate:

```text
produces validation error
→ creates no accepted fact
→ creates no decision fact
```

This is the nearest deterministic end-to-end proof of the trust boundary and policy composition.

## 7. Live model evaluation is an experiment, not a unit test

`scripts/evaluate_python_support_models.py` performs real LM Studio calls over fourteen semantic cases.

Each `EvaluationCase` has:

```python
case_id
text
expected_facts
```

The evaluator creates a synthetic accepted release-note `EvidenceItem`, invokes the real model, validates its candidates, and records both raw-candidate and trusted-output behavior.

Its results depend on:

- the exact model;
- LM Studio/runtime version;
- model loading and backend;
- prompt and schema;
- token ceiling;
- timeout;
- validator code;
- repeated-run variability.

That makes it valuable experimental evidence but unsuitable as the only deterministic regression suite.

## 8. Three result concepts

The evaluator deliberately separates:

### `candidate_correct`

Does the model's raw proposed fact set match the expected facts?

```python
sorted(candidate_facts) == sorted(expected_facts)
```

This measures candidate/model-method behavior before validation.

### `trusted_output_correct`

Do the validator's accepted facts match the expected facts?

```python
sorted(actual_facts) == sorted(expected_facts)
```

This measures the admitted output of the hybrid boundary.

### `passed`

```python
candidate_correct
and trusted_output_correct
and not validation_errors
```

This is intentionally stricter than trusted-output correctness. A model that produces an unsafe candidate which the validator blocks has correct trusted output but does not receive a clean end-to-end pass.

## 9. Interpret the important combinations

| Candidate | Trusted output | Meaning |
|---|---|---|
| Correct | Correct | Clean model/method behavior for the case |
| Wrong | Correct | Validator intervened successfully or removed an extra candidate |
| Correct | Wrong | Validator falsely rejected, altered coverage, or another boundary failed |
| Wrong | Wrong | Unsafe/incorrect candidate reached trust or expected fact was lost |
| No result due error | Wrong | Request, content, schema, or parsing failure |

Example from the repeated proof:

```text
model follows embedded directive
→ candidate_correct = false
→ validator rejects candidate
→ trusted_output_correct = true
→ passed = false
```

This is why `42/42 trusted` does not mean the models themselves were safe or clean.

## 10. Why the evaluator may exit with status 1

At the end:

```python
return 0 if all(result.passed for result in all_results) else 1
```

If a model candidate is wrong—even when validation protects trusted output—the process returns nonzero.

Interpretation:

- nonzero does not automatically mean the validator failed;
- it means at least one full case was not clean under the evaluator's strict `passed` definition;
- inspect candidate correctness, trusted correctness, validation errors, and request errors separately.

## 11. Repetition versus coverage

Three repetitions of the same fourteen cases provide evidence about repeatability under that configuration.

They do not create forty-two distinct language cases.

```text
14 cases × 3 repetitions
= 42 executions
≠ 42 independent wording patterns
```

Repeated runs help detect instability. New holdout cases help detect wording gaps. These are different evaluation goals.

## 12. Synthetic cases versus real examples

The current cases are synthetic sentences designed to discriminate meanings:

- actual drop/add;
- paraphrase;
- deprecation;
- future removal;
- continued support;
- irrelevance;
- embedded directives;
- legitimate declarative control;
- multiple facts.

Advantages:

- exact expected result is clear;
- a failure can be localized;
- specific semantic distinctions are tested deliberately.

Limitations:

- real release notes are longer and messier;
- formatting, tables, links, bullets, and surrounding context are underrepresented;
- the proof set is small;
- repeated fixture tuning can overstate generality.

The plan correctly treats this as an engineering proof set, not final production evaluation.

## 13. JSON result artifacts

The evaluator supports:

```bash
--json-output <path>
```

It serializes every `CaseResult`, including:

- model and repetition;
- case ID;
- candidate and trusted correctness;
- candidate and accepted facts;
- unresolved output;
- validation errors;
- raw candidate output;
- finish reason;
- token usage;
- latency;
- request/error information.

The console summary is useful for immediate observation. The JSON artifact is needed for later per-case audit and reproducibility evidence.

## 14. Failure diagnosis matrix

| Symptom | First boundary to inspect | Discriminating evidence |
|---|---|---|
| No request made for empty text | Input guard | Fake-client call list remains empty |
| Request exception | Transport/runtime | Wrapped exception and latency |
| Partial JSON | Completion/content | `finish_reason`, raw output, completion/reasoning tokens |
| Schema-invalid JSON | Pydantic/schema | Validation error and output preview |
| Valid but wrong candidate | Model semantics/prompt-method | `candidate_facts` versus expected |
| Wrong candidate blocked | Validator intervention | `validation_errors`, empty/correct trusted facts |
| Legitimate candidate blocked | Validator false rejection | Candidate correct, trusted wrong, error code |
| Accepted fact but policy abstains | Decision rule | `DecisionInput` and current rule conditions |

Do not change multiple layers before localizing the strongest supported failure boundary.

## 15. Narrow commands and what they prove

Run from the repository root in the existing environment.

```bash
python -m unittest discover -s tests -p 'test_extraction_validation.py'
```

Proves: current deterministic validator tests pass.

Does not prove: model behavior or universal wording coverage.

```bash
python -m unittest discover -s tests -p 'test_llm_extractor.py'
```

Proves: request construction, parsing, settings, and controlled failure tests pass using fakes.

Does not prove: LM Studio is running or a real model is semantically correct.

```bash
python -m unittest discover -s tests -p 'test_extraction_service.py'
```

Proves: controlled candidates compose through validation, conversion, and decision policy.

Does not prove: the real model produces the candidate.

```bash
python -m unittest discover -s tests
```

Proves: the complete current deterministic repository test suite passes in this environment.

Does not prove: production readiness, general prompt-injection resistance, or Ali ownership.

```bash
python scripts/evaluate_python_support_models.py \
  --models qwen3-4b-instruct-2507 \
  --repetitions 3 \
  --max-tokens 512 \
  --json-output working-memory/m2-s02-evaluation.json
```

Measures: real configured model behavior plus trusted validation outcomes on the current proof set.

Requires: reachable LM Studio and exact model availability.

## 16. Predict the owning layer

### A

Test error: `UPGRADEPILOT_LLM_MODEL must be set`.

<details>
<summary>Answer</summary>

Runtime configuration validation in `LLMExtractorSettings.from_environment()`.
</details>

### B

Model JSON is valid, candidate says `dropped`, source says `remains supported`, trusted facts are empty.

<details>
<summary>Answer</summary>

Model semantic error plus successful deterministic validator intervention.
</details>

### C

Candidate is correct for a legitimate sentence, but trusted facts are empty with `INSTRUCTION_LIKE_SOURCE_CONTEXT`.

<details>
<summary>Answer</summary>

Likely validator false rejection or a disputed supported-boundary case. Inspect the containing line and pattern match before changing the prompt.
</details>

### D

Accepted dropped-support fact exists, but decision is `abstain`.

<details>
<summary>Answer</summary>

Inspect the deterministic policy's other required evidence. The current `run_targeted_checks` rule also requires missing repository Python-support evidence.
</details>

## 17. Current depth boundary

### Required now

- explain why each test layer exists;
- read Arrange/Act/Assert in current tests;
- explain fake client versus fake extractor;
- calculate candidate, trusted, and clean outcomes;
- interpret nonzero evaluator exit correctly;
- distinguish repetition from new linguistic coverage;
- localize representative failures before proposing repairs.

### Deferred

- formal statistical model evaluation;
- frozen held-out corpus construction;
- confidence intervals and calibration;
- CI integration for live GPU/model experiments;
- production load and reliability testing;
- M5 evaluation-system depth.

## 18. Ownership checkpoint

Answer without reading the tables:

1. What does each of the three current test files isolate?
2. Why can trusted output be correct while `passed` is false?
3. What does repeating fourteen cases three times add, and what does it not add?
4. Why is a fake client better than a real model for transport unit tests?
5. Which evidence distinguishes token truncation from semantic misclassification?
6. What can 62 passing repository tests honestly establish, and what can they not establish?
