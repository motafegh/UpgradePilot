# B2 Dependency Environment and CI Consumption Evidence — Implementation Record

**Date opened:** 2026-08-16  
**Operation:** bounded implementation of [`../plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md`](../plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md)  
**Result classification:** IN PROGRESS — CLUSTER 2 IMPLEMENTED / VALIDATION PENDING  
**Execution branch:** `main`  
**Pre-working-memory selected-plan revision:** `b7f04961bac1f7b2a5ef6873c360fccd523556b9`  
**Validated Cluster-0 baseline:** `7444324e511b1e6fb49e6dba0bac371272bff7ba`  
**Validated Cluster-1 implementation revision:** `ef8b4aa623bb53356b0969d099d2e32ee250b3e9`

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

Any new or materially modified source follows [`../OPERATING_GUIDE.md`](../OPERATING_GUIDE.md): meaningful docstrings/comments explain responsibility, proof boundaries, invariants, abstention, and deliberate non-claims without noisy line-by-line narration.

## 3. Implementation checklist

- [x] **Cluster 0 — synchronize, freeze, and validate baseline**
- [x] **Cluster 1 — bounded dependency-environment evidence contract**
- [ ] **Cluster 2 — exact `pyproject.toml` optional-extra transition evidence** — IMPLEMENTED / VALIDATION PENDING
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

package present somewhere in uv.lock != member of every selected environment
.[dev] != .[mlx]
static environment selection/consumption declaration != runtime execution/success
changed dependency consumed != changed package directly exercised
resolver-satisfiable != behavioral compatibility
missing/ambiguous evidence != negative fact
```

## 5. Cluster 0 — green baseline

**Status:** COMPLETED / GREEN  
**Validated baseline:** `7444324e511b1e6fb49e6dba0bac371272bff7ba`

```text
nearest application: 13 tests / OK
complete suite:       435 tests / OK
HEAD/origin:          7444324e511b1e6fb49e6dba0bac371272bff7ba
worktree:             clean
```

## 6. Cluster 1 — bounded dependency-environment evidence contract

**Status:** COMPLETED / GREEN  
**Validated implementation revision:** `ef8b4aa623bb53356b0969d099d2e32ee250b3e9`

Cluster 1 introduced dependency-owned typed source contexts and made them stored truth:

```text
RequirementsFileDependencyContext
ConstraintsFileDependencyContext
UvLockDependencyContext
PyprojectOptionalExtraDependencyContext
PyprojectDependencyGroupContext
```

The old `direct_requirements_install_path` survives only as a derived compatibility projection. Current CI behavior remains unchanged.

```text
complete suite: 439 tests / OK
HEAD/origin:    ef8b4aa623bb53356b0969d099d2e32ee250b3e9
worktree:       clean
```

## 7. Cluster 2 — exact `pyproject.toml` optional-extra transition evidence

**Status:** IMPLEMENTED / VALIDATION PENDING

### 7.1 Owned proposition

Cluster 2 answers only:

> Can exact base/head `pyproject.toml` evidence establish one conservative exact dependency-version transition inside one `[project.optional-dependencies]` extra, while preserving that extra identity as dependency evidence?

Target result:

```text
DependencyVersionChange(package, old_version, proposed_version)
+
PyprojectOptionalExtraDependencyContext(extra=<source-established extra>)
```

The extra name is dependency-source evidence. It is **not** evidence that CI selected, installed, executed, or successfully formed that extra.

### 7.2 Real S011 pressure

Frozen Dictare source:

```text
repository: dragfly/dictare
base: 9921be73b4a55ba54b7b1f46ba424ada0d38aaa7
head: 62d65da86f902d4b54a9d87e9ced5ff2e1f61e55
source: pyproject.toml
extra: mlx
base requirement: numpy==1.26.4
head requirement: numpy==2.4.6
```

The same real extra contains unchanged non-exact and marker-bearing requirements. Therefore the implementation parses general unchanged PEP 508 entries and requires exact-pin semantics only for the changed pair.

### 7.3 Frozen extraction rule

```text
modified pyproject.toml
→ exact base/head RepositoryTextFile
→ strong repository/path/revision/blob/byte provenance
→ tomllib syntax parsing
→ [project.optional-dependencies]
→ packaging.Requirement per entry
→ conservative base/head collection comparison
```

A transition is admitted only when exactly one removed + one added requirement occur in the same extra, identify the same normalized package, preserve dependency extras/marker/direct-reference identity, and each side has exactly one non-wildcard `==version` specifier.

Broader changes abstain explicitly.

### 7.4 Implemented source changes

#### `src/upgradepilot/dependency/change.py`

Extended the source-evidence vocabulary with:

```text
file_format = pyproject_optional_extra
```

and explicit pyproject ambiguity/unsupported-change problem codes. The generic comparison contract itself remains source-agnostic.

#### `src/upgradepilot/dependency/pyproject.py`

New dependency-owned extractor with educational proof-boundary documentation.

Key responsibilities:

- validate strong exact base/head file provenance;
- parse TOML with `tomllib`;
- parse requirement strings with `packaging.Requirement` rather than hand-parsing PEP 508;
- normalize package identity through the existing package-identity owner;
- preserve extra identity separately from the canonical version change;
- reject repeated package records in one extra under this first bounded rule rather than guessing across marker forks;
- reject several simultaneous changes, cross-extra moves, marker/extras changes, direct-reference changes, wildcard/non-exact specifiers, and malformed structures.

Source-specific result:

```text
ExtractedPyprojectOptionalExtraChange
├─ change: ExtractedDependencyVersionChange
└─ extra: str
```

This avoids adding generic optional scope fields to the shared dependency-change contract.

#### Neutral pyproject result

Implementation review exposed an important project-file boundary: `pyproject.toml` is not exclusively a dependency file. Unrelated metadata edits must not poison PR-wide dependency analysis.

Therefore the extractor also has:

```text
PyprojectOptionalExtraNoChange
```

Meaning only:

```text
exact optional-dependency surface unchanged
```

It does **not** mean the whole pyproject is unchanged or that dependencies are absent. `analyze_dependency_change()` treats this result as neutral so another admitted requirements/uv source in the same PR remains usable.

Absence of a PEP 621 `[project]` table or optional-dependency table is likewise neutral for this bounded rule; a malformed table that is actually present remains an explicit problem.

#### `src/upgradepilot/dependency/analysis.py`

PR-wide analysis now recognizes exact `pyproject.toml` paths, explicitly rejects non-`modified` status, acquires exact base/head files, delegates to the new extractor, and preserves the source-established extra into:

```text
PyprojectOptionalExtraDependencyContext(extra=...)
```

A missing extra mapping after a trusted pyproject extraction is treated as an internal invariant failure, not silently downgraded.

Current downstream CI/application consumption still uses the old derived requirements-path view; source-context consumer migration remains later work.

#### `src/upgradepilot/dependency/environment.py`

No semantic widening was required. The Cluster-1 `PyprojectOptionalExtraDependencyContext` contract was already sufficient and is now produced from real trusted source evidence.

### 7.5 Test pressure added/updated

`tests/test_pyproject_optional_extra_change.py` covers:

- S011-shaped `numpy==1.26.4 → 2.4.6` in arbitrary extra `mlx`;
- normalized package spelling across the changed pair;
- unchanged general/marker-bearing requirements;
- neutral unrelated pyproject metadata edits;
- several simultaneous changes;
- added extra;
- non-exact specifier change;
- marker change;
- repeated package records/marker-fork ambiguity;
- malformed TOML.

`tests/test_pyproject_dependency_analysis.py` covers:

- PR-wide S011-shaped admission;
- exact `PyprojectOptionalExtraDependencyContext(extra="mlx")` output;
- no direct-requirements compatibility projection for pyproject evidence;
- unrelated pyproject metadata not blocking a separate valid requirements transition;
- non-modified pyproject status stops explicitly without file acquisition.

`tests/test_dependency_change_contracts.py` now protects the expanded file-format/problem vocabulary.

`tests/test_source_topology.py` now imports the new extractor from the dependency owner and retains the pre-existing obsolete-flat-module guard.

### 7.6 Semantic result so far

Before Cluster 2, S011 normal dependency analysis stopped at:

```text
pyproject.toml ignored
→ no_supported_dependency_file
```

After this slice, the dependency-analysis layer can represent:

```text
numpy 1.26.4 → 2.4.6
+
PyprojectOptionalExtraDependencyContext(extra="mlx")
```

This is the first real production of the pyproject optional-extra context designed in Cluster 1.

### 7.7 Deliberate non-claims / not yet implemented

Cluster 2 still does **not** establish:

```text
workflow selects mlx
.[dev] excludes/contains mlx by execution proof
optional environment is installed or formed
CI consumed numpy through mlx
exact numpy 2.4.6 was observed at runtime
NumPy behavior was exercised
MLX behavior is compatible
```

Those questions belong to later environment-selection, consumption, runtime, and behavioral responsibilities.

### 7.8 Validation gate

Current source/test implementation head before this WM update:

```text
78d0a8f22b7d3c2d9c630a9647a8854cbcdad6c5
```

Cluster 2 is not complete until focused extractor/analysis/contract/topology tests, nearest consumer regressions, and the full deterministic suite are green from a synchronized clean `main`.

Do **not** start Cluster 3 before that validation is recorded here.
