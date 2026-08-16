# B2 Dependency Environment and CI Consumption Evidence — Implementation Record

**Date opened:** 2026-08-16  
**Operation:** bounded implementation of [`../plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md`](../plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md)  
**Result classification:** IN PROGRESS — CLUSTER 2 ACTIVE / DESIGN FROZEN BEFORE SOURCE EDIT  
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

Any new or materially modified source must follow [`../OPERATING_GUIDE.md`](../OPERATING_GUIDE.md):

- meaningful module/class/function docstrings for non-obvious responsibility;
- comments where proof-strength limits, invariants, precedence/abstention, or non-obvious reasons matter;
- explain **why / guarantee / deliberate non-claim**, not line-by-line syntax;
- proportional nearby documentation improvements only; no broad comment-only refactor.

This is part of implementation acceptance discipline, not optional polish.

## 3. Implementation checklist

- [x] **Cluster 0 — synchronize, freeze, and validate baseline**
- [x] **Cluster 1 — bounded dependency-environment evidence contract**
- [ ] **Cluster 2 — exact `pyproject.toml` optional-extra transition evidence** — ACTIVE
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

User-observed validation:

```text
nearest application: 13 tests / OK
complete suite:       435 tests / OK
HEAD/origin:          7444324e511b1e6fb49e6dba0bac371272bff7ba
worktree:             clean
```

The trailing `__vsc_update_prompt:6: RPROMPT: parameter not set` was classified as a local shell/prompt-hook issue after validation, not an UpgradePilot failure.

## 6. Cluster 1 — bounded dependency-environment evidence contract

**Status:** COMPLETED / GREEN  
**Validated implementation revision:** `ef8b4aa623bb53356b0969d099d2e32ee250b3e9`

Cluster 1 replaced the format-specific stored handoff `direct_requirements_install_path: str | None` with dependency-owned typed source contexts:

```text
RequirementsFileDependencyContext
ConstraintsFileDependencyContext
UvLockDependencyContext
PyprojectOptionalExtraDependencyContext
PyprojectDependencyGroupContext
```

`DependencyChangeAnalysis.source_contexts` is now stored truth. `direct_requirements_install_path` survives only as a derived compatibility projection until CI migrates later.

Current trusted extraction populates requirements, constraints, and uv-lock contexts. The pyproject variants are contract surface only until Cluster 2 produces them from exact source evidence.

S001-style `uv.lock` evidence is therefore now preserved as `UvLockDependencyContext(...)` instead of collapsing to an undifferentiated `None`, while current CI semantics remain unchanged.

Deliberate non-claims remain:

```text
source context != group/extra selection
source context != selected-environment membership
source context != CI consumption
source context != command execution/success
source context != runtime exact-version witness
source context != package exercise
```

User-observed Cluster-1 validation:

```text
complete suite: 439 tests / OK
HEAD/origin:    ef8b4aa623bb53356b0969d099d2e32ee250b3e9
worktree:       clean
```

## 7. Cluster 2 — exact `pyproject.toml` optional-extra transition evidence

**Status:** ACTIVE — design/proof rule frozen before source mutation

### 7.1 Owned proposition

Cluster 2 answers only:

> Can exact base/head `pyproject.toml` evidence establish one conservative exact dependency-version transition inside one `[project.optional-dependencies]` extra, while preserving that extra identity as dependency evidence?

Target output:

```text
DependencyVersionChange(package, old_version, proposed_version)
+
PyprojectOptionalExtraDependencyContext(extra=<source-established extra>)
```

The extra name comes from exact project metadata. It is **not** evidence that a workflow selected, installed, executed, or successfully formed that extra.

### 7.2 Real S011 pressure

Frozen Dictare revisions:

```text
repository: dragfly/dictare
base: 9921be73b4a55ba54b7b1f46ba424ada0d38aaa7
head: 62d65da86f902d4b54a9d87e9ced5ff2e1f61e55
source: pyproject.toml
```

Exact base/head source shows `[project.optional-dependencies].mlx` with one relevant change:

```text
base: numpy==1.26.4
head: numpy==2.4.6
```

The same real extra also contains unchanged non-exact requirements (`soundfile>=0.12.0`) and marker-bearing requirements (`mlx-metal==0.30.4; sys_platform == 'darwin'`). Therefore the bounded parser must tolerate general unchanged PEP 508 requirement strings and require exact-pin semantics only for the changed pair.

### 7.3 Selected extraction rule

Use complete exact base/head files, not patch-only reasoning:

```text
modified pyproject.toml
→ exact base/head RepositoryTextFile
→ validate repository/path/revision/blob/byte provenance
→ tomllib parses TOML syntax
→ inspect [project.optional-dependencies]
→ packaging.Requirement parses each requirement string
→ compare optional-extra collections conservatively
```

Admit a transition only when all are true:

1. base/head exact file provenance is coherent with the changed file and PR identity;
2. `[project.optional-dependencies]` is structurally valid on both sides;
3. all entries in the admitted table are valid requirement strings;
4. there is exactly one removed requirement and one added requirement across the optional-extra surface;
5. both differences occur in the same exact extra name;
6. removed/added requirements identify the same normalized package;
7. extras and marker identity are unchanged across the pair;
8. neither side is a URL/direct reference;
9. both sides contain exactly one non-wildcard `==` specifier;
10. exact versions differ.

Anything broader remains a typed problem/abstention rather than heuristic pairing.

### 7.4 Why this rule is proportionate

It is broad enough to support arbitrary optional-extra names and arbitrary valid unchanged requirements, but narrow enough that the exact transition meaning is deterministic.

It deliberately does **not** yet support:

```text
[project].dependencies changes
dependency-group changes
added/removed dependencies
several simultaneous optional-extra transitions
specifier-shape changes such as >=1 → >=2
marker/extras changes
URL/direct-reference transitions
workflow selection of extras
CI consumption of extras
```

Those boundaries prevent S011 from turning Cluster 2 into a general PEP 621/735 dependency engine.

### 7.5 Implementation shape

Planned first source slice:

1. add a dependency-owned `pyproject.py` extractor with educational proof-boundary docstrings/comments;
2. extend the dependency source format contract to represent `pyproject_optional_extra` evidence;
3. return a small pyproject-specific extraction wrapper carrying both the canonical file-level change and its source-established `extra` name, avoiding a generic optional-field scope model;
4. integrate modified `pyproject.toml` acquisition through `analyze_dependency_change()`;
5. translate trusted pyproject evidence into `PyprojectOptionalExtraDependencyContext`;
6. add focused generic tests plus an S011-shaped regression;
7. leave CI/application consumption behavior unchanged until later clusters.

No Cluster-3 workflow/environment-selection semantics are authorized inside this slice.
