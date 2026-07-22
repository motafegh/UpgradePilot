# M2-S03 Learning Orientation — Evidence-to-Report Vertical Slice

**Status:** Current learning entry point for M2-S03.

**Purpose:** Explain the current responsibility, identify which foundations are already implemented, and prevent planned report behavior from being mistaken for existing code.

**Controlling plan:** [`../../plans/M2_S03_EVIDENCE_REPORT_VERTICAL_SLICE_PLAN.md`](../../plans/M2_S03_EVIDENCE_REPORT_VERTICAL_SLICE_PLAN.md)

## 1. Required outcome

Given one bounded real PR input and supplied or replayed evidence, UpgradePilot must produce:

- one reproducible machine-readable report;
- one useful human-readable report;
- one deterministic decision or explicit abstention;
- visible evidence provenance, limitations, and degraded states.

Conceptual path:

```text
raw case input + supplied/replayed evidence
→ strict case and evidence contracts
→ preserved observations and attributed claims
→ deterministic decision policy
→ machine report + human report
```

M2-S03 completes the first evidence-to-report vertical slice. It is not another extraction-only experiment and does not require an adopted LLM.

## 2. What is already implemented

Current foundations include:

- strict `InitialCaseRecord` construction and snapshot identity;
- strict `EvidenceItem` and `EvidenceSet` contracts;
- missing-versus-accepted evidence states;
- attributed model-derived claim contracts and mechanical grounding;
- deterministic decision outcomes limited to `run_targeted_checks` or `abstain`;
- traceable reasons, evidence IDs, targeted checks, limitations, and policy version;
- machine-readable Pydantic serialization of current decision objects;
- negative model and detector experiment artifacts.

These are starting components, not the complete report slice.

## 3. What is planned but not yet established

Do not claim these as implemented until source and tests exist:

- one application-level input/result contract composing the full slice;
- one normal orchestration entry point from raw case/evidence input;
- a versioned machine-report representation;
- a human report renderer;
- report-level provenance for every material statement;
- stable relationship between application, serialized, and human representations;
- a runnable no-model command producing both reports;
- a recorded real-PR output artifact;
- changed-evidence and degraded-evidence report proofs;
- the final M2 pass assessment.

## 4. Why M2-S03 does not need an LLM

M2-S02 rejected both tested local deployments for normal extraction.

The plan therefore permits the slice to preserve:

```text
release-note observation
+ unresolved interpretation
+ explicit limitation
```

rather than fabricate an automated semantic answer.

A caller-supplied claim may be used only when honestly represented by its real source/authority. It must not be disguised as model extraction.

The supported clean run must succeed with LM Studio unavailable.

## 5. Core concepts to learn as implementation lands

### Application composition

How one application result combines:

- case identity;
- evidence;
- attributed claims where available;
- decision result;
- report provenance;
- limitations and degraded states.

### Representation separation

The project explicitly distinguishes:

```text
application object
serialized machine report
human-readable rendering
```

They may contain related information but should not be treated as the same representation.

### Deterministic serialization

Machine output must be reproducible, version-aware before compatibility matters, and free of hidden Python-only values.

### Human rendering

The renderer should explain the evidence and decision without adding unsupported conclusions such as `safe`, `compatible`, or `ready to merge`.

### Report provenance

Every material report statement must trace to:

- case/evidence contracts;
- attributed claim provenance;
- deterministic policy output;
- or an explicit limitation.

### Degraded evidence

Missing, unresolved, invalid, rejected, unsupported, and not-applicable states must remain distinguishable where activated.

### No-model operation

The normal M2-S03 path must reproduce without credentials, live network acquisition, or a loaded model.

## 6. Important boundaries carried forward

- Accepted evidence does not establish source truth.
- Grounded extraction is attribution, not corroboration.
- Model output cannot assign authority or decision effect.
- Favorable or absent model claims cannot justify reduced caution.
- The deterministic decision module remains the only current decision authority.
- Human-readable text must not invent stronger conclusions than the machine/application result.
- Report output must not silently erase missing or unresolved evidence.

## 7. Proofs the implementation must eventually demonstrate

| Proof | Required observation |
|---|---|
| Real selected PR | Both reports identify the same case revision and evidence |
| Missing repository support | Limitation remains visible and decision follows current policy |
| Changed evidence | Output changes deterministically for a traceable reason |
| Invalid caller input | Fails as input invalidity, not as unavailable external evidence |
| Serialization | Stable schema/version marker and JSON-safe values |
| No-model run | Supported path succeeds with LM Studio unavailable |
| Security boundary | Source text cannot add fields, authority, tools, or actions |
| Regression | Tests, compilation, imports, and diff checks pass |

## 8. Learning workflow for M2-S03

As each source increment is implemented:

```text
read the current plan boundary
→ inspect the new source contract
→ predict one normal and one degraded result
→ inspect focused tests
→ run the narrow test
→ trace one field into both report forms
→ record what is implemented versus still planned
→ add or revise one focused learning note only when durable understanding exists
```

Do not pre-write a large report-framework course before the source exists.

## 9. Recommended study order now

Before implementing or reviewing M2-S03, be able to explain:

1. `InitialCaseRecord` and snapshot identity;
2. `EvidenceItem` accepted versus missing states;
3. `AttributedPythonSupportClaim` authority/provenance;
4. `DecisionInput` evidence-reference checks;
5. `DecisionResult` reasons, limitations, and policy version;
6. why application, JSON, and human text are different representations;
7. why unresolved interpretation is preferable to disguised manual meaning.

Use the closed [`../m2-s02/`](../m2-s02/) package for claim, grounding, authority, model-failure, and design-reversal learning.

## 10. Current ownership checkpoint

Before the first report implementation increment, Ali should be able to answer:

1. Which parts of the future report already exist as trusted contracts?
2. Which report behaviors are still only plan requirements?
3. How can the slice run without a model?
4. Why must both report forms derive from the same application result?
5. What is the difference between invalid input and missing evidence?
6. Why can a human renderer not describe an update as safe merely because the policy abstained?
7. Which current object remains the only decision authority?
