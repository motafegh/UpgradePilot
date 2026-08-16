# B2 Dependency Environment and CI Consumption Evidence — Implementation Record

**Date opened:** 2026-08-16  
**Operation:** bounded implementation of [`../plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md`](../plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md)  
**Result classification:** IN PROGRESS — CLUSTER 1 CONTRACT WORK  
**Execution branch:** `main`  
**Pre-working-memory selected-plan revision:** `b7f04961bac1f7b2a5ef6873c360fccd523556b9`  
**Validated Cluster-0 baseline:** `7444324e511b1e6fb49e6dba0bac371272bff7ba`

## 1. Purpose and operating mode

Preserve the single progressive implementation, debugging, validation, learning, and decision trail for the selected Dependency Environment and CI Consumption Evidence responsibility.

This file is updated throughout the implementation rather than creating one record per command, cluster, or failure. `../MEMORY.md` remains the sole live-state/continuation owner.

The responsibility begins from a real limitation exposed during S001/S011 learning:

```text
trusted dependency transition
!= dependency-environment membership
!= static workflow environment selection/consumption
!= runtime execution/success
!= exact-version witness
!= package exercise
!= behavioral compatibility/safety/action
```

The implementation must broaden the current direct-requirements-only CI input without turning GitHub Actions, CI, or `dependency/direct_install.py` into a universal package-manager/environment interpreter.

## 2. Learning-by-building / source-documentation mode

Implementation proceeds in bounded clusters. Before each material source change, record the exact responsibility/proof question; after it, record what changed, why, what the output means, what it deliberately does not mean, and the validation evidence.

Any new or materially modified source must follow [`../OPERATING_GUIDE.md`](../OPERATING_GUIDE.md):

- meaningful module/class/function docstrings for non-obvious responsibility;
- comments where proof-strength limits, invariants, precedence, abstention, or non-obvious reasons matter;
- explain **why / guarantee / deliberate non-claim**, not line-by-line syntax;
- proportional nearby documentation improvements only; no broad comment-only refactor.

This is part of the implementation acceptance discipline, not optional polish.

## 3. Implementation checklist

- [x] **Cluster 0 — synchronize, freeze, and validate baseline**
- [ ] **Cluster 1 — bounded dependency-environment evidence contract**
- [ ] **Cluster 2 — exact `pyproject.toml` optional-extra transition evidence**
- [ ] **Cluster 3 — bounded project-environment selection semantics**
- [ ] **Cluster 4 — bounded `uv.lock` selected-environment membership/reachability**
- [ ] **Cluster 5 — CI migration to typed consumption evidence**
- [ ] **Cluster 6 — application/CLI integration + S001/S011/S005 pressure**
- [ ] **Cluster 7 — AUDIT-004 resolver-satisfiability reassessment gate**
- [ ] **Cluster 8 — regression, acceptance, STOP/REVIEW**

A checked cluster means its bounded objective and applicable focused/nearest/full validation are satisfied. Code presence alone is insufficient.

## 4. Continuation-critical guards

```text
Tranche 1 remains accepted historical foundation; do not reopen it
Tranche 2 remains separate and not selected
GitHub provider owns GitHub Actions structure, not package-manager meaning
Dependency owns dependency source/environment membership/selection meaning
CI owns CI-specific evidence composition and package-exercise interpretation
Application owns sequencing, not source semantics

package present somewhere in uv.lock
!= member of every selected environment

.[dev]
!= .[mlx]

static environment selection/consumption declaration
!= runtime execution
!= installation success

changed dependency consumed
!= changed package directly exercised

resolver-satisfiable
!= behavioral compatibility

missing/ambiguous evidence
!= negative fact
```

## 5. Cluster 0 — green baseline

**Status:** COMPLETED / GREEN  
**Validated baseline:** `7444324e511b1e6fb49e6dba0bac371272bff7ba`

### 5.1 Baseline preparation

The selected plan was published and selected before product-source implementation. The progressive WM and live memory were then added/updated. Before the user executed the baseline, the active test-module surface was checked and one stale draft module name was corrected:

```text
stale draft: tests.test_uv_lock_dependency_change
active test: tests.test_uv_lock_change
adjacent boundary: tests.test_uv_lock_versionless_records
```

This was a validation-command correction, not a product-source defect.

### 5.2 User-observed fail-fast baseline evidence

The user ran the documented fail-fast Cluster-0 command locally after synchronizing `main`.

Because the block used:

```bash
set -euo pipefail
```

and reached the complete-suite and final-state sections, the earlier repository-identity, import smoke, focused dependency/workflow/CI tests, and nearest application tests completed successfully before the visible final output.

Visible nearest-application result:

```text
Ran 13 tests in 0.011s
OK
```

Visible complete deterministic product suite:

```text
Ran 435 tests in 0.080s
OK
```

Final repository state:

```text
branch      : main
HEAD        : 7444324e511b1e6fb49e6dba0bac371272bff7ba
origin/main : 7444324e511b1e6fb49e6dba0bac371272bff7ba
worktree    : clean
```

The trailing shell message:

```text
__vsc_update_prompt:6: RPROMPT: parameter not set
```

occurred after the test/final-state block and is classified as a local shell/prompt-hook issue, not an UpgradePilot test or repository failure.

### 5.3 Cluster-0 conclusion

The new responsibility now has a fresh, aligned, clean, deterministic green baseline. Product-source changes may begin in Cluster 1.

The accepted Tranche-1 revision remains historical proof for Tranche 1; `7444324...` is the starting validation point for this new implementation responsibility.

## 6. Cluster 1 — bounded dependency-environment evidence contract

**Status:** ACTIVE — source inspection/design before first product edit

### 6.1 Bounded question

> What is the smallest typed dependency-owned evidence contract that can replace the format-specific `direct_requirements_install_path: str | None` handoff while preserving exact source provenance and representing requirements, uv project/lock, optional-extra, and dependency-group contexts **without** encoding runtime execution or a universal environment graph?

### 6.2 Required design properties before coding

The Cluster-1 contract must:

- be owned under `upgradepilot.dependency`;
- preserve normalized changed-package identity and exact source/revision/path provenance already established upstream;
- represent a source/environment context without claiming that environment was selected by a workflow;
- preserve the existing exact-requirements path as one supported source shape rather than special-casing it in CI;
- leave room for `uv.lock` + project metadata and `pyproject.toml` extra/group contexts needed by later clusters;
- avoid putting GitHub Actions objects, runtime CI status, package-manager execution results, or resolver-success claims into the dependency-source/environment contract;
- avoid a universal dependency/environment graph merely for symmetry.

Before the first edit, inspect the active handoff through dependency analysis, CI evaluation, application orchestration, and existing tests. Record the chosen contract shape and why narrower/wider alternatives were rejected.
