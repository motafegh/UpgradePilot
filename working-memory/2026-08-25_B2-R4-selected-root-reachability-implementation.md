# Working Memory — B2 R4 Selected-Root Reachability Implementation

**Date:** 2026-08-25  
**Status:** IMPLEMENTED TO STATIC/SOURCE-REVIEW DEPTH; LOCAL RUNTIME VALIDATION DEFERRED  
**Execution branch:** `main`  
**Current plan:** `../plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`

## 1. Bounded responsibility

R4 narrows the uv dependency proposition from broad selected-environment membership language to the fact the implementation actually proves:

```text
changed package from exact uv.lock
+ admitted explicit uv selector/scope
+ admitted exact lock structure
→ explicit selected-root reachability
```

The implementation deliberately does not claim complete uv environment formation, lock currentness, resolver satisfiability, command execution, installation success, runtime version observation, direct package exercise, or behavioral compatibility.

## 2. New preferred contract

New preferred owner:

```text
src/upgradepilot/dependency/uv_reachability.py
```

New public API:

```text
evaluate_uv_selected_root_reachability(...)
→ UvSelectedRootReachability
```

States:

```text
reachable
not_established
unresolved
```

Positive witness classification remains:

```text
direct | transitive
```

The exact meanings are now local to the reachability type rather than being implied by a broad environment-membership name.

## 3. `pyproject.toml` participation removed from this proposition

The new evaluator accepts:

```text
UvLockDependencyContext
+ ProjectEnvironmentSelectionDeclaration
+ exact uv.lock evidence
```

It no longer accepts exact `pyproject.toml` content.

Reasoning:

- the selection declaration already owns the selected project root and explicit selectors;
- the admitted lock already materializes local editable/virtual package source paths, selected optional/dev roots, and dependency edges;
- the former project-name/group-name cross-check did not establish project/lock currentness;
- project-source optional-extra/dependency-group evidence remains a separate responsibility and is not deleted from UpgradePilot;
- project/lock currentness remains a separate proposition.

The selected project root is now bound directly to exactly one local lock package by its editable/virtual source path relative to the lock root. Ambiguous/missing binding is `unresolved`.

## 4. Root semantics

Explicit selectors are resolved directly against roots materialized in the bound lock package:

```text
OptionalExtraSelector       → optional-dependencies[name]
DependencyGroupSelector     → dev-dependencies[name]
AllOptionalExtrasSelector   → all materialized optional-dependency roots
AllDependencyGroupsSelector → all materialized dev-dependency-group roots
```

`include` versus `only` remains preserved in the declaration. R4 does not interpret the rest of the command-selected environment because the proposition is only explicit selected-root reachability.

## 5. R3 scope semantics preserved

Proof asymmetry remains explicit:

```text
one unconditional selected-root witness
→ reachable

complete modeled bound-project root domain exhausted with no witness
→ not_established

all_workspace_packages + no bound-package witness
+ complete workspace root domain not exhausted
→ unresolved
  uv_selected_root_workspace_scope_not_exhausted
```

R4 does not enumerate guessed workspace members.

## 6. Universal-lock ambiguity and resource bounds preserved

Markers, resolution-scoped packages, unresolved/missing edges, activated-extra ambiguity, repeated-record ambiguity, traversal-state bound, and path-depth bound remain conservative:

```text
no unconditional witness + material ambiguity
→ unresolved
```

Direct/transitive witness paths are retained.

## 7. Migration boundary before R5

`uv_membership.py` remains temporarily because the existing Cluster-5 CI composition imports its legacy membership evidence type. R4 does not prematurely change that CI consumer; R5 owns the rebind.

The new preferred source topology now imports:

```text
upgradepilot.dependency.uv_reachability.evaluate_uv_selected_root_reachability
```

The new module currently reuses the already-tested reachability-specific lock projection helpers from `uv_membership.py`. This avoids creating a second external `uv.lock` structural interpretation during the staged migration. The remaining legacy/internal coupling is transitional and should be reconsidered when R5 migrates the CI consumer and the old membership surface can be retired or collapsed.

## 8. Focused regression added

New test owner:

```text
tests/test_uv_selected_root_reachability.py
```

It statically protects:

```text
S001-shaped transitive docs witness without pyproject input
direct selected-root witness
bounded not_established semantics
R3 all-workspace no-witness unresolved semantics
project-root → local-lock-package binding
missing selector → unresolved
all-groups roots sourced from uv.lock
marker-only path → unresolved
exact lock identity/unavailability → unresolved
```

`tests/test_source_topology.py` now names the new reachability API as the preferred responsibility owner.

## 9. Deliberately not changed

R4 does not implement:

```text
complete workspace member enumeration
complete uv environment interpretation
default groups/exclusions/conflicts/package targeting
project/lock currentness or resolver proof
CI consumption rebind (R5)
R6 real-case pressure
R7 final reconciliation acceptance
```

## 10. Validation state

Per user instruction, local runtime validation is intentionally deferred.

Current evidence:

```text
plan/audit/source responsibility trace          COMPLETE
new R4 source contract                          IMPLEMENTED
focused R4 tests                                IMPLEMENTED
preferred source-topology import                UPDATED
post-write connector source inspection          PASS to static review depth
local focused runtime                           DEFERRED
uv-focused regression discovery                 DEFERRED
complete standard suite                         DEFERRED
compileall                                      DEFERRED
```

No runtime PASS is claimed.

## 11. Learning loop state

Pre-implementation orientation was completed in conversation. The user explicitly requested the remaining explanation/ownership work after implementation.

Next learning closure should use the real R4 source/data flow:

```text
static uv command
→ ProjectEnvironmentSelectionDeclaration
→ selected project_root + selectors + package_scope

exact uv.lock
→ shared structural admission
→ project-root/local-package binding
→ selected roots
→ bounded graph traversal
→ reachable | not_established | unresolved
```

Then proceed to R5 only after the R4 post-implementation learning/ownership closure, unless the user explicitly redirects the sequence.
