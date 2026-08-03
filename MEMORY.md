# UpgradePilot Current Memory

**Last updated:** 2026-08-02  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, selected continuation, and current learning state.

Stable plans, specifications, ADRs, source, tests, and dated working records retain their own responsibilities. They must not mirror or compete with this file for live status.

## Single-live-state rule

`MEMORY.md` is replacement state, not append-only history. It alone answers what is selected now, what behavior is verified, what remains open, what happens next, and what learning depth is established.

## Live position

- **Execution branch:** `main`. No separate implementation branch is selected.
- **Route:** B2 — Public PR vertical slice.
- **Selected parent plan:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)
- **Selected Step 5 plan:** [`plans/B2_STEP_5_UPSTREAM_INTERVAL_ACQUISITION_PLAN.md`](plans/B2_STEP_5_UPSTREAM_INTERVAL_ACQUISITION_PLAN.md)
- **Behavior-validated:** parent-plan Steps 1–4, Step 5A, and Step 5B.
- **Current responsibility:** Step 5C — exact immutable-commit changelog-file acquisition and `TaggedChangelogEvidence` composition.
- **Current Step 5C state:** implemented with controlled tests; **local validation is required before Step 5D authority composition begins**.
- **Step 5B validation record:** [`working-memory/2026-08-02_B2-step-5b-git-tag-commit-validation.md`](working-memory/2026-08-02_B2-step-5b-git-tag-commit-validation.md)
- **Step 5C implementation record:** [`working-memory/2026-08-02_B2-step-5c-tagged-changelog-implementation.md`](working-memory/2026-08-02_B2-step-5c-tagged-changelog-implementation.md)

## Last behavior-validated executable boundary

Step 5B source/test behavior is validated through:

```text
783a22c790b0c45487acf3b4d3a4698ba7484a82
```

The user reported the complete deterministic suite:

```text
Ran 294 tests in 0.064s

OK
```

The exact focused Step 5B summary was not supplied and is not invented. The complete discovery run contains the Step 5B tag, release, upstream-source, and package-interface tests, so another focused rerun is not required solely to establish the same behavior.

## Step 5B closure

Step 5B is **closed and behavior-validated**.

Established flow:

```text
repository + exact requested version tag
→ exact refs/tags/{tag}
→ lightweight commit target
   or bounded annotated-tag peeling
→ GitHubTagCommitEvidence.resolved_commit_sha
```

Validated behavior includes exact tag-ref identity, lightweight tags, nested annotated tags, cycle detection, peel-depth bounds, unsupported object types, explicit acquisition/malformed states, and preservation of the direct tag object separately from the final commit.

No live S001 tag lookup is claimed by this deterministic validation.

## Step 5C implemented boundary awaiting validation

The current Step 5C source/test revision is:

```text
6aa809059a54f2a65cf00409c33d2758f17694d0
```

Later Step 5B validation, Step 5C implementation-record, and `MEMORY.md` commits do not alter that executable boundary.

### Exact commit file acquisition

`src/upgradepilot/github_repository.py` now exposes:

```text
GitHubRepositoryClient.get_exact_commit_text_file(
    repository,
    commit_sha,
    path,
)
```

Data flow:

```text
resolved immutable commit SHA
+ explicit repository-relative path
→ GitHub contents API at ref=<commit SHA>
→ strict path/blob/size/Base64/UTF-8 checks
→ ExactRepositoryTextFile
   or UnavailableRepositoryFile
```

The new API accepts only hexadecimal immutable object identifiers:

```text
40 hex characters
or
64 hex characters
```

Therefore movable names such as:

```text
main
v2.8.4
feature-branch
```

cannot enter this exact-commit acquisition path.

The existing PR base/head helpers retain their original public authority and guards. Their strict complete-file mechanics now share one private exact-revision implementation with the Step 5C reader rather than duplicating decoding and byte checks.

### Retrieval-time evidence

`ExactRepositoryTextFile` now has:

```text
retrieved_at: datetime | None
```

The default preserves compatibility with older manually constructed fixtures. Every successful strict acquisition by `GitHubRepositoryClient` populates the actual retrieval time.

This is required because `TaggedChangelogEvidence` must preserve when the exact file response was acquired. Step 5C does not reuse the Step 5B tag-lookup timestamp as a false substitute for file-acquisition time.

### Tagged changelog composition

`src/upgradepilot/upstream_interval_acquisition.py` now exposes:

```text
TaggedChangelogCompositionResult
build_tagged_changelog_evidence(...)
```

The pure join is:

```text
DependencyReleaseInterval
+ GitHubTagCommitEvidence
+ ExactRepositoryFileEvidence
→ TaggedChangelogEvidence
   or UpstreamAuthoritySourceProblem
```

The crucial identity rule is:

```text
file_evidence.revision
==
tag_commit.resolved_commit_sha
```

A matching repository and path are insufficient if the file came from a different commit.

The composition also requires:

- tag identifies the interval's proposed version or its `v`-prefixed form;
- exact tag ref/object identity remains internally consistent;
- file repository matches tag repository;
- requested and returned file paths agree;
- blob SHA is preserved;
- reported and decoded byte counts agree;
- exact UTF-8 content exists;
- file retrieval time exists.

An unavailable exact file remains:

```text
source_unavailable
```

An exact but empty changelog file is also not promoted into interval authority.

Identity contradictions become:

```text
identity_mismatch
```

Malformed exact evidence becomes:

```text
malformed_source
```

### Changelog path boundary

Step 5C accepts one explicit path. It does **not** search arbitrary repository files or hardcode an S001-specific changelog path.

Automated changelog-path discovery remains outside this increment unless a later activated need justifies a separate bounded rule.

## Controlled Step 5C tests

Added:

```text
tests/test_exact_commit_repository_files.py
tests/test_tagged_changelog_acquisition.py
```

and extended the package-interface contract.

Coverage includes:

- successful exact-commit repository text acquisition;
- actual retrieval timestamp preservation;
- rejection of movable ref names;
- 40/64-hex immutable IDs;
- exact 404 repository/path/revision evidence;
- shared strict byte-agreement behavior;
- annotated and lightweight tag composition;
- proposed-version tag identity;
- repository and resolved-commit joins;
- unavailable and empty changelog handling;
- missing retrieval-time evidence;
- public input types and Step 5C exports.

No Step 5C pass is claimed yet.

## Exact continuation

From the real checkout:

```bash
git pull --ff-only

python -m unittest \
  tests.test_exact_commit_repository_files \
  tests.test_pull_request_repository_files \
  tests.test_tagged_changelog_acquisition \
  tests.test_package_interface \
  -v

python -m unittest discover -s tests -v
```

Derived expectations at the current Step 5C source/test boundary are:

```text
focused: 33 tests
complete: 310 tests
```

These are derived expectations only. Observed terminal output controls validation truth.

If validation fails, diagnose and repair only within the Step 5C repository-file/composition boundary unless evidence proves an older regression.

If validation passes:

1. close Step 5C as behavior-validated;
2. activate Step 5D — compose the validated crossed-release index and tagged changelog through the existing `assemble_upstream_interval_authority(...)` implementation;
3. do not begin semantic claim extraction, model integration, CLI reordering, or full S001 product execution yet.

## Stop line

Until Step 5C validates, do not begin:

- Step 5D integrated interval-authority composition;
- semantic claim extraction/model integration;
- target-Python or CLI orchestration changes;
- S001 live end-to-end product execution;
- compatibility, safety, merge, defer, targeted-check, or recommendation logic.

## Explicitly not established

- a passing Step 5C focused suite;
- a passing complete suite containing Step 5C;
- live S001 changelog acquisition;
- live Step 1 `AuthoritativeUpstreamIntervalEvidence` from Step 5 acquisition;
- automated semantic extraction/model path;
- conditional target-Python activation in CLI runtime;
- S001 automated end-to-end relevance result;
- compatibility, safety, recommendation, maintainer action, or production readiness;
- user mastery of Steps 1–5C.

## Learning state

Steps 1–5B are behavior-validated at product level. Step 5C concepts are introduced and implemented but not yet behavior-validated.

Step 5C learning concepts include:

- **commit versus ref:** a commit SHA is immutable evidence identity; a branch/tag name can move or require resolution;
- **tree/file identity:** a resolved commit selects one source tree, while the blob SHA identifies the exact file contents inside that tree;
- **reported versus decoded bytes:** HTTP/JSON metadata and actual decoded content must agree before evidence is trusted;
- **source retrieval time:** acquisition time belongs to the source actually fetched and must not be borrowed from a different request;
- **identity join:** independent records become one trusted record only when repository, resolved commit, path, and exact source evidence agree;
- **acquisition versus composition:** network retrieval is separate from the pure function that gives acquired records Step 1 changelog meaning.

Current depth:

```text
Step 5B behavior validated
+ Step 5C data flow and evidence distinctions introduced
+ educational source/docstrings/comments available
+ controlled Step 5C tests written
+ Step 5C implementation complete
but
Step 5C local execution not yet observed
no user-owned Step 5C technical explanation recorded
no independent implementation proof
no formal mastery assessment
not mastered
```

Product validation and learning mastery remain separate claims.

## State-maintenance rule

When route, selected responsibility, verified executable boundary, blocker, learning state, or exact continuation changes:

1. update `MEMORY.md` only for live state;
2. replace obsolete live statements instead of accumulating them;
3. change plans/specifications/ADRs only when their stable responsibility actually changes;
4. create dated working-memory only for material historical evidence or reasoning, never as another status owner;
5. keep navigation READMEs non-state-bearing.
