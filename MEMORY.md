# UpgradePilot Current Memory

**Last updated:** 2026-07-31 18:54 +03:30  
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
- **Step 5 validation:** [`working-memory/2026-07-31_1854_B2-step-5-uv-lock-extraction-validation.md`](working-memory/2026-07-31_1854_B2-step-5-uv-lock-extraction-validation.md)
- **Behavior-validated repository state:** `0925b9e2bf146be920f50f584201f346094743f0`.
- **Behavior-validated Step 5 product/test revision:** `82237ee4b11b1df7182a58cf5913194d8b231eac`.
- **Step 5 validation-record revision:** `c0a35dd056d450817398a1253bf6695ab5b07053`.

Later validation or memory commits do not alter the validated Step 5 product/test revision.

## Current phase

Steps 1–5 are complete and behavior-validated.

Step 6 is now the next bounded plan step:

```text
migrate downstream dependency input
```

Do not start Step 7 CI-result migration or Step 8 command integration before Step 6 is behavior-validated.

## Step 5 validated boundary

### Deterministic execution

Validated checkout:

```text
main @ 0925b9e2bf146be920f50f584201f346094743f0
clean working tree
Python 3.12.3
```

Focused Step 5 result:

```text
Ran 24 tests in 0.004s
OK
```

Complete deterministic result:

```text
Ran 125 tests in 0.030s
OK
```

### Installed S004 regression

The post-correction installed anonymous command preserved:

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

### Public S001 live extraction

Public case:

```text
pydantic/pydantic #13432
uv.lock
```

Observed:

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

The exact revisions, blobs, and byte counts match the Step 4 acquisition evidence.

## Validated `uv.lock` behavior

The source-specific parser now supports:

```text
modified same-path uv.lock
+ exact base/head text evidence
+ schema version = 1
+ non-negative revision
+ valid package records
→ one file-level ExtractedDependencyVersionChange
  or one explicit DependencyChangeEvidenceProblem
```

Validated distinctions include:

- malformed TOML and malformed schema controls;
- unsupported schema version;
- invalid package records;
- unchanged package set;
- package addition/removal;
- several package transitions;
- source or resolution-marker changes;
- same-version non-artifact structural changes;
- unchanged versus changed repeated-name groups;
- artifact-only `sdist`/`wheels` changes;
- unavailable or contradictory exact-file evidence;
- exact base/head provenance preservation.

Version-bearing registry/package records may establish transitions.

Versionless records are admitted only for one exact non-empty textual `editable` or `virtual` source. They are structural workspace context only: they cannot establish transitions and must remain structurally unchanged.

## Current runtime boundary

The installed CLI still follows the legacy dependency input:

```text
ChangedFile[]
→ extract_pinned_dependency_change
→ PinnedDependencyChange or UnsupportedDependencyChange
```

Therefore this command does not yet use the new `uv.lock` parser:

```bash
upgradepilot pydantic/pydantic 13432
```

One-line installed S001 behavior belongs to later integration, not Step 5.

## Step 6 responsibility

Step 6 must replace downstream dependence on `PinnedDependencyChange` with the trusted shared record:

```text
DependencyVersionChange
```

Required architectural flow:

```text
admitted source-specific results
→ compare_extracted_dependency_changes
→ DependencyVersionChange or explicit problem
→ downstream target/package/upstream inputs
```

Step 6 must preserve current S004 behavior while separating:

```text
dependency source evidence path
from
CI installation evidence
```

A requirements or lockfile path identifies where dependency evidence came from. It must not automatically be treated as proof that CI installed that path.

## Exact Step 6 continuation

Begin with read-only inspection of:

1. every runtime and test reference to `PinnedDependencyChange`;
2. `src/upgradepilot/cli.py` dependency extraction and downstream calls;
3. current CI-authority input assumptions tied to `source_file`;
4. target-Python, PyPI, provenance, and upstream functions that consume package/version identity;
5. tests that encode the legacy dependency object or automatic source-file installation assumption.

Then teach and freeze the migration boundary before writing source:

```text
legacy combined record
PinnedDependencyChange
├── source_file
├── package
├── normalized_package
├── old_version
└── proposed_version

shared trusted record
DependencyVersionChange
├── package
├── normalized_package
├── old_version
├── proposed_version
├── source_evidence[]
└── limitations[]
```

The central Step 6 distinction is:

```text
package/version identity can migrate now
but
file-specific CI consumption cannot be inferred from generic source evidence
```

Step 6 must not yet:

- rename or redesign CI result states;
- claim `uv.lock` CI consumption;
- complete the public S001 one-line CLI path;
- add PEP 440 ordering;
- implement target-Python relevance;
- decide compatibility, safety, recommendation, or maintainer action.

## Learning state

Step 5 introduced and reviewed:

- TOML and Python `tomllib`;
- schema version versus lock revision;
- package records and normalized distribution identity;
- unique records versus repeated resolver branches;
- unordered multiset comparison;
- artifact versus structural metadata;
- valid version absence under editable/virtual workspace sources;
- file-level extraction versus PR-wide trusted comparison;
- using a real validation failure to refine a generic evidence boundary.

Current depth:

```text
structured explanation completed
+ implementation and tests reviewed
+ real failure diagnosed
+ correction implemented
+ focused and complete tests observed
+ installed S004 regression observed
+ live S001 extraction observed
but
no independent implementation practice recorded
no user-owned technical explanation recorded
no formal assessment recorded
not mastered
```

Product behavior validation and learning mastery remain separate claims.

## Not established

- Step 6 downstream migration;
- live PR-wide trusted `DependencyVersionChange` for S001 orchestration;
- one-line installed S001 command behavior;
- `uv.lock` CI-consumption or exercise proof;
- shared `DependencyCIExerciseResult` runtime behavior;
- PEP 440 validity or forward ordering;
- Python-support relevance;
- compatibility, safety, maintainer action, or production readiness;
- mastery of Steps 1–5 concepts.

## State-maintenance rule

When route, selected plan, verified behavior, blocker, learning state, or exact continuation changes, update this file only. Change another file only when its stable responsibility or dated evidence changes.
