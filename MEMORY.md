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

The architecture-reconciliation reasoning/continuation changes through this memory update change documentation/reasoning state only. They do not change product runtime source or tests.

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

**Phase B architecture-option comparison is complete enough to advance the selected checkpoint to Phase C transfer/adversarial pressure testing.** Continue executing [`plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_RECONCILIATION_PLAN.md`](plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_RECONCILIATION_PLAN.md) before any source refactor, target-artifact-environment expansion, or cross-mechanism orchestration implementation.

Use [`working-memory/2026-08-14_B2-cross-responsibility-architecture-reconciliation-progress.md`](working-memory/2026-08-14_B2-cross-responsibility-architecture-reconciliation-progress.md) as the progressive evidence/reasoning record. Findings F-001 through F-034 establish the current architecture/parser pressure; subsequent comparison/pressure conclusions remain provisional until promotion/closure.

### Option-B minimum contract carried into Phase C

```text
RepositoryTextFile
→ provider-specific GitHub Actions workflow-definition IR under upgradepilot.github
→ separate CI / Target interpreters

WorkflowDefinitionResult
├─ WorkflowDefinition
│  ├─ workflow-level defaults.run
│  └─ ordered JobEntry[]
│     ├─ StepsJobDefinition
│     ├─ ReusableWorkflowJobDefinition
│     └─ JobProblem
└─ WorkflowDefinitionProblem

StepEntry
├─ RunStepDefinition
├─ UsesStepDefinition
└─ StepProblem
```

Minimum typed structural surface:

```text
SourceSpan + source_index locators
bounded GitHubActionsStaticValue = scalar | sequence | mapping
workflow/job defaults.run shell + working-directory
job key/name/needs/runs-on/if/continue-on-error
job matrix fragment / container fragment
job-level reusable-workflow uses + with inputs
ordered run/uses steps
step name/if/continue-on-error
run command + step shell/working-directory
uses + with inputs
```

Important contract rules:

```text
source_index = structural occurrence/order locator, not runtime identity
SourceSpan = diagnostic/source-origin information, not runtime identity
raw RepositoryTextFile remains authoritative
selected YAML structure is normalized; arbitrary workflow fields remain raw/unmodeled
normal steps jobs and reusable-workflow jobs are distinct valid shapes
dynamic values are readable structure, not parser failure
whole-workflow hard problem != scoped JobProblem/StepProblem != consumer-level unresolved
workflow/job/step run context is preserved; effective context is derived later
static workflow definition remains separate from runtime WorkflowRun/WorkflowJob/WorkflowStep evidence
```

The leading parser implementation candidate inside Option B is:

```text
PyYAML node composition with BaseLoader-style scalar handling
→ bounded/guarded UpgradePilot Actions extraction
→ typed IR
```

No YAML dependency is accepted yet. Any later handoff must preserve safe/non-constructing parsing, duplicate-key visibility, alias-cycle protection, bounded recursion/node traversal, and the existing bounded source-size contract.

### Formal Phase-B comparison result

```text
Option A — local CI/Target parsers
  status: retained fallback
  strength: lowest immediate migration/new-dependency cost
  weakness: preserves demonstrated duplicated syntax reading and semantic-drift pressure

Option B — shared bounded static workflow IR + separate interpreters
  status: LEADING CANDIDATE for Phase C
  strength: shares demonstrated provider structure while preserving CI/Target and static/runtime proof boundaries
  cost: one bounded new provider contract and likely YAML parser dependency if later accepted

Option C — broad combined static+runtime Actions evidence model
  status: currently premature in broad form
  strength: could centralize later execution correlation
  weakness: risks merging definition identity with execution identity and designing the static↔runtime join before its safe semantics are earned
```

If Option C is constrained enough to preserve proof boundaries, it tends to decompose into:

```text
Option B static definition contract
+
existing runtime Actions evidence
+
explicit later correlation layer
```

which is currently a stronger dependency direction than making one broad combined base object.

### Next active Phase-C pressure

Pressure the leading Option B against discriminating real/known cases rather than adding more fields. At minimum test:

1. **S008** — prevent Dockerfile/repository Python context and workflow installation structure from being flattened into one fabricated exact environment;
2. **S011** — preserve macOS/Python workflow context while still refusing to infer that the optional `mlx` dependency environment was formed/exercised;
3. **existing CI audit hazards** — `|| true`, `continue-on-error`, `if`, install-after-test ordering, and whole-job success must remain insufficient for stronger matched-step runtime proof;
4. **S004 multi-job/matrix pressure** — preserve multiple jobs, `needs`/matrix/run context without inferring cross-job environment continuity or matrix runtime instances;
5. **reusable workflow / alias / scoped-problem pressure** — confirm valid static structure can survive without requiring recursive workflow execution semantics;
6. **future third-consumer test** — verify the IR is provider-specific enough to be reusable without becoming a generic workflow engine.

Phase C must determine whether these pressures **support, modify, or reject** Option B. Only after that should Phase D accept an architecture direction and decide ADR disposition.

Do **not** refactor source, add PyYAML, or rename Target/CI contracts during Phase C.

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
- dynamic Actions values, reusable workflows, matrices, or unsupported consumer semantics must not be mislabeled as parser failure when their source structure is safely preservable;
- source order and `needs` are structural evidence, not proof of runtime environment continuity;
- run path interpretation must account for working-directory context rather than matching command text in isolation;
- parser safety for untrusted public workflow text requires both safe/non-constructing YAML handling and explicit resource/recursion bounds;
- a combined static+runtime abstraction must not be introduced merely to avoid an explicit evidence-correlation boundary;
- the completed August 4 source-reconciliation plan must not be silently reactivated for the new architecture question;
- do not introduce universal planners, registries, environment reconstructors, generic provenance graphs, workflow execution engines, plugin systems, or similar infrastructure without demonstrated need.

## Learning state

Current demonstrated depth remains **substantial guided implementation exposure with repeated evidence-driven reasoning/debugging; no formal mastery assessment**.

Current learning emphasis is architecture-option evaluation and transfer testing: distinguish a low-cost local design from a genuinely shared responsibility and from an over-broad abstraction; recognize when a larger abstraction safely decomposes into a smaller base seam plus an explicit join; pressure candidate contracts against real counterexamples; preserve static/runtime proof tiers; and learn to treat an architecture ranking as provisional until adversarial transfer cases survive.