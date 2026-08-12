# B2 Artifact Serviceability — Increment 1

**Date:** 2026-08-12  
**Type:** Dated implementation working memory  
**Live-state authority:** `../MEMORY.md` only  
**Entry checkpoint:** `2026-08-12_B2-transfer-checkpoint-second-mechanism-entry.md`

## Scope

Implement only the first small step of the second materially different technical mechanism:

```text
exact dependency transition
+ exact old PyPI release inventory
+ exact proposed PyPI release inventory
→ target-agnostic published artifact-transition candidate
```

This increment intentionally does **not** establish exact target artifact compatibility, source-build success, CI coverage of an artifact branch, or a maintainer action.

## Source/test changes

- `b25529c74c3025666fae74f36eac95611d72a99d` — added `tests/test_artifact_serviceability.py`;
- `c6d1c4bde7b9d972ba86927269e0e6071f16f1ed` — added `src/upgradepilot/impact/artifact_serviceability.py`.

## Implemented contract

`build_artifact_serviceability_impact_candidate(...)` consumes:

- exact `PullRequestIdentity`;
- exact `DependencyVersionChange`;
- exact old `PackageReleaseEvidence`;
- exact proposed `PackageReleaseEvidence`.

It validates that the two package-release records match the dependency package and exact old/proposed versions.

For each published `bdist_wheel` file it uses `packaging.utils.parse_wheel_filename()` to preserve the exact wheel compatibility tags encoded by the filename.

The candidate preserves:

- exact pull-request/target identity;
- exact dependency transition;
- exact old/proposed release evidence;
- parsed old/proposed published wheels;
- removed and added published wheel-tag sets;
- old/proposed source-distribution presence;
- mechanism established / target exposure to evaluate / consequence possible states;
- a target-exposure proposition without self-authorizing it;
- a bounded possible installation-path consequence.

## Semantics

The central boundary is:

```text
old published tag set - proposed published tag set
→ removed published wheel tags

removed published wheel tags
!= target loses a compatible wheel
```

The first statement is package-release evidence interpretation.

The second requires exact target environment compatibility evidence and is deliberately deferred to Increment 2.

Likewise:

```text
proposed sdist exists
!= source fallback succeeds
```

The candidate may state that source-distribution fallback is published, but it does not claim that a native/source installation will succeed in any exact target environment.

## No-candidate and evidence-problem behavior

If no old published wheel compatibility tag disappears, the bounded builder returns `None` rather than manufacturing an artifact-loss candidate.

If a PyPI record is labeled as a wheel but its filename cannot be interpreted by the admitted packaging method, the implementation returns `ArtifactServiceabilityEvidenceProblem(state="wheel_filename_uninterpretable")` rather than treating the external evidence problem as a negative compatibility conclusion.

A parsed wheel whose package/version identity conflicts with the exact release record is preserved as a distinct wheel-identity evidence problem.

Supplying old/proposed release evidence for the wrong dependency transition is a caller/contract error and raises `ValueError`, matching the exact-identity discipline used elsewhere in the active product.

## Focused test intent

The new tests cover:

1. a generic old CPython-3.6 manylinux wheel tag disappearing while the proposed release publishes different wheel tags plus an sdist;
2. unchanged published wheel tags producing no candidate;
3. malformed wheel filename producing an evidence problem;
4. exact release/dependency transition identity mismatch rejection.

The test data uses the generic package name `demo`; it does not hardcode CARLA/OpenCV or the S008 answer.

## Learning point

A wheel compatibility tag is a triple:

```text
interpreter
+
ABI (Application Binary Interface)
+
platform
```

A wheel filename may encode compressed tag components. `parse_wheel_filename()` expands those into exact `Tag` values, so UpgradePilot does not hand-parse this packaging standard.

The project dependency `packaging>=26.2,<27` supports the parsing method used here.

## Current proof status

```text
source implementation: PRESENT
focused tests: PRESENT
GitHub static consistency review: PASSED
fresh executable test run in normal UpgradePilot environment: PENDING
```

Do not advance into target-environment applicability until this increment is freshly executed and any failure is diagnosed.

## Next after green verification

Increment 2 should answer:

> What exact admitted target-environment evidence is sufficient to determine whether that target had a compatible old wheel and lacks a compatible proposed wheel?

Constraints:

- do not use UpgradePilot's local `sys_tags()` as a proxy for a remote target;
- do not collapse interpreter metadata, wheel availability, sdist availability, and source-build success;
- reuse generic proposition/path applicability composition only where the semantics fit;
- keep target evidence acquisition separate from package artifact inventory evidence.
