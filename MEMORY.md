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
- **Behavior-validated:** parent-plan Steps 1–4 and Step 5A–5C.
- **Current responsibility:** Step 5D — deterministic integration of acquired crossed-release and tagged-changelog evidence through the existing Step 1 authority assembler.
- **Current Step 5D state:** integration proof implemented; **local validation is required before the remaining live S001 Step 5 acquisition proof begins**.
- **Step 5C validation record:** [`working-memory/2026-08-02_B2-step-5c-tagged-changelog-validation.md`](working-memory/2026-08-02_B2-step-5c-tagged-changelog-validation.md)
- **Step 5D integration record:** [`working-memory/2026-08-02_B2-step-5d-interval-authority-integration.md`](working-memory/2026-08-02_B2-step-5d-interval-authority-integration.md)

## Last behavior-validated executable boundary

Step 5C source/test behavior is validated through:

```text
6aa809059a54f2a65cf00409c33d2758f17694d0
```

The user reported the complete deterministic suite:

```text
Ran 310 tests in 0.054s

OK
```

The exact focused Step 5C summary was not supplied and is not invented. The complete discovery run includes the exact-commit repository-file, tagged-changelog composition, prior PR exact-file regression, and package-interface tests, so another focused rerun is not required solely to establish the same behavior.

## Step 5C closure

Step 5C is **closed and behavior-validated**.

Established acquisition/composition flow:

```text
GitHubTagCommitEvidence.resolved_commit_sha
+ explicit repository-relative changelog path
→ GitHubRepositoryClient.get_exact_commit_text_file(...)
→ ExactRepositoryTextFile

DependencyReleaseInterval
+ GitHubTagCommitEvidence
+ ExactRepositoryFileEvidence
→ build_tagged_changelog_evidence(...)
→ TaggedChangelogEvidence
   or explicit UpstreamAuthoritySourceProblem
```

Validated behavior includes immutable commit-only acquisition, path/blob/byte/UTF-8 evidence, actual file retrieval time, repository/commit joins, proposed-version tag identity, and explicit unavailable/identity/malformed states.

No live S001 changelog acquisition is claimed by this deterministic validation.

## Step 5D integration boundary awaiting validation

The Step 5D executable change is test-only:

```text
2fff38d86be18d544249f45d7f19e82f9d78f8d6
```

Created:

```text
tests/test_upstream_interval_acquisition_integration.py
```

No production source changed because Step 1 already owns the correct composition function:

```text
assemble_upstream_interval_authority(...)
```

Adding another production wrapper would duplicate authority ownership without adding evidence or behavior.

## Step 5D deterministic data flow

The controlled integration test exercises the already implemented responsibilities as one chain:

```text
PackageReleaseIndexEvidence
→ select_crossed_release_index(...)
→ CrossedReleaseIndexEvidence

GitHubTagCommitEvidence
+ ExactRepositoryTextFile
→ build_tagged_changelog_evidence(...)
→ TaggedChangelogEvidence

CrossedReleaseIndexEvidence
+ TaggedChangelogEvidence
→ assemble_upstream_interval_authority(...)
→ AuthoritativeUpstreamIntervalEvidence
```

### Minimum authority proof

The S001-shaped controlled interval is:

```text
soupsieve 2.6 → 2.8.4
```

with expected admitted crossed releases:

```text
2.7
2.8
2.8.1
2.8.2
2.8.3
2.8.4
```

The test proves that:

```text
complete crossed-release index
+ exact proposed-tag changelog
+ no GitHub Release bodies
→ authority_basis = tagged_changelog
```

This is the intentionally selected minimum Step 1 authority path for S001.

### Identity-preservation proof

A second integration case supplies individually valid crossed-release and tagged-changelog records from different dependency intervals.

Expected result:

```text
identity_mismatch
```

Step 5D therefore cannot erase interval identity merely because both inputs are structurally valid.

## Exact continuation

From the real checkout:

```bash
git pull --ff-only

python -m unittest \
  tests.test_upstream_interval_acquisition_integration \
  tests.test_upstream_interval \
  tests.test_upstream_interval_authority_edges \
  tests.test_upstream_interval_acquisition \
  tests.test_tagged_changelog_acquisition \
  -v

python -m unittest discover -s tests -v
```

The complete-suite count is expected to increase from the observed 310 to **312** because Step 5D adds two tests. This is a derived expectation only; observed terminal output controls validation truth.

If validation fails, diagnose only within the Step 5D integration assumptions unless evidence proves an older regression. Do not change Step 1 authority rules merely to make the integration test pass.

If validation passes:

1. close deterministic Step 5D composition as behavior-validated;
2. perform the remaining **live S001 upstream acquisition proof** using the implemented Step 5A–5C clients against real public source identities;
3. require live acquisition to produce or honestly fail to produce the exact records needed by `assemble_upstream_interval_authority(...)`;
4. close parent-plan Step 5 only after that live proof is observed;
5. do not begin semantic extraction/model integration or CLI orchestration before Step 5 closes.

## Why live S001 proof remains required

The Step 5 plan closes only when UpgradePilot can acquire enough exact public upstream evidence for the selected S001 path from real source identities.

Controlled tests establish deterministic behavior but cannot prove that the real external path currently works:

```text
PyPI soupsieve project release index
+ facelessuser/soupsieve exact proposed tag
+ resolved immutable tag commit
+ exact changelog path/file
→ AuthoritativeUpstreamIntervalEvidence
```

The live proof must not substitute simulation data for network evidence and must preserve any real acquisition failure explicitly.

## Stop line

Until Step 5D deterministic integration validates and the remaining live S001 Step 5 proof is completed, do not begin:

- semantic support-drop extraction/model integration;
- target-Python or CLI acquisition-order changes;
- full S001 end-to-end product execution;
- compatibility, safety, merge, defer, targeted-check, or recommendation logic.

## Explicitly not established

- a passing Step 5D integration test;
- a passing complete suite containing Step 5D;
- live S001 PyPI release-index acquisition;
- live S001 tag-to-commit resolution;
- live S001 exact changelog-file acquisition;
- live S001 `AuthoritativeUpstreamIntervalEvidence`;
- automated semantic extraction/model path;
- conditional target-Python activation in CLI runtime;
- S001 automated end-to-end relevance result;
- compatibility, safety, recommendation, maintainer action, or production readiness;
- user mastery of Steps 1–5D.

## Learning state

Steps 1–5C are behavior-validated at product level. Step 5D integration is implemented but not yet behavior-validated.

Current Step 5 concepts now exposed include:

- **source acquisition versus authority:** obtaining exact records does not itself grant interval authority;
- **composition instead of reinvention:** Step 5 feeds evidence into the Step 1 authority contract rather than creating a second authority implementation;
- **object identity preservation:** the same crossed-release and tagged-changelog records survive into the authoritative bundle;
- **interval identity join:** independently trustworthy records can still be incompatible with each other if they describe different intervals;
- **deterministic proof versus live-source proof:** mocked/controlled tests establish code behavior, while live public acquisition establishes that the selected external evidence path is actually obtainable.

Current depth:

```text
Step 5C behavior validated
+ Step 5D integration design implemented
+ deterministic end-to-end acquisition-to-authority test written
but
Step 5D local execution not yet observed
live S001 upstream acquisition not yet observed
no user-owned Step 5 technical explanation recorded
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
