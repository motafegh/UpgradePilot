# B2 Cross-Responsibility Architecture — Tranche 1 Implementation Record

**Date:** 2026-08-15  
**Operation:** Phase E / Tranche 1 — static workflow architecture implementation and migration  
**Result classification:** OPEN / progressive implementation evidence record  
**Validated product/source baseline:** `92e6ea6cb6dbfad7c50986d95e23de924a9b36c1` on `main`  
**Latest validated implementation revision:** `0d2c7f9eba08bd3c80f1b128d5b223b4e10a9667` on `main`  

## 1. Purpose and current operating mode

Preserve material implementation, debugging, findings, exact validation evidence, and cluster results while executing Tranche 1 of [`../plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_IMPLEMENTATION_PLAN.md`](../plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_IMPLEMENTATION_PLAN.md).

This file is an implementation evidence trail, not the live-state owner. `../MEMORY.md` alone owns current continuation.

Accepted durable architecture remains [`../docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md`](../docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md).

### Learning deferral decision

The short onboarding pause after Cluster 1 is ended. The user selected the learning-by-doing/building path again and explicitly deferred broad mastery/system/data-flow teaching until a meaningful implementation milestone.

Operationally:

```text
build/validate cluster-by-cluster
→ explain only prerequisites/reasoning needed to proceed correctly
→ preserve learning questions/context
→ at a meaningful milestone, pause for deeper current-system + real-data-flow learning
```

This learning deferral changes teaching cadence only. It does not weaken implementation, evidence, validation, architecture, or documentation gates.

## 2. Tranche-1 checklist

- [x] **Cluster 0 — synchronize and validate baseline**
- [x] **Cluster 1 — add PyYAML and prove parser dependency boundary**
- [ ] **Cluster 2 — implement bounded GitHub Actions static workflow IR** — implementation written, validation pending
- [ ] **Cluster 3 — implement shared direct-installation declaration observation**
- [ ] **Cluster 4 — migrate Target artifact-environment interpretation**
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

User-run WSL preflight established:

```text
branch: main
HEAD: 92e6ea6cb6dbfad7c50986d95e23de924a9b36c1
origin/main: same revision
worktree: clean
```

Focused migration-relevant regressions passed, followed by:

```text
Ran 403 tests in 0.256s
OK
```

### T1-F001 — clean pre-implementation source baseline

The Phase-E source baseline was reproduced green before parser/dependency changes. Later documentation commits do not change the product/source revision that was validated.

## 5. Cluster 1 — PyYAML dependency/parser boundary

**Status:** COMPLETED / GREEN  
**Validated implementation revision:** `0d2c7f9eba08bd3c80f1b128d5b223b4e10a9667`

Changes:

```text
pyproject.toml
→ PyYAML>=6.0.3,<7

src/upgradepilot/github/workflow_definition.py
→ BaseLoader composition boundary
→ private PyYAML representation nodes
→ controlled parse failure
→ bounded recursive-alias/depth/node traversal guards
```

Focused parser tests cover node shapes, block scalars/source marks, duplicate mapping-pair visibility, malformed YAML, recursion, depth, and traversal bounds.

### Failure / repair

The first post-change full suite exposed one stale dependency-contract expectation:

```text
test_packaging_dependency_uses_the_accepted_26x_bound
Ran 409 tests in 0.311s
FAILED (failures=1)
```

Cause: the explicit exact runtime dependency list still expected only requests + packaging after PyYAML was intentionally added.

Repair commit:

```text
0d2c7f9eba08bd3c80f1b128d5b223b4e10a9667
Update runtime dependency contract for PyYAML
```

The repaired test explicitly protects all three approved runtime dependencies and verifies installed PyYAML satisfies `>=6.0.3,<7`.

User then reran runtime dependency contract tests, focused Cluster-1 parser tests, and the complete deterministic suite and reported all green/passed.

### T1-F002 — dependency-surface regression was protective, not brittle

```text
approved runtime dependency change
→ exact dependency contract fails
→ contract deliberately updated
→ dependency change cannot enter silently
```

## 6. Cluster 2 — bounded static GitHub Actions workflow IR

**Status:** IMPLEMENTATION WRITTEN / VALIDATION PENDING  
**Cluster-2 source commits before documentation update:**

```text
db57de7fed4e039c3381c661f332082bf880a365
→ Implement bounded GitHub Actions static workflow IR

9c2abce10242ce5baf77a21d280cef474a06fd90
→ Add static workflow IR regressions

54ce69082b0d74ec0412b05264dfae897f970d47
→ Protect static workflow definition owner
```

### Expected

Implement the provider-owned typed static GitHub Actions representation required by ADR-0008 without entering dependency interpretation, Target migration, CI migration, runtime correlation, matrix expansion, or reusable-workflow execution.

### Changes

`src/upgradepilot/github/workflow_definition.py` now exposes the bounded provider contracts:

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

Provider entry point:

```text
parse_workflow_definition(RepositoryTextFile)
```

The parser boundary remains internal:

```text
RepositoryTextFile.content
→ PyYAML representation nodes
→ bounded GitHub Actions extraction
→ typed provider IR
```

### Preserved structural semantics

The implementation preserves:

- the authoritative `RepositoryTextFile` source object;
- workflow run defaults;
- ordered jobs with 0-based source indices;
- job key/name;
- `needs`;
- scalar/sequence/mapping `runs-on` structure;
- raw `if` conditions;
- `continue-on-error` declarations;
- job run defaults;
- strategy/matrix fragment without expansion;
- container fragment;
- reusable-workflow job reference + bounded `with` inputs;
- ordered steps;
- run command/shell/working-directory declarations;
- uses reference + bounded `with` inputs;
- 1-based diagnostic source spans;
- scalar `contains_expression` for `${{ ... }}`-backed values.

Required boundaries remain explicit:

```text
absent != literal != dynamic
multiple jobs preserved != consumer can compose them
source order != runtime scheduling
needs != environment continuity
static definition != runtime instance
```

### Structural problem model

Workflow-level problems are returned for malformed/unsupported whole-workflow structure such as malformed YAML, unsupported workflow path, non-mapping root/jobs, missing jobs, duplicate material workflow keys, or duplicate job IDs.

Job/step-local structural problems remain scoped where sibling structure can still be preserved. Current examples include ambiguous `uses`+`steps` jobs, missing/non-sequence steps on normal jobs, non-mapping steps, or a step declaring both/neither `run`/`uses`.

This separation implements the accepted rule:

```text
hard workflow problem
!= scoped local structural problem
!= later consumer-level unresolved
```

### Focused regression changes

`tests/test_github_workflow_definition.py` retains the Cluster-1 parser-boundary tests and adds IR coverage for:

- ordered multi-job preservation;
- workflow/job/step run-default inputs;
- literal and expression-backed values;
- `needs`;
- strategy/matrix preservation without expansion;
- container preservation;
- ordered run and uses steps;
- `if` / `continue-on-error` preservation;
- reusable-workflow job preservation without execution/expansion;
- duplicate job identity as a hard workflow problem;
- scoped job problem with readable sibling preservation;
- scoped step problem with sibling-step order preservation;
- malformed YAML/non-workflow path typed problems.

`tests/test_source_topology.py` now imports `parse_workflow_definition` from the `upgradepilot.github` provider owner.

### Current non-goals / not yet changed

Cluster 2 deliberately does not alter:

```text
ci/workflow_commands.py
target/artifact_environment.py
dependency direct-install interpretation
runtime WorkflowRun/WorkflowJob/WorkflowStep
repository-path ownership
application orchestration
```

Therefore old consumer-local workflow readers still exist until their planned migrations.

### Validation

Pending user-run WSL evidence.

Minimum requested gate:

```text
focused test_github_workflow_definition.py
+ test_source_topology.py
+ nearest GitHub repository/actions regressions
+ complete deterministic product suite
+ clean worktree
```

### Cluster result

`PARTIAL / IMPLEMENTATION WRITTEN / VALIDATION PENDING`

Cluster 3 must not begin until this gate is green and Cluster 2 is explicitly classified complete.

## 7. Remaining plan responsibilities

- Cluster 3 — shared direct-install declaration observation: **PENDING**
- Cluster 4 — Target migration: **PENDING**
- Cluster 5 — CI migration: **PENDING**
- Cluster 6 — repository-path ownership reconciliation: **PENDING**
- Cluster 7 — Tranche-1 acceptance gate: **PENDING**
- Tranche-1 stop/review: **PENDING**

Tranche 2 remains separately reviewed work and is outside this record.