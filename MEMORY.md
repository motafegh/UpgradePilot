# UpgradePilot Current Memory

**Last updated:** 2026-07-31 18:11 +03:30  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, and exact continuation.

Stable plans, ADRs, source, tests, and dated evidence retain their own responsibilities. This file records only the current state needed to continue.

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Selected plan:** [`plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)
- **Accepted architecture:** [`docs/architecture/ADR-0004-dependency-version-change-evidence.md`](docs/architecture/ADR-0004-dependency-version-change-evidence.md)
- **Step 1 validation:** [`working-memory/2026-07-30_2138_B2-step-1-dependency-contracts-validation.md`](working-memory/2026-07-30_2138_B2-step-1-dependency-contracts-validation.md)
- **Step 2 validation:** [`working-memory/2026-07-31_1612_B2-step-2-exact-requirement-validation.md`](working-memory/2026-07-31_1612_B2-step-2-exact-requirement-validation.md)
- **Step 3 validation:** [`working-memory/2026-07-31_1635_B2-step-3-dependency-comparison-validation.md`](working-memory/2026-07-31_1635_B2-step-3-dependency-comparison-validation.md)
- **Step 4 validation:** [`working-memory/2026-07-31_1729_B2-step-4-exact-pr-file-acquisition-validation.md`](working-memory/2026-07-31_1729_B2-step-4-exact-pr-file-acquisition-validation.md)
- **Step 5 failure/correction evidence:** [`working-memory/2026-07-31_1811_B2-step-5-live-validation-failure-and-correction.md`](working-memory/2026-07-31_1811_B2-step-5-live-validation-failure-and-correction.md)
- **Last fully behavior-validated repository state:** `84fdd422152cd2b098fb88b6245e86b8750add29`.
- **Last fully behavior-validated product-source revision:** `7bb542acf4ca24a89e384f9a9c590345939c8673`.
- **Latest Step 5 product/test correction revision:** `82237ee4b11b1df7182a58cf5913194d8b231eac`.

Later evidence or memory commits do not alter the Step 5 product/test correction revision.

## Current phase

Steps 1–4 are complete and behavior-validated.

Step 5 source and tests are implemented and corrected on `main`:

```text
extract uv.lock changes
```

Step 5 remains **open and unvalidated**. Do not begin Step 6.

## Supplied validation evidence

### Installed S004 regression

The user ran:

```bash
unset GITHUB_TOKEN
upgradepilot googlefonts/glyphsLib 1145
```

Observed behavior remained intact:

```text
requirements-dev.txt
pytest 9.0.2 → 9.0.3
project_table_absent
exact-head CI authority sufficient
pytest==9.0.3
2 of 2 provenance
pytest-dev/pytest release tag 9.0.3
unresolved_claim
```

This establishes installed S004 compatibility for the supplied run.

### First live S001 extraction

The user ran the Step 5 extractor against:

```text
pydantic/pydantic #13432
uv.lock
```

Observed result:

```text
DependencyChangeEvidenceProblem
reason: invalid_dependency_record
detail: The exact base uv.lock package record at index 104 had an invalid non-empty textual 'version'.
```

The failure was correct evidence that the controlled fixtures had missed a valid uv record variant. It did not establish Soup Sieve identity.

## Root cause and corrected boundary

The failing record is a valid editable workspace record:

```toml
[[package]]
name = "pydantic"
source = { editable = "." }
```

A second `pydantic-core` workspace record has the same versionless editable shape.

The initial parser incorrectly required a textual `version` on every package table.

The corrected parser now distinguishes:

```text
version-bearing package record
→ may establish a dependency version transition

versionless editable/virtual workspace record
→ structural context only
```

A missing version is admitted only when `source` is exactly one non-empty textual local source using:

```text
editable
virtual
```

A missing version with a registry, absent, malformed, multi-key, or unknown source remains:

```text
invalid_dependency_record
```

An admitted versionless record:

- participates in normalized-name grouping;
- participates in structural comparison after removing only top-level `sdist` and `wheels`;
- may coexist unchanged with one clear version-bearing transition;
- cannot itself produce `ExtractedDependencyVersionChange`;
- stops as `unsupported_uv_lock_structural_change` if its non-artifact structure changes;
- stops as `unsupported_uv_lock_structural_change` if it gains or loses a textual version.

The correction is generic and contains no S001 repository, package, version, SHA, index, byte count, or expected-answer condition.

## Step 5 implementation boundary

Public API:

```text
src/upgradepilot/uv_lock_change.py
    is_modified_uv_lock_file
    extract_uv_lock_changes
```

Inputs and output:

```text
ChangedFile
+ exact base file evidence
+ exact head file evidence
→ ExtractedDependencyVersionChange
  or DependencyChangeEvidenceProblem
```

Admission remains:

```text
normalized repository-relative POSIX path
+ basename exactly uv.lock
+ status modified
```

Parsing remains:

```text
Python standard-library tomllib
schema version = 1
revision = non-negative integer
package = array of tables
```

Unique version-bearing records require exact source and `resolution-markers` context before an exact raw version change may be extracted.

Repeated normalized-name groups remain provable only as unchanged unordered multisets after removing top-level `sdist` and `wheels`. Changed repeated groups remain `ambiguous_uv_lock_package_records`.

No PEP 440 parsing, ordering, dependency-role inference, CI-consumption inference, compatibility, safety, recommendation, or maintainer-action logic is present.

## Step 5 tests

Existing focused file:

```text
tests/test_uv_lock_change.py
19 tests
```

New regression file:

```text
tests/test_uv_lock_versionless_records.py
5 tests
```

The new tests prove:

1. unchanged editable workspace record does not block another clear transition;
2. unchanged virtual workspace record does not block another clear transition;
3. changed versionless record stops as unsupported structure;
4. missing version with a registry source remains invalid;
5. gaining or losing a version stops as unsupported structure.

Expected focused Step 5 total:

```text
24 tests
```

Expected complete deterministic total if no unrelated tests were added:

```text
125 tests
```

These are expectations, not passing repository results.

## Correction revisions

```text
bf9fb555a328240399601839ddcd815966bace29
Handle versionless uv workspace records

82237ee4b11b1df7182a58cf5913194d8b231eac
Test versionless uv workspace records
```

An isolated Python 3.13.5 harness passed the five new regression cases and representative compatibility scenarios for the prior Step 5 behavior. This is development evidence only.

## Runtime compatibility boundary

The installed CLI still follows the legacy path:

```text
ChangedFile[]
→ extract_pinned_dependency_change
→ PinnedDependencyChange or UnsupportedDependencyChange
```

It does not yet invoke `extract_uv_lock_changes` during normal orchestration.

Step 5 has not modified:

- CLI orchestration;
- exact-requirement extraction behavior;
- PR-wide comparison behavior;
- CI semantics;
- target-Python interpretation;
- PyPI or upstream evidence;
- PEP 440 runtime semantics;
- compatibility, safety, or recommendation logic.

## Learning state

Step 5 has introduced and reviewed:

- TOML parsing with `tomllib`;
- schema version versus schema revision;
- package-table grouping by normalized distribution name;
- unique versus repeated package records;
- unordered multiset comparison;
- artifact versus non-artifact structure;
- explicit abstention on ambiguous resolver branches;
- a structured-record variant in which field absence can be valid only under a narrow source discriminator;
- the distinction between a version-bearing dependency record and versionless workspace context.

Current depth:

```text
structured explanation completed
+ design translated into source and fixtures
+ first live S001 failure observed and diagnosed
+ bounded correction implemented
+ isolated regression and compatibility harness passed
+ installed S004 compatibility supplied
but
real repository focused suite not yet supplied
complete suite not yet supplied
corrected live S001 extraction not yet supplied
no independent implementation practice recorded
no user-owned technical explanation recorded
no formal assessment recorded
not mastered
```

Product behavior validation and learning mastery remain separate claims.

## Exact continuation

Remain inside Step 5.

Run from an updated real checkout:

```bash
git switch main
git pull --ff-only

git rev-parse HEAD
git status --short
python --version
```

Then run the focused Step 5 tests:

```bash
python -m unittest \
  tests.test_uv_lock_change \
  tests.test_uv_lock_versionless_records \
  -v
```

Expected count:

```text
Ran 24 tests
OK
```

Run the complete suite:

```bash
python -m unittest discover -s tests -v
```

Expected count:

```text
Ran 125 tests
OK
```

Repeat the installed anonymous S004 control and the live S001 extraction.

The corrected S001 extraction must establish only:

```text
package: soupsieve
normalized package: soupsieve
old version: 2.6
proposed version: 2.8.4
path: uv.lock
```

It must preserve the Step 4 exact base/head revisions, blob SHAs, and byte counts.

After all evidence is supplied, create the dated Step 5 validation record, update this memory, and only then discuss Step 6.

## Not established

- corrected Step 5 focused-suite pass;
- corrected complete-suite pass;
- corrected live S001 Soup Sieve extraction;
- PR-wide comparison using live `uv.lock` evidence;
- CLI orchestration through the shared dependency flow;
- `uv.lock` CI-consumption semantics;
- downstream `DependencyVersionChange` migration;
- `DependencyCIExerciseResult` runtime behavior;
- PEP 440 runtime semantics;
- Python-support relevance;
- compatibility, safety, maintainer action, or production readiness;
- mastery of Steps 1–5 concepts.

## State-maintenance rule

When route, selected plan, verified behavior, blocker, learning state, or exact continuation changes, update this file only. Change another file only when its stable responsibility or dated evidence changes.
