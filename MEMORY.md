# UpgradePilot Current Memory

**Last updated:** 2026-08-15  
**Authority:** Sole repository owner of live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Controlling route plan:** [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md).
- **B2 parent plan:** [`plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md).
- **Selected B2 responsibility:** [`plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md`](plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md).
- **Selected subordinate checkpoint:** [`plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_RECONCILIATION_PLAN.md`](plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_RECONCILIATION_PLAN.md).
- **Active progressive reconciliation record:** [`working-memory/2026-08-14_B2-cross-responsibility-architecture-reconciliation-progress.md`](working-memory/2026-08-14_B2-cross-responsibility-architecture-reconciliation-progress.md).
- **Phase-C simulation pressure evidence:** [`product-simulation/CROSS_RESPONSIBILITY_ARCHITECTURE_PHASE_C_PRESSURE_TEST_01.md`](product-simulation/CROSS_RESPONSIBILITY_ARCHITECTURE_PHASE_C_PRESSURE_TEST_01.md) — non-controlling transfer/adversarial evidence reviewed and adopted by main as evidence, not architecture authority.
- **Canonical accepted product-decision semantics:** [`docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`](docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md).
- **Documentation/decision ownership map:** [`docs/README.md`](docs/README.md).
- **Knowledge-architecture correction record:** [`working-memory/2026-08-14_UPGRADEPILOT-knowledge-architecture-and-decision-promotion.md`](working-memory/2026-08-14_UPGRADEPILOT-knowledge-architecture-and-decision-promotion.md).
- **Architecture-plan alignment record:** [`working-memory/2026-08-14_B2-cross-responsibility-architecture-plan-alignment.md`](working-memory/2026-08-14_B2-cross-responsibility-architecture-plan-alignment.md).
- **Artifact Increment 2:** [`working-memory/2026-08-13_B2-artifact-serviceability-increment-2-target-applicability.md`](working-memory/2026-08-13_B2-artifact-serviceability-increment-2-target-applicability.md).
- **Adopted target-evidence boundary:** [`working-memory/2026-08-13_B2-target-evidence-boundary-adoption.md`](working-memory/2026-08-13_B2-target-evidence-boundary-adoption.md).
- **Target Artifact Environment Increment 1:** [`working-memory/2026-08-14_B2-target-artifact-environment-increment-1-implementation.md`](working-memory/2026-08-14_B2-target-artifact-environment-increment-1-implementation.md).
- Product-simulation Cycle 02 evidence through S012 and its target-environment handoff are merged into `main` through `0c57754af3cc3757444f6c7f672e9781bc7a18e9`; the later architecture Phase-C pressure record was added in `b255a9bd620c708597ba0ca2ca16646e6ed65ef0`.

The accepted A→B→C product decision semantics are no longer reconstructed primarily from dated working-memory. The Product Decision Model specification is their normal durable owner; the August 6 reconciliation and AUDIT-003 remain provenance/reasoning evidence.

The selected B2 foundation plan uses that canonical semantic owner and contains the mandatory architecture gate now being executed because a second real mechanism/source consumer exposed cross-responsibility overlap and proof-strength ambiguity.

The older [`plans/B2_SOURCE_CODE_STRUCTURE_RECONCILIATION_PLAN.md`](plans/B2_SOURCE_CODE_STRUCTURE_RECONCILIATION_PLAN.md) is **completed historical precedent**, not the selected architecture plan. Its different August 4 topology reconciliation is behavior-validated in [`working-memory/2026-08-04_B2-source-structure-reconciliation-final-acceptance.md`](working-memory/2026-08-04_B2-source-structure-reconciliation-final-acceptance.md). The CI/Target/workflow/orchestration question is owned by the selected subordinate checkpoint above.

The active progressive reconciliation record is the normal dated reasoning/evidence surface for this checkpoint. Findings F-001 through F-054 now preserve Phase-A mapping, Phase-B option design/comparison, Phase-C transfer pressure, and main-side supplemental conclusions. Promote stable accepted conclusions to their durable owners only after Phase-D classification.

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

Its current environment-formation state remains `established` or `not_observed`. Phase C now reinforces that this static-only naming is stronger than the underlying proof and requires correction before further Target expansion:

```text
workflow definition declares command/path X
!= command/path X executed
!= command/path X succeeded
!= runtime environment formed
!= relevant dependency path exercised
```

The increment deliberately leaves `exact_wheel_compatibility_state="unresolved"`. It does **not** derive exact `packaging.tags.Tag` sets or produce `TargetWheelCompatibilityEvidence`.

No runtime source, tests, YAML dependency, CI/Target public contract, or orchestration implementation changed during the Phase-B/Phase-C architecture work. The latest architecture updates are documentation/reasoning state only.

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

The architecture/design records do not require or imply new product-runtime verification. Their correctness is checked through repository content/ownership/link reconciliation rather than being counted as product behavior proof.

## Adopted evidence and decision boundaries

The supported responsibility before `TargetWheelCompatibilityEvidence` remains:

```text
exact repository + immutable revision
→ proposition-specific scoped target evidence
→ partial, provenance-carrying environment/configuration facts
→ exact wheel compatibility only when genuinely justified
→ otherwise explicit insufficient / unresolved
```

GitHub Actions workflow evidence is one possible provider-specific Target evidence source. It is not the general Target-context model. S008 and S012 reinforce that target evidence may require separately scoped repository/build/package/runtime/historical/persisted-state facts.

Any static proposition may be established only at its actual declaration/configuration strength; it must not be mislabeled as runtime execution, success, environment formation, or behavior exercise.

Direct visible installation recognition is likewise one bounded evidence primitive, not the universal meaning of exact changed-dependency consumption. S005 shows that exact CI dependency authority may require lock, resolver, tox/uv, matrix, or other evidence chains.

The current `TargetWheelCompatibilityEvidence` remains the downstream exact contract. No universal environment reconstruction model is accepted.

## Immediate project action

**Phase C transfer/adversarial pressure testing is COMPLETE. The selected architecture checkpoint now enters Phase D — decision classification and durable-owner selection.** Continue executing [`plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_RECONCILIATION_PLAN.md`](plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_RECONCILIATION_PLAN.md) before any source refactor, Target expansion, YAML dependency addition, stronger CI runtime-correlation implementation, or cross-mechanism orchestration implementation.

Use [`working-memory/2026-08-14_B2-cross-responsibility-architecture-reconciliation-progress.md`](working-memory/2026-08-14_B2-cross-responsibility-architecture-reconciliation-progress.md) as the detailed evidence/reasoning record. The main-side Phase-C consolidation adopts [`product-simulation/CROSS_RESPONSIBILITY_ARCHITECTURE_PHASE_C_PRESSURE_TEST_01.md`](product-simulation/CROSS_RESPONSIBILITY_ARCHITECTURE_PHASE_C_PRESSURE_TEST_01.md) as major non-controlling evidence and supplements it with S003/S005/S007/S012 transfer checks.

### Phase-C result carried into Phase D

```text
OPTION B — SUPPORTED WITH REQUIRED MODIFICATIONS / CONSTRAINTS

RepositoryTextFile
→ bounded provider-specific GitHub Actions workflow-definition IR under upgradepilot.github
→ separate CI / Target interpretation

runtime WorkflowRun / WorkflowJob / WorkflowStep
→ separate evidence family

optional later static↔runtime correlation
→ explicit bounded responsibility, not part of the base IR
```

No examined pressure requires returning to duplicated local parsers or adopting a broad combined static+runtime base abstraction.

The decision-critical constraints are:

```text
C-01 static declaration != execution != success != runtime formation != exercise
C-02 consumer unsupported/unresolved != shared structural parser failure
C-03 multi-source Target facts do not become one synthetic exact environment without a justified join
C-04 static and runtime Actions evidence remain separate base contracts
C-05 source order / needs / same workflow or job != runtime environment continuity proof
C-06 preserve run text/context without becoming a full shell interpreter
C-07 keep the IR GitHub-Actions-specific and selectively normalized
C-08 parser safety requires graph/resource bounds as well as non-constructing parsing
C-09 direct-install observation != generic exact-dependency consumption
C-10 workflow evidence is one Target evidence source, not the Target model
C-11 stronger runtime proof/correlation is proposition-relative, not universally mandatory
```

### Phase-D decision packet

Resolve these seams individually and classify each conclusion by its durable owner:

1. **Shared static workflow seam** — accept/reject Option B as the durable architecture direction and confirm `upgradepilot.github` ownership.
2. **Parser method/dependency** — decide whether YAML node composition is part of the durable method and whether PyYAML is accepted, deferred pending implementation proof, or replaced.
3. **Parser security contract** — place source-size, duplicate-key, alias-cycle, active-recursion, depth/node-budget requirements in the correct durable owner.
4. **Target proof-strength correction** — accept the static declaration/configuration boundary and determine contract migration away from runtime-sounding formation semantics.
5. **Direct-install observation ownership** — admit, keep local, or defer the shared bounded primitive while explicitly preventing generic dependency-consumption overreach.
6. **Static↔runtime correlation disposition** — admit the separate architecture boundary now while deferring algorithm/implementation, or defer the responsibility itself to the later CI-strengthening tranche.
7. **Multi-job support boundary** — accept structural preservation now and separately decide how much CI/Target consumer interpretation belongs in the first implementation tranche.
8. **Heterogeneous mechanism orchestration** — admit a small typed mechanism-result collection/envelope now as a separate responsibility or defer until artifact-serviceability application integration requires it.
9. **Repository-path semantic drift** — retain the local GitHub path-validator duplication as a bounded reconciliation correction under existing source-neutral ownership.
10. **ADR disposition** — determine which accepted structural/method decisions require a new ADR, which are already owned by specifications/ADR-0007, and which belong only in the Phase-E implementation/refactor plan.

After Phase D accepts and classifies the durable direction, Phase E must produce the smallest coherent implementation/refactor handoff and test obligations. **Do not begin source edits merely because Option B survived Phase C.**

## Continuation-critical guards

- load canonical owners before reconstructing accepted decisions from dated working-memory;
- stable accepted reusable conclusions must be promoted to their durable owner while dated records remain provenance;
- the active architecture reconciliation should normally append to its single progressive working record rather than fragmenting the same investigation across many dated files;
- product-simulation pressure evidence is non-controlling until adopted/classified by the normal project owner;
- the Mature System Horizon remains non-controlling and may not self-authorize architecture or implementation;
- candidate formulation does not manufacture applicability;
- missing evidence is not negative evidence;
- evidence coverage, path-model coverage, and candidate-discovery coverage remain distinct;
- package evidence and repository-environment evidence remain separate;
- exact repository/revision provenance and workflow/job scope must be preserved;
- UpgradePilot's own environment is not evidence for another repository environment;
- broad environment labels must not become exact wheel tags;
- static workflow declaration/configuration must not become runtime execution/success/formation without appropriate observation;
- CI/platform presence must not imply affected dependency-environment formation beyond the admitted proposition strength;
- `not_observed` must not be interpreted as established absence;
- multi-environment evidence must not be flattened into one repository-wide union;
- apparent disagreement must be scoped before it is classified as conflict;
- wheel loss, source fallback availability, and source-build success remain separate;
- share primitives only when their meaning is genuinely identical across callers; structural sameness does not require shared domain conclusions;
- direct-install declaration observation must not become a generic dependency-consumption abstraction;
- dynamic Actions values, reusable workflows, matrices, or unsupported consumer semantics must not be mislabeled as parser failure when their source structure is safely preservable;
- source order and `needs` are structural evidence, not proof of runtime environment continuity;
- run path interpretation must account for working-directory context rather than matching command text in isolation;
- parser safety for untrusted public workflow text requires both safe/non-constructing YAML handling and explicit resource/recursion bounds;
- a combined static+runtime abstraction must not be introduced merely to avoid an explicit evidence-correlation boundary;
- stronger runtime correlation must remain proposition/evidence-relative rather than becoming mandatory pipeline work;
- the completed August 4 source-reconciliation plan must not be silently reactivated for the new architecture question;
- do not introduce universal planners, registries, environment reconstructors, generic provenance graphs, workflow execution engines, plugin systems, universal impact objects, or similar infrastructure without demonstrated need.

## Learning state

Current demonstrated depth remains **substantial guided implementation exposure with repeated evidence-driven reasoning/debugging; no formal mastery assessment**.

Current learning emphasis is architecture decision classification and promotion: distinguish evidence from accepted architecture; separate a durable structural decision from an implementation sequence; decide when an ADR is warranted; preserve proof-strength boundaries while selecting shared primitives; recognize that a shared primitive can be useful without becoming the general domain conclusion; and carry adversarial-case constraints into implementation planning without over-generalizing them.
