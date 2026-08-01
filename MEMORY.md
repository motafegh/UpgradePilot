# UpgradePilot Current Memory

**Last updated:** 2026-08-01  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, selected continuation, and current learning state.

Stable plans, specifications, ADRs, source, tests, and dated working records retain their own responsibilities. They must not mirror or compete with this file for live status.

## Single-live-state rule

`MEMORY.md` is the only repository file allowed to answer what is selected now, what behavior is verified, what remains open, what happens next, and what learning depth is established.

This file is replacement state, not append-only history. Remove superseded live statements when the project advances; Git history and dated evidence preserve history.

## Live position

- **Execution branch:** `main`. No separate implementation branch is selected.
- **Route:** B2 — Public PR vertical slice.
- **Selected parent plan:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)
- **Selected Step 4 plan:** [`plans/B2_STEP_4_TARGET_PYTHON_RELEVANCE_PLAN.md`](plans/B2_STEP_4_TARGET_PYTHON_RELEVANCE_PLAN.md)
- **Completed and behavior-validated:** Steps 1–3.
- **Current responsibility:** Step 4 — deterministic target-Python relevance mapping with manual trusted inputs.
- **Current Step 4 state:** planned, implemented, and covered by controlled tests; **local validation is still required before Step 4 closes**.
- **Step 4 implementation record:** [`working-memory/2026-08-01_B2-step-4-target-python-relevance-implementation.md`](working-memory/2026-08-01_B2-step-4-target-python-relevance-implementation.md)

## Last behavior-validated executable boundary

The most recent locally observed complete executable validation remains:

```text
baacd71e4be93b9d0633edd1fd311f5c45c627d5
```

Observed locally on `main`:

```text
python -m unittest \
  tests.test_upstream_claim \
  tests.test_upstream_claim_edges \
  -v

Ran 24 tests in 0.003s
OK
```

and:

```text
python -m unittest discover -s tests -v

Ran 251 tests in 0.053s
OK
```

That validation closes Steps 1–3, including the 2026-08-01 Step 2 Python-line quote-token regression fix.

## Step 4 product/test boundary awaiting validation

The current Step 4 source/test revision is:

```text
cceb8da55e5908f346141545eacdca4672f7d977
```

Later working-memory and `MEMORY.md` commits do not alter that product/test boundary.

Step 4 adds:

```text
plans/B2_STEP_4_TARGET_PYTHON_RELEVANCE_PLAN.md
src/upgradepilot/target_python_relevance.py
tests/test_target_python_relevance.py
```

and updates:

```text
src/upgradepilot/__init__.py
tests/test_package_interface.py
```

No CLI, acquisition, network, model, or recommendation source was changed.

## Step 4 implemented contract

The selected data flow is:

```text
UpstreamSupportDropClaimResult
├── UpstreamSupportDropClaimProblem
│   + no target evidence admitted
│   → upstream_claim_unresolved
│
└── GroundedPythonSupportDropClaim
    + TargetPythonEvidence
      ├── TargetPythonDeclarationProblem
      │   → target_declaration_unresolved
      │
      └── TargetPythonDeclaration
          → evaluate_python_line_specifier(...)
             ├── stable X.Y.Z witness exists
             │   → declared_python_overlap
             ├── no stable X.Y.Z witness
             │   → outside_declared_python_range
             └── method problem
                 → explicit unresolved/unsupported mapping
```

Public Step 4 names:

```text
TargetPythonRelevanceState
TargetPythonRelevanceResult
evaluate_target_python_relevance
```

### Relevance states

```text
declared_python_overlap
outside_declared_python_range
target_declaration_unresolved
upstream_claim_unresolved
comparison_unsupported
```

These states describe only the relationship between one grounded upstream Python support drop and the target's declared `[project].requires-python` range. They do not mean compatibility, safety, merge readiness, or a maintainer action.

### Activation rule

An unresolved upstream claim stops before target evidence is admitted.

```text
upstream problem + target_evidence=None
→ upstream_claim_unresolved
```

Once a grounded claim exists, one target evidence result is required.

Supplying target evidence beside an unresolved upstream result or omitting target evidence after a grounded claim is caller sequencing misuse, not a product evidence state.

This API prepares the later conditional orchestration step but does not yet change the CLI acquisition order.

### Trust-boundary rule

Step 4 does not re-ground Step 2 source spans and does not re-parse target TOML. It consumes and preserves the exact records produced by those owning boundaries.

No shared cross-source identity exists at this boundary that can be honestly reconciled without introducing new evidence.

### Step 3 method-problem mapping

```text
invalid_python_line
→ upstream_claim_unresolved
```

This is a defensive result for a malformed manually constructed purported trusted claim; normal Step 2 behavior should prevent it.

```text
invalid_requires_python_specifier
unsatisfiable_requires_python_specifier
→ target_declaration_unresolved
```

```text
unsupported_requires_python_specifier
→ comparison_unsupported
```

The distinction is intentional: invalid/contradictory target declarations fail to establish a usable target range, while unsupported means both inputs exist but the deliberately bounded Step 3 method does not admit that valid form.

## Controlled Step 4 tests

The new focused test module covers:

- S001-shaped Python `3.8` drop + target `>=3.10` → `outside_declared_python_range`;
- positive overlap and exact stable witness preservation;
- every target-parser problem state;
- unresolved upstream non-activation;
- invalid activation sequencing;
- unsupported arbitrary equality;
- invalid and unsatisfiable target PEP 440 declarations;
- defensive invalid upstream Python-line handling;
- public argument type checks;
- package-level Step 4 exports.

No pass is claimed yet for these new tests.

## Exact continuation

From the real checkout:

```bash
git pull --ff-only

python -m unittest \
  tests.test_target_python_relevance \
  tests.test_package_interface \
  -v

python -m unittest discover -s tests -v
```

Derived counts at the current product/test revision are:

```text
focused: 17 tests
complete: 263 tests
```

These counts are expectations only. The observed terminal result controls validation truth.

If either command fails:

1. diagnose only inside the Step 4 contract/integration boundary unless evidence proves an older regression;
2. repair minimally;
3. rerun the focused command;
4. rerun the complete suite.

If both commands pass:

1. close Step 4 as behavior-validated in `MEMORY.md`;
2. record the observed command summaries without inventing timings/counts;
3. activate parent-plan Step 5 — authoritative upstream interval acquisition;
4. do not jump directly to model integration, CLI orchestration, or S001 end-to-end execution.

## Stop line

Until Step 4 validates, do not begin:

- Step 5 upstream network acquisition;
- release-index/tagged-changelog acquisition changes;
- model or Instructor integration;
- CLI acquisition-order changes;
- S001 live end-to-end integration;
- compatibility, safety, merge, defer, targeted-check, or recommendation logic.

## Explicitly not established

- a passing Step 4 focused suite;
- a passing complete suite containing Step 4;
- live automated S001 target relevance;
- complete crossed-release network acquisition;
- tagged-changelog acquisition/tag peeling;
- automated semantic extraction/model path;
- conditional target-Python activation in CLI runtime;
- compatibility, safety, recommendation, maintainer action, or production readiness;
- user mastery of Steps 1–4.

## Learning state

Steps 1–3 are behavior-validated at product level. Step 4 concepts are now introduced and implemented but not yet behavior-validated.

Step 4 learning concepts include:

- a **discriminated state mapping**: one bounded state explains why comparison succeeded, could not start, or exceeded the accepted method;
- **early return as an authority boundary**: unresolved upstream evidence prevents target comparison rather than merely saving computation;
- **single-owner validation**: Step 4 preserves trusted Step 2/target-parser records instead of duplicating their checks;
- **nested evidence preservation**: the result keeps owning records instead of copying identity/provenance/witness fields;
- **invalid versus unsupported**: malformed or contradictory evidence differs from valid evidence outside the selected method's scope;
- **pure domain mapping**: no network, model, CLI, or repository mutation is needed to answer the Step 4 question.

Current depth:

```text
structured design explanation available
+ focused Step 4 plan available
+ educational source/docstrings/data-flow representation available
+ controlled tests written
+ implementation complete
but
Step 4 local execution not yet observed
no user-owned Step 4 explanation recorded
no independent implementation proof
no formal mastery assessment
not mastered
```

Product validation and learning mastery remain separate claims.

## State-maintenance rule

When route, selected responsibility, verified executable boundary, blocker, learning state, or exact continuation changes:

1. update `MEMORY.md` only for live state;
2. replace obsolete live statements instead of accumulating them;
3. change plans/specifications/ADRs only when their stable responsibility actually changes;
4. create dated working-memory only for material historical evidence or reasoning, never as another status owner;
5. keep navigation READMEs non-state-bearing.
