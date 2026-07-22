# 02 — Contracts, Pydantic, and Orchestration

**Depth target:** implementation understanding of the final claim contracts, Pydantic controls, provenance, and service composition.

**Read with:**

- [`../../src/upgradepilot/extraction.py`](../../src/upgradepilot/extraction.py)
- [`../../src/upgradepilot/decision.py`](../../src/upgradepilot/decision.py)
- [`../../tests/test_extraction_validation.py`](../../tests/test_extraction_validation.py)
- [`../../tests/test_extraction_service.py`](../../tests/test_extraction_service.py)
- [`../../tests/test_decision.py`](../../tests/test_decision.py)

## 1. Why the contracts were renamed

The original code used names such as:

```text
CandidatePythonSupportChange
ExtractedPythonSupportChange
PythonSupportChange
```

The final code uses:

```text
CandidatePythonSupportClaim
GroundedPythonSupportClaim
AttributedPythonSupportClaim
```

This is not cosmetic. “Fact” or “trusted change” suggested independent truth. “Claim” accurately represents a statement attributed to an external source and transformation.

## 2. Candidate contract

```python
class CandidatePythonSupportClaim(BaseModel):
    change: Literal["dropped", "added"]
    python_version: str
    source_quote: str
```

The candidate contains only the model’s proposed interpretation and quotation.

It cannot contain:

- evidence state;
- authority level;
- policy version;
- recommendation;
- action or tool request;
- transformation identity chosen by the model.

The JSON Schema and Pydantic contract reject unknown fields.

## 3. Grounded claim contract

```python
class GroundedPythonSupportClaim(BaseModel):
    change: PythonSupportClaimType
    python_version: str
    evidence_id: str
    source_quote: str
    extractor_id: str
    authority: Literal["model_derived"]
```

This object is created by application code after mechanical grounding.

Two fields are especially important:

### `extractor_id`

Identifies the transformation that produced the candidate. For LM Studio it includes model, structured-output mode, and seed.

### `authority`

Currently only `model_derived` is activated. The model does not submit this value; the validator assigns it.

## 4. Decision claim contract

`GroundedPythonSupportClaim.to_decision_claim()` creates:

```python
AttributedPythonSupportClaim(
    change=...,
    python_version=...,
    evidence_ids=(evidence_id,),
    authority="model_derived",
    transformation_id=extractor_id,
)
```

This conversion deliberately preserves authority and transformation identity.

A boundary conversion that dropped those fields would erase the distinction between:

```text
model-derived interpretation
independently corroborated evidence
```

## 5. Pydantic configuration

The central models use:

```python
ConfigDict(strict=True, extra="forbid", frozen=True)
```

### `strict=True`

Material values are not silently coerced across incompatible runtime types.

### `extra="forbid"`

Unknown fields are rejected. This prevents model JSON from smuggling fields such as `authority`, `outcome`, or `approved` into trusted contracts.

### `frozen=True`

Created objects are immutable. This reduces accidental mutation after validation and makes state transitions easier to reason about.

## 6. Literals as finite authority boundaries

```python
ClaimAuthorityLevel = Literal["model_derived"]
DecisionOutcome = Literal["run_targeted_checks", "abstain"]
```

`Literal` restricts accepted values to an explicit finite set.

A test proves that:

```python
authority="trusted"
```

is rejected because that authority level is not activated.

This is stronger than accepting arbitrary strings and relying on comments.

## 7. Evidence-reference validation

`DecisionInput` verifies that every claim references:

- an evidence ID present in the same `EvidenceSet`;
- evidence whose state is `accepted`.

Therefore a claim cannot point to:

- an unknown source;
- missing evidence;
- a source outside the current decision input.

This is provenance validation, not truth validation.

## 8. Protocol and dependency injection

```python
class PythonSupportCandidateExtractor(Protocol):
    extractor_id: str
    def extract(self, text: str) -> CandidateExtractionResult: ...
```

The service depends on a small structural contract rather than a concrete LM Studio class.

Practical benefits:

- tests inject `_FakeExtractor`;
- orchestration tests remain deterministic;
- experimental model transport can be replaced without changing service logic;
- the application boundary is smaller than the provider implementation.

## 9. Current orchestration

```python
PythonSupportExtractionService(extractor).extract(evidence)
```

Execution order:

1. require source observation;
2. call the extractor;
3. receive untrusted `CandidateExtractionResult`;
4. call mechanical grounding;
5. return `ExtractionResult` containing grounded claims, unresolved items, and validation errors;
6. convert grounded claims to authority-bearing decision claims;
7. apply the deterministic policy.

The service has one injected dependency. The earlier mandatory risk-detector dependency was removed.

## 10. Why contradictory claims are preserved

Given:

```text
Drops Python 3.8 support and adds Python 3.8 support.
```

and two uniquely quoted candidates, the validator preserves both grounded claims.

It does not guess which is correct or silently discard one.

That matches the project rule:

```text
conflicting source claims remain visible
→ later conflict handling or corroboration resolves them
```

## 11. A useful migration failure

When the contract changed from facts to attributed claims, focused tests initially failed because they still called:

```python
to_decision_fact()
```

and expected the previous limitation count.

The corrected method is:

```python
to_decision_claim()
```

The additional decision limitation explicitly states that the claim is model-derived and uncorroborated.

These failures were expected contract-migration signals, not model or runtime failures. The tests were updated only after verifying that the failures matched the intended boundary change.

## 12. Predict before checking

### Case A

A model returns valid JSON with:

```json
{
  "claims": [],
  "unresolved": [],
  "authority": "trusted"
}
```

Prediction: schema/Pydantic rejects the extra field before a trusted claim exists.

### Case B

Application code attempts to create `AttributedPythonSupportClaim` without `transformation_id`.

Prediction: Pydantic rejects the missing required field.

### Case C

A grounded claim references evidence state `missing`.

Prediction: `DecisionInput` rejects the claim/evidence relationship.

## 13. Deferred depth

Not required yet:

- advanced Pydantic internals;
- plugin/provider registries;
- generalized authority lattices;
- persistence schema migration;
- cross-source claim-resolution engines;
- dependency-injection frameworks.

The current small contracts are sufficient for the activated responsibility.

## Ownership check

Locate and explain:

1. where authority is assigned;
2. where transformation identity is preserved;
3. where unknown evidence IDs are rejected;
4. why contradictory claims remain visible;
5. why the service no longer takes a risk detector;
6. why `extra="forbid"` is a security and correctness control rather than formatting preference.
