# 03 — Input-Risk Screening and Quarantine

**Depth target:** implementation understanding of the pre-extraction risk gate and its limitations.

**Read with:**

- [`../../src/upgradepilot/input_risk.py`](../../src/upgradepilot/input_risk.py)
- [`../../src/upgradepilot/llm_input_risk_detector.py`](../../src/upgradepilot/llm_input_risk_detector.py)
- [`../../tests/test_input_risk.py`](../../tests/test_input_risk.py)
- [`../../tests/test_llm_input_risk_detector.py`](../../tests/test_llm_input_risk_detector.py)
- [`../../tests/test_extraction_service.py`](../../tests/test_extraction_service.py)

## 1. Why this gate exists

Both current semantic-extraction models followed instruction-like text embedded in release notes. A separate detector was therefore placed before semantic extraction.

The gate is **defense in depth**:

```text
untrusted source text
→ risk detector proposes signals
→ deterministic validation chooses proceed/quarantine
→ semantic extraction runs only on proceed
```

The detector is not trusted and `none_detected` is not a safety certificate.

## 2. Preserved text versus inspection text

`prepare_untrusted_text()` does not overwrite the evidence observation.

It creates a derived `PreparedUntrustedText` with:

- normalized newlines;
- Unicode NFKC normalization;
- SHA-256 of the inspection text;
- preprocessing findings.

### Why NFKC?

**NFKC** means *Normalization Form Compatibility Composition*.

Practical purpose: visually or semantically similar Unicode forms are converted into a more consistent inspection representation. This can expose some concealed or confusing text forms to the detector.

NFKC can change representation, so the original evidence must remain preserved separately.

### Suspicious control characters

The preprocessor scans Unicode categories `Cc` and `Cf`, except normal newline, carriage return, and tab characters.

A suspicious control character adds:

```text
SUSPICIOUS_CONTROL_CHARACTER
```

Any preprocessing finding forces quarantine.

The preprocessor detects only the encoded controls it was designed to expose. It is not a universal deobfuscator.

## 3. Detector output is a candidate

`LMStudioInputRiskDetector` asks a local model to classify the text into:

```text
none_detected
suspicious
high
```

It may propose signals such as:

```text
instruction_override
output_manipulation
role_impersonation
tool_request
secret_request
encoded_or_concealed_instruction
other_instruction_like_content
```

Each signal must include an exact source quote and explanation.

The candidate is schema-constrained, but still untrusted because the model may:

- miss an attack;
- invent a quote;
- produce inconsistent risk and signals;
- misclassify benign text;
- obey instructions targeting the detector itself.

## 4. Deterministic risk validation

`validate_input_risk_assessment()` checks stable invariants.

### Consistency rules

```text
none_detected + signals
→ NONE_DETECTED_WITH_SIGNALS
```

```text
suspicious/high + no signals
→ RISK_LEVEL_WITHOUT_SIGNALS
```

### Grounding rule

Each `signal.source_quote` must occur in `prepared.inspection_text`.

An invented quote produces:

```text
signal[index]: SOURCE_QUOTE_NOT_FOUND
```

### Route rule

The initial route is `proceed`, but any of these force `quarantine`:

- risk level is not `none_detected`;
- detector reports unresolved uncertainty;
- deterministic validation error exists;
- preprocessing finding exists.

This means only a clean, grounded, `none_detected` assessment with no uncertainty and no suspicious preprocessing can proceed.

## 5. Detector failure is explicit application state

The detector raises `InputRiskDetectionError` for request, empty-output, or malformed-output failures.

The service catches that error and calls `failed_input_risk_assessment()`.

Result:

```text
risk_level = high
route = quarantine
unresolved = INPUT_RISK_DETECTOR_ERROR: ...
```

This preserves the distinction between:

```text
attack detected
```

and:

```text
required detector could not complete
```

Both route to quarantine, but for different observable reasons.

## 6. Why `none_detected` does not mean safe

The validated assessment carries this limitation:

```text
Input-risk detection reduces exposure but does not establish that text is safe.
```

A false negative can still reach semantic extraction. Therefore:

- semantic model output remains untrusted;
- post-extraction validation remains active;
- detector output cannot reduce decision caution;
- absence of a detected signal cannot prove an update safe.

The route means:

```text
proceed with the next bounded control
```

not:

```text
trust the content
```

## 7. Why the detector is separate from the semantic extractor

Combining risk classification and support-change extraction into one model response would blur responsibilities.

Separate boundaries make it possible to observe:

- whether the detector quarantined;
- whether semantic extraction ran;
- which model and seed produced each transformation;
- whether a failure belongs to risk detection or semantic interpretation;
- whether different local models should perform the two responsibilities.

A real demonstrated path used Qwen as detector and Gemma as extractor. That is possible because the service depends on two protocols rather than one combined model component.

## 8. The risk detector's LM Studio request

The detector uses the same `LLMExtractorSettings` class as the semantic extractor.

It sends:

```python
model=settings.model
temperature=0
seed=settings.seed
max_tokens=settings.max_tokens
response_format=json_schema
```

Its provenance ID includes responsibility and seed:

```text
lm-studio:<model>:input-risk-json-schema:seed=<seed>
```

The detector's JSON Schema restricts structure and vocabulary. It does not prove detection correctness.

## 9. Tests and what they prove

### `test_input_risk.py`

Deterministic tests directly supply detector candidates and prove:

- clean `none_detected` may proceed without claiming safety;
- grounded high-risk signal quarantines;
- invented detector quote fails closed;
- inconsistent `none_detected` fails closed;
- suspicious control data quarantines.

### `test_llm_input_risk_detector.py`

Fake-client tests prove:

- the request uses temperature zero, configured seed, JSON Schema, and input wrapper;
- structured response becomes an untrusted candidate assessment;
- request failure is wrapped;
- invalid schema output is rejected with bounded raw-output evidence.

### `test_extraction_service.py`

Service tests prove:

- quarantine prevents the extractor call;
- detector failure also prevents extraction;
- proceed permits extraction and retains the risk assessment.

## 10. Predict before checking

### A — Clean candidate, suspicious control character

The model returns `none_detected`, no signals, no unresolved output. Preprocessing found a zero-width control character.

<details>
<summary>Expected result</summary>

`quarantine`, because preprocessing findings independently force fail-closed routing.
</details>

### B — High risk with invented quote

<details>
<summary>Expected result</summary>

`SOURCE_QUOTE_NOT_FOUND` plus `quarantine`. The risk level already quarantines, and invalid grounding is also recorded.
</details>

### C — Detector malformed JSON on an obvious attack

<details>
<summary>Expected result</summary>

The detector raises `InputRiskDetectionError`; the service represents the failure as explicit quarantine. Operational containment succeeds, but the detector evaluation should still record a model/output failure rather than award semantic detection credit.
</details>

### D — False-negative `none_detected`

<details>
<summary>Expected result</summary>

The route may proceed. This demonstrates the detector's limitation and why downstream untrusted-candidate validation and deterministic decision authority remain necessary.
</details>

## 11. False negatives and false positives

### False negative

Instruction-like manipulation is present but the route is `proceed`.

This increases exposure to the semantic extractor.

### False positive

Benign release-note text is quarantined.

This lowers useful coverage and may prevent legitimate extraction.

Both matter. Fail-closed routing reduces unsafe continuation but does not make over-quarantine costless.

## 12. Current evaluation boundary

The current risk evaluator includes benign controls and explicit attacks. It is evidence for the tested set only.

Still needed at the responsibility level:

- adaptive wording;
- obfuscation and encoding;
- quoted instructions;
- multilingual attacks;
- benign near-neighbor controls;
- false-negative and false-positive analysis beyond the seed set.

Do not repair every new miss by adding phrase-specific production rules. The selected project method must generalize beyond a growing list of known attack strings.

## 13. Current depth boundary

### Required now

- explain preprocessing and preserved-source separation;
- trace candidate assessment into deterministic route;
- list every quarantine trigger;
- explain detector failure handling;
- explain `none_detected` accurately;
- distinguish detector unit tests, transport tests, and live evaluation;
- name realistic false-negative and false-positive risks.

### Deferred

- universal prompt-injection detection;
- full Unicode security analysis;
- multilingual and encoded-attack coverage;
- production security guarantees;
- a final responsibility-level authority method.

## 14. Ownership checkpoint

Explain without reading:

1. what NFKC changes and why the original evidence is preserved;
2. which fields the detector proposes and which route deterministic code creates;
3. all conditions that force quarantine;
4. why an invented high-risk quote is still invalid;
5. why detector failure and attack detection should remain distinguishable;
6. why `none_detected` cannot justify a safer final recommendation.
