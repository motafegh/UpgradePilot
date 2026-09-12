# UpgradePilot Current Memory

**Last updated:** 2026-09-12  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position

- **Current responsibility:** exact-revision requirements/constraints dependency-evidence coherence; A-phase design is complete and B is ready but not started.
- **Mode:** Learning-by-Doing handoff. Product source/test mutation requires Ali's explicit Build/Implement authorization before B begins.
- **Selected parent plan:** `plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`.
- **Active working memory:** `working-memory/2026-09-12_exact-revision-requirements-constraints-evidence-coherence.md`.
- **Previous working memory:** `working-memory/2026-09-12_ci-static-runtime-correlation-bridge.md`.
- **Repository route:** continue directly on `main` unless Ali later requests otherwise.
- **Framework status:** ordinary-Python / LangGraph / LangChain comparison remains closed; no framework re-entry is justified.

The parent synthesis plan treats accepted synthesis semantics, the abstention-only evaluator, exact-attempt CI identity, and bounded static↔runtime correlation as existing foundations. Its durable dependency route prioritizes correctness/provenance reinforcement before broader evidence/action expansion.

## Current exact-revision repair — A design CLOSED

### Problem retained

The requirements/constraints route can currently misattribute mutable PR-files patch evidence to an earlier frozen pull-request revision:

```text
PullRequestIdentity freezes head A
+
get_changed_files(identity) later reads mutable PR files
+
PR advances to head B while changed-file count stays equal
+
requirements/constraints extraction consumes B patch
+
source context is associated with identity.head_sha = A
→ B dependency evidence can be attributed to A
```

This defect is specific to patch-backed requirements/constraints evidence. `uv.lock`, admitted pyproject evidence, workflow files, and other repository-text reads already use exact SHA-bound acquisition where required.

### Selected A mechanism

The smallest adequate design is a **provider-owned snapshot fence around the existing PR-files acquisition**:

```text
frozen PullRequestIdentity A
→ acquire all PR-file pages
→ validate each changed-file head locator against A.head_sha
→ re-read PR identity after acquisition
→ require base_sha + head_sha + changed_files still equal A
→ only then return ChangedFile records
```

The relationship belongs at `GitHubPullRequestClient.get_changed_files(...)`, the earliest owner of mutable changed-file acquisition. Dependency analysis and synthesis must not reconstruct this provenance downstream.

Expected successful records do not need a duplicate durable `head_sha` merely because the provider used revision metadata to admit them. Provider validation metadata should normally be consumed and discarded unless implementation shows a real downstream need.

### Rejected first-line alternatives

**Exact base/head file reads** remain a valid immutable primitive but were not selected as the first repair because the candidate path set would still originate from mutable PR-files evidence and requirements extraction would need a new whole-file comparison/diff contract.

**Exact commit comparison** is conceptually clean and remains a stronger fallback, but GitHub's compare result has a narrower changed-file detail boundary than the current PR-files provider. Replacing normal acquisition would regress current breadth; adding a second changed-file inventory would duplicate provider responsibility.

### Claim limit

The selected fence is an enforceable client-side snapshot-consistency contract, not a claim of transactional/cryptographic linearizability across GitHub endpoints. It rejects observable file-locator or post-read PR-identity disagreement with the frozen snapshot. A theoretical external ABA-style mutation that changes and returns to the identical base/head/count inside the read window is outside the current admitted proof boundary; stronger immutable comparison evidence can be reconsidered if that threat becomes product-relevant.

## B handoff — READY / NOT STARTED

Expected primary implementation owner:

- `src/upgradepilot/github/pull_request.py`

Expected focused proof starts at:

- `tests/test_github_client.py`

Nearest regressions include exact requirements extraction, dependency analysis, investigation/application composition, and unchanged exact-file repository paths.

B must prove at minimum:

```text
stable snapshot + matching file locators
→ accepted

same-count head A→B race
→ rejected

base/head/count drift during pagination
→ rejected

missing/malformed required revision locator metadata
→ rejected

zero-file acquisition
→ still receives final identity fence

normal requirements/constraints exact-pin extraction
→ remains supported

uv.lock / admitted pyproject exact-file paths
→ remain unregressed
```

Do not confuse a per-file Git blob `sha` with the PR commit SHA.

## Maintainer-action synthesis baseline retained

The accepted maintainer-action synthesis specification remains the stable semantic owner.

The deterministic evaluator remains intentionally abstention-only:

```text
PublicPullRequestInvestigation
→ synthesize_maintainer_action(...)
→ MaintainerActionSynthesis(action="abstain")
```

No merge, targeted-check, investigate, block, or defer permission is implemented yet. Stronger technical evidence does not create action permission by itself.

## CI producer foundations retained

### Exact run/job attempt coherence — CLOSED

The mixed-rerun-attempt defect is repaired and proven. Exact job acquisition binds:

```text
frozen PR head SHA
+ workflow run ID
+ run attempt
→ jobs from that exact attempt
```

This issue remains retired unless regression evidence appears.

### Static↔runtime correlation bridge — CLOSED A→E

The first bounded bridge relates exact-head static workflow declarations to exact-attempt runtime jobs/steps only under an explicit safety contract. Dependency CI distinguishes:

```text
supported_not_correlated
supported_runtime_correlated
```

The stronger state means an already-supported static consuming step is safely tied to a runtime step reported completed/successfully, with visible `continue-on-error` masking excluded.

It still does not prove exact installed dependency version, selected wheel/sdist, artifact tags, behavioral compatibility, complete target coverage, proposal safety, or a maintainer action.

Ali's WSL proof for the completed bridge ended with the full deterministic suite green at 549 tests.

## Remaining correctness priority after the current cycle

The second confirmed correctness responsibility remains static shell/direct-install false-positive recognition.

Current bounded command-text splitting can promote install-looking comments/quoted separator payloads into positive requirements consumption. Runtime correlation can make that wrong static premise look stronger by correctly proving that the containing step ran.

Do not combine that repair with the current snapshot/provenance cycle.

## Evidence bottlenecks retained for later reassessment

After correctness is trustworthy, select the next decision-critical bottleneck rather than broadening everything:

1. preserve an already-known CI consuming `job_key` into Target composition;
2. acquire exact runtime dependency-version/artifact evidence only when a precise proposition requires it;
3. produce exact target wheel-compatibility evidence through a normal producer;
4. freshly discriminate CI acquisition-failure containment if it becomes decision-relevant;
5. broaden matrix/reusable/dynamic-name correlation only under real case/product pressure.

These are not all defects. Conservative unsupported/unresolved behavior remains valid where UpgradePilot cannot safely establish a fact.

## Durable journey

```text
accepted synthesis semantics
+ abstention-only evaluator
+ exact-attempt CI identity
+ bounded static↔runtime correlation
        ↓
CURRENT: exact-revision requirements/constraints provenance
        ↓
static command-recognition correctness
        ↓
re-audit / retire corrected trust restrictions
        ↓
select next decision-critical evidence bottleneck
        ↓
re-evaluate non-abstention action reachability
        ↓
admit one action path at a time through normal producer proof
```

## Current Learning-by-Doing cycle

```text
Slice: exact-revision requirements/constraints evidence coherence

A — DONE
    provider-owned PR-files snapshot fence selected
B — READY / NOT STARTED
    awaiting Ali's explicit Build authorization
C — NOT STARTED
D — NOT STARTED
E — NOT STARTED
```

## Current stop line

Do not yet:

- modify product source/tests before Build is explicitly authorized;
- repair shell/direct-install recognition in the same cycle;
- parse job logs or workflow artifacts;
- add exact wheel/version installation semantics;
- redesign Target composition;
- enable `run targeted checks` or any other non-abstention action;
- redesign CLI/reporting;
- broaden matrix/reusable/dynamic-name support merely for completeness;
- introduce generic snapshot infrastructure unless implementation proves the selected minimal repair genuinely needs a shared provider primitive.

`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`
