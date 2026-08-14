# UpgradePilot Current Memory

**Last updated:** 2026-08-14  
**Authority:** Sole repository owner of live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Controlling route plan:** [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md).
- **B2 parent plan:** [`plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md).
- **Selected B2 responsibility:** [`plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md`](plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md).
- **Selected subordinate checkpoint:** [`plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_RECONCILIATION_PLAN.md`](plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_RECONCILIATION_PLAN.md).
- **Active progressive reconciliation record:** [`working-memory/2026-08-14_B2-cross-responsibility-architecture-reconciliation-progress.md`](working-memory/2026-08-14_B2-cross-responsibility-architecture-reconciliation-progress.md).
- **Canonical accepted product-decision semantics:** [`docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`](docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md).
- **Documentation/decision ownership map:** [`docs/README.md`](docs/README.md).
- **Knowledge-architecture correction record:** [`working-memory/2026-08-14_UPGRADEPILOT-knowledge-architecture-and-decision-promotion.md`](working-memory/2026-08-14_UPGRADEPILOT-knowledge-architecture-and-decision-promotion.md).
- **Architecture-plan alignment record:** [`working-memory/2026-08-14_B2-cross-responsibility-architecture-plan-alignment.md`](working-memory/2026-08-14_B2-cross-responsibility-architecture-plan-alignment.md).
- **Artifact Increment 2:** [`working-memory/2026-08-13_B2-artifact-serviceability-increment-2-target-applicability.md`](working-memory/2026-08-13_B2-artifact-serviceability-increment-2-target-applicability.md).
- **Adopted target-evidence boundary:** [`working-memory/2026-08-13_B2-target-evidence-boundary-adoption.md`](working-memory/2026-08-13_B2-target-evidence-boundary-adoption.md).
- **Target Artifact Environment Increment 1:** [`working-memory/2026-08-14_B2-target-artifact-environment-increment-1-implementation.md`](working-memory/2026-08-14_B2-target-artifact-environment-increment-1-implementation.md).
- Product-simulation Cycle 02 evidence through S012 and its target-environment handoff are merged into `main` through `0c57754af3cc3757444f6c7f672e9781bc7a18e9`.

The accepted A→B→C product decision semantics are no longer reconstructed primarily from dated working-memory. The Product Decision Model specification is their normal durable owner; the August 6 reconciliation and AUDIT-003 remain provenance/reasoning evidence.

The selected B2 foundation plan has been revised to use that canonical semantic owner and now contains an explicit mandatory architecture gate when a second real mechanism/source consumer exposes cross-responsibility overlap or proof-strength ambiguity.

The older [`plans/B2_SOURCE_CODE_STRUCTURE_RECONCILIATION_PLAN.md`](plans/B2_SOURCE_CODE_STRUCTURE_RECONCILIATION_PLAN.md) is **completed historical precedent**, not the selected architecture plan. Its different August 4 topology reconciliation is behavior-validated in [`working-memory/2026-08-04_B2-source-structure-reconciliation-final-acceptance.md`](working-memory/2026-08-04_B2-source-structure-reconciliation-final-acceptance.md). The new CI/Target/workflow/orchestration question is owned by the selected subordinate checkpoint above.

The active progressive reconciliation record is the normal dated reasoning/evidence surface for this checkpoint. Continue appending material architecture findings, option comparisons, transfer/adversarial results, and rejected alternatives there rather than creating one working-memory file per discussion. Promote accepted durable conclusions later to their normal specification/ADR/plan owner.

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

Its current environment-formation state remains `established` or `not_observed`. The canonical Product Decision Model specification makes the proof-strength boundary explicit:

```text
workflow definition declares command/path X
!= command/path X executed
!= command/path X succeeded
```

The architecture reconciliation must determine whether the current target-environment naming/contracts need refinement and how static workflow definition evidence should relate to runtime Actions evidence.

The increment deliberately leaves `exact_wheel_compatibility_state="unresolved"`. It does **not** yet derive exact `packaging.tags.Tag` sets or produce `TargetWheelCompatibilityEvidence`.

The knowledge/planning alignment through `262e75318d4e53d746bc03d12b7ef34fc1fffe4e` changed documentation, plan ownership, and continuation only. It did not change product runtime source or tests.

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

The knowledge/planning/architecture-record changes do not require or imply new product-runtime verification. Their correctness is checked through repository content/ownership/link reconciliation rather than being counted as product behavior proof.

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

Any static proposition may be established only at its actual declaration/configuration strength; it must not be mislabeled as runtime exercise/success.

The current `TargetWheelCompatibilityEvidence` remains the downstream exact contract. No universal environment reconstruction model is accepted.

## Immediate project action

Continue the **inspection/design phases** of [`plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_RECONCILIATION_PLAN.md`](plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_RECONCILIATION_PLAN.md) before any further target-artifact-environment feature expansion or cross-mechanism orchestration refactor.

Use [`working-memory/2026-08-14_B2-cross-responsibility-architecture-reconciliation-progress.md`](working-memory/2026-08-14_B2-cross-responsibility-architecture-reconciliation-progress.md) as the progressive evidence/reasoning record for this checkpoint.

The major Phase-A baseline findings are now recorded there: current data flow, concrete CI/Target workflow-parser duplication, static-declaration versus runtime-execution proof-strength mismatch, multi-job structural-versus-consumer distinction, ordered-step/modifier pressure, static↔runtime step-correlation opportunity, first-mechanism orchestration pressure, repository-path semantic drift, and provisional future-pressure classification.

Continue by completing any source checks needed for those findings, then compare credible architecture options under Phase B. The checkpoint must ultimately decide:

- what raw/normalized GitHub Actions structure is genuinely shared;
- what remains CI-specific versus Target-specific;
- how static definition and runtime execution evidence correlate without proof inflation;
- whether direct installation recognition has a neutral/shared owner;
- how multiple jobs are structurally preserved versus interpreted;
- how Python-support and artifact-serviceability results coexist in application orchestration;
- the dependency direction for the affected packages;
- which foreseeable horizon pressures shape architecture now versus merely remain compatible/open;
- whether a new ADR, an existing-ADR amendment, or no ADR is warranted;
- the bounded implementation/refactor handoff if source changes are justified.

Do **not** refactor source during the architecture inspection merely because duplication is visible. Do **not** add another target-environment capability until the reconciliation determines the durable ownership/dependency direction.

## Continuation-critical guards

- load canonical owners before reconstructing accepted decisions from dated working-memory;
- stable accepted reusable conclusions must be promoted to their durable owner while dated records remain provenance;
- the active architecture reconciliation should normally append to its single progressive working record rather than fragmenting the same investigation across many dated files;
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
- the completed August 4 source-reconciliation plan must not be silently reactivated for the new architecture question;
- do not introduce universal planners, registries, environment reconstructors, generic provenance graphs, workflow execution engines, plugin systems, or similar infrastructure without demonstrated need.

## Learning state

Current demonstrated depth remains **substantial guided implementation exposure with repeated evidence-driven reasoning/debugging; no formal mastery assessment**.

Current learning emphasis is cross-responsibility architecture: distinguish raw source acquisition, normalized source structure, static declaration evidence, runtime execution evidence, and domain-specific interpretation; compare the existing CI and target-environment implementations; identify where reuse is genuinely semantic versus merely syntactic; understand how CI proof can be strengthened without turning CI into Target; and understand how a second impact mechanism should pressure orchestration without premature universal abstraction.