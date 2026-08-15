# B2 Cross-Responsibility Architecture — Tranche 1 Implementation Record

**Date:** 2026-08-15  
**Operation:** Phase E / Tranche 1 — static workflow architecture implementation and migration  
**Result classification:** OPEN / progressive implementation evidence record  
**Validated product/source baseline:** `92e6ea6cb6dbfad7c50986d95e23de924a9b36c1` on `main`  
**Latest validated implementation revision:** `2980e22994216c069b2f4fb36dc31ea80398367f` on `main`  

## 1. Purpose and current operating mode

Preserve material implementation, debugging, findings, exact validation evidence, and cluster results while executing Tranche 1 of [`../plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_IMPLEMENTATION_PLAN.md`](../plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_IMPLEMENTATION_PLAN.md).

This file is an implementation evidence trail, not the live-state owner. `../MEMORY.md` alone owns current continuation.

Accepted durable architecture remains [`../docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md`](../docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md).

### Learning deferral decision

The user selected the learning-by-doing/building path and explicitly deferred broad mastery/system/data-flow teaching until a meaningful implementation milestone.

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
- [x] **Cluster 3 — implement shared direct-installation declaration observation**
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

Source commits:

```text
db57de7fed4e039c3381c661f332082bf880a365
→ Implement bounded GitHub Actions static workflow IR

9c2abce10242ce5baf77a21d280cef474a06fd90
→ Add static workflow IR regressions

54ce69082b0d74ec0412b05264dfae897f970d47
→ Protect static workflow definition owner
```

The validated provider IR preserves the bounded GitHub Actions static structure required by ADR-0008 while keeping PyYAML nodes private and static/runtime evidence separate.

User-run WSL validation at exact `1e3027f...` passed the focused/nearest gate and complete deterministic suite:

```text
Ran 416 tests in 0.087s
OK
```

Final branch/HEAD/origin were aligned on `main` and the worktree remained clean.

### T1-F003 — provider IR is independently green before consumer migration

```text
validated provider IR
!= migrated consumers
```

Cluster 3+ therefore build against a proven provider contract and later consumer failures remain attributable.

## 7. Cluster 3 — shared direct-install declaration observation

**Status:** COMPLETED / GREEN  
**Validated implementation revision:** `2980e22994216c069b2f4fb36dc31ea80398367f`

### Expected

Add one dependency-owned bounded primitive only after the provider IR is stable:

```text
static RunStepDefinition
+ workflow/job/step working-directory declarations
+ independently established dependency-source path
→ direct installation declaration observation
```

Proof strength stops at static declaration/configuration.

### Changes

New module:

```text
src/upgradepilot/dependency/direct_install.py
```

Provider-consuming entry point:

```text
observe_direct_installation_declaration(...)
```

The result model preserves:

```text
state = observed | not_observed | unresolved
reason/detail
step source index
static command text
independently established dependency-source path
effective working-directory state/source/path/raw value
matched requirements argument where observed
```

Working-directory precedence:

```text
step
↓
job defaults.run
↓
workflow defaults.run
↓
repository root
```

Dynamic or unsupported higher-precedence working-directory context becomes `unresolved`; the implementation does not fall through to lower-precedence context and fabricate certainty.

The primitive recognizes only bounded direct requirements-file forms beginning with:

```text
pip install ...
pip3 install ...
python -m pip install ...
python3 -m pip install ...
```

plus `-r` / `--requirement` path arguments. Admitted relative paths are resolved against the effective working directory, including safe parent resolution that remains inside the repository.

It deliberately avoids false-positive treatment of non-direct text such as:

```text
echo "pip install -r requirements.txt"
```

### Proof boundary

```text
direct install declaration observed
!= command executed
!= command succeeded
!= environment formed
!= exact proposed dependency version installed
!= generic dependency consumption
!= package exercise
```

Package invocation/exercise remains CI-specific.

### Focused regressions

New:

```text
tests/test_direct_install_declaration.py
```

Coverage includes:

- repository-root direct requirements install;
- step > job > workflow working-directory precedence;
- safe `../` requirements resolution back to repository source;
- dynamic effective working-directory → unresolved;
- dynamic requirements path → unresolved;
- visible nonmatching requirements source → not observed;
- non-direct pip text not misclassified;
- direct install inside a bounded shell-segment sequence;
- invalid independently established repository source paths rejected.

`tests/test_source_topology.py` protects `upgradepilot.dependency.direct_install` as the dependency owner.

Source/test commits:

```text
465ccd9e4b5ecf62728c5472294d80f6487d2e41
→ Implement direct install declaration observation

1cb72f7506e68dbe9de57047fcb5ff0062542788
→ Add direct install declaration regressions

2b4cc976c3bfe014a061e4e63f5cce5e219f719a
→ Protect direct install declaration owner
```

### Validation

User ran the requested fail-fast Cluster-3 gate in WSL at exact revision:

```text
branch: main
HEAD: 2980e22994216c069b2f4fb36dc31ea80398367f
origin/main: 2980e22994216c069b2f4fb36dc31ea80398367f
worktree: clean
```

The gate covered:

```text
test_direct_install_declaration.py
test_source_topology.py
test_github_workflow_definition.py
test_identity_primitives.py
test_ci_dependency_exercise.py
test_target_artifact_environment.py
```

Because the fail-fast block reached its final completion marker, all focused/nearest commands returned success.

Complete deterministic suite:

```text
Ran 425 tests in 0.085s
OK
```

Final branch/HEAD/origin remained aligned and the worktree remained clean.

### T1-F004 — dependency declaration observation is green before consumer migration

The shared dependency-owned interpretation is now independently validated before Target or CI are migrated onto it:

```text
validated static provider IR
+
validated direct-install declaration primitive
!= Target migrated
!= CI migrated
```

This keeps later consumer migration failures attributable and preserves the proof-strength boundary.

### Cluster result

`COMPLETED / GREEN`

## 8. Current handoff / deliberate stop for discussion

Implementation is deliberately stopped after the validated Cluster-3 checkpoint at the user's request.

No Cluster-4 Target migration has begun. Cluster 4 remains next in the approved sequence but is **not currently selected for execution** until discussion/decision resumes the plan.

The current validated implementation foundation is therefore:

```text
Cluster 0 — green baseline
+
Cluster 1 — PyYAML parser boundary
+
Cluster 2 — typed GitHub Actions static IR
+
Cluster 3 — dependency-owned direct-install declaration observation
```

## 9. Remaining plan responsibilities — not yet executed

- Cluster 4 — Target migration: **PENDING / NOT SELECTED**
- Cluster 5 — CI migration: **PENDING**
- Cluster 6 — repository-path ownership reconciliation: **PENDING**
- Cluster 7 — Tranche-1 acceptance gate: **PENDING**
- Tranche-1 stop/review: **PENDING**

Tranche 2 remains separately reviewed work and is outside this record.