# UpgradePilot Current Memory

**Last updated:** 2026-07-31 17:36 +03:30  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, and exact continuation.

Stable plans, ADRs, source, tests, and dated validation records retain their own responsibilities. This file records only the current state needed to continue.

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Selected plan:** [`plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)
- **Accepted architecture:** [`docs/architecture/ADR-0004-dependency-version-change-evidence.md`](docs/architecture/ADR-0004-dependency-version-change-evidence.md)
- **Step 1 validation:** [`working-memory/2026-07-30_2138_B2-step-1-dependency-contracts-validation.md`](working-memory/2026-07-30_2138_B2-step-1-dependency-contracts-validation.md)
- **Step 2 validation:** [`working-memory/2026-07-31_1612_B2-step-2-exact-requirement-validation.md`](working-memory/2026-07-31_1612_B2-step-2-exact-requirement-validation.md)
- **Step 3 validation:** [`working-memory/2026-07-31_1635_B2-step-3-dependency-comparison-validation.md`](working-memory/2026-07-31_1635_B2-step-3-dependency-comparison-validation.md)
- **Step 4 validation:** [`working-memory/2026-07-31_1729_B2-step-4-exact-pr-file-acquisition-validation.md`](working-memory/2026-07-31_1729_B2-step-4-exact-pr-file-acquisition-validation.md)
- **Last behavior-validated repository state:** `84fdd422152cd2b098fb88b6245e86b8750add29`.
- **Last behavior-validated product-source revision:** `7bb542acf4ca24a89e384f9a9c590345939c8673`.
- **Latest Step 5 product/test implementation revision:** `137fe282c9d372be7b21708011e1d8bcb46b9fbd`.

Later memory-only commits do not alter the Step 5 product/test implementation revision.

## Current phase

Steps 1–4 are complete and behavior-validated.

Step 5 source and focused tests are implemented on `main`:

```text
extract uv.lock changes
```

Step 5 is **not yet behavior-validated** in the real Python 3.12 checkout or through live S001 extraction.

Do not begin Step 6.

## Last validated boundary

Observed before Step 5:

```text
complete deterministic suite: 101 passed
installed anonymous S004 command: passed
live S001 exact base/head uv.lock acquisition: passed
```

Step 5 extends this boundary only after its focused tests, the complete suite, installed S004 regression, and live S001 extraction pass.

## Step 5 implementation

Added:

```text
src/upgradepilot/uv_lock_change.py
```

Public API:

```text
is_modified_uv_lock_file
extract_uv_lock_changes
```

Package-level imports are available:

```python
from upgradepilot import is_modified_uv_lock_file, extract_uv_lock_changes
```

### Admission

A file is admitted only when it has:

```text
normalized repository-relative POSIX path
+ basename exactly uv.lock
+ GitHub status modified
```

Added, deleted, renamed, uppercase, absolute, traversal, repeated-separator, and backslash paths remain unsupported.

### Input and result

```text
ChangedFile
+ exact base file evidence
+ exact head file evidence
→ ExtractedDependencyVersionChange
  or DependencyChangeEvidenceProblem
```

The result is file-level evidence, not the final PR-wide trusted change.

### TOML and schema

The implementation uses Python standard-library `tomllib` and adds no runtime dependency.

Admitted structure:

```text
version = 1
revision = non-negative integer
package = array of tables
```

Distinct stopping states include:

- malformed TOML or schema controls → `malformed_dependency_file`;
- another integer schema version → `unsupported_uv_lock_schema`;
- unusable package array or package record → `invalid_dependency_record`.

Package records require a non-empty admitted distribution name and a non-empty exact version string without surrounding whitespace. Package identity uses the shared normalized-name rule. Extraction does not perform PEP 440 parsing or ordering.

### Unique package records

One base and one head record may form a transition only when:

```text
normalized package identity agrees
source structure agrees exactly
resolution-markers structure agrees exactly
exact version strings differ
```

Attached dependency/package metadata may change with a version transition.

A same-version unique record with another non-artifact structural change produces:

```text
unsupported_uv_lock_structural_change
```

### Repeated-name groups

The implementation proves a repeated group unchanged by:

1. removing only top-level `sdist` and `wheels`;
2. retaining every other known or unknown parsed field;
3. preserving internal list order;
4. comparing records as an unordered multiset with multiplicity.

```text
unchanged duplicate group
→ does not block another clear transition

changed duplicate group
→ ambiguous_uv_lock_package_records
```

It does not pair repeated records by position, select one record, normalize marker meaning, or implement uv resolver semantics.

### Structural outcomes

- artifact-only `sdist`/`wheels` differences do not create transitions;
- package addition/removal, source change, resolution-context change, and same-version non-artifact change remain explicit stopping results;
- several unambiguous changed packages → `multiple_dependency_version_changes`;
- no changed package → `version_unchanged`.

### Exact source evidence

Successful extraction preserves:

```text
complete path
file_format = uv_lock
extraction_method = exact_base_head_files
base revision/blob/byte count
head revision/blob/byte count
```

Repository/path contradictions, missing revision/blob identity, or inconsistent byte evidence stop as `invalid_dependency_record` before TOML interpretation.

## Step 5 tests

Added:

```text
tests/test_uv_lock_change.py
```

Nineteen focused tests cover:

- path and modified-status admission;
- one successful normalized transition with exact provenance;
- unavailable or contradictory exact files;
- malformed TOML and unsupported schema;
- invalid schema controls and package records;
- unchanged, added, removed, and several changed packages;
- source and resolution-marker changes;
- same-version structural change;
- artifact-only change;
- unchanged duplicate groups;
- changed duplicate groups.

Fixtures are case-neutral. No S001 repository, package, version, SHA, byte count, or expected answer is hardcoded.

Expected deterministic total if no unrelated tests were added:

```text
120 tests
```

This is an expectation, not a passing result.

## Step 5 revisions

```text
6c57032cc850ea00ee3406bb2ede93d39bdb1121
Test uv lock dependency extraction

8ee2f5135e7af9140a15987b4205be93c4addb0e
Extract uv lock dependency changes

eb2d3a6353f4963e4d7a55ec0e54097602a8cc5d
Validate uv lock package names

137fe282c9d372be7b21708011e1d8bcb46b9fbd
Export uv lock extraction API
```

An isolated Python 3.13.5 syntax and behavior harness exercised the same 19 scenario groups successfully. This is development feedback only; it is not repository behavior validation and does not replace the Python 3.12 suite.

## Real S001 structural review

The exact Step 4 files contain one Soup Sieve record at each revision:

```text
base: soupsieve 2.6, PyPI registry source
head: soupsieve 2.8.4, same PyPI registry source
```

Neither record is split by `resolution-markers`; the surrounding changed fields are version and package artifacts. This matches the generic unique-record rule without a case-specific exception.

This review is not live product validation.

## Runtime compatibility boundary

The installed CLI still follows:

```text
ChangedFile[]
→ extract_pinned_dependency_change
→ PinnedDependencyChange or UnsupportedDependencyChange
```

It does not yet invoke `extract_uv_lock_changes`, acquire dependency base/head files during normal orchestration, or pass lockfile results through `compare_extracted_dependency_changes`.

Step 5 did not modify:

- CLI orchestration;
- exact-requirement behavior;
- PR-wide comparator behavior;
- CI semantics;
- target-Python interpretation;
- PyPI/upstream evidence;
- PEP 440 semantics;
- compatibility, safety, or recommendation logic.

## Learning state

Step 5 introduced and reviewed:

- **TOML — Tom's Obvious Minimal Language**;
- **`tomllib`** — Python's standard-library TOML parser;
- **array of tables** — repeated `[[package]]` sections parsed into a list;
- **normalized-name grouping**;
- **source and resolution-marker context**;
- **artifact metadata** — `sdist` and `wheels`;
- **unordered multiset** — order-independent records with duplicate counts preserved;
- **conservative abstention** for changed duplicate resolver branches;
- **raw version preservation** without PEP 440 interpretation.

Current depth:

```text
structured explanation completed
+ ADR rules revisited during implementation
+ real S001 record shape inspected
+ focused tests and source implemented
+ isolated syntax/behavior harness completed
but
no real repository execution recorded
no installed S004 regression recorded after Step 5
no live S001 extraction recorded
no independent implementation practice recorded
no user-owned technical explanation recorded
no formal assessment recorded
not mastered
```

Product behavior validation and learning mastery remain separate claims.

## Exact continuation

Synchronize and capture the actual checkout state rather than assuming a self-referential expected `main` SHA:

```bash
git switch main
git pull --ff-only
git rev-parse HEAD
git status --short
python --version
git log --oneline -6
```

Confirm that the history includes the Step 5 product/test revision:

```text
137fe282c9d372be7b21708011e1d8bcb46b9fbd
```

Run focused Step 5 tests:

```bash
python -m unittest tests.test_uv_lock_change -v
```

Run the complete deterministic suite:

```bash
python -m unittest discover -s tests -v
```

Expected if no unrelated tests were added:

```text
Step 5 tests: 19
complete suite: 120
```

Run installed S004 regression:

```bash
unset GITHUB_TOKEN
upgradepilot googlefonts/glyphsLib 1145
```

Then run live S001 extraction without CLI integration:

```bash
python - <<'PY'
import os

from upgradepilot.dependency_change import (
    DependencyChangeEvidenceProblem,
    ExtractedDependencyVersionChange,
)
from upgradepilot.github_client import GitHubReadClient
from upgradepilot.github_repository import GitHubRepositoryClient
from upgradepilot.uv_lock_change import extract_uv_lock_changes

token = os.getenv("GITHUB_TOKEN")
pull_client = GitHubReadClient(token=token)
repository_client = GitHubRepositoryClient(token=token)

identity = pull_client.get_pull_request("pydantic/pydantic", 13432)
changed_files = pull_client.get_changed_files(identity)
uv_lock = next(record for record in changed_files if record.filename == "uv.lock")

result = extract_uv_lock_changes(
    uv_lock,
    repository_client.get_pull_request_base_file(identity, uv_lock.filename),
    repository_client.get_pull_request_head_file(identity, uv_lock.filename),
)

print(type(result).__name__)
if isinstance(result, ExtractedDependencyVersionChange):
    print(f"package: {result.package}")
    print(f"normalized package: {result.normalized_package}")
    print(f"old version: {result.old_version}")
    print(f"proposed version: {result.proposed_version}")
    print(f"path: {result.source_evidence.path}")
    print(f"base revision: {result.source_evidence.base_revision}")
    print(f"base blob: {result.source_evidence.base_blob_sha}")
    print(f"base bytes: {result.source_evidence.base_byte_count}")
    print(f"head revision: {result.source_evidence.head_revision}")
    print(f"head blob: {result.source_evidence.head_blob_sha}")
    print(f"head bytes: {result.source_evidence.head_byte_count}")
else:
    assert isinstance(result, DependencyChangeEvidenceProblem)
    print(f"reason: {result.reason}")
    print(f"detail: {result.detail}")
PY
```

Expected bounded identity:

```text
ExtractedDependencyVersionChange
soupsieve
2.6 → 2.8.4
uv.lock
```

The exact revisions, blobs, and byte counts must match the Step 4 S001 evidence.

After all checks pass:

1. create one dated Step 5 validation record;
2. update this file with exact execution facts;
3. close Step 5;
4. only then discuss Step 6 downstream migration.

If any check fails, remain in Step 5 and correct the parser or test boundary before proceeding.

## Step 5 exclusions

Do not add during validation or repair:

- CLI integration;
- downstream `DependencyVersionChange` migration;
- CI dependency-exercise migration;
- changed duplicate-record pairing;
- uv workspace/resolver semantics;
- PEP 440 parsing or ordering;
- Python-support relevance;
- compatibility, safety, recommendation, or maintainer action.

## Not established

- passing Step 5 repository tests;
- behavior validation of `uv_lock_change.py`;
- live S001 Soup Sieve extraction through product code;
- PR-wide comparison including lockfile extraction;
- CLI integration through the shared dependency flow;
- constraints or `uv.lock` CI-consumption semantics;
- downstream migration or CI result migration;
- PEP 440 runtime semantics;
- Python-support relevance;
- compatibility, safety, maintainer action, or production readiness;
- mastery of Steps 1–5 concepts.

## State-maintenance rule

When route, selected plan, verified behavior, blocker, learning state, or exact continuation changes, update this file only. Change another file only when its stable responsibility or dated evidence changes.
