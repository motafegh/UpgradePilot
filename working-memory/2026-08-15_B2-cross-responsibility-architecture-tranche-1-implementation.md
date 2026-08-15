# B2 Cross-Responsibility Architecture — Tranche 1 Implementation Record

**Date:** 2026-08-15  
**Operation:** Phase E / Tranche 1 — static workflow architecture implementation and migration  
**Result classification:** OPEN / progressive implementation evidence record  
**Validated product/source baseline:** `92e6ea6cb6dbfad7c50986d95e23de924a9b36c1` on `main`  
**Latest validated implementation revision:** `1e3027f87fa5b187c7d333472fe849aa6a49b049` on `main`  

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
- [x] **Cluster 2 — implement bounded GitHub Actions static workflow IR**
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

The first post-change full suite exposed one stale dependency-contract expectation because the exact runtime dependency list had not yet admitted PyYAML. Repair commit `0d2c7f9eba08bd3c80f1b128d5b223b4e10a9667` deliberately updated the dependency contract and added installed-PyYAML bound verification. User then reran the runtime dependency contract, focused parser tests, and complete suite and reported all green.

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

### Changes

Source commits:

```text
db57de7fed4e039c3381c661f332082bf880a365
→ Implement bounded GitHub Actions static workflow IR

9c2abce10242ce5baf77a21d280cef474a06fd90
→ Add static workflow IR regressions

54ce69082b0d74ec0412b05264dfae897f970d47
→ Protect static workflow definition owner
```

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

The IR preserves the authoritative source, workflow/job/step run context, ordered jobs/steps, `needs`, `runs-on`, conditions, `continue-on-error`, strategy/matrix fragment without expansion, container fragment, reusable workflow references, bounded `with` inputs, source indices/spans, and scalar expression presence.

Required boundaries remain explicit:

```text
absent != literal != dynamic
multiple jobs preserved != consumer can compose them
source order != runtime scheduling
needs != environment continuity
static definition != runtime instance
```

Workflow-level structural failures remain separate from scoped job/step problems, and both remain separate from later consumer-level unresolved states.

### Validation

User ran the requested fail-fast Cluster-2 gate in WSL at exact revision:

```text
HEAD: 1e3027f87fa5b187c7d333472fe849aa6a49b049
origin/main: same revision
branch: main
worktree: clean
```

The gate covered:

```text
test_github_workflow_definition.py
test_source_topology.py
test_github_actions.py
test_exact_commit_repository_files.py
test_ci_dependency_exercise.py
test_target_artifact_environment.py
```

All focused/nearest commands passed. Complete deterministic suite:

```text
Ran 416 tests in 0.087s
OK
```

Final worktree remained clean.

### T1-F003 — the provider IR is now independently green before consumer migration

Cluster 2 establishes the shared static GitHub Actions structure as a validated responsibility before dependency, Target, or CI consumers are migrated onto it:

```text
validated provider IR
!= migrated consumers
```

This gives Cluster 3+ a stable provider contract and preserves blame isolation if later consumer migration exposes failures.

### Cluster result

`COMPLETED / GREEN`

## 7. Cluster 3 — shared direct-install declaration observation

**Status:** PENDING

Selected next responsibility: add the dependency-owned bounded primitive that combines a static run declaration, effective workflow/job/step working-directory context, and an independently established repository-relative dependency-source path. It may recognize the admitted direct pip requirements-file forms but must stop at static declaration evidence.

## 8. Remaining plan responsibilities

- Cluster 4 — Target migration: **PENDING**
- Cluster 5 — CI migration: **PENDING**
- Cluster 6 — repository-path ownership reconciliation: **PENDING**
- Cluster 7 — Tranche-1 acceptance gate: **PENDING**
- Tranche-1 stop/review: **PENDING**

Tranche 2 remains separately reviewed work and is outside this record.