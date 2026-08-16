# B2 Dependency Environment and CI Consumption Evidence — Implementation Record

**Date opened:** 2026-08-16  
**Operation:** bounded implementation of [`../plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md`](../plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md)  
**Result classification:** IN PROGRESS — CLUSTER 0 BASELINE GATE  
**Execution branch:** `main`  
**Pre-working-memory selected-plan revision:** `b7f04961bac1f7b2a5ef6873c360fccd523556b9`

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

- [ ] **Cluster 0 — synchronize, freeze, and validate baseline**
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

## 5. Cluster 0 — baseline gate

**Status:** IN PROGRESS  
**Pre-WM remote main:** `b7f04961bac1f7b2a5ef6873c360fccd523556b9`

### 5.1 Remote baseline observation

GitHub `main` was re-read immediately before opening this record and pointed to:

```text
b7f04961bac1f7b2a5ef6873c360fccd523556b9
```

That revision selects the new plan but contains no new product-source implementation for it. Accepted Tranche-1 product/source proof remains `ef4283db0a7ce3eec75a56ccc5c07354015fd2e3`; later learning/audit/plan/WM commits do not themselves replace runtime validation.

### 5.2 Validation execution constraint

The assistant execution container cannot resolve `github.com`, so a fresh local checkout/test run cannot be performed from that environment. GitHub remote state is still available through the connected GitHub provider, but repository/CI metadata must not be substituted for the plan-required deterministic product-suite baseline.

Therefore Cluster 0 remains open until a local fail-fast baseline run is observed after synchronizing `main`.

### 5.3 Required local fail-fast baseline

Run from the normal local UpgradePilot checkout after pulling `main`:

```bash
set -euo pipefail

cd ~/projects/UpgradePilot

git switch main
git pull --ff-only origin main

printf '\n=== REPOSITORY IDENTITY ===\n'
git branch --show-current
git rev-parse HEAD
git rev-parse origin/main
git status --short

printf '\n=== ENVIRONMENT / IMPORT SMOKE ===\n'
python --version
python -c "import upgradepilot, yaml, packaging, requests; print('imports: OK')"

printf '\n=== FOCUSED DEPENDENCY / WORKFLOW / CI BASELINE ===\n'
python -m unittest -v \
  tests.test_dependency_analysis \
  tests.test_dependency_change \
  tests.test_dependency_change_comparison \
  tests.test_dependency_change_contracts \
  tests.test_exact_requirement_change \
  tests.test_uv_lock_dependency_change \
  tests.test_direct_install_declaration \
  tests.test_github_workflow_definition \
  tests.test_workflow_commands \
  tests.test_ci_dependency_exercise \
  tests.test_github_actions

printf '\n=== NEAREST APPLICATION BASELINE ===\n'
python -m unittest -v \
  tests.test_investigation \
  tests.test_cli \
  tests.test_step7f_end_to_end

printf '\n=== COMPLETE PRODUCT SUITE ===\n'
python -m unittest discover -s tests -p 'test_*.py'

printf '\n=== FINAL REPOSITORY STATE ===\n'
printf 'branch      : '; git branch --show-current
printf 'HEAD        : '; git rev-parse HEAD
printf 'origin/main : '; git rev-parse origin/main
printf 'worktree    : '; test -z "$(git status --porcelain)" && echo clean || git status --short
```

If any module name above has been renamed since the accepted Tranche-1 gate, classify that command mismatch before changing product source; do not silently skip the affected responsibility.

### 5.4 Cluster-0 pass condition

Cluster 0 closes only when:

```text
main synchronized
+ HEAD == origin/main
+ clean worktree
+ import smoke green
+ focused dependency/workflow/CI baseline green
+ nearest investigation/CLI/end-to-end baseline green
+ complete deterministic product suite green
```

No product source is to be modified before this gate is satisfied.

## 6. Cluster 1 — pending

After Cluster 0 is green, the next bounded question is:

> What is the smallest typed dependency-owned evidence contract that can replace the format-specific `direct_requirements_install_path: str | None` handoff while preserving exact source provenance and representing requirements, uv project/lock, optional-extra, and dependency-group contexts **without** encoding runtime execution or a universal environment graph?

Do not begin this source design until Cluster 0 is closed in this record.
