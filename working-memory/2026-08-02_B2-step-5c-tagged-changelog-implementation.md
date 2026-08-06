# B2 Step 5C — Exact Tagged Changelog Acquisition Implementation

**Date:** 2026-08-02  
**Role:** Historical implementation evidence only. `MEMORY.md` owns live project state.

## Responsibility implemented

Step 5C now provides the deterministic bridge:

```text
GitHubTagCommitEvidence
+ explicit changelog path
→ exact repository file at resolved_commit_sha
→ exact path/blob/byte/UTF-8/retrieval-time evidence
→ build_tagged_changelog_evidence(...)
→ TaggedChangelogEvidence
   or UpstreamAuthoritySourceProblem
```

The source/test implementation boundary is:

```text
6aa809059a54f2a65cf00409c33d2758f17694d0
```

## Modified source

### `src/upgradepilot/github_repository.py`

Added:

```text
GitHubRepositoryClient.get_exact_commit_text_file(
    repository,
    commit_sha,
    path,
)
```

The method:

- requires an explicit normalized repository locator;
- accepts only 40- or 64-character hexadecimal commit/object IDs, so movable refs such as `main` or `v2.8.4` cannot enter this API;
- reuses the existing strict complete-file acquisition mechanics;
- preserves requested path, returned path, revision, blob SHA, reported bytes, decoded bytes, UTF-8 text, and retrieval time;
- preserves 404 absence/inaccessibility as `UnavailableRepositoryFile`.

The existing PR base/head methods keep their original public responsibility and their guard restricting them to the PR's base/head revisions. Their strict decoding logic now delegates to the same private exact-revision implementation rather than being copied.

`ExactRepositoryTextFile` gained optional `retrieved_at`. Existing manual fixtures remain source-compatible because the field has a default, while every successful strict client acquisition now populates it.

### `src/upgradepilot/upstream_interval_acquisition.py`

Added:

```text
TaggedChangelogCompositionResult
build_tagged_changelog_evidence(...)
```

The composition boundary requires:

- tag identity for the interval's exact proposed version or `v`-prefixed equivalent;
- internally consistent tag ref/object identity;
- file repository equal to the resolved tag repository;
- file revision exactly equal to `resolved_commit_sha`;
- exact path/returned-path, blob, byte-count, content, and retrieval-time evidence.

An unavailable file becomes an explicit tagged-changelog `source_unavailable` problem. An empty exact file is also not promoted into changelog authority. Identity contradictions stop as `identity_mismatch`; malformed exact evidence remains `malformed_source`.

The function does not search for a changelog path and does not call the network.

## Tests added

```text
tests/test_exact_commit_repository_files.py
tests/test_tagged_changelog_acquisition.py
```

Coverage includes:

- successful exact-commit text acquisition;
- exact source retrieval time;
- rejection of branch/tag-like movable refs;
- accepted 40/64-hex object identifiers;
- explicit 404 file evidence;
- inherited strict reported/decoded byte agreement;
- annotated and lightweight tag composition;
- proposed-version tag identity;
- repository and resolved-commit joins;
- unavailable/empty changelog handling;
- missing retrieval-time evidence;
- public type boundary;
- package-level Step 5C composition exports.

## Intentionally not implemented

Step 5C does not yet:

- call `assemble_upstream_interval_authority(...)` as an integrated Step 5D path;
- discover a changelog path automatically;
- perform live S001 acquisition;
- extract semantic support-drop claims;
- alter CLI orchestration;
- make compatibility, safety, or recommendation claims.

## Validation state

Implementation and controlled tests are committed, but no local pass is claimed yet for this Step 5C boundary. The next action is focused plus complete deterministic validation before Step 5D begins.
