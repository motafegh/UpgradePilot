# UpgradePilot Current Memory

**Last updated:** 2026-08-15  
**Authority:** Sole repository owner of live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Controlling route plan:** [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md).
- **B2 parent plan:** [`plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md).
- **Selected B2 responsibility:** [`plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md`](plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md).
- **Completed architecture checkpoint through Phase D:** [`plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_RECONCILIATION_PLAN.md`](plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_RECONCILIATION_PLAN.md).
- **Selected Phase-E implementation/refactor plan:** [`plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_IMPLEMENTATION_PLAN.md`](plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_IMPLEMENTATION_PLAN.md).
- **Current Phase-E Tranche-1 implementation record:** [`working-memory/2026-08-15_B2-cross-responsibility-architecture-tranche-1-implementation.md`](working-memory/2026-08-15_B2-cross-responsibility-architecture-tranche-1-implementation.md).
- **Accepted architecture:** [`docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md`](docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md).
- **Closed Phase-A/B/C progressive reasoning record:** [`working-memory/2026-08-14_B2-cross-responsibility-architecture-reconciliation-progress.md`](working-memory/2026-08-14_B2-cross-responsibility-architecture-reconciliation-progress.md).
- **Phase-D closure/acceptance provenance:** [`working-memory/2026-08-15_B2-cross-responsibility-architecture-reconciliation-phase-d-closure.md`](working-memory/2026-08-15_B2-cross-responsibility-architecture-reconciliation-phase-d-closure.md).
- **Phase-C simulation pressure evidence:** [`product-simulation/CROSS_RESPONSIBILITY_ARCHITECTURE_PHASE_C_PRESSURE_TEST_01.md`](product-simulation/CROSS_RESPONSIBILITY_ARCHITECTURE_PHASE_C_PRESSURE_TEST_01.md) — non-controlling evidence adopted during main-side reconciliation.
- **Canonical accepted product-decision semantics:** [`docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`](docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md).
- **Source ownership baseline:** [`docs/architecture/ADR-0007-responsibility-based-python-subpackages.md`](docs/architecture/ADR-0007-responsibility-based-python-subpackages.md).
- **Documentation/decision ownership map:** [`docs/README.md`](docs/README.md).
- **Artifact Serviceability Increment 2:** [`working-memory/2026-08-13_B2-artifact-serviceability-increment-2-target-applicability.md`](working-memory/2026-08-13_B2-artifact-serviceability-increment-2-target-applicability.md).
- **Target Artifact Environment Increment 1:** [`working-memory/2026-08-14_B2-target-artifact-environment-increment-1-implementation.md`](working-memory/2026-08-14_B2-target-artifact-environment-increment-1-implementation.md).

The mandatory cross-responsibility architecture gate was triggered because a second real mechanism/source consumer exposed duplicated GitHub Actions parsing and proof-strength ambiguity. Phase A mapped the current source/evidence responsibilities, Phase B compared architecture options, Phase C adversarially pressure-tested the leading option, and Phase D accepted/promoted the durable direction.

Future sessions should load ADR-0008 and the selected Phase-E plan before reconstructing the decision from dated working-memory. The closed architecture records remain provenance and reasoning evidence; Phase-E source changes, findings, failures, and exact validation results now belong in the selected Tranche-1 implementation working record.

**Phase-E status:** Tranche 1 Cluster 0 is complete and green. Cluster 1 implementation is written on `main` and is awaiting user-run WSL dependency/install and focused/full validation before it can be classified complete.

## Accepted architecture now governing Phase E

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

An optional later explicit static↔runtime correlation responsibility may strengthen CI proof when a proposition requires it. It is not part of the base static IR and is not mandatory pipeline work.

PyYAML is the accepted parser dependency/method for the shared static reader:

```text
RepositoryTextFile.content
→ PyYAML representation/node parsing
→ bounded GitHub Actions extraction
→ typed provider IR
```

Cluster 1 has now added `PyYAML>=6.0.3,<7` to `pyproject.toml`, plus the private initial parser/traversal boundary in `src/upgradepilot/github/workflow_definition.py` and its focused dependency-boundary tests. Those changes are **not yet runtime-validated in the user's WSL checkout**.

The shared IR must preserve safely readable multi-job/provider structure without manufacturing consumer semantics. Dynamic values, matrices, reusable-workflow jobs, containers, or other consumer limitations are not parser failure when their source structure is safely preservable.

The durable proof boundary remains:

```text
static declaration
!= runtime execution
!= runtime success
!= environment formation
!= dependency exercise
```

## Current implementation truth

The first Python-support candidate → applicability → discriminating observation → reevaluation loop is implemented and verified green.

Artifact Serviceability Increment 1 compares exact old/proposed PyPI artifact inventories, parses wheel compatibility tags, preserves sdist availability, and creates a target-agnostic candidate when published wheel capabilities disappear.

Artifact Serviceability Increment 2 adds `TargetWheelCompatibilityEvidence`, `TargetWheelCompatibilityProblem`, `ArtifactServiceabilityImpactAssessment`, and `evaluate_artifact_serviceability_impact(...)`. It evaluates complete old/proposed wheel inventories against an **already-established exact target-supported tag set**.

Critical guards remain:

```text
removed published wheel tag != exact repository loses a compatible wheel
sdist exists != source build succeeds
```

Target Artifact Environment Increment 1 remains implemented in `src/upgradepilot/target/artifact_environment.py` with its original first-slice shallow workflow reader. It preserves exact repository/workflow/job provenance plus literal runner, literal setup-python version, visible direct dependency-source installation, limitations, and unresolved exact wheel compatibility.

Its current source contract still uses:

```text
dependency_environment_formation = established | not_observed
```

ADR-0008/Phase D accept that this runtime-sounding static-only semantic must migrate during Phase-E Tranche 1 to direct-installation-declaration/configuration meaning. **The source has not been migrated yet.**

Current CI still uses `state="proven"` for a bounded combination of successful exact-head run/job evidence plus static install/invocation recognition. ADR-0008/Phase D require Tranche 1 to narrow/refine this claim so it is not read as matched-command runtime-success proof. **Static↔runtime step correlation is not implemented yet.**

The current duplicated shallow workflow parsing in:

```text
src/upgradepilot/ci/workflow_commands.py
src/upgradepilot/target/artifact_environment.py
```

has not yet been replaced by the accepted shared IR.

The duplicate private repository-path validator in `src/upgradepilot/github/repository.py` has not yet been reconciled with the source-neutral `src/upgradepilot/repository_path.py` owner.

Application orchestration in `src/upgradepilot/investigation.py` remains Python-support-shaped. Phase D accepts the future need for a small typed heterogeneous mechanism-result transport when artifact serviceability actually enters the application path, but no exact envelope or orchestration implementation is accepted now.

Cluster 1 source/dependency work currently present on `main`:

```text
pyproject.toml
→ PyYAML>=6.0.3,<7

src/upgradepilot/github/workflow_definition.py
→ private BaseLoader composition boundary
→ controlled YAML parse error
→ bounded recursive-alias/depth/node traversal guard
→ PyYAML nodes remain private implementation machinery

tests/test_github_workflow_definition.py
→ scalar/sequence/mapping node contract
→ literal/folded block-scalar decoding + source marks
→ duplicate mapping-pair visibility
→ malformed-YAML controlled failure
→ recursive alias rejection
→ depth/node guard enforcement
```

This is intentionally **not yet the GitHub Actions job/step IR**; that responsibility remains Cluster 2.

## Verification truth

### Phase E / Tranche 1 Cluster 0 baseline

On 2026-08-15, user-run WSL preflight established exact synchronized baseline:

```text
branch: main
HEAD: 92e6ea6cb6dbfad7c50986d95e23de924a9b36c1
origin/main: 92e6ea6cb6dbfad7c50986d95e23de924a9b36c1
worktree: clean
```

The fail-fast preflight passed the existing import/Python checks plus focused migration-relevant regressions:

```text
test_github_actions.py
test_exact_commit_repository_files.py
test_ci_dependency_exercise.py
test_target_artifact_environment.py
test_identity_primitives.py
test_source_topology.py
```

and the complete deterministic suite finished:

```text
Ran 403 tests in 0.256s
OK
```

Final worktree remained clean. Therefore **Cluster 0 is COMPLETED / GREEN BASELINE**. No product source edits preceded this gate.

### Phase E / Tranche 1 Cluster 1

Implementation is written but **validation is pending**. No passing import/install, focused parser-boundary, nearest regression, or post-change full-suite result is claimed yet.

Fresh user WSL verification for Artifact Serviceability Increment 2 after pulling `main` through `f4c3ecdcbd738eceed7f50d30acb567a13c78642` remains:

```text
retained Increment-2 smoke: PASS
focused artifact-serviceability suite: 11 tests, OK
full active suite: 397 tests, OK
```

Artifact Serviceability Increment 2 remains **VERIFIED COMPLETE AT ITS BOUNDED SCOPE**.

For Target Artifact Environment Increment 1, the permanent focused regression file covers six bounded behaviors. An assistant reconstructed focused harness was green, and on 2026-08-14 Ali reported both requested real-repository WSL commands green after pulling current `main`:

```text
python -m unittest discover -s tests -p 'test_target_artifact_environment.py' -v
python -m unittest discover -s tests
```

No exact test count or timing is inferred because only the green result was reported. No separate nearest-regression command/result is recorded. GitHub exposes no configured commit status checks for that implementation commit, so no remote CI proof is inferred.

Therefore Target Artifact Environment Increment 1 remains **VERIFIED COMPLETE AT ITS ORIGINAL BOUNDED SCOPE**. That verification does not prove the newly accepted ADR-0008 architecture or its future migrated contracts.

The architecture documents/ADR/plan are validated as decision/ownership artifacts; they do not substitute for Phase-E runtime dependency, source, and regression proof.

## Adopted evidence and decision boundaries

The responsibility before `TargetWheelCompatibilityEvidence` remains:

```text
exact repository + immutable revision
→ proposition-specific scoped target evidence
→ partial, provenance-carrying environment/configuration facts
→ exact wheel compatibility only when genuinely justified
→ otherwise explicit insufficient / unresolved
```

GitHub Actions workflow evidence is one possible provider-specific Target evidence source. It is not the general Target-context model. S008 and S012 reinforce that Target may require separately scoped repository/build/package/runtime/historical/persisted-state evidence.

A shared direct-installation-declaration observation is accepted under `upgradepilot.dependency`:

```text
static run command
+ effective working-directory context
+ independently established dependency-source path
→ direct installation declaration observation
```

Its meaning stops at declaration/configuration:

```text
direct install declaration observed
!= executed
!= succeeded
!= exact proposed dependency version installed
!= generic dependency consumption
!= package exercise
```

Package invocation/exercise recognition remains CI-specific. S005 demonstrates that exact dependency consumption may require lock/resolver/tox/uv/matrix or other evidence chains.

Parser safety for untrusted public workflow text is owned generally by `SECURITY.md` and must remain proportionate: safe/non-arbitrary-object parsing, controlled malformed/ambiguous failure, existing source-size bounds, and sufficient recursion/traversal protection without building an unrelated hostile-parser framework.

## Selected implementation sequence

The selected Phase-E plan deliberately separates two tranches.

### Tranche 1 — active implementation responsibility

```text
✓ baseline synchronization + validation
↓
→ PyYAML dependency/parser boundary: implementation written, validation pending
↓
implement bounded github-owned static workflow IR
↓
implement dependency-owned direct-install declaration observation
↓
migrate Target + correct static proof semantics
↓
migrate CI + narrow current proof claim
↓
reconcile repository-path duplication
↓
focused + nearest + full regression acceptance
STOP / REVIEW
```

The selected dated evidence/log surface for this tranche is [`working-memory/2026-08-15_B2-cross-responsibility-architecture-tranche-1-implementation.md`](working-memory/2026-08-15_B2-cross-responsibility-architecture-tranche-1-implementation.md). It mirrors Clusters 0–7 as a local checklist but does not replace this live-state file or the implementation plan.

### Tranche 2 — later separately reviewed strengthening

```text
static workflow job/step
↕ explicit bounded correlation
runtime WorkflowJob/WorkflowStep
→ stronger CI proof where justified
```

Do not automatically begin Tranche 2 after Tranche 1 without review.

Heterogeneous mechanism orchestration remains a separate later responsibility when artifact serviceability is actually integrated into the application path.

## Immediate project action

**Validate the written Cluster 1 change in the user's WSL environment before expanding to Cluster 2.** Pull current `main`, install/update the editable project so the new PyYAML dependency is present, verify PyYAML 6.0.3 is imported, run `tests/test_github_workflow_definition.py`, run the nearest source-topology/GitHub tests, then run the complete deterministic suite. Record exact observed results in the Tranche-1 implementation working record.

If Cluster 1 is green, classify it complete and immediately begin Cluster 2 — the bounded GitHub Actions static workflow IR. If dependency/parser behavior differs materially from the accepted assumptions, diagnose that bounded discrepancy before broadening the design.

## Continuation-critical guards

- load ADR-0008 and the selected Phase-E plan before reconstructing architecture from dated working-memory;
- the closed architecture reconciliation record must not be reused as the Phase-E implementation log;
- use the selected Tranche-1 working record for material implementation/debugging/validation evidence only;
- `MEMORY.md` alone owns live continuation/latest verification;
- ADR acceptance does not prove implementation or tests;
- static workflow declaration/configuration must not become runtime execution/success/formation without appropriate observation;
- consumer unsupported/unresolved must not be mislabeled as shared parser failure when source structure remains safely preservable;
- multiple jobs / `needs` / source order do not prove cross-job environment continuity;
- dynamic Actions values do not become established evaluated runtime values;
- run path interpretation must account for effective working-directory context;
- direct-install declaration observation must not become a generic dependency-consumption abstraction;
- package invocation/exercise remains CI-specific unless later demonstrated sameness earns a broader owner;
- static and runtime Actions evidence remain separate base contracts;
- stronger runtime correlation remains proposition/evidence-relative rather than mandatory pipeline work;
- workflow evidence is one Target evidence source, not the Target model;
- exact target wheel tags must be independently established; broad runner/Python labels are insufficient;
- `not_observed` is not established absence;
- multi-environment facts must not be flattened into one synthetic repository environment;
- PyYAML parsing must follow the proportional untrusted-evidence safeguards in `SECURITY.md`;
- do not introduce a generic YAML AST, universal CI provider, shell interpreter, workflow engine, universal environment reconstructor, generic provenance graph, universal impact object, registry/plugin system, or planner without demonstrated need;
- repository-relative structural validation should reuse `repository_path.py` where semantics are identical;
- do not design the heterogeneous mechanism-result envelope before the second mechanism actually enters the application path.

## Learning state

Current demonstrated depth remains **substantial guided implementation exposure with repeated evidence-driven reasoning/debugging; no formal mastery assessment**.

The architecture-theory checkpoint is closed and the baseline gate is complete. The learning emphasis is now implementation-by-doing: validate the concrete PyYAML representation-node boundary, then build the shared static IR and migrate real consumers under the accepted proof boundaries.