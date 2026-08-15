# UpgradePilot Current Memory

**Last updated:** 2026-08-15  
**Authority:** Sole repository owner of live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Selected responsibility:** Phase E / Tranche 1 of [`plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_IMPLEMENTATION_PLAN.md`](plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_IMPLEMENTATION_PLAN.md).
- **Accepted architecture:** [`docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md`](docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md).
- **Current implementation evidence record:** [`working-memory/2026-08-15_B2-cross-responsibility-architecture-tranche-1-implementation.md`](working-memory/2026-08-15_B2-cross-responsibility-architecture-tranche-1-implementation.md).
- **Canonical product-decision semantics:** [`docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`](docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md).
- **Source ownership baseline:** [`docs/architecture/ADR-0007-responsibility-based-python-subpackages.md`](docs/architecture/ADR-0007-responsibility-based-python-subpackages.md).

### Current Phase-E status

```text
✓ Cluster 0 — synchronized green baseline
✓ Cluster 1 — PyYAML dependency/parser boundary
✓ Cluster 2 — typed static GitHub Actions workflow IR
✓ Cluster 3 — shared direct-install declaration observation

PAUSE — discussion / decision checkpoint

[ ] Cluster 4 — Target migration
[ ] Cluster 5 — CI migration / proof-claim narrowing
[ ] Cluster 6 — repository-path reconciliation
[ ] Cluster 7 — Tranche-1 acceptance gate
[ ] Tranche-1 stop/review
```

**Cluster 4 has not begun and is not currently selected for execution.** The approved plan still defines it as the next implementation responsibility if/when the user decides to resume.

**Learning mode:** deep learning/mastery, full current-system walkthrough, and real end-to-end data-flow study remain deferred until a meaningful implementation milestone. Proceed learning-by-doing when implementation resumes; explain prerequisites/reasoning just-in-time unless the user explicitly chooses a learning pause.

## Accepted architecture governing the work

```text
RepositoryTextFile
        ↓
bounded provider-specific GitHub Actions static workflow-definition IR
owner = upgradepilot.github
        ↓
   ┌────┴────┐
   ▼         ▼
  CI       Target
```

Runtime GitHub Actions evidence remains separate:

```text
WorkflowRun
WorkflowJob
WorkflowStep
```

Canonical proof boundary:

```text
static declaration
!= runtime execution
!= runtime success
!= environment formation
!= dependency exercise
```

The shared static representation owns bounded visible GitHub Actions source structure only. It does not own CI conclusions, Target conclusions, dependency exercise, exact target compatibility, or runtime-success claims.

## Verification truth

### Cluster 0 — green baseline

Validated baseline:

```text
branch: main
revision: 92e6ea6cb6dbfad7c50986d95e23de924a9b36c1
origin/main: same revision
worktree: clean
```

Migration-relevant focused regressions passed, followed by:

```text
Ran 403 tests in 0.256s
OK
```

Cluster 0 is **COMPLETED / GREEN BASELINE**.

### Cluster 1 — PyYAML parser boundary

Validated source-bearing revision:

```text
0d2c7f9eba08bd3c80f1b128d5b223b4e10a9667
```

Runtime dependency surface:

```text
requests>=2.32,<3
packaging>=26.2,<27
PyYAML>=6.0.3,<7
```

The parser boundary and dependency contract are validated green. Cluster 1 is **COMPLETED / GREEN**.

### Cluster 2 — static GitHub Actions workflow IR

Validated implementation revision:

```text
1e3027f87fa5b187c7d333472fe849aa6a49b049
```

The provider-owned typed static IR preserves the bounded GitHub Actions source structure required by ADR-0008 while keeping PyYAML nodes private and static/runtime evidence separate.

User-run WSL validation passed the focused/nearest gate and complete deterministic suite:

```text
Ran 416 tests in 0.087s
OK
```

Final branch/HEAD/origin were aligned on `main` and the worktree remained clean. Cluster 2 is **COMPLETED / GREEN**.

### Cluster 3 — direct-install declaration observation

Validated implementation revision:

```text
2980e22994216c069b2f4fb36dc31ea80398367f
```

Dependency-owned module:

```text
src/upgradepilot/dependency/direct_install.py
```

Entry point:

```text
observe_direct_installation_declaration(...)
```

It consumes the validated static `RunStepDefinition`, optional workflow/job `RunDefaults`, and an independently established repository-relative dependency source path.

Effective working-directory precedence:

```text
step
↓
job defaults.run
↓
workflow defaults.run
↓
repository root
```

Bounded result:

```text
observed | not_observed | unresolved
```

Dynamic/unsupported path context becomes `unresolved`; it is not converted into a fabricated negative. The primitive recognizes only admitted direct `pip` / `python -m pip` requirements-file declarations and stops at static declaration/configuration evidence.

Proof boundary:

```text
direct install declaration observed
!= command executed
!= command succeeded
!= environment formed
!= exact proposed dependency version installed
!= general dependency consumption
!= package exercise
```

User ran the requested fail-fast Cluster-3 validation gate. It covered:

```text
test_direct_install_declaration.py
test_source_topology.py
test_github_workflow_definition.py
test_identity_primitives.py
test_ci_dependency_exercise.py
test_target_artifact_environment.py
```

Because the fail-fast block reached its completion marker, all focused/nearest commands passed.

Complete deterministic suite:

```text
Ran 425 tests in 0.085s
OK
```

Final state:

```text
branch: main
HEAD: 2980e22994216c069b2f4fb36dc31ea80398367f
origin/main: 2980e22994216c069b2f4fb36dc31ea80398367f
worktree: clean
```

Therefore Cluster 3 is **COMPLETED / GREEN**.

## Current implementation foundation

The validated foundation through the current stop point is:

```text
exact repository workflow source
→ PyYAML bounded parser boundary
→ typed GitHub Actions static workflow IR
→ dependency-owned direct-install declaration observation
```

This foundation is validated independently before consumer migration.

## Remaining liabilities intentionally present

The following are not defects in the completed Clusters 0–3; they are remaining approved plan responsibilities:

- `target/artifact_environment.py` still uses its existing shallow static reader;
- Target still exposes runtime-sounding `dependency_environment_formation` semantics from static YAML;
- `ci/workflow_commands.py` still uses its existing shallow static reader;
- CI still exposes current bounded `state="proven"` semantics;
- no static↔runtime step correlation exists;
- duplicate GitHub-local repository-path validation remains;
- application orchestration remains Python-support-shaped.

## Current continuation

**STOP. Do not implement Cluster 4 or any later responsibility yet.**

The current selected action is discussion/review with the user at the validated Cluster-3 checkpoint. Cluster 4 — Target migration — remains the next item in the approved sequence only if the user later explicitly resumes implementation.

No new working-memory file is needed for this stop; the active Tranche-1 record already owns the implementation evidence and now records the validated Cluster-3 closure.

## Continuation-critical guards

- `MEMORY.md` alone owns current continuation/latest verification;
- latest validated implementation revision is `2980e22994216c069b2f4fb36dc31ea80398367f`;
- documentation commits after that revision may advance `main` without constituting new product/source validation;
- static IR structure is not runtime evidence;
- direct-install observation is dependency-owned and declaration-strength only;
- package invocation/exercise remains CI-specific;
- Target and CI migration remain separate consumer responsibilities;
- `not_observed` is not established absence;
- dynamic path context must remain unresolved;
- do not introduce a shell interpreter, generic dependency tracer, universal workflow engine, or broader abstraction without demonstrated need;
- Tranche 2 remains separate and must not start automatically;
- do not begin Cluster 4 until the user explicitly chooses to resume.

## Learning state

Current demonstrated depth remains substantial guided implementation exposure with repeated evidence-driven reasoning/debugging; no formal mastery assessment. Deep system/data-flow learning remains intentionally deferred until a meaningful milestone selected with the user.