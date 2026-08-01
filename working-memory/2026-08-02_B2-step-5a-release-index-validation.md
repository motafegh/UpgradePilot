# B2 Step 5A — Release Index Validation

**Date:** 2026-08-02  
**Responsibility:** Record observed local behavior validation for Step 5A only  
**Live-state owner:** [`../MEMORY.md`](../MEMORY.md)

## Validated boundary

Step 5A introduced the bounded path:

```text
PyPI package project response
→ PackageReleaseIndexEvidence
→ select_crossed_release_index(...)
→ SelectedCrossedReleaseIndex
   └── CrossedReleaseIndexEvidence
```

The executable Step 5A source/test boundary was:

```text
4ad56dabf6613f7ad46b096bcda7198ac1baff25
```

Later working-memory and `MEMORY.md` commits did not alter that product/test boundary before validation.

## Observed local result

The user reported running the requested Step 5A validation from the real project checkout on `main` and observed the complete deterministic suite:

```text
Ran 281 tests in 0.066s

OK
```

The exact focused-suite summary was not supplied and is not invented. The complete discovery run contains the Step 5A release-index acquisition/selection tests and package-interface coverage, so another focused rerun is not required solely to establish the same executable behavior.

## Established behavior

At the validated boundary, UpgradePilot behavior-validly provides:

- bounded PyPI project release-index acquisition;
- exact requested/normalized/published package identity preservation;
- exact raw release-key preservation without assigning source-side semantic order;
- explicit package-missing, identity-mismatch, malformed-response, and acquisition-failure results;
- PEP 440 old-exclusive/proposed-inclusive release selection;
- exact raw proposed-version presence enforcement;
- rejection of PEP 440-equivalent selected release identities;
- deterministic `CrossedReleaseIndexEvidence` ordering;
- explicit preservation of non-PEP-440 registry keys as ignored/out-of-scope source evidence.

## What this validation does not establish

It does not establish:

- live S001 PyPI acquisition;
- Git tag resolution or annotated-tag peeling;
- exact changelog-file acquisition;
- Step 1 authority composition from live upstream evidence;
- semantic support-drop extraction;
- target comparison, CLI integration, compatibility, safety, or recommendation behavior.

## Continuation

Step 5A is behavior-validated and closed. The next bounded increment is Step 5B: resolve one explicitly supplied accepted Git version tag to an immutable commit, including bounded annotated-tag peeling, before changelog-file acquisition begins.
