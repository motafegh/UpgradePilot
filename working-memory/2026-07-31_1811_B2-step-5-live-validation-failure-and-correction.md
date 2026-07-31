# B2 Step 5 — Live Validation Failure and Correction

**Date:** 2026-07-31 18:11 +03:30  
**Step:** 5 — extract `uv.lock` changes  
**Status:** correction implemented; behavior validation still pending

## Validation evidence supplied

The installed anonymous S004 regression control was run:

```bash
unset GITHUB_TOKEN
upgradepilot googlefonts/glyphsLib 1145
```

Its existing behavior was preserved, including:

```text
requirements-dev.txt
pytest 9.0.2 → 9.0.3
project_table_absent
exact-head CI authority sufficient
pytest==9.0.3
2 of 2 provenance
pytest-dev/pytest release tag 9.0.3
unresolved_claim
```

This establishes installed S004 compatibility for the supplied run. It does not validate the new `uv.lock` parser.

The live S001 extraction was then run against:

```text
pydantic/pydantic #13432
uv.lock
```

Observed result:

```text
DependencyChangeEvidenceProblem
reason: invalid_dependency_record
detail: The exact base uv.lock package record at index 104 had an invalid non-empty textual 'version'.
```

## Root cause

Record index 104 is a valid local workspace record:

```toml
[[package]]
name = "pydantic"
source = { editable = "." }
```

Its version is omitted intentionally because the workspace project uses an editable local source and may have a dynamic version. A second editable workspace record for `pydantic-core` has the same shape.

The first Step 5 implementation incorrectly required every package table to contain a non-empty textual `version`. That requirement was too broad for valid uv schema-v1 workspace records.

## Corrected boundary

The parser now distinguishes version-bearing dependency records from versionless workspace context:

```text
missing version + exactly one editable/virtual textual local source
→ admitted versionless workspace record

missing version + registry, missing, malformed, or unknown source
→ invalid_dependency_record
```

An admitted versionless record:

- participates in normalized-name grouping;
- participates in exact structural comparison after removing only top-level `sdist` and `wheels`;
- may coexist unchanged with one unambiguous version-bearing dependency transition;
- cannot itself produce `ExtractedDependencyVersionChange`;
- produces `unsupported_uv_lock_structural_change` if it changes non-artifact structure;
- produces `unsupported_uv_lock_structural_change` if it gains or loses a textual version.

This correction is generic. It contains no S001 repository, package, index, version, SHA, or expected-answer condition.

## Correction commits

```text
bf9fb555a328240399601839ddcd815966bace29
Handle versionless uv workspace records

82237ee4b11b1df7182a58cf5913194d8b231eac
Test versionless uv workspace records
```

New focused regression file:

```text
tests/test_uv_lock_versionless_records.py
```

It adds five cases:

1. unchanged editable record does not block another clear transition;
2. unchanged virtual record does not block another clear transition;
3. changed versionless record stops as unsupported structure;
4. missing version with a registry source remains invalid;
5. gaining or losing a version stops as unsupported structure.

An isolated Python 3.13.5 harness passed all five new cases and compatibility scenarios for the prior Step 5 rules. This is development evidence only, not repository behavior validation.

## Required rerun

Focused Step 5 tests now total:

```text
24 tests
```

The complete deterministic suite is expected to total:

```text
125 tests
```

Required validation remains:

1. real checkout identity and Python version;
2. 24 focused Step 5 tests;
3. 125-test complete suite;
4. installed anonymous S004 control;
5. live S001 extraction establishing only:

```text
soupsieve 2.6 → 2.8.4
```

Step 5 must remain open and Step 6 must not begin until that evidence is supplied and reviewed.

## Learning-state note

The failure exposed an important structured-data distinction:

```text
field absent
≠ automatically malformed
```

Validity depends on the record variant and source context. The parser now models this as a narrow discriminated record shape rather than making `version` optional for every package record.

This explanation and correction do not establish independent implementation ability or mastery.
