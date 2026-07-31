# UpgradePilot Current Memory

**Last updated:** 2026-07-31 16:49 +03:30  
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
- **Last behavior-validated repository state:** `0b1e045ad18915fed59c34318cf482f0132d9112`.
- **Latest Step 4 implementation revision:** `7bb542acf4ca24a89e384f9a9c590345939c8673`.

## Current phase

Steps 1, 2, and 3 are complete and behavior-validated.

Step 4 source and focused tests are now implemented on `main`:

```text
generalize exact pull-request dependency-file acquisition
```

Step 4 has **not** yet been behavior-validated in the local Python 3.12 checkout or through a live exact base/head acquisition.

Do not begin Step 5.

## Last behavior-validated product boundary

The last validated repository state remains:

```text
0b1e045ad18915fed59c34318cf482f0132d9112
```

Observed validation at that boundary:

```text
complete deterministic suite: 92 passed
installed anonymous S004 command: passed
```

The Step 4 commits do not extend this boundary until the new acquisition tests, prior repository/target/CI tests, the complete suite, the installed S004 control, and one bounded live exact base/head acquisition pass.

## Step 4 implementation present on main

Updated:

```text
src/upgradepilot/github_repository.py
```

Added strict successful evidence:

```text
ExactRepositoryTextFile
├── repository
├── path
├── returned_path
├── revision
├── blob_sha
├── reported_byte_count
├── decoded_byte_count
└── content
```

Added result union:

```text
ExactRepositoryFileEvidence
=
ExactRepositoryTextFile | UnavailableRepositoryFile
```

Added explicit client methods:

```text
get_pull_request_base_file
get_pull_request_head_file
```

These methods select only `PullRequestIdentity.base_sha` or `PullRequestIdentity.head_sha`. Their private shared implementation rejects any revision outside that exact pair.

## Exact acquisition rule now implemented

The strict dependency-file path performs:

```text
normalized repository-relative path
→ GitHub contents request at exact base/head SHA
→ regular-file and returned-path reconciliation
→ non-empty blob SHA
→ required non-negative GitHub-reported size
→ reject reported size above 1,000,000 bytes before decoding
→ require Base64 transport text
→ strict Base64 decode
→ calculate actual decoded byte count
→ require reported and decoded counts to agree
→ reapply the 1,000,000 decoded-byte bound
→ require valid UTF-8
→ immutable ExactRepositoryTextFile
```

A contents HTTP 404 remains:

```text
UnavailableRepositoryFile
reason = not_found_or_inaccessible
```

The strict base/head methods also preserve the repository identity in that unavailable record.

## Compatibility boundary preserved

Existing validated APIs remain present and retain their previous result shape:

```text
get_exact_head_text_file
→ RepositoryTextFile or UnavailableRepositoryFile

get_exact_head_workflow_file
→ RepositoryTextFile or UnavailableRepositoryFile
```

The current CLI still uses those existing APIs for:

- `pyproject.toml` target-Python evidence;
- exact-head workflow definitions;
- current CI-authority evaluation.

Step 4 does not route the CLI through `ExactRepositoryTextFile`. It does not parse `uv.lock`.

`UnavailableRepositoryFile.repository` was added as an optional final field. Existing workflow, target, CI, and test constructors remain compatible because the default is `None`.

## Step 4 focused tests present

Added:

```text
tests/test_pull_request_repository_files.py
```

The file defines nine tests proving:

1. base and head methods use the exact immutable PR SHAs;
2. successful evidence preserves repository, requested path, returned path, revision, blob SHA, both byte counts, and UTF-8 text;
3. ambiguous HTTP 404 preserves repository/path/revision and does not become empty text;
4. returned path must match the requested path;
5. reported size must be a non-negative JSON integer and reject booleans;
6. reported oversize stops before Base64 decoding;
7. malformed Base64 remains distinct;
8. reported and decoded byte counts must agree;
9. invalid UTF-8 and missing reported size remain explicit malformed-response failures.

The fixtures use a fictional repository and package-neutral lock text. No S001 answer, package, version, SHA, or expected public result is hardcoded into product logic.

## Relevant Step 4 revisions

```text
e9ab5faa5477122c7b5f2b574aa33965da7dc5e1
Test exact pull request file acquisition

7bb542acf4ca24a89e384f9a9c590345939c8673
Acquire exact pull request repository files
```

## Learning state

Step 4 introduced and reviewed:

- **commit SHA** — immutable identifier selecting one repository state, unlike a movable branch name;
- **base/head acquisition** — separate reads of the same path before and after the proposed pull-request change;
- **blob SHA** — GitHub identity of one exact file-content object;
- **reported byte count** — size declared by GitHub before decoding;
- **decoded byte count** — actual number of bytes obtained from Base64 content;
- **size reconciliation** — requiring those independent counts to agree;
- **pre-decode bound** — rejecting known oversized content before allocating decoded bytes;
- **defense-in-depth bound** — checking actual decoded bytes again;
- **transport encoding versus text encoding** — Base64 carries bytes; UTF-8 converts validated bytes into Python text;
- **additive compatibility** — stricter dependency-file evidence is introduced without replacing current workflow/target contracts.

Current Step 4 depth:

```text
structured explanation completed
+ existing acquisition code and direct callers inspected
+ exact evidence fields and decision order reviewed
+ focused tests defined
+ source implemented
but
no local execution recorded
no live exact base/head execution recorded
no independent implementation practice recorded
no formal assessment recorded
not mastered
```

Product validation and learning mastery remain separate claims.

## Exact continuation

Synchronize the local checkout and capture the exact execution boundary:

```bash
git switch main
git pull --ff-only
git rev-parse HEAD
git status --short
python --version
```

Run the focused Step 4 tests:

```bash
python -m unittest tests.test_pull_request_repository_files -v
```

Preserve the existing repository-file consumers:

```bash
python -m unittest tests.test_github_repository -v
python -m unittest tests.test_target_python -v
python -m unittest tests.test_ci_authority -v
python -m unittest tests.test_cli -v
```

Run the complete deterministic suite:

```bash
python -m unittest discover -s tests -v
```

Expected counts if no unrelated tests are added:

```text
Step 4 exact base/head tests: 9
complete deterministic suite: 101
```

Run the installed S004 regression control:

```bash
unset GITHUB_TOKEN
upgradepilot googlefonts/glyphsLib 1145
```

Then run one bounded live acquisition-only S001 check. This does not parse `uv.lock`:

```bash
python - <<'PY'
import os
from upgradepilot.github_client import GitHubReadClient
from upgradepilot.github_repository import (
    ExactRepositoryTextFile,
    GitHubRepositoryClient,
)

token = os.getenv("GITHUB_TOKEN")
identity = GitHubReadClient(token=token).get_pull_request(
    "pydantic/pydantic",
    13432,
)
client = GitHubRepositoryClient(token=token)
base = client.get_pull_request_base_file(identity, "uv.lock")
head = client.get_pull_request_head_file(identity, "uv.lock")

for label, result in (("base", base), ("head", head)):
    print(label, type(result).__name__)
    if isinstance(result, ExactRepositoryTextFile):
        print(result.repository)
        print(result.path)
        print(result.revision)
        print(result.blob_sha)
        print(result.reported_byte_count)
        print(result.decoded_byte_count)
PY
```

Expected evidence from the accepted architecture record:

```text
base revision: 652a61ce4f9d7d76eaada31535807a485ece0e21
base blob: b4a68ab725de337889d50d5374ac0f05db7fb484
base bytes: 606,307

head revision: aa2dc024d33f61cdef50bf1973ab5adf0a974f5a
head blob: def33fe05d78ab851ce91a33db5bc55a439873a1
head bytes: 606,313
```

If all checks pass:

1. create one dated Step 4 validation record;
2. update this file with exact local revision, interpreter, working-tree state, deterministic results, S004 output, and live base/head evidence;
3. mark Step 4 behavior-validated;
4. only then begin Step 5 discussion: `uv.lock` extraction.

If any check fails, remain in Step 4 and correct the acquisition or compatibility regression before proceeding.

## Not established

- Step 4 behavior validation;
- `uv.lock` parsing or package-record comparison;
- duplicate-group handling;
- S001 dependency identity through extraction, comparison, or CLI;
- CLI orchestration through the shared dependency flow;
- constraints-file CI consumption semantics;
- migration to `DependencyVersionChange` in downstream modules;
- `DependencyCIExerciseResult` runtime behavior;
- PEP 440 runtime validation or ordering;
- Python-support relevance;
- compatibility, safety, maintainer action, or production readiness;
- mastery of Step 1, Step 2, Step 3, or Step 4 concepts.

## State-maintenance rule

When route, selected plan, verified behavior, blocker, learning state, or exact continuation changes, update this file only. Change another file only when its stable responsibility or dated evidence changes.
