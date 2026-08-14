# UpgradePilot Current Memory

**Last updated:** 2026-08-14  
**Authority:** Sole repository owner of live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Controlling route plan:** [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md).
- **B2 parent plan:** [`plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md).
- **Selected B2 responsibility:** [`plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md`](plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md).
- **Artifact Increment 2:** [`working-memory/2026-08-13_B2-artifact-serviceability-increment-2-target-applicability.md`](working-memory/2026-08-13_B2-artifact-serviceability-increment-2-target-applicability.md).
- **Adopted target-evidence boundary:** [`working-memory/2026-08-13_B2-target-evidence-boundary-adoption.md`](working-memory/2026-08-13_B2-target-evidence-boundary-adoption.md).
- **Target Artifact Environment Increment 1:** [`working-memory/2026-08-14_B2-target-artifact-environment-increment-1-implementation.md`](working-memory/2026-08-14_B2-target-artifact-environment-increment-1-implementation.md).
- Product-simulation Cycle 02 evidence through S012 and its target-environment handoff are merged into `main` through `0c57754af3cc3757444f6c7f672e9781bc7a18e9`.

## Current implementation truth

The first Python-support candidate → applicability → discriminating observation → reevaluation loop is implemented and verified green.

Artifact Serviceability Increment 1 compares exact old/proposed PyPI artifact inventories, parses wheel compatibility tags, preserves sdist availability, and creates a target-agnostic artifact candidate when published wheel capabilities disappear.

Artifact Serviceability Increment 2 adds `TargetWheelCompatibilityEvidence`, `TargetWheelCompatibilityProblem`, `ArtifactServiceabilityImpactAssessment`, and `evaluate_artifact_serviceability_impact(...)`. It evaluates complete old/proposed wheel inventories against an **already-established exact target-supported tag set**.

Critical guards remain:

```text
removed published wheel tag != exact repository loses a compatible wheel
sdist exists != source build succeeds
```

Target Artifact Environment Increment 1 is now implemented in `src/upgradepilot/target/artifact_environment.py`. It interprets one statically readable GitHub Actions job from strongly provenanced `RepositoryTextFile` evidence and preserves:

- exact repository/revision/workflow/blob/job scope;
- literal runner when available;
- literal `actions/setup-python` `with.python-version` when available;
- direct visible changed-dependency source installation;
- explicit limitations for missing/dynamic facts;
- explicit unsupported/problem state for admitted ambiguous shapes such as multiple or matrix jobs.

Its environment-formation result is evidence-shaped: `established` or `not_observed`. `not_observed` does not establish absence.

The increment deliberately leaves `exact_wheel_compatibility_state="unresolved"`. It does **not** yet derive exact `packaging.tags.Tag` sets or produce `TargetWheelCompatibilityEvidence`.

## Verification truth

Fresh user WSL verification for Artifact Serviceability Increment 2 after pulling `main` through `f4c3ecdcbd738eceed7f50d30acb567a13c78642` remains:

```text
retained Increment-2 smoke: PASS
focused artifact-serviceability suite: 11 tests, OK
full active suite: 397 tests, OK
```

Artifact Serviceability Increment 2 remains **VERIFIED COMPLETE AT ITS BOUNDED SCOPE**. This proves evaluator behavior given exact target wheel-compatibility evidence; it does not prove real target-evidence acquisition/interpretation.

For Target Artifact Environment Increment 1:

```text
source implementation: PRESENT
permanent focused regression coverage: PRESENT (6 focused behaviors)
assistant reconstructed focused smoke: GREEN (6 tests, OK)
real repository focused suite: NOT YET RUN/RECORDED
nearest regression suite: NOT YET RUN/RECORDED
full active suite: NOT YET RUN/RECORDED
```

GitHub exposes no configured commit status checks for the implementation commit, so no remote CI proof is inferred.

Therefore Target Artifact Environment Increment 1 is **IMPLEMENTED, VERIFICATION PENDING** rather than verified complete.

## Adopted evidence boundary

The supported responsibility before `TargetWheelCompatibilityEvidence` remains:

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

First close the real-repository verification gap for Target Artifact Environment Increment 1 in the normal UpgradePilot WSL environment.

Minimum verification:

```text
python -m unittest discover -s tests -p 'test_target_artifact_environment.py' -v
python -m unittest discover -s tests
```

If the repository's normal nearest-regression convention identifies additional target/CI/artifact tests, run them before declaring the increment verified complete.

After green verification:

1. transfer-check the concrete slice against S008, S011, Buildtest/C203, S006, S007, and S001;
2. confirm that `not_observed`, partial facts, and unsupported shapes preserve the intended scope under those anchors;
3. identify the smallest next proposition/evidence step that can genuinely move partial target facts toward exact `TargetWheelCompatibilityEvidence`, or justify remaining unresolved;
4. do not expand to matrix/reusable/container workflows unless transfer pressure earns that capability;
5. admit S013 only if the concrete implementation exposes behavior the existing anchors cannot discriminate.

## Continuation-critical guards

- candidate formulation does not manufacture applicability;
- missing evidence is not negative evidence;
- package evidence and repository-environment evidence remain separate;
- exact repository/revision provenance and workflow/job scope must be preserved;
- UpgradePilot's own environment is not evidence for another repository environment;
- broad environment labels must not become exact wheel tags;
- CI/platform presence must not imply affected dependency-environment formation;
- `not_observed` must not be interpreted as established absence;
- multi-environment evidence must not be flattened into one repository-wide union;
- apparent disagreement must be scoped before it is classified as conflict;
- wheel loss, source fallback availability, and source-build success remain separate;
- do not introduce universal planners, registries, environment reconstructors, generic provenance graphs, plugin systems, or similar infrastructure without demonstrated need.

## Learning state

Current demonstrated depth remains **substantial guided implementation exposure with repeated evidence-driven reasoning/debugging; no formal mastery assessment**.

Current learning emphasis is concrete target-environment evidence interpretation: distinguish observation from inference, preserve exact identity/provenance and partial facts, separate environment formation from broad CI presence, and keep exact wheel compatibility unresolved until the repository evidence actually justifies it.
