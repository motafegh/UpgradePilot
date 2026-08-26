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

### R7 — Remote-first acceptance, cleanup, final local validation, and mandatory AI/agentic handoff

**Goal:** close the reconciliation cleanly using GitHub-backed source, test, diff, and real-case evidence first; remove only justified transitional residue; freeze one final executable candidate; then perform the local pull + deterministic validation only once the remote R7 work is otherwise complete.

R7 is a **remote-first staged closure campaign**, not a sequence of local test runs after every remote edit. Through R7.8, repository work is performed against the GitHub `main` state and runtime claims remain pending. Local execution is deliberately concentrated at R7.9 after the final remote executable candidate is frozen.

#### R7 execution and recording discipline

Use one primary dated R7 working-memory record and update it progressively after material checkpoints. Create a separate dated repair/debug record only when a material finding or later local failure needs independent reasoning/evidence provenance; do not create one file per routine review action.

For remote R7 slices:

```text
re-anchor exact GitHub state
→ inspect/trace/review the bounded responsibility
→ implement remote change only when evidence justifies it
→ inspect actual source/test/diff evidence
→ record result + non-proof + resulting revision
→ perform proportionate post-action learning/ownership closure
→ continue to the next bounded remote slice
```

Remote source/test review can establish implementation structure, test intent, evidence preservation, caller/consumer ownership, and diff correctness. It **cannot** establish that the tests execute successfully. Until R7.9, use terms such as `SOURCE/TEST REVIEW PASS`, `IMPLEMENTED`, or `PENDING LOCAL EXECUTION`; do not convert them into runtime PASS.

If the final local validation in R7.9 fails, do not patch locally as an unrecorded side path. Preserve the exact failure output, reopen the smallest owning remote R7 slice, implement the repair on GitHub, freeze a new final candidate, then rerun the required local validation.

R7 distinguishes three revision concepts:

```text
REMOTE CANDIDATE REVISION
= exact final code/test SHA after remote review and cleanup, before local validation

ACCEPTED EXECUTABLE REVISION
= that exact code/test SHA after final local deterministic validation passes

CLOSURE REVISION
= any later audit/memory/documentation-only revision that records/dispositions the accepted result
```

A later documentation-only SHA is not newly execution-tested. Any executable code/test change after a local PASS creates a new remote candidate and invalidates the prior executable acceptance until the required local gate is rerun.

#### R7.0 — Re-anchor exact entry state

Before remote review/cleanup:

- record the exact `main` revision entering R7;
- reconcile the latest R6 implementation and bounded corrective slices, including proof-preservation fixes;
- record which R3/R4/R5/R6 runtime validations remain pending;
- update live continuation through `MEMORY.md` when R7 is selected;
- do not require the local checkout merely to begin R7.

**Gate:** R7 has one exact GitHub entry SHA, one current implementation model, and no stale claim that deferred runtime acceptance already passed.

#### R7.1 — Remote focused R3–R6 source/test contract audit

Inspect the current source and focused tests together, without executing them yet, to confirm that the intended responsibilities and regressions are actually represented in the final remote tree.

At minimum trace:

```text
R3
→ explicit selector/package-scope preservation
→ unsupported/dynamic selection represented as unresolved

R4
→ direct/transitive selected-root reachability
→ all-workspace no-witness does not claim bounded not_established
→ conditional candidate paths remain unresolved diagnostics

R5
→ reachability/project-source evidence maps to calibrated CI consumption
→ static consumption remains separate from direct exercise/runtime authority

R6
→ exact workflow text drives R3 → R4/project-source membership → R5
→ all supported matching commands remain preservable
→ irrelevant commands remain non-positive
→ material R3 unresolved selection is preserved as unresolved through CI coverage
→ S011 remains project-source evidence
→ S005 mediated tox pressure does not manufacture direct uv support
```

The post-R6 proof-preservation rule is mandatory:

```text
R3 unresolved
!= no evidence
!= not_established

R3 unresolved
→ unresolved CI-consumption evidence
→ unresolved coverage consumption state unless stronger independent supported evidence exists
```

Inspect focused test assertions as proof intent, not runtime evidence. Record any missing regression or contract mismatch and repair it remotely before advancing.

**Gate:** source and focused tests form a coherent R3–R6 contract/regression set with no known missing required case; runtime remains explicitly pending R7.9.

#### R7.2 — Remote normal investigation/CI orchestration trace

Trace the actual normal product path end-to-end from current source and tests:

```text
PR dependency analysis
→ typed changed-dependency source context
→ exact admitted pull-request workflow run/definition
→ exact project/lock acquisition required by that context
→ workflow_commands.py R6 derivation seam
→ R3 selection
→ R4 reachability or separate project-source membership
→ R5 static CI consumption
→ CI coverage aggregation
→ application/CLI result surface
```

Confirm from source/tests that:

- `investigation.py` derives project-environment consumption itself rather than requiring prebuilt semantic objects;
- PR-CI admission remains bound to exact PR-head workflow runs/definitions;
- multiple supported matching commands can survive as evidence;
- unrelated/unsupported commands do not inherit positivity;
- material unresolved R3 selection is not dropped;
- application/CLI uses the current coverage-oriented responsibility rather than silently reverting to the legacy ordinary path.

This checkpoint is an ownership/integration review, not a substitute for execution.

**Gate:** the normal remote source/test trace has one coherent producer → orchestration → consumer route with the intended admission/proof boundaries and no known test-side-only integration gap.

#### R7.3 — Remote real-case GitHub evidence pressure

Use the GitHub connector against the retained public cases, especially S001, to verify that the real external evidence still has the shapes the implementation/tests claim to support.

For S001, begin from the real Pydantic PR identity and exact head evidence. Verify the admitted workflow text and exact `uv.lock` facts rather than injecting `docs` or a prebuilt semantic result.

Expected evidence pressure includes:

```text
real admitted workflow commands
→ more than one possible selection command
→ docs command(s) include the selected docs roots
→ exact lock graph contains:
   mkdocs-llmstxt → beautifulsoup4 → soupsieve
→ unrelated commands remain distinct evidence
```

Also retain the S011 and S005 separation claims from their real/simulation evidence where useful to confirm that R6 did not overfit S001.

This remote real-case evidence does **not** prove that current UpgradePilot source executes successfully. It proves that the retained external cases remain legitimate pressure for the implemented semantics and tests.

**Gate:** real GitHub evidence still supports the intended R6 cases, or any changed/unavailable evidence is recorded without claim inflation and the affected test/fixture assumptions are reconciled before continuing.

#### R7.4 — Final architecture, naming, and retention review

Inspect the reconciled result for unnecessary transitional residue and Source/Naming Clarity drift before any cleanup.

Apply the retention burden and end-to-end responsibility trace. Mandatory candidates include:

```text
evaluate_dependency_ci_exercise(...)
inspect_workflow_commands(...)
transitional ci_exercise_result read alias
WorkflowDependencyExerciseInput / external_consumptions naming and responsibility after R6 production migration
uv_reachability.py reuse of private/transitional uv_membership.py helpers
```

For each candidate record proportionately:

```text
exact proposition/responsibility supplied
→ normal producer/caller
→ integration/composition boundary
→ downstream consumer
→ independent supported compatibility/proof/risk need, if any
→ simpler adequate owner/mechanism, if any
→ KEEP / MOVE / NARROW / REMOVE
```

Also inspect touched R1–R6 source against current Source Clarity and Naming Clarity outcomes so responsibility, primary entry point, cross-file flow, conservative branches, proof limits, and transitional surfaces remain recoverable without prior chat.

**Gate:** every material transitional surface reviewed in R7 has an evidence-backed disposition; no decision rests only on current use, a `legacy` label, test inertia, or aesthetic preference.

#### R7.5 — Bounded remote cleanup

Implement only cleanup justified by R7.4.

Allowed cleanup may remove, move, narrow, rename, or clarify a transitional surface when the smaller mechanism preserves all admitted behavior/proof obligations.

Do not use cleanup to introduce:

- new product semantics;
- generic package-manager/graph/framework abstractions;
- broad uv config/default interpretation;
- static↔runtime correlation;
- target-repository execution;
- agentic orchestration;
- unrelated repository-wide refactors.

After each code/test-bearing remote cleanup slice:

```text
inspect changed source/tests
→ inspect exact GitHub diff
→ confirm nearest regression intent still protects the responsibility
→ record changed revision + pending-local-execution status
```

If R7.4 justifies no executable cleanup, R7.5 may make no source/test change.

**Gate:** cleanup is bounded to demonstrated ownership/clarity findings and introduces no new responsibility.

#### R7.6 — Remote post-cleanup source/diff and proof-boundary audit

Inspect the final remote executable candidate after all cleanup. This is the last semantic/source gate before audit lifecycle work and final candidate freeze.

At minimum confirm from source/tests/diff:

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

multiple supported matching commands
!= one unique correct command
```

Also inspect the complete R7 source/test diff for accidental scope expansion, stale transitional comments, missing renamed references, and test-side composition that bypasses the normal product path.

**Gate:** no known proof-strengthening, uncertainty erasure, authority conflation, or unexplained executable diff remains in the remote candidate. Runtime remains pending R7.9.

#### R7.7 — Audit lifecycle reconciliation

Disposition canonical audits finding-by-finding after the final remote architecture/proof result is known.

Update `audits/active/README.md`, `audits/scheduled/README.md`, `audits/absorbed/README.md`, and/or `audits/deferred/README.md` so each canonical audit has one current lifecycle classification.

Rules:

- absorb only when material active findings are incorporated into stronger current owners;
- defer valid but unselected questions explicitly;
- keep active only genuinely unfinished current findings;
- keep AUDIT-005 scheduled until R7's final local deterministic validation succeeds;
- do not activate the post-R7 AI/agentic plan merely because remote cleanup is complete.

If lifecycle review exposes a new executable blocker, return to the owning earlier R7 remote slice rather than freezing the candidate.

**Gate:** audit lifecycle indexes are internally consistent for the pre-acceptance state, with AUDIT-005 still waiting on final R7 validation.

#### R7.8 — Freeze the final remote candidate and local validation bundle

Once all remote source/test/real-case/retention/proof/audit work is complete, freeze the exact final executable candidate SHA.

Record:

```text
remote candidate revision
+ exact source/test files changed since R7 entry
+ final retention/cleanup dispositions
+ remote real-case evidence result
+ known proof/authority boundaries
+ exact final local validation commands
```

The local validation bundle should be small enough to run once but broad enough to justify the final claim. Normally it should include:

```text
sync/pull exact main
→ confirm clean worktree + exact candidate SHA
→ focused R3–R6 regressions
→ nearest dependency/CI/application integration regressions
→ complete deterministic standard suite
→ compile/static checks required by current repository procedure
→ live S001 verifier only if still required and practical for the claimed R7 evidence
```

Do not change source/tests after freezing the candidate unless a new remote issue is discovered; any such change produces a new candidate and requires refreezing.

**Gate:** one exact final GitHub code/test SHA and one exact local validation bundle are ready; no further planned remote executable work remains.

#### R7.9 — Final local pull and executable validation

Only now use the project checkout.

Ali pulls/synchronizes the final remote `main` candidate and runs the R7.8 validation bundle in the admitted WSL/Python environment. This local phase is validation, not a parallel implementation branch.

Record exactly:

```text
candidate SHA actually checked out
runtime/interpreter identity when material
clean-worktree state
exact commands
exact test/check counts
PASS / FAIL
```

Rules:

- do not claim PASS from remote source review;
- do not patch a failure only on the local checkout;
- if any required local gate fails, preserve the output, mark R7 unaccepted, return to the smallest owning remote R7 slice, repair on GitHub, freeze a new candidate, and rerun the required local gate;
- the accepted executable revision is the exact remote candidate SHA that the final local gate validates successfully.

**Gate:** focused + nearest integration + complete deterministic validation required by the final bundle pass against the exact frozen candidate, with any required compile/static/live verification result separately recorded.

#### R7.10 — Freeze accepted baseline, record closure, and hand off

After R7.9 succeeds, freeze the deterministic baseline consumed by the scheduled AI/agentic evaluation.

Record in the R7 working memory and promote only live continuation to `MEMORY.md`:

```text
accepted executable revision
+ exact local deterministic validation commands/counts/results
+ separately recorded remote/live S001 evidence result
+ normal investigation/orchestration behavior
+ reconciled typed evidence/capability contracts
+ final retention/cleanup dispositions
+ known unresolved/proof/authority boundaries
+ closure revision when later audit/memory/docs-only commits exist
```

Only after the local acceptance gate succeeds does successful R7 satisfy AUDIT-005's trigger. Reconcile its lifecycle accordingly and activate the scheduled B2/X1 checkpoint.

The accepted executable revision and closure revision may differ. If later commits change only audit/memory/docs, state that explicitly; do not call the closure SHA newly execution-tested.

R7 acceptance means the reconciliation has a trustworthy deterministic executable baseline and exact handoff. It does **not** prove target-repository runtime compatibility, universal package-manager correctness, or future AI/agentic superiority.

### Mandatory post-R7 handoff

Successful R7 acceptance activates:

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

Old Cluster 6 or another ordinary B2 expansion must not become live work before that checkpoint reaches an explicit evidence-backed disposition.

## 7. Stop/review conditions

Stop and review before continuing if any proposed change would:

- retain a material field/check/type/helper/abstraction primarily because existing code, tests, or another under-review consumer already uses it;
- justify two under-review mechanisms circularly from each other's existence;
- retain or add a downstream check/field/defense without tracing the admitted producer → integration → consumer path and locating the earliest sufficient owner;
- use direct internal callability, manually fabricable fixtures, or hypothetical misuse as the primary reason for production duplicate validation when that route is not admitted;
- remove a transitional/legacy surface merely because of its label without proving no admitted responsibility remains;
- weaken external GitHub/file validation merely to reduce code;
- require a generic evidence/trust wrapper or generic dependency graph/package-manager layer;
- require broad uv defaults/workspace/config semantics not demanded by current proof;
- execute target repository/tooling as part of ordinary static analysis;
- merge resolver/currentness/runtime meaning into static reachability;
- break accepted dependency transition semantics to simplify the shared parser;
- make `not_established` stronger than the actually modeled scope;
- erase R3 `unresolved` and reinterpret absence as `not_established`;
- promote a conditional candidate into `reachable` without soundly established conditions;
- treat remote source/test review as runtime PASS;
- perform piecemeal local validation before the final R7.9 gate unless Ali explicitly changes this execution mode;
- patch a final local validation failure only in the local checkout instead of returning to the remote owning slice;
- freeze a candidate SHA and then change executable code/tests without refreezing;
- call a documentation-only closure SHA execution-tested;
- activate AUDIT-005 before the final local acceptance gate succeeds;
- bypass the mandatory post-R7 AI/agentic checkpoint.

## 8. Definition of done

This plan is done only when all of the following are true:

- every material retained mechanism touched by the reconciliation has a current independent justification rather than legacy/current-use rationale;
- every retained downstream validation/propagation/defensive mechanism touched by the reconciliation has an end-to-end ownership trace showing why the earliest sufficient owner is not enough by itself;
- exact-file guarantees have one clear owner and downstream duplicate-invariant validation is reduced only where safe;
- uv structural format truth has one bounded shared owner for current consumers;
- transition comparison and reachability remain distinct semantic responsibilities;
- uv reachability naming and proof language match what is actually established;
- S001 `--all-packages` scope is represented sufficiently for the admitted proposition;
- no false `not_established` can arise from silently ignoring in-scope workspace members;
- unsupported/dynamic R3 selection uncertainty remains explicit through the R6/CI coverage path;
- project metadata participates only where necessary for the exact proposition;
- the normal `investigation.py` path derives R3 → R4/project-source membership → R5 evidence from admitted workflow/source evidence without prebuilt test-side semantic objects;
- all supported matching commands are preservable and irrelevant commands remain non-positive;
- S001, S011, S005 and workspace pressure remain represented by real/source-backed evidence and focused regression intent;
- Cluster-5 CI consumption/coverage calibration remains intact;
- transitional/compatibility/naming surfaces reviewed in R7 have explicit KEEP / MOVE / NARROW / REMOVE dispositions with independent reasons;
- final remote source/test/diff review satisfies current Source Clarity and Naming Clarity outcomes;
- the remote proof-boundary audit finds no known proof-strengthening, uncertainty erasure, or authority conflation;
- canonical audit lifecycle indexes are consistent before acceptance;
- one exact final remote executable candidate and validation bundle are frozen;
- Ali pulls that exact candidate only at the final local R7.9 gate and focused + nearest integration + complete deterministic validation required by the bundle pass;
- the exact accepted executable revision, local commands/counts/results, proof limits, and any later documentation-only closure revision are recorded without conflation;
- AUDIT-005 is activated only after that final local acceptance succeeds;
- the exact deterministic baseline for the scheduled AI evaluation is recorded;
- working memory and `MEMORY.md` contain the final exact handoff;
- `B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md` is the mandatory next B2/X1 checkpoint after R7 rather than an optional continuation.
