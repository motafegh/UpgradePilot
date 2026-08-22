# UpgradePilot Current Memory

**Last updated:** 2026-08-22  
**Authority:** Sole repository owner of live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Non-negotiable implementation-retention rule

**Existing code is evidence to inspect, not authority to preserve.** Current use, passing tests, comments, historical intent, prior effort, or another under-review consumer does not by itself justify keeping a field, check, type, helper, abstraction, metadata value, alias, dependency, or compatibility surface.

For every material mechanism under review:

```text
What current admitted responsibility / proof need / material risk / real compatibility obligation requires it?
→ if independently justified: keep the smallest adequate mechanism
→ if not independently justified: remove or narrow it
```

Do not invent reasons for legacy/current implementation. Do not use circular retention arguments such as “field X must stay because consumer Y uses it” when Y's dependence on X is itself under review. Passing tests protect behavior; they do not prove that the mechanism producing that behavior is architecturally necessary.

This rule is now durable in `AGENTS.md` and `docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md` (`JUST-*`) and is bound explicitly into the active reconciliation plan.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice. X1 remains available only through its evidence-gated admission rule.
- **Current mode:** normal **learning by doing and building** under `OPERATING_GUIDE.md`; the dedicated learning-folder route is paused, not abandoned as project learning.
- **Current implementation responsibility:** [`plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`](plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md).
- **Current plan position:** **R0 COMPLETE; R1 IN PROGRESS — contract/field necessity investigation before production edits**.
- **Current progressive working record:** [`working-memory/2026-08-22_B2-source-evidence-and-uv-reconciliation-session.md`](working-memory/2026-08-22_B2-source-evidence-and-uv-reconciliation-session.md).
- **Current active audit inputs:** AUDIT-001, AUDIT-006, AUDIT-007, classified in [`audits/active/README.md`](audits/active/README.md); canonical audit files remain directly under `audits/`.
- **Audit lifecycle:** [`audits/LIFECYCLE.md`](audits/LIFECYCLE.md) — active / deferred / absorbed.
- **Dedicated learning package:** [`learning/2026-08-17-b2-dependency-environment-ci-consumption-mastery/`](learning/2026-08-17-b2-dependency-environment-ci-consumption-mastery/) is **PAUSED at its recorded Plan-02/Chunk-1 state**. Do not advance its learning-memory/checklists during the reconciliation unless the plan explicitly requires a historical note.
- **Previous dependency-environment/CI plan:** [`plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md`](plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md) is **DEFERRED at the completed Cluster-5 boundary**. Cluster 6 must not start while the reconciliation plan is active.
- **Agentic evaluation:** [`plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md`](plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md) is **DEFERRED** until the reconciliation closes and older continuations are re-reviewed against the modified source/contracts.
- **Current product status:** previously accepted Clusters 0–5 remain historical green evidence; Cluster 6 is not started.
- **Latest product-runtime validation point:** `bfdfd4257574f85cc3a2d094bf46a37ad6373dea` — `508 tests / OK`, `HEAD == origin/main`, clean worktree at that validation point.
- Governance/plan/working-memory commits after that point do not create a newer product-runtime validation point.
- **Tranche 2 static↔runtime correlation:** NOT SELECTED / NOT AUTHORIZED.

## Why the live continuation changed

Learning/review of the current B2 implementation exposed concrete design pressure before wider integration:

```text
strong provider validation
+ permissive/weakly expressed exact-file internal type
→ repeated downstream invariant revalidation

one external uv.lock format
→ duplicated structural parsers
→ demonstrated admission-rule drift

real uv command scope
→ --all-packages dropped from current declaration
→ negative-ish not_established can be stronger than modeled scope

current uv membership name
→ can sound like complete environment membership
while implementation principally proves
→ explicit selected-root reachability
```

Ali explicitly selected normal learning-by-building so these source/design issues can be reconciled before they become deeper application dependencies.

## Current selected responsibility

The plan seeks the **smallest sound architecture**, not maximal modeling and not minimal line count.

Desired responsibility direction:

```text
UNTRUSTED GITHUB FILE RESPONSE
→ GitHub-owned necessary acquisition validation
→ strong exact repository text evidence containing only justified durable facts
→ domain parsing / necessary relational composition

EXACT uv.lock TEXT
→ one bounded uv-specific structural interpretation
   ├─ dependency-transition comparison
   └─ explicit selected-root reachability

STATIC uv COMMAND
→ explicit selectors + minimum required workspace/project scope
→ explicit-root reachability evidence
→ CI static-consumption composition
```

Stable proof ladder remains:

```text
dependency transition
!= explicit-root/environment membership evidence
!= static environment selection
!= static dependency consumption
!= resolver satisfiability/currentness
!= runtime execution/success
!= exact-version witness
!= direct package exercise
!= behavioral compatibility/safety/action
```

## R0 frozen conclusions

R0 completed without product behavior changes.

**R0 inventory is not a retention list.** It established what exists, where checks currently live, and how responsibilities currently connect. Under the now-explicit `JUST-*` retention rule, every material mechanism still has to earn retention from an independent current need. R0 does not need to be rerun; its classifications are interpreted as ownership categories, not blanket approval of every current check or field inside a category.

### Exact-file ownership

`GitHubRepositoryClient` currently validates path/type/blob/size/base64/decoded-size/UTF-8 facts strongly, but `RepositoryTextFile` permits weaker/manual construction and `ExactRepositoryTextFile` is only an alias. Dependency, target, and upstream consumers therefore repeat some provider-owned invariant checks.

R1 may simplify only after strengthening the owning exact-file contract. External-boundary validation, semantic/domain validation, and relational/rebinding **categories** remain protected, but an individual check/field still must be necessary for the admitted acquisition/domain/relation it claims to protect.

### Validation taxonomy

```text
KEEP AS RESPONSIBILITY CATEGORY — external trust boundary
validate the untrusted response enough to establish the admitted exact text-file acquisition

KEEP AS RESPONSIBILITY CATEGORY — semantic/domain
uv.lock / pyproject schema and meaning required by the selected proposition

KEEP AS RESPONSIBILITY CATEGORY — relational/rebinding
only relations that remain independently necessary between retained evidence objects

R1 CANDIDATES — repeated internal invariants
returned_path == path after acquisition admission
reported/decoded count propagation after boundary checks
other provider-owned facts repeated only because the type is weak

R1 NECESSITY REASSESSMENT — provider metadata
blob_sha presence/propagation and any downstream blob rebinding
retrieved_at placement and scope

REASSESS STRUCTURALLY — impossible states
manual/internal fabrication of purported exact evidence that the real admitted construction boundary should make unrepresentable
```

Specific R0 correction: `blob_sha` was previously grouped with protected external validation. That ownership classification does **not** establish that UpgradePilot needs provider blob identity. R1 must first determine whether blob identity supports a current acquisition/product/proof requirement beyond exact repository + immutable revision + path. If not, both durable propagation and unnecessary provider strictness around it should be removed rather than defended from current usage.

### uv structural duplication

`uv_lock.py` and `uv_membership.py` independently parse overlapping `uv.lock` structural truth. A concrete divergence exists: transition parsing admits a missing package version only for exact editable/virtual workspace-source shapes, while membership parsing currently permits `version=None` without the same source restriction.

R2 is therefore justified as one bounded **uv-specific** structural parser/model, not a generic graph/package-manager framework.

### uv scope/proposition

Current `ProjectEnvironmentSelectionDeclaration` has no place for S001 `--all-packages`; the S001-shaped test contains the flag but preserves only group/extra selectors.

The uv proposition is frozen as:

> Given a changed package established from an exact admitted `uv.lock`, a statically explicit positive uv group/extra selector with enough admitted project/workspace scope, and the exact admitted lock structure, determine whether an in-scope explicitly selected root has a deterministic unconditional lock-backed path to the changed package.

```text
member
→ one sound in-scope explicit root/path is enough

not_established
→ all roots in the represented proposition scope exhausted with no witness/ambiguity

unresolved
→ scope/marker/fork/edge/source/traversal uncertainty prevents the conclusion
```

This does not establish complete uv environment formation, defaults, currentness, resolver success, sync/install success, runtime execution, or compatibility.

S001 positive regression witness remains:

```text
docs
→ mkdocs-llmstxt
→ beautifulsoup4
→ soupsieve
```

### pyproject status

R0 did not authorize removing `pyproject.toml`. Current uv membership uses project name for one workspace-package binding, group/extra names for namespace cross-checking, and project path for project-root binding. R4 will decide which of those facts remain necessary after R1–R3 establish stronger evidence/structure/scope. Current use is evidence for that review, not proof that each fact must remain.

### CI proof split

Preserve:

```text
STATIC DEPENDENCY CONSUMPTION
!= STATIC DIRECT EXERCISE
!= EXACT-HEAD RUNTIME AUTHORITY
```

and:

```text
successful exact-head CI
+ supported static dependency consumption
→ supported_not_correlated
```

CI package/workflow/job/step/segment joins remain only where the relation they establish is independently required by the retained CI proposition.

## Audit lifecycle and current disposition

Canonical audit records keep stable paths directly under `audits/`. Lifecycle titles/classification are maintained through the three lifecycle indexes.

### Active

- [`AUDIT-001`](audits/2026-08-01_AUDIT-001_exact-pr-file-acquisition-evidence-contract.md)
- [`AUDIT-006`](audits/2026-08-21_AUDIT-006_internal-evidence-type-strength-and-revalidation-boundaries.md)
- [`AUDIT-007`](audits/2026-08-22_AUDIT-007_uv-membership-proposition-and-lock-model-boundaries.md)

### Deferred

- [`AUDIT-004`](audits/2026-08-16_AUDIT-004_uv-lock-resolution-satisfiability-evidence-boundary.md)
- [`AUDIT-005`](audits/2026-08-21_AUDIT-005_product-ai-agentic-orchestration-sequencing.md)

### Absorbed

- [`AUDIT-002`](audits/2026-08-02_AUDIT-002_ci-dependency-exercise-proof-boundary.md)
- [`AUDIT-003`](audits/2026-08-10_AUDIT-003_post-conversation-c-product-decision-model.md)

## Current plan status

```text
✓ R0  re-anchor contracts + freeze behavior
→ R1  strengthen exact repository-file evidence ownership — IN PROGRESS
  R2  one bounded uv-specific structural lock model
  R3  preserve minimum real uv command/workspace scope
  R4  narrow uv membership to explicit selected-root reachability
  R5  rebind CI consumption to reconciled evidence
  R6  pressure S001 / S011 / S005 + changed-case workspace transfer
  R7  acceptance + audit disposition + deferred-plan re-review
```

No R1 product-source implementation has started yet; R1 is currently freezing the minimum justified contract.

## Pressure/proof anchors

- **S001:** real `uv sync --all-packages --group docs`; preserve the positive docs witness and honest workspace-scope semantics.
- **S011:** optional-extra `mlx` versus selected `dev`; keep source-established project environment membership separate from uv lock reachability.
- **S005:** tox/uv-mediated lock consumption; keep selection interpretation and lock reachability separate.

## Continuation-critical guards

- `MEMORY.md` alone owns live continuation.
- The current reconciliation plan is the only active implementation route until its final STOP/REVIEW gate or Ali changes selection.
- Existing implementation/current use/passing tests/history are not retention authority; every touched mechanism must earn retention independently under `JUST-*`.
- Never justify an upstream field from a downstream consumer whose dependence on that field is itself being reviewed.
- Do not start old Cluster 6, the agentic evaluation, Tranche 2, or a separate source-clarity pass in parallel.
- Preserve necessary GitHub/external trust-boundary validation; simplification must not weaken the admitted acquisition contract, but provider metadata/checks that prove no required fact must not be retained merely because they already exist.
- Preserve relational/rebinding checks only when the retained relation itself is independently necessary.
- Do not introduce generic trust/provenance wrappers, generic dependency graphs, or generic package-manager abstractions without new evidence and explicit admission.
- Do not build a complete uv environment interpreter merely to justify an over-broad name.
- project/lock coherence/currentness and resolver/runtime evidence remain separate propositions.
- static dependency consumption != runtime execution/success != exact changed-version exercise.

## Immediate project action

Continue **R1 — strengthen exact repository-file evidence ownership**.

The A/B type question is sufficiently resolved for the current design direction:

```text
RepositoryTextFile itself
→ leading strong successful repository-text contract

separate ExactRepositoryTextFile hierarchy
→ not justified merely for legacy/test convenience
```

Next bounded investigation:

```text
for each candidate durable field/check
→ identify the exact independent product/proof/acquisition need
→ pressure that need against dependency + materially different consumers
→ reject current-use/circular justification
→ freeze the minimum strong RepositoryTextFile contract
→ map aliases/checks/tests that must migrate
→ only then make the first production source edit
```

`returned_path` and duplicated byte-count propagation currently lean toward validate-and-discard. `retrieved_at` currently has a plausible independent provenance requirement from the project evidence doctrine and upstream acquisition, but still must be placed at the narrowest correct layer. `blob_sha` is explicitly **reopened**: current propagation/consumer comparisons do not themselves justify it.

## Learning state

The project remains learning-oriented through implementation itself. Ali's predictions and reasoning are learning inputs, not engineering authority. The AI must lead from current responsibilities, source/evidence, proof boundaries, professional technical judgment, and simpler adequate alternatives; it should correct Ali's reasoning when needed and explain why rather than designing around an incorrect learner assumption.

For each bounded reconciliation step:

```text
real responsibility/problem
→ smallest blocking concept
→ Ali predicts/explains
→ inspect source/data flow
→ test the prediction against actual technical evidence
→ bounded change only after the responsibility is justified
→ inspect evidence/tests
→ separate observation from interpretation
→ diagnose/refine
→ preserve meaningful learning in code/working memory where useful
```

The dedicated learning-folder route remains paused because the source being learned is under active redesign. Resume, rewrite, or close it only after R7 re-review.