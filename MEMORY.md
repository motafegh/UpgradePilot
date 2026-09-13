# UpgradePilot Current Memory

**Last updated:** 2026-09-13  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position

- **Current responsibility:** exact-revision requirements/constraints dependency-evidence coherence; A design and B implementation/proof are complete, and D post-action ownership review is next.
- **Mode:** Learning-by-Doing post-action review. No further product mutation is currently required for this slice.
- **Selected parent plan:** `plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`.
- **Active working memory:** `working-memory/2026-09-12_exact-revision-requirements-constraints-evidence-coherence.md`.
- **Previous working memory:** `working-memory/2026-09-12_ci-static-runtime-correlation-bridge.md`.
- **Repository route:** continue directly on `main` unless Ali later requests otherwise.
- **Framework status:** ordinary-Python / LangGraph / LangChain comparison remains closed; no framework re-entry is justified.

The parent synthesis plan continues to treat accepted synthesis semantics, the abstention-only evaluator, exact-attempt CI identity, and bounded static↔runtime correlation as existing foundations. The durable route still prioritizes correctness/provenance reinforcement before broader evidence/action expansion.

## Current exact-revision repair — A + B CLOSED

### Problem repaired

The requirements/constraints route could misattribute mutable PR-files patch evidence to an earlier frozen pull-request revision:

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

This defect was specific to patch-backed requirements/constraints evidence. `uv.lock`, admitted pyproject evidence, workflow files, and other repository-text reads already use exact SHA-bound acquisition where required.

### Selected and implemented mechanism

`GitHubPullRequestClient.get_changed_files(...)` now owns a provider-level snapshot fence:

```text
frozen PullRequestIdentity A
→ acquire all PR-file pages
→ require each changed-file contents_url to identify:
     same repository identity
     exact returned filename
     ref == A.head_sha
→ retain complete-count check
→ re-read PR identity after acquisition, including zero-file snapshots
→ require base_sha + head_sha + changed_files still equal A
→ only then return ChangedFile records
```

Primary implementation owner:

- `src/upgradepilot/github/pull_request.py`

Focused proof owner:

- `tests/test_github_client.py`

The durable `ChangedFile` shape remains unchanged. `contents_url` is consumed only as provider admission metadata; no duplicate `head_sha` or transport locator is propagated downstream.

GitHub repository identity is compared case-insensitively while the changed-file path and head ref remain exact. The changed-file `sha` remains intentionally unused for revision binding because it identifies a Git blob, not the PR head commit.

### B implementation/proof commits

- `48b2b204` — add changed-file snapshot fence;
- `4d76dcb8` — add initial focused fence proof;
- `7a8fed2b` — preserve repository case-insensitive locator semantics;
- `9c3a4d0c` — protect repository case behavior;
- `ba4bbdfb` — prove drift rejection after multi-page acquisition.

### Executable proof — GREEN

Ali synchronized local `main`, activated the project virtual environment, and ran the required validation sequence.

```text
Focused provider proof:
13 tests passed

Nearby regressions:
15 tests passed

Full deterministic suite:
566 tests passed
```

The nearby regressions covered exact requirements extraction, dependency analysis, pull-request exact repository-file behavior, and investigation composition.

Current admitted proof:

- stable matching changed-file snapshots are accepted;
- same-count head drift is rejected by per-file locator validation;
- observable base/head/count drift around acquisition, including multi-page and zero-file cases, is rejected;
- malformed/missing or wrong-repository/path locators are rejected;
- existing requirements, dependency-analysis, exact-file, and investigation paths remain green;
- the complete current deterministic product test horizon remains green.

### Claim limit retained

The implemented fence is an enforceable client-side snapshot-consistency contract, not transactional or cryptographic linearizability across GitHub endpoints.

It rejects observable locator or post-read base/head/count disagreement. A theoretical external ABA-style mutation that changes and returns to the same observed base/head/count during the read window remains outside the admitted proof boundary. Exact base→head commit comparison remains the stronger fallback if future evidence makes that threat product-relevant.

## Current Learning-by-Doing cycle

```text
Slice: exact-revision requirements/constraints evidence coherence

A — DONE
    provider-owned PR-files snapshot fence selected

B — DONE
    implementation + focused/nearby/full executable proof green

C — DONE
    detailed progression and final proof preserved in working memory
    compact live state reconciled here

D — NEXT
    post-action learning / ownership review

E — NOT STARTED
```

D should review, without reopening implementation by default:

1. why snapshot correspondence belongs in the GitHub provider rather than `requirements.py`;
2. why per-file locator validation and the final PR reread protect different observation windows;
3. why `contents_url` remains admission metadata rather than a durable `ChangedFile` field;
4. what the 13 → 15 → 566 proof progression establishes at each layer;
5. what stronger transactional/ABA claims remain unsupported.

If D exposes no concrete correctness gap, E should close this exact-revision cycle and hand off to the separately retained static shell/direct-install false-positive correctness responsibility.

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

The mixed-rerun-attempt defect remains repaired and proven. Exact job acquisition binds:

```text
frozen PR head SHA
+ workflow run ID
+ run attempt
→ jobs from that exact attempt
```

Do not reopen it without regression evidence.

### Static↔runtime correlation bridge — CLOSED A→E

The first bounded bridge relates exact-head static workflow declarations to exact-attempt runtime jobs/steps under its accepted safety contract. Dependency CI distinguishes:

```text
supported_not_correlated
supported_runtime_correlated
```

The stronger state means an already-supported static consuming step is safely tied to a runtime step reported completed/successfully, with visible `continue-on-error` masking excluded.

It still does not prove exact installed dependency version, selected wheel/sdist, artifact tags, behavioral compatibility, complete target coverage, proposal safety, or a maintainer action.

## Remaining correctness priority after this cycle

The next confirmed correctness responsibility remains **static shell/direct-install false-positive recognition**.

Current bounded command-text splitting can promote install-looking comments/quoted separator payloads into positive requirements consumption. Runtime correlation can make that wrong static premise look stronger by correctly proving that the containing step ran.

Do not combine that repair with the current D/E closure of the exact-revision cycle.

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
+ exact-revision requirements/constraints provenance repair
        ↓
CURRENT: D/E closeout of exact-revision cycle
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

## Current stop line

Do not now:

- reopen B without concrete failing evidence;
- repair shell/direct-install recognition before this cycle's D/E closeout;
- parse job logs or workflow artifacts;
- add exact wheel/version installation semantics;
- redesign Target composition;
- enable `run targeted checks` or another non-abstention action;
- redesign CLI/reporting;
- broaden matrix/reusable/dynamic-name support merely for completeness;
- introduce generic snapshot infrastructure without evidence that the current bounded mechanism is insufficient.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-working-memory`
