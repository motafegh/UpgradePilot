# B2 Step 5 — `uv.lock` extraction validation

**Recorded:** 2026-07-31 18:54 +03:30  
**Route:** B2 — Public PR vertical slice  
**Step:** 5 — Extract `uv.lock` changes  
**Status:** Complete and behavior-validated

## Validated implementation

Step 5 product/test correction revision:

```text
82237ee4b11b1df7182a58cf5913194d8b231eac
```

Validated repository state before this evidence-only record:

```text
0925b9e2bf146be920f50f584201f346094743f0
```

The later state contains the Step 5 implementation, versionless workspace correction, regression tests, prior failure/correction evidence, and post-correction S004 partial validation. No product source or tests changed after `82237ee...`.

## Checkout and interpreter evidence

The user ran:

```bash
git switch main
git pull --ff-only

git rev-parse HEAD
git status --short
python --version
```

Observed:

```text
already on main
branch up to date with origin/main
fast-forward to 0925b9e2bf146be920f50f584201f346094743f0
git status --short produced no output
Python 3.12.3
```

This establishes the exact local revision, clean working tree, and required Python 3.12 runtime for the deterministic validation.

## Focused deterministic validation

Command:

```bash
python -m unittest \
  tests.test_uv_lock_change \
  tests.test_uv_lock_versionless_records \
  -v
```

Observed:

```text
Ran 24 tests in 0.004s
OK
```

The focused tests prove:

- exact modified `uv.lock` path admission;
- exact base/head identity and provenance reconciliation;
- TOML, schema, revision, package-name, and version validation;
- one exact version transition;
- unchanged, added/removed, several-change, source-change, marker-change, and structural-change outcomes;
- artifact-only `sdist`/`wheels` differences do not create transitions;
- unchanged duplicate groups remain admissible context;
- changed duplicate groups remain ambiguous;
- unchanged editable and virtual versionless workspace records do not block another clear transition;
- changed or inconsistently versioned workspace records stop explicitly;
- missing versions outside the admitted local-workspace source boundary remain invalid.

## Complete deterministic validation

Command:

```bash
python -m unittest discover -s tests -v
```

Observed:

```text
Ran 125 tests in 0.030s
OK
```

This preserves all previously validated repository behavior together with the Step 5 parser and correction.

## Installed S004 regression

The post-correction installed anonymous command was already supplied and recorded:

```bash
unset GITHUB_TOKEN
upgradepilot googlefonts/glyphsLib 1145
```

Observed behavior remained:

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

This proves the Step 5 source-specific correction did not regress the existing installed exact-requirements path.

## Public S001 live extraction

Public case:

```text
pydantic/pydantic #13432
uv.lock
```

Observed live result:

```text
ExtractedDependencyVersionChange
package: soupsieve
normalized package: soupsieve
old version: 2.6
proposed version: 2.8.4
path: uv.lock
file format: uv_lock
extraction method: exact_base_head_files
base revision: 652a61ce4f9d7d76eaada31535807a485ece0e21
base blob: b4a68ab725de337889d50d5374ac0f05db7fb484
base bytes: 606307
head revision: aa2dc024d33f61cdef50bf1973ab5adf0a974f5a
head blob: def33fe05d78ab851ce91a33db5bc55a439873a1
head bytes: 606313
```

The revisions, blob SHAs, and byte counts exactly match the Step 4 acquisition evidence.

## What Step 5 now proves

UpgradePilot can deterministically interpret one admitted modified same-path `uv.lock` by:

```text
exact base/head repository files
→ TOML schema and package-record validation
→ normalized package grouping
→ conservative unique/duplicate comparison
→ one ExtractedDependencyVersionChange
   or an explicit evidence problem
```

S001 now establishes only the bounded file-level identity:

```text
soupsieve 2.6 → 2.8.4
```

with complete source provenance.

The implementation contains no S001 repository, package, version, SHA, byte count, record index, or expected-answer condition.

## Boundaries preserved

Step 5 does not yet establish:

- PR-wide trusted `DependencyVersionChange` for live S001 orchestration;
- one-line installed S001 CLI behavior;
- `uv.lock` CI consumption or exercise;
- downstream migration away from `PinnedDependencyChange`;
- PEP 440 validity or forward ordering;
- target-Python relevance;
- compatibility, safety, recommendation, or maintainer action.

The installed CLI still follows the legacy exact-requirements dependency path.

## Learning state

Observed learning exposure includes:

- TOML and `tomllib`;
- lock schema version versus revision;
- package records and normalized identity;
- unique records versus repeated resolver branches;
- unordered multiset comparison;
- artifact versus structural metadata;
- valid version absence under editable/virtual workspace sources;
- file-level extraction versus PR-wide trust;
- live-case failure as evidence for refining a generic boundary.

Current depth remains:

```text
introduced and reviewed
+ implementation and tests inspected
+ real failure diagnosed
+ corrected behavior validated
but
no independent implementation practice recorded
no user-owned technical explanation recorded
no formal assessment recorded
not mastered
```

## Continuation

Step 5 is closed.

Proceed to Step 6 of the controlling plan:

```text
migrate downstream dependency input
```

Step 6 must replace downstream dependence on `PinnedDependencyChange` with the trusted shared `DependencyVersionChange` while preserving S004 behavior and preventing dependency-file paths from automatically becoming installation evidence.

Do not start Step 7 CI-result migration or Step 8 command integration before Step 6 is behavior-validated.
