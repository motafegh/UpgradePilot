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
→ Cluster 3 — direct-install declaration observation: implementation written, validation pending
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

The parser boundary and dependency contract are validated green. Cluster 1 is **COMPLETED / GREEN**.

### Cluster 2 — static GitHub Actions workflow IR

Validated implementation revision:

```text
1e3027f87fa5b187c7d333472fe849aa6a49b049
```

The provider-owned typed static IR now preserves the bounded GitHub Actions source structure required by ADR-0008 while keeping PyYAML nodes private and static/runtime evidence separate.

User-run WSL validation passed the focused/nearest gate and complete deterministic suite:

```text
Ran 416 tests in 0.087s
OK
```

Final branch/HEAD/origin were aligned on `main` and the worktree remained clean. Therefore Cluster 2 is **COMPLETED / GREEN**.

## Current implementation truth

### Cluster 3 — implementation written, validation pending

New dependency-owned module:

```text
src/upgradepilot/dependency/direct_install.py
```

Entry point:

```text
observe_direct_installation_declaration(...)
```

It consumes `RunStepDefinition` plus optional workflow/job `RunDefaults` and one independently established repository-relative dependency source path.

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

The bounded result is:

```text
observed | not_observed | unresolved
```

and preserves the effective working-directory state/source plus matched requirements argument when observed.

Admitted direct forms begin with `pip`/`pip3` or `python[3] -m pip install` and inspect `-r` / `--requirement` paths only. Relative requirement paths are resolved against the effective working directory only when that context is statically safe. Dynamic/unsupported path context becomes `unresolved`, not a fabricated negative.

Proof strength remains:

```text
direct install declaration observed
!= command executed
!= command succeeded
!= environment formed
!= exact proposed dependency version installed
!= general dependency consumption
!= package exercise
```

New focused tests:

```text
tests/test_direct_install_declaration.py
```

plus source-topology protection for the dependency owner.

Current Cluster-3 source/test commits:

```text
465ccd9e4b5ecf62728c5472294d80f6487d2e41
1cb72f7506e68dbe9de57047fcb5ff0062542788
2b4cc976c3bfe014a061e4e63f5cce5e219f719a
```

No Target or CI migration has begun. Cluster 4 is not selected until Cluster 3 is validated and closed.

## Remaining liabilities intentionally present

- `ci/workflow_commands.py` still has its old shallow static reader;
- `target/artifact_environment.py` still has its old shallow static reader;
- Target still exposes runtime-sounding `dependency_environment_formation` semantics from static YAML;
- CI still exposes current bounded `state="proven"` semantics;
- no static↔runtime step correlation exists;
- duplicate GitHub-local repository-path validation remains;
- application orchestration remains Python-support-shaped.

These are later plan responsibilities, not Cluster-3 defects.

## Immediate project action

Validate Cluster 3 before any Target migration. Required gate: focused direct-install tests, source topology, retained static-workflow IR tests, nearest current CI/Target regressions, complete deterministic suite, and clean aligned worktree.

If green, close Cluster 3 and then select Cluster 4. If failures appear, classify them within Cluster 3 before touching Target/CI migration.

## Continuation-critical guards

- `MEMORY.md` alone owns current continuation/latest verification;
- latest validated implementation revision remains `1e3027f87fa5b187c7d333472fe849aa6a49b049` until Cluster 3 is validated;
- later documentation commits may advance `main` without constituting new product/source validation;
- static IR structure is not runtime evidence;
- direct-install observation is dependency-owned and declaration-strength only;
- package invocation/exercise remains CI-specific;
- Target/CI consumer migration must not be pulled into Cluster 3;
- `not_observed` is not established absence;
- dynamic path context must remain unresolved;
- do not introduce a shell interpreter, generic dependency tracer, universal workflow engine, or broader abstraction without demonstrated need;
- Tranche 2 remains separate and must not start automatically.

## Learning state

Current demonstrated depth remains substantial guided implementation exposure with repeated evidence-driven reasoning/debugging; no formal mastery assessment. Deep system/data-flow learning is intentionally deferred until the next meaningful implementation milestone.