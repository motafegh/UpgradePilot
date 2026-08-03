# B2 Step 5 — Live S001 Upstream Acquisition Validation

**Date:** 2026-08-03  
**Route:** B2 — Public PR vertical slice  
**Parent:** `plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`  
**Step plan:** `plans/B2_STEP_5_UPSTREAM_INTERVAL_ACQUISITION_PLAN.md`  
**Result:** Step 5 closed; deterministic integration and live S001 acquisition both passed

## Validation boundary

The deterministic Step 5D integration test was added at:

```text
2fff38d86be18d544249f45d7f19e82f9d78f8d6
```

The user reported the complete deterministic suite:

```text
Ran 312 tests in 0.053s

OK
```

No focused-count result is invented. The complete discovery run contains the Step 5D integration cases.

## First live attempt and diagnostic correction

The first live runner execution stopped honestly at Git tag acquisition:

```text
LIVE STEP 5 PROOF: FAIL
stage: Git tag-to-commit resolution
state: acquisition_failed
detail: GitHub returned HTTP 401 while acquiring tag-reference evidence.
```

The runner reads only optional environment variable `GITHUB_TOKEN` for GitHub REST authentication. The user verified that `GITHUB_TOKEN` was set, then removed it from the current shell with:

```bash
unset GITHUB_TOKEN
```

No token value was printed or recorded.

This failure did not reveal a Step 5 product-evidence defect. It demonstrated that an invalid/expired optional credential can cause GitHub to reject a request that otherwise works anonymously against public sources.

## Observed live S001 proof

The user reran:

```bash
python tools/live_s001_upstream_interval_proof.py
```

and reported:

```text
S001 live Step 5 upstream-acquisition proof
dependency interval: soupsieve 2.6 -> 2.8.4

LIVE STEP 5 PROOF: PASS
source identities acquired by UpgradePilot:
  PyPI source: https://pypi.org/pypi/soupsieve/json
  crossed releases: 2.7, 2.8, 2.8.1, 2.8.2, 2.8.3, 2.8.4
  ignored non-PEP-440 release keys: none
  tag ref: refs/tags/2.8.4
  direct tag object: commit 28108ab805818c832d9568142a99844fd95a0d39
  resolved commit: 28108ab805818c832d9568142a99844fd95a0d39
  annotated-tag peel depth: 0
  changelog path: docs/src/markdown/about/changelog.md
  changelog blob SHA: 6f221b7398681a580fa199044b3d3f1e11b55493
  changelog bytes: reported=17370, decoded=17370
  authority basis: tagged_changelog
  GitHub Release bodies admitted: 0

No changelog semantics or target-Python relevance were evaluated.
```

## What is now established

For real public S001 identities, active UpgradePilot code acquired and composed:

```text
PyPI soupsieve project release index
→ exact admitted releases inside 2.6 < release <= 2.8.4
→ CrossedReleaseIndexEvidence

facelessuser/soupsieve
+ refs/tags/2.8.4
→ direct lightweight commit
→ 28108ab805818c832d9568142a99844fd95a0d39

that exact commit
+ docs/src/markdown/about/changelog.md
→ blob 6f221b7398681a580fa199044b3d3f1e11b55493
→ 17,370 reported bytes
→ 17,370 decoded bytes
→ TaggedChangelogEvidence

CrossedReleaseIndexEvidence
+ TaggedChangelogEvidence
→ assemble_upstream_interval_authority(...)
→ AuthoritativeUpstreamIntervalEvidence
   authority_basis = tagged_changelog
```

The tag was lightweight in the observed S001 run (`peel_depth=0`). Controlled Step 5B tests separately validate annotated and nested annotated tag behavior.

## Step 5 closure

Parent Step 5 is **closed and behavior-validated**.

It has both required proof classes:

1. controlled deterministic behavior across acquisition, identity, failure, and authority boundaries;
2. observed live acquisition against the selected S001 public identities.

The live proof does not extract the Python 3.8 support-drop meaning and does not compare target Python declarations. Those responsibilities remain downstream.

## Learning-depth statement

Product behavior is validated. User mastery is not claimed.

Current learning exposure includes source observation versus interpretation, PEP 440 interval selection, Git refs/tag objects/commits, annotated-tag peeling, immutable file/blob identity, byte agreement, provenance timestamps, evidence joins, authority composition, and live-vs-controlled proof.

No user-owned end-to-end Step 5 explanation or formal mastery assessment has been recorded.
