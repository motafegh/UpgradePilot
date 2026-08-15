# B2 Cross-Responsibility Architecture — Tranche 1 Implementation Record

**Date:** 2026-08-15  
**Operation:** Phase E / Tranche 1 — static workflow architecture implementation and migration  
**Result classification:** OPEN / progressive implementation evidence record  
**Validated product/source baseline:** `92e6ea6cb6dbfad7c50986d95e23de924a9b36c1` on `main`  
**Latest validated implementation revision:** `f40e7348a38966e7e30b462846a4962a116a9e80` on `main`  

## 1. Purpose and current operating mode

Preserve material implementation, debugging, findings, exact validation evidence, and cluster results while executing Tranche 1 of [`../plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_IMPLEMENTATION_PLAN.md`](../plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_IMPLEMENTATION_PLAN.md).

This file is an implementation evidence trail, not the live-state owner. `../MEMORY.md` alone owns current continuation.

Accepted durable architecture remains [`../docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md`](../docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md).

### Learning deferral decision

The user selected the learning-by-doing/building path and deferred broad mastery/system/data-flow teaching until a meaningful implementation milestone.

```text
build/validate cluster-by-cluster
→ explain only prerequisites/reasoning needed to proceed correctly
→ preserve learning questions/context
→ at a meaningful milestone, pause for deeper current-system + real-data-flow learning
```

### Source documentation rule

The user explicitly requested useful source comments/docstrings. The stable rule is owned by [`../OPERATING_GUIDE.md`](../OPERATING_GUIDE.md): new/materially modified source should document responsibility, proof boundaries, invariants, precedence/abstention logic, and non-obvious reasoning without comments that merely restate syntax.

## 2. Tranche-1 checklist

- [x] **Cluster 0 — synchronize and validate baseline**
- [x] **Cluster 1 — add PyYAML and prove parser dependency boundary**
- [x] **Cluster 2 — implement bounded GitHub Actions static workflow IR**
- [x] **Cluster 3 — implement shared direct-installation declaration observation**
- [x] **Cluster 4 — migrate Target artifact-environment interpretation**
- [ ] **Cluster 5 — migrate CI static reading and narrow proof strength** — implementation written, validation pending
- [ ] **Cluster 6 — reconcile repository-path ownership drift**
- [ ] **Cluster 7 — Tranche-1 regression and acceptance gate**
- [ ] **Tranche-1 stop/review completed**

A checked cluster means its bounded objective and applicable validation were satisfied; code presence alone is insufficient.

## 3. Continuation-critical guards

```text
static declaration != execution != success
consumer unresolved != parser failure
multiple jobs / needs / source order != runtime environment continuity
workflow evidence != complete Target context
direct-install declaration != generic dependency consumption
package invocation/exercise remains CI-specific
static Actions evidence != runtime Actions evidence
Tranche 1 != automatic authorization for Tranche 2
```

## 4. Cluster 0 — green baseline

**Status:** COMPLETED / GREEN BASELINE  
Validated baseline `92e6ea6cb6dbfad7c50986d95e23de924a9b36c1`; full suite: `403 tests / OK`.

## 5. Cluster 1 — PyYAML dependency/parser boundary

**Status:** COMPLETED / GREEN  
**Validated implementation revision:** `0d2c7f9eba08bd3c80f1b128d5b223b4e10a9667`

PyYAML runtime dependency + private bounded representation-node parsing were established and validated.

## 6. Cluster 2 — bounded static GitHub Actions workflow IR

**Status:** COMPLETED / GREEN  
**Validated implementation revision:** `1e3027f87fa5b187c7d333472fe849aa6a49b049`

The provider-owned static IR was independently validated; full suite: `416 tests / OK`.

## 7. Cluster 3 — shared direct-install declaration observation

**Status:** COMPLETED / GREEN  
**Validated implementation revision:** `2980e22994216c069b2f4fb36dc31ea80398367f`

Dependency-owned direct-install observation with working-directory precedence was independently validated; full suite: `425 tests / OK`.

## 8. Cluster 4 — Target migration and proof-strength correction

**Status:** COMPLETED / GREEN  
**Validated implementation revision:** `f40e7348a38966e7e30b462846a4962a116a9e80`

Target now consumes the shared static workflow IR and shared dependency observer. The old static-only runtime-sounding environment-formation contract was replaced by declaration-strength `observed | not_observed | unresolved` evidence.

User-run fail-fast Cluster-4 validation reached its completion marker; full suite:

```text
Ran 430 tests in 0.089s
OK
```

Final validation state was aligned `main`, `HEAD == origin/main == f40e7348...`, and clean worktree.

### T1-F005 — Target is now a consumer rather than a second workflow parser

```text
shared provider structure
+ shared dependency declaration observation
→ Target-specific partial evidence
```

## 9. Cluster 5 — CI migration and proof-claim narrowing

**Status:** IMPLEMENTATION WRITTEN / VALIDATION PENDING

### Expected

Migrate CI static reading away from its local indentation/regex YAML reader onto the validated shared workflow IR and dependency direct-install observer where semantics are identical. Keep package invocation/exercise CI-specific. Narrow the strongest current CI result so successful runtime run/job evidence plus static path recognition is not described as matched-command runtime success.

Do not implement static↔runtime step correlation.

### Changes

#### Small shared-observer refinement

`src/upgradepilot/dependency/direct_install.py` now exposes:

```text
matched_segment_index: int | None
```

for an observed direct install declaration. This zero-based locator refers only to the bounded static shell-segment split already performed by the dependency observer. It exists so CI can compare static declaration order without duplicating install parsing.

The contract explicitly states:

```text
static segment ordinal
!= runtime command/step identity
```

Focused direct-install tests now protect that locator.

#### CI static command migration

`src/upgradepilot/ci/workflow_commands.py` was rewritten as a consumer of:

```text
parse_workflow_definition(...)
observe_direct_installation_declaration(...)
```

It no longer owns GitHub Actions YAML/indentation parsing or a second pip requirements matcher.

CI-specific responsibility retained here:

```text
direct package invocation recognition
+ one-job current selection boundary
+ static install-before-invocation ordering
```

The current rule requires one statically readable local steps job because static↔runtime job correlation is not implemented. Multiple jobs remain CI-level unresolved rather than being composed or guessed.

Static source ordering is now checked using `(step source_index, shell segment index)` so a visible invocation before installation is not treated as a valid static dependency path. This is still static source evidence only.

`WorkflowCommandEvidence.status = supported` now means:

```text
one bounded static job
+ supplied dependency-source install declaration
+ later direct package invocation declaration
```

and explicitly does **not** mean runtime execution/success.

#### CI combined proof-state correction

`src/upgradepilot/ci/dependency_exercise.py` replaces the old strongest state:

```text
proven
```

with:

```text
supported_not_correlated
```

The state requires two separate premises:

```text
successful exact-head workflow/run + at least one successful runtime job record
+
exact-head static workflow definition declares an ordered install→package-invocation path
```

The source comments/docstrings explicitly preserve the missing link:

```text
successful runtime workflow/job evidence
+ ordered static path
!= matched static commands observed executing/succeeding at runtime
```

Top-level reason:

```text
successful_exact_head_ci_with_static_dependency_path
```

Workflow-level reason:

```text
successful_ci_with_ordered_static_dependency_path
```

If successful runtime CI exists but the admitted static path cannot be established, the aggregate remains `unresolved` rather than `proven`.

#### Regression changes

`tests/test_workflow_commands.py` now exercises the shared-IR consumer boundary, including:

- ordered named run steps;
- ordered install/invocation segments in one run block;
- invocation-before-install → unresolved;
- multiple jobs → unresolved without static↔runtime job correlation.

`tests/test_ci_dependency_exercise.py` now protects:

- `supported_not_correlated` rather than `proven`;
- explicit non-correlation detail;
- no successful CI;
- unavailable/mismatched evidence boundaries;
- indirect tox path remains unresolved;
- multi-job unresolved behavior;
- install-before-invocation requirement;
- explicit requirements-path requirement;
- heterogeneous workflow results preserved.

### Source/test commits

```text
c18e6a57e2c80f7ea2e6d360280d0239f24ed10d
→ Expose static install segment location

e6431b76ab64b109681672d636fe8d256fe3a03a
→ Test static install segment location

f222b7c4975c4b98b4e9be834dafa5cc46d4e6ff
→ Migrate CI static command reading to shared workflow IR

01330c3e9d9895c0a76f50a9fcd62797c664bd10
→ Narrow CI dependency exercise proof state

80d187edf6d1b0e0089a32d757c77c3c0a7e02d3
→ Update CI static path regressions for shared IR

f561b4b271092af08412c91b49de27f7a754bc8f
→ Update CI exercise regressions for narrowed proof state
```

### Current non-goals

Cluster 5 does not implement:

```text
static↔runtime job/step correlation
runtime log interpretation
matrix runtime-instance mapping
reusable-workflow execution
repository-path cleanup
application orchestration changes
```

### Validation

Pending user-run WSL focused/nearest/full gate.

### Cluster result

`PARTIAL / IMPLEMENTATION WRITTEN / VALIDATION PENDING`

Cluster 6 must not begin until Cluster 5 is validated and explicitly closed.

## 10. Remaining plan responsibilities

- Cluster 6 — repository-path ownership reconciliation: **PENDING**
- Cluster 7 — Tranche-1 acceptance gate: **PENDING**
- Tranche-1 stop/review: **PENDING**

Tranche 2 remains separately reviewed work and is outside this record.
