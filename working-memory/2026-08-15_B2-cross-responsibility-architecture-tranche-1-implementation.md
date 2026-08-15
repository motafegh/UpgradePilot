# B2 Cross-Responsibility Architecture — Tranche 1 Implementation Record

**Date:** 2026-08-15  
**Operation:** Phase E / Tranche 1 — static workflow architecture implementation and migration  
**Result classification:** OPEN / progressive implementation evidence record  
**Validated product/source baseline:** `92e6ea6cb6dbfad7c50986d95e23de924a9b36c1` on `main`  
**Latest validated implementation revision:** `2980e22994216c069b2f4fb36dc31ea80398367f` on `main`  

## 1. Purpose and current operating mode

Preserve material implementation, debugging, findings, exact validation evidence, and cluster results while executing Tranche 1 of [`../plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_IMPLEMENTATION_PLAN.md`](../plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_IMPLEMENTATION_PLAN.md).

This file is an implementation evidence trail, not the live-state owner. `../MEMORY.md` alone owns current continuation.

Accepted durable architecture remains [`../docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md`](../docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md).

### Learning deferral decision

The user selected the learning-by-doing/building path and deferred broad mastery/system/data-flow teaching until a meaningful implementation milestone.

```text
build/validate cluster-by-cluster
→ explain only prerequisites/reasoning needed to proceed correctly
→ preserve learning questions/context
→ at a meaningful milestone, pause for deeper current-system + real-data-flow learning
```

### Source documentation rule

On 2026-08-15 the user explicitly requested better comments/docstrings in source code. The stable operating rule is now recorded in [`../OPERATING_GUIDE.md`](../OPERATING_GUIDE.md): new/materially modified source should document responsibility, proof boundaries, invariants, precedence/abstention logic, and non-obvious reasoning while avoiding comments that merely restate syntax.

## 2. Tranche-1 checklist

- [x] **Cluster 0 — synchronize and validate baseline**
- [x] **Cluster 1 — add PyYAML and prove parser dependency boundary**
- [x] **Cluster 2 — implement bounded GitHub Actions static workflow IR**
- [x] **Cluster 3 — implement shared direct-installation declaration observation**
- [ ] **Cluster 4 — migrate Target artifact-environment interpretation** — implementation written, validation pending
- [ ] **Cluster 5 — migrate CI static reading and narrow proof strength**
- [ ] **Cluster 6 — reconcile repository-path ownership drift**
- [ ] **Cluster 7 — Tranche-1 regression and acceptance gate**
- [ ] **Tranche-1 stop/review completed**

A checked cluster means its bounded objective and applicable validation were satisfied; code presence alone is insufficient.

## 3. Continuation-critical guards

```text
static declaration != execution != success
consumer unresolved != parser failure
multiple jobs / needs / source order != runtime environment continuity
workflow evidence != complete Target context
direct-install declaration != generic dependency consumption
package invocation/exercise remains CI-specific
static Actions evidence != runtime Actions evidence
Tranche 1 != automatic authorization for Tranche 2
```

Also:

- `RepositoryTextFile` remains authoritative raw source evidence;
- PyYAML nodes remain private parser machinery;
- dynamic/matrix/reusable/container structure must not become parser failure merely because a consumer cannot interpret it;
- no exact wheel-tag inference from broad workflow labels;
- material contradiction of ADR-0008 requires classification rather than silent architecture drift.

## 4. Cluster 0 — green baseline

**Status:** COMPLETED / GREEN BASELINE

User-run WSL preflight established exact clean baseline `92e6ea6cb6dbfad7c50986d95e23de924a9b36c1`, migration-relevant focused regressions passed, and the complete deterministic suite reported:

```text
Ran 403 tests in 0.256s
OK
```

### T1-F001 — clean pre-implementation source baseline

The Phase-E source baseline was reproduced green before parser/dependency changes.

## 5. Cluster 1 — PyYAML dependency/parser boundary

**Status:** COMPLETED / GREEN  
**Validated implementation revision:** `0d2c7f9eba08bd3c80f1b128d5b223b4e10a9667`

PyYAML became an explicit runtime dependency and `github/workflow_definition.py` established the private non-object-constructing representation-node boundary with controlled malformed/recursive handling.

The first post-change full suite exposed a stale exact dependency-contract expectation; the contract was deliberately updated to include PyYAML and user rerun evidence was green.

### T1-F002 — dependency-surface regression was protective, not brittle

```text
approved runtime dependency change
→ exact dependency contract fails
→ contract deliberately updated
→ dependency change cannot enter silently
```

## 6. Cluster 2 — bounded static GitHub Actions workflow IR

**Status:** COMPLETED / GREEN  
**Validated implementation revision:** `1e3027f87fa5b187c7d333472fe849aa6a49b049`

The provider-owned typed static IR preserves the bounded GitHub Actions structure required by ADR-0008 while keeping PyYAML nodes private and static/runtime evidence separate.

User-run WSL validation passed focused/nearest tests and:

```text
Ran 416 tests in 0.087s
OK
```

### T1-F003 — provider IR is independently green before consumer migration

```text
validated provider IR
!= migrated consumers
```

## 7. Cluster 3 — shared direct-install declaration observation

**Status:** COMPLETED / GREEN  
**Validated implementation revision:** `2980e22994216c069b2f4fb36dc31ea80398367f`

`src/upgradepilot/dependency/direct_install.py` now owns the bounded relation:

```text
RunStepDefinition
+ workflow/job/step working-directory context
+ independently established dependency source path
→ observed | not_observed | unresolved static direct-install declaration
```

Working-directory precedence is:

```text
step > job defaults.run > workflow defaults.run > repository root
```

Dynamic/unsafe higher-precedence path context remains unresolved rather than falling through to lower-precedence context. Proof strength stops at static declaration/configuration.

User-run fail-fast WSL validation covered the focused direct-install suite, source topology, retained provider IR, nearest CI/Target regressions, and the complete deterministic suite:

```text
Ran 425 tests in 0.085s
OK
```

Final state at validation:

```text
branch: main
HEAD: 2980e22994216c069b2f4fb36dc31ea80398367f
origin/main: same revision
worktree: clean
```

### T1-F004 — dependency-source declaration is now independently validated before consumer migration

The shared dependency primitive is green before Target/CI cutover, preserving blame isolation for later consumer migration failures.

## 8. Cluster 4 — Target migration and proof-strength correction

**Status:** IMPLEMENTATION WRITTEN / VALIDATION PENDING

### Expected

Migrate `target/artifact_environment.py` from its local indentation/regex workflow reader onto:

```text
RepositoryTextFile
→ shared GitHub Actions static IR
→ shared direct-install declaration observation
→ Target-specific interpretation
```

Correct the old runtime-sounding static-only contract:

```text
dependency_environment_formation
```

so static YAML no longer claims environment formation.

### Changes

`src/upgradepilot/target/artifact_environment.py` was rewritten as a consumer of:

```text
parse_workflow_definition(...)
observe_direct_installation_declaration(...)
```

The old local `_single_job`, indentation parsing, run extraction, pip regex matching, and literal-YAML interpretation helpers were removed from Target.

The Target evidence contract now uses:

```text
dependency_installation_declaration = observed | not_observed | unresolved
installation_declaration_source = static command text | None
```

This is intentionally declaration-strength only:

```text
observed static install declaration
!= command executed
!= command succeeded
!= environment formed
!= proposed version installed
!= package exercised
```

Target-specific interpretation remains local:

- literal scalar `runs-on` can establish a partial runner fact;
- `actions/setup-python@...` + literal `with.python-version` can establish a partial Python declaration fact;
- dynamic/structured runner or Python values remain limitations rather than fabricated literals;
- exact wheel compatibility remains `unresolved`;
- workflow evidence remains only one Target evidence source.

### Consumer-level abstention vs parser failure

The migration now relies on the shared IR to distinguish readable provider structure from Target limitations:

- multiple structurally readable jobs → `ambiguous_target_job_selection`;
- reusable-workflow job → `unsupported_target_job` because following the separate workflow source is outside this Target slice;
- matrix/strategy structure on a readable local steps job → partial evidence plus `strategy_context_not_interpreted`;
- container structure → partial evidence plus `container_context_not_interpreted`;
- shared provider definition problem → `workflow_definition_unreadable` with the provider reason/detail preserved.

Thus:

```text
provider structure readable but Target cannot finish proposition
!= shared parser failure
```

### Working-directory integration

Target passes workflow/job defaults plus each `RunStepDefinition` into the validated dependency observer. This means Target now inherits the already-proven precedence/path behavior rather than reimplementing it.

Dynamic effective working-directory context propagates to:

```text
dependency_installation_declaration = unresolved
```

rather than becoming `not_observed`.

### Source documentation improvement

The migrated Target module now includes responsibility/proof-boundary docstrings and comments around job selection, runner/setup-python interpretation, dependency observation composition, and unresolved precedence behavior, following the new operating-guide rule.

### Focused regression changes

`tests/test_target_artifact_environment.py` now covers:

- literal runner/Python + observed static install declaration;
- non-observed install remains nonfinal;
- dynamic setup-python version;
- `python-version` outside `with` is not a fact;
- multi-job Target-selection ambiguity rather than parser failure;
- matrix strategy preserved as Target limitation;
- container context preserved as Target limitation;
- workflow working-directory flowing through shared install observer;
- dynamic working-directory → unresolved install declaration;
- reusable-workflow Target abstention;
- malformed YAML flowing through the shared definition problem.

### Source/test commits

```text
67396ab1ec63b93cba3edddfa73d09ff9990f83a
→ Migrate Target artifact environment to shared workflow IR

670a34e5952bd87aa53b77bfb5f05d89a4d65b74
→ Update Target migration regressions
```

A separate operating-guide commit added the durable source documentation rule:

```text
902f430daf74836c3d0f5ec6c0d06bd821776388
→ Add source documentation guidance
```

### Current non-goals

Cluster 4 does not migrate or change:

```text
ci/workflow_commands.py
ci/dependency_exercise.py
runtime GitHub Actions evidence
repository-path ownership
application orchestration
```

### Validation

Pending user-run WSL focused/nearest/full gate.

### Cluster result

`PARTIAL / IMPLEMENTATION WRITTEN / VALIDATION PENDING`

Cluster 5 must not begin until Cluster 4 is green and explicitly closed.

## 9. Remaining plan responsibilities

- Cluster 5 — CI migration: **PENDING**
- Cluster 6 — repository-path ownership reconciliation: **PENDING**
- Cluster 7 — Tranche-1 acceptance gate: **PENDING**
- Tranche-1 stop/review: **PENDING**

Tranche 2 remains separately reviewed work and is outside this record.
