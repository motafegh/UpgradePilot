# Exact-Revision Requirements/Constraints Evidence Coherence — Working Memory

**Date:** 2026-09-12  
**Session status:** ACTIVE  
**Primary mode:** Learning-by-Doing + Build/Implement  
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

The normal path remains:

```text
GitHubPullRequestClient.get_pull_request(...)
→ PullRequestIdentity(base_sha, head_sha, changed_files, ...)

GitHubPullRequestClient.get_changed_files(identity)
→ GET /repos/{repository}/pulls/{number}/files
→ provider validates changed-file snapshot correspondence
→ ChangedFile(..., patch=...)

analyze_dependency_change(identity, changed_files, repository_client)
→ requirements/constraints path consumes ChangedFile.patch directly
→ extract_exact_requirement_changes(...)
→ dependency/source context later receives identity.head_sha
```

By contrast, admitted `uv.lock` and pyproject optional-extra paths acquire exact base/head repository files through `GitHubRepositoryClient` before extracting the dependency transition.

Therefore the repair does not redesign dependency semantics. It strengthens the provider trust boundary that produces the patch-backed `ChangedFile` evidence.

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

The pre-B source established that `get_changed_files(identity)` already owned PR-file pagination, response validation, and complete-count checking, but consumed only repository/PR number and `changed_files`; it did not use the frozen base/head SHA to establish patch correspondence.

The September 8 controlled reproduction established the exact failure that matters:

```text
identity = head A
files response = head B
changed-file count unchanged
→ dependency transition from B accepted
→ source context revision = A
```

GitHub's PR-files response supplies per-file locator metadata such as `contents_url`, `raw_url`, and `blob_url`; a real public response for `googlefonts/glyphsLib#1145` showed the returned `contents_url` carrying the same exact head SHA as the PR identity. The separate changed-file `sha` is a Git blob identity and is not the PR head commit SHA.

The final PR-identity re-read closes the separate observation window around pagination: base/head/count drift while files are being acquired becomes an explicit response-coherence failure instead of being silently accepted.

### Why exact base/head file reads were not selected as the first repair

Exact repository-file acquisition is already a strong immutable primitive and remains correct for `uv.lock` and admitted pyproject evidence. It was not selected for requirements/constraints because it does not independently solve the whole current responsibility:

```text
mutable PR-files path discovery
+ exact file reads for those discovered paths
```

can still start from a path set belonging to a later PR state.

Using only exact files would also require a new whole-file requirements comparison/extraction contract or local diff reconstruction, replacing the current bounded patch-oriented extractor even though the defect is snapshot binding rather than exact-pin parsing.

### Why exact base→head commit comparison was not selected as the first repair

An immutable commit comparison is conceptually clean because it can bind changed-file paths and diff evidence directly to explicit base/head SHAs. It also aligns naturally with the existing patch-oriented requirements extractor.

However, GitHub's comparison JSON exposes changed-file detail only for a smaller bounded result set than the current PR-files provider. Replacing the normal changed-file provider with compare evidence would therefore narrow an already-supported acquisition boundary, while adding a second changed-file inventory only for dependency analysis would duplicate provider semantics and reconciliation responsibility.

Keep exact commit comparison as a stronger fallback/re-entry mechanism if later evidence shows the provider-level snapshot fence is insufficient for the admitted responsibility.

### Why mutable PR-files + snapshot revalidation is the selected baseline

It satisfies the current responsibility with the smallest ownership and migration surface:

- keeps changed-file acquisition in its existing provider owner;
- keeps the current PR-files pagination and finite acquisition boundary;
- keeps the existing `ChangedFile` application record shape;
- keeps `extract_exact_requirement_changes(...)` patch-oriented;
- catches the already-reproduced same-count A→B race through per-file head-locator validation;
- catches observable base/head/count drift across pagination through the post-acquisition identity fence;
- avoids duplicating revision checks in dependency analysis or synthesis;
- does not require a new generic snapshot service or exact-diff subsystem.

This remains consistent with Core `SNAP-001`, `PROV-001`, `JUST-003`, and `JUST-004`.

### Validation metadata is consumed and discarded

The implementation does **not** add a duplicate `head_sha` to every successful `ChangedFile`.

```text
external changed-file response
→ provider validates repository/path/head/snapshot relationship
→ trusted ChangedFile keeps only downstream-needed fields
```

`contents_url` is therefore provider-only admission metadata. The durable `ChangedFile` contract remains unchanged.

### Important claim limit

The selected snapshot fence is an enforceable client-side consistency contract, not a claim of transactional or cryptographic linearizability across GitHub endpoints.

It is intended to establish:

> UpgradePilot will not accept mutable PR-file patch evidence when the required file locator metadata or the post-acquisition PR identity contradicts the frozen PR snapshot.

A theoretical external ABA-style mutation that changes and then returns to exactly the same base/head/count during the observation window is not independently observable through these reads. Solving adversarial transactional consistency would require a stronger immutable source such as exact comparison evidence and is not currently justified by the product evidence horizon.

## B — bounded Build implementation — IMPLEMENTED / EXECUTABLE VALIDATION PENDING

Ali explicitly authorized B after the A-phase learning review.

### Product implementation

Primary owner changed:

- `src/upgradepilot/github/pull_request.py`

Implementation commits in this B slice:

- `48b2b204` — add the provider-owned changed-file snapshot fence;
- `7a8fed2b` — preserve GitHub's case-insensitive repository identity while keeping file-path matching exact.

Current behavior:

```text
PullRequestIdentity A
→ acquire PR-files pages when changed_files > 0
→ require each changed-file contents_url to identify:
     GitHub API host
     same repository identity
     exact returned filename
     ref == A.head_sha
→ retain existing complete-count check
→ re-read PR identity even for changed_files == 0
→ require final base_sha/head_sha/changed_files == A
→ only then return tuple[ChangedFile, ...]
```

The required locator is the canonical API `contents_url`. The implementation intentionally does not validate all equivalent `blob_url`/`raw_url` representations because they would repeat the same repository/path/head proposition without adding an independent proof responsibility.

The changed-file `sha` remains unused for revision binding because it identifies a Git blob, not the PR head commit.

### Build-time refinement: repository case semantics

Initial implementation review exposed a compatibility edge:

```text
caller identity.repository = GoogleFonts/glyphsLib
GitHub locator repository = googlefonts/glyphsLib
```

GitHub repository identity is case-insensitive, but Git repository file paths are case-sensitive. A naïve full decoded-path comparison would therefore reject a valid repository spelling while trying to enforce exact file identity.

The implementation was narrowed so that:

- owner/repository comparison is case-insensitive;
- the `contents` marker and filename remain exact/case-sensitive;
- the head `ref` remains exact.

This keeps the snapshot fence from introducing an unrelated repository-locator regression.

### Focused proof added

Focused proof owner changed:

- `tests/test_github_client.py`

Test commits in this B slice:

- `4d76dcb8` — establish the snapshot-fence proof family;
- `9c3a4d0c` — protect case-insensitive repository locator semantics;
- `ba4bbdfb` — add explicit multi-page drift rejection.

The focused tests now discriminate:

```text
stable matching locator + stable post-read
→ accepted ChangedFile

same-count head A→B locator mismatch
→ rejected before dependency extraction

base/head/count drift after acquisition
→ rejected

multi-page acquisition followed by head drift
→ rejected

missing/malformed contents_url
→ rejected

wrong repository or wrong file path in locator
→ rejected

repository case-only difference
→ accepted while exact file-path semantics remain

count disagreement
→ remains rejected

zero-file snapshot with post-read drift
→ rejected instead of bypassing the fence
```

The test also protects that `contents_url` remains validation-only metadata and is not added to the durable `ChangedFile` record.

### Real external response-shape check

During B, the live/public response for `googlefonts/glyphsLib#1145` was re-inspected. Its PR metadata identified:

```text
head_sha = f3cda8a94600e58d27f1bc17c99b7693718b6350
changed_files = 1
```

and its changed-file response for `requirements-dev.txt` contained:

```text
contents_url = .../contents/requirements-dev.txt?ref=f3cda8a94600e58d27f1bc17c99b7693718b6350
```

which matches the selected locator contract. Current GitHub REST documentation also retains the PR-files endpoint's 3000-file maximum, matching the provider's existing bound.

This is response-shape evidence, not execution proof of the new Python implementation.

### Validation status and proof limit

Executable validation is **not yet claimed green**.

The repository's hosted verification workflow is intentionally `workflow_dispatch`-only. The current GitHub connector exposes read/re-run actions but no action to dispatch a fresh workflow run for the new commit. The execution container also has no network route to clone the repository. Therefore this session could not honestly execute the repository's focused or full Python suite.

Available validation performed here:

- inspected the committed source diff and focused test diff;
- checked the selected parser logic against the real `contents_url` shape;
- re-inspected nearest regression owners:
  - `tests/test_dependency_analysis.py` still establishes requirements patch extraction and exact `uv.lock` base/head acquisition as separate paths;
  - `tests/test_pull_request_repository_files.py` still owns exact immutable base/head repository-file behavior;
  - `tests/test_investigation.py` composes through the unchanged public `get_changed_files(identity) -> tuple[ChangedFile, ...]` contract;
- confirmed `ChangedFile` shape and dependency-analysis/requirements source were not changed.

This establishes implementation and proof intent, but **does not establish runtime green**.

### Required executable validation before B closes

Run in this order when an executable repository environment is available:

```text
python -m unittest discover -s tests -p 'test_github_client.py' -v

python -m unittest discover -s tests -p 'test_exact_requirement_change.py' -v
python -m unittest discover -s tests -p 'test_dependency_analysis.py' -v
python -m unittest discover -s tests -p 'test_pull_request_repository_files.py' -v
python -m unittest discover -s tests -p 'test_investigation.py' -v

python -m unittest discover -s tests -v
```

If any focused proof fails, diagnose inside this same B responsibility before broadening.

## Stop line

This cycle still owns only requirements/constraints snapshot/provenance coherence.

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

B — IMPLEMENTED / EXECUTABLE VALIDATION PENDING
    source + focused proof committed
    runtime test execution still required before B can close

C — DONE FOR CURRENT STOPPING POINT
    implementation/proof progression preserved here and in MEMORY.md

D — NOT STARTED
    post-action ownership/learning review follows executable evidence

E — NOT STARTED
```

`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-working-memory`
