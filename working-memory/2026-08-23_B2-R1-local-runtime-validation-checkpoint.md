# Working Memory — B2 R1 Local Runtime Validation Checkpoint

**Date:** 2026-08-23  
**Status:** PARTIAL RUNTIME VALIDATION COMPLETE; R1 MIGRATION BLOCKERS CONFIRMED  
**Execution branch:** `agent/r1-exact-file-contract-migration`  
**Current plan:** `../plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`

## 1. Why this checkpoint exists

R1 exact-file migration work was intentionally accumulated while local WSL execution was unavailable. Once local access returned, validation was run before further implementation so migration defects would not be mixed with later `main` reconciliation effects.

No `main` merge/rebase/reset was performed before these tests.

Environment reported by the user:

```text
branch: agent/r1-exact-file-contract-migration
Python: 3.12.3
interpreter: /home/motafeq/projects/UpgradePilot/.venv/bin/python
```

## 2. Focused runtime gates

### Gate 1 — strong exact-file provider/type foundation

Executed:

```text
tests.test_github_repository
tests.test_exact_commit_repository_files
```

Result:

```text
Ran 13 tests in 0.008s
OK
```

Interpretation: the migrated `RepositoryTextFile` / `UnavailableRepositoryFile` foundation and GitHub exact-file acquisition behavior are runtime-green under the focused suite.

### Gate 2 — dependency exact-file semantic extraction

Executed focused dependency contract/extractor tests covering:

```text
tests.test_dependency_change_contracts
tests.test_dependency_analysis
tests.test_uv_lock_change
tests.test_uv_lock_versionless_records
tests.test_pyproject_dependency_analysis
tests.test_pyproject_optional_extra_change
```

Result reported: **green / passed**.

Interpretation: Step 2B dependency provenance/extractor migration is runtime-green under its focused suite.

### Gate 3 — uv composition + Target artifact environment

Executed:

```text
tests.test_uv_selected_environment_membership
tests.test_uv_membership_universal_lock_boundary
tests.test_dependency_environment
tests.test_target_artifact_environment
```

Result:

```text
Ran 34 tests in 0.011s
OK
```

Interpretation: Step 2C independent-composition joins and Target artifact-environment migration are runtime-green under the focused suite.

### Gate 4 — tagged changelog / upstream authority / bounded semantic pipeline

Executed:

```text
tests.test_tagged_changelog_acquisition
tests.test_upstream_interval
tests.test_upstream_interval_authority_edges
tests.test_upstream_interval_acquisition_integration
tests.test_upstream_changelog
tests.test_upstream_claim
tests.test_upstream_claim_edges
tests.test_upstream_support_drop
tests.test_support_drop_extractor
experiments.tests.test_step6_support_drop_semantic_corpus
```

Result:

```text
Ran 88 tests in 0.010s
OK
```

Interpretation: the tagged-changelog exact-source migration, interval authority, deterministic source-window grounding, and mocked local-model semantic contract are runtime-green under the focused suite.

## 3. Broader validation checkpoint

Additional results:

```text
tests.test_source_topology
→ Ran 3 tests / OK

experiments/tests discovery
→ Ran 27 tests / OK

python -m compileall -q src tests experiments/step6_support_drop_smoke.py
→ exit 0
```

These establish that source topology and compilation are healthy and the experiment test package remains coherent after the migrated contracts.

## 4. Confirmed Target Python blocker

`tests.test_target_python` was run before any Target-Python migration.

Result:

```text
Ran 8 tests
FAILED (errors=8)
```

The dominant failure is stale construction of the retired exact-file contract:

```text
TypeError: RepositoryTextFile.__init__() got an unexpected keyword argument 'blob_sha'
```

The unavailable-file fixture also still omits the now-required repository identity:

```text
TypeError: UnavailableRepositoryFile.__init__() missing 1 required positional argument: 'repository'
```

This confirms the previously discovered source pressure in:

```text
src/upgradepilot/target/python.py
tests/test_target_python.py
```

Production code still attempts `evidence.blob_sha` propagation into:

```text
TargetPythonDeclaration.blob_sha
TargetPythonDeclarationProblem.blob_sha
```

The focused test failures happen during stale fixture construction before most semantic Target-Python cases execute, so they do not yet prove a Target semantic regression. They prove an incomplete R1 contract migration.

## 5. Full-suite result

The standard suite was also run to inventory remaining fan-out:

```text
Ran 507 tests in 0.113s
FAILED (failures=5, errors=51)
```

This result is **not** interpreted as 56 independent product bugs. The focused gates show large migrated surfaces are already green, while the Target-Python failure demonstrates at least one stale old-contract family that can cascade into higher-level tests.

Therefore the full-suite result is a migration-pressure inventory. Failures must be grouped by earliest responsible contract before fixes are made.

## 6. What this validation proves now

Runtime-green focused surfaces:

```text
R1 Step 1 exact-file provider/type foundation
R1 Step 2B dependency exact-file extractors
R1 Step 2C uv membership/composition
R1 Target artifact-environment migration
R1 tagged-changelog/upstream exact-source migration
source topology
experiment test package
Python compilation
```

Not yet proven:

```text
Target Python exact-file consumer
all remaining stale exact-file consumers/fixtures
full branch integration
post-main-reconciliation integration
```

The historical `508 tests / OK` baseline remains the last full accepted runtime baseline. This checkpoint adds newer **focused runtime evidence** but does not yet supersede the historical full-suite proof because the current branch full suite is red.

## 7. Branch/reconciliation decision

Do not merge `main` into the migration branch yet.

Reason:

```text
known current R1 migration failures
+ main reconciliation effects
→ mixed failure provenance
```

Required order:

```text
finish remaining R1 contract migrations
→ focused runtime validation
→ full current-branch suite green
→ merge current main INTO SAME migration branch
→ resolve non-destructively
→ affected tests
→ full suite again
```

No second migration branch is justified.

## 8. Exact continuation

Next bounded R1 responsibility trace:

```text
src/upgradepilot/target/python.py
+ tests/test_target_python.py
+ immediate downstream Target-Python relevance/impact/CLI consumers as needed for ownership tracing
```

Question to answer before editing:

> After deriving `[project].requires-python` from one strong exact-head `pyproject.toml`, which source locator/provenance fields does the durable Target-Python declaration actually need, and does `blob_sha` establish any independent Target-Python proposition?

Do not patch the 51/5 full-suite failures individually. Migrate this earliest confirmed stale contract first, rerun its focused/downstream tests later, then regroup the residual full-suite failures.