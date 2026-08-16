# B2 Dependency Environment and CI Consumption Evidence — Implementation Record

**Date opened:** 2026-08-16  
**Operation:** bounded implementation of [`../plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md`](../plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md)  
**Result classification:** IN PROGRESS — CLUSTER 3 ACTIVE / DESIGN FROZEN BEFORE SOURCE EDIT  
**Execution branch:** `main`  
**Pre-working-memory selected-plan revision:** `b7f04961bac1f7b2a5ef6873c360fccd523556b9`  
**Validated Cluster-0 baseline:** `7444324e511b1e6fb49e6dba0bac371272bff7ba`  
**Validated Cluster-1 implementation revision:** `ef8b4aa623bb53356b0969d099d2e32ee250b3e9`  
**Validated Cluster-2 implementation revision:** `f3e226a27216f75a689b73acbc4404cafb53f1c1`  
**Pre-Cluster-3 documentation head:** `16c2ead070a4683d76f4b5d0ebe6a5cc03c9b10a`

## 1. Purpose and operating mode

Preserve the single progressive implementation, debugging, validation, learning, and decision trail for the selected Dependency Environment and CI Consumption Evidence responsibility. `../MEMORY.md` remains the sole live-state/continuation owner.

The responsibility keeps this proof ladder explicit:

```text
trusted dependency transition
!= dependency-environment membership
!= static workflow environment selection/consumption
!= runtime execution/success
!= exact-version witness
!= package exercise
!= behavioral compatibility/safety/action
```

## 2. Learning-by-building / source-documentation mode

Before each material source change, record the exact responsibility/proof question; after it, record what changed, why, what the output means, what it deliberately does not mean, and the validation evidence.

New/materially modified source follows `../OPERATING_GUIDE.md`: meaningful docstrings/comments explain ownership, proof boundaries, invariants, abstention, and deliberate non-claims rather than narrating syntax.

## 3. Implementation checklist

- [x] **Cluster 0 — synchronize, freeze, and validate baseline**
- [x] **Cluster 1 — bounded dependency-environment evidence contract**
- [x] **Cluster 2 — exact `pyproject.toml` optional-extra transition evidence**
- [ ] **Cluster 3 — bounded project-environment selection semantics** — ACTIVE
- [ ] **Cluster 4 — bounded `uv.lock` selected-environment membership/reachability**
- [ ] **Cluster 5 — CI migration to typed consumption evidence**
- [ ] **Cluster 6 — application/CLI integration + S001/S011/S005 pressure**
- [ ] **Cluster 7 — AUDIT-004 resolver-satisfiability reassessment gate**
- [ ] **Cluster 8 — regression, acceptance, STOP/REVIEW**

A checked cluster means code plus applicable focused/nearest/full validation is green. Code presence alone is insufficient.

## 4. Continuation-critical guards

```text
Tranche 1 remains accepted historical foundation; do not reopen it
Tranche 2 remains separate and not selected
GitHub owns GitHub Actions source structure
Dependency owns dependency/project selection meaning
CI owns CI-specific composition
Application owns sequencing

package present somewhere in uv.lock != member of every selected environment
.[dev] != .[mlx]
static environment selection != runtime environment formation
static selection != command execution/success
changed dependency consumed != changed package exercised
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
**Validated revision:** `ef8b4aa623bb53356b0969d099d2e32ee250b3e9`

Stored truth became typed dependency source contexts:

```text
RequirementsFileDependencyContext
ConstraintsFileDependencyContext
UvLockDependencyContext
PyprojectOptionalExtraDependencyContext
PyprojectDependencyGroupContext
```

`direct_requirements_install_path` survives only as a derived compatibility projection. S001-style `uv.lock` evidence therefore survives as `UvLockDependencyContext(...)` instead of an undifferentiated `None`.

```text
complete suite: 439 tests / OK
```

## 7. Cluster 2 — exact pyproject optional-extra transition evidence

**Status:** COMPLETED / GREEN  
**Validated revision:** `f3e226a27216f75a689b73acbc4404cafb53f1c1`

Owned proposition:

> Can exact base/head `pyproject.toml` evidence establish one conservative exact version transition inside one `[project.optional-dependencies]` extra while preserving that extra identity as dependency evidence?

Accepted S011-shaped result:

```text
numpy 1.26.4 → 2.4.6
+
PyprojectOptionalExtraDependencyContext(extra="mlx")
```

Implementation uses exact base/head `RepositoryTextFile`, strong provenance validation, `tomllib`, `packaging.Requirement`, conservative collection comparison, and a neutral `PyprojectOptionalExtraNoChange` result for unrelated project-metadata edits. Broader/ambiguous changes abstain explicitly.

Deliberate non-claims remain workflow selection, environment formation, CI consumption, runtime exact-version observation, package exercise, and compatibility.

```text
complete suite: 452 tests / OK
HEAD/origin:    f3e226a27216f75a689b73acbc4404cafb53f1c1
worktree:       clean
```

## 8. Cluster 3 — bounded project-environment selection semantics

**Status:** ACTIVE — design/proof rule frozen before source mutation

### 8.1 Owned proposition

Cluster 3 answers only:

> Given one provider-owned static `RunStepDefinition` plus an independently established exact project path/context, what project optional extras and dependency groups does the run declaration visibly select?

Target shape is **static declaration evidence**, not runtime evidence:

```text
RunStepDefinition
+ workflow/job/step working-directory context
+ exact project file path
→ observed | not_observed | unresolved
→ zero or more typed project-environment selectors
```

### 8.2 Real pressure

S011 exact-head workflow contains:

```text
pip install -e ".[dev]"
```

while the affected dependency context is:

```text
PyprojectOptionalExtraDependencyContext(extra="mlx")
```

Cluster 3 must preserve the declaration fact:

```text
selected extra = dev
```

without upgrading it to repository-wide absence of `mlx` or runtime installation.

S001 exact-head workflows contain explicit uv selectors including forms such as:

```text
uv sync --group <name>
uv sync --only-group <name>
uv sync --all-extras
```

and the plan requires bounded support for `uv sync` / `uv run` positive project selection.

### 8.3 Current uv semantic facts used by this design

Current official uv documentation establishes:

```text
--extra NAME       includes the named optional extra
--all-extras       includes all optional dependencies
--group NAME       includes the named dependency group
--only-group NAME  selects only the named group (within uv's group semantics)
--all-groups       includes all dependency groups
uv run in a project creates/updates the project environment before invocation
uv extras are not synced by default
uv has default dependency-group behavior
```

Therefore Cluster 3 will recognize **visible positive selection** and will not treat selector omission as a negative fact. Default-group reconstruction is deferred until exact source/config evidence justifies it.

### 8.4 Selected type shape

Use a dependency-owned observation with one or more static declarations. Each declaration preserves:

```text
package manager: pip | uv
operation:       install | sync | run
shell-segment index
exact project file/root binding
selectors:
  OptionalExtraSelector(name)
  DependencyGroupSelector(name, mode=include|only)
  AllOptionalExtrasSelector
  AllDependencyGroupsSelector
```

A declaration may contain multiple selectors when command semantics make them explicit.

The observation state remains:

```text
observed
not_observed
unresolved
```

Known literal selectors may still be preserved in an `unresolved` observation when another material selector/path is dynamic or unsupported.

### 8.5 Project binding and working-directory rule

The observer must not assume every `pip`/`uv` command belongs to the affected project.

It receives an independently established repository-relative `pyproject.toml` path and uses effective GitHub Actions working-directory precedence:

```text
step > job defaults.run > workflow defaults.run > repository root
```

Initial binding rules:

- `pip install [-e|--editable] .[extra...]` or the corresponding literal local project requirement is resolved against effective working directory and must match the expected project root;
- `uv sync` / `uv run` without `--project` is admitted only when the effective working directory statically equals the expected project root;
- literal `uv --project`/command `--project` path may bind when it safely resolves to the expected project root;
- dynamic working directory or dynamic project path is unresolved;
- `--directory`, `--package`, `--no-project`, or other project-targeting forms not modeled by the first rule must not be guessed.

### 8.6 Command interpretation boundary

This is not a shell interpreter.

The implementation may reuse the existing bounded static shell segmentation and lexical tokenization needed for quoted literals, but it will not evaluate shell variables, substitutions, conditionals, pipes beyond the already admitted separators, or runtime filesystem state.

Rules:

- environment-variable assignments before an admitted command may be skipped;
- malformed quoting in a plausible candidate command → unresolved;
- unrelated command text such as `echo "pip install -e .[dev]"` → not observed;
- expressions in a material project path/extra/group → unresolved;
- an unrelated expression elsewhere must not erase a visible literal selection;
- negative uv selectors (`--no-extra`, `--no-group`) and project-target modifiers that materially alter the selected set are detected and conservatively unresolved in the first rule rather than silently ignored.

### 8.7 Working-directory ownership cleanup

Existing `dependency/direct_install.py` currently owns reusable working-directory resolution and bounded shell segmentation even though those mechanics are no longer direct-install-specific.

Cluster 3 will extract only those shared static workflow-context primitives into a narrowly named dependency-owned module, then migrate `direct_install.py` to consume them. This is not a new generic environment framework; it prevents duplicated GitHub working-directory precedence from drifting across two dependency observers and keeps `direct_install.py` narrow as required by the plan.

### 8.8 Deliberate non-claims

Cluster 3 does **not** establish:

```text
selected environment contains the changed package
uv.lock reachability/membership
resolver satisfiability
runtime command execution
successful environment formation
exact proposed version installed
package behavior exercised
CI coverage result
```

Those are later clusters.

### 8.9 Planned first implementation slice

1. extract shared effective-working-directory/path/segment mechanics from `direct_install.py` without changing its behavior;
2. add `dependency/environment_selection.py` with typed selectors/declarations/observation;
3. support the literal S011 pip-local-project extra form;
4. support explicit uv `--extra`, `--all-extras`, `--group`, `--only-group`, and `--all-groups` on bounded `uv sync` / `uv run` forms;
5. preserve multiple explicit selectors;
6. return unresolved for dynamic/materially unsupported project-selection modifiers;
7. add focused tests for S011, S001-style uv selectors, working-directory precedence, dynamic values, multiple selectors, quoted commands, false-positive guards, and unchanged direct-install behavior;
8. stop for local validation before Cluster 4.
