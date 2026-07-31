# B2 Step 4 — Exact Pull-Request File Acquisition Validation

**Local timestamp:** 2026-07-31 17:29 +03:30  
**Route:** B2 — Public PR vertical slice  
**Selected plan:** [`../plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](../plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)  
**Architecture:** [`../docs/architecture/ADR-0004-dependency-version-change-evidence.md`](../docs/architecture/ADR-0004-dependency-version-change-evidence.md)  
**Operation:** Validate Step 4 exact base/head repository-file acquisition, preserve all prior deterministic behavior and installed S004 behavior, and exercise exact complete `uv.lock` acquisition against public S001  
**Result:** Step 4 behavior validation passed; Step 5 `uv.lock` extraction may be discussed next

## Validated source position

Immediately after the supplied local execution, remote repository `main` resolved to:

```text
84fdd422152cd2b098fb88b6245e86b8750add29
Record Step 4 file acquisition implementation
```

The last product-source revision inside that state is:

```text
7bb542acf4ca24a89e384f9a9c590345939c8673
Acquire exact pull request repository files
```

The later `84fdd422...` commit changed only `MEMORY.md`; it did not modify product source or tests.

The supplied transcript showed the local checkout on branch `main`, but did not separately include:

```text
git rev-parse HEAD
git status --short
python --version
```

Therefore this validation record binds the observed results to repository `main` as resolved immediately after the run. It does not independently establish the local exact commit, a clean working tree, or the exact interpreter version for this execution.

No product source or test file changed during the validation operation.

## Complete deterministic-suite validation

Observed result:

```text
Ran 101 tests in 0.023s

OK
```

The complete suite includes:

- 9 Step 4 exact pull-request file-acquisition tests;
- 6 Step 3 dependency-comparison tests;
- 10 Step 2 exact-requirement tests;
- 6 legacy dependency-change tests;
- 4 Step 1 shared-contract tests;
- all existing GitHub, workflow, CI, CLI, target-Python, package, provenance, upstream, and JSON-contract tests.

No failure, error, or skip was reported.

This establishes that the new strict base/head acquisition path and its shared decoding helpers did not regress the deterministic behavior covered by the repository suite.

## Step 4 behavior established

The following successful evidence record is behavior-validated:

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

The following client methods are behavior-validated:

```text
get_pull_request_base_file
get_pull_request_head_file
```

Validated acquisition order:

```text
normalized relative repository path
→ exact immutable PR base or head SHA
→ GitHub Contents API
→ regular-file response
→ requested and returned path agreement
→ non-empty blob SHA
→ required non-negative reported byte count
→ reject reported size above 1,000,000 bytes before decoding
→ strict Base64 decoding
→ actual decoded byte count
→ reported/decoded size agreement
→ decoded-byte bound
→ valid UTF-8 text
→ ExactRepositoryTextFile
```

Validated stopping behavior includes:

- ambiguous HTTP 404 becomes `UnavailableRepositoryFile` with repository, path, revision, reason, and detail;
- returned-path mismatch is rejected;
- missing, negative, or boolean reported size is rejected as malformed evidence;
- reported oversize stops before Base64 decoding;
- malformed Base64 remains distinct;
- reported/decoded size disagreement is rejected;
- invalid UTF-8 remains distinct.

## Existing S004 installed regression control

Observed command:

```bash
unset GITHUB_TOKEN
upgradepilot googlefonts/glyphsLib 1145
```

The installed command completed successfully and preserved the established S004 evidence chain:

```text
googlefonts/glyphsLib #1145
requirements-dev.txt
pytest 9.0.2 → 9.0.3
project_table_absent
exact-head CI authority sufficient
pytest==9.0.3 package evidence
2 of 2 provenance coverage
pytest-dev/pytest release tag 9.0.3
unresolved_claim
```

The visible CI authority remained based on the `Regression Tests` workflow installing `requirements-dev.txt` and directly invoking `pytest`. The `Test + Deploy` workflow remained unresolved under the current multi-job boundary.

This proves that the new Step 4 path did not alter the existing installed CLI behavior. It does not prove that the CLI uses the new strict base/head API; it still uses the existing exact-head workflow and target-file APIs.

## Public S001 exact base/head acquisition

Observed public case:

```text
repository: pydantic/pydantic
pull request: 13432
path: uv.lock
```

Base result:

```text
type: ExactRepositoryTextFile
repository: pydantic/pydantic
path: uv.lock
revision: 652a61ce4f9d7d76eaada31535807a485ece0e21
blob SHA: b4a68ab725de337889d50d5374ac0f05db7fb484
reported bytes: 606307
decoded bytes: 606307
```

Head result:

```text
type: ExactRepositoryTextFile
repository: pydantic/pydantic
path: uv.lock
revision: aa2dc024d33f61cdef50bf1973ab5adf0a974f5a
blob SHA: def33fe05d78ab851ce91a33db5bc55a439873a1
reported bytes: 606313
decoded bytes: 606313
```

Both public files were below the authorized 1,000,000-byte bound. For each revision, GitHub's reported size matched the actual Base64-decoded byte count exactly.

This is the first newly implemented capability in the selected dependency plan that has been exercised against S001.

## What this validation proves

Established:

- complete exact `uv.lock` text can be acquired from the immutable S001 base revision;
- complete exact `uv.lock` text can be acquired from the immutable S001 head revision;
- repository, path, revision, blob SHA, and byte evidence are preserved;
- reported size is validated before decoding;
- actual decoded size is calculated and must agree with the reported size;
- existing workflow and target-Python repository-file acquisition remains green in the complete suite;
- installed S004 behavior remains unchanged;
- no S001 repository, package, version, SHA, byte count, or answer was hardcoded into product logic.

Not established:

- TOML parsing of either `uv.lock` file;
- `uv.lock` schema or revision validation;
- package-record validation;
- duplicate package-group comparison;
- artifact-only change filtering;
- Soup Sieve `2.6 → 2.8.4` dependency identity;
- PR-wide comparison combining future `uv.lock` results with requirement-file results;
- CLI integration through the new shared dependency evidence flow;
- CI consumption or exercise semantics for `uv.lock`;
- PEP 440 ordering;
- Python-support relevance;
- compatibility, safety, recommendation, or maintainer action.

## Learning depth recorded

This step introduced and reviewed:

- commit SHA versus movable branch identity;
- explicit base and head file acquisition;
- blob SHA provenance;
- GitHub-reported versus decoded byte counts;
- pre-decode resource bounds;
- defense-in-depth decoded bounds;
- Base64 transport encoding versus UTF-8 text encoding;
- additive compatibility between old and stricter evidence records.

Current depth:

```text
structured explanation completed
+ existing acquisition code and callers inspected
+ focused proof obligations defined
+ source implementation reviewed
+ complete-suite execution observed
+ installed S004 regression observed
+ live S001 exact base/head acquisition observed
but
no independent implementation practice recorded
no user-owned technical explanation recorded
no formal assessment recorded
not mastered
```

Product behavior validation and learning mastery remain separate claims.

## Step 4 closure

Step 4 is complete and behavior-validated.

The next selected-plan step is Step 5:

```text
extract uv.lock changes
```

The next session should begin with a focused educational inspection of controlled `uv.lock` structure and the exact Step 5 comparison rules before modifying source.

Step 5 must remain limited to source-specific `uv.lock` interpretation and focused fixtures. Do not migrate the CLI, CI result contracts, PEP 440 behavior, target-Python relevance, compatibility, safety, or recommendation logic during Step 5.
