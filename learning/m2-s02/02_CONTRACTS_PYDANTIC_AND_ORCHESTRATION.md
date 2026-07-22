# 02 — Contracts, Pydantic, and Orchestration

**Depth target:** implementation understanding of the current data contracts and two-stage service composition.

**Read with:**

- [`../../src/upgradepilot/evidence.py`](../../src/upgradepilot/evidence.py)
- [`../../src/upgradepilot/input_risk.py`](../../src/upgradepilot/input_risk.py)
- [`../../src/upgradepilot/extraction.py`](../../src/upgradepilot/extraction.py)
- [`../../src/upgradepilot/decision.py`](../../src/upgradepilot/decision.py)
- [`../../tests/test_extraction_service.py`](../../tests/test_extraction_service.py)

## 1. What a contract means here

A contract defines which data may cross a boundary and which encoded invariants must already hold.

Current examples:

- `EvidenceItem` — preserved normalized evidence input;
- `PreparedUntrustedText` — derived inspection view;
- `CandidateInputRiskAssessment` — untrusted detector output;
- `InputRiskAssessment` — validated detector evidence and deterministic route;
- `CandidateExtractionResult` — untrusted semantic-extractor output;
- `ExtractionResult` — application result containing accepted/rejected state and risk evidence;
- `DecisionInput` — trusted facts and evidence consumed by policy.

A contract proves only the rules encoded in that class. It does not prove an external claim is true.

## 2. Why Pydantic is used

Pydantic provides:

- runtime field validation;
- explicit allowed values;
- rejection of unknown fields;
- text normalization;
- immutable value objects;
- JSON-to-model parsing;
- clear errors at untrusted model boundaries.

Accurate mental model:

> Pydantic enforces declared structural and field-level invariants. It does not establish semantic correctness or safety.

## 3. Shared model configuration

Most current contracts use:

```python
ConfigDict(strict=True, extra="forbid", frozen=True)
```

### `strict=True`

Avoids broad implicit coercion at Python-object boundaries and exposes representation mistakes.

### `extra="forbid"`

Rejects fields not owned by the contract. A model cannot silently add concepts such as `confidence`, `approved`, or `recommended_action`.

### `frozen=True`

Makes validated objects immutable. A state transition requires a new object rather than mutation in place.

This supports traceable state changes:

```text
candidate object
→ validated application object
```

rather than changing a candidate until it “looks trusted.”

## 4. `Literal` defines bounded vocabularies

### Input-risk vocabularies

```python
InputRiskLevel = Literal["none_detected", "suspicious", "high"]
InputRiskRoute = Literal["proceed", "quarantine"]
```

Signal types are also bounded, including:

```text
instruction_override
output_manipulation
role_impersonation
tool_request
secret_request
encoded_or_concealed_instruction
other_instruction_like_content
```

### Semantic extraction vocabulary

```python
PythonSupportChangeType = Literal["dropped", "added"]
```

`Literal` restricts vocabulary. It does not prove the selected value correctly describes the source.

## 5. Input-risk contracts

### `CandidateInputRiskSignal`

One untrusted detector-proposed signal:

```python
signal_type
source_quote
explanation
```

### `CandidateInputRiskAssessment`

One untrusted detector response:

```python
risk_level
signals
unresolved
```

### `PreparedUntrustedText`

Derived inspection state:

```python
inspection_text
inspection_sha256
preprocessing_findings
```

The SHA-256 value identifies the exact normalized inspection view. It supports traceability; it is not proof that the content is safe or authentic.

### `InputRiskAssessment`

Validated application state:

```python
detector_id
risk_level
signals
unresolved
validation_errors
preprocessing_findings
inspection_sha256
route
limitation
```

The route is deterministic application output, not a field chosen directly by the model.

## 6. Extraction contracts changed

`ExtractionResult` now contains:

```python
accepted_facts
unresolved
validation_errors
input_risk_assessment
```

This allows both proceed and quarantine outcomes to retain the risk evidence that controlled the route.

On quarantine:

```python
accepted_facts = ()
unresolved = ("INPUT_RISK_QUARANTINED",)
input_risk_assessment.route = "quarantine"
```

On proceed, the completed risk assessment remains attached alongside semantic extraction results.

## 7. Tuples and the JSON boundary

Collections use tuples:

```python
signals: tuple[CandidateInputRiskSignal, ...] = ()
facts: tuple[CandidatePythonSupportChange, ...] = ()
unresolved: tuple[str, ...] = ()
```

Tuples support immutable value objects and deterministic comparison.

JSON uses arrays, not tuples. The earlier semantic-extractor failure came from:

```text
JSON decode
→ Python lists
→ strict Python tuple contract
→ rejection
```

The repaired model boundaries validate directly from JSON:

```python
CandidateExtractionResult.model_validate_json(content, strict=True)
CandidateInputRiskAssessment.model_validate_json(content, strict=True)
```

Pydantic can interpret the JSON array as the serialized representation of the tuple field while still enforcing the declared JSON/model schema.

## 8. Field validation versus application validation

### Pydantic contract validation

Examples:

- allowed `risk_level` and `signal_type` values;
- required strings cannot be empty;
- unknown fields are forbidden;
- collection members have declared types.

### Deterministic risk validation

Examples:

- `none_detected` must not include signals;
- suspicious/high must include signals;
- signal quotes must occur in inspection text;
- unresolved, preprocessing findings, or validation errors force quarantine.

### Deterministic semantic validation

Examples:

- source quote exists uniquely;
- version occurs in quote;
- unsupported contexts are rejected;
- duplicates and contradictions are controlled.

These are separate layers with different responsibilities.

## 9. Two provider protocols

### Risk detector

```python
class InputRiskDetector(Protocol):
    detector_id: str

    def assess(self, text: str) -> CandidateInputRiskAssessment: ...
```

### Semantic extractor

```python
class PythonSupportCandidateExtractor(Protocol):
    extractor_id: str

    def extract(self, text: str) -> CandidateExtractionResult: ...
```

A real LM Studio object or a test fake can satisfy each protocol without inheriting from a shared base class. This is structural subtyping.

## 10. Dependency injection now has two dependencies

The service is constructed as:

```python
PythonSupportExtractionService(extractor, risk_detector)
```

It does not instantiate either model client internally.

Benefits:

- input-risk behavior can be tested without a model;
- semantic extraction can be tested independently;
- quarantine can prove that the extractor was never called;
- detector and extractor model choices can differ;
- orchestration stays independent from one concrete provider.

The abstraction is justified by real replacement/testing needs.

## 11. Service composition

The current service performs:

```text
EvidenceItem
→ prepare_untrusted_text
→ risk_detector.assess
→ validate_input_risk_assessment
→ failed_input_risk_assessment on detector error
→ quarantine OR continue
→ extractor.extract
→ validate_python_support_extraction
→ ExtractionResult including InputRiskAssessment
```

The semantic extractor receives the original observation, while the detector receives the normalized inspection view. That is a deliberate preserved-versus-derived boundary.

## 12. Error as data versus raised error

`InputRiskDetectionError` is raised by the detector boundary when it cannot produce a schema-valid assessment.

The orchestration service catches that specific error and converts it into explicit quarantine evidence using `failed_input_risk_assessment()`.

This means:

```text
detector request/output failure
→ not silently ignored
→ not propagated as successful extraction
→ represented as quarantined application state
```

Other programmer/precondition errors, such as missing evidence text, still raise normally.

## 13. Read the orchestration tests as composition proofs

`tests/test_extraction_service.py` now injects both `_FakeRiskDetector` and `_FakeExtractor`.

It proves:

- ordinary text proceeds and reaches extraction;
- the risk assessment is attached to the result;
- grounded semantic output reaches deterministic policy;
- ungrounded semantic output produces no decision fact;
- suspicious input quarantines before extraction;
- detector failure quarantines before extraction;
- the extractor's `received_text` stays `None` on quarantine.

That final observation proves control flow, not merely the final empty fact list.

## 14. Predict before checking

### Case A — Inconsistent detector output

```python
CandidateInputRiskAssessment(
    risk_level="none_detected",
    signals=(some_signal,),
)
```

<details>
<summary>Check the answer</summary>

The Pydantic contract accepts the structure if the signal fields are valid. `validate_input_risk_assessment()` records `NONE_DETECTED_WITH_SIGNALS` and routes to quarantine.
</details>

### Case B — Detector transport failure

<details>
<summary>Check the answer</summary>

The detector raises `InputRiskDetectionError`. The service converts it into `InputRiskAssessment` with high risk, an unresolved detector-error message, and route `quarantine`. The semantic extractor is not called.
</details>

### Case C — Allowed semantic structure, wrong meaning

```python
CandidatePythonSupportChange(
    change="dropped",
    python_version="3.8",
    source_quote="Python 3.8 support is deprecated.",
)
```

<details>
<summary>Check the answer</summary>

The candidate contract accepts the structure. The post-extraction validator rejects the non-effective support context.
</details>

## 15. Current depth boundary

### Required now

- explain every input-risk and extraction contract;
- explain `strict`, `extra`, `frozen`, `Literal`, and tuple fields;
- explain direct JSON validation;
- explain both protocols and fakes;
- trace the service's proceed/quarantine branches;
- explain why detector errors become explicit quarantine state;
- explain the SHA-256 field accurately.

### Deferred

- advanced Pydantic internals;
- generalized dependency-injection frameworks;
- cryptographic provenance systems;
- broad security-signal ontology;
- reorganizing modules only for aesthetic purity.

## 16. Ownership checkpoint

Answer from the source:

1. Which fields are model-proposed and which route field is deterministically created?
2. Why can `none_detected` still be untrusted?
3. What is the difference between `InputRiskDetectionError` and `InputRiskAssessment.validation_errors`?
4. Why does `ExtractionResult` carry `input_risk_assessment`?
5. What two objects are injected into `PythonSupportExtractionService`?
6. Why does the detector see inspection text while extraction uses preserved source text?
