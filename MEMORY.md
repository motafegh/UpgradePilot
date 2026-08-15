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
→ Cluster 2 — typed static GitHub Actions workflow IR: implementation written, validation pending
[ ] Cluster 3 — direct-install declaration observation
[ ] Cluster 4 — Target migration
[ ] Cluster 5 — CI migration / proof-claim narrowing
[ ] Cluster 6 — repository-path reconciliation
[ ] Cluster 7 — Tranche-1 acceptance gate
[ ] Tranche-1 stop/review
```

**Learning mode:** the prior onboarding pause is ended. Deep learning/mastery, full current-system walkthrough, and real end-to-end data-flow study are deliberately **deferred until a meaningful implementation milestone**. Until then, proceed learning-by-doing and preserve momentum. Explain prerequisites or implementation reasoning just-in-time when they are needed to build or decide correctly; do not stop the implementation sequence for broad teaching unless the user requests it.

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

### Cluster 1 — PyYAML/parser boundary

Latest validated source-bearing Cluster-1 revision:

```text
0d2c7f9eba08bd3c80f1b128d5b223b4e10a9667
```

Runtime dependency surface:

```text
requests>=2.32,<3
packaging>=26.2,<27
PyYAML>=6.0.3,<7
```

`src/upgradepilot/github/workflow_definition.py` established the private parser boundary:

```text
untrusted workflow YAML text
→ yaml.compose(..., Loader=yaml.BaseLoader)
→ PyYAML representation nodes
→ controlled parse failure
→ bounded recursive-alias/depth/node traversal validation
```

The first post-change full suite exposed one stale runtime-dependency-contract expectation after PyYAML was intentionally added. The test was deliberately updated to protect all three approved runtime dependencies and to verify the installed PyYAML bound. The user then reran the runtime dependency contract tests, focused parser tests, and complete product suite and reported all green. Cluster 1 is **COMPLETED / GREEN**.

## Current Cluster 2 implementation truth

Cluster 2 source and focused regressions are now written on `main`, but **real WSL validation is still pending**, so Cluster 2 is not yet classified complete.

### Provider model now implemented

`src/upgradepilot/github/workflow_definition.py` now translates private PyYAML nodes into bounded typed GitHub Actions static structure.

The current public provider contracts include:

```text
SourceSpan

GitHubActionsStaticValue
├─ StaticScalarValue
├─ StaticSequenceValue
└─ StaticMappingValue / StaticMappingEntry

RunDefaults

StepEntry
├─ RunStepDefinition
├─ UsesStepDefinition
└─ StepProblem

JobEntry
├─ StepsJobDefinition
├─ ReusableWorkflowJobDefinition
└─ JobProblem

WorkflowDefinitionResult
├─ WorkflowDefinition
└─ WorkflowDefinitionProblem
```

`parse_workflow_definition(RepositoryTextFile)` is the provider entry point.

### Preserved semantics

The IR currently preserves, where safely readable:

- authoritative `RepositoryTextFile` source reference;
- workflow-level run defaults;
- ordered jobs and 0-based source occurrence indices;
- job key/name;
- `needs`;
- scalar/sequence/mapping `runs-on` structure;
- raw `if` condition scalars;
- `continue-on-error` scalars;
- job run defaults;
- bounded strategy/matrix structure without expansion;
- bounded container structure;
- reusable-workflow job reference + `with` inputs;
- ordered run/uses/scoped-problem steps;
- run command, shell, and working-directory declarations;
- uses reference + `with` inputs;
- 1-based diagnostic source spans;
- scalar `contains_expression` state for `${{ ... }}`-backed values.

Required distinctions remain:

```text
absent != literal != dynamic
source order != runtime scheduling
needs != environment continuity
static definition != runtime instance
```

PyYAML node objects remain private implementation machinery and are not exposed as the UpgradePilot IR contract.

### Structural problem boundaries

Current whole-workflow typed problems include malformed YAML, unsupported workflow path, non-mapping root/jobs, missing jobs, duplicate material workflow keys, and duplicate job IDs.

Current job/step-local structural problems remain scoped so one malformed local entry does not automatically destroy readable sibling structure. Examples include ambiguous `uses`+`steps` jobs, missing/non-sequence normal-job steps, non-mapping steps, and steps declaring both/neither `run`/`uses`.

### Cluster-2 tests written

`tests/test_github_workflow_definition.py` now retains the Cluster-1 parser-boundary tests and adds IR regressions for:

- ordered multi-job preservation;
- workflow/job/step run-default inputs;
- literal and expression-backed values;
- `needs`;
- strategy/matrix preservation without expansion;
- container preservation;
- ordered run + uses steps;
- `if` and `continue-on-error` preservation;
- reusable-workflow job preservation without expansion;
- hard duplicate job identity failure;
- scoped job and step problems;
- malformed YAML and non-workflow path typed problems.

`tests/test_source_topology.py` now imports `parse_workflow_definition` from `upgradepilot.github.workflow_definition`, protecting the accepted provider owner.

## Existing liabilities intentionally still present

Cluster 2 does **not** migrate consumers yet. Therefore:

- `ci/workflow_commands.py` still uses the existing shallow local workflow reader;
- `target/artifact_environment.py` still uses its existing shallow local workflow reader;
- no dependency-owned direct-install declaration primitive exists yet;
- Target still exposes runtime-sounding `dependency_environment_formation` static-only semantics;
- CI still exposes the current bounded `state="proven"` semantics;
- no static↔runtime step correlation exists;
- the duplicate repository-path validator remains in `github/repository.py`;
- `investigation.py` remains Python-support-shaped;
- no heterogeneous mechanism-result envelope exists.

These are later plan responsibilities, not defects to solve inside Cluster 2.

## Immediate project action

**Validate Cluster 2 in the user's WSL checkout before beginning Cluster 3.**

Required next evidence should include at minimum:

```text
pull current main
→ focused tests/test_github_workflow_definition.py
→ tests/test_source_topology.py
→ nearest GitHub repository/actions regressions
→ complete deterministic product suite
→ final clean worktree
```

Any failure must be classified as an implementation defect, test-contract correction, or pre-existing unrelated failure before Cluster 2 is marked complete.

If validation is green, update the Tranche-1 working record and this file to classify Cluster 2 complete; only then resume Cluster 3.

## Continuation-critical guards

- `MEMORY.md` alone owns current continuation/latest verification;
- deep learning/system/data-flow onboarding is deferred until a meaningful milestone; keep implementation momentum and use just-in-time teaching only as needed;
- Cluster 0 baseline revision is `92e6ea6...`; Cluster-1 validated source-bearing revision is `0d2c7f9...`;
- Cluster 2 is written but not yet validated/complete;
- `RepositoryTextFile` remains authoritative raw source evidence;
- PyYAML parser nodes remain internal syntax machinery;
- valid dynamic values are source evidence, not parser failure;
- multiple jobs / `needs` / source order do not prove runtime environment continuity;
- no matrix expansion or reusable-workflow execution is performed;
- static workflow declaration != execution != success;
- consumer unresolved != parser failure when source structure remains safely readable;
- workflow evidence is one Target evidence source, not the Target model;
- direct-install declaration != generic dependency consumption;
- package invocation/exercise remains CI-specific;
- static and runtime Actions evidence remain separate base contracts;
- `not_observed` is not established absence;
- parser safety remains proportionate; do not build a generalized hostile-YAML framework;
- do not introduce a generic YAML AST, universal CI provider, shell interpreter, workflow engine, universal environment model, provenance graph, universal impact object, plugin registry, or planner without demonstrated need;
- do not begin Cluster 3 until Cluster 2 validation is green.

## Learning state

Current demonstrated depth remains **substantial guided implementation exposure with repeated evidence-driven reasoning/debugging; no formal mastery assessment**.

Current operating preference for this tranche is learning-by-doing. A deeper system walkthrough—including current implementation relationships and real end-to-end data flow—will be resumed at a meaningful milestone rather than interrupting each implementation cluster.