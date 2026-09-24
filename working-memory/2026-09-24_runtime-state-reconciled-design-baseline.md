# Runtime dependency-state proof — reconciled design baseline v1

**Date:** 2026-09-24  
**Status:** RECONCILED STARTING BASELINE; progressively maintained, not a final architecture/Build approval.  
**Purpose:** one compact, retrievable map of what UpgradePilot has already implemented, accepted, investigated, and still needs to design. This is a working-memory reconciliation, **not** a replacement for controlling specs/ADRs/plans, the existing investigation record, or `MEMORY.md`'s live-state authority.  
**Active detailed record:** [Effective package-manager semantics system design](2026-09-24_effective-package-manager-semantics-system-design.md).  
**Goal:** design and build the proper and smartest *coherent* effective package-manager semantics and runtime dependency-state proof capability for real UpgradePilot cases—not an isolated flag classifier, and not artificial minimality.

## 1. Established product/evidence ladder

```text
exact dependency/version and source
→ exact selected dependency environment and static consumption
→ exact command/step runtime correlation and reported success
→ effective package-manager semantics + relevant environment/destination relation
→ exact proposed-version state at a justified observation boundary
→ separately proven same-version use by a later exercise, if required
→ separately evaluated behavior / maintainer-action permission
```

Each arrow needs independently justified evidence. Static declaration != execution; correlated success != installed version; state at command completion != persistence; package presence != exact version used by a later test; green CI != compatibility or maintainer permission. A command-specific defeater defeats *that inference*, not proof that the package is absent.

## 2. Status map — reuse before designing anything new

| Status | Already-owned responsibility / finding | Primary existing owner |
| --- | --- | --- |
| IMPLEMENTED, bounded | Exact dependency source and selected environment; static pip/uv consumption; static direct changed-package invocation ordered after consumption. | `src/upgradepilot/dependency/`, `src/upgradepilot/ci/workflow_commands.py`, `ci/static_command_order.py`, `ci/dependency_exercise.py` and their tests. |
| IMPLEMENTED, bounded | Exact-head/run-attempt/job/step correlation and eligible runtime-success strengthening for identified static occurrences. Not exact package-state proof. | `src/upgradepilot/ci/workflow_runtime_correlation.py`, `ci/runtime_strengthening.py`, `ci/dependency_exercise.py` and their tests. |
| ACCEPTED CONCEPTUAL CONTRACT (B1–B5); NOT IMPLEMENTED as a coherent effective-semantics/state producer | Command-local eligibility is only an intermediate filter. Effective semantics must resolve each *material, exact-proposition-relative* dimension as `resolved_non_defeating`, `resolved_defeating`, or `unresolved`. A known defeater prevents using this command as a state-producing witness; unknown required dimensions fail closed. | [Cycle-1 B1–B5 investigation](2026-09-21_runtime-install-command-semantic-eligibility.md). |
| ACCEPTED PROOF STRATEGY; NO GRAPH ENGINE SELECTED | Bottom-up/backward, demand-driven proof from the exact process and semantic dimension; top-down tracing only as needed to understand scope/propagation/overrides and find missing edges. Graphs are explanatory evidence relationships, not selected runtime data structures/CFG/SSA. | [B4 environment/data-flow note — graph examples and backward refinement](2026-09-22_b4-environment-evidence-data-flow-learning.md). |
| INVESTIGATED, NOT BUILT | Direct target-owned installed-state witnesses (`pip inspect`, targeted `importlib.metadata.version`, inventories, uv inspection) and separately qualified installer reports/logs; exact run/job/environment/observation-time provenance and retention. | [F6 feasibility/alternatives](2026-09-21_f6-post-install-package-state-feasibility.md). |
| ALREADY IDENTIFIED DOWNSTREAM GAP, NOT A NEW SUBSYSTEM | Binding an observed version to a later exercise needs matching environment/interpreter, proven ordering and no unaccounted material intervening mutation. Existing CI direct-exercise and runtime-correlation axes are reusable but do not prove exact-version use. | [B2 dependency/CI proof ladder](../plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md), [F6 §7–9](2026-09-21_f6-post-install-package-state-feasibility.md). |

## 3. Previously established semantic surface

Material pip/uv families: mutation/sync (`--dry-run`, `--no-sync`, `PIP_DRY_RUN`, `UV_NO_SYNC`); relevant package/group/root exclusions; retargeting (`--target`, `--user`, `--root`, `--prefix`, uv environment/project selection); invocation overlays/version overrides; configuration-loading and ambient `PIP_*`/`UV_*`; environment/interpreter/destination identity. Relevance is relative to the **exact changed-package state proposition**. Later mutation belongs to the temporal handoff to a later observation/exercise, not to command-completion semantics. [Cycle-1 investigation](2026-09-21_runtime-install-command-semantic-eligibility.md).

**Accepted B4 reasoning model:** for each required dimension, start at the exact pip/uv process; use decisive process/CLI evidence if established, else trace shell-local assignments → applicable step environment → positively proven same-job `GITHUB_ENV` updates and job/workflow environment → applicable observable manager configuration, only as far backward as needed. The most recent *proven applicable* write matters; a later potentially relevant but execution-unresolved write cannot simply be ignored. Higher-precedence decisive evidence may render lower-precedence unknowns irrelevant **for that dimension only**. Missing/unproved edges remain `unresolved`. [B4 graph, write, precedence and backward analysis](2026-09-22_b4-environment-evidence-data-flow-learning.md).

**Accepted owner split:** GitHub workflow/shell evidence owns declarations, source order, scope, propagation and exact-process value relationships; dependency/pip/uv owns manager semantics; CI/state-proof composition owns runtime correlation and proof conclusions. Do not turn Tree-sitter or generic runtime correlation into the pip/uv semantic owner. [ADR-0008](../docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md), [Cycle-1](2026-09-21_runtime-install-command-semantic-eligibility.md).

**Accepted B5 command-derived claim:** exact proposed dependency/source + exact relevant environment + static consumption occurrence + admitted command-local semantics + fully non-defeating effective dimensions + exact successful runtime occurrence + the applicable manager-operation guarantee may establish **requirement satisfied/present at that command-completion boundary**. This does not prove fresh installation, selected artifact, subsequent persistence/use, behavioral compatibility, or any maintainer action. [Cycle-1 B5](2026-09-21_runtime-install-command-semantic-eligibility.md).

## 4. Existing investigation decision and current route

**Previous Cycle-1 B6:** rejected only incomplete approaches (visible flag rules alone, declarative `env` alone, or artificial explicit fixtures) and selected **no partial Cycle-1 Build**. This did **not** reject designing/building a coherent, broader capability. [Cycle-1 B6](2026-09-21_runtime-install-command-semantic-eligibility.md).

**Current user direction:** seek the proper and smartest system, rather than treating the rejected partial patch as a reason to stop building indefinitely. The [runtime-state master plan](../plans/RUNTIME_DEPENDENCY_STATE_PROOF_COMPLETION_PLAN.md) retains its historical conditional Cycle-2 / action-criticality gate; it needs an explicit, owner-correct reconciliation **before** any materially changed Build sequence. The [parent action-relative investigation](2026-09-24_runtime-package-state-decision-criticality.md) is paused, not discarded. [Current detailed design record](2026-09-24_effective-package-manager-semantics-system-design.md) contains an unapproved R2 *candidate* that allows command-derived proof and independent direct installed-state proof; do not promote that candidate to accepted architecture just by repeating it here.

## 5. Genuine open design and proof questions (R2 → R3)

1. **Supported evidence boundary:** which command, workflow/job/step `env`, shell assignment/export, positively proven `GITHUB_ENV` write/propagation, manager config, and target/interpreter relation shapes can establish effective values in *normal real* pip/uv paths? Specify opaque/dynamic/external cases that remain unresolved **only when material**.
2. **Backward proof realization:** how do we preserve the necessary process-near value, scope/order, precedence, provenance and unresolved edges without duplicating the existing parser, CI correlator, or building an unneeded general graph/runner simulator? Resolve the current gap where parsed command occurrences and workflow IR do not yet supply the needed environment facts.
3. **Proof-route architecture:** determine whether command-derived completion-state inference and independent target-owned installed-state observations are separate typed paths composed into a common exact-state proposition, and how installer reports remain distinct from observed inventory. Preserve the **different observation-time claims**.
4. **Real applicability and tests:** pressure-test the chosen architecture on real normal pip/uv cases and close defeaters; establish exact process/step identity and actual run evidence. A later-in-step command must not inherit the step-success proof currently admitted only for a sole/first eligible command.
5. **Downstream integration:** retain data needed for future version-to-exercise binding, but do not duplicate the already implemented static order/runtime correlation or silently claim later persistence/behavior. Reconcile the master-plan sequence and action-relative value explicitly before Build.

**Next focused work:** review the already-recorded R2 candidate against these gaps and source truth; decide the coherent *supported evidence and proof-route boundary*, then R3 designs concrete types, owners, and data flow. No product code, tests, stable specifications, ADRs, or plan semantics were changed by this reconciliation.

## 6. Progressive-update rule

This file is the **compact reconciliation/index**, not a competing specification or a second live-status owner. Update its *status map, open questions and reference links* when evidence or an owner-approved decision materially changes them; keep long investigation, implementation, proof, and teaching details in the owning work record/source/test/plan. Label each addition `IMPLEMENTED`, `ACCEPTED`, `CANDIDATE`, `DEFERRED`, or `UNRESOLVED`, with its owner/proof/claim limit; mark superseded claims rather than silently rewriting history. Promote durable decisions to their actual spec/ADR/plan owner when approved. Re-check `MEMORY.md` before resuming later.

UP-SKILL:upgradepilot-planning-design  
UP-SKILL:upgradepilot-learning-by-doing  
UP-SKILL:upgradepilot-working-memory
