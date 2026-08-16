# B2 Dependency Environment and CI Consumption Evidence — Implementation Record

**Date opened:** 2026-08-16  
**Operation:** bounded implementation of [`../plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md`](../plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md)  
**Result classification:** IN PROGRESS — CLUSTER 3 COMPLETE / GREEN; CLUSTER 4 NOT STARTED  
**Execution branch:** `main`  
**Validated Cluster-0 baseline:** `7444324e511b1e6fb49e6dba0bac371272bff7ba`  
**Validated Cluster-1 implementation revision:** `ef8b4aa623bb53356b0969d099d2e32ee250b3e9`  
**Validated Cluster-2 implementation revision:** `f3e226a27216f75a689b73acbc4404cafb53f1c1`  
**Validated Cluster-3 implementation revision:** `82fdf314e3361f90ab8fd3862247d4bd895a440d`

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
- [x] **Cluster 3 — bounded project-environment selection semantics**
- [ ] **Cluster 4 — bounded `uv.lock` selected-environment membership/reachability** — NOT STARTED / HOLD
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

**Status:** COMPLETED / GREEN  
**Validated revision:** `82fdf314e3361f90ab8fd3862247d4bd895a440d`

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

For `uv run`, only uv's option prefix before the invoked command is interpreted. Child-command arguments do not become uv environment selectors.

A bound `uv sync`/`uv run` with no explicit positive extra/group selector is unresolved rather than `not_observed`, because default-group selection requires project/config evidence.

### 8.8 Implementation corrections found during the slice

Four useful corrections were made before validation:

1. **S011 lexical root-extra form** — the first local-path predicate recognized `.` and `./path[...]` but missed the actual `.[dev]` spelling. It was corrected so the real S011 declaration is admitted.
2. **Environment-name identity** — exact spelling cannot be the comparison identity for extras/groups. Source contexts and selectors preserve original spelling while exposing normalized names for later composition.
3. **uv child-command scope** — material uv flags are inspected only inside uv's own option prefix for `uv run`; child-command arguments cannot accidentally become uv environment selectors.
4. **Test-contract cleanup** — normalization tests no longer fabricate a future dependency-group source-evidence format, and `--only-group` / `--all-groups` are tested independently.

### 8.9 Validation truth

The user ran the strict validation inside the documented subshell after synchronizing `main`. The validation reached the complete-suite/final-state markers, therefore Cluster-3 import smoke, focused selector/shared-context/direct-install tests, and nearest dependency/CI/application regressions passed before the visible final result.

```text
complete deterministic suite: 476 tests / OK
HEAD:                         82fdf314e3361f90ab8fd3862247d4bd895a440d
origin/main:                  same
worktree:                     clean
```

The previous VS Code/zsh `RPROMPT` warning did not recur. This confirms the subshell validation wrapper prevented `set -u` / `NOUNSET` from leaking into the parent interactive shell.

### 8.10 Cluster-3 conclusion

Cluster 3 satisfies its bounded objective and is accepted green at `82fdf314e3361f90ab8fd3862247d4bd895a440d` with `476 tests / OK`.

It now establishes the static **selection side** of the later consumption proposition:

```text
Cluster 2: affected environment identity
Cluster 3: workflow-selected environment identity
Cluster 4: selected-environment membership/reachability — not started
```

### 8.11 Deliberate non-claims

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

## 9. Cluster 4 — not started

**Status:** NOT STARTED / HOLD

Next bounded question when explicitly resumed:

> Given exact uv project/lock evidence plus a static selected project/group/extra proposition, can UpgradePilot establish whether the changed normalized package is a direct or transitive member/reachable package of that selected environment without flattening universal-lock marker/platform/Python forks?

Do not start Cluster 4 until the user explicitly resumes.
