# B2 Step 5 — Live S001 Upstream Acquisition Proof Runner

**Date:** 2026-08-03  
**Route:** B2 — Public PR vertical slice  
**Scope:** live Step 5 closure proof harness  
**Live-state owner:** `MEMORY.md`

## Why this runner exists

Steps 5A–5D are now deterministically behavior-validated, but the selected Step 5 plan closes only after the implemented acquisition path is observed against the real public S001 source identities.

A scenario-specific runner was added at:

```text
tools/live_s001_upstream_interval_proof.py
```

This file is validation tooling, not production orchestration. S001 constants remain outside `src/upgradepilot/` so fixture-specific package/version/path choices do not leak into generalized product logic.

## Live path exercised

```text
PyPI soupsieve project JSON
→ PyPIReleaseIndexClient
→ select_crossed_release_index(...)
→ CrossedReleaseIndexEvidence

facelessuser/soupsieve + exact tag 2.8.4
→ GitHubTagCommitClient.resolve_tag_to_commit(...)
→ immutable commit SHA

immutable commit SHA
+ docs/src/markdown/about/changelog.md
→ GitHubRepositoryClient.get_exact_commit_text_file(...)
→ ExactRepositoryTextFile
→ build_tagged_changelog_evidence(...)
→ TaggedChangelogEvidence

crossed releases + tagged changelog
→ assemble_upstream_interval_authority(...)
→ AuthoritativeUpstreamIntervalEvidence
```

The runner performs no changelog semantic extraction, no target-Python comparison, no CLI orchestration, and no recommendation.

## Expected bounded success shape

For the selected S001 identities, a successful live proof should report:

```text
crossed releases:
2.7, 2.8, 2.8.1, 2.8.2, 2.8.3, 2.8.4

authority basis:
tagged_changelog

GitHub Release bodies admitted:
0
```

The exact Git tag object type/SHA, resolved commit SHA, changelog blob SHA, byte counts, and retrieval evidence must come from the live clients rather than being asserted by this record.

## External preflight corroboration

Before adding the runner, separate official-source inspection showed:

- PyPI currently lists Soup Sieve releases `2.6`, `2.7`, `2.8`, `2.8.1`, `2.8.2`, `2.8.3`, and `2.8.4`;
- PyPI provenance for 2.8.4 identifies `facelessuser/soupsieve` and `refs/tags/2.8.4`;
- the provenance commit shown by PyPI is `28108ab805818c832d9568142a99844fd95a0d39`;
- the exact repository path `docs/src/markdown/about/changelog.md` exists at that commit and contains the 2.8-series changelog.

This corroboration does **not** substitute for running UpgradePilot's own clients.

## Execution

From the real checkout:

```bash
git pull --ff-only
python tools/live_s001_upstream_interval_proof.py
```

An optional `GITHUB_TOKEN` may be present in the environment to increase GitHub API rate limits. The runner remains read-only.

## Honesty boundary

Until the user reports the actual runner output, do not claim:

- that UpgradePilot acquired the real PyPI release index;
- that its tag client resolved the live tag;
- that its repository client acquired the live changelog;
- that live S001 interval authority was established;
- that parent Step 5 is closed.
