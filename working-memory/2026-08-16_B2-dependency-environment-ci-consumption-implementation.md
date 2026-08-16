# B2 Dependency Environment and CI Consumption Evidence — Implementation Record

**Date opened:** 2026-08-16  
**Operation:** bounded implementation of [`../plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md`](../plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md)  
**Result classification:** IN PROGRESS — CLUSTER 4 COMPLETE / GREEN; CLUSTER 5 NOT STARTED  
**Execution branch:** `main`  
**Validated Cluster-0 baseline:** `7444324e511b1e6fb49e6dba0bac371272bff7ba`  
**Validated Cluster-1 implementation revision:** `ef8b4aa623bb53356b0969d099d2e32ee250b3e9`  
**Validated Cluster-2 implementation revision:** `f3e226a27216f75a689b73acbc4404cafb53f1c1`  
**Validated Cluster-3 implementation revision:** `82fdf314e3361f90ab8fd3862247d4bd895a440d`  
**Validated Cluster-4 implementation revision:** `cf2b4ca1a78c6cd008a9c55cb502ed5072647561`

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
- [x] **Cluster 4 — bounded `uv.lock` selected-environment membership/reachability**
- [ ] **Cluster 5 — CI migration to typed consumption evidence** — NOT STARTED / HOLD
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

Cluster 3 established only the static selection side of the later consumption proposition:

```text
RunStepDefinition
+ exact project file path
+ effective working-directory context
→ observed | not_observed | unresolved
→ typed project-environment selection declarations
```

Accepted examples:

```text
pip install -e ".[dev]"
→ OptionalExtraSelector("dev")

uv sync --group docs --all-extras
→ DependencyGroupSelector("docs")
→ AllOptionalExtrasSelector()
```

Shared `dependency/workflow_context.py` owns effective working-directory precedence, safe repository-relative path resolution, and bounded shell segmentation. Cluster 3 preserves normalized environment-name identity, separates uv options from `uv run` child-command arguments, binds literal project roots, and leaves dynamic/default/ambiguous selection unresolved.

```text
complete deterministic suite: 476 tests / OK
HEAD/origin:                  82fdf314e3361f90ab8fd3862247d4bd895a440d
worktree:                     clean
```

## 9. Cluster 4 — bounded uv selected-environment membership/reachability

**Status:** COMPLETED / GREEN  
**Validated revision:** `cf2b4ca1a78c6cd008a9c55cb502ed5072647561`

### 9.1 Owned proposition

> Given exact-head uv project metadata, exact-head `uv.lock`, one changed package from `UvLockDependencyContext`, and one static uv environment-selection declaration, can UpgradePilot establish direct or transitive reachability from the explicitly selected dependency group/optional extra?

Result states:

```text
member
├─ direct | transitive
└─ deterministic witness root/path

not_established
→ complete traversal of bounded explicit roots found no witness
→ NOT repository/runtime absence

unresolved
→ exact source/project binding, selector roots, lock structure,
  markers/forks, activated extras, or traversal safety is insufficient
```

### 9.2 Real S001 proof pressure

Frozen exact S001 evidence establishes:

```text
workflow declaration:
uv sync --all-packages --group docs

exact project metadata:
[dependency-groups].docs includes mkdocs-llmstxt

exact uv.lock:
pydantic package.dev-dependencies.docs
→ mkdocs-llmstxt

mkdocs-llmstxt
→ beautifulsoup4

beautifulsoup4
→ soupsieve 2.8.4
```

So the accepted witness is genuinely transitive:

```text
docs
→ mkdocs-llmstxt
→ beautifulsoup4
→ soupsieve
```

This proves why `soupsieve` merely appearing somewhere in `uv.lock` or merely scanning direct docs entries would be insufficient.

### 9.3 New dependency-owned source

Created:

```text
src/upgradepilot/dependency/uv_membership.py
```

Main entry:

```python
evaluate_uv_selected_environment_membership(
    context,
    declaration,
    *,
    project_file,
    lock_file,
)
```

The function consumes existing typed facts rather than reparsing workflow YAML or rediscovering the dependency transition.

### 9.4 Exact source/provenance gate

Before graph reasoning the implementation requires:

- declaration manager is `uv` and has explicit positive selectors;
- exact project and lock sources are available;
- normalized `pyproject.toml` / `uv.lock` paths;
- repository and immutable revision match `UvLockDependencyContext`;
- lock path/revision/blob/byte count match the exact source evidence that established the changed dependency;
- exact project/lock byte evidence is internally coherent;
- declaration project root matches the supplied project source.

Mismatch returns `unresolved`, never a guessed repair.

### 9.5 Exact project / workspace binding

The implementation parses project metadata only far enough to establish:

```text
[project].name
[project.optional-dependencies] names
[dependency-groups] names
```

It validates these as structured TOML surfaces and preserves normalized environment-name identity.

The exact project is then bound to exactly one lock workspace package by:

```text
normalized project distribution name
+
editable/virtual source path relative to the uv.lock workspace root
```

This supports the repository-root project and bounded nested workspace members without implementing generic uv workspace command semantics.

### 9.6 Selected environment roots

The project metadata validates that the selected extra/group exists. The bound workspace package in `uv.lock` provides resolved root package edges through:

```text
package.optional-dependencies
package.dev-dependencies
```

Admitted Cluster-3 selectors:

```text
OptionalExtraSelector
DependencyGroupSelector
AllOptionalExtrasSelector
AllDependencyGroupsSelector
```

Using lock-materialized group roots avoids reimplementing full PEP 735 include-group expansion while still requiring exact project metadata to establish the environment identity.

This cross-file consistency is not a resolver-currentness claim; Cluster 7/AUDIT-004 retains that separate question.

### 9.7 Graph traversal semantics

Each lock package record preserves normalized package identity, version/source identity, resolution markers, dependencies, optional-dependencies, and dev-dependencies. Each dependency edge preserves package identity plus optional version/source discriminator, marker, and activated extras.

Activated extras matter because a lock edge such as a dependency on `package[imaging]` changes which outgoing optional-dependency roots must be traversed.

Traversal is iterative, bounded, and cycle-safe:

```text
_MAX_VISITED_STATES = 10_000
_MAX_PATH_DEPTH = 100
```

Crossing a guard is `unresolved`, not negative evidence.

### 9.8 Universal-lock fork/marker safety

A positive witness requires both unmarked dependency edges and unscoped package records throughout the witness path.

Current first rule:

- marked dependency edge → conditional branch, do not traverse as unconditional;
- package record with `resolution-markers` → conditional branch;
- repeated normalized package records require version/source identity to select exactly one record;
- ambiguous repeated record → do not union branches;
- if an unconditional witness exists elsewhere, it may still prove positive membership;
- if no unconditional witness exists and any selected branch is conditional/ambiguous, result is `unresolved`;
- only a completely traversed explicit-root graph without such ambiguity may return `not_established`.

No marker evaluator is implemented.

### 9.9 Direct versus transitive witness

```text
direct
= changed package is itself one explicit selected extra/group root

transitive
= changed package is reached through >=1 exact lock dependency edge
```

A deterministic witness is preserved for explanation:

```text
witness_root
witness_path
```

S001-shaped witness:

```text
witness_root = mkdocs-llmstxt
witness_path = mkdocs-llmstxt → beautifulsoup4 → soupsieve
```

### 9.10 Test pressure

Cluster-4 tests cover:

- S001-shaped transitive docs membership;
- direct selected-root membership;
- `not_established` versus absence;
- marker-dependent path → unresolved;
- package-level `resolution-markers`;
- activated dependency-extra traversal;
- selected optional-extra roots;
- all-groups/all-extras explicit root union;
- selected group missing from exact project/lock evidence;
- repeated intermediate package ambiguity;
- version-discriminated repeated record;
- cycle safety;
- nested workspace-member binding;
- exact lock blob identity mismatch;
- source-topology ownership.

### 9.11 Deliberate non-claims

Cluster 4 still does **not** establish:

```text
lock is resolver-current against pyproject
resolver constraints are satisfiable
uv command executed
selected environment formed successfully
exact proposed package version installed at runtime
package behavior exercised
CI coverage/exercise result
static↔runtime step correlation
```

No `uv`, project code, investigated dependency, resolver, or external command is executed by this capability.

### 9.12 Validation truth

The user ran the documented strict Cluster-4 validation on synchronized `main`. The block reached the complete-suite/final-state markers, therefore import smoke, focused membership/universal-lock tests, and nearest uv/dependency/CI/application regressions passed before the visible final result.

```text
complete deterministic suite: 490 tests / OK
HEAD:                         cf2b4ca1a78c6cd008a9c55cb502ed5072647561
origin/main:                  same
worktree:                     clean
```

Cluster 4 satisfies its bounded objective and is accepted green at `cf2b4ca1a78c6cd008a9c55cb502ed5072647561`.

## 10. Cluster 5 — not started

**Status:** NOT STARTED / HOLD

Next bounded question when explicitly resumed:

> How should CI consume the typed dependency source/environment-selection/membership evidence from Clusters 1–4, while preserving the separation between static dependency consumption, runtime CI evidence, and actual package exercise?

Do not start Cluster 5 until the user explicitly resumes.
