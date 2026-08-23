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
- `../audits/deferred/README.md`
- `../audits/absorbed/README.md`

Active canonical audit evidence:

- `../audits/2026-08-01_AUDIT-001_exact-pr-file-acquisition-evidence-contract.md`
- `../audits/2026-08-21_AUDIT-006_internal-evidence-type-strength-and_revalidation_boundaries.md`
- `../audits/2026-08-22_AUDIT-007_uv-membership-proposition-and-lock-model-boundaries.md`

Deferred but important proof guards:

- `../audits/2026-08-16_AUDIT-004_uv-lock-resolution-satisfiability-evidence-boundary.md`
  - lock-backed reachability must not become lock-currentness/resolver/runtime proof;
- `../audits/2026-08-21_AUDIT-005_product-ai-agentic-orchestration-sequencing.md`
  - agentic evaluation remains a valid later experiment but must not be layered over contracts currently being reconciled.

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

## 4. Previous plans while this plan is active

Until this plan reaches its final acceptance/STOP-REVIEW gate:

- `B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md` is **deferred at the completed Cluster-5 boundary**; Cluster 6 must not start;
- `B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md` is **deferred**;
- the dedicated learning package `../learning/2026-08-17-b2-dependency-environment-ci-consumption-mastery/` is **paused**, preserving its exact learning state;
- every other older plan remains historical/complete/deferred according to its own record but is **not live execution authority** while this plan is active.

After this plan closes, do **not** simply resume an older plan from its former next checkbox. First re-review each candidate continuation against the resulting source/contracts and update/supersede only what is materially stale. `MEMORY.md` then selects the next responsibility.

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
member/direct-or-transitive | not_established | unresolved
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
- preserve `unresolved` for markers/forks/ambiguity/resource bounds where the proposition cannot be established safely.

Do not build a complete uv selected-environment interpreter merely to justify the old name.

**Gate:** names and public contracts no longer imply whole-environment completeness; no-witness results are bounded to actually modeled roots/scope.

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

### R7 — Acceptance, cleanup, and deferred-plan re-review

**Goal:** close the reconciliation cleanly and determine what should resume next.

Validation order:

1. focused changed-module tests;
2. nearest dependency/CI integration tests;
3. full deterministic test suite;
4. inspect diff for source-clarity contract compliance;
5. confirm no unsupported proof-strengthening occurred;
6. record exact revision/test count/result in the working memory and `MEMORY.md`.

Then disposition active audits finding-by-finding:

- update `audits/active/README.md`, `audits/absorbed/README.md`, and/or `audits/deferred/README.md` so each canonical audit has one current lifecycle classification;
- classify an audit as absorbed only when its material active findings are incorporated into stronger owners;
- classify remaining valid but unselected questions as deferred;
- keep active only a genuinely unfinished selected finding.

Finally re-review, rather than blindly resume:

- `B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md` from Cluster 6 onward;
- `B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md`;
- any source-clarity/refactoring continuation that depends on the changed contracts;
- the paused dedicated learning package and whether it should resume, be rewritten, or be closed because the new learning-by-building work superseded part of its content.

`MEMORY.md` selects exactly one next live continuation after that review.

## 7. Stop/review conditions

Stop and review before continuing if any proposed change would:

- retain a material field/check/type/helper/abstraction primarily because existing code, tests, or another under-review consumer already uses it;
- justify two under-review mechanisms circularly from each other's existence;
- retain or add a downstream check/field/defense without first tracing the admitted producer → integration → consumer path and locating the earliest sufficient owner;
- use direct internal callability, manually fabricable fixtures, or hypothetical misuse as the primary reason for production duplicate validation when that alternate route is not an admitted supported boundary;
- weaken external GitHub/file validation merely to reduce code;
- remove a relational/rebinding guard whose relation remains independently necessary **and whose end-to-end ownership trace shows this layer must establish it** merely because it looks duplicated;
- require a generic evidence/trust wrapper framework;
- require a generic dependency graph/package-manager layer;
- require implementing broad uv defaults/workspace/config semantics not demanded by current proof;
- execute target repository/tooling as part of ordinary static analysis;
- merge resolver/currentness/runtime meaning into static reachability;
- break accepted dependency transition semantics to simplify the shared parser;
- make `not_established` stronger than the actually modeled scope;
- introduce agentic orchestration before this contract reconciliation closes.

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
- project metadata participates only where its facts are necessary for the exact proposition;
- S001, S011, S005 and changed-case pressure pass their intended proof boundaries;
- Cluster-5 CI consumption/coverage calibration remains intact;
- focused + nearest integration + full deterministic validation pass;
- active audits are dispositioned in the lifecycle indexes;
- working memory and `MEMORY.md` contain the final exact handoff;
- older deferred plans are re-reviewed before any becomes active.