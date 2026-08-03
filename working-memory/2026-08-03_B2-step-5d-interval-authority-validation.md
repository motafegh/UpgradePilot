# B2 Step 5D — Interval Authority Integration Validation

**Date:** 2026-08-03  
**Route:** B2 — Public PR vertical slice  
**Scope:** deterministic Step 5D integration validation only  
**Live-state owner:** `MEMORY.md`

## Observed validation

The user reported the complete deterministic suite from the real checkout:

```text
Ran 312 tests in 0.053s

OK
```

The exact focused Step 5D command summary was not supplied and is not invented.

The complete discovery run includes the two Step 5D integration cases in:

```text
tests/test_upstream_interval_acquisition_integration.py
```

The Step 5D executable change remains test-only at:

```text
2fff38d86be18d544249f45d7f19e82f9d78f8d6
```

## What this validates

The deterministic chain is behavior-validated:

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

The S001-shaped minimum path establishes:

```text
complete crossed-release index
+ exact proposed-tag changelog
+ zero GitHub Release bodies
→ authority_basis = tagged_changelog
```

The integration also preserves interval identity: individually valid records from different intervals produce `identity_mismatch` rather than one combined authority record.

## What this does not validate

This run does not establish:

- live PyPI acquisition for Soup Sieve;
- live GitHub tag-to-commit resolution for `facelessuser/soupsieve`;
- live exact changelog-file acquisition;
- live S001 `AuthoritativeUpstreamIntervalEvidence`;
- semantic support-drop extraction;
- target-Python orchestration;
- CLI integration;
- compatibility, safety, recommendation, or maintainer action;
- user mastery.

The remaining Step 5 proof obligation is therefore live public-source acquisition through the implemented clients, not another deterministic authority implementation.
