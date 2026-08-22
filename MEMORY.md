# UpgradePilot Current Memory

**Last updated:** 2026-08-22  
**Authority:** Sole repository owner of live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice. X1 remains available only through its evidence-gated admission rule.
- **Current mode:** normal **learning by doing and building** under `OPERATING_GUIDE.md`; the dedicated learning-folder route is paused, not abandoned as project learning.
- **Current implementation responsibility:** [`plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`](plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md).
- **Current progressive working record:** [`working-memory/2026-08-22_B2-source-evidence-and-uv-reconciliation-session.md`](working-memory/2026-08-22_B2-source-evidence-and-uv-reconciliation-session.md).
- **Current active audit inputs:** AUDIT-001, AUDIT-006, AUDIT-007, classified in [`audits/active/README.md`](audits/active/README.md); canonical audit files remain directly under `audits/`.
- **Audit lifecycle:** [`audits/LIFECYCLE.md`](audits/LIFECYCLE.md) — active / deferred / absorbed.
- **Dedicated learning package:** [`learning/2026-08-17-b2-dependency-environment-ci-consumption-mastery/`](learning/2026-08-17-b2-dependency-environment-ci-consumption-mastery/) is **PAUSED at its recorded Plan-02/Chunk-1 state**. Do not advance its learning-memory/checklists during the reconciliation unless the plan explicitly requires a historical note.
- **Previous dependency-environment/CI plan:** [`plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md`](plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md) is **DEFERRED at the completed Cluster-5 boundary**. Cluster 6 must not start while the reconciliation plan is active.
- **Agentic evaluation:** [`plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md`](plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md) is **DEFERRED** until the reconciliation closes and older continuations are re-reviewed against the modified source/contracts.
- **Current product status:** previously accepted Clusters 0–5 remain historical green evidence; Cluster 6 is not started.
- **Latest product-runtime validation point:** `bfdfd4257574f85cc3a2d094bf46a37ad6373dea` — `508 tests / OK`, `HEAD == origin/main`, clean worktree at that validation point.
- Later learning/audit/governance/plan commits do not create a newer product-runtime validation point by themselves.
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

Ali explicitly selected a temporary return from dedicated learning-only progression to normal learning-by-building so these source/design issues can be reconciled before they become deeper application dependencies.

## Current selected responsibility

The fresh plan must seek the **smallest sound architecture**, not maximal modeling and not minimal line count.

Desired responsibility direction:

```text
UNTRUSTED GITHUB FILE RESPONSE
→ GitHub-owned validation
→ strong exact repository text evidence
→ domain parsing / relational composition

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

## Audit lifecycle and current disposition

Canonical audit records keep stable paths directly under `audits/`. Lifecycle titles/classification are maintained through the three lifecycle indexes so existing audit-relative references remain valid.

### Active — current engineering inputs

- [`AUDIT-001`](audits/2026-08-01_AUDIT-001_exact-pr-file-acquisition-evidence-contract.md)
  - reassess validation-time versus durable exact-file fields while preserving exact acquisition rigor;
- [`AUDIT-006`](audits/2026-08-21_AUDIT-006_internal-evidence-type-strength-and-revalidation-boundaries.md)
  - strengthen exact internal evidence ownership before deleting downstream defensive checks;
- [`AUDIT-007`](audits/2026-08-22_AUDIT-007_uv-membership-proposition-and-lock-model-boundaries.md)
  - narrow the uv proposition, preserve required workspace scope, coordinate project facts, and evaluate one shared uv-specific structural lock model.

### Deferred — valid but not current implementation

- [`AUDIT-004`](audits/2026-08-16_AUDIT-004_uv-lock-resolution-satisfiability-evidence-boundary.md) — resolver/currentness evidence opportunity;
- [`AUDIT-005`](audits/2026-08-21_AUDIT-005_product-ai-agentic-orchestration-sequencing.md) — bounded agentic investigation/orchestration evaluation.

### Absorbed — not current implementation work

- [`AUDIT-002`](audits/2026-08-02_AUDIT-002_ci-dependency-exercise-proof-boundary.md) — material proof-strength correction absorbed by the newer Cluster-5 static-consumption/runtime-authority split; future runtime correlation remains separately gated;
- [`AUDIT-003`](audits/2026-08-10_AUDIT-003_post-conversation-c-product-decision-model.md) — reconciliation applied into stronger product-decision owners.

## Current plan status

Fresh plan sequence:

```text
R0  re-anchor contracts + freeze behavior
R1  strengthen exact repository-file evidence ownership
R2  one bounded uv-specific structural lock model
R3  preserve minimum real uv command/workspace scope
R4  narrow uv membership to explicit selected-root reachability
R5  rebind CI consumption to reconciled evidence
R6  pressure S001 / S011 / S005 + changed-case workspace transfer
R7  acceptance + audit disposition + deferred-plan re-review
```

No R1+ implementation has started yet.

## Pressure/proof anchors

- **S001:** real `uv sync --all-packages --group docs`; preserve the positive `docs → mkdocs-llmstxt → beautifulsoup4 → soupsieve` witness while representing enough workspace scope for honest no-witness semantics.
- **S011:** optional-extra `mlx` versus selected `dev`; keep source-established project environment membership separate from uv lock reachability.
- **S005:** tox/uv-mediated lock consumption; keep selection interpretation and lock reachability separate so the uv graph is not coupled to one direct command form.

## Continuation-critical guards

- `MEMORY.md` alone owns live continuation.
- The current reconciliation plan is the only active implementation route until its final STOP/REVIEW gate or Ali changes selection.
- Do not start old Cluster 6, the agentic evaluation, Tranche 2, or a separate source-clarity pass in parallel.
- Preserve GitHub/external trust-boundary validation; simplification must not weaken it.
- Relational/rebinding checks are not duplicate internal checks merely because they compare already-valid objects.
- Do not introduce `Trusted[T]`, `Validated[T]`, generic provenance frameworks, generic dependency graphs, or generic package-manager abstractions without new evidence and explicit admission.
- Do not build a complete uv environment interpreter merely to justify an over-broad name.
- `--all-packages` scope must be represented sufficiently before broad reliance on uv no-witness/`not_established` results.
- project/lock coherence/currentness and resolver/runtime evidence remain separate propositions.
- `uv workspace metadata` is not ordinary product runtime merely because uv recommends it for tooling; any execution on target repositories requires separate security/method admission.
- static dependency consumption != runtime execution/success != exact changed-version exercise.
- model output/agent proposal != authorization or trusted evidence.

## Immediate project action

Begin **R0 only** from [`plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`](plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md) when Ali explicitly says to start.

R0 is an inspect/classify/freeze step before source behavior changes:

```text
inspect affected source/tests
→ classify repeated validations by ownership
→ inventory duplicated uv structural rules
→ freeze the exact explicit-root reachability proposition
→ identify baseline focused tests/change surface
→ then review with Ali before or while entering the first bounded source modification
```

## Learning state

The project remains learning-oriented through implementation itself. For each bounded reconciliation step:

```text
real responsibility/problem
→ smallest blocking concept
→ Ali predicts/explains
→ inspect source/data flow
→ bounded change
→ inspect evidence/tests
→ separate observation from interpretation
→ diagnose/refine
→ preserve meaningful learning in code/working memory where useful
```

The dedicated learning-folder route is paused because the source being learned is now under active redesign. Resume, rewrite, or close that learning route only after R7 re-review establishes what remains accurate and useful.
