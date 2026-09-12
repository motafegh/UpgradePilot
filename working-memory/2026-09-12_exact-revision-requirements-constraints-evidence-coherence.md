# Exact-Revision Requirements/Constraints Evidence Coherence — Working Memory

**Date:** 2026-09-12  
**Session status:** ACTIVE  
**Primary mode:** Learning-by-Doing + Planning/Design  
**Selected parent plan:** [`../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)  
**Previous:** [`2026-09-12_ci-static-runtime-correlation-bridge.md`](2026-09-12_ci-static-runtime-correlation-bridge.md)

## Why this responsibility is selected

The preceding E inventory separated confirmed correctness/provenance defects from evidence bottlenecks, deliberate conservative limits, and future product gaps.

The first selected repair is the requirements/constraints patch-to-frozen-revision coherence defect because it can create **misattributed source evidence before all later exact-head reasoning**:

```text
PR identity freezes head A
+
changed-file patch is later acquired from the mutable PR files endpoint
+
PR advances to head B while changed-file count remains the same
→ B patch content can be interpreted while the dependency source context is attributed to A
```

This is more foundational than broadening correlation/Target/runtime evidence because stronger downstream evidence cannot repair a dependency transition whose snapshot identity is wrong.

The second confirmed correctness responsibility remains the static shell/direct-install false-positive defect. It is intentionally retained as the next correctness reinforcement candidate after this cycle closes; no implementation for it begins inside this record.

## Current source path

The current normal path is:

```text
GitHubPullRequestClient.get_pull_request(...)
→ PullRequestIdentity(base_sha, head_sha, changed_files, ...)

GitHubPullRequestClient.get_changed_files(identity)
→ GET /repos/{repository}/pulls/{number}/files
→ ChangedFile(..., patch=...)

analyze_dependency_change(identity, changed_files, repository_client)
→ requirements/constraints path consumes ChangedFile.patch directly
→ extract_exact_requirement_changes(...)
→ dependency/source context later receives identity.head_sha
```

By contrast, admitted `uv.lock` and pyproject optional-extra paths acquire exact base/head repository files through `GitHubRepositoryClient` before extracting the dependency transition.

Therefore the defect is **not** that UpgradePilot fails to acquire base/head SHAs or never uses immutable revisions. The defect is narrower: the requirements/constraints patch evidence itself is not proven to correspond to those frozen SHAs.

## A — pre-implementation investigation/design — DONE

### Selected invariant

Every `ChangedFile` collection admitted from the mutable PR-files endpoint must be accepted only when the pull-request provider can establish that the observed collection corresponds to the already-frozen `PullRequestIdentity` snapshot strongly enough for the current bounded product responsibility.

For the current GitHub provider, the selected smallest mechanism is a **provider-owned snapshot fence around the existing PR-files acquisition**:

```text
frozen PullRequestIdentity A
→ acquire all PR-file pages
→ validate each changed-file head locator against A.head_sha
→ re-read PR identity after acquisition
→ require base_sha + head_sha + changed_files to remain equal to A
→ only then return ChangedFile records
```

This is an acquisition/provenance responsibility of `GitHubPullRequestClient`, not a dependency-parser or synthesis responsibility.

### Evidence supporting the selection

Current source establishes that `get_changed_files(identity)` already owns PR-file pagination, response validation, and complete-count checking, but currently consumes only repository/PR number and `changed_files`; it does not use the frozen base/head SHA to establish patch correspondence.

The September 8 controlled reproduction established the exact failure that matters:

```text
identity = head A
files response = head B
changed-file count unchanged
→ dependency transition from B accepted
→ source context revision = A
```

The current provider therefore has the correct owner but an incomplete snapshot contract.

GitHub's PR-files response supplies per-file locator metadata such as `contents_url`, `raw_url`, and `blob_url`; a real public response for `googlefonts/glyphsLib#1145` showed the returned file locators carrying the same exact head SHA as the PR identity. This metadata is currently discarded by `ChangedFile`, which is acceptable if it is validated at the provider boundary before the trusted record is returned.

The final PR-identity re-read closes the separate observation window around pagination: base/head/count drift while files are being acquired becomes an explicit response-coherence failure instead of being silently accepted.

### Why exact base/head file reads were not selected as the first repair

Exact repository-file acquisition is already a strong immutable primitive and remains correct for `uv.lock` and admitted pyproject evidence. It was not selected for requirements/constraints because it does not independently solve the whole current responsibility:

```text
mutable PR-files path discovery
+ exact file reads for those discovered paths
```

can still start from a path set belonging to a later PR state.

Using only exact files would also require a new whole-file requirements comparison/extraction contract or local diff reconstruction, replacing the current bounded patch-oriented extractor even though the defect is snapshot binding rather than exact-pin parsing.

Therefore exact file reads are a credible stronger mechanism, but not the smallest adequate first correction.

### Why exact base→head commit comparison was not selected as the first repair

An immutable commit comparison is conceptually clean because it can bind changed-file paths and diff evidence directly to explicit base/head SHAs. It also aligns naturally with the existing patch-oriented requirements extractor.

However, GitHub's comparison JSON exposes changed-file detail only for a smaller bounded result set than the current PR-files provider. Replacing the normal changed-file provider with compare evidence would therefore narrow an already-supported acquisition boundary, while adding a second changed-file inventory only for dependency analysis would duplicate provider semantics and reconciliation responsibility.

Keep exact commit comparison as a stronger fallback/re-entry mechanism if later evidence shows the provider-level snapshot fence is insufficient for the admitted responsibility.

### Why mutable PR-files + snapshot revalidation is the selected baseline

It satisfies the current responsibility with the smallest ownership and migration surface:

- keeps changed-file acquisition in its existing provider owner;
- keeps the current PR-files pagination and finite acquisition boundary;
- keeps the existing `ChangedFile` application record shape unless implementation evidence proves a new field is necessary;
- keeps `extract_exact_requirement_changes(...)` patch-oriented;
- catches the already-reproduced same-count A→B race through per-file head-locator validation;
- catches observable base/head/count drift across pagination through the post-acquisition identity fence;
- avoids duplicating revision checks in dependency analysis or synthesis;
- does not require a new generic snapshot service or exact-diff subsystem.

This is consistent with Core `SNAP-001`, `PROV-001`, `JUST-003`, and `JUST-004`.

### Validation metadata should normally be consumed and discarded

The selected design does **not** require adding a duplicate `head_sha` to every successful `ChangedFile` merely because the provider used head metadata to validate the response.

Preferred responsibility:

```text
external changed-file response
→ provider validates path/head/snapshot relationship
→ trusted ChangedFile keeps only downstream-needed fields
```

This follows the existing exact-file provider pattern: transport metadata needed to admit a response does not automatically become durable domain evidence.

### Important claim limit

The selected snapshot fence is an enforceable client-side consistency contract, not a claim of transactional or cryptographic linearizability across GitHub endpoints.

It establishes:

> UpgradePilot will not accept mutable PR-file patch evidence when the file locator metadata or the post-acquisition PR identity contradicts the frozen PR snapshot.

A theoretical external ABA-style mutation that changes and then returns to exactly the same base/head/count during the observation window is not independently observable through these reads. Solving adversarial transactional consistency would require a stronger immutable source such as exact comparison evidence and is not currently justified by the product evidence horizon.

Do not overstate the selected mechanism beyond the race/provenance class it can actually detect.

## B handoff — bounded Build responsibility

B is ready but has not started. Product source/test mutation requires Ali's Build authorization.

### Expected owning changes

Primary owner:

- `src/upgradepilot/github/pull_request.py`

Likely focused proof owner:

- `tests/test_github_client.py`

Nearest regression/integration evidence:

- `tests/test_exact_requirement_change.py`
- `tests/test_dependency_analysis.py`
- `tests/test_investigation.py` where normal-path acquisition/composition pressure is needed
- `tests/test_pull_request_repository_files.py` for unchanged exact-file paths

`src/upgradepilot/dependency/analysis.py` and `src/upgradepilot/dependency/requirements.py` should remain unchanged unless implementation evidence shows a genuinely necessary migration. Snapshot correspondence must not be reconstructed downstream merely because those modules consume the admitted patch.

### Implementation shape to prove, not blindly copy

The expected minimal provider behavior is:

1. acquire all changed-file pages under the frozen identity;
2. validate provider-supplied per-file head locator metadata against `identity.head_sha` and the requested repository/path;
3. retain the existing changed-file count completeness check;
4. re-read the PR identity after acquisition, including the zero-file path;
5. reject when `base_sha`, `head_sha`, or `changed_files` differs from the frozen identity;
6. only then return the trusted `ChangedFile` collection.

During Build, inspect exact GitHub response/status semantics before hardcoding one URL parser. In particular, do not confuse a changed-file `sha` (Git blob identity) with a PR commit SHA. If an admitted file status exposes locator semantics that cannot prove the required relationship, fail closed or narrow the supported response shape rather than guessing.

## Required Build proof

The B slice must discriminate at least:

```text
STABLE SNAPSHOT
frozen base/head/count + matching file head locators + unchanged post-read
→ supported requirements transition remains established

SAME-COUNT HEAD RACE
identity captures head A
files response locators identify head B
changed-file count remains equal
→ reject before dependency extraction

BASE DRIFT
files can look head-consistent but the PR base changed during acquisition
→ final identity fence rejects

PAGINATION DRIFT
PR base/head/count changes while pages are being acquired
→ final identity fence rejects

COUNT DISAGREEMENT
existing completeness check
→ remains rejected

MALFORMED / MISSING REQUIRED LOCATOR METADATA
→ cannot become trusted changed-file evidence

ZERO-FILE SNAPSHOT
identity.changed_files == 0
→ snapshot still receives final identity revalidation rather than bypassing the fence

NORMAL REQUIREMENTS + CONSTRAINTS
→ current exact-pin extraction semantics remain supported

STRUCTURED EXACT-FILE PATHS
uv.lock / admitted pyproject exact base/head acquisition
→ remain correct and unregressed
```

Proof must exercise the normal provider path, not only manually constructed trusted `ChangedFile` objects.

Validation order after implementation:

```text
focused GitHub PR provider tests
→ exact requirements / dependency-analysis regressions
→ nearest investigation/application regressions
→ full deterministic suite
```

## Stop line

This cycle owns only requirements/constraints snapshot/provenance coherence.

Do not in this cycle:

- repair shell/direct-install parsing;
- add matrix/reusable workflow correlation;
- parse job logs or artifacts;
- prove exact installed dependency version/wheel;
- redesign Target artifact-environment composition;
- enable targeted checks or another non-abstention maintainer action;
- redesign CLI/reporting;
- introduce generic repository snapshot infrastructure unless implementation proves the smallest selected repair genuinely needs a shared provider primitive.

## Current Learning-by-Doing state

```text
Slice: exact-revision requirements/constraints evidence coherence

A — DONE
    provider-owned PR-files snapshot fence selected
B — READY / NOT STARTED
    awaiting explicit Build authorization
C — NOT STARTED
D — NOT STARTED
E — NOT STARTED
```

No product source/test mutation occurred in A.

`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`
