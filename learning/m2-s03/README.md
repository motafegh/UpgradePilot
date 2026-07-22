# M2-S03 Learning Orientation — Evidence-to-Report Vertical Slice

**Status:** Paused implementation orientation retained for later comparison.  
**Current learning entry point:** [`../product-simulation/`](../product-simulation/)  
**Purpose:** Preserve the intended M2-S03 implementation responsibility, existing foundations, and implementation boundaries without implying that this plan controls current work.  
**Paused plan:** [`../../plans/M2_S03_EVIDENCE_REPORT_VERTICAL_SLICE_PLAN.md`](../../plans/M2_S03_EVIDENCE_REPORT_VERTICAL_SLICE_PLAN.md)

> Manual product simulation currently controls project work. Do not resume M2-S03 implementation or use this file as the active study path until product-simulation evidence and synthesis produce an explicitly approved corrected implementation responsibility.

## 1. Intended implementation outcome

The paused plan intended one bounded real PR input and supplied or replayed evidence to produce:

- one reproducible machine-readable report;
- one useful human-readable report;
- one deterministic decision or explicit abstention;
- visible evidence provenance, limitations, and degraded states.

Planned conceptual path:

```text
raw case input + supplied/replayed evidence
→ strict case and evidence contracts
→ preserved observations and attributed claims
→ deterministic decision policy
→ machine report + human report
```

This remains useful historical implementation orientation. It is not the current complete product-runtime model.

## 2. Why implementation was paused

The project discovered that a report slice could be locally coherent while still lacking an evidence-derived model of:

- runtime invocation;
- discovered and frozen identity;
- live evidence acquisition;
- operation and failure history;
- raw preservation;
- transformations and findings;
- complete decision behavior;
- machine and human report responsibilities;
- follow-up, rerun, replay, and supersession;
- factual review, owner review, external confirmation, and capability evidence.

`product-simulation/` now performs those responsibilities manually on real cases before implementation continues.

## 3. Foundations that existed before the pause

Current implementation foundations include:

- strict `InitialCaseRecord` construction and snapshot identity;
- strict `EvidenceItem` and `EvidenceSet` contracts;
- missing-versus-accepted evidence states;
- attributed model-derived claim contracts and mechanical grounding;
- deterministic decision outcomes limited to `run_targeted_checks` or `abstain`;
- traceable reasons, evidence IDs, targeted checks, limitations, and policy version;
- machine-readable Pydantic serialization of current decision objects;
- negative model and detector experiment artifacts.

These remain real source/test evidence. They do not define the complete manual simulation artifact family.

## 4. Planned behavior not established as implementation

Do not claim these as implemented until current source and tests establish them:

- one application-level input/result contract composing the full slice;
- one normal orchestration entry point from raw case/evidence input;
- a versioned complete machine-report representation;
- a human report renderer;
- report-level provenance for every material statement;
- stable relationship between application, serialized, and human representations;
- a runnable no-model command producing both reports;
- a recorded real-PR output artifact;
- changed-evidence and degraded-evidence report proofs;
- the final M2 pass assessment;
- the broader acquisition, operation, artifact, follow-up, and review behavior now being discovered in product simulation.

## 5. Why an adopted LLM was not required

M2-S02 rejected both tested local deployments for normal semantic extraction.

The paused plan therefore allowed:

```text
release-note observation
+ unresolved interpretation
+ explicit limitation
```

rather than a fabricated automated semantic answer.

A caller-supplied claim could be used only under its actual source and authority. It could not be disguised as model extraction.

The intended supported clean run had to succeed with LM Studio unavailable.

## 6. Concepts retained for later implementation review

### Application composition

How one application result combines case identity, evidence, attributed claims, decision, provenance, limitations, and degraded states.

### Representation separation

```text
application object
≠ serialized machine report
≠ human-readable rendering
```

### Deterministic serialization

Machine output should be reproducible, version-aware, and free of hidden Python-only values.

### Human rendering

A renderer must not add unsupported conclusions such as `safe`, `compatible`, or `ready to merge`.

### Report provenance

Every material report statement must trace to trusted input/evidence, attributed claim provenance, deterministic policy output, or an explicit limitation.

### Degraded evidence

Missing, unresolved, invalid, rejected, unsupported, and not-applicable states must remain distinguishable where activated.

### No-model operation

The planned normal path must not depend on credentials, live acquisition, or a loaded model.

## 7. Boundaries carried forward

- Accepted evidence does not establish source truth.
- Grounded extraction is attribution, not corroboration.
- Model output cannot assign authority or decision effect.
- Favorable or absent model claims cannot justify reduced caution.
- The current deterministic decision module remains the only implemented decision authority.
- Human-readable text must not invent stronger conclusions than the application result.
- Report output must not silently erase missing or unresolved evidence.
- Conceptual product-simulation responsibilities are not implemented merely because they now have manual artifacts.

## 8. Original proof expectations

| Proof | Required observation |
|---|---|
| Real selected PR | Both reports identify the same case revision and evidence |
| Missing repository support | Limitation remains visible and decision follows current policy |
| Changed evidence | Output changes deterministically for a traceable reason |
| Invalid caller input | Fails as input invalidity, not unavailable external evidence |
| Serialization | Stable schema/version marker and JSON-safe values |
| No-model run | Supported path succeeds with LM Studio unavailable |
| Security boundary | Source text cannot add fields, authority, tools, or actions |
| Regression | Tests, compilation, imports, and diff checks pass |

These proofs remain useful candidates. Product-simulation evidence may revise their scope or add missing responsibilities before implementation resumes.

## 9. How to use this package now

Use this file only when comparing:

- current implemented foundations;
- the old planned report slice;
- responsibilities discovered by product simulation;
- eventual corrected implementation scope.

For current learning, start with [`../product-simulation/README.md`](../product-simulation/README.md).

Do not perform the old M2-S03 ownership checkpoint as though implementation is about to begin. Replace it with the current product-simulation ownership workbook until implementation is explicitly resumed.

## 10. Resume condition

This package becomes active again only after:

1. sufficient prospective and contrasting product-simulation cases exist;
2. cross-case synthesis identifies the smallest corrected implementation responsibility;
3. conflicts with current plans/specifications are resolved explicitly;
4. Ali approves implementation resumption;
5. this learning orientation is updated against the accepted responsibility and actual source state.

Until then, its depth is historical orientation, not current execution guidance.
