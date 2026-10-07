# ADR-0012 — Canonical Investigation Workspace and recovery boundary

**Status:** Proposed for Ali's review; the B2 composition direction is already accepted, but this completed method and recovery boundary are not yet an accepted ADR or implemented capability.
**Date:** 2026-10-08
**Responsibility:** One evolving canonical investigation contract around native producers/evaluators, with revision-bound interaction, consumer projections, replacement migration and durable recovery.
**Requirements:** [Charter §6](../../PROJECT_CHARTER.md), [Core §§3–6.3](../specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md), [Product Decision Model](../specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md), [Maintainer Action Synthesis](../specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md), [Security](../../SECURITY.md).
**Execution coordination:** [Workspace/interface design plan](../../plans/INVESTIGATION_WORKSPACE_AND_INVESTIGATOR_INTERFACE_DESIGN_PLAN.md).
**Design and pressure evidence:** [single design-cycle record](../../working-memory/2026-10-07_investigation-workspace-and-investigator-interface-design_lbd-cycle.md), including its proposed Core §6.4 recovery semantics. That semantic delta requires review/promotion to its Core owner; this ADR does not silently amend the specification.

## Context

The current [PublicPullRequestInvestigation](../../src/upgradepilot/investigation.py) is a frozen result of a fixed acquisition/evaluation sequence. Native CI/package-manager, upstream, target and impact owners already establish distinct bounded facts and assessments. [ADR-0010](ADR-0010-package-manager-semantic-facts-and-runtime-dependency-state-composition.md) and [ADR-0011](ADR-0011-explicit-source-association-bases-and-proposal-boundary.md) protect those meanings.

Adaptive investigation requires additional cross-domain ownership: evolving target-bound state, bounded discovery before candidates, proposal/evaluation and request/observation histories, material premise bindings, bounded context, candidate refinement and adequacy authority. The saved report deliberately omits some content, method identity and operation history; it cannot supply canonical continuation. Adding all this to a frozen result or scattering it among uncoordinated owners obscures state validity and recovery.

## Proposed decision

Use a **distinct composed/evolving Investigation Workspace** as the product's canonical logical investigation state. Compose focused records/services around native records, rather than requiring one giant class or a universal evidence hierarchy. The Workspace owns investigation identity, cross-domain relationships, lifecycle and recovery; native owners retain factual/semantic authority and synthesis retains action permission.

Each revision binds the investigation lineage to the exact repository/PR/base/head/dependency transition. A host-controlled ingestion/publication boundary performs identity, reference, scope and allowed-effect checks, records problems without fabricating observations, and advances canonical state with triggering-record and predecessor/successor links. This boundary is a logical method, not an event-store or transaction-technology decision.

The update path is:

```text
exact native evidence / attributed proposal or request
→ host structural/reference/target admission
→ admitted capability execution and observation/problem, where requested
→ result identity/meaning validation
→ admitted domain or adequacy evaluation, where applicable
→ canonical revision with retained basis/history and explicit gaps
→ one-way consumer projections
```

Native facts need not pass through a model proposal or redundant generic evaluation. Unsupported evaluation remains an explicit attempt outcome when no admitted owner exists; an actual native evaluator's bounded unresolved/unsupported-comparison result retains its own meaning. Pending evaluation can be represented without pretending it already occurred.

### Interaction and authority

- A bounded discovery objective can justify pre-candidate acquisition with exact scope, relevance and discovery-coverage limits. Proposition-directed follow-up instead cites a genuine material unresolved/conflicted proposition and discriminator. Neither basis authorizes execution by itself.
- Semantic/candidate proposals, structural admission, host request admission, execution attempts, observations/problems and evaluator-owned assessments are separate responsibilities. The host cannot promote admitted proposals into truth or requests into maintainer actions.
- Available, delivered, observably examined/used, cited, evaluated support and sufficient are separate relationships. Bounded omission disclosure preserves known addressability and content/reference/retention limits without promising an exhaustive relevance inventory.
- Procedural termination and attributed stopping proposals cannot establish canonical adequacy. Only an admitted owner/method can establish a current stop/continue assessment; absent that method, preserve unsupported evaluation and open obligations. No particular evaluator or second model is selected.

### Validity and knowledge change

Preserve original target/revision and material basis for every proposal, view, request, observation and evaluation. A delayed same-target result may enter a later revision after its target, request meaning, scope and premises are validated. Revision inequality alone is not staleness. Target or material premise changes require explicit validation/rebinding or historical/stale treatment.

Counterevidence and mechanism refinement preserve prior assessments/candidates and trigger affected successor evaluations through their owners. New evidence or newly feasible critical investigation can invalidate an old adequacy basis without changing head SHA. Exact duplicate delivery does not become independent support; inconsistent identity/content is an ingestion problem before semantic conflict evaluation.

### Projections and durable recovery

Investigator, evaluator, synthesis and report consume explicit one-way Workspace projections. Projection cannot strengthen evidence, recompute competing truth or invent omitted lifecycle state. Evaluator selection must include owner-relevant counterevidence/unknowns rather than inheriting proposer citations as its whole boundary.

**Durable canonical Workspace recovery is an intended product responsibility.** Restore a declared coherent historical checkpoint with exact identity, material native content/recovery limits, method/basis/history and unfinished obligations. The proposed Core §6.4 delta owns the minimum semantics and fault outcomes. Recovery is offline; explicit continuation validates current target/premise/method/authorization bindings before new activity. Missing material state blocks affected continuation, not inspection of unaffected history.

A saved report is insufficient for this boundary. A reference/digest is not retained content; interruption is not a negative observation; historical admission is not present execution permission. Recovery does not promise hidden model-state restoration, deterministic model rerunning or exactly-once capability effects. Storage technology, checkpoint frequency, retention period and implementation activation remain open.

### Replacement-oriented migration

Migrate the normal product path to native producers/evaluators → Workspace → consumer projections. Do not maintain independent old/new acquisition or interpretation paths. A temporary `PublicPullRequestInvestigation` projection is permitted only for an identified caller, compatibility obligation or proof need, derived one-way from Workspace with explicit limits and removal/reassessment trigger.

Retirement requires consumer cutover, preserved native semantic regressions, proof of the admitted lifecycle/recovery boundary, and no remaining independent legacy obligation. Migrate meaningful tests to native/Workspace consumers; remove obsolete snapshot plumbing and adapter-only tests when their purpose ends. An explicitly staged Build can leave named obligations incomplete, but cannot redefine the full target as the smaller delivered slice.

## Alternatives and trade-offs

Extending the frozen result would reuse familiar callers, but adding adaptive lifecycle/history effectively repurposes it and mixes final-result with evolving-state semantics. A smaller distributed state owner reduces apparent initial migration cost but recreates the same lifecycle/revision/recovery responsibilities indirectly. Both were rejected in B2; focused modular internals remain appropriate.

Report-only retention is cheaper but cannot recover the identified investigation consumer's missing state. Full execution replay imposes substantially greater capture/compatibility/privacy obligations without establishing deterministic model/external behavior. Bounded canonical checkpoint recovery is the adequate middle responsibility.

The selected composition adds identity, retention, projection and invalidation work. It reduces duplicate truth paths and makes gaps inspectable, but does not solve semantic accuracy, candidate-discovery completeness, independent usefulness or adequacy evaluation. Overly generic records, implicit re-evaluation and incomplete material retention are material failure risks, covered by the plan's proof obligations.

## Non-selections, reversal and acceptance boundary

No Python class/module/schema layout, mutability choice, database/SQLite/file/event-store mechanism, framework, model, agent topology, discovery policy, capability catalog, semantic/adequacy evaluation method, broader execution authority or action default is selected. Security and existing semantic owners remain controlling.

Before cutover, reversal can stop the Workspace adoption without changing native meanings or converting reports into checkpoints. After cutover, reverting to the old snapshot requires a deliberate capability/retention decision: it would otherwise lose newly admitted lifecycle/recovery state. Keep evidence history recoverable under its contract rather than silently downgrading it during rollback.

Reassess if a native owner already satisfies an alleged new responsibility, a projection requires recomputing domain truth, a real compatibility obligation contradicts retirement, material retained context is missing, or valid variation cannot be represented without hidden authority promotion. Reopen the proper semantic/design owner before widening the method.

Acceptance requires Ali's review of this method and the proposed Core recovery delta. Executable adoption then needs a separately admitted Build with canonical-path native regression proof, request/evaluation/adequacy and variation tests, delayed/stale/conflicting/duplicate results, recovery interruption/failure/continuation proof, and consumer cutover/retirement evidence. This proposal and its conceptual walkthroughs establish no implemented Workspace, durability, model quality, compatibility or learner mastery.
