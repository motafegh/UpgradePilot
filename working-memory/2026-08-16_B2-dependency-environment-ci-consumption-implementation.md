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

Because the block used `set -euo pipefail` and reached the complete-suite/final-state sections, the earlier repository-identity, import smoke, focused dependency/workflow/CI tests, and nearest application tests completed successfully.

Visible nearest-application result:

```text
Ran 13 tests in 0.011s
OK
```

Complete deterministic product suite:

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

The trailing `__vsc_update_prompt:6: RPROMPT: parameter not set` occurred after validation and is a local shell/prompt-hook issue, not an UpgradePilot failure.

### 5.3 Cluster-0 conclusion

The new responsibility has a fresh aligned deterministic green baseline. Product-source changes may begin in Cluster 1.

## 6. Cluster 1 — bounded dependency-environment evidence contract

**Status:** ACTIVE — design selected; first product edit next

### 6.1 Current handoff and demonstrated limitation

Active dependency analysis stores:

```text
DependencyChangeAnalysis
├─ dependency: DependencyVersionChange
└─ direct_requirements_install_path: str | None
```

Application orchestration copies the string and CI stops early when it is `None`.

That shape collapses materially different evidence into the same value:

```text
uv.lock change                    → None
constraints-file change           → None
multiple requirements sources     → None
future pyproject optional extra   → None
```

Therefore `None` currently means several different things and cannot carry the new responsibility honestly.

### 6.2 Selected contract shape

Use one dependency-owned typed union of concrete **source contexts**, not one generic object with many optional fields and not a universal environment graph.

Selected conceptual variants:

```text
RequirementsFileDependencyContext
ConstraintsFileDependencyContext
UvLockDependencyContext
PyprojectOptionalExtraDependencyContext
PyprojectDependencyGroupContext
```

Each context preserves:

```text
exact repository
exact head revision
normalized changed-package identity
source provenance/path through DependencyChangeSourceEvidence
+ environment identity only where the source itself establishes it
```

The pyproject variants are admitted contract shapes for the immediately following Cluster 2; they must not be produced as trusted evidence before a real pyproject extractor establishes the extra/group identity.

### 6.3 Transitional compatibility decision

`DependencyChangeAnalysis` will store the typed context tuple as the new source of truth.

The existing `direct_requirements_install_path` API will temporarily remain as a **derived property** for current CI/application callers until Cluster 5 migrates them. It must not remain duplicated stored state.

Projection rule:

```text
exactly one RequirementsFileDependencyContext
→ return its source path

zero or multiple requirements contexts
→ None
```

This preserves current behavior, including the existing rule that multiple requirements paths do not guess one CI path, while allowing uv/constraints/future pyproject evidence to remain distinguishable.

### 6.4 Why alternatives were rejected

Rejected: keep `str | None` and add more command special cases in CI.

Reason: source/environment semantics belong to Dependency, and `None` cannot distinguish the real source shapes now required.

Rejected: one generic dataclass with `kind`, `name`, `path`, `project_root`, and many optional fields.

Reason: it permits invalid combinations and hides which facts are actually established by each source form.

Rejected: universal dependency/environment graph in Cluster 1.

Reason: S001 later needs bounded uv reachability, but no current evidence requires a package-manager-neutral graph architecture.

Rejected: put workflow selection/runtime information into these contexts.

Reason: source context is a dependency-domain fact. Workflow selection belongs to the later static-consumption responsibility; runtime evidence stays separate under ADR-0008.

### 6.5 First implementation slice

The first code change will:

1. add the typed source-context contract under `src/upgradepilot/dependency/` with educational proof-boundary docstrings;
2. populate requirements / constraints / uv contexts from current trusted analysis evidence;
3. change `DependencyChangeAnalysis` to store those contexts;
4. retain `direct_requirements_install_path` only as a derived compatibility projection;
5. add focused tests proving the new distinctions without changing current CI behavior yet.

No CI, GitHub workflow, runtime, resolver, or application semantics are strengthened in this slice.
