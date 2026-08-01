# UpgradePilot Current Memory

**Last updated:** 2026-08-02  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, selected continuation, and current learning state.

Stable plans, specifications, ADRs, source, tests, and dated working records retain their own responsibilities. They must not mirror or compete with this file for live status.

## Single-live-state rule

`MEMORY.md` is the only repository file allowed to answer what is selected now, what behavior is verified, what remains open, what happens next, and what learning depth is established.

This file is replacement state, not append-only history. Remove superseded live statements when the project advances; Git history and dated evidence preserve history.

## Live position

- **Execution branch:** `main`. No separate implementation branch is selected.
- **Route:** B2 — Public PR vertical slice.
- **Selected parent plan:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)
- **Completed and behavior-validated:** parent-plan Steps 1–4 and Step 5A.
- **Selected Step 5 plan:** [`plans/B2_STEP_5_UPSTREAM_INTERVAL_ACQUISITION_PLAN.md`](plans/B2_STEP_5_UPSTREAM_INTERVAL_ACQUISITION_PLAN.md)
- **Current responsibility:** Step 5B — exact Git version-tag resolution to an immutable commit with bounded annotated-tag peeling.
- **Current Step 5B state:** implemented with controlled tests; **local validation is required before Step 5C exact changelog-file acquisition begins**.
- **Step 5A validation record:** [`working-memory/2026-08-02_B2-step-5a-release-index-validation.md`](working-memory/2026-08-02_B2-step-5a-release-index-validation.md)
- **Step 5B implementation record:** [`working-memory/2026-08-02_B2-step-5b-git-tag-commit-implementation.md`](working-memory/2026-08-02_B2-step-5b-git-tag-commit-implementation.md)

## Last behavior-validated executable boundary

Step 5A source/test behavior is validated through:

```text
4ad56dabf6613f7ad46b096bcda7198ac1baff25
```

The user reported the complete deterministic suite from the real checkout:

```text
Ran 281 tests in 0.066s

OK
```

The exact focused Step 5A summary was not supplied and is not invented. The complete discovery run contains the Step 5A release-index acquisition/selection tests and package-interface coverage, so another focused rerun is not required solely to establish the same behavior.

## Step 5A closure

Step 5A is **closed and behavior-validated**.

Established flow:

```text
PyPI project response
→ PackageReleaseIndexEvidence
→ select_crossed_release_index(...)
→ SelectedCrossedReleaseIndex
   └── CrossedReleaseIndexEvidence
```

The validated behavior preserves exact raw PyPI release keys, assigns PEP 440 meaning only in the downstream selector, enforces the old-exclusive/proposed-inclusive interval, rejects equivalent ambiguous selected identities, requires exact proposed raw identity, and keeps non-PEP-440 registry keys explicitly visible as ignored/out-of-scope.

No live S001 network acquisition is claimed by this deterministic validation.

## Step 5B implemented boundary awaiting validation

The current Step 5B source/test revision is:

```text
783a22c790b0c45487acf3b4d3a4698ba7484a82
```

Later working-memory and `MEMORY.md` commits do not alter that executable boundary.

### Git tag terminology and responsibility

A Git **reference** is a named pointer such as:

```text
refs/tags/v2.8.4
```

Two relevant shapes exist:

```text
lightweight tag
refs/tags/v2.8.4
→ commit SHA directly
```

```text
annotated tag
refs/tags/v2.8.4
→ Git tag object SHA
→ object target
→ possibly another tag object
→ eventually commit SHA
```

Following annotated tag objects until the underlying commit is reached is called **tag peeling**. Step 5B implements only this identity-resolution responsibility.

### New source contract

Created:

```text
src/upgradepilot/github_tag.py
```

Public names:

```text
GitHubTagCommitClient
GitHubTagCommitEvidence
GitHubTagCommitProblem
GitHubTagCommitResult
```

Primary operation:

```text
GitHubTagCommitClient.resolve_tag_to_commit(repository, requested_tag)
```

Successful evidence preserves:

```text
repository
requested_tag
tag_ref
tag_object_type
tag_object_sha
resolved_commit_sha
peeled_tag_object_shas[]
retrieved_at
```

The direct tag-reference object and the finally resolved commit are intentionally separate facts.

### Exact tag identity

The supplied tag is an explicit identity, not a search hint.

The GitHub response must return exactly:

```text
refs/tags/{requested_tag}
```

Step 5B does not infer a tag from a release title and does not add or remove a `v` prefix.

### Bounded annotated-tag peeling

The client accepts only Git object types:

```text
commit
tag
```

For annotated tags it follows exact tag-object SHAs until a commit is reached.

Safety/diagnostic bounds:

```text
default maximum tag-object peel depth: 8
cycle detection: required
```

A repeated object SHA produces `peel_cycle`. Needing another tag object after the configured maximum produces `peel_depth_exceeded`.

### Explicit Step 5B problems

```text
source_unavailable
identity_mismatch
malformed_response
unsupported_object_type
peel_cycle
peel_depth_exceeded
acquisition_failed
```

These are evidence-resolution states, not compatibility or recommendation states.

### One owner for exact tag-reference parsing

`GitHubReleaseClient` previously had its own parser for exact tag-reference identity. That pure parsing rule now lives in `github_tag.py` and is reused by both the release client and Step 5B tag-to-commit client.

The responsibilities remain distinct:

```text
GitHubReleaseClient
→ published release + direct exact tag-reference object

GitHubTagCommitClient
→ exact tag reference + bounded peeling to immutable commit
```

The release client does not perform Step 5B peeling merely because the parser is shared.

## Controlled Step 5B tests

Added:

```text
tests/test_github_tag.py
```

Coverage includes:

- lightweight tag resolution;
- one-level annotated tag peeling;
- nested annotated tags;
- exact ref mismatch;
- missing tag;
- unsupported object type;
- tag-object SHA mismatch;
- cycle detection;
- maximum-depth enforcement;
- malformed tag-object response;
- acquisition timeout;
- strict public inputs and configured bounds;
- package-level Step 5B exports.

No Step 5B passing result is claimed yet.

## Exact continuation

From the real checkout:

```bash
git pull --ff-only

python -m unittest \
  tests.test_github_tag \
  tests.test_github_release \
  tests.test_upstream_source \
  tests.test_package_interface \
  -v

python -m unittest discover -s tests -v
```

Derived counts at the current source/test boundary are:

```text
focused: 32 tests
complete: 294 tests
```

These are derived expectations only. Observed terminal output controls validation truth.

If validation fails:

1. diagnose within the Step 5B tag/reference integration boundary unless evidence proves an older regression;
2. repair minimally;
3. rerun focused tests;
4. rerun the complete suite.

If validation passes:

1. close Step 5B as behavior-validated;
2. activate Step 5C — exact bounded repository text acquisition at the resolved immutable commit;
3. do not yet assemble semantic claims or alter CLI orchestration.

## Stop line

Until Step 5B validates, do not begin:

- Step 5C arbitrary immutable-commit repository-file acquisition;
- tagged-changelog composition;
- Step 5D interval-authority composition;
- semantic claim extraction/model integration;
- target-Python or CLI orchestration changes;
- S001 live end-to-end product execution;
- compatibility, safety, merge, defer, targeted-check, or recommendation logic.

## Explicitly not established

- a passing Step 5B focused suite;
- a passing complete suite containing Step 5B;
- live S001 Git tag resolution;
- exact changelog-file acquisition;
- live Step 1 interval authority from upstream acquisition;
- automated semantic extraction/model path;
- conditional target-Python activation in CLI runtime;
- S001 automated end-to-end relevance result;
- compatibility, safety, recommendation, maintainer action, or production readiness;
- user mastery of Steps 1–5B.

## Learning state

Steps 1–5A are behavior-validated at product level. Step 5B concepts are introduced and implemented but not yet behavior-validated.

Step 5B learning concepts include:

- **Git reference:** a named pointer such as `refs/tags/v2.8.4`;
- **lightweight tag:** a tag reference that points directly to another Git object, normally a commit;
- **annotated tag:** a tag reference whose direct target is a Git tag object containing metadata and another object pointer;
- **tag peeling:** repeatedly following annotated tag objects until the underlying non-tag object is reached;
- **immutable commit identity:** the final commit SHA later used for exact file acquisition;
- **cycle/depth bounds:** defensive rules preventing malformed or pathological object graphs from becoming unbounded acquisition work;
- **direct object versus resolved object:** the SHA named by the tag ref is not always the same SHA as the commit whose tree contains the tagged source.

Current depth:

```text
Step 5A behavior validated
+ Step 5B terminology and data flow introduced
+ educational Step 5B source/docstrings/comments available
+ controlled Step 5B tests written
+ Step 5B implementation complete
but
Step 5B local execution not yet observed
no user-owned Step 5B technical explanation recorded
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
