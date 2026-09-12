# UpgradePilot Current Memory

**Last updated:** 2026-09-12  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position

- **Current responsibility:** exact-revision requirements/constraints dependency-evidence coherence; provider snapshot-fence implementation and focused proof are committed, but executable validation is still required before B closes.
- **Mode:** Learning-by-Doing + Build/Implement validation handoff.
- **Selected parent plan:** `plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`.
- **Active working memory:** `working-memory/2026-09-12_exact-revision-requirements-constraints-evidence-coherence.md`.
- **Previous working memory:** `working-memory/2026-09-12_ci-static-runtime-correlation-bridge.md`.
- **Repository route:** continue directly on `main` unless Ali later requests otherwise.
- **Framework status:** ordinary-Python / LangGraph / LangChain comparison remains closed; no framework re-entry is justified.

The parent synthesis plan treats accepted synthesis semantics, the abstention-only evaluator, exact-attempt CI identity, and bounded static↔runtime correlation as existing foundations. Its durable dependency route prioritizes correctness/provenance reinforcement before broader evidence/action expansion.

## Current exact-revision repair — A CLOSED, B IMPLEMENTED / VALIDATION PENDING

### Problem

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

This defect is specific to patch-backed requirements/constraints evidence. `uv.lock`, admitted pyproject evidence, workflow files, and other repository-text reads already use exact SHA-bound acquisition where required.

### Selected and now implemented mechanism

The provider-owned snapshot fence remains the selected smallest adequate mechanism:

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

The durable `ChangedFile` shape remains unchanged. `contents_url` is consumed only as provider admission metadata; no duplicate `head_sha` or transport locator was propagated downstream.

GitHub repository identity is compared case-insensitively while the changed-file path and head ref remain exact. This preserves GitHub repository naming semantics without weakening file identity.

Do not confuse the changed-file `sha` Git blob identity with the PR head commit SHA.

### B commits

Implementation/proof commits in the active slice:

- `48b2b204` — add changed-file snapshot fence;
- `4d76dcb8` — add initial focused fence proof;
- `7a8fed2b` — preserve repository case-insensitive locator semantics;
- `9c3a4d0c` — protect repository case behavior;
- `ba4bbdfb` — prove drift rejection after multi-page acquisition.

A later unrelated governance commit on main does not alter this responsibility.

### Focused behavior now represented in tests

```text
stable snapshot + matching locator
→ accepted

same-count head A→B locator race
→ rejected

base/head/count drift after acquisition
→ rejected

multi-page acquisition + post-read head drift
→ rejected

missing/malformed contents_url
→ rejected

wrong repository/path locator
→ rejected

repository case-only difference
→ accepted

count disagreement
→ rejected

zero-file snapshot + post-read drift
→ rejected
```

### Current proof limit

Executable validation is **not yet claimed green**.

The repository's hosted product-verification workflow is `workflow_dispatch`-only, and the current GitHub connection does not expose a fresh workflow-dispatch action. The execution container also cannot clone the repository over the network. Therefore this session could inspect/commit source and tests and compare the locator logic with real GitHub response shapes, but could not honestly execute the repository's Python suite.

A real public `googlefonts/glyphsLib#1145` response matches the selected locator contract: its PR head SHA and changed-file `contents_url?ref=<head_sha>` agree. This is response-shape evidence, not runtime proof of the new implementation.

### Exact continuation

Before B can close, execute validation in this order:

```text
python -m unittest discover -s tests -p 'test_github_client.py' -v

python -m unittest discover -s tests -p 'test_exact_requirement_change.py' -v
python -m unittest discover -s tests -p 'test_dependency_analysis.py' -v
python -m unittest discover -s tests -p 'test_pull_request_repository_files.py' -v
python -m unittest discover -s tests -p 'test_investigation.py' -v

python -m unittest discover -s tests -v
```

If any focused proof fails, diagnose inside this same B responsibility before broadening. If the required validation is green, close B, perform the D ownership/proof review, then E selects whether this cycle is fully closed and hands off to the separate static shell/direct-install correctness responsibility.

### Alternatives remain deferred

**Exact base/head file reads** remain a valid immutable primitive but were not selected as the first repair because the candidate path set would still originate from mutable PR-files evidence and requirements extraction would need a new whole-file comparison/diff contract.

**Exact commit comparison** remains the stronger fallback if future evidence shows the client-side fence is insufficient. It was not selected first because replacing normal acquisition would narrow current changed-file detail breadth, while running a second changed-file inventory would duplicate provider/reconciliation responsibility.

### Claim limit

The implemented fence is intended as an enforceable client-side snapshot-consistency contract, not transactional/cryptographic linearizability across GitHub endpoints. It rejects observable locator or post-read base/head/count disagreement. A theoretical ABA-style external mutation that changes and returns to exactly the same observed snapshot remains outside the admitted proof boundary.

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

B — IMPLEMENTED / EXECUTABLE VALIDATION PENDING
    source + focused tests committed
    run focused → regression → full deterministic suite before closure

C — DONE FOR CURRENT STOPPING POINT
    implementation/proof progression preserved in working memory + this live owner

D — NOT STARTED
    post-action learning/ownership review follows executable evidence

E — NOT STARTED
```

## Current stop line

Do not yet:

- claim B or this correctness cycle closed before executable validation;
- repair shell/direct-install recognition in the same cycle;
- parse job logs or workflow artifacts;
- add exact wheel/version installation semantics;
- redesign Target composition;
- enable `run targeted checks` or any other non-abstention action;
- redesign CLI/reporting;
- broaden matrix/reusable/dynamic-name support merely for completeness;
- introduce generic snapshot infrastructure unless evidence proves the selected minimal repair genuinely needs a shared provider primitive.

`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-working-memory`
