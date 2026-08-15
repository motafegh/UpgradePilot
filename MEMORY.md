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
- **Execution/learning/code-documentation rules:** [`OPERATING_GUIDE.md`](OPERATING_GUIDE.md).

### Current Phase-E status

```text
✓ Cluster 0 — synchronized green baseline
✓ Cluster 1 — PyYAML dependency/parser boundary
✓ Cluster 2 — typed static GitHub Actions workflow IR
✓ Cluster 3 — shared direct-install declaration observation
→ Cluster 4 — Target migration: implementation written, validation pending
[ ] Cluster 5 — CI migration / proof-claim narrowing
[ ] Cluster 6 — repository-path reconciliation
[ ] Cluster 7 — Tranche-1 acceptance gate
[ ] Tranche-1 stop/review
```

**Learning mode:** continue learning-by-doing/building. Deep mastery, full current-system walkthrough, and real end-to-end data-flow study remain deferred until a meaningful implementation milestone. Explain only prerequisites/reasoning needed to build or decide correctly unless the user requests a learning pause.

**Source documentation rule:** new/materially modified source should include useful docstrings/comments that explain responsibility, proof boundaries, invariants, precedence/abstention behavior, or other non-obvious reasoning. Avoid comments that merely restate syntax. Improve older nearby documentation proportionately when touching it rather than starting broad comment-only refactors.

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

Validated baseline `92e6ea6cb6dbfad7c50986d95e23de924a9b36c1`; focused regressions passed and:

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

The parser boundary and explicit PyYAML dependency contract are validated green. Cluster 1 is **COMPLETED / GREEN**.

### Cluster 2 — static GitHub Actions workflow IR

Validated implementation revision:

```text
1e3027f87fa5b187c7d333472fe849aa6a49b049
```

User-run WSL focused/nearest validation and complete deterministic suite passed:

```text
Ran 416 tests in 0.087s
OK
```

Cluster 2 is **COMPLETED / GREEN**.

### Cluster 3 — direct-install declaration observation

Validated implementation revision:

```text
2980e22994216c069b2f4fb36dc31ea80398367f
```

The dependency-owned observer consumes the provider IR, respects step > job > workflow > repository-root working-directory precedence, and returns `observed | not_observed | unresolved` at static declaration strength only.

User-run fail-fast validation covered focused direct-install, source topology, retained provider IR, nearest CI/Target regressions, and:

```text
Ran 425 tests in 0.085s
OK
```

Final validation state was aligned `main`, `HEAD == origin/main == 2980e229...`, and clean worktree. Cluster 3 is **COMPLETED / GREEN**.

## Current implementation truth — Cluster 4

Cluster 4 source/tests are written but **not yet runtime-validated**.

### Target consumer migration

`src/upgradepilot/target/artifact_environment.py` now consumes:

```text
parse_workflow_definition(...)
observe_direct_installation_declaration(...)
```

instead of owning a second indentation/regex workflow reader and a second pip requirements matcher.

The old static-only runtime-sounding contract:

```text
dependency_environment_formation = established | not_observed
```

has been replaced in active source by:

```text
dependency_installation_declaration = observed | not_observed | unresolved
installation_declaration_source = static command text | None
```

This is a proof-strength correction:

```text
observed static install declaration
!= command executed
!= command succeeded
!= environment formed
!= exact proposed version installed
!= package exercised
```

### Target-specific interpretation retained

Target still owns interpretation of Target-relevant declarations:

- one literal scalar `runs-on` can establish a partial runner fact;
- one literal `actions/setup-python@...` `with.python-version` can establish a partial Python declaration fact;
- dynamic/structured values remain limitations rather than fabricated literals;
- exact wheel compatibility remains unresolved unless independently established;
- workflow evidence remains one Target evidence source rather than the complete Target model.

### Readable provider structure vs Target limitations

The migrated code now treats:

```text
multiple readable jobs
→ ambiguous_target_job_selection

reusable-workflow job
→ unsupported_target_job

matrix/strategy structure
→ partial evidence + strategy_context_not_interpreted

container structure
→ partial evidence + container_context_not_interpreted
```

These are Target-level limitations/abstentions, not shared parser failures.

Dynamic effective working-directory context from the shared dependency observer becomes:

```text
dependency_installation_declaration = unresolved
```

rather than a fabricated `not_observed` state.

### Cluster-4 source/test commits

```text
67396ab1ec63b93cba3edddfa73d09ff9990f83a
→ Migrate Target artifact environment to shared workflow IR

670a34e5952bd87aa53b77bfb5f05d89a4d65b74
→ Update Target migration regressions
```

The stable source-documentation rule was added separately:

```text
902f430daf74836c3d0f5ec6c0d06bd821776388
→ Add source documentation guidance
```

No CI migration, repository-path cleanup, runtime correlation, or orchestration work has been started in Cluster 4.

## Immediate project action

**Validate Cluster 4 before beginning Cluster 5.**

Required gate should cover:

```text
test_target_artifact_environment.py
+ test_github_workflow_definition.py
+ test_direct_install_declaration.py
+ test_source_topology.py
+ retained artifact-serviceability/Target-nearest regressions
+ current CI regression (unchanged consumer)
+ complete deterministic suite
+ clean aligned worktree
```

If green, close Cluster 4 and only then select Cluster 5. If failures appear, classify them inside the Target migration before changing CI.

## Continuation-critical guards

- `MEMORY.md` alone owns current continuation/latest verification;
- latest validated implementation revision remains `2980e22994216c069b2f4fb36dc31ea80398367f` until Cluster 4 is validated;
- later source/documentation commits may advance `main` without constituting new validation;
- Target no longer owns YAML/GitHub Actions parsing or generic direct-install recognition in the migrated source;
- static Target declaration evidence must not be described as runtime environment formation;
- static IR structure is not runtime evidence;
- package invocation/exercise remains CI-specific;
- multi-job/strategy/container/reusable structure being readable does not imply Target can fully interpret it;
- `not_observed` is not established absence;
- dynamic context remains unresolved;
- do not start CI migration before Target migration validation;
- do not introduce a shell interpreter, generic dependency tracer, universal workflow engine, or broader abstraction without demonstrated need;
- Tranche 2 remains separate and must not start automatically.

## Learning state

Current demonstrated depth remains substantial guided implementation exposure with repeated evidence-driven reasoning/debugging; no formal mastery assessment. Deep system/data-flow learning remains intentionally deferred until a meaningful milestone selected with the user.
