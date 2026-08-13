# UpgradePilot Current Memory

**Last updated:** 2026-08-13  
**Authority:** Sole repository owner of live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Controlling route plan:** [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md).
- **B2 parent plan:** [`plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md).
- **Selected B2 responsibility:** [`plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md`](plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md).
- **Artifact Increment 2:** [`working-memory/2026-08-13_B2-artifact-serviceability-increment-2-target-applicability.md`](working-memory/2026-08-13_B2-artifact-serviceability-increment-2-target-applicability.md).
- **Evidence-design checkpoint:** [`working-memory/2026-08-13_B2-target-evidence-design-checkpoint.md`](working-memory/2026-08-13_B2-target-evidence-design-checkpoint.md).
- **Main-side simulation review:** [`working-memory/2026-08-13_B2-product-simulation-review-summary.md`](working-memory/2026-08-13_B2-product-simulation-review-summary.md).
- **Adopted target-evidence boundary:** [`working-memory/2026-08-13_B2-target-evidence-boundary-adoption.md`](working-memory/2026-08-13_B2-target-evidence-boundary-adoption.md).
- Product-simulation Cycle 02 evidence through S012 and its target-environment handoff are merged into `main` through `0c57754af3cc3757444f6c7f672e9781bc7a18e9`.

## Current implementation truth

The first Python-support candidate → applicability → discriminating observation → reevaluation loop is implemented and verified green.

Artifact Serviceability Increment 1 compares exact old/proposed PyPI artifact inventories, parses wheel compatibility tags, preserves sdist availability, and creates a target-agnostic artifact candidate when published wheel capabilities disappear.

Increment 2 adds `TargetWheelCompatibilityEvidence`, `TargetWheelCompatibilityProblem`, `ArtifactServiceabilityImpactAssessment`, and `evaluate_artifact_serviceability_impact(...)`. It evaluates complete old/proposed wheel inventories against an **already-established exact target-supported tag set**.

Critical guards:

```text
removed published wheel tag != exact repository loses a compatible wheel
sdist exists != source build succeeds
```

Increment 2 does **not** yet acquire or derive target-environment evidence from a real repository. The next acquisition/interpretation boundary is now adopted, but its source implementation is not yet present.

## Verification truth

Fresh user WSL verification after pulling `main` through `f4c3ecdcbd738eceed7f50d30acb567a13c78642`:

```text
retained Increment-2 smoke: PASS
focused artifact-serviceability suite: 11 tests, OK
full active suite: 397 tests, OK
```

Artifact Serviceability Increment 2 is **VERIFIED COMPLETE AT ITS BOUNDED SCOPE**. This proves evaluator behavior given exact target wheel-compatibility evidence; it does not prove real target-evidence acquisition/interpretation.

No fresh product-test execution is inferred from the later simulation/documentation merge.

## Adopted evidence boundary

The expanded simulation corpus supports this bounded responsibility before `TargetWheelCompatibilityEvidence`:

```text
exact repository + immutable revision
→ one identified environment/job scope
→ proposition-specific repository evidence
→ partial, provenance-carrying environment facts
→ exact wheel compatibility only when genuinely justified
→ otherwise explicit insufficient / unresolved
```

For the first slice, scope is anchored by exact repository, immutable revision, workflow source path, and one statically readable GitHub Actions job.

Literal runner/platform, literal setup-python version, and visible changed-dependency installation evidence may be preserved when available. Platform/CI presence alone does not prove the affected dependency environment is formed. Broad labels must not be converted directly into exact `packaging.tags.Tag` sets.

The current `TargetWheelCompatibilityEvidence` remains the downstream exact contract. No universal environment reconstruction model is accepted.

## Immediate project action

Proceed with a **fixture-first bounded acquisition/interpretation increment** for one statically readable GitHub Actions job.

1. Add focused deterministic workflow examples for:
   - literal runner + literal setup-python + visible changed-dependency installation → partial environment facts with provenance, but no invented exact tags;
   - S011-style platform/Python context without installation of the affected dependency environment → no environment-formation claim, scoped only to that job;
   - partial evidence with a missing/dynamic/unsupported fact → preserve known facts and remain unresolved for exact compatibility;
   - unsupported/ambiguous workflow shape → explicit unresolved/unsupported rather than guessing.
2. Introduce the smallest coherent partial target-environment evidence contract needed by those behaviors. Preserve repository/revision/workflow/job scope, fact provenance, partiality, environment-formation state, and explicit insufficient/problem state.
3. Reuse `RepositoryTextFile` exact-file provenance and the bounded deterministic parsing discipline of `ci/workflow_commands.py`. Do not blindly reuse its current `installed + directly invoked` final predicate; artifact serviceability needs environment formation, not necessarily runtime invocation.
4. Compose to `TargetWheelCompatibilityEvidence` only when exact tags are genuinely established. The first slice may stop with useful partial evidence plus unresolved exact compatibility.
5. Run focused, nearest, and full regression verification, then transfer-test the concrete slice against S008, S011, Buildtest/C203, S006, S007, and S001.
6. Admit S013 only if the concrete implementation exposes a behavior those existing anchors cannot discriminate.

The current tests use inline workflow examples rather than a dedicated fixture framework. Do not add generic fixture infrastructure unless actual reuse pressure earns it.

## Continuation-critical guards

- candidate formulation does not manufacture applicability;
- missing evidence is not negative evidence;
- package evidence and repository-environment evidence remain separate;
- exact repository/revision provenance and workflow/job scope must be preserved;
- UpgradePilot's own environment is not evidence for another repository environment;
- broad environment labels must not become exact wheel tags;
- CI/platform presence must not imply affected dependency-environment formation;
- multi-environment evidence must not be flattened into one repository-wide union;
- apparent disagreement must be scoped before it is classified as conflict;
- wheel loss, source fallback availability, and source-build success remain separate;
- do not introduce universal planners, registries, environment reconstructors, generic provenance graphs, plugin systems, or similar infrastructure without demonstrated need.

## Learning state

Current demonstrated depth remains **substantial guided implementation exposure with repeated evidence-driven reasoning/debugging; no formal mastery assessment**.

Current learning emphasis is the fixture-first target-environment acquisition increment: preserve exact evidence identity and partial facts, distinguish environment formation from broad CI presence, maintain unresolved states honestly, and connect repository evidence to exact wheel compatibility only when justified.
