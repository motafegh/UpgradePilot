# UpgradePilot Current Memory

**Last updated:** 2026-07-31 21:57 +03:30  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, and exact continuation.

Stable plans, ADRs, source, tests, and dated evidence retain their own responsibilities. This file records only the current state needed to continue.

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Completed dependency-foundation plan:** [`plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)
- **Completed Step 8 plan:** [`plans/B2_STEP_8_MULTI_FORMAT_COMMAND_INTEGRATION_PLAN.md`](plans/B2_STEP_8_MULTI_FORMAT_COMMAND_INTEGRATION_PLAN.md)
- **Dependency architecture:** [`docs/architecture/ADR-0004-dependency-version-change-evidence.md`](docs/architecture/ADR-0004-dependency-version-change-evidence.md)
- **Step 8 implementation:** [`working-memory/2026-07-31_2123_B2-step-8-multi-format-command-integration-implementation.md`](working-memory/2026-07-31_2123_B2-step-8-multi-format-command-integration-implementation.md)
- **Step 8 public-case validation:** [`working-memory/2026-07-31_2153_B2-step-8-public-cases-partial-validation.md`](working-memory/2026-07-31_2153_B2-step-8-public-cases-partial-validation.md)
- **Final Step 8 validation:** [`working-memory/2026-07-31_2157_B2-step-8-multi-format-command-integration-validation.md`](working-memory/2026-07-31_2157_B2-step-8-multi-format-command-integration-validation.md)
- **Behavior-validated Step 8 product/test revision:** `16c74f887d960a5e2dede56d05d7a55c16395a08`.
- **Final Step 8 validation-record revision:** `319b725769e5ece686b773429f78e82fec7cee19`.
- **Selected next plan:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)

Later validation and memory commits do not alter the behavior-validated Step 8 product/test revision.

## Current phase

The dependency-version-change evidence foundation is complete and behavior-validated.

Completed foundation sequence:

```text
shared dependency contracts
→ exact-requirements / constraints extraction
→ PR-wide comparison
→ exact base/head repository-file acquisition
→ uv.lock extraction
→ canonical downstream migration
→ CI dependency-exercise migration
→ multi-format installed command integration
→ deterministic and public-case validation
```

The prerequisite required by the target Python support relevance plan is now satisfied.

The selected next bounded step is:

```text
B2 Target Python Support Relevance Plan
Step 1 — Freeze upstream interval and source authority
```

Do not return to dependency-parser implementation or begin target comparison, LLM extraction, conditional CLI orchestration, compatibility, safety, or recommendation logic before Step 1 authority contracts are frozen.

## Validated dependency foundation

### One active multi-format coordinator

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

Command boundary:

```text
PullRequestIdentity
+ complete ChangedFile[]
+ GitHubRepositoryClient
        │
        ├── requirements / constraints patch extraction
        └── modified uv.lock exact base/head extraction
                         │
                         ▼
        compare_extracted_dependency_changes
                         │
            ┌────────────┴────────────┐
            ▼                         ▼
DependencyChangeAnalysis   DependencyChangeEvidenceProblem
            │
            ├── DependencyVersionChange
            └── direct_requirements_install_path: str | None
```

No source-specific parser branch remains in `cli.py`.

### Requirements, constraints, and CI input

```text
is_exact_requirement_file
→ admits requirements and constraints as dependency evidence

is_admitted_requirements_file
→ identifies requirements-family paths only
```

A direct requirements path is exposed to the current CI rule only when exactly one successful requirements-family source supports the trusted transition.

```text
one requirements path → that path
zero requirements paths → None
several requirements paths → None
constraints only → None
uv.lock only → None
```

Path admission does not itself prove installation. The CI evaluator still requires visible installation of the explicit path plus direct changed-package invocation in successful exact-head CI.

### Structured lockfile boundary

```text
is_uv_lock_file
→ exact normalized lowercase uv.lock path recognition

is_modified_uv_lock_file
→ current modified-status extraction admission
```

Recognized modified `uv.lock` files use exact immutable PR base/head acquisition. Added, deleted, or renamed lockfiles remain explicit unsupported-status results.

### PR-wide trust

Every recognized extraction success and evidence problem reaches:

```text
compare_extracted_dependency_changes
```

Validated outcomes include:

- one trusted transition;
- equivalent evidence with combined source records;
- conflicting exact transitions;
- several changed packages;
- recognized malformed or unavailable evidence blocking convenient success;
- no supported dependency file;
- exact source provenance preservation.

## Deterministic validation

The user reported that all required Step 8 tests passed:

```text
focused Step 8 suite: passed
complete deterministic suite: passed
```

The focused suite covered:

```text
tests.test_dependency_analysis
tests.test_step8_source_recognition
tests.test_exact_requirement_change
tests.test_cli
tests.test_package_interface
```

The exact final terminal summary lines and timings were not supplied, so they are not invented. The pass result is recorded from the user's explicit report.

## Public S001 validation

Observed installed command:

```bash
unset GITHUB_TOKEN
upgradepilot pydantic/pydantic 13432
```

Validated dependency evidence:

```text
Repository: pydantic/pydantic
PR: 13432
Changed file: uv.lock (modified)
Package: soupsieve
Old version: 2.6
Proposed version: 2.8.4
Format: uv_lock
Extraction method: exact_base_head_files
```

Validated exact provenance:

```text
base revision: 652a61ce4f9d7d76eaada31535807a485ece0e21
base blob: b4a68ab725de337889d50d5374ac0f05db7fb484
base bytes: 606307
head revision: aa2dc024d33f61cdef50bf1973ab5adf0a974f5a
head blob: def33fe05d78ab851ce91a33db5bc55a439873a1
head bytes: 606313
```

Validated downstream results:

```text
Target requires-python: >=3.10
CI dependency exercise: unresolved
CI dependency exercise reason: dependency_exercise_not_proven
Published package: soupsieve==2.8.4
Distribution files: 2
Upstream source: unsupported_source
```

The unresolved CI result is correct. Successful exact-head CI existed, but no admitted rule proved `uv.lock` consumption and Soup Sieve exercise. Generic evidence paths were not promoted into installation proof.

The upstream source problem is independent. It does not invalidate dependency identity, exact provenance, target evidence, CI classification, or package evidence.

## Public S004 regression validation

Observed installed command:

```bash
unset GITHUB_TOKEN
upgradepilot googlefonts/glyphsLib 1145
```

Preserved result:

```text
requirements-dev.txt
pytest 9.0.2 → 9.0.3
CI dependency exercise: proven
CI dependency exercise reason: exact_head_dependency_exercised
published pytest==9.0.3
2 of 2 provenance
pytest-dev/pytest tag 9.0.3
unresolved_claim
```

The `Regression Tests` workflow remained proven through visible installation of `requirements-dev.txt` and direct invocation of `pytest`. The multi-job `Test + Deploy` workflow remained unresolved.

S001 and S004 do not need to be repeated unless later product-source changes touch their active paths.

## Completed dependency-foundation stop line

Established:

```text
materially different admitted dependency representations
→ one representation-neutral DependencyVersionChange
   or explicit unsupported, ambiguous, multiple, incomplete, unavailable,
   malformed, structural, or conflicting evidence result
```

The completed parent plan owns and has validated:

- source-specific dependency interpreters;
- exact base/head structured-file acquisition;
- canonical package/old-version/proposed-version identity;
- deterministic PR-wide reconciliation;
- evidence-path versus CI-consumption separation;
- S004 exact-requirements preservation;
- S001 `uv.lock` dependency-transition admission;
- canonical downstream and CI contract migration;
- installed multi-format command integration.

The dependency-version-change evidence plan is closed.

## Selected next plan

```text
plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md
```

Purpose:

```text
trusted DependencyVersionChange
→ authoritative upstream evidence across old_version < release <= proposed_version
→ one grounded Python support-drop claim
+ exact-head target [project].requires-python
→ declared overlap, declared non-overlap, or unresolved relevance
```

This remains a relevance result only. It is not a compatibility, safety, merge, or recommendation result.

### Next bounded step

```text
Step 1 — Freeze upstream interval and source authority
```

Required design and tests:

1. exact old-version-exclusive/proposed-version-inclusive interval identity;
2. admitted exact GitHub Release and tagged-changelog source records;
3. authoritative source ordering;
4. exact release/tag/revision/path/blob provenance;
5. unavailable, incomplete, ambiguous, and conflicting source states;
6. rejection of arbitrary documentation search and model-selected authority;
7. prevention of final-release-only evidence from hiding changes introduced in intermediate crossed releases.

### Exact continuation

Before product implementation:

1. inspect the selected target-relevance plan in full;
2. inspect current package, provenance, upstream-source, GitHub release, repository-file, target-Python, and CLI contracts;
3. inspect S001 product-simulation evidence and existing working-memory records relevant to the Soup Sieve 2.6 → 2.8.4 interval;
4. determine the exact authoritative source representations and acquisition gaps;
5. create a focused Step 1 plan if the parent step is too terse to control interval identity, source precedence, provenance, and problem states;
6. freeze controlled tests before source changes.

Do not add an LLM, Instructor, arbitrary web search, target range comparison, or conditional CLI reordering during Step 1.

## Not established

- authoritative crossed-release interval acquisition;
- a trusted upstream Python support-drop claim;
- `packaging` version/specifier runtime admission;
- Python-line overlap comparison;
- conditional target-Python activation;
- S001 `outside_declared_python_range` result;
- `uv.lock`, constraints, or another new CI-consumption rule;
- compatibility, safety, recommendation, maintainer action, or production readiness;
- user mastery.

## Learning state

Dependency-foundation concepts introduced, implemented, and behavior-validated:

- canonical domain models;
- source-specific interpretation behind a static coordinator;
- immutable base/head and blob provenance;
- PR-wide evidence comparison;
- recognized-problem precedence;
- dependency identity versus CI operational evidence;
- visible unresolved states;
- localized extension boundaries;
- compatibility migration and deliberate retirement of temporary contracts.

Current depth:

```text
structured explanations completed
+ architecture and focused plans reviewed
+ tests written before implementation
+ source implementation reviewed
+ focused and complete deterministic tests reported passing
+ installed S004 and S001 behavior observed
but
no user-owned technical explanation recorded
no independent implementation practice recorded
no formal assessment recorded
not mastered
```

Product behavior validation and learning mastery remain separate claims.

## State-maintenance rule

When route, selected plan, verified behavior, blocker, learning state, or exact continuation changes, update this file only. Change another file only when its stable responsibility or dated evidence changes.
