# UpgradePilot Current Memory

**Last updated:** 2026-07-31 18:26 +03:30  
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
- **Step 5 failure/correction:** [`working-memory/2026-07-31_1811_B2-step-5-live-validation-failure-and-correction.md`](working-memory/2026-07-31_1811_B2-step-5-live-validation-failure-and-correction.md)
- **Post-correction S004 partial validation:** [`working-memory/2026-07-31_1826_B2-step-5-post-correction-s004-partial-validation.md`](working-memory/2026-07-31_1826_B2-step-5-post-correction-s004-partial-validation.md)
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

Step 5 remains **open and only partially validated**. Do not begin Step 6.

## Step 5 correction boundary

The first live S001 run exposed valid versionless editable workspace records such as:

```toml
[[package]]
name = "pydantic"
source = { editable = "." }
```

The corrected parser now distinguishes:

```text
version-bearing package record
→ may establish a dependency version transition

versionless editable/virtual workspace record
→ structural context only
```

A missing version is admitted only for one exact non-empty textual `editable` or `virtual` source. Registry, absent, malformed, multi-key, and unknown sources remain `invalid_dependency_record`.

Versionless records:

- participate in normalized-name grouping and structural comparison;
- may coexist unchanged with one clear version-bearing transition;
- cannot produce `ExtractedDependencyVersionChange`;
- stop as `unsupported_uv_lock_structural_change` if they change structure or gain/lose a textual version.

Correction revisions:

```text
bf9fb555a328240399601839ddcd815966bace29
Handle versionless uv workspace records

82237ee4b11b1df7182a58cf5913194d8b231eac
Test versionless uv workspace records
```

## Partial validation now established

The user reran after the correction:

```bash
unset GITHUB_TOKEN
upgradepilot googlefonts/glyphsLib 1145
```

Observed S004 behavior remained intact:

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

This proves that the post-correction installed package and legacy exact-requirements path still work for S004. It also preserves the existing target-Python, workflow, CI-authority, package, provenance, and upstream-release behavior for that case.

The supplied transcript did not include `git rev-parse HEAD`, `git status --short`, or `python --version`, so the exact local commit, clean-tree state, and interpreter version remain unverified for that run.

Do not repeat S004 again for this correction unless later source changes touch the legacy path or another regression appears.

## Remaining Step 5 validation gates

Focused suite:

```bash
python -m unittest \
  tests.test_uv_lock_change \
  tests.test_uv_lock_versionless_records \
  -v
```

Expected:

```text
Ran 24 tests
OK
```

Complete suite:

```bash
python -m unittest discover -s tests -v
```

Expected:

```text
Ran 125 tests
OK
```

Corrected live S001 extraction must establish only:

```text
package: soupsieve
normalized package: soupsieve
old version: 2.6
proposed version: 2.8.4
path: uv.lock
```

It must preserve the Step 4 exact base/head revisions, blob SHAs, and byte counts.

## Runtime boundary

The installed CLI still follows the legacy path:

```text
ChangedFile[]
→ extract_pinned_dependency_change
→ PinnedDependencyChange or UnsupportedDependencyChange
```

It does not yet invoke `extract_uv_lock_changes` during normal orchestration.

Step 5 has not modified:

- CLI orchestration;
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
- package grouping by normalized distribution name;
- unique versus repeated package records;
- unordered multiset comparison;
- artifact versus non-artifact structure;
- explicit abstention on ambiguous resolver branches;
- valid field absence under a narrow source discriminator;
- version-bearing dependency records versus versionless workspace context.

Current depth:

```text
structured explanation completed
+ design translated into source and fixtures
+ first live S001 failure observed and diagnosed
+ bounded correction implemented
+ post-correction S004 compatibility observed
but
focused 24-test repository suite not yet supplied
complete 125-test suite not yet supplied
corrected live S001 extraction not yet supplied
no independent implementation practice recorded
no user-owned technical explanation recorded
no formal assessment recorded
not mastered
```

Product behavior validation and learning mastery remain separate claims.

## Exact continuation

Remain inside Step 5.

From the updated checkout, run:

```bash
git switch main
git pull --ff-only

git rev-parse HEAD
git status --short
python --version

python -m unittest \
  tests.test_uv_lock_change \
  tests.test_uv_lock_versionless_records \
  -v

python -m unittest discover -s tests -v
```

Then rerun the corrected live S001 extraction script.

After the 24 focused tests, 125 complete tests, and corrected S001 extraction are supplied, create the dated Step 5 validation record, update this memory, and only then discuss Step 6.

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
