# B2 Source Evidence and uv Reachability Reconciliation Plan

**Status:** ACTIVE — selected 2026-08-22  
**Execution branch:** `main`  
**Mode:** learning by doing and building  
**Live-state owner:** `../MEMORY.md`  
**Working record:** `../working-memory/2026-08-22_B2-source-evidence-and-uv-reconciliation-session.md`

## 1. Why this plan exists

B2 dependency-environment/CI work reached a validated Cluster-5 implementation, but learning/review exposed concrete design pressure before ordinary Cluster-6 integration:

- exact repository-file provider guarantees are stronger than the nominal internal `RepositoryTextFile` contract, so downstream consumers repeatedly revalidate invariants already established on the normal provider path;
- some exact-file metadata appears to be acquisition/validation detail rather than durable domain evidence;
- `uv_lock.py` and `uv_membership.py` independently encode overlapping `uv.lock` structural truth and have already drifted;
- the current uv membership name can be read as complete selected-environment membership although the implementation principally proves reachability from explicit group/extra roots;
- real S001 uses `uv sync --all-packages --group docs`, but the current static selection declaration drops the `--all-packages` workspace scope;
- current narrow lock-backed reachability requires `pyproject.toml` content even where that content may only corroborate facts already materialized in the lock rather than establish the proposition itself.

The correct response is not to add more checks and not to rewrite everything. It is to reconcile ownership so each invariant is established once at the strongest appropriate boundary and each result says exactly what it proves.

## 2. Audit inputs

Lifecycle indexes:

- `../audits/active/README.md`
- `../audits/scheduled/README.md`
- `../audits/deferred/README.md`
- `../audits/absorbed/README.md`

Active canonical audit evidence:

- `../audits/2026-08-01_AUDIT-001_exact-pr-file-acquisition-evidence-contract.md`
- `../audits/2026-08-21_AUDIT-006_internal-evidence-type-strength-and-revalidation-boundaries.md`
- `../audits/2026-08-22_AUDIT-007_uv-membership-proposition-and-lock-model-boundaries.md`

Scheduled post-reconciliation checkpoint:

- `../audits/2026-08-21_AUDIT-005_product-ai-agentic-orchestration-sequencing.md`
  - owning plan: `B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md`;
  - activation trigger: successful R7 acceptance/validation of this reconciliation;
  - handoff rule: enter the B2/X1 AI-agentic checkpoint before old Cluster 6 or another ordinary B2 continuation.

Deferred but important proof guard:

- `../audits/2026-08-16_AUDIT-004_uv-lock-resolution-satisfiability-evidence-boundary.md`
  - lock-backed reachability must not become lock-currentness/resolver/runtime proof.

Absorbed historical audits remain review evidence, not current work:

- `../audits/2026-08-02_AUDIT-002_ci-dependency-exercise-proof-boundary.md`
- `../audits/2026-08-10_AUDIT-003_post-conversation-c-product-decision-model.md`

## 3. Controlling boundaries

This plan is subordinate to:

- `../AGENTS.md`
- `../PROJECT_CHARTER.md`
- `../OPERATING_GUIDE.md`
- `../SECURITY.md`
- accepted specifications and ADRs.

In particular:

```text
observation != interpretation != evidence quality != decision
```

and:

```text
dependency transition
!= explicit-root reachability/environment evidence
!= static dependency consumption
!= resolver/currentness
!= runtime execution/success
!= exact-version witness
!= behavioral compatibility/safety/action
```

must remain true after the refactor.

### Non-negotiable retention burden

This reconciliation must not rationalize the current implementation merely because it exists.

```text
current code / field / check / consumer / test / historical design
→ evidence to inspect for behavior, migration pressure, and regressions
!= justification to retain the mechanism
```

Every material field, check, type, helper, abstraction, metadata propagation, alias, compatibility surface, or dependency that survives this plan must trace to a **current admitted product responsibility, proof need, material risk, or real compatibility/external obligation**. Passing tests prove current behavior, not architectural necessity. A downstream consumer's use of an upstream field does not justify that field when the consumer's dependence is itself under review. If a simpler mechanism preserves every independently justified responsibility and proof boundary, prefer the simpler mechanism and remove or narrow the unnecessary one rather than inventing a reason for it.

This is a retention burden, not a deletion quota: external trust checks, real relational joins, proof-calibrating distinctions, and genuine compatibility obligations stay when their independent reason survives review.

### End-to-end responsibility trace gate

Do not decide whether a mechanism belongs by inspecting only the file that currently contains it. Before retaining or adding a material check, field, transformation, metadata propagation, compatibility surface, or defensive mechanism, trace the admitted normal flow end-to-end:

```text
1. state the exact proposition / behavior the mechanism supplies
2. trace normal producer → integration/orchestration → consumer ownership
3. identify the earliest boundary that already guarantees that proposition
4. decide whether the reviewed downstream layer is an independent supported trust/public/composition boundary
5. identify the concrete failure or proof loss that becomes possible if the downstream mechanism is removed
6. distinguish supported alternate invocation from tests/fixtures/manual misuse
7. only then KEEP, MOVE, NARROW, or REMOVE
```

A proposition being real does not mean every downstream layer should re-establish it. Direct callable access, manually fabricable fixtures, or the possibility of inconsistent internal composition are not by themselves retention reasons. If an alternate invocation/composition route is genuinely supported, that route must be explicitly admitted as a responsibility/contract and protected accordingly.

This gate applies across R1–R7 wherever ownership, validation, propagation, transformation, compatibility, or defensive code is reviewed. It specifically prevents the mistake of classifying a check as “relational” or “defensive” and then retaining it without first asking whether an earlier boundary already establishes the relation for every admitted normal path.

This plan does **not** authorize a universal package-manager model, generic validation/trust framework, generic graph framework, shell/workflow interpreter, target-repository execution, runtime uv invocation, agentic controller, or unrelated source rewrite.

## 4. Previous and scheduled plans while this plan is active

Until this plan reaches R7 acceptance/validation:

- `B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md` is **deferred at the completed Cluster-5 boundary**; Cluster 6 must not start;
- `B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md` is **scheduled and blocked by this reconciliation**, not indefinitely deferred;
- the dedicated learning package `../learning/2026-08-17-b2-dependency-environment-ci-consumption-mastery/` is **paused**, preserving its exact learning state;
- every other older plan remains historical/complete/deferred according to its own record but is **not live execution authority** while this plan is active.

The scheduled agentic plan has a concrete activation trigger:

```text
R7 accepted + deterministic validation recorded
→ activate B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md as the next B2/X1 checkpoint
→ execute through an explicit evidence-backed disposition
→ only then may MEMORY.md select old Cluster 6 or another ordinary B2 continuation
```

This does not pre-adopt an agent architecture. The checkpoint may conclude `ADOPT`, `RETAIN AS PILOT`, `REJECT`, or `DEFER`; what is no longer allowed is silently skipping the AI/LLM evaluation because more deterministic feature work is available.

## 5. Desired end state

The reconciliation is successful when the product has a smaller and more exact responsibility chain resembling:

```text
UNTRUSTED GITHUB FILE RESPONSE
        ↓
GitHub-owned validation
        ↓
STRONG EXACT REPOSITORY TEXT EVIDENCE
        ↓
source/domain parsing
        ↓
semantic evidence
```

with:

```text
EXACT uv.lock TEXT
        ↓
one admitted uv-specific structural interpretation
        ├── dependency-transition consumer
        └── explicit-root reachability consumer
```

and:

```text
STATIC uv COMMAND
        ↓
bounded explicit selector + required workspace/project scope
        ↓
EXPLICIT SELECTED-ROOT REACHABILITY
reachable/direct-or-transitive | not_established | unresolved
```

The exact class/function names are not frozen before the relevant implementation step. Naming must follow the Naming Clarity Specification and match the actual proposition.

## 6. Implementation sequence

### R0 — Re-anchor contracts and freeze behavior

**Goal:** establish the exact pre-change behavior and affected ownership before structural edits.

Actions:

- inspect the current exact-file provider, dependency extractors, environment selection, uv membership, CI consumption/coverage, and directly affected tests;
- inventory repeated exact-file checks and classify each as:
  - external-boundary validation;
  - semantic/domain validation;
  - relational/rebinding validation;
  - repeated internal invariant;
  - impossible-state defense;
- inventory duplicated `uv.lock` structural rules in `uv_lock.py` and `uv_membership.py`;
- freeze the actual uv proposition as the smallest currently justified responsibility, expected to be explicit selected-root reachability unless source/test evidence contradicts that;
- preserve the current accepted S001 positive witness as a regression anchor.

**Retention interpretation:** R0's inventory records what exists and what currently depends on it; it is **not a retention list**. Classification as “currently used,” “tested,” or “historically intentional” does not establish necessity. Later steps must still trace retained mechanisms to an independently justified responsibility/risk/proof obligation.

**Learning-by-building checkpoint:** Ali should be able to explain which checks belong to GitHub, which belong to the uv parser, and which remain necessary when two independently valid evidence objects are joined.

**Gate:** no production behavior changes yet; exact change surface and baseline tests identified.

---

### R1 — Strengthen exact repository-file evidence ownership

**Goal:** make successful exact repository text evidence express the guarantees that the normal provider actually establishes, without inventing a generic trust framework.

Required design questions:

- Should `RepositoryTextFile` itself become the strong exact type, or is one separate strong exact-file type/factory materially clearer?
- Which values are required durable identity/provenance because a current product/proof responsibility actually needs them, versus acquisition-only validation detail?
- Can `returned_path` be validated and discarded after equality is established?
- Can decoded/reported byte-count propagation be reduced while preserving actual-input size bounds and provider contradiction checks?
- Does provider-reported blob identity add a currently required product/proof fact beyond exact repository + immutable revision + path, or is current downstream use circular retention pressure that should be removed?
- Which current aliases (`ExactRepositoryTextFile`, `ExactRepositoryFileEvidence`) remain useful versus misleading?
- For every proposed retained downstream relation/check, what does the full `investigation → analysis/orchestration → provider → semantic consumer` path already guarantee before the consumer runs?
- Is the consumer actually an independent supported trust/composition boundary, or merely a semantic layer receiving already-bound evidence from the normal product route?
- If direct/internal callers can construct inconsistent combinations, is that alternate invocation an admitted supported contract or only fixture/manual misuse pressure?

Implementation constraints:

- keep GitHub path/type/blob/size/base64/UTF-8 validation strong at the external trust boundary even when some response metadata is discarded after admission;
- keep explicit typed unavailability;
- do not make tests the reason production evidence remains weak;
- do not make current consumers the reason a field survives without independently justifying the proposition that consumer needs;
- preserve relational/rebinding validation only when the relation itself remains necessary **and the end-to-end ownership trace shows this layer must establish it**;
- remove downstream invariant checks only after the stronger upstream contract or admitted orchestration path genuinely makes them redundant;
- prefer the smallest strong contract that preserves every independently justified responsibility and proof boundary.

**Pressure:** migrate the dependency exact-file path first; use another materially different exact-file consumer as a sanity check before claiming a shared contract improvement.

**Gate:** focused GitHub/file + dependency-source tests green; impossible-state coverage is located at the boundary that owns it; every retained downstream check in the migrated path has an explicit end-to-end ownership reason rather than only a local classification.

---

### R2 — Introduce one bounded uv-specific structural lock model

**Goal:** establish external `uv.lock` structural truth once and feed separate semantic consumers.

The shared parser/model may own only facts genuinely common to current consumers, such as admitted lock schema/revision, package record identity/source/version rules, repeated-record preservation, dependency edges, selected optional/dev group roots, markers/extras needed by reachability, and canonical/raw structure needed by transition comparison.

It must **not** become:

- `GenericDependencyGraph`;
- `PackageManagerGraph`;
- a general package-manager abstraction;
- a complete uv runtime/config interpreter.

Required reconciliation:

- eliminate demonstrated versionless-record admission drift;
- preserve conservative repeated/universal-lock behavior;
- keep dependency-transition comparison semantics independent from graph/reachability semantics;
- keep malformed/unsupported lock structure explicit.

**Learning-by-building checkpoint:** distinguish structural parsing (“what valid lock structure says”) from semantic consumers (“what proposition this consumer establishes from it”).

**Gate:** all current `uv_lock` transition tests and uv reachability structural/ambiguity/cycle/bounds tests remain green or are deliberately updated with equivalent/stronger proof semantics.

---

### R3 — Preserve the minimum real uv command scope required by current evidence

**Goal:** stop losing material scope from admitted commands, beginning with S001 `--all-packages`.

Required behavior:

- preserve enough workspace/package scope in the static uv selection declaration to know whether explicit selectors apply to the current project/member, all workspace packages, or another admitted bounded scope;
- retain `include` versus `only` spelling/meaning where it is material to the claimed proposition;
- do not implement defaults, exclusions, conflicts, package targeting, or every uv flag unless a current proposition actually requires them;
- unsupported/dynamic scope must remain `unresolved`, not silently collapse to current-project scope.

Key asymmetry:

```text
positive witness
→ one sound in-scope root/path may establish reachability

not_established
→ requires exhaustion of the complete root/scope domain claimed by the result
```

Add a multi-member workspace regression where inspecting one member cannot incorrectly produce `not_established` for an all-packages command.

**Gate:** S001-shaped command preserves workspace-wide scope; positive and negative-ish semantics are sound under the admitted scope.

---

### R4 — Narrow uv membership to the proposition it actually proves

**Goal:** align names, inputs, comments, tests, and output semantics with explicit selected-root reachability rather than complete uv environment formation.

Expected direction:

```text
changed package from exact uv.lock
+ admitted explicit uv selector/scope
+ admitted exact lock structure
→ selected-root reachability evidence
```

Required decisions:

- choose concrete names that state reachability/root semantics;
- decide which `pyproject.toml` facts remain necessary for root/scope binding;
- remove mandatory project-content participation only where equivalent required identity/scope is already established elsewhere;
- keep project-source optional-extra/dependency-group evidence as its own responsibility for S011;
- keep project/lock coherence/currentness separate;
- preserve direct/transitive witness paths;
- preserve `unresolved` for markers/forks/ambiguity/resource bounds where the proposition cannot be established safely;
- when a deterministic structural path reaches the changed package only through unevaluated edge markers or package resolution markers, preserve one diagnostic conditional candidate root/path plus the raw unresolved conditions while keeping the state `unresolved`; these diagnostics must not assert that the conditions are mutually satisfiable, applicable to the target, or sufficient for a new `conditionally_reachable` state.

Do not build a complete uv selected-environment interpreter merely to justify the old name. Do not add target-marker evaluation or symbolic condition solving inside R4 merely to promote conditional candidates.

**Gate:** names and public contracts no longer imply whole-environment completeness; no-witness results are bounded to actually modeled roots/scope; conditional candidate diagnostics improve explanation without weakening the `unresolved` proof boundary.

---

### R5 — Rebind CI consumption to the reconciled evidence

**Goal:** ensure Cluster-5 CI composition consumes the new/narrowed dependency evidence without regressing its proof split.

Preserve:

```text
STATIC CONSUMPTION
!= STATIC DIRECT EXERCISE
!= RUNTIME AUTHORITY
```

and strongest current coverage meaning:

```text
successful exact-head CI
+ supported static dependency consumption
→ supported_not_correlated
```

Actions:

- update `ci/consumption.py`, workflow evidence composition, tests, and naming only as required by the reconciled dependency contract;
- keep static↔runtime correlation out of scope;
- do not resurrect the old `proven` semantics from absorbed AUDIT-002.

**Gate:** S001/S011 requirements-consumption behavior retains or improves current proof calibration.

---

### R6 — Real-case pressure and transfer

**Goal:** prove the reconciled architecture is not a cleanup that only serves one fixture.

Required cases:

#### S001

```text
uv sync --all-packages --group docs
+ exact lock graph
→ docs-root witness
→ mkdocs-llmstxt → beautifulsoup4 → soupsieve
```

Must preserve the positive witness without package-name hardcoding and without pretending static lock evidence proves runtime lock consumption/currentness.

#### S011

```text
changed dependency belongs to mlx optional environment
workflow selects dev
→ affected-environment consumption not established
```

Must remain separate from uv lock reachability.

#### S005

Must remain representable as mediated tox/uv lock-consumption pressure without forcing tox support or direct-uv-command coupling into the reachability module.

Also add at least one changed-case workspace scenario that would fail if `--all-packages` scope were ignored.

**Gate:** real cases support the responsibility split rather than exposing fixture-specific architecture.

---

### R7 — Acceptance, cleanup, and mandatory AI/agentic handoff

**Goal:** close the reconciliation cleanly, validate the architecture that actually exists after R1–R6, remove only unjustified transitional residue, freeze a trustworthy deterministic executable baseline, and hand off to the scheduled B2/X1 AI-agentic evaluation before ordinary B2 expansion resumes.

R7 is a **staged closure campaign**, not one broad test command and not an open-ended cleanup phase. Every checkpoint must preserve the distinction between observation, interpretation, proof strength, and live continuation.

#### R7 execution and recording discipline

Use one primary dated R7 working-memory record and update it progressively after material checkpoints. Create a separate dated repair/debug record only when an unexpected failure or design issue is substantial enough to need its own reasoning/evidence provenance; do not create one file per routine command.

For each substantive R7 slice:

```text
re-anchor exact state
→ perform the bounded check/review/change
→ inspect actual evidence/diff
→ record result + non-proof + resulting revision when material
→ perform proportionate post-action learning/ownership closure
→ continue only when that slice's gate is satisfied
```

If a validation failure contradicts the expected model, stop broad progression, diagnose the smallest affected boundary, repair only the demonstrated issue if authorized by this R7 scope, and rerun the discriminating gate before continuing.

R7 must distinguish these two revision concepts:

```text
ACCEPTED EXECUTABLE REVISION
= exact post-cleanup code/test revision that receives final deterministic executable validation

CLOSURE REVISION
= any later audit/memory/documentation-only revision that records/dispositions the accepted result
```

A documentation-only closure revision is not a newly tested executable authority. If executable code or tests change after the accepted executable revision is recorded, the accepted executable revision is superseded and final executable validation must be repeated.

#### R7.0 — Re-anchor exact entry state

Before running acceptance or cleanup:

- record the exact `main` revision that enters R7;
- reconcile the latest R6 implementation and any bounded corrective slices that occurred after the original R6 record, including proof-preservation fixes;
- record which R3/R4/R5/R6 runtime validations remain pending rather than inferring prior PASS from static/source review;
- load current environment/test-command facts only as needed for reproducible execution;
- update live continuation separately through `MEMORY.md` when R7 is actually selected; this reusable plan does not own live position.

**Gate:** R7 has one exact entry SHA, one current implementation model, and no stale claim that deferred runtime acceptance already passed.

#### R7.1 — Focused R3–R6 executable acceptance

Run the closest discriminating tests/checks for the reconciled chain before any broader suite.

At minimum, focused pressure must cover the material responsibilities established in R3–R6:

```text
R3
→ explicit selector/package-scope preservation
→ unsupported/dynamic selection remains unresolved

R4
→ direct/transitive selected-root reachability
→ all-workspace no-witness does not become false not_established
→ conditional candidate paths remain unresolved diagnostics

R5
→ reachability/project-source evidence maps to calibrated CI consumption
→ static consumption remains separate from direct exercise/runtime authority

R6
→ exact workflow text drives R3 → R4/project-source membership → R5
→ all supported matching commands are retained independently
→ irrelevant commands remain non-positive
→ material R3 unresolved selection is preserved as unresolved through CI coverage
```

The focused gate must include the bounded proof-preservation lesson established after R6 integration:

```text
R3 unresolved
!= no evidence
!= not_established

R3 unresolved
→ unresolved CI-consumption evidence
→ unresolved coverage consumption state unless stronger independent supported evidence exists
```

**Failure rule:** a focused failure blocks R7.2. Diagnose and repair before broadening.

**Gate:** focused R3–R6 executable checks pass and their results are recorded with exact commands/counts rather than summarized as “looks green.”

#### R7.2 — Normal investigation/CI integration acceptance

Validate the real production orchestration path, not only direct component calls:

```text
PR dependency analysis
→ typed changed-dependency source context
→ exact admitted pull-request workflow run/definition
→ exact project/lock source acquisition as required by that context
→ workflow_commands.py R6 derivation seam
→ R3 selection
→ R4 reachability or separate project-source membership
→ R5 static CI consumption
→ CI coverage aggregation
→ application/CLI result surface
```

Required assertions include:

- the normal `investigation.py` path derives project-environment consumption itself; it does not require test-side/prebuilt `ProjectEnvironmentSelectionDeclaration`, reachability, or consumption evidence;
- PR-CI admission remains bound to exact pull-request head workflow runs/definitions rather than arbitrary repository workflows;
- multiple supported matching commands can survive aggregation as evidence even if one representative consumption is selected for a summary field;
- unrelated/unsupported commands do not become positive by association with another command;
- the application/CLI contract reflects the current CI coverage responsibility rather than silently depending on the legacy ordinary-path evaluator.

**Gate:** nearest dependency/CI/application integration checks pass with the current production orchestration path.

#### R7.3 — Real S001 external verification

Run the retained S001 live verification through the normal product path against the frozen public case when provider access is available.

The live verification must begin from the public PR identity and acquire the exact admitted PR-head workflow definitions and exact `uv.lock`; it must not inject `docs`, a prebuilt declaration, a prebuilt reachability result, or a prebuilt consumption.

Expected semantic pressure includes:

```text
many admitted real commands
→ evaluate each independently
→ preserve every supported SoupSieve matching command
→ keep irrelevant commands non-positive
→ retain unresolved commands as unresolved when their selection cannot be established
```

The known S001 positive witness remains an anchor:

```text
uv sync --all-packages --group docs
→ mkdocs-llmstxt → beautifulsoup4 → soupsieve
```

Live external verification is **not the deterministic baseline**. Record it separately because provider/network state is external and time-varying.

- A semantic mismatch in successfully acquired exact evidence blocks acceptance and requires diagnosis.
- Provider/network unavailability must be recorded as external unavailability, not mislabeled as a semantic regression or a deterministic PASS. Deterministic acceptance may continue only if all deterministic real-case regressions remain green and the outstanding external verification dependency is explicitly preserved; R7 must not claim the live verifier passed when it did not run successfully.

**Gate:** live S001 result is either successfully verified and recorded, or explicitly unavailable with no semantic claim inflation and no loss of deterministic S001 regression coverage.

#### R7.4 — Full deterministic suite

After focused and nearest integration gates are trustworthy, run the complete deterministic validation required by the current repository/environment owners.

Record exactly:

```text
accepted candidate revision
runtime/interpreter identity when material
exact commands
exact test/check counts
PASS / FAIL
```

Use the current repository's standard deterministic verification owners rather than inventing a new suite list inside this plan. Include compile/static checks or experiment suites only where the current accepted repository verification procedure makes them part of the claimed baseline.

**Failure rule:** a broad failure is evidence, not permission for random multi-layer patching. Diagnose against the narrowest affected owner and rerun from the discriminating layer outward.

**Gate:** complete deterministic acceptance for the current executable candidate passes.

#### R7.5 — Final architecture, naming, and retention review

Only after executable behavior is understood, inspect the reconciled result for unnecessary transitional residue and source-clarity drift.

Apply the plan's retention burden and end-to-end responsibility trace to each material candidate. R7 must not pre-decide that something is removable merely because it is named “legacy,” nor keep it merely because tests/callers still exist.

Mandatory review candidates include, at minimum:

```text
evaluate_dependency_ci_exercise(...)
inspect_workflow_commands(...)
transitional ci_exercise_result read alias
WorkflowDependencyExerciseInput / external_consumptions naming and responsibility after R6 production migration
uv_reachability.py reuse of private/transitional uv_membership.py helpers
```

For each candidate, record proportionately:

```text
exact proposition/responsibility supplied
→ normal producer/caller
→ integration/composition boundary
→ downstream consumer
→ independent supported compatibility/proof/risk need, if any
→ simpler adequate owner/mechanism, if any
→ KEEP / MOVE / NARROW / REMOVE
```

Also inspect touched R1–R6 source against the current Source Clarity and Naming Clarity outcomes: responsibility, primary entry point, important cross-file flow, conservative branches, proof limits, and current/transitional surfaces should be recoverable from the repository without relying on prior chat.

**Gate:** every material transitional surface touched by this reconciliation has an evidence-backed disposition; no cleanup decision rests only on current use, label, test inertia, or aesthetic preference.

#### R7.6 — Bounded cleanup

Implement only cleanup justified by R7.5.

Allowed cleanup may include removing, moving, narrowing, renaming, or clarifying a transitional surface when its retained responsibility has been traced and the smaller mechanism preserves all admitted behavior/proof obligations.

Do not use R7 cleanup to introduce:

- new product semantics;
- generic package-manager/graph/framework abstractions;
- broad uv config/default interpretation;
- static↔runtime correlation;
- target-repository execution;
- agentic orchestration;
- unrelated repository-wide refactors.

If R7.5 concludes that all reviewed transitional surfaces still have independent justified owners, R7.6 may legitimately make no executable change.

After each code-bearing cleanup slice:

```text
focused regression
→ inspect actual diff
→ record changed revision + result
```

**Gate:** cleanup is bounded to demonstrated ownership/clarity findings and introduces no new responsibility.

#### R7.7 — Final post-cleanup executable validation

If R7.6 changes executable code or tests, rerun the acceptance ladder required by the changed risk:

```text
focused R3–R6 checks
→ nearest dependency/CI/application integration
→ complete deterministic suite
```

Rerun live S001 where the cleanup could materially affect its acquisition/orchestration/reachability behavior and external access is available.

The **accepted executable revision** is the exact final code/test revision that receives this post-cleanup deterministic validation. A pre-cleanup green SHA must not be frozen as the final executable baseline after code changes.

If R7.6 makes no executable change, the already-validated R7.4 executable candidate may remain the accepted executable revision, subject to R7.8 proof review.

**Gate:** one exact executable revision has final deterministic acceptance evidence after all executable cleanup.

#### R7.8 — Explicit proof-boundary audit

Before acceptance, inspect the final source/tests/results specifically for proof inflation or uncertainty erasure. Green tests alone are insufficient for this semantic gate.

At minimum confirm:

```text
unsupported/dynamic R3 selection
→ unresolved
→ does not disappear into not_established

conditional graph candidate
→ unresolved diagnostic
→ does not become reachable

all_workspace_packages + no complete witness domain
→ unresolved
→ does not become bounded-project not_established

supported static consumption
!= direct package exercise
!= command execution
!= runtime lock/version consumption

successful exact-head workflow + supported static consumption
→ supported_not_correlated
!= static↔runtime correlation

lock-backed reachability
!= resolver/currentness/satisfiability proof
!= behavioral compatibility/safety/action
```

Also confirm that preserving multiple matching commands does not imply uniqueness and that selecting one representative summary item does not erase the underlying evidence collection.

**Gate:** no unexplained proof-strengthening, uncertainty erasure, or authority conflation remains in the accepted executable candidate.

#### R7.9 — Audit lifecycle reconciliation

Disposition canonical audits finding-by-finding after the executable/proof result is known.

Update `audits/active/README.md`, `audits/scheduled/README.md`, `audits/absorbed/README.md`, and/or `audits/deferred/README.md` so each canonical audit has exactly one current lifecycle classification.

Rules:

- absorb only when material active findings are incorporated into stronger current owners;
- defer valid but unselected questions explicitly rather than letting them disappear;
- keep active only genuinely unfinished current findings;
- keep scheduled only while its explicit trigger has not yet been satisfied;
- once successful R7 acceptance satisfies AUDIT-005's trigger, reconcile its lifecycle according to the audit-index rules so it becomes the actual next checkpoint rather than remaining indefinitely “scheduled.”

Audit lifecycle edits are documentation/governance closure unless they expose a new executable blocker. If they expose such a blocker, R7 is not accepted; return to the owning earlier gate.

**Gate:** canonical audit lifecycle indexes are mutually consistent and AUDIT-005's post-R7 activation is explicit.

#### R7.10 — Freeze baseline, record closure, and hand off

Freeze the deterministic baseline consumed by the scheduled AI/agentic evaluation.

Record in the R7 working memory and promote only live continuation to `MEMORY.md`:

```text
accepted executable revision
+ exact deterministic validation commands/counts/results
+ separately recorded live S001 verification result or explicit external unavailability
+ normal investigation/orchestration behavior
+ reconciled typed evidence/capability contracts
+ final retention/cleanup dispositions
+ known unresolved/proof/authority boundaries
+ closure revision when later audit/memory/docs-only commits exist
```

The accepted executable revision and closure revision may be identical. If they differ only because of documentation/audit/memory changes, state that explicitly; do not call the closure revision newly execution-tested.

R7 acceptance means the reconciliation has a trustworthy deterministic executable baseline and an exact evidence-backed handoff. It does **not** prove target-repository runtime compatibility, universal package-manager correctness, or future AI/agentic superiority.

### Mandatory post-R7 handoff

Successful R7 acceptance satisfies AUDIT-005's scheduled trigger.

The next checkpoint is therefore:

```text
B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md
Phase 0 — refreshed route/AI-engineering/baseline reconciliation
→ Phase 1 — capability/orchestration inventory
→ Phase 2 — planner state/action/result contracts
→ Phase 3 — deterministic baseline/replay harness
→ Phase 4 — bounded model-planning pilot
→ Phase 5 — diagnosis/comparison
→ Phase 6 — ADOPT / RETAIN AS PILOT / REJECT / DEFER
→ Phase 7 only if adopted — bounded product integration
```

Old Cluster 6, another ordinary B2 expansion, or a source-clarity continuation must **not** become the next live implementation merely because it is available. The scheduled AI checkpoint must first reach an explicit evidence-backed disposition. If Phase 0 finds the experiment is no longer justified or correctly timed, that result must be recorded as an explicit `REJECT`, `DEFER`, or `RESCHEDULE`; it is not a silent skip.

After that disposition, `MEMORY.md` selects exactly one continuation using the new evidence.

## 7. Stop/review conditions

Stop and review before continuing if any proposed change would:

- retain a material field/check/type/helper/abstraction primarily because existing code, tests, or another under-review consumer already uses it;
- justify two under-review mechanisms circularly from each other's existence;
- retain or add a downstream check/field/defense without first tracing the admitted producer → integration → consumer path and locating the earliest sufficient owner;
- use direct internal callability, manually fabricable fixtures, or hypothetical misuse as the primary reason for production duplicate validation when that alternate route is not an admitted supported boundary;
- remove a transitional/legacy surface merely because its name says “legacy” without establishing that no admitted product/proof/compatibility responsibility remains;
- weaken external GitHub/file validation merely to reduce code;
- remove a relational/rebinding guard whose relation remains independently necessary **and whose end-to-end ownership trace shows this layer must establish it** merely because it looks duplicated;
- require a generic evidence/trust wrapper framework;
- require a generic dependency graph/package-manager layer;
- require implementing broad uv defaults/workspace/config semantics not demanded by current proof;
- execute target repository/tooling as part of ordinary static analysis;
- merge resolver/currentness/runtime meaning into static reachability;
- break accepted dependency transition semantics to simplify the shared parser;
- make `not_established` stronger than the actually modeled scope;
- erase an R3 `unresolved` selection and later reinterpret the absence as `not_established`;
- promote a conditional reachability candidate into `reachable` without the missing conditions being soundly established by an authorized owner;
- treat the live S001 external verifier as part of the deterministic baseline or convert provider unavailability into a semantic PASS/FAIL without evidence;
- freeze a pre-cleanup executable SHA as the final baseline after executable cleanup changes it;
- call a documentation-only closure SHA “execution-tested” when the accepted executable revision is earlier;
- mark R7 accepted before required post-cleanup executable validation and proof-boundary review complete;
- introduce agentic orchestration before this contract reconciliation closes;
- bypass the scheduled post-R7 AI/agentic checkpoint by resuming an ordinary continuation without an explicit checkpoint disposition.

## 8. Definition of done

This plan is done only when all of the following are true:

- every material retained mechanism touched by the reconciliation has a current independent justification rather than legacy/current-use rationale;
- every retained downstream validation/propagation/defensive mechanism touched by the reconciliation has an end-to-end ownership trace showing why the earliest sufficient owner is not enough by itself;
- exact-file guarantees have one clear owner and downstream duplicate-invariant validation is reduced only where safe;
- uv structural format truth has one bounded shared owner for current consumers;
- transition comparison and reachability remain distinct semantic responsibilities;
- uv reachability naming and proof language match what is actually established;
- S001 `--all-packages` scope is represented sufficiently for the admitted proposition;
- no false negative-ish `not_established` can arise from silently ignoring in-scope workspace members;
- unsupported/dynamic R3 selection uncertainty remains explicit through the R6/CI coverage path rather than disappearing into `not_established`;
- project metadata participates only where its facts are necessary for the exact proposition;
- the normal `investigation.py` path derives R3 → R4/project-source membership → R5 evidence from exact admitted workflow/source evidence without requiring prebuilt test-side semantic objects;
- all supported matching commands are preservable as evidence and irrelevant commands remain non-positive;
- S001, S011, S005 and changed-case pressure pass their intended deterministic proof boundaries;
- live S001 external verification is recorded separately from deterministic acceptance, without overclaiming if external acquisition is unavailable;
- Cluster-5 CI consumption/coverage calibration remains intact;
- focused + nearest integration + full deterministic validation pass for the final accepted executable revision;
- transitional/compatibility/naming surfaces reviewed in R7 have explicit KEEP / MOVE / NARROW / REMOVE dispositions with independent reasons;
- final source/diff review satisfies current Source Clarity and Naming Clarity outcomes;
- the explicit proof-boundary audit finds no unexplained proof-strengthening, uncertainty erasure, or authority conflation;
- active/scheduled/deferred/absorbed audits are dispositioned consistently in the lifecycle indexes;
- the exact accepted executable revision, deterministic commands/counts/results, proof limits, and any later documentation-only closure revision are recorded without conflating them;
- the exact deterministic baseline for the scheduled AI evaluation is recorded;
- working memory and `MEMORY.md` contain the final exact handoff;
- `B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md` is identified as the mandatory next B2/X1 checkpoint after R7 rather than one optional continuation among several.
