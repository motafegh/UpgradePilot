# B2 Target-Python Step 7A — Exact-Commit Changelog Discovery Implementation

**Date:** 2026-08-03  
**Parent:** `plans/B2_TARGET_PYTHON_STEP_7_BOUNDED_EXTRACTOR_RUNTIME_INTEGRATION_PLAN.md`  
**Status at this record:** implemented; deterministic and live validation pending

## Why this increment exists

Step 5 behavior-validly proved exact changelog acquisition when the path is already supplied, and S001 used:

```text
docs/src/markdown/about/changelog.md
```

That path was intentionally scenario-specific proof input. Normal product runtime cannot hardcode it.

Step 7A therefore adds one bounded source-location rule before semantic extraction:

```text
trusted upstream repository
+ exact proposed-tag commit SHA
→ exact commit object
→ exact root tree
→ complete recursive tree
→ admitted Markdown changelog basename filter
→ exactly one changelog path or explicit problem
```

No model or changelog prose interpretation is involved.

## New product module

```text
src/upgradepilot/upstream_changelog.py
```

Public contracts:

```text
ADMITTED_CHANGELOG_BASENAMES
DiscoveredChangelogPath
ChangelogPathDiscoveryProblemState
ChangelogPathDiscoveryProblem
ChangelogPathDiscoveryResult
GitHubChangelogPathClient
```

Initial admitted basenames:

```text
changelog.md
changes.md
history.md
release-notes.md
```

Matching is case-insensitive on basename; directory location is unconstrained.

The discovery method does not rank multiple candidates. Several admitted paths become `multiple_candidate_paths`.

## Exact identity and completeness checks

The client performs two exact GitHub reads:

```text
GET /repos/{repository}/git/commits/{commit_sha}
→ returned commit SHA must equal requested exact SHA
→ preserve root tree SHA

GET /repos/{repository}/git/trees/{tree_sha}?recursive=1
→ returned tree SHA must equal commit root tree SHA
→ truncated must be false
→ inspect regular blob paths only
```

A truncated recursive tree cannot prove absence or uniqueness, so it returns:

```text
recursive_tree_truncated
```

Malformed tree items are not silently ignored because doing so could create a false uniqueness conclusion.

## Problem states

```text
source_unavailable
malformed_response
identity_mismatch
recursive_tree_truncated
no_candidate_path
multiple_candidate_paths
acquisition_failed
```

Invalid mutable locators such as `main` are rejected before network access; the discovery input must be a 40- or 64-character hexadecimal object ID.

## Controlled tests

Added:

```text
tests/test_upstream_changelog.py
```

The tests cover:

- S001-shaped nested path discovery without a directory constant;
- case-insensitive admitted basename matching;
- non-blob exclusion;
- no candidate;
- multiple candidates and no ranking;
- truncated tree rejection;
- exact commit identity mismatch;
- exact tree identity mismatch;
- malformed `truncated` field;
- malformed tree item;
- missing source;
- transport timeout;
- mutable/invalid commit locator rejection before HTTP.

Package-interface regression was also extended so the discovery contracts are intentionally public.

## Live S001 proof tool

Added:

```text
tools/live_s001_changelog_discovery_proof.py
```

This is scenario-specific validation tooling, not product logic. It supplies the already behavior-validated S001 repository and exact proposed-tag commit:

```text
facelessuser/soupsieve
28108ab805818c832d9568142a99844fd95a0d39
```

and verifies that the generic product discovery method reaches the historical oracle path:

```text
docs/src/markdown/about/changelog.md
```

The live tool intentionally performs anonymous public GitHub reads so the stale-`GITHUB_TOKEN` failure seen during Step 5 cannot contaminate this source-discovery proof.

## Implementation mistake caught before validation

While wiring the new package exports, the first `__init__.py` edit accidentally placed:

```text
DependencyCIExerciseResult
DependencyCIExerciseState
```

inside the `dependency_change` import block as well as their correct `ci_dependency_exercise` import block.

This would have caused package import failure even though the new discovery module itself was valid.

The mistake was identified immediately from static review and corrected before the user validation gate. A package-interface regression now protects the intended public exports.

This is a useful reminder that integration wiring can fail independently of the newly implemented domain behavior.

## Current implementation boundary

The Step 7A source/tests/package API/live-proof candidate boundary is represented by the repository through:

```text
d3738cc4408f7eb65df2a6ff7f5d56b94ee42446
```

Later documentation/live-state commits do not change the executable 7A behavior.

## Validation required

From WSL:

```bash
python -m unittest \
  tests.test_upstream_changelog \
  tests.test_package_interface \
  -v

python -m unittest discover -s tests -v

python tools/live_s001_changelog_discovery_proof.py
```

No LM Studio call is needed for Step 7A.

## Stop line

Do not implement Step 7B source-windowing or the normal-runtime model adapter until this exact-commit discovery boundary passes focused tests, the complete deterministic suite, and the live S001 proof.
