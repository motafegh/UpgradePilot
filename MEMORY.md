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

The active progressive reconciliation record is the normal dated reasoning/evidence surface for this checkpoint. Findings F-001 through F-054 preserve Phase-A mapping, Phase-B option design/comparison, and Phase-C transfer pressure. Phase-D D1/D2/D3 decisions are accepted and will be consolidated into that progressive record before durable ADR/plan promotion at Phase-D closure.

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

Its current runtime contract still uses `dependency_environment_formation="established" | "not_observed"`. Phase D3 now **accepts that this public/internal semantic must migrate** to static direct-installation-declaration meaning during the first implementation tranche; the current source remains unchanged until Phase E.

```text
workflow definition declares command/path X
!= command/path X executed
!= command/path X succeeded
!= runtime environment formed
!= relevant dependency path exercised
```

The increment deliberately leaves `exact_wheel_compatibility_state="unresolved"`. It does **not** derive exact `packaging.tags.Tag` sets or produce `TargetWheelCompatibilityEvidence`.

Current CI still uses `state="proven"` for a bounded composition of successful exact-head run/job evidence plus static install/invocation recognition. Phase D3 accepts that this claim must be narrowed/refined during the first migration tranche so it is not read as matched-command runtime-success proof. Exact stronger static↔runtime correlation remains a separate later implementation tranche.

No runtime source, tests, YAML runtime dependency, CI/Target public contract, or orchestration implementation changed during Phase D so far. PyYAML is now an accepted parser dependency/method choice for the future shared workflow reader, but it is not added to `pyproject.toml` until the Phase-E implementation handoff.

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

Direct visible installation recognition is one bounded evidence primitive, not the universal meaning of exact changed-dependency consumption. Phase D3 accepts a shared direct-installation-declaration observation under `upgradepilot.dependency`; package invocation/exercise remains CI-specific. The shared primitive must account for effective working-directory context and must stop at declaration strength.

Static workflow definition evidence and runtime `WorkflowRun` / `WorkflowJob` / `WorkflowStep` evidence remain separate base contracts. Phase D3 accepts an optional explicit static↔runtime correlation responsibility as a future strengthening seam, but its algorithm and implementation are deferred to the second implementation tranche and remain proposition-relative rather than mandatory pipeline work.

The current `TargetWheelCompatibilityEvidence` remains the downstream exact contract. No universal environment reconstruction model is accepted.

## Immediate project action

**Phase D is active. Decision blocks D1, D2, and D3 are ACCEPTED; continue with D4 — surrounding architecture, durable-owner/ADR disposition, and Phase-E handoff.** Continue executing [`plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_RECONCILIATION_PLAN.md`](plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_RECONCILIATION_PLAN.md) before any source refactor, Target expansion, YAML dependency installation, stronger CI runtime-correlation implementation, or cross-mechanism orchestration implementation.

### Accepted Phase-D block D1 — shared static workflow architecture

```text
D1-A ACCEPT
RepositoryTextFile
→ bounded provider-specific GitHub Actions static workflow-definition IR
→ separate responsibility-specific consumers

D1-B ACCEPT
owner = upgradepilot.github

D1-C ACCEPT
shared structural layer preserves multiple jobs and their visible structure even when a current CI/Target consumer cannot safely interpret them

D1-D REJECT
no broad base abstraction that merges static workflow definition with runtime WorkflowRun / WorkflowJob / WorkflowStep evidence

D1-E DEFER
arbitrary multi-job CI/Target semantic composition; consumer reasoning remains bounded and may return unresolved/unsupported
```

Multiple jobs being structurally visible does not establish cross-job environment continuity.

### Accepted Phase-D block D2 — parser method and bounded security

```text
D2-A ACCEPT
mature YAML representation/node parsing
→ bounded GitHub Actions extraction
→ typed provider IR

D2-B ACCEPT
PyYAML is the selected parser dependency/method for this architecture.
The implementation handoff will add and validate it; implementation problems may justify a later correction rather than keeping the architecture undecided now.

D2-C ACCEPT
public workflow YAML remains untrusted evidence and requires proportionate parser safeguards:
- no arbitrary application-object construction;
- safe failure/abstention on malformed or materially ambiguous structure;
- preserve the existing source-size boundary;
- bounded recursion/traversal sufficient to prevent obvious resource abuse.
Exact depth/node constants and similar mechanics remain Phase-E implementation/test choices unless demonstrated evidence requires stronger durable policy.

D2-D ACCEPT
parser/node objects remain internal syntax machinery; the UpgradePilot contract is the selectively normalized GitHub Actions IR, not a generic YAML AST.

D2-E REJECT
default/arbitrary-object YAML loading of untrusted repository workflow evidence.
```

The general D2-C invariant is owned by [`SECURITY.md`](SECURITY.md). This security boundary must remain proportionate: it protects obvious trust/resource boundaries without expanding into an independent hostile-parser framework absent demonstrated need.

### Accepted Phase-D block D3 — Target/CI proof semantics

```text
D3-A ACCEPT
Target's current runtime-sounding dependency-environment-formation semantics must migrate in Tranche 1 to static direct-installation-declaration semantics. Exact field/type names are Phase-E API work.

D3-B ACCEPT
share one bounded direct-installation-declaration observation primitive under upgradepilot.dependency.
Input meaning includes the static run command, effective working-directory context, and independently established dependency-source path.
Output meaning stops at “direct installation declaration observed.”

D3-C ACCEPT
package invocation/exercise recognition remains CI-specific; it is not part of the shared installation primitive.

D3-D ACCEPT
current CI `proven` semantics must be narrowed/refined in Tranche 1 so successful run/job + static path recognition is not presented as matched install/exercise runtime success.
Exact enum/API naming remains Phase-E work.

D3-E ACCEPT ARCHITECTURE / DEFER IMPLEMENTATION
static↔runtime correlation is a separate optional evidence-strengthening responsibility. Its exact trustworthy matching algorithm belongs to Tranche 2, not the base static IR and not Tranche 1.

D3-F DEFER
arbitrary multi-job CI/Target semantic composition. The shared IR preserves multiple jobs now; consumers may remain unresolved where safe selection/composition is not established.
```

### Remaining Phase-D decision packet

1. **D4 surrounding architecture/handoff** — heterogeneous mechanism orchestration, repository-path drift correction, ADR/specification disposition, progressive-record consolidation, and Phase-E implementation/refactor plan.

After D4 accepts and classifies the durable direction, Phase E must produce the smallest coherent implementation/refactor handoff and test obligations. **Do not begin source edits merely because D1/D2/D3 are accepted.**

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
- package invocation/exercise recognition remains CI-specific unless later demonstrated sameness earns a broader owner;
- dynamic Actions values, reusable workflows, matrices, or unsupported consumer semantics must not be mislabeled as parser failure when their source structure is safely preservable;
- source order and `needs` are structural evidence, not proof of runtime environment continuity;
- run path interpretation must account for working-directory context rather than matching command text in isolation;
- parser safety for untrusted public workflow text requires safe/non-constructing YAML handling and proportionate resource/recursion bounds without turning parser safety into a separate framework;
- a combined static+runtime abstraction must not be introduced merely to avoid an explicit evidence-correlation boundary;
- stronger runtime correlation must remain proposition/evidence-relative rather than becoming mandatory pipeline work;
- current CI `proven` wording/state must not be treated as matched-command runtime-success proof before its Phase-E migration;
- the completed August 4 source-reconciliation plan must not be silently reactivated for the new architecture question;
- do not introduce universal planners, registries, environment reconstructors, generic provenance graphs, workflow execution engines, plugin systems, universal impact objects, or similar infrastructure without demonstrated need.

## Learning state

Current demonstrated depth remains **substantial guided implementation exposure with repeated evidence-driven reasoning/debugging; no formal mastery assessment**.

Current learning emphasis is fast Phase-D decision classification: turn pressure-tested evidence into explicit durable architecture decisions, keep implementation mechanics out until Phase E where possible, and move quickly enough that architecture work does not displace implementation learning.
