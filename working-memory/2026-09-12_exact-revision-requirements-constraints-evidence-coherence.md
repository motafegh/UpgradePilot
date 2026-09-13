# Exact-Revision Requirements/Constraints Evidence Coherence — Working Memory

**Date:** 2026-09-12  
**Session status:** ACTIVE  
**Primary mode:** Learning-by-Doing — E closeout / next-slice review  
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

The normal path is now:

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

Therefore this repair does not redesign dependency semantics. It strengthens the provider trust boundary that produces patch-backed `ChangedFile` evidence.

## A — pre-implementation investigation/design — DONE

### Selected invariant

Every `ChangedFile` collection admitted from the mutable PR-files endpoint must be accepted only when the pull-request provider can establish that the observed collection corresponds to the already-frozen `PullRequestIdentity` snapshot strongly enough for the current bounded product responsibility.

The selected smallest mechanism is a **provider-owned snapshot fence around the existing PR-files acquisition**:

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

The pre-B source established that `get_changed_files(identity)` already owned PR-file pagination, response validation, and complete-count checking, but did not use the frozen base/head SHA to establish patch correspondence.

The September 8 controlled reproduction established the exact failure that matters:

```text
identity = head A
files response = head B
changed-file count unchanged
→ dependency transition from B accepted
→ source context revision = A
```

GitHub's PR-files response supplies per-file locator metadata such as `contents_url`, `raw_url`, and `blob_url`; a real public response for `googlefonts/glyphsLib#1145` showed the returned `contents_url` carrying the same exact head SHA as the PR identity. The separate changed-file `sha` is a Git blob identity and is not the PR head commit SHA.

The final PR-identity re-read closes the separate observation window around pagination: observable base/head/count drift while files are being acquired becomes an explicit response-coherence failure instead of being silently accepted.

### Alternatives retained but not selected first

**Exact base/head file reads** remain a valid immutable primitive but were not selected first because the candidate path set would still originate from mutable PR-files evidence and requirements extraction would need a new whole-file comparison/diff contract.

**Exact base→head commit comparison** remains the stronger immutable fallback. It was not selected first because GitHub comparison changed-file detail has a narrower bounded result set than the current PR-files provider; replacing normal acquisition would narrow current breadth, while running a second changed-file inventory would duplicate provider/reconciliation responsibility.

### Why the selected baseline is proportionate

Mutable PR-files + snapshot revalidation:

- keeps changed-file acquisition in its existing provider owner;
- keeps the current PR-files pagination and finite acquisition boundary;
- keeps the existing `ChangedFile` application record shape;
- keeps `extract_exact_requirement_changes(...)` patch-oriented;
- catches the reproduced same-count A→B race through per-file head-locator validation;
- catches observable base/head/count drift across pagination through the post-acquisition identity fence;
- avoids duplicating revision checks in dependency analysis or synthesis;
- does not require generic snapshot infrastructure or an exact-diff subsystem.

This remains consistent with Core `SNAP-001`, `PROV-001`, `JUST-003`, and `JUST-004`.

### Validation metadata is consumed and discarded

The implementation does **not** add a duplicate `head_sha` to every successful `ChangedFile`:

```text
external changed-file response
→ provider validates repository/path/head/snapshot relationship
→ trusted ChangedFile keeps only downstream-needed fields
```

`contents_url` is provider-only admission metadata. The durable `ChangedFile` contract remains unchanged.

### Claim limit

The selected snapshot fence is an enforceable client-side consistency contract, not transactional or cryptographic linearizability across GitHub endpoints.

It establishes the bounded claim:

> UpgradePilot will not accept mutable PR-file patch evidence when required file-locator metadata or the post-acquisition PR identity contradicts the frozen PR snapshot.

A theoretical external ABA-style mutation that changes and returns to exactly the same base/head/count during the observation window is not independently observable through these reads. A stronger immutable source such as exact comparison evidence can be reconsidered only if that threat becomes product-relevant.

## B — bounded Build implementation — DONE

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

The implementation intentionally does not validate all equivalent `blob_url`/`raw_url` representations because they repeat the same repository/path/head proposition without adding an independent proof responsibility.

The changed-file `sha` remains unused for revision binding because it identifies a Git blob, not the PR head commit.

### Build-time refinement: repository case semantics

Implementation review exposed a compatibility edge:

```text
caller identity.repository = GoogleFonts/glyphsLib
GitHub locator repository = googlefonts/glyphsLib
```

GitHub repository identity is case-insensitive, but Git repository file paths are case-sensitive. The implementation was narrowed so that:

- owner/repository comparison is case-insensitive;
- the `contents` marker and filename remain exact/case-sensitive;
- the head `ref` remains exact.

This prevents the snapshot fence from introducing an unrelated repository-locator regression.

### Focused proof added

Focused proof owner changed:

- `tests/test_github_client.py`

Test commits in this B slice:

- `4d76dcb8` — establish the snapshot-fence proof family;
- `9c3a4d0c` — protect case-insensitive repository locator semantics;
- `ba4bbdfb` — add explicit multi-page drift rejection.

The focused tests discriminate:

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

The proof also protects that `contents_url` remains validation-only metadata and is not added to the durable `ChangedFile` record.

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

which matches the selected locator contract. This was response-shape evidence supporting the implementation choice, not by itself executable proof.

### Executable validation — GREEN

Ali executed the required validation locally from the synchronized `main` branch and active project virtual environment.

Focused provider proof:

```text
python -m unittest discover -s tests -p 'test_github_client.py' -v
→ 13 tests passed
```

Nearby regression proof:

```text
test_exact_requirement_change.py
test_dependency_analysis.py
test_pull_request_repository_files.py
test_investigation.py
→ 15 tests passed
```

Full deterministic regression:

```text
python -m unittest discover -s tests -v
→ 566 tests passed
```

Interpretation:

- the new provider snapshot fence behaves as intended under the focused controlled cases;
- existing requirements extraction, dependency coordination, exact `uv.lock`/repository-file behavior, and investigation composition remain green in the selected nearby regressions;
- the complete current deterministic product test horizon remains green after the change.

These tests do **not** establish transactional GitHub snapshot isolation, eliminate the theoretical ABA limitation, or prove live external-service behavior beyond the separately inspected response shape.

B is therefore closed at the admitted implementation/proof boundary.

## C — progressive state preservation — DONE

The A reasoning, B implementation/refinement, response-shape evidence, proof limits, exact commits, and final executable validation are preserved in this record. `MEMORY.md` is separately reconciled to the compact live position.

## D — post-action learning / ownership review — DONE

D was intentionally kept as one integrated teaching round plus one ownership-check round rather than being expanded into a nested mini-cycle.

### Learning-by-Doing stage-granularity rule

Ali explicitly clarified the preferred cycle discipline:

> A→B→C→D→E are the real cycle stages. Do not recursively turn each stage into another elaborate sub-cycle. By default, finish each stage in one or two substantive rounds. Use more only when the situation genuinely demands it or Ali explicitly asks for smaller sub-cycles.

This is a session/process preference for applying the existing Learning-by-Doing loop, not a redefinition of the loop itself.

### Ownership transferred

The integrated D review covered the job-relevant concepts behind A/B/C rather than line-by-line memorization:

- TOCTOU / race-condition reasoning;
- evidence provenance and exact revision attribution;
- provider trust boundaries versus downstream domain semantics;
- immutable identifiers versus mutable PR state;
- fail-closed evidence admission;
- smallest sufficient design rather than strongest imaginable mechanism;
- validation-only metadata and keeping trusted domain objects small;
- layered proof: focused behavior → nearby integration/regression → full deterministic regression;
- explicit proof limits, including external-service behavior and the theoretical ABA gap.

Ali's ownership-check answers established the core reasoning:

1. **Same-count A→B race:** if the PR head changes while the file count stays equal, a count-only check cannot detect that the returned changed-file evidence belongs to another head.
2. **Provider ownership:** snapshot correspondence belongs at the provider trust boundary so downstream consumers receive already-admitted evidence instead of each reimplementing GitHub-specific provenance checks.
3. **Two checks:** Ali correctly identified the need to ensure correct files and the same PR revision; the refinement is that these are distinct proof responsibilities rather than generic duplicate safety — per-file `contents_url` binds each file to the frozen head, while the final PR reread detects observable base/head/count drift across the complete acquisition window.
4. **Proof limit:** deterministic tests cover modeled scenarios and local product behavior but cannot control or prove all external GitHub mutations/service behavior; therefore they do not establish atomic/transactional snapshot consistency or eliminate an unobservable ABA transition.

D therefore closes without reopening implementation.

## E — bounded gap / next-slice review — NEXT

E should now answer one bounded question: did this exact-revision cycle expose any remaining defect inside its own responsibility that justifies reopening it?

Current evidence going into E says:

- the reproduced same-count provenance defect is repaired at the selected owner;
- focused, nearby, and full deterministic proof are green;
- no new correctness gap was discovered during D;
- exact commit comparison remains a deliberate stronger fallback, not an unfinished requirement;
- theoretical ABA remains an explicit non-claim rather than a currently justified product defect.

Unless E finds contradictory evidence, close this exact-revision cycle and hand off to the separately retained **static shell/direct-install false-positive recognition** correctness responsibility.

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
- introduce generic repository snapshot infrastructure without new evidence that the selected bounded repair is insufficient.

## Current Learning-by-Doing state

```text
Slice: exact-revision requirements/constraints evidence coherence

A — DONE
    provider-owned PR-files snapshot fence selected

B — DONE
    source + focused proof committed
    13 focused + 15 nearby + 566 full deterministic tests green

C — DONE
    progression and final proof preserved in working memory + MEMORY.md

D — DONE
    integrated ownership review passed; one refinement recorded for the two-check distinction

E — NEXT
    bounded gap review / cycle closure and next-slice handoff
```

`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-working-memory`
