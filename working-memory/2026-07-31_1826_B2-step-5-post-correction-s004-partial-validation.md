# B2 Step 5 — Post-correction S004 partial validation

**Recorded:** 2026-07-31 18:26 +03:30  
**Route:** B2 — Public PR vertical slice  
**Step:** 5 — `uv.lock` dependency-change extraction  
**Status:** Partial validation only; Step 5 remains open

## Purpose

Record the installed S004 regression run supplied after the Step 5 correction for valid versionless editable/virtual workspace records.

The correction modified only the source-specific `uv.lock` parser and its tests. This run checks that the already validated installed exact-requirements path remains behaviorally intact after that correction.

## Supplied command

```bash
unset GITHUB_TOKEN
upgradepilot googlefonts/glyphsLib 1145
```

## Observed result

The installed command completed successfully and preserved the existing S004 evidence chain:

```text
Repository: googlefonts/glyphsLib
PR: 1145
requirements-dev.txt
pytest 9.0.2 → 9.0.3
Target Python declaration: project_table_absent
Exact-head workflow runs: 2
CI authority: sufficient
CI authority reason: exact_head_dependency_exercised
Published package: pytest==9.0.3
Upstream repository: pytest-dev/pytest
Provenance coverage: 2 of 2 files
Accepted tag: 9.0.3
Claim state: unresolved_claim
```

## What this proves

- The post-correction installed package still imports and executes.
- The legacy exact-requirements extraction path remains intact.
- Existing target-Python, exact-head workflow, CI-authority, PyPI, provenance, and upstream-release behavior remains intact for S004.
- The Step 5 versionless-workspace correction did not alter the visible S004 output boundary.

## What this does not prove

This run does not validate the corrected `uv.lock` parser itself. Step 5 still requires:

```text
24 focused Step 5 tests passing
125 complete tests passing
corrected live S001 extraction establishing soupsieve 2.6 → 2.8.4
```

The supplied transcript did not include:

```text
git rev-parse HEAD
git status --short
python --version
```

Therefore this record does not independently establish the exact local commit, clean working tree, or interpreter version used for the run.

## Continuation

Do not repeat S004 again for this correction unless later source changes touch the legacy runtime path or another regression appears.

Remain in Step 5 and next run:

```bash
python -m unittest \
  tests.test_uv_lock_change \
  tests.test_uv_lock_versionless_records \
  -v

python -m unittest discover -s tests -v
```

Then rerun the corrected live S001 extraction.
