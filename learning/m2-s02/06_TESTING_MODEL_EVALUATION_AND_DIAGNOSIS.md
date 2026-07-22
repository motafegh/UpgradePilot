# 06 — Testing, Model Evaluation, and Diagnosis

**Depth target:** implementation understanding of the current deterministic test layers, two live evaluators, and failure localization.

**Read with:**

- [`../../tests/test_input_risk.py`](../../tests/test_input_risk.py)
- [`../../tests/test_llm_input_risk_detector.py`](../../tests/test_llm_input_risk_detector.py)
- [`../../tests/test_extraction_validation.py`](../../tests/test_extraction_validation.py)
- [`../../tests/test_llm_extractor.py`](../../tests/test_llm_extractor.py)
- [`../../tests/test_extraction_service.py`](../../tests/test_extraction_service.py)
- [`../../scripts/evaluate_input_risk_models.py`](../../scripts/evaluate_input_risk_models.py)
- [`../../scripts/evaluate_python_support_models.py`](../../scripts/evaluate_python_support_models.py)

## 1. Why several proof layers exist

The current pipeline has distinct boundaries:

```text
preprocessing
→ risk-detector transport and candidate
→ deterministic risk validation/routing
→ semantic-extractor transport and candidate
→ deterministic semantic validation
→ orchestration
→ decision policy
```

One live end-to-end result cannot reliably localize every failure. Each test layer asks a narrower question.

## 2. Current layer map

| Layer | Main question | Real model? |
|---|---|---:|
| Contract tests | Are allowed shapes, values, and invariants enforced? | No |
| Input-risk deterministic tests | Does a supplied detector candidate route correctly? | No |
| Risk-detector boundary tests | Is the request built and response parsed correctly? | No; fake client |
| Semantic-validator tests | Is a supplied extraction candidate admitted/rejected correctly? | No |
| Semantic-extractor boundary tests | Is semantic request/parsing/diagnostics behavior correct? | No; fake client |
| Service integration tests | Do screening, quarantine/proceed, extraction, validation, and decision compose? | No; fake detector/extractor |
| Input-risk live evaluator | How do real models route benign and adversarial text? | Yes |
| Semantic live evaluator | How do real models propose facts, and what does post-validation admit? | Yes |

## 3. Arrange, Act, Assert

Most deterministic tests follow:

```text
Arrange → Act → Assert
```

- **Arrange:** construct evidence, candidate, fake detector/extractor/client, or response.
- **Act:** call one owned behavior.
- **Assert:** verify result, route, error, provenance, or whether a dependency was called.

A good assertion checks the boundary, not only a final count.

Example quarantine proof:

```python
self.assertIsNone(extractor.received_text)
```

This proves semantic extraction never ran.

## 4. Input-risk deterministic tests

`test_input_risk.py` directly supplies candidate assessments.

It proves current deterministic behavior for:

- clean `none_detected` → proceed, with explicit limitation;
- grounded high risk → quarantine;
- ungrounded detector signal → validation error and quarantine;
- `none_detected` plus signals → inconsistency and quarantine;
- suspicious control character → quarantine.

These tests do not measure whether a real model detects attacks.

## 5. Risk-detector boundary tests

`test_llm_input_risk_detector.py` injects a fake OpenAI-compatible client.

It proves:

- configured model request is made;
- temperature zero and seed are forwarded;
- JSON Schema response format is used;
- input is wrapped as untrusted text;
- schema-valid response becomes an untrusted candidate;
- request errors are wrapped in `InputRiskDetectionError`;
- malformed assessment output is rejected with bounded raw-output evidence.

It does not prove semantic detection quality or LM Studio availability.

## 6. Semantic-validator tests

`test_extraction_validation.py` bypasses the model and supplies candidate facts directly.

It isolates:

```text
Given this evidence and exact candidate,
what does deterministic admission do?
```

Representative classes include grounding, version, instruction context, non-effective support context, ambiguity, duplicate, contradiction, unresolved preservation, and evidence-kind checks.

## 7. Semantic-extractor boundary tests

`test_llm_extractor.py` uses a fake client to prove:

- settings and environment parsing;
- model, temperature, seed, token limit, prompt wrapper, and JSON Schema request;
- response diagnostics;
- empty-input short circuit;
- endpoint-error wrapping;
- empty/malformed/schema-invalid output rejection;
- direct JSON validation into tuple-based contracts.

These tests do not prove Qwen or Gemma understands release notes.

## 8. Service integration tests

`test_extraction_service.py` injects:

```text
_FakeRiskDetector
_FakeExtractor
```

It proves two control-flow branches.

### Proceed branch

- risk detector receives inspection text;
- semantic extractor receives original observation;
- risk route is attached as `proceed`;
- semantic candidate is validated;
- accepted fact converts into policy input;
- demonstrated evidence produces `run_targeted_checks`.

### Quarantine branch

- suspicious detector result or detector failure routes to quarantine;
- extractor is not called;
- accepted facts remain empty;
- `INPUT_RISK_QUARANTINED` is explicit;
- detector evidence/error is preserved.

The service test is the nearest deterministic proof of the screened vertical slice.

## 9. Input-risk live evaluator

`evaluate_input_risk_models.py` measures route behavior over eleven current cases:

- five benign controls;
- six instruction-like attacks.

Each result records:

```python
model
case_id
expected_route
actual_route
passed
risk_level
signal_types
latency_seconds
error
```

### Important error interpretation

On detector exception, the evaluator records:

```text
actual_route = quarantine
passed = false
```

Why? Operational fail-closed containment occurred, but the detector did not produce a valid assessment for the test case. The evaluator does not award a clean semantic pass merely because failure happened to quarantine.

This distinction explains Gemma's observed case: malformed/truncated output caused quarantine, while a larger token budget later showed the attack was semantically detected.

## 10. Semantic live evaluator

`evaluate_python_support_models.py` intentionally evaluates:

```text
semantic extractor
→ post-extraction validator
```

It does **not** call the normal `PythonSupportExtractionService` or pre-extraction risk detector. This isolation is deliberate: it measures raw semantic candidate behavior and validator intervention without the earlier gate hiding those outcomes.

Each scored result separates:

- `candidate_correct`;
- `trusted_output_correct`;
- `passed`;
- candidate facts;
- accepted facts;
- validation errors;
- diagnostics and latency.

## 11. Candidate, trusted, and clean outcomes

### Candidate correctness

Does the semantic model's proposed fact set match expected facts?

### Trusted-output correctness

Do accepted post-validation facts match expected facts?

### Clean pass

```python
candidate_correct
and trusted_output_correct
and no validation_errors
```

Therefore:

| Candidate | Trusted | Meaning |
|---|---|---|
| correct | correct | clean case |
| wrong | correct | validator intervened successfully |
| correct | wrong | validator false rejection or other admission failure |
| wrong | wrong | incorrect candidate not safely contained or expected fact lost |

A blocked unsafe candidate can produce correct trusted output while `passed` remains false.

## 12. Seed, repetition, warm-up, and metadata

The semantic evaluator now improves reproducibility evidence by:

- recording a seed sent with every request;
- reusing one client/extractor per model;
- running one unscored warm-up by default;
- capturing model metadata before and after warm-up;
- recording quantization and loaded instances when available;
- saving one self-describing report with configuration, model runs, summaries, and results.

### Repetition

```text
14 cases × 3 repetitions = 42 executions
```

This measures local repeatability under the recorded configuration. It is not forty-two independent wording patterns.

### Warm-up

Separates cold model-load/first-inference cost from scored warm latency.

### Metadata

Prevents pretending that model name alone describes the deployment. Different quantizations make the comparison a local deployment comparison, not a controlled architecture benchmark.

## 13. Two evaluators answer different questions

| Evaluator | Primary question |
|---|---|
| Input-risk evaluator | Does the detector/risk-validation route benign text to proceed and attacks to quarantine? |
| Semantic evaluator | What semantic candidates does the extractor propose, and what does post-validation trust? |

Do not combine their pass counts as though they were one metric.

A full screened application path also depends on service orchestration and deterministic decision tests.

## 14. Synthetic proof-set limits

Synthetic cases are useful because expected behavior is explicit and failures are discriminating.

They remain limited because real evidence can contain:

- long paragraphs and multiple sections;
- Markdown, tables, links, and code blocks;
- quoted or historical instructions;
- obfuscated or multilingual manipulation;
- unfamiliar semantic categories;
- context relationships spanning lines.

Passing the current set does not establish production readiness or responsibility-complete generalization.

## 15. Failure-diagnosis matrix

| Symptom | First boundary | Discriminating evidence |
|---|---|---|
| Unicode/control finding before model | Preprocessing | `preprocessing_findings` and inspection hash |
| Detector valid but wrong route | Detector semantics/risk method | expected vs actual route, risk/signals |
| Detector malformed or times out | Detector transport/output | `InputRiskDetectionError`, raw preview, latency |
| Quarantine but extractor was called | Orchestration defect | fake extractor call record |
| Semantic partial JSON | Completion budget/output | finish reason and token diagnostics |
| Valid but wrong semantic candidate | Extractor semantics | candidate facts vs expected |
| Unsafe semantic candidate blocked | Validator intervention | validation error and correct trusted facts |
| Legitimate candidate blocked | Validator false rejection | candidate correct, trusted wrong |
| Accepted fact but `abstain` | Decision policy/evidence combination | policy rule conditions and `DecisionInput` |

Do not change multiple layers before localizing the strongest supported boundary.

## 16. Commands and honest conclusions

```bash
python -m unittest discover -s tests -p 'test_input_risk.py'
```

Proves current deterministic risk-validation tests pass. Does not prove real detector accuracy.

```bash
python -m unittest discover -s tests -p 'test_llm_input_risk_detector.py'
```

Proves fake-client request/parsing/error behavior. Does not prove LM Studio runtime behavior.

```bash
python -m unittest discover -s tests -p 'test_extraction_validation.py'
python -m unittest discover -s tests -p 'test_llm_extractor.py'
python -m unittest discover -s tests -p 'test_extraction_service.py'
```

Prove their respective deterministic boundaries and composition.

```bash
python -m unittest discover -s tests
```

Current project records report 76 passing tests. Passing establishes the encoded deterministic repository behavior in that environment—not model safety, broad language coverage, production readiness, or Ali ownership.

```bash
python scripts/evaluate_input_risk_models.py \
  --models qwen3-4b-instruct-2507 \
  --seed 0 \
  --max-tokens 512 \
  --json-output working-memory/input-risk-results.json
```

Measures current risk routes on the selected live cases.

```bash
python scripts/evaluate_python_support_models.py \
  --models gemma-4-e2b-it qwen3-4b-instruct-2507 \
  --seed 0 \
  --repetitions 3 \
  --max-tokens 512 \
  --json-output working-memory/semantic-results.json
```

Measures current semantic candidate and post-validation behavior with warm-up/metadata by default.

## 17. Predict the owning layer

### A

Risk model returns `none_detected` plus one signal.

<details>
<summary>Answer</summary>

Candidate structure may parse, but deterministic risk validation records inconsistency and quarantines.
</details>

### B

Detector output truncates on an attack; application quarantines.

<details>
<summary>Answer</summary>

Operational fail-closed routing succeeded, but detector evaluation should record a failed assessment, not a clean detection pass.
</details>

### C

Semantic evaluator reports candidate wrong, trusted correct, validation error present.

<details>
<summary>Answer</summary>

Post-extraction validation contained the model error. Trusted output is correct, but the case is not clean.
</details>

### D

Full service quarantines benign command-documentation text.

<details>
<summary>Answer</summary>

Investigate detector/risk-method false positive and route evidence before changing semantic extraction or policy.
</details>

## 18. Current depth boundary

### Required now

- explain every test layer;
- distinguish fake client, fake detector, and fake extractor;
- explain why semantic evaluation bypasses the pre-risk gate;
- interpret detector error quarantine versus clean detector pass;
- interpret candidate/trusted/clean metrics;
- explain seed, repetition, warm-up, metadata, and quantization caveats;
- localize representative failures.

### Deferred

- frozen held-out corpus design;
- formal statistical evaluation and confidence intervals;
- production load/reliability testing;
- CI for live GPU experiments;
- M5-level evaluation architecture.

## 19. Ownership checkpoint

Answer without reading:

1. What does each current test file isolate?
2. Why does the semantic evaluator bypass the normal risk gate?
3. Why can detector failure quarantine but still fail evaluation?
4. Why can trusted semantic output be correct while clean pass is false?
5. What do seed, repetitions, and warm-up each contribute?
6. Why do different quantizations limit model-comparison claims?
7. What can 76 passing tests honestly establish and not establish?
