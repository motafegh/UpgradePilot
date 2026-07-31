# UpgradePilot Current Memory

**Last updated:** 2026-07-31 17:36 +03:30  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, and exact continuation.

Stable route definitions, specifications, ADRs, source, tests, plans, and dated evidence retain their own responsibilities. This file records only the current position needed to continue.

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Controlling route:** [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md)
- **B2 gate:** [`plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)
- **Selected plan:** [`plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)
- **Accepted architecture:** [`docs/architecture/ADR-0004-dependency-version-change-evidence.md`](docs/architecture/ADR-0004-dependency-version-change-evidence.md)
- **Step 1 validation:** [`working-memory/2026-07-30_2138_B2-step-1-dependency-contracts-validation.md`](working-memory/2026-07-30_2138_B2-step-1-dependency-contracts-validation.md)
- **Step 2 validation:** [`working-memory/2026-07-31_1612_B2-step-2-exact-requirement-validation.md`](working-memory/2026-07-31_1612_B2-step-2-exact-requirement-validation.md)
- **Step 3 validation:** [`working-memory/2026-07-31_1635_B2-step-3-dependency-comparison-validation.md`](working-memory/2026-07-31_1635_B2-step-3-dependency-comparison-validation.md)
- **Step 4 validation:** [`working-memory/2026-07-31_1729_B2-step-4-exact-pr-file-acquisition-validation.md`](working-memory/2026-07-31_1729_B2-step-4-exact-pr-file-acquisition-validation.md)
- **Last behavior-validated repository state:** `84fdd422152cd2b098fb88b6245e86b8750add29`.
- **Last behavior-validated product-source revision:** `7bb542acf4ca24a89e384f9a9c590345939c8673`.
- **Latest Step 5 implementation revision:** `137fe282c9d372be7b21708011e1d8bcb46b9fbd`.

## Current phase

Steps 1, 2, 3, and 4 are complete and behavior-validated.

Step 5 source and focused tests are now implemented on `main`:

```text
extract uv.lock changes
```

Step 5 has **not** yet been behavior-validated in the real Python 3.12 checkout or against live S001 extraction.

Do not begin Step 6.

## Last behavior-validated boundary

Observed at the Step 4 boundary:

```text
complete deterministic suite: 101 passed
installed anonymous S004 command: passed
live S001 exact base/head uv.lock acquisition: passed
```

The Step 5 commits do not extend the behavior-validated boundary until focused lockfile tests, the complete suite, installed S004, and one live S001 extraction pass.

## Step 5 implementation present on main

Added:

```text
src/upgradepilot/uv_lock_change.py
```

Public functions:

```text
is_modified_uv_lock_file
extract_uv_lock_changes
```

Package-level exports are available through:

```python
from upgradepilot import is_modified_uv_lock_file, extract_uv_lock_changes
```

### Admission boundary

`is_modified_uv_lock_file` requires:

```text
normalized repository-relative POSIX path
+ final basename exactly uv.lock
+ GitHub status modified
```

Added, deleted, renamed, uppercase, absolute, traversal, repeated-separator, and backslash paths remain outside the first boundary.

### Extraction input and output

Input:

```text
ChangedFile
+ ExactRepositoryFileEvidence at base
+ ExactRepositoryFileEvidence at head
```

Output:

```text
ExtractedDependencyVersionChange
or
DependencyChangeEvidenceProblem
```

The result remains file-level evidence. It is not yet the PR-wide trusted `DependencyVersionChange`.

### TOML and schema boundary

The implementation uses Python standard-library `tomllib` and adds no runtime dependency.

Admitted controls:

```text
version = 1
revision = non-negative integer
package = array of tables
```

Stopping distinctions include:

- malformed TOML → `malformed_dependency_file`;
- missing or incorrectly typed schema controls → `malformed_dependency_file`;
- another integer schema version → `unsupported_uv_lock_schema`;
- unusable package array or records → `invalid_dependency_record`.

Package records require:

```text
non-empty distribution name
+ admitted distribution-name grammar
+ non-empty exact version string
+ no leading/trailing whitespace
```

Package identity is grouped through the shared normalized distribution-name rule. PEP 440 validation and ordering remain outside extraction.

### Unique-record comparison

For one record at base and one at head:

```text
same normalized package
+ exact source structure unchanged
+ exact resolution-markers structure unchanged
```

If the exact version changes, attached dependency and package metadata may also change.

If the version does not change, any non-artifact structural change produces:

```text
unsupported_uv_lock_structural_change
```

### Repeated-name comparison

For repeated normalized package names, the implementation:

1. removes only top-level `sdist` and `wheels`;
2. retains every other known or unknown parsed field;
3. preserves internal list order;
4. freezes the parsed structure into hashable values;
5. compares record collections as unordered multisets with multiplicity.

Outcomes:

```text
unchanged duplicate group
→ does not block another clear transition

changed duplicate group
→ ambiguous_uv_lock_package_records
```

No file-position pairing, first-record selection, marker normalization, or uv resolver semantics are used.

### Artifact and structural boundaries

Artifact-only changes in:

```text
sdist
wheels
```

do not create dependency transitions.

Package additions/removals, source changes, resolution-context changes, and same-version non-artifact structural changes remain explicit unsupported or ambiguous results.

Several unambiguous changed packages produce:

```text
multiple_dependency_version_changes
```

No changed package produces:

```text
version_unchanged
```

### Exact source evidence

Successful extraction preserves one `DependencyFileEvidence` with:

```text
complete path
file_format = uv_lock
extraction_method = exact_base_head_files
base revision/blob/byte count
head revision/blob/byte count
```

Repository/path contradictions, missing revision/blob identity, or inconsistent byte evidence produce `invalid_dependency_record` before TOML interpretation.

## Step 5 focused tests present

Added:

```text
tests/test_uv_lock_change.py
```

The file defines 19 tests covering:

1. admitted modified nested/root `uv.lock` paths;
2. rejected status and path forms;
3. explicit non-modified status problem;
4. non-lockfile path abstention;
5. one successful normalized transition and complete source evidence;
6. unavailable exact file evidence;
7. repository/path/returned-path contradictions;
8. malformed TOML;
9. unsupported schema version;
10. missing, negative, boolean, or incorrectly typed schema controls;
11. invalid package records and names;
12. unchanged lockfile;
13. package addition/removal;
14. several version transitions;
15. source-context change;
16. resolution-marker change;
17. same-version non-artifact structural change;
18. artifact-only differences;
19. unchanged and changed repeated-name groups.

Fixtures use a fictional repository and package-neutral records. No S001 repository, package, version, SHA, byte count, or expected result is hardcoded into product logic.

Expected complete deterministic total if no unrelated tests were added:

```text
120 tests
```

This is an expectation, not a passing result.

## Relevant Step 5 revisions

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

The implementation was created through the GitHub connector, which could inspect and modify repository files but could not execute the real repository suite.

An isolated Python 3.13.5 syntax and behavior harness exercised the same 19 scenario groups successfully. That harness is development feedback only; it is not repository behavior validation and does not replace the user's Python 3.12 suite.

## Real S001 structural review

The exact public records already acquired in Step 4 show:

```text
base:
name = soupsieve
version = 2.6
source = PyPI registry

head:
name = soupsieve
version = 2.8.4
source = the same PyPI registry
```

Neither record is resolution-marker-split. The surrounding changes are version and artifact fields. This matches the generic unique-record boundary without any S001-specific rule.

This review does not establish product behavior. Live extraction must still be executed after the local suite passes.

## Compatibility boundary preserved

The installed CLI still follows:

```text
ChangedFile[]
→ extract_pinned_dependency_change
→ PinnedDependencyChange or UnsupportedDependencyChange
```

It does not yet call `extract_uv_lock_changes`, acquire dependency base/head files during normal CLI orchestration, or pass lockfile results through `compare_extracted_dependency_changes`.

Step 5 therefore expands internal source-specific capability but does not yet expand the installed CLI behavior boundary.

No Step 5 change touched:

- `cli.py`;
- existing exact-requirement extraction;
- PR-wide comparison behavior;
- CI authority or dependency-exercise logic;
- target-Python interpretation;
- PyPI or upstream evidence;
- PEP 440 semantics;
- compatibility, safety, or recommendation logic.

## Learning state

Step 5 introduced and reviewed:

- **TOML — Tom's Obvious Minimal Language** — the structured syntax used by `uv.lock`;
- **`tomllib`** — Python 3.12 standard-library TOML parser;
- **array of tables** — repeated `[[package]]` sections parsed into a list of mappings;
- **normalized-name grouping** — package spelling variants share one distribution identity;
- **resolution context** — exact source and `resolution-markers` used to pair unique records;
- **artifact metadata** — `sdist` and `wheels`, excluded from dependency-transition identity;
- **unordered multiset** — record order is irrelevant while duplicate multiplicity remains significant;
- **conservative abstention** — changed duplicate resolver branches remain ambiguous rather than heuristically paired;
- **raw version preservation** — extraction observes textual inequality without PEP 440 interpretation.

Current Step 5 depth:

```text
structured explanation completed
+ accepted ADR rules revisited at implementation time
+ real S001 record shape inspected
+ focused proof obligations defined
+ source and tests implemented
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

Synchronize the local checkout and capture the exact boundary:

```bash
git switch main
git pull --ff-only
git rev-parse HEAD
git status --short
python --version
```

Expected repository head before unrelated concurrent changes:

```text
137fe282c9d372be7b21708011e1d8bcb46b9fbd
```

Run focused Step 5 tests:

```bash
python -m unittest tests.test_uv_lock_change -v
```

Preserve earlier dependency and acquisition boundaries:

```bash
python -m unittest tests.test_pull_request_repository_files -v
python -m unittest tests.test_dependency_change_comparison -v
python -m unittest tests.test_exact_requirement_change -v
python -m unittest tests.test_github_repository -v
python -m unittest tests.test_target_python -v
python -m unittest tests.test_ci_authority -v
python -m unittest tests.test_cli -v
```

Run the complete deterministic suite:

```bash
python -m unittest discover -s tests -v
```

Expected counts if no unrelated tests were added:

```text
Step 5 uv.lock tests: 19
complete deterministic suite: 120
```

Run the installed S004 regression control:

```bash
unset GITHUB_TOKEN
upgradepilot googlefonts/glyphsLib 1145
```

Then execute live S001 extraction without CLI integration:

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

Expected bounded result:

```text
ExtractedDependencyVersionChange
package: soupsieve
normalized package: soupsieve
old version: 2.6
proposed version: 2.8.4
path: uv.lock
```

The exact source revisions, blobs, and byte counts should match the Step 4 validated S001 evidence.

If every check passes:

1. create one dated Step 5 validation record;
2. update this file with exact execution facts;
3. mark Step 5 behavior-validated;
4. only then discuss Step 6 downstream migration.

If any check fails, remain in Step 5, correct the parser or fixture boundary, and rerun focused, complete, S004, and live S001 checks.

## Step 5 exclusions still active

Do not add during validation or repair:

- CLI integration;
- downstream migration to `DependencyVersionChange`;
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
- CLI orchestration through the shared dependency flow;
- constraints or `uv.lock` CI-consumption semantics;
- downstream `DependencyVersionChange` migration;
- `DependencyCIExerciseResult` runtime behavior;
- PEP 440 runtime semantics;
- Python-support relevance;
- compatibility, safety, maintainer action, or production readiness;
- mastery of Steps 1–5 concepts.

## State-maintenance rule

When route, selected plan, verified behavior, blocker, learning state, or exact continuation changes, update this file only. Change another file only when its stable responsibility or dated evidence changes.
