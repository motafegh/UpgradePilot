# B2 Source-Structure Reconciliation — Pre-Migration Baseline

**Date:** 2026-08-04  
**Purpose:** Preserve the last user-observed behavior baseline before responsibility-based source migration begins.

## Baseline state

The source-structure reconciliation was selected after the flat `src/upgradepilot/` package accumulated demonstrated GitHub, PyPI, dependency, CI, upstream, target, and application boundaries.

Before the first structural source edits, Ali synchronized the repository and reported the complete deterministic suite:

```text
Ran 353 tests in 0.077s

OK
```

This is the pre-refactor deterministic comparison point.

## Live Step 7A regression baseline

Ali then ran:

```text
python tools/live_s001_changelog_discovery_proof.py
```

Observed output:

```text
S001 live Step 7A changelog-path discovery proof
repository: facelessuser/soupsieve
exact commit: 28108ab805818c832d9568142a99844fd95a0d39

Discovered exact-commit changelog evidence:
  tree SHA: 183f563a271635247327f1f0b1dddb158e0add39
  path: docs/src/markdown/about/changelog.md
  admitted candidate count: 1

LIVE STEP 7A PROOF: PASS
The generic exact-commit discovery rule recovered the historical S001 changelog path without a product path constant.
```

This establishes the behavior that must survive the later move of GitHub-specific changelog discovery into the GitHub provider package.

## Architectural admission

After this baseline, ADR-0007 accepted responsibility-based Python subpackages while preserving the `src/upgradepilot/` distribution boundary and prohibiting speculative empty layers.

## First structural batch started after the baseline

The first code batch creates genuinely shared source-neutral primitives:

```text
src/upgradepilot/package_identity.py
src/upgradepilot/repository_path.py
```

and begins redirecting existing dependency code to them.

No Step 7B/model-runtime/target-activation capability is part of this batch.

## Diagnostic use

If a later migration produces a regression, compare against this baseline before changing product behavior. A structural defect must be fixed as a structural defect; it must not be hidden by weakening evidence, authority, extraction, or abstention contracts.
