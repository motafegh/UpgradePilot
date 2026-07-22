# 02 — Contracts, Pydantic, and Orchestration

**Depth target:** implementation understanding of the data contracts and composition mechanisms used in M2-S02.

**Read with:**

- [`../../src/upgradepilot/extraction.py`](../../src/upgradepilot/extraction.py)
- [`../../src/upgradepilot/evidence.py`](../../src/upgradepilot/evidence.py)
- [`../../src/upgradepilot/decision.py`](../../src/upgradepilot/decision.py)
- [`../../tests/test_extraction_service.py`](../../tests/test_extraction_service.py)

## 1. What a contract means here

A contract defines which data is allowed to cross a boundary and which invariants must already hold.

Examples:

- `EvidenceItem` defines normalized evidence input;
- `CandidateExtractionResult` defines untrusted extractor output;
- `ExtractionResult` defines the validator result;
- `DecisionInput` defines what the policy can consume.

A contract does not prove the external world is true. It proves that the in-memory object satisfies the declared application rules.

## 2. Why Pydantic is used

Pydantic converts external or constructed data into validated Python objects.

In this repository it provides:

- runtime field validation;
- clear allowed values;
- rejection of unknown fields;
- normalization of required text;
- immutable value objects;
- JSON parsing at the model boundary;
- useful validation errors for malformed model output.

The important idea is not “Pydantic is safe.” The useful statement is:

> Pydantic enforces the structural and field-level invariants that the project explicitly encoded.

It does not understand whether a release-note sentence truly means `added` or `dropped`.

## 3. `ConfigDict(strict=True, extra="forbid", frozen=True)`

The extraction models use:

```python
model_config = ConfigDict(strict=True, extra="forbid", frozen=True)
```

### `strict=True`

Pydantic should not freely coerce incompatible Python values into the requested type.

Practical intent:

- avoid silently converting surprising inputs;
- expose representation mistakes early;
- keep the boundary predictable.

Strictness applies to the encoded contract, not semantic truth.

### `extra="forbid"`

Unknown fields are rejected.

For example, this model output should not be accepted silently:

```json
{
  "change": "dropped",
  "python_version": "3.8",
  "source_quote": "Python 3.8 support was dropped.",
  "confidence": 0.99
}
```

`confidence` is not part of the current contract. Rejecting it prevents an extractor from quietly expanding the application protocol.

### `frozen=True`

Validated models are immutable.

Instead of changing a fact in place, code must construct another object. This helps preserve provenance and makes state transitions more visible.

## 4. `Literal` narrows allowed vocabulary

```python
PythonSupportChangeType = Literal["dropped", "added"]
```

`Literal` means only the listed exact values are valid for that field.

This rejects values such as:

```text
removed-later
maybe-dropped
deprecated
supported
```

The name makes sense: the value must literally be one of the declared options.

This does not prove that the chosen direction is correct. A model may still select the allowed value `dropped` for a sentence that only describes deprecation.

## 5. Why tuples are used

The contracts use tuples for collections:

```python
facts: tuple[CandidatePythonSupportChange, ...] = ()
unresolved: tuple[str, ...] = ()
```

The `...` means any number of elements of the declared type.

Tuples support the value-object style:

- they are immutable;
- they make accidental append/mutation less likely;
- they fit `frozen=True` models;
- they make outputs easier to compare in deterministic tests.

### The JSON-array/tuple boundary failure

JSON has arrays, not Python tuples. A model response contains JSON arrays:

```json
{"facts": [], "unresolved": []}
```

The earlier failure path decoded JSON into ordinary Python lists and then asked strict Pydantic models to accept those lists as tuples. Strict validation rejected the representation.

The repaired path uses:

```python
CandidateExtractionResult.model_validate_json(content, strict=True)
```

This validates directly from JSON. Pydantic understands that a JSON array is the serialized representation of the tuple field while still applying strict validation to the JSON boundary.

Mental model:

```text
JSON array
→ direct JSON-aware validation
→ Python tuple contract
```

Do not generalize this into “strict mode converts everything.” This is specifically the JSON representation boundary.

## 6. Field validators

The helper:

```python
def _normalize_required_text(value: str, field_name: str) -> str:
    normalized = value.strip()
    if not normalized:
        raise ValueError(f"{field_name} must not be empty")
    return normalized
```

is applied through `@field_validator`.

It performs two tasks:

1. trims surrounding whitespace;
2. rejects empty text after trimming.

This prevents values such as:

```python
python_version="   "
source_quote=""
extractor_id="  "
```

The validator is reusable across fields, while `ValidationInfo.field_name` allows an accurate error message.

## 7. Field validation versus semantic validation

Keep two layers separate.

### Pydantic field/contract validation

Examples:

- `change` must be `added` or `dropped`;
- required strings cannot be empty;
- unknown fields are forbidden;
- collections have declared element types.

### Extraction semantic validation

Examples:

- the source quote must occur in the evidence text;
- the Python version must occur in the quote;
- instruction-like source context must be rejected;
- deprecation must not become a dropped-support fact.

Pydantic owns structure. `validate_python_support_extraction()` owns the current deterministic semantic admission rules.

## 8. `Protocol` and structural subtyping

The orchestration service depends on:

```python
class PythonSupportCandidateExtractor(Protocol):
    extractor_id: str

    def extract(self, text: str) -> CandidateExtractionResult: ...
```

A `Protocol` describes required behavior and attributes. An object can satisfy it without inheriting from a shared base class.

The real LM Studio extractor satisfies the protocol because it has:

- `extractor_id`;
- `extract(text)` returning `CandidateExtractionResult`.

The test `_FakeExtractor` also satisfies it.

This is **structural subtyping**: compatibility depends on the object's shape and behavior, not its inheritance family.

## 9. Dependency injection

`PythonSupportExtractionService` receives its extractor:

```python
service = PythonSupportExtractionService(extractor)
```

This is dependency injection: the service's dependency is supplied from outside rather than created inside the service.

Why it is useful here:

- unit/integration tests can inject `_FakeExtractor`;
- orchestration can be tested without running LM Studio;
- the service does not depend on a specific model name;
- transport changes do not require policy changes;
- the boundary stays small and reversible.

This abstraction is justified by an actual replacement need, not hypothetical architecture.

## 10. Why there is a local import

Inside `PythonSupportExtractionService.extract()`:

```python
from upgradepilot.extraction_validation import validate_python_support_extraction
```

The import occurs inside the method to avoid a module cycle.

The dependency relationship is:

```text
extraction.py defines contracts
extraction_validation.py imports those contracts
extraction.py service needs to call extraction_validation.py
```

If both modules imported each other at module-load time, Python could encounter a partially initialized module. The local import delays loading the validator until the method runs, after `extraction.py` has defined its classes.

This is a practical cycle repair, not a claim that local imports are always preferable.

## 11. Read the orchestration test as a composition proof

`tests/test_extraction_service.py` injects `_FakeExtractor` and proves:

1. the release-note observation is passed to the extractor;
2. the candidate is validated;
3. the accepted fact contains `extractor_id`;
4. accepted facts convert into decision facts;
5. the deterministic policy returns `run_targeted_checks` for the demonstrated evidence combination;
6. an ungrounded candidate produces no decision fact.

The fake extractor removes live-model variability so the test can focus on service composition.

## 12. Predict before checking

Consider:

```python
CandidatePythonSupportChange(
    change="removed-later",
    python_version="3.8",
    source_quote="Python 3.8 may be removed later.",
)
```

Which layer rejects it first?

<details>
<summary>Check the answer</summary>

The Pydantic candidate contract rejects it because `change` is restricted by `Literal["dropped", "added"]`. The deterministic extraction validator never receives a successfully constructed candidate object.
</details>

Now consider:

```python
CandidatePythonSupportChange(
    change="dropped",
    python_version="3.8",
    source_quote="Python 3.8 may be removed later.",
)
```

<details>
<summary>Check the answer</summary>

The candidate contract accepts the structure. The semantic validator rejects it as `NON_EFFECTIVE_SUPPORT_CONTEXT` because future removal is not an effective support drop.
</details>

## 13. Current depth boundary

### Required now

- explain every extraction contract;
- explain `strict`, `extra`, and `frozen` practically;
- explain `Literal`, tuple fields, and field validators;
- explain why the fake extractor satisfies the protocol;
- explain the JSON-array/strict-tuple repair;
- trace the orchestration service.

### Deferred

- advanced Pydantic internals and schema generation;
- Python typing theory beyond the current protocol;
- generalized dependency-injection frameworks;
- reorganizing modules solely to remove the local import.

## 14. Ownership checkpoint

Answer from the source:

1. Which candidate values can `change` contain?
2. What happens if the model adds an unknown JSON field?
3. Why can a valid Pydantic candidate still be semantically unsafe?
4. Why does the service accept a protocol rather than construct LM Studio directly?
5. Why did direct JSON validation repair the list/tuple failure?
6. What exact output does `ExtractionResult.to_decision_facts()` ignore?
