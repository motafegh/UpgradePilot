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
→ Cluster 3 — shared direct-install declaration observation
[ ] Cluster 4 — Target migration
[ ] Cluster 5 — CI migration / proof-claim narrowing
[ ] Cluster 6 — repository-path reconciliation
[ ] Cluster 7 — Tranche-1 acceptance gate
[ ] Tranche-1 stop/review
```

**Learning mode:** deep learning/mastery, full current-system walkthrough, and real end-to-end data-flow study remain deliberately deferred until a meaningful implementation milestone. Proceed learning-by-doing; explain only prerequisites/reasoning needed to build or decide correctly unless the user asks to pause and learn.

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

`src/upgradepilot/github/workflow_definition.py` established the private BaseLoader representation-node boundary, controlled parse failure, and bounded recursion/depth/node traversal. After one deliberately repaired stale dependency-contract expectation, the user reran the dependency contract, focused parser tests, and complete deterministic suite and reported all green.

Cluster 1 is **COMPLETED / GREEN**.

### Cluster 2 — static GitHub Actions workflow IR

Validated implementation revision:

```text
1e3027f87fa5b187c7d333472fe849aa6a49b049
```

The provider-owned typed static IR now exists in `src/upgradepilot/github/workflow_definition.py` and preserves the bounded GitHub Actions structure required by ADR-0008: authoritative source, run defaults, ordered jobs/steps, `needs`, `runs-on`, conditions, `continue-on-error`, strategy/matrix and container fragments, reusable-workflow shape, run/uses steps, bounded `with` mappings, source indices/spans, expression presence, and scoped structural problems.

The old CI/Target readers are intentionally still present; Cluster 2 proves only the shared provider responsibility, not consumer migration.

User-run WSL validation at exact `1e3027f...` passed the focused/nearest gate:

```text
test_github_workflow_definition.py
test_source_topology.py
test_github_actions.py
test_exact_commit_repository_files.py
test_ci_dependency_exercise.py
test_target_artifact_environment.py
```

Complete deterministic suite:

```text
Ran 416 tests in 0.087s
OK
```

Final state:

```text
branch: main
HEAD: 1e3027f87fa5b187c7d333472fe849aa6a49b049
origin/main: same revision
worktree: clean
```

Therefore Cluster 2 is **COMPLETED / GREEN**.

## Current implementation truth and remaining liabilities

The shared provider IR is now validated, but consumers have not yet migrated:

- `ci/workflow_commands.py` still has its old shallow static reader;
- `target/artifact_environment.py` still has its old shallow static reader;
- Target still exposes runtime-sounding `dependency_environment_formation` semantics from static YAML;
- CI still exposes current bounded `state="proven"` semantics;
- no static↔runtime step correlation exists;
- duplicate GitHub-local repository-path validation remains;
- application orchestration remains Python-support-shaped.

These remain later plan responsibilities and do not invalidate Cluster 2.

## Selected next responsibility — Cluster 3

Implement the shared dependency-owned direct-installation declaration observation only now that the static IR is validated.

Conceptual input:

```text
static run command
+ effective workflow/job/step working-directory context
+ independently established repository-relative dependency-source path
```

Conceptual result:

```text
direct installation declaration observed
or
not observed / unresolved under bounded interpretation
```

The primitive may recognize the currently admitted direct `pip` / `python -m pip` requirements-file forms and must account for workflow/job/step `working-directory` precedence.

Its proof strength stops at declaration/configuration:

```text
direct install declaration observed
!= command executed
!= command succeeded
!= exact proposed dependency version installed
!= general dependency consumption
!= package exercise
```

Package invocation/exercise remains CI-specific. Do not migrate Target or CI in Cluster 3; those are Clusters 4 and 5.

## Immediate project action

Proceed with **Cluster 3 only**: implement and focused-test the dependency-owned direct-install declaration primitive against the validated static workflow IR. Preserve literal/dynamic working-directory uncertainty and repository-path safety. After the implementation is written, run a focused/nearest/full validation gate before selecting Cluster 4.

## Continuation-critical guards

- `MEMORY.md` alone owns current continuation/latest verification;
- current validated implementation revision is `1e3027f87fa5b187c7d333472fe849aa6a49b049`;
- later documentation commits may advance `main` without constituting new product/source validation;
- PyYAML parser nodes remain internal syntax machinery;
- static IR structure is not runtime evidence;
- `needs`/source order do not prove environment continuity;
- direct-install declaration must remain dependency-owned and declaration-strength only;
- package invocation/exercise remains CI-specific;
- Target/CI consumer migration must not be pulled into Cluster 3;
- `not_observed` is not established absence;
- dynamic values must not be silently treated as literals;
- do not introduce a shell interpreter, generic dependency tracer, universal workflow engine, or broader abstraction without demonstrated need;
- Tranche 2 remains separate and must not start automatically.

## Learning state

Current demonstrated depth remains substantial guided implementation exposure with repeated evidence-driven reasoning/debugging; no formal mastery assessment. Deep system/data-flow learning is intentionally deferred until the next meaningful implementation milestone.