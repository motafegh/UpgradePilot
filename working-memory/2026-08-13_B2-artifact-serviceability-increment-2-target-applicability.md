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

This increment does **not** acquire target-environment evidence yet. Acquisition/interpretation and investigation-selection behavior remain later work.

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

## Permanent regression coverage

Commit `192bde924c32ce6629aa6cd044c8cc77b52437e8` adds permanent Increment-2 regression coverage to `tests/test_artifact_serviceability.py` for:

1. no target compatibility evidence → unresolved;
2. old-compatible / proposed-incompatible target → established applicable;
3. an alternative proposed compatible wheel remains → established not applicable;
4. target never had an old compatible wheel → established not applicable;
5. insufficient target evidence → unresolved;
6. mismatched target repository/revision → rejected.

The retained developer replay remains:

- `tools/verification/2026-08-13_b2_artifact_serviceability_increment2_smoke.py`.

## Fresh user verification — GREEN

After pulling `main` through commit `f4c3ecdcbd738eceed7f50d30acb567a13c78642`, Ali ran the retained and permanent verification in the normal UpgradePilot WSL environment.

Observed results reported by Ali:

```text
retained Increment-2 smoke:
B2 Artifact Serviceability Increment 2 retained smoke: PASS

focused artifact-serviceability suite:
Ran 11 tests in 0.002s
OK

full active suite:
Ran 397 tests in 0.068s
OK
```

These are user-reported local execution results. No additional timing/count is inferred beyond the reported output.

Current proof classification:

```text
Increment 1 post-fix user WSL verification: GREEN
Increment 2 source implementation: PRESENT
Increment 2 permanent focused regression coverage: PRESENT
Increment 2 retained developer verification: GREEN
Increment 2 focused permanent regression: GREEN
Increment 2 full active regression suite: GREEN
Increment 2: VERIFIED COMPLETE AT ITS BOUNDED SCOPE
```

## What remains outside Increment 2

Increment 2 verifies the downstream behavior **given** exact target wheel-compatibility evidence. It does not establish that UpgradePilot can yet acquire or derive that evidence from a real repository.

The next design/implementation responsibility therefore remains:

```text
raw exact target-owned evidence
→ partial, provenance-carrying, environment-specific facts
→ determine whether exact wheel compatibility is justified
→ TargetWheelCompatibilityEvidence OR explicit unresolved/problem
→ existing artifact applicability evaluator
```

Do not synthesize exact target tags from weak metadata, flatten multiple target environments into one repository-wide union, or use local `sys_tags()` as remote-target evidence.
