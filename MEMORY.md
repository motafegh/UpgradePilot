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
✓ Cluster 4 — Target migration / proof-strength correction
→ Cluster 5 — CI migration / proof-claim narrowing
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

Validated source-bearing revision `0d2c7f9eba08bd3c80f1b128d5b223b4e10a9667`. The parser boundary and explicit PyYAML dependency contract are validated green. Cluster 1 is **COMPLETED / GREEN**.

### Cluster 2 — static GitHub Actions workflow IR

Validated implementation revision `1e3027f87fa5b187c7d333472fe849aa6a49b049`.

User-run WSL focused/nearest validation and complete deterministic suite passed:

```text
Ran 416 tests in 0.087s
OK
```

Cluster 2 is **COMPLETED / GREEN**.

### Cluster 3 — direct-install declaration observation

Validated implementation revision `2980e22994216c069b2f4fb36dc31ea80398367f`.

The dependency-owned observer consumes the provider IR, respects step > job > workflow > repository-root working-directory precedence, and returns `observed | not_observed | unresolved` at static declaration strength only.

User-run validation passed focused/nearest tests and:

```text
Ran 425 tests in 0.085s
OK
```

Cluster 3 is **COMPLETED / GREEN**.

### Cluster 4 — Target migration

Validated implementation revision:

```text
f40e7348a38966e7e30b462846a4962a116a9e80
```

Target now consumes the shared static workflow IR and dependency-owned direct-install observer instead of owning a second YAML/indentation parser and a second pip requirements matcher.

The old static-only runtime-sounding contract:

```text
dependency_environment_formation = established | not_observed
```

has been replaced by declaration-strength evidence:

```text
dependency_installation_declaration = observed | not_observed | unresolved
installation_declaration_source = static command text | None
```

Proof strength is now explicit:

```text
observed static install declaration
!= command executed
!= command succeeded
!= environment formed
!= exact proposed version installed
!= package exercised
```

Readable multi-job/matrix/container/reusable structure now becomes Target-level ambiguity/limitations where necessary instead of being mislabeled as shared parser failure.

User-run fail-fast Cluster-4 validation reached its completion marker; all focused/nearest commands therefore passed. Complete deterministic suite:

```text
Ran 430 tests in 0.089s
OK
```

Final validation state:

```text
branch: main
HEAD: f40e7348a38966e7e30b462846a4962a116a9e80
origin/main: same revision
worktree: clean
```

Therefore Cluster 4 is **COMPLETED / GREEN**.

## Current implementation foundation

The validated foundation and first migrated consumer now form:

```text
exact repository workflow source
→ PyYAML bounded parser boundary
→ typed GitHub Actions static workflow IR
→ dependency-owned direct-install declaration observation
→ Target-specific partial artifact-environment evidence
```

Target no longer owns YAML/GitHub Actions parsing or generic direct-install recognition.

## Selected next responsibility — Cluster 5

Migrate CI static reading onto the validated shared workflow IR and shared direct-install observation where semantics are identical, while preserving CI-specific responsibilities:

```text
successful exact-head WorkflowRun / WorkflowJob evidence
+ package invocation/exercise interpretation
+ CI-specific result composition
```

The current CI contract must be narrowed so a successful exact-head run/job plus statically identified install/invocation commands is not described as if those exact commands were runtime-correlated and successful.

Current important proof ladder remains:

```text
successful exact-head run/job
+ static install declaration identified
+ static package invocation identified
!= matched static commands observed succeeding at runtime
```

Static↔runtime job/step correlation is **not** part of Cluster 5 and must remain deferred to the separately reviewed optional Tranche 2.

Multiple jobs/readable provider structure may remain CI-level unresolved where the current proposition cannot safely select/compose them; do not infer cross-job environment continuity from `needs` or source order.

## Remaining liabilities intentionally present

- `ci/workflow_commands.py` / `ci/dependency_exercise.py` still require Cluster-5 migration and claim narrowing;
- no static↔runtime step correlation exists;
- duplicate GitHub-local repository-path validation remains for Cluster 6;
- application orchestration remains Python-support-shaped;
- Cluster-7 whole-tranche regression/pressure acceptance remains pending.

## Immediate project action

Proceed with **Cluster 5 only**. Inspect the current CI static-command and dependency-exercise contracts, migrate them onto the validated shared IR/direct-install primitive where responsibilities are identical, preserve package invocation/exercise as CI-specific, add useful source docstrings/comments, and narrow proof-state wording/semantics without implementing runtime step correlation.

After Cluster-5 implementation is written, run focused CI + shared-provider/dependency + Target-nearest regressions and the complete deterministic suite before selecting Cluster 6.

## Continuation-critical guards

- `MEMORY.md` alone owns current continuation/latest verification;
- latest validated implementation revision is `f40e7348a38966e7e30b462846a4962a116a9e80`;
- later documentation/source commits may advance `main` without constituting new validation;
- static Target/CI declarations are not runtime execution evidence;
- package invocation/exercise remains CI-specific;
- successful run/job evidence must not be treated as static-command runtime correlation;
- multi-job/`needs`/source order do not prove environment continuity;
- `not_observed` is not established absence;
- dynamic/uninterpretable context remains unresolved;
- do not introduce static↔runtime correlation in Cluster 5;
- do not introduce a shell interpreter, generic dependency tracer, universal workflow engine, or broader abstraction without demonstrated need;
- Tranche 2 remains separate and must not start automatically.

## Learning state

Current demonstrated depth remains substantial guided implementation exposure with repeated evidence-driven reasoning/debugging; no formal mastery assessment. Deep system/data-flow learning remains intentionally deferred until a meaningful milestone selected with the user.
