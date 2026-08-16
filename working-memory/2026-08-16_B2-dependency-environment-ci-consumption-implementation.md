# B2 Dependency Environment and CI Consumption Evidence — Implementation Record

**Date opened:** 2026-08-16  
**Operation:** bounded implementation of [`../plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md`](../plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md)  
**Result classification:** IN PROGRESS — CLUSTER 2 COMPLETE / GREEN; CLUSTER 3 NOT STARTED  
**Execution branch:** `main`  
**Pre-working-memory selected-plan revision:** `b7f04961bac1f7b2a5ef6873c360fccd523556b9`  
**Validated Cluster-0 baseline:** `7444324e511b1e6fb49e6dba0bac371272bff7ba`  
**Validated Cluster-1 implementation revision:** `ef8b4aa623bb53356b0969d099d2e32ee250b3e9`  
**Validated Cluster-2 implementation revision:** `f3e226a27216f75a689b73acbc4404cafb53f1c1`

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
- [x] **Cluster 2 — exact `pyproject.toml` optional-extra transition evidence**
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

**Status:** COMPLETED / GREEN  
**Validated implementation revision:** `f3e226a27216f75a689b73acbc4404cafb53f1c1`

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

Extended the source-evidence vocabulary with `pyproject_optional_extra` and explicit pyproject ambiguity/unsupported-change problem codes. The generic comparison contract remains source-agnostic.

#### `src/upgradepilot/dependency/pyproject.py`

New dependency-owned extractor with educational proof-boundary documentation. It validates strong exact-file provenance, parses TOML with `tomllib`, parses PEP 508 requirements with `packaging.Requirement`, normalizes package identity with the existing owner, preserves optional-extra identity, and explicitly abstains on broader/ambiguous transitions.

Source-specific result:

```text
ExtractedPyprojectOptionalExtraChange
├─ change: ExtractedDependencyVersionChange
└─ extra: str
```

A neutral `PyprojectOptionalExtraNoChange` result prevents unrelated `pyproject.toml` metadata edits from becoming false dependency-analysis failures. Absence of an admitted PEP 621 optional-dependency surface is neutral; malformed present structures remain problems.

#### `src/upgradepilot/dependency/analysis.py`

PR-wide analysis now recognizes exact `pyproject.toml` paths, explicitly rejects non-`modified` status, acquires exact base/head files, delegates source interpretation, ignores neutral pyproject metadata changes, and preserves trusted extra identity into `PyprojectOptionalExtraDependencyContext(extra=...)`.

Current downstream CI/application consumption still uses the old derived requirements-path compatibility view; migration remains later work.

### 7.5 Test pressure

Focused coverage protects:

- S011-shaped `numpy==1.26.4 → 2.4.6` inside arbitrary extra `mlx`;
- normalized package spelling;
- unchanged general and marker-bearing requirements;
- neutral unrelated pyproject edits;
- several simultaneous changes;
- added extras;
- non-exact changes;
- marker changes;
- repeated package/marker-fork ambiguity;
- malformed TOML;
- PR-wide S011 admission and typed extra context;
- requirements evidence remaining usable beside neutral pyproject edits;
- source contract/problem vocabulary and source topology.

### 7.6 Semantic result

Before Cluster 2:

```text
S011 pyproject.toml
→ ignored by dependency analysis
→ no_supported_dependency_file
```

After Cluster 2:

```text
numpy 1.26.4 → 2.4.6
+
PyprojectOptionalExtraDependencyContext(extra="mlx")
```

This remains source/environment evidence only.

### 7.7 Deliberate non-claims

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

### 7.8 User-observed Cluster-2 validation

The user ran the documented fail-fast Cluster-2 validation after synchronizing `main`. Reaching the complete-suite/final-state markers means the import smoke, focused Cluster-2 tests, and nearest consumer regressions all passed before the visible final result.

Complete deterministic product suite:

```text
Ran 452 tests in 0.085s
OK
```

Final repository state:

```text
branch      : main
HEAD        : f3e226a27216f75a689b73acbc4404cafb53f1c1
origin/main : f3e226a27216f75a689b73acbc4404cafb53f1c1
worktree    : clean
```

The trailing shell message:

```text
__vsc_update_prompt:6: RPROMPT: parameter not set
```

occurred after the validation block and is not an UpgradePilot test failure. It is tracked as a local interactive-shell/prompt integration issue rather than product evidence.

### 7.9 Cluster-2 conclusion

Cluster 2 satisfies its bounded objective and is accepted green at `f3e226a27216f75a689b73acbc4404cafb53f1c1` with `452 tests / OK`.

## 8. Cluster 3 — not started

**Status:** NOT STARTED / HOLD

Next bounded question when the user resumes:

> Given a typed affected dependency source/environment context, can UpgradePilot conservatively recognize which project environment a static workflow install/sync declaration selects, without yet claiming runtime execution or dependency membership through `uv.lock`?

No Cluster-3 source inspection, design selection, implementation, or mutation is authorized until the user explicitly resumes.
