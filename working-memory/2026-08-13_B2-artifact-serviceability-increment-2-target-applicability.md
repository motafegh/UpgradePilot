# B2 Artifact Serviceability — Increment 2 Target Applicability

**Date:** 2026-08-13  
**Type:** Dated implementation working memory  
**Live-state authority:** `../MEMORY.md` only

## Entry state

Artifact Serviceability Increment 1 was freshly rerun by the user after the compressed-wheel parsing correction. The focused artifact tests, nearest package/PyPI regressions, and full active suite were reported green. Increment 1 is therefore verified complete.

## Increment 2 scope

Implement only the next bounded reasoning step:

```text
artifact-serviceability candidate
+ exact target-supported wheel-tag evidence
→ evaluate whether the target had an old compatible published wheel
→ evaluate whether the proposed release still has any compatible published wheel
→ compose bounded candidate applicability
```

This increment does **not** acquire target-environment evidence yet. Acquisition/interpretation and investigation-selection behavior remain the next increment.

## Source change

Commit `a37edf3b8941d085427c276a68496da2b3282555` extends:

- `src/upgradepilot/impact/artifact_serviceability.py`

with:

- `TargetWheelCompatibilityEvidence`;
- `TargetWheelCompatibilityProblem`;
- `ArtifactServiceabilityImpactAssessment`;
- `evaluate_artifact_serviceability_impact(...)`.

## Evidence boundary

The target compatibility contract intentionally starts after target evidence has been acquired and interpreted. It must not be populated from UpgradePilot's own `packaging.tags.sys_tags()` and must not guess exact wheel tags from broad facts such as only `Python 3.6 + Linux`.

The evaluator validates exact target repository/revision identity before using target evidence.

## Applicability semantics

One bounded path is represented:

1. published wheel transition established;
2. exact target wheel compatibility established;
3. target had at least one compatible old published wheel;
4. target has no compatible proposed-release published wheel.

The generic proposition/path/candidate applicability composer is reused.

A key correction to naive reasoning is that target applicability is **not** calculated from `removed_wheel_tags` alone. Instead:

```text
old published tags ∩ target-supported tags
```

and

```text
proposed published tags ∩ target-supported tags
```

are evaluated separately.

This matters because one exact old tag can disappear while a different proposed tag still serves the same target environment.

## Educational comments

Comments were added only around non-obvious boundaries:

- why target tags must not be derived from the analyzer's own environment;
- why compatibility is a set intersection rather than independent string guesses;
- why the full proposed wheel inventory must be checked instead of only removed tags.

## Verification status

A connector-side safety classifier repeatedly blocked writes to `tests/test_artifact_serviceability.py`, including a harmless comment-only replacement. Therefore focused executable coverage for the new evaluator could not be committed in this turn.

A disposable local clone was also unavailable because that runtime had no network access.

Current proof classification:

```text
Increment 1 post-fix user WSL verification: GREEN
Increment 2 source implementation: PRESENT
Increment 2 static connector review: PASSED
Increment 2 committed focused tests: BLOCKED BY CONNECTOR WRITE RESTRICTION
Increment 2 fresh executable proof: PENDING
```

Do not classify Increment 2 complete until its new applicability behavior is executed in the normal UpgradePilot WSL environment and permanent regression coverage is present.

## Required behavior to verify

1. no target compatibility evidence → candidate remains unresolved;
2. target supports an old wheel tag and no proposed wheel tag → established applicable;
3. target supports old and a different proposed wheel tag → bounded candidate established not applicable;
4. target supports no old wheel tag → bounded candidate established not applicable;
5. target compatibility evidence problem → unresolved;
6. mismatched target repository/revision → rejected.

## Next after verification

Proceed to target artifact-environment evidence acquisition/interpretation and discriminating investigation/stop behavior. Do not synthesize exact target tags from weak metadata and do not use local `sys_tags()` as remote-target evidence.
