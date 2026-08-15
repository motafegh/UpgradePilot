# UpgradePilot Current Memory

**Last updated:** 2026-08-15  
**Authority:** Sole repository owner of live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Controlling route plan:** [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md).
- **B2 parent plan:** [`plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md).
- **Selected B2 responsibility:** [`plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md`](plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md).
- **Completed architecture checkpoint:** Phase A–D of [`plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_RECONCILIATION_PLAN.md`](plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_RECONCILIATION_PLAN.md).
- **Accepted architecture:** [`docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md`](docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md).
- **Selected Phase-E plan:** [`plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_IMPLEMENTATION_PLAN.md`](plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_IMPLEMENTATION_PLAN.md).
- **Current Phase-E evidence record:** [`working-memory/2026-08-15_B2-cross-responsibility-architecture-tranche-1-implementation.md`](working-memory/2026-08-15_B2-cross-responsibility-architecture-tranche-1-implementation.md).
- **Canonical product-decision semantics:** [`docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`](docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md).
- **Source ownership baseline:** [`docs/architecture/ADR-0007-responsibility-based-python-subpackages.md`](docs/architecture/ADR-0007-responsibility-based-python-subpackages.md).

**Phase-E state:** Tranche 1 Cluster 0 and Cluster 1 are complete and green. Implementation is deliberately paused after Cluster 1 for user onboarding and understanding. **Cluster 2 has not begun and is not currently selected for execution.**

The approved Phase-E plan still defines the remaining sequence, but no further source work should begin until the user completes the onboarding/review checkpoint and explicitly decides to resume implementation.

## Accepted architecture governing the current work

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

Runtime GitHub Actions evidence remains a separate family:

```text
WorkflowRun
WorkflowJob
WorkflowStep
```

A later optional static↔runtime correlation responsibility may strengthen CI proof where justified. It is not part of the base static IR and is not mandatory pipeline work.

Canonical proof boundary:

```text
static declaration
!= runtime execution
!= runtime success
!= environment formation
!= dependency exercise
```

## Current Phase-E implementation truth

### Cluster 0 — baseline

Validated product/source baseline:

```text
branch: main
revision: 92e6ea6cb6dbfad7c50986d95e23de924a9b36c1
origin/main: same revision
worktree: clean
```

Focused migration-relevant regressions passed:

```text
test_github_actions.py
test_exact_commit_repository_files.py
test_ci_dependency_exercise.py
test_target_artifact_environment.py
test_identity_primitives.py
test_source_topology.py
```

Complete deterministic suite:

```text
Ran 403 tests in 0.256s
OK
```

Therefore Cluster 0 is **COMPLETED / GREEN BASELINE**.

### Cluster 1 — PyYAML dependency/parser boundary

Latest validated source-bearing Cluster-1 revision:

```text
0d2c7f9eba08bd3c80f1b128d5b223b4e10a9667
```

Current runtime dependency surface in `pyproject.toml`:

```text
requests>=2.32,<3
packaging>=26.2,<27
PyYAML>=6.0.3,<7
```

Current new provider module:

```text
src/upgradepilot/github/workflow_definition.py
```

Its present responsibility is intentionally narrow:

```text
untrusted workflow YAML text
→ yaml.compose(..., Loader=yaml.BaseLoader)
→ PyYAML representation nodes
→ controlled parse failure
→ bounded recursive-alias/depth/node traversal validation
```

It does **not** yet implement the typed GitHub Actions job/step IR. PyYAML nodes are private parser machinery and must not leak into CI/Target/domain contracts.

Focused Cluster-1 coverage in `tests/test_github_workflow_definition.py` establishes the selected parser assumptions:

- textual scalar preservation under `BaseLoader`;
- scalar/sequence/mapping node shapes;
- literal/folded block-scalar decoding;
- source marks;
- duplicate mapping-pair visibility before ordinary dictionary collapse;
- malformed-YAML controlled failure;
- recursive alias rejection;
- bounded nesting/node traversal.

`tests/test_runtime_dependency_contract.py` now explicitly protects the three approved runtime dependencies and verifies installed PyYAML satisfies `>=6.0.3,<7`.

### Cluster-1 validation incident

The first post-change full-suite run produced one failure:

```text
test_packaging_dependency_uses_the_accepted_26x_bound
Ran 409 tests in 0.311s
FAILED (failures=1)
```

Cause: the explicit runtime dependency contract still expected only `requests` and `packaging`, while the accepted Cluster-1 implementation had intentionally added PyYAML.

This was classified as a stale dependency-contract expectation, not a parser or architecture defect.

Repair:

```text
0d2c7f9eba08bd3c80f1b128d5b223b4e10a9667
Update runtime dependency contract for PyYAML
```

The repair strengthened the test to require the approved three-dependency surface and added installed-PyYAML bound verification.

After repair, the user reran:

```text
runtime dependency contract tests
focused Cluster-1 parser-boundary tests
complete deterministic product suite
```

and reported all green/passed. No exact post-repair test count/timing is inferred because those numeric lines were not supplied.

Therefore Cluster 1 is **COMPLETED / GREEN**.

## Existing implementation liabilities intentionally still present

The following are **not** fixed merely because Cluster 1 is complete:

- no typed shared GitHub Actions static workflow IR yet;
- `ci/workflow_commands.py` and `target/artifact_environment.py` still contain their existing shallow workflow parsing;
- Target still uses the runtime-sounding `dependency_environment_formation` static-only contract;
- CI still exposes the current bounded `state="proven"` semantics;
- no static↔runtime step correlation exists;
- the duplicate private repository-path validator still exists in `github/repository.py`;
- `investigation.py` remains Python-support-shaped;
- no heterogeneous mechanism-result envelope exists.

These are remaining plan responsibilities, not evidence that Cluster 1 is incomplete.

## Phase-E Tranche-1 plan state

```text
✓ Cluster 0 — synchronize and validate baseline
✓ Cluster 1 — PyYAML dependency/parser boundary

PAUSE — onboarding / current-state understanding checkpoint

[ ] Cluster 2 — bounded GitHub Actions static workflow IR
[ ] Cluster 3 — shared direct-install declaration observation
[ ] Cluster 4 — Target migration
[ ] Cluster 5 — CI migration / proof-claim narrowing
[ ] Cluster 6 — repository-path reconciliation
[ ] Cluster 7 — Tranche-1 acceptance gate
[ ] Tranche-1 stop/review
```

The unchecked items remain in the approved plan but are **not current authorization to proceed**.

Tranche 2 remains a separately reviewed future strengthening and must not be started automatically.

## Immediate project action

**Do not implement or modify further Phase-E source code yet.**

The current selected responsibility is an onboarding/review checkpoint: understand the project and Phase-E architecture/implementation through the completed Cluster-1 point, including why Cluster 1 exists, how the new parser boundary works, what it proves and does not prove, how it relates to the existing CI/Target code, and which responsibilities remain intentionally unimplemented.

After that onboarding/review, the user will decide whether and how to resume the Phase-E implementation plan. No later cluster is selected before that decision.

## Continuation-critical guards

- `MEMORY.md` alone owns current continuation/latest verification;
- load ADR-0008 + the Phase-E plan + the current Tranche-1 record for orientation;
- the Phase-A–D architecture reconciliation records are historical provenance, not active logs;
- Cluster 0 baseline validation revision is `92e6ea6...`; Cluster-1 validated source-bearing revision is `0d2c7f9...`;
- later documentation commits may advance `main` without constituting new product/source validation;
- PyYAML parser nodes remain internal syntax machinery;
- YAML syntax normalization != GitHub Actions domain interpretation;
- static workflow declaration != execution != success;
- consumer unresolved != parser failure when structure is safely readable;
- multiple jobs / `needs` / source order != runtime environment continuity;
- workflow evidence is one Target evidence source, not the Target model;
- direct-install declaration != generic dependency consumption;
- package invocation/exercise remains CI-specific;
- static and runtime Actions evidence remain separate base contracts;
- exact target wheel tags require independently established compatibility evidence;
- `not_observed` is not established absence;
- PyYAML safety remains proportionate: no arbitrary-object construction and bounded malformed/recursive handling without a generalized parser-hardening program;
- do not introduce a generic YAML AST, universal CI provider, shell interpreter, workflow engine, universal environment model, provenance graph, universal impact object, plugin registry, or planner without demonstrated need;
- do not begin Cluster 2 or any later implementation responsibility until the onboarding checkpoint is complete and the user explicitly resumes implementation.

## Learning state

Current demonstrated depth remains **substantial guided implementation exposure with repeated evidence-driven reasoning/debugging; no formal mastery assessment**.

The immediate learning goal is now explicit: onboard through the full current project/Phase-E state up to and including Cluster 1 before choosing further implementation work.