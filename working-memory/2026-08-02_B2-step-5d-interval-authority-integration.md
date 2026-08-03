# B2 Step 5D — Interval Authority Integration Evidence

**Date:** 2026-08-02  
**Route:** B2 — Public PR vertical slice  
**Parent plan:** `plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`  
**Step plan:** `plans/B2_STEP_5_UPSTREAM_INTERVAL_ACQUISITION_PLAN.md`  
**Evidence role:** Historical implementation/integration record only. `MEMORY.md` remains the sole owner of live project position.

## Why Step 5D adds no production wrapper

Step 1 already owns the authoritative interval composition rule through:

```text
assemble_upstream_interval_authority(...)
```

Steps 5A–5C earn the exact inputs that function requires. Adding another production function that merely forwards those records would duplicate ownership and create a second name for the same authority transition.

Step 5D is therefore implemented as an integration proof rather than a new authority layer.

## Added controlled integration test

Created:

```text
tests/test_upstream_interval_acquisition_integration.py
```

The test executes the deterministic chain:

```text
PackageReleaseIndexEvidence
→ select_crossed_release_index(...)
→ SelectedCrossedReleaseIndex.evidence

GitHubTagCommitEvidence
+ ExactRepositoryTextFile
→ build_tagged_changelog_evidence(...)
→ TaggedChangelogEvidence

CrossedReleaseIndexEvidence
+ TaggedChangelogEvidence
→ assemble_upstream_interval_authority(...)
→ AuthoritativeUpstreamIntervalEvidence
```

No network requests are made by this test.

## Proof obligations encoded

### Minimum S001-shaped authority path

The controlled case uses a Soup Sieve-shaped interval:

```text
2.6 < release <= 2.8.4
```

and proves:

```text
complete admitted crossed-release index
+ exact proposed-tag changelog
+ zero GitHub Release bodies
→ authority_basis = tagged_changelog
```

The expected ordered releases are:

```text
2.7
2.8
2.8.1
2.8.2
2.8.3
2.8.4
```

The test also checks that the Step 1 result preserves the exact crossed-release and tagged-changelog objects rather than replacing them with copied approximations.

### Cross-interval contradiction

A second controlled case creates individually valid crossed-release and changelog evidence for different proposed-version intervals and proves the Step 1 assembler returns:

```text
identity_mismatch
```

This prevents Step 5D from erasing interval identity merely because both records are structurally valid.

## Source/test boundary

The Step 5D executable change is test-only and ends at:

```text
2fff38d86be18d544249f45d7f19e82f9d78f8d6
```

No production source, CLI, model, target-Python, semantic extraction, or recommendation code changed for Step 5D.

## Validation status

Local execution has not yet been observed for the new integration test. No pass is claimed.

After the Step 5D integration and complete deterministic suite pass, the remaining Step 5 proof obligation is **live S001 upstream acquisition from real public source identities**. Deterministic integration alone does not prove that the real Soup Sieve release index, version tag, immutable changelog path, and GitHub responses are currently obtainable through the implemented clients.
