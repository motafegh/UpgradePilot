# UpgradePilot Current Memory

**Last updated:** 2026-07-31 21:23 +03:30  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, and exact continuation.

Stable plans, ADRs, source, tests, and dated evidence retain their own responsibilities. This file records only the current state needed to continue.

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Parent plan:** [`plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)
- **Step 8 controlling plan:** [`plans/B2_STEP_8_MULTI_FORMAT_COMMAND_INTEGRATION_PLAN.md`](plans/B2_STEP_8_MULTI_FORMAT_COMMAND_INTEGRATION_PLAN.md)
- **Accepted architecture:** [`docs/architecture/ADR-0004-dependency-version-change-evidence.md`](docs/architecture/ADR-0004-dependency-version-change-evidence.md)
- **Step 7 validation:** [`working-memory/2026-07-31_2112_B2-step-7-ci-dependency-exercise-validation.md`](working-memory/2026-07-31_2112_B2-step-7-ci-dependency-exercise-validation.md)
- **Step 8 implementation:** [`working-memory/2026-07-31_2123_B2-step-8-multi-format-command-integration-implementation.md`](working-memory/2026-07-31_2123_B2-step-8-multi-format-command-integration-implementation.md)
- **Behavior-validated Step 7 product/test revision:** `93f93dd2da10bc98cf1b14363f2164eefbee75c1`.
- **Latest Step 8 product/test implementation revision:** `16c74f887d960a5e2dede56d05d7a55c16395a08`.
- **Step 8 implementation-record revision:** `7b58a56f6f491c7cd9e537566ea3b078e2a9af89`.

Later implementation-record and memory commits do not alter the Step 8 product/test revision.

## Current phase

Steps 1–7 are complete and behavior-validated.

Step 8 is fully implemented in source and controlled tests but remains **open and unvalidated**:

```text
integrate the multi-format dependency command path
```

Do not close the parent dependency-evidence plan or return to Python-support relevance before Step 8 validation is complete.

## Last validated boundary

Observed Step 7 complete suite:

```text
Ran 138 tests in 0.033s
OK
```

Observed installed S004:

```text
requirements-dev.txt
pytest 9.0.2 → 9.0.3
CI dependency exercise: proven
exact_head_dependency_exercised
pytest==9.0.3
2 of 2 provenance
pytest-dev/pytest tag 9.0.3
unresolved_claim
```

## Step 8 implemented boundary

### One active coordinator

Created:

```text
src/upgradepilot/dependency_analysis.py
```

Active contracts:

```text
DependencyChangeAnalysis
DependencyChangeAnalysisResult
analyze_dependency_change
is_uv_lock_file
```

Successful coordinator result:

```text
DependencyChangeAnalysis
├── dependency: DependencyVersionChange
└── direct_requirements_install_path: str | None
```

The active CLI calls the coordinator once with:

```text
PullRequestIdentity
+ complete ChangedFile[]
+ GitHubRepositoryClient
```

No source-specific parser branch remains in `cli.py`.

### Source coordination

Requirements and constraints:

```text
is_exact_requirement_file
→ extract_exact_requirement_changes
```

Requirements-family role:

```text
is_admitted_requirements_file
```

This narrower helper distinguishes requirements from constraints. It does not prove installation.

Structured lockfile:

```text
is_uv_lock_file
→ path-only exact lowercase uv.lock recognition

is_modified_uv_lock_file
→ modified-status extraction admission
```

Coordinator behavior:

```text
recognized non-modified uv.lock
→ unsupported_dependency_file_status
→ no exact-file acquisition

recognized modified uv.lock
→ exact PR base file
→ exact PR head file
→ extract_uv_lock_changes
```

Arbitrary files are ignored.

### PR-wide trust

Every recognized success and problem reaches:

```text
compare_extracted_dependency_changes
```

The coordinator does not prefer requirements, constraints, or `uv.lock`.

Validated component semantics preserved in source:

- equivalent evidence may combine source records;
- conflicting raw transitions remain explicit;
- several changed packages remain explicit;
- a recognized problem cannot be hidden by another convenient success;
- unavailable exact lockfile text remains a dependency evidence problem.

### Direct-requirements CI input

The coordinator emits a path only when exactly one distinct successful requirements-family source supports the trusted transition.

```text
one requirements path → that path
zero requirements paths → None
several requirements paths → None
```

Constraints and `uv.lock` never populate the path.

The Step 7 evaluator still must prove visible installation of the explicit path and direct package invocation.

### Temporary ingress retired

Removed from active source:

```text
LegacyDependencyIngress
LegacyDependencyIngressResult
extract_legacy_dependency_ingress
```

Removed test:

```text
tests/test_legacy_dependency_ingress.py
```

Retained historical compatibility API:

```text
PinnedDependencyChange
UnsupportedDependencyChange
extract_pinned_dependency_change
```

The retained API is not used by the active command.

### Package interface

New exports:

```text
DependencyChangeAnalysis
DependencyChangeAnalysisResult
analyze_dependency_change
is_admitted_requirements_file
is_uv_lock_file
```

## Controlled test boundary

Step 8 focused files:

```text
tests/test_dependency_analysis.py: 12
tests/test_step8_source_recognition.py: 2
tests/test_exact_requirement_change.py: 11
tests/test_cli.py: 9
tests/test_package_interface.py: 2
```

Expected focused total:

```text
36 tests
```

Expected complete deterministic total:

```text
153 tests
```

These are derived counts, not observed passing results.

## Validation status

No Step 8 repository test pass, installed S004 pass, or installed S001 pass is claimed.

The GitHub connector exposes no repository test runner and reported no combined status for `16c74f887d960a5e2dede56d05d7a55c16395a08`.

## Exact continuation

From the real checkout:

```bash
git switch main
git pull --ff-only

python -m unittest \
  tests.test_dependency_analysis \
  tests.test_step8_source_recognition \
  tests.test_exact_requirement_change \
  tests.test_cli \
  tests.test_package_interface \
  -v

python -m unittest discover -s tests -v
```

Expected:

```text
focused: Ran 36 tests / OK
complete: Ran 153 tests / OK
```

### Installed S004 regression

```bash
unset GITHUB_TOKEN
upgradepilot googlefonts/glyphsLib 1145
```

Required material behavior:

```text
pytest 9.0.2 → 9.0.3
requirements-dev.txt exact_requirement evidence
CI dependency exercise: proven
exact_head_dependency_exercised
published pytest==9.0.3
2 of 2 provenance
pytest-dev/pytest tag 9.0.3
unresolved_claim
```

### Installed S001 integration

```bash
unset GITHUB_TOKEN
upgradepilot pydantic/pydantic 13432
```

Required dependency result:

```text
Package: soupsieve
Old version: 2.6
Proposed version: 2.8.4
Dependency evidence: uv.lock
Format: uv_lock
Extraction method: exact_base_head_files
```

Required exact provenance:

```text
base revision: 652a61ce4f9d7d76eaada31535807a485ece0e21
base blob: b4a68ab725de337889d50d5374ac0f05db7fb484
base bytes: 606307
head revision: aa2dc024d33f61cdef50bf1973ab5adf0a974f5a
head blob: def33fe05d78ab851ce91a33db5bc55a439873a1
head bytes: 606313
```

Required CI boundary when successful exact-head CI exists:

```text
CI dependency exercise: unresolved
CI dependency exercise reason: dependency_exercise_not_proven
```

Package, upstream, and target evidence must continue independently and report their own states.

After all four proofs are supplied, create the dated Step 8 validation record, close Step 8 and the parent dependency-evidence plan, and select the next authorized route through this memory.

## Not established

- Step 8 focused-suite pass;
- Step 8 complete-suite pass;
- post-integration S004 behavior;
- one-line installed S001 behavior;
- `uv.lock`, constraints, or another new CI-consumption rule;
- PEP 440 semantics;
- Python-support relevance;
- compatibility, safety, recommendation, maintainer action, or production readiness;
- user mastery.

## Learning state

Step 8 concepts introduced and implemented:

- orchestration versus source-specific parsing;
- static coordinator extension boundary;
- PR-wide evidence comparison;
- requirements evidence versus constraints evidence versus CI operational input;
- path recognition versus status admission;
- normal evidence problems versus exceptional acquisition failures;
- removal of a temporary compatibility boundary after migration.

Current depth:

```text
structured explanation completed
+ focused plan created
+ tests written before source
+ coordinator and CLI integration implemented
+ package interface migrated
+ temporary ingress retired
+ implementation diff reviewed
but
repository execution not yet observed
installed S001 not yet observed
no user-owned technical explanation recorded
no independent implementation practice recorded
no formal assessment recorded
not mastered
```

Product behavior validation and learning mastery remain separate claims.

## State-maintenance rule

When route, selected plan, verified behavior, blocker, learning state, or exact continuation changes, update this file only. Change another file only when its stable responsibility or dated evidence changes.
