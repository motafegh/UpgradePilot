# B2 Dependency Environment and CI Consumption Evidence — Implementation Record

**Date opened:** 2026-08-16  
**Operation:** bounded implementation of [`../plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md`](../plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md)  
**Result classification:** IN PROGRESS — CLUSTER 1 IMPLEMENTED / VALIDATION PENDING  
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

The user ran the documented fail-fast Cluster-0 command locally under `set -euo pipefail` after synchronizing `main`.

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

## 6. Cluster 1 — bounded dependency-environment evidence contract

**Status:** IMPLEMENTED / VALIDATION PENDING

### 6.1 Current handoff and demonstrated limitation

Before this cluster, dependency analysis stored:

```text
DependencyChangeAnalysis
├─ dependency: DependencyVersionChange
└─ direct_requirements_install_path: str | None
```

That collapsed materially different evidence into the same `None` value:

```text
uv.lock change                    → None
constraints-file change           → None
multiple requirements sources     → None
future pyproject optional extra   → None
```

### 6.2 Selected contract shape

Use one dependency-owned typed union of concrete source contexts:

```text
RequirementsFileDependencyContext
ConstraintsFileDependencyContext
UvLockDependencyContext
PyprojectOptionalExtraDependencyContext
PyprojectDependencyGroupContext
```

Each context preserves exact repository/head revision, normalized package identity, and the existing `DependencyChangeSourceEvidence`. Environment identity is present only where source evidence can establish it.

The pyproject variants define the immediate next contract surface but must not become trusted product evidence until Cluster 2 implements exact source extraction.

### 6.3 Transitional compatibility rule

`DependencyChangeAnalysis.source_contexts` is now the stored source of truth.

`direct_requirements_install_path` remains only as a derived compatibility property:

```text
exactly one RequirementsFileDependencyContext
→ source path

zero or multiple requirements contexts
→ None
```

This preserves existing CI behavior while avoiding duplicated format-specific stored truth.

### 6.4 Implemented source changes

#### `src/upgradepilot/dependency/environment.py`

New dependency-owned contract module with educational proof-boundary docstrings. It explicitly states:

```text
source context
!= workflow selection
!= runtime execution
!= resolver/install success
!= package exercise
```

Concrete source-context dataclasses prevent invalid combinations that a generic optional-field record would permit.

#### `src/upgradepilot/dependency/analysis.py`

`DependencyChangeAnalysis` now stores:

```text
dependency
source_contexts
```

and derives the legacy requirements path when current CI still needs it.

Current trusted extraction evidence is translated as:

```text
requirements-family exact requirement → RequirementsFileDependencyContext
constraints-family exact requirement  → ConstraintsFileDependencyContext
uv_lock                               → UvLockDependencyContext
```

The translation deliberately does not invent uv group/extra membership or treat a constraints file as a directly installable environment.

#### focused tests

Added `tests/test_dependency_environment.py` to prove:

- requirements context + legacy projection;
- constraints remain distinct and do not become direct requirements;
- uv lock has a typed context without invented membership;
- multiple requirements contexts are preserved while legacy projection abstains.

Controlled investigation and Step-7F fixtures were migrated from constructing `DependencyChangeAnalysis` with the old string keyword to constructing a real `RequirementsFileDependencyContext`.

### 6.5 What changed semantically

We now preserve more truthful dependency-domain information:

```text
S001 uv.lock
OLD → direct_requirements_install_path = None
NEW → UvLockDependencyContext(...) + derived old projection None
```

So later code can distinguish “uv lock source exists” from “no source information.”

### 6.6 What did NOT change

This cluster does **not** yet establish:

```text
which uv group/extra is selected
whether the changed package belongs to that selected environment
whether CI consumes the environment
whether commands execute/succeed
whether the exact proposed version is present at runtime
whether the changed package is exercised
```

CI/application still consume the derived old requirements-path view for now. Consumer migration is deliberately deferred to Cluster 5 after the dependency/environment semantics are implemented.

### 6.7 Validation gate

Cluster 1 is not complete until the user runs focused validation from synchronized `main` and the new tests plus nearest existing dependency/application regressions are green.
