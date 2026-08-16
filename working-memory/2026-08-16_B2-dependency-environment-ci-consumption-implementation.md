# B2 Dependency Environment and CI Consumption Evidence — Implementation Record

**Date opened:** 2026-08-16  
**Operation:** bounded implementation of [`../plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md`](../plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md)  
**Result classification:** IN PROGRESS — CLUSTER 3 IMPLEMENTED / VALIDATION PENDING  
**Execution branch:** `main`  
**Validated Cluster-0 baseline:** `7444324e511b1e6fb49e6dba0bac371272bff7ba`  
**Validated Cluster-1 implementation revision:** `ef8b4aa623bb53356b0969d099d2e32ee250b3e9`  
**Validated Cluster-2 implementation revision:** `f3e226a27216f75a689b73acbc4404cafb53f1c1`  
**Cluster-3 source/test implementation point before this WM update:** `94239f480928625ddd52ea1832a6028425c37751`

## 1. Purpose and operating mode

Preserve the single progressive implementation, debugging, validation, learning, and decision trail for the selected Dependency Environment and CI Consumption Evidence responsibility. `../MEMORY.md` remains the sole live-state/continuation owner.

Core proof ladder:

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
- [ ] **Cluster 3 — bounded project-environment selection semantics** — IMPLEMENTED / VALIDATION PENDING
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
complete suite: 435 tests / OK
```

## 6. Cluster 1 — bounded dependency-environment evidence contract

**Status:** COMPLETED / GREEN  
**Validated revision:** `ef8b4aa623bb53356b0969d099d2e32ee250b3e9`

Stored truth became typed dependency source contexts. `direct_requirements_install_path` remains only as a derived compatibility projection.

```text
complete suite: 439 tests / OK
```

## 7. Cluster 2 — exact pyproject optional-extra transition evidence

**Status:** COMPLETED / GREEN  
**Validated revision:** `f3e226a27216f75a689b73acbc4404cafb53f1c1`

S011 can now produce:

```text
numpy 1.26.4 → 2.4.6
+
PyprojectOptionalExtraDependencyContext(extra="mlx")
```

using exact base/head source, strong provenance, `tomllib`, `packaging.Requirement`, conservative comparison, and neutral handling of unrelated pyproject metadata edits.

```text
complete suite: 452 tests / OK
```

## 8. Cluster 3 — bounded project-environment selection semantics

**Status:** IMPLEMENTED / VALIDATION PENDING

### 8.1 Owned proposition

> Given one provider-owned static `RunStepDefinition` plus an independently established exact `pyproject.toml` path, what project optional extras and dependency groups does the run declaration visibly select?

Output remains static declaration evidence:

```text
RunStepDefinition
+ workflow/job/step working-directory context
+ exact project file path
→ observed | not_observed | unresolved
→ typed project-environment selection declarations
```

### 8.2 Real pressure preserved

S011:

```text
pip install -e ".[dev]"
→ OptionalExtraSelector(name="dev")
```

This does **not** itself establish repository-wide absence of `mlx`, runtime installation, or changed-dependency consumption.

S001-style uv declarations:

```text
uv sync --group docs --all-extras
→ DependencyGroupSelector(name="docs", mode="include")
→ AllOptionalExtrasSelector()
```

The selector declaration still does **not** establish that Soup Sieve belongs to the selected environment; that is Cluster 4.

### 8.3 Standards/current-tool semantics checked before implementation

Current official uv command semantics confirm explicit positive selectors such as `--extra`, `--all-extras`, `--group`, `--only-group`, and `--all-groups`; uv also has default dependency-group behavior. Therefore omission of a selector is not treated as a negative fact.

Python packaging extra names and standardized dependency-group names are normalized before comparison. Source/command spelling is preserved for explanation while normalized identities are exposed for later matching.

### 8.4 New shared static workflow context

Created:

```text
src/upgradepilot/dependency/workflow_context.py
```

It owns only dependency-side reusable static mechanics:

```text
step > job defaults.run > workflow defaults.run > repository root
safe repository-relative path resolution
bounded shell-segment splitting
```

It does not own GitHub parsing, filesystem existence, shell execution, or runtime state.

`dependency/direct_install.py` was migrated to consume these helpers without changing its public observation semantics. It continues to re-export its previously visible working-directory types for compatibility.

This extraction prevents the direct-requirements observer and project-environment observer from drifting on working-directory precedence while keeping `direct_install.py` narrow.

### 8.5 New project-environment selector observer

Created:

```text
src/upgradepilot/dependency/environment_selection.py
```

Main entry:

```python
observe_project_environment_selection(
    step,
    *,
    project_file_path,
    workflow_defaults=None,
    job_defaults=None,
)
```

Typed selectors:

```text
OptionalExtraSelector(name)
DependencyGroupSelector(name, mode=include|only)
AllOptionalExtrasSelector()
AllDependencyGroupsSelector()
```

Each observed declaration preserves:

```text
manager: pip | uv
operation: install | sync | run
static shell-segment index
bound project root
explicit positive selectors
```

The overall observation preserves:

```text
observed | not_observed | unresolved
```

and may keep known literal declarations/selectors even when another material selector/path forces the overall state to unresolved.

### 8.6 Bounded pip semantics

Admitted local-project forms include the real S011 shape and equivalent literal local project requirements, for example:

```text
pip install -e ".[dev]"
pip install ".[mlx]"
python -m pip install ".[dev,mlx]"
```

The local project path is resolved against effective working-directory context and must bind to the independently established project root.

Dynamic project/extra text or dynamic effective working-directory context is unresolved. Echoed command text is not treated as a declaration.

### 8.7 Bounded uv semantics

Admitted commands are explicit selectors on bounded:

```text
uv sync ...
uv run ...
```

Positive selectors currently preserved:

```text
--extra NAME
--all-extras
--group NAME
--only-group NAME
--all-groups
```

Literal `--project` can bind a subproject when the path resolves safely. Without `--project`, the first rule requires the effective working directory to equal the independently established project root; parent/nested project discovery remains unresolved rather than guessed.

Negative/target-changing forms such as `--no-extra`, `--no-group`, `--directory`, `--package`, and `--no-project` are detected conservatively and make the first bounded result unresolved instead of being silently ignored.

For `uv run`, only uv's option prefix before the invoked command is interpreted. Child-command arguments such as:

```text
uv run --extra mlx pytest --no-group application-argument
```

do not turn pytest's `--no-group` argument into uv environment semantics.

A bound `uv sync`/`uv run` with no explicit positive extra/group selector is unresolved rather than `not_observed`, because default-group selection requires project/config evidence.

### 8.8 Implementation corrections found during the slice

Two useful issues were caught before validation:

1. **S011 lexical root-extra form** — the first local-path predicate recognized `.` and `./path[...]` but missed the actual `.[dev]` spelling. It was corrected so the real S011 declaration is admitted.
2. **Environment-name identity** — exact spelling cannot be the comparison identity for extras/groups. `PyprojectOptionalExtraDependencyContext`, `PyprojectDependencyGroupContext`, `OptionalExtraSelector`, and `DependencyGroupSelector` now preserve original spelling and expose normalized names for later composition.

### 8.9 Test pressure added/updated

`tests/test_project_environment_selection.py` covers:

- real S011 `.[dev]` declaration;
- multiple pip extras;
- local project without extras through editable install;
- effective working-directory binding;
- dynamic working directory and dynamic extra;
- false-positive echo guard;
- S001-style uv group + all-extras;
- `--only-group` / all-groups selector preservation;
- `uv run --extra` before child command;
- child-command flags not interpreted as uv selectors;
- uv command with no explicit selector remaining unresolved;
- dynamic uv group;
- literal `--project` binding;
- unresolved parent/nested project discovery;
- negative selector conservative handling;
- multiple static shell segments and segment indices;
- unrelated expressions not erasing literal selection;
- malformed quoting;
- invalid project-file boundary;
- normalized extra/group selector identity.

`tests/test_dependency_environment.py` now protects normalized source-context environment names.

`tests/test_source_topology.py` protects the new dependency-owned observer import.

Existing `tests/test_direct_install_declaration.py` remains the regression guard for the extracted shared working-directory/path mechanics.

### 8.10 Deliberate non-claims

Cluster 3 still does **not** establish:

```text
selected environment contains changed dependency
uv.lock membership/reachability
resolver satisfiability
runtime command execution
successful environment formation
exact proposed version installed
package behavior exercised
CI coverage/exercise result
```

### 8.11 Validation gate

Current source/test implementation point before this WM update:

```text
94239f480928625ddd52ea1832a6028425c37751
```

Cluster 3 is not complete until the new selector tests, shared-context/direct-install regressions, dependency/CI/application nearest tests, and the complete deterministic suite are green on synchronized clean `main`.

**Do not start Cluster 4 before that validation is recorded here.**
