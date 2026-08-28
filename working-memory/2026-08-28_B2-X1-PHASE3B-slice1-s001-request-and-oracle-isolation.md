# B2/X1 Phase 3B Slice 1 — S001 Request Reconstruction and Oracle Isolation

**Date:** 2026-08-28  
**Status:** IMPLEMENTED — FOCUSED WSL VALIDATION PENDING  
**Owning checkpoint:** `../plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md`  
**Accepted protocol:** `../plans/B2_X1_PHASE3_EVALUATION_PROTOCOL.md` (`b2-x1-phase3a-v2`)

## 1. Bounded responsibility

Implement the first deterministic Phase-3B harness slice without any model/provider call:

```text
accepted protocol + frozen S001/source identities
→ reconstruct the real protected S001 planning state
→ keep evaluator oracle/trace metadata outside planner authority
→ render only admitted planner-facing state/schema
```

This slice deliberately does **not** implement replay, all protected cases, grading, manifests,
LM Studio transport, prompt calibration, model scoring, or product integration.

## 2. Pre-change model

The correct owner is `experiments/`, next to the Phase-2 planner contract. Product `src/` remains
unchanged because this machinery exists only to administer the accepted evaluation.

Expected proof:

- accepted S001/protocol source identities can be checked from exact file bytes;
- S001 reconstructs the accepted multi-proposition state in exact order;
- A1 remains pre-bound to `pydantic/pydantic`, the exact PR head, and `pyproject.toml`;
- evaluator-only case/oracle/baseline metadata cannot affect planner-facing request bytes;
- no model/provider is required for the proof.

## 3. Pre-implementation source check

Before implementation, current GitHub source identities were checked against the accepted
protocol and matched for the first S001 subset, including:

```text
src/upgradepilot/impact/python_support.py
→ c6f5e04ee1c8e0b1272e1c81509223a417b64a3b

product-simulation/.../S001.../CASE_IDENTITY.json
→ a124240ff7387c42bb266c384da4c4788f4457e5

product-simulation/.../S001.../FINDINGS.json
→ b12f0a5542f028a3eaf2716efff3ffe0699efb45

working-memory/2026-08-05_B2-step-7f-normal-path-live-s001-proof.md
→ b114e729872b5afd7d2666cdecdca8b6bdd6321f

tools/verification/2026-08-25_r6_s001_real_ci_reachability.py
→ 800a0decae5c09a0dfa7a63eb978ed5dd9b48c1a

tests/test_r6_project_environment_workflow_integration.py
→ 8dad66af993a7d5bb0be50a39145da32a65913b4

tests/test_python_support_impact.py
→ 30fd26eb07aee138873217caa4139742a6fb621a

product-simulation/AGENTS.md
→ a26ff184c4be155e27869924c0b648dc21b6ed2f
```

The accepted protocol blob remains:

```text
82cd30a4d42c3f941b0db5a3d7f29dd06b7e2610
```

## 4. Important implementation finding — `case_key` is not safe planner input

The accepted protocol requires protected/development/oracle metadata to stay out of planner
input. During source preflight, the current internal trace keys were noticed to be human-readable:

```text
p-s001-action
p-s005-defer
p-s008-stop
...
```

Therefore treating `InvestigationSnapshot.case_key` as model-facing data would leak the expected
disposition even though the field was originally described as an opaque trace identity.

The implementation resolves this at the narrowest correct boundary:

```text
InvestigationSnapshot.case_key
→ retained internally for evaluator traceability
→ deliberately omitted by the Phase-3B planner-request projection
```

No Phase-2 contract mutation is needed. The stronger accepted rule is preserved: evaluator
labels/oracles must not reach planner input.

## 5. Implemented files

### `experiments/b2_x1_phase3b_harness.py`

Adds the first deterministic harness responsibilities:

```text
S001_REQUIRED_GIT_BLOBS
→ accepted protocol + exact S001 source/evidence identities

validate_s001_required_source_identities(...)
→ computes Git SHA-1 blob identity from local bytes
→ returns explicit missing/mismatch problems

build_s001_protected_case()
→ real pydantic/pydantic #13432 exact-head identity
→ five ordered propositions
→ one pre-bound A1 action
→ evaluator-only oracle

render_planner_request(...)
→ generic task instruction
→ exact frozen planning question
→ planner-facing snapshot projection
→ strict output schema
→ no case key / partition / oracle / baseline / grader fields

render_planner_request_json(...)
→ stable canonical JSON for later hashing/replay
```

### `experiments/tests/test_b2_x1_phase3b_harness.py`

Adds focused tests for:

1. accepted S001 source identity subset matching the real checkout;
2. missing frozen sources failing closed;
3. exact S001 proposition order/state reconstruction;
4. exact pre-bound A1 locator/result semantics;
5. admitted top-level request shape;
6. oracle/internal-case-key independence;
7. proposition/action rendering order and exact identity;
8. output schema copy isolation;
9. deterministic/parseable JSON rendering.

The strongest leakage test deliberately changes the hidden oracle and internal trace keys and
requires the rendered planner request to remain byte-for-byte identical.

## 6. Repository impact

Pre-slice main:

```text
15d01a746a57cf314be0604c1ce271acfd1e8da0
```

Implementation commits:

```text
f9690273119133746e862b5a18a9bab855ffda6e
→ add experiments/b2_x1_phase3b_harness.py

a626afb47ccb67d1b903a42deaab10fd7dfc8f70
→ add experiments/tests/test_b2_x1_phase3b_harness.py
```

GitHub range inspection confirms exactly two added files:

```text
experiments/b2_x1_phase3b_harness.py
experiments/tests/test_b2_x1_phase3b_harness.py
```

No `src/`, product tests, accepted protocol, Phase-2 contract, provider, or model integration was
changed by this implementation slice.

## 7. Validation state

Runtime validation is **not yet claimed**.

The required focused WSL gate is:

```bash
cd ~/projects/UpgradePilot
git pull --ff-only origin main

.venv/bin/python -m unittest -v \
  experiments.tests.test_b2_x1_phase3b_harness \
  experiments.tests.test_b2_x1_planner_contract

.venv/bin/python -m compileall -q \
  experiments/b2_x1_phase3b_harness.py \
  experiments/b2_x1_planner_contract.py \
  experiments/tests/test_b2_x1_phase3b_harness.py \
  experiments/tests/test_b2_x1_planner_contract.py
```

Expected current count is **32 focused tests** if the original Phase-2 suite remains 23 and the
new slice contributes 9. The exact observed count, not this expectation, controls the record.

## 8. Proof boundary

A passing focused gate would establish only:

```text
accepted S001 frozen inputs are still byte-identical
+ real S001 request reconstruction behaves as designed
+ evaluator-only oracle/trace data does not influence the rendered request
+ Phase-2 admission tests remain green
+ touched modules compile
```

It would **not** establish:

- planner/model quality;
- LM Studio availability;
- prompt quality;
- all protected-case reconstruction;
- replay/grader correctness beyond S001 request construction;
- general agent value;
- product adoption or integration.

## 9. Next continuation after focused PASS

Only after the focused WSL gate passes:

```text
mark Slice 1 COMPLETE
→ promote exact evidence to MEMORY.md
→ continue Phase 3B with the next smallest deterministic slice
```

The next likely slice is to extend the accepted case reconstruction beyond S001 and introduce
the first no-tool real cases while preserving the same renderer/oracle-isolation boundary.
Model scoring remains blocked until the complete Phase-3B deterministic harness gate passes.
