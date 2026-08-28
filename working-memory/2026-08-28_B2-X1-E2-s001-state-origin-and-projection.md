# B2/X1 E2 — S001 State Origin and Planner Projection

**Date:** 2026-08-28  
**Status:** E2.1 COMPLETE  
**Parent exploration:** `working-memory/2026-08-28_B2-X1-evidence-first-llm-risk-and-design-exploration.md`

## Purpose

Trace the real pre-X1 product state at the S001 Python-support investigation decision and distinguish:

```text
raw-text carryover
from
semantic carryover
```

before deciding which prompt-injection controls a future planner actually needs.

The experiment uses the normal product entry point for real S001:

```text
pydantic/pydantic#13432
→ investigate_public_pull_request(...)
→ python_support_drop_pre_investigation_result
→ python_support_drop_investigation_selection
```

It compares:

1. a small proposition/selection projection; and
2. the nested `PythonSupportDropImpactAssessment` / candidate graph.

Experiment source:

`experiments/b2_x1_e2_s001_state_origin_probe.py`

## Environment observations encountered before E2 execution

The first run failed with HTTP 401 because an ambient `GITHUB_TOKEN` was supplied to public GitHub REST acquisition.

After removing that token, the next run progressed further but timed out while `urllib3` was preparing an ambient proxy for `api.github.com`.

A direct control succeeded:

```text
curl --noproxy '*' https://api.github.com/repos/pydantic/pydantic/pulls/13432
→ HTTP 200
```

The successful E2 run therefore used process-local environment isolation:

```text
unset/omit GITHUB_TOKEN
+ omit HTTP_PROXY / HTTPS_PROXY / ALL_PROXY
+ omit lowercase equivalents
```

This is environment/transport evidence, not an E2 semantic finding. The reusable execution rule is recorded in `ENVIRONMENT.md`; do not duplicate the incident detail there.

## E2.1 live result

User-executed normal S001 product flow produced:

```text
case: pydantic/pydantic#13432
proposition_projection_contains_raw_external_text: False
nested_assessment_contains_raw_external_text: True
semantic_carryover_without_raw_text: True
naive_whole_object_serialization_would_cross_raw_text_boundary: True
```

Exact PR head observed:

```text
aa2dc024d33f61cdef50bf1973ab5adf0a974f5a
```

### Nested raw external text

The real nested pre-investigation assessment contains:

```text
python_support_drop_pre_investigation_result
→ candidate
→ upstream_claim
→ source_evidence[]
→ source_quote
```

Observed exact source quote:

```text
-   **NEW**: Drop support for Python 3.8.
```

Therefore a naive whole-object serialization would expose real externally controlled upstream prose to a future planner.

## Proposition-only projection

The small projection contained three propositions and no raw external changelog text.

### 1. Upstream support drop

```text
key: upstream_python_support_drop_crossed
state: established
evidence_coverage: sufficient
evidence_owner: upstream.claim
origin: model_derived_semantics_deterministically_grounded
raw_external_text: false
```

Detail:

```text
Authoritative upstream evidence grounds a Python 3.8 support drop inside the exact dependency release interval.
```

This is **semantic carryover**: the proposition is typed/project-authored text, but its established truth depends on the earlier support-drop semantic extractor plus deterministic grounding.

### 2. Exact target declaration

```text
key: exact_target_python_declaration_established
state: unresolved
evidence_coverage: insufficient
evidence_owner: target.python
origin: deterministic_pre_acquisition_state
raw_external_text: false
```

### 3. Range intersection

```text
key: declared_python_range_intersects_dropped_line
state: unresolved
evidence_coverage: insufficient
evidence_owner: target.relevance
origin: deterministic_derived_state
raw_external_text: false
```

## Deterministic selected investigation

The existing product selector produced:

```text
kind: acquire_exact_target_python_declaration
repository: pydantic/pydantic
revision: aa2dc024d33f61cdef50bf1973ab5adf0a974f5a
path: pyproject.toml
proposition_key: exact_target_python_declaration_established
origin: deterministic_selector_output
raw_external_text: false
```

This remains the deterministic baseline/control, not a planner requirement.

## Finding E2-F1 — raw planner prompt-injection exposure is not inevitable

Observed evidence:

```text
whole nested product object
→ contains raw upstream changelog quote

small proposition/selection projection
→ contains no raw upstream changelog quote
```

Therefore prompt-injection exposure at the first planner seam depends materially on the chosen projection. A planner does not need raw upstream changelog prose merely because the product retains that evidence internally.

**Engineering implication:** avoid naive whole-object serialization. This conclusion is supported by the real S001 object graph, not generic LLM advice.

## Finding E2-F2 — removing raw text does not remove upstream semantic dependence

The proposition-only projection still contains:

```text
upstream_python_support_drop_crossed = established
```

whose truth was influenced by the already-adopted semantic extractor.

Therefore:

```text
no raw-text carryover
!=
fully deterministic semantic state
```

This is not prompt injection into the planner. It is semantic carryover from an earlier model boundary and remains governed by the E1 finding: current live probes did not expose a failure, while deterministic grounding is not an independent English-semantic backstop.

## Finding E2-F3 — context projection can be a simpler control than prompt hardening

For the first candidate-specific planner seam, a deliberately small typed projection can remove the currently observed raw upstream instruction surface before the planner call.

That does not yet prove the final planner schema or that no explanatory text should ever be included. It does show that a large prompt-injection defense framework is not required merely because raw changelog prose exists somewhere inside the product object graph.

## What E2.1 does not prove

E2.1 does not establish that:

- every future planner field is free of external text;
- all `detail` fields are always project-authored;
- no later mechanism will need raw or near-raw evidence;
- proposition-only state is sufficient for good planner decisions;
- the planner can correctly distinguish actionable from dependent unresolved propositions;
- upstream semantic extraction is universally reliable.

Those remain separate questions.

## Next discriminating step

Proceed to **E3 — minimally constrained planner capability probe** using real/faithfully projected S001 typed state.

The purpose is to observe what the adopted model naturally proposes before imposing the full previous planner restrictions. Keep execution side-effect-free: proposal/record only, no capability execution.

Initial E3 comparison should answer:

```text
real typed S001 state
+ bounded planning question
+ materially fewer planner constraints
→ what next step does the model naturally propose?
→ does it identify pyproject.toml / target Python declaration?
→ does it invent unrelated actions or arguments?
→ does it stop/defer incorrectly?
```

Do not add guardrails before an observed/reachable failure requires them.
