# UpgradePilot Current Memory

**Last updated:** 2026-08-14  
**Authority:** Sole repository owner of live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Controlling route plan:** [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md).
- **B2 parent plan:** [`plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md).
- **Selected B2 responsibility:** [`plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md`](plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md).
- **Canonical accepted product-decision semantics:** [`docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`](docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md).
- **Documentation/decision ownership map:** [`docs/README.md`](docs/README.md).
- **Knowledge-architecture correction record:** [`working-memory/2026-08-14_UPGRADEPILOT-knowledge-architecture-and-decision-promotion.md`](working-memory/2026-08-14_UPGRADEPILOT-knowledge-architecture-and-decision-promotion.md).
- **Artifact Increment 2:** [`working-memory/2026-08-13_B2-artifact-serviceability-increment-2-target-applicability.md`](working-memory/2026-08-13_B2-artifact-serviceability-increment-2-target-applicability.md).
- **Adopted target-evidence boundary:** [`working-memory/2026-08-13_B2-target-evidence-boundary-adoption.md`](working-memory/2026-08-13_B2-target-evidence-boundary-adoption.md).
- **Target Artifact Environment Increment 1:** [`working-memory/2026-08-14_B2-target-artifact-environment-increment-1-implementation.md`](working-memory/2026-08-14_B2-target-artifact-environment-increment-1-implementation.md).
- Product-simulation Cycle 02 evidence through S012 and its target-environment handoff are merged into `main` through `0c57754af3cc3757444f6c7f672e9781bc7a18e9`.

The accepted A→B→C product decision semantics are no longer expected to be reconstructed primarily from dated working-memory. The Product Decision Model specification is their normal durable owner; the August 6 reconciliation and AUDIT-003 remain provenance/reasoning evidence.

## Current implementation truth

The first Python-support candidate → applicability → discriminating observation → reevaluation loop is implemented and verified green.

Artifact Serviceability Increment 1 compares exact old/proposed PyPI artifact inventories, parses wheel compatibility tags, preserves sdist availability, and creates a target-agnostic artifact candidate when published wheel capabilities disappear.

Artifact Serviceability Increment 2 adds `TargetWheelCompatibilityEvidence`, `TargetWheelCompatibilityProblem`, `ArtifactServiceabilityImpactAssessment`, and `evaluate_artifact_serviceability_impact(...)`. It evaluates complete old/proposed wheel inventories against an **already-established exact target-supported tag set**.

Critical guards remain:

```text
removed published wheel tag != exact repository loses a compatible wheel
sdist exists != source build succeeds
```

Target Artifact Environment Increment 1 is implemented in `src/upgradepilot/target/artifact_environment.py`. It interprets one statically readable GitHub Actions job from strongly provenanced `RepositoryTextFile` evidence and preserves:

- exact repository/revision/workflow/blob/job scope;
- literal runner when available;
- literal `actions/setup-python` `with.python-version` when available;
- direct visible changed-dependency source installation;
- explicit limitations for missing/dynamic facts;
- explicit unsupported/problem state for admitted ambiguous shapes such as multiple or matrix jobs.

Its current environment-formation state remains `established` or `not_observed`. The new canonical Product Decision Model specification makes the proof-strength boundary explicit: static workflow definition/configuration evidence is not runtime execution/success evidence. The upcoming architecture reconciliation must decide whether current naming/contracts need refinement so the source expresses that distinction precisely.

The increment deliberately leaves `exact_wheel_compatibility_state="unresolved"`. It does **not** yet derive exact `packaging.tags.Tag` sets or produce `TargetWheelCompatibilityEvidence`.

The knowledge-architecture correction through `59593e4510a0b71dd77df4d7c719f80613e2f537` changed documentation/governance ownership only. It did not change product runtime source or tests.

## Verification truth

Fresh user WSL verification for Artifact Serviceability Increment 2 after pulling `main` through `f4c3ecdcbd738eceed7f50d30acb567a13c78642` remains:

```text
retained Increment-2 smoke: PASS
focused artifact-serviceability suite: 11 tests, OK
full active suite: 397 tests, OK
```

Artifact Serviceability Increment 2 remains **VERIFIED COMPLETE AT ITS BOUNDED SCOPE**.

For Target Artifact Environment Increment 1, the permanent focused regression file covers six bounded behaviors. An assistant reconstructed focused harness was green, and on 2026-08-14 Ali reported both requested real-repository WSL commands green after pulling current `main`:

```text
python -m unittest discover -s tests -p 'test_target_artifact_environment.py' -v
python -m unittest discover -s tests
```

No exact test count or timing is inferred because only the green result was reported. No separate nearest-regression command/result is recorded. GitHub exposes no configured commit status checks for the implementation commit, so no remote CI proof is inferred.

Therefore Target Artifact Environment Increment 1 remains **VERIFIED COMPLETE AT ITS BOUNDED SCOPE**. This proves the admitted partial target-environment interpretation behavior and compatibility with the active repository suite. It does not prove exact wheel-tag derivation or broader workflow/environment reconstruction.

The documentation/knowledge-architecture changes do not require or imply new product-runtime verification. Their correctness is checked through repository content/ownership/link reconciliation rather than being counted as product behavior proof.

## Adopted evidence and decision boundaries

The supported responsibility before `TargetWheelCompatibilityEvidence` remains:

```text
exact repository + immutable revision
→ one identified environment/job scope
→ proposition-specific repository evidence
→ partial, provenance-carrying environment facts
→ exact wheel compatibility only when genuinely justified
→ otherwise explicit insufficient / unresolved
```

For the first target-environment slice, scope is anchored by exact repository, immutable revision, workflow source path, and one statically readable GitHub Actions job.

Literal runner/platform, literal setup-python version, and visible changed-dependency installation evidence may be preserved when available. Platform/CI presence alone does not prove the affected dependency environment is formed. Broad labels must not be converted directly into exact `packaging.tags.Tag` sets.

The canonical decision-model guard now also makes this explicit:

```text
workflow definition declares command/path X
!= command/path X executed
!= command/path X succeeded
```

Any static proposition may still be established at its own declaration/configuration strength; it must not be mislabeled as runtime exercise/success.

The current `TargetWheelCompatibilityEvidence` remains the downstream exact contract. No universal environment reconstruction model is accepted.

## Immediate project action

Pause further target-artifact-environment feature expansion and perform a **cross-responsibility source-architecture reconciliation** before another implementation increment.

Use the canonical knowledge surface first:

1. `PROJECT_CHARTER.md` only where mission/boundary/claims matter;
2. `docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`;
3. `docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`;
4. `docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`;
5. `docs/architecture/ADR-0007-responsibility-based-python-subpackages.md` and relevant existing ADRs;
6. `proposals/UPGRADEPILOT_MATURE_SYSTEM_HORIZON.md` as non-controlling whole-system pressure/orientation;
7. current source/tests, especially CI workflow interpretation, target artifact-environment interpretation, impact mechanisms, applicability, and `investigation.py` orchestration;
8. dated working-memory/audits only where rationale/provenance or unresolved structural questions require them.

The architecture checkpoint must answer:

1. What exact raw/normalized GitHub Actions workflow structure is genuinely shared between CI and target-environment consumers?
2. What semantics must remain CI-specific versus target-specific?
3. How should static workflow-definition evidence and runtime workflow-execution evidence be represented/correlated without proof-strength inflation?
4. Which duplicated parser/normalization/installation-recognition primitives have genuinely identical meaning and deserve a neutral owner?
5. Should structural reading preserve multiple jobs while consumers remain responsible for safe selection/composition?
6. How should Python-support and artifact-serviceability results join application orchestration without indefinite mechanism-specific field sprawl and without a speculative `UniversalImpactEngine`?
7. Which future pressures are foreseeable from the mature-system horizon and current plans, and which are still too speculative to shape source architecture?
8. Does the accepted reconciliation justify a new ADR, an amendment/supersession of an existing ADR, or only a bounded refactor plan?

Do not refactor or add target-environment capability until this reconciliation determines the durable ownership/dependency direction.

## Continuation-critical guards

- load canonical owners before reconstructing accepted decisions from dated working-memory;
- when a dated record reaches a stable accepted reusable conclusion, promote it to the normal durable owner and retain the dated record as provenance;
- the Mature System Horizon remains non-controlling and may not self-authorize architecture or implementation;
- candidate formulation does not manufacture applicability;
- missing evidence is not negative evidence;
- evidence coverage, path-model coverage, and candidate-discovery coverage remain distinct;
- package evidence and repository-environment evidence remain separate;
- exact repository/revision provenance and workflow/job scope must be preserved;
- UpgradePilot's own environment is not evidence for another repository environment;
- broad environment labels must not become exact wheel tags;
- static workflow declaration/configuration must not become runtime execution/success without appropriate observation;
- CI/platform presence must not imply affected dependency-environment formation beyond the admitted proposition strength;
- `not_observed` must not be interpreted as established absence;
- multi-environment evidence must not be flattened into one repository-wide union;
- apparent disagreement must be scoped before it is classified as conflict;
- wheel loss, source fallback availability, and source-build success remain separate;
- share primitives only when their meaning is genuinely identical across callers; structural sameness does not require shared domain conclusions;
- do not introduce universal planners, registries, environment reconstructors, generic provenance graphs, workflow execution engines, plugin systems, or similar infrastructure without demonstrated need.

## Learning state

Current demonstrated depth remains **substantial guided implementation exposure with repeated evidence-driven reasoning/debugging; no formal mastery assessment**.

Current learning emphasis shifts to cross-responsibility architecture: distinguish raw source acquisition, normalized source structure, static declaration evidence, runtime execution evidence, and domain-specific interpretation; compare the existing CI and target-environment implementations; identify where reuse is genuinely semantic versus merely syntactic; and understand how a second impact mechanism should pressure orchestration without premature universal abstraction.
