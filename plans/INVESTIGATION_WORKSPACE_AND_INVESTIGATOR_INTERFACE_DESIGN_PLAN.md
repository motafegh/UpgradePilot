# Investigation Workspace and Investigator-interface Design Plan

## Responsibility and outcome

Design the product composition and update boundary between native evidence producers, an Investigator, independent evaluation and downstream synthesis. The outcome is a reviewable ownership/interface proposal and its proof/migration obligations, not an executable Investigator or another source-only prompt experiment. Live selection and cycle position belong only in [MEMORY.md](../MEMORY.md).

The relevant product responsibility is evidence-backed dependency-update investigation for public Python maintainers. This cycle covers the shared knowledge and interface boundary through which existing and foreseeable investigation mechanisms can serve that responsibility. Acquisition breadth, semantic accuracy and recommendation usefulness still require later implementation and evaluation; the design must not imply that today's two impact mechanisms exhaust the product.

## Controlling owners and entry evidence

- [Core §§3–6.3](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md): evidence/trust, representation, retention and authority invariants.
- [Product Decision Model §§5–14](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md): proposals, applicability, coverage, investigation, feedback, lineage and stopping semantics.
- [ADR-0010](../docs/architecture/ADR-0010-package-manager-semantic-facts-and-runtime-dependency-state-composition.md) and [ADR-0011](../docs/architecture/ADR-0011-explicit-source-association-bases-and-proposal-boundary.md): domain-owned mechanical facts and distinct source-association/proposal boundaries.
- [Maintainer Action Synthesis specification](../docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md), [Charter](../PROJECT_CHARTER.md) and [Security](../SECURITY.md): controlled recommendation/execution, product scope and untrusted-content boundaries.
- [Minimum Useful Generality](../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md): real cases pressure the design; they do not supply case-specific product answers.
- [AUDIT-010](../audits/2026-10-07_AUDIT-010_hybrid-investigation-architecture-compatibility.md), main checkpoint `1dca28855c091bc99805c7b39b6ea513ea5235e5`: existing hybrid compatibility and the genuine workspace/interface delta. Selecting the hybrid direction alone requires no restatement ADR or specification amendment.
- Research checkpoint `74835751cf53171ec31ce0fc01e505aaf4fae8e0`: [two-case interpretation review](https://github.com/motafegh/UpgradePilot/blob/74835751cf53171ec31ce0fc01e505aaf4fae8e0/working-memory/evidence/2026-10-07-broader-agency-evidence-interface/README.md). Mechanically complete known-case reports require semantic revision despite relevant supplied evidence. Attribution, composition, applicability and recommendation support remain separate problems; this is neither intrinsic model incapacity nor a Fixed-versus-Agent result.
- Completed research checkpoint `cde0ea9906fa37e4184962d0ba65577e4d62396e`: [repaired known-case Contract-2 comparison](https://github.com/motafegh/UpgradePilot/blob/cde0ea9906fa37e4184962d0ba65577e4d62396e/working-memory/evidence/2026-10-07-broader-agency-contract2-comparison/README.md) and its [interface requirements for main](https://github.com/motafegh/UpgradePilot/blob/cde0ea9906fa37e4184962d0ba65577e4d62396e/working-memory/evidence/2026-10-07-broader-agency-contract2-comparison/interface-requirements-for-main.md). Both Gemma12 and Qwen35 pass fresh Contract-2 qualification; all eight Fixed/Agent final reports validate mechanically while all eight require semantic revision. Agent used less input/elapsed time in all four matched pairs, but discovery/interpretation advantages vary and no policy winner is established. This completed comparison is non-controlling design pressure only; main retains product Workspace/interface ownership.
- [Operating Guide §4.1 and §4.4](../OPERATING_GUIDE.md): existing implementation must earn retention, and bounded increments must remain product-faithful. For this responsibility Ali explicitly prefers coherent-target-first design and replacement-oriented migration over accumulating parallel “minimal” layers; staged implementation must converge directly on the accepted target rather than redefining it downward for convenience.

Inspect the native producer-to-consumer paths below before choosing a representation. Prior test results are dated evidence, not proof of a new design or current runtime.

## Questions the design must resolve

Names below describe responsibilities, not selected classes, modules or schema fields.

| Design area | Required decision/output | Current anchor or constraint |
| --- | --- | --- |
| Workspace composition and ownership | Define the selected distinct Workspace as the canonical owner of evolving investigation identity, native-record relationships, proposals, assessments, capabilities and history while keeping composition separate from domain interpretation. | The design selects a distinct composed/evolving Workspace. [PublicPullRequestInvestigation](../src/upgradepilot/investigation.py) remains current implementation evidence/migration input, not a promised permanent parallel contract. |
| Native deterministic records | Define retention and reference rules for exact domain records/content, available provenance, producer limitations and explicitly missing content. Identify any genuinely needed adapters and the earliest sufficient owner. Make the identity/digest basis explicit when later host annotations are attached so consumers can distinguish the original native payload from annotation/enrichment lineage. | Preserve CI consumption/execution, package-manager facts, scoped command-completion state, dependency contexts and upstream authority without flattening their meanings. Host annotations must not silently redefine an existing record identity. |
| Evidence, proposals and evaluated propositions | Define distinguishable conceptual contracts and who may produce/admit each; prevent a proposal, valid JSON or citation from writing an established assessment. Keep source version, target binding, activation, capture authority and observation scope as separately evaluable propositions when they are materially independent. | [PropositionAssessment](../src/upgradepilot/impact/applicability.py) depends on its mechanism owner; it is not a general semantic validator. A correct source fact does not establish target binding or activation. |
| Typed evidence, use/derivation lineage and missing-premise links | Bind references to native record kind, exact identity/scope and the specific proposition they support or fail to close. Distinguish evidence availability, delivery/current visibility, reference/examination/use, citation, evaluated support and sufficiency where those states are observable; do not retroactively credit unexamined evidence to a conclusion. Preserve derivation lineage when one evidence record/result is produced from other evidence and a named method. Represent required-but-unavailable evidence separately from a performed negative observation; scoped negative observations must not become global absence or safety. | Coverage axes, source versus executed revision, temporal/environment context and absence scope remain explicit. Workspace/corpus availability is not proof of model examination, use or support. |
| Investigator capability/request interface | Define its input view, offered capability descriptions, proposed requests and no-request/unresolved outcomes; locate host-owned binding, eligibility and admission. Accommodate separately admitted discovery and proposition-relative follow-up without selecting a policy. | [Planner boundary](../experiments/evidence_gap_planner_model_boundary.py) and [action admission](../experiments/evidence_gap_action_admission.py) are narrow experiment evidence, not a product-wide interface to copy unchanged. |
| Proposal admission and independent evaluation | Separate structural/reference/request admission from source support, applicability and action evaluation. Specify rejection, unsupported evaluation and genuine conflict; evaluation-method selection can remain open. Treat source-version association, target binding, activation and capture authority as distinct obligations rather than letting one mechanically valid reference satisfy all of them. | Literal reconstruction, delivery and type checks do not establish entailment. A second model is not independent source corroboration. |
| Observation ingestion and knowledge update | Specify who records capability results/failures, validates their identity/meaning, invokes domain evaluators and advances the Workspace view; describe ordering, stale-input handling and failure preservation. Represent failed reads, empty reads/files, scoped zero-result searches and other typed host/trial observations honestly; an empty or failed observation is not fabricated source content or global absence. | Successful execution can yield unusable evidence. [Transition traces](../experiments/evidence_gap_investigation_transition.py) illustrate an explicit before/result/after boundary without defining the general product method. |
| Candidate/proposition lineage | Preserve identity, revision/refinement relationships, triggering observations and assessment changes. Identify which changes invalidate earlier evaluations rather than silently overwriting them. | Product Decision Model §12 owns the semantics; no event-sourcing technology is implied. |
| Current context and recoverable history | Define a bounded Investigator view and what remains available outside it, including source content, request/result/evaluation lineage and method identity where available. State recovery limits and context omissions explicitly. Preserve procedural/stage completion separately from investigation adequacy and stopping justification; a completed stage/report cannot imply the required investigation was sufficient. | Historically delivered evidence, currently supplied evidence and actual model understanding are different. No universal raw capture, storage technology or full replay promise is selected. |
| Product/result/report relationships | Define the replacement-oriented migration from today's fixed investigation result/report pipeline to the canonical Workspace and explicit Workspace-owned Investigator/evaluator/synthesis/report projections. Any temporary `PublicPullRequestInvestigation` adapter must be derived from the canonical Workspace, have an independently justified compatibility/proof purpose and a removal/reassessment trigger. Keep saved-report versus future recoverable-investigation obligations separate. | Current report projection consumes `PublicPullRequestInvestigation`, but current consumers/tests establish migration pressure rather than permanent retention authority. Saved-report handling cannot be reinterpreted as complete resumable state or as proof that a recommendation is adequately supported. |

## Completed research pressure to carry through the interface design

The completed `cde0ea99` comparison does not reopen the ownership trace and does not supply a product contract. It sharpens the following interface responsibilities that must be testable in the selected design:

1. Preserve available → delivered/currently visible → referenced/examined/used → cited → evaluated support → sufficient as distinguishable states where observable; available-but-unexamined evidence remains available, not absent and not retroactive support.
2. Preserve source version, target binding, activation, capture authority and scope as distinct propositions. Upstream/reference truth does not automatically establish the target's installed/bound runtime state.
3. Preserve unknowns and scoped negative observations without upgrading them to global absence, harmlessness or safety. Named decision-critical unknowns remain consequential for synthesis.
4. Preserve procedural/stage/report completion separately from investigation adequacy, stopping justification and remaining semantic responsibilities.
5. Represent failed reads, empty reads/files, zero-result searches and other typed observations directly rather than inventing source content or coercing everything into a citation-shaped artifact.
6. Keep mechanical report validity/completeness separate from recommendation admission; a valid report can still be semantically unsupported for the proposed action.
7. Make record identity/hash/digest basis explicit when host annotations are attached later. Consumers must be able to tell whether an identifier covers the original native payload, an annotated/enriched form, or a successor record.

These are interface obligations, not selected fields, classes, storage, deterministic tools, critics, frameworks or agent topology.

## Selected structural direction and migration rule

The product design uses a **distinct composed/evolving Investigation Workspace as the canonical investigation state/contract**. It is a composition/lifecycle owner, not a replacement for native domain truth owners or maintainer-action authority.

`PublicPullRequestInvestigation` is not selected as a permanent parallel architecture or mandatory compatibility boundary. It is existing implementation to migrate from. Later Build may temporarily retain/project it only when a concrete caller, regression-proof need or real compatibility obligation independently earns that retention. Any transitional adapter must preserve native semantics, derive one-way from the canonical Workspace rather than run a second truth path, and have an explicit removal/reassessment trigger.

A smaller top-level state/update owner is rejected as a competing architecture. Its useful lesson survives only as **modular internal decomposition**: the canonical Workspace should compose focused identity/reference/proposal/request-observation/assessment/lineage/adequacy responsibilities rather than become one giant class.

The migration is **replacement-oriented, not coexistence-oriented**. Design the coherent final responsibility first; implementation may be staged for proof/complexity control, but each slice must converge directly on that accepted target. Do not create a deliberately reduced “starter Workspace” or stack temporary mini-architectures that each pass locally while leaving a duplicated or incomplete end-to-end product. Migration safety and reversibility protect correctness; they do not independently authorize legacy retention.

## Canonical Workspace contract design obligations

The reviewed contract must preserve the following responsibilities without requiring a universal evidence wrapper or a global confidence/status field:

- exact investigation lineage plus revision-bound repository/PR/base/head/dependency-transition identity;
- native-record bindings that preserve owner/type/identity/scope/provenance/retention and original-payload identity basis;
- host annotations as separate lineage rather than mutation of native evidence identity;
- bounded Investigator views that record what was delivered and what material available content was omitted, without pretending delivery equals examination;
- mechanism-run records that preserve method/model identity, procedural outcome and observable use/examination receipts while allowing use to remain unknown;
- semantic/candidate proposals plus separate structural proposal admission;
- explicit evaluation attempts whose outcomes distinguish evaluated, unsupported, failed and stale, with a domain assessment only when an admitted evaluator actually evaluates the proposition;
- proposition-relative investigation needs and discriminating targets;
- capability requests, host admission/rejection, execution attempts, actual observations and distinct attempt problems/failures;
- candidate/proposition refinement/supersession lineage and affected assessment history;
- investigation stop/adequacy assessment separate from stage/report completion and separate from maintainer-action sufficiency;
- one-way consumer projections for Investigator, evaluator, synthesis, report, future recovery and any temporary legacy compatibility surface.

Evidence-use states are relational rather than one lifecycle enum: Workspace retention establishes availability; a consumer view establishes delivery; an observable mechanism receipt may establish examination/use; a proposal establishes citation; an evaluator establishes assessed support/counterevidence; proposition-relative coverage or action-relative synthesis owns sufficiency. The Workspace does not own a universal `sufficient` flag.

Evaluator input must not be limited to proposer citations. The evaluator owner must receive the relevant evidence/counterevidence/unknown boundary needed for the exact proposition, or explicitly record its coverage limitation. If no admitted semantic evaluator exists, preserve an unsupported evaluation attempt; do not fabricate an `unresolved` authoritative assessment merely to fill the Workspace.

Every proposal/request/evaluation/view/attempt is revision-bound. A later target change makes earlier results stale for the current target unless an admitted owner explicitly revalidates/rebinds them. Stale history is retained; it is not silently rewritten onto the new head.

## Consumer projection obligations

- **Investigator projection:** exact target/workspace revision, relevant native/observation records at their admitted retention strength, current proposals/assessments/open investigation needs, capability descriptors and material omission manifest. It has no truth/action authority.
- **Evaluator projection:** exact proposition/proposal/candidate, target revision, proposer citations plus owner-selected relevant evidence/counterevidence/unknowns, scope/association/use/coverage information and evaluator method identity. It must not inherit the proposer's evidence selection as the whole evidence boundary.
- **Synthesis projection:** exact decision identity, domain-owned evaluated states, residual uncertainty/conflicts, material failed/unsupported investigation/evaluation outcomes, stopping state and provenance/coverage limits. Raw proposals cannot satisfy action permission.
- **Report projection:** synthesis/action result plus material evidence links/findings/unknowns/limitations and projection/version/retention metadata. It is not canonical or resumable state.
- **Recovery projection/checkpoint, only if persistence/resume is later admitted:** enough canonical state/history/content/method identity to satisfy the explicitly admitted continuation contract. Saved report prose is not a substitute.
- **Temporary legacy snapshot projection, only if independently justified:** one-way projection from the canonical Workspace; never a second acquisition/orchestration path or permanent source of truth.

## Replacement-oriented migration completion conditions

Migration is not complete merely because a Workspace type exists. Completion requires, where applicable:

1. normal investigation constructs/advances the Workspace directly from admitted native producers/evaluators;
2. every currently admitted product/report fact has a native binding or intentional Workspace projection with no silent authority change;
3. CLI/orchestration, maintainer synthesis and report generation consume Workspace-owned projections;
4. any remaining legacy snapshot adapter is one-way from the Workspace and has a concrete independent compatibility/proof owner plus removal/reassessment trigger;
5. current deterministic/report regression behavior and representative cases pass through the Workspace path, with additional proof for proposal admission versus support, unsupported evaluation, failed/empty observations, evidence-use distinctions and stale-state handling;
6. domain facts/evaluations have one authoritative owner and the Workspace/projections do not recompute competing truth;
7. saved-report reopening remains an offline projection operation, while any admitted resumable investigation uses a Workspace recovery contract;
8. obsolete `PublicPullRequestInvestigation` normal-path plumbing is removed when no independent compatibility/external obligation remains; a surviving real compatibility adapter is explicitly bounded/versioned;
9. active documentation/tests teach the Workspace as the canonical investigation boundary after cutover.

## Design sequence and deliverables

1. Reconcile the accepted architecture and research delta, initialize the single cycle record, and orient Ali to the proposed responsibility before consequential design selection. Apply the canonical learning gates proportionately under root AGENTS.md.
2. Trace native producer → composition → Investigator/validator → synthesis/report for representative paths. Produce a compact ownership/retention ledger, including existing sufficient owners and genuine missing owners.
3. Compare the credible workspace-composition alternatives and establish the distinct canonical Workspace/replacement-oriented migration direction before contract design.
4. Define the canonical Workspace input/output/lifecycle contract: native binding, proposals/admission, evaluation including unsupported outcomes, request/admission/attempt/observation/problem, lineage/staleness, bounded views, investigation adequacy/stopping, consumer projections and migration completion. Demonstrate both an acquisition flow and a semantic-proposal flow against real pressure cases rather than synthetic happy paths alone.
5. Walk the complete contract through the broader cases below. Resolve boundary defects and explicitly preserve questions that depend on semantic evaluation methods or later mechanism experiments.
6. If the consequential cross-module composition/update/interface method remains justified after contract design and case walkthroughs, prepare a focused ADR for review with alternatives, trade-offs, reversal and migration/proof consequences. Do not mark it accepted from the assistant's own recommendation. Amend a specification only if a genuinely new or changed stable semantic responsibility is identified; do not copy accepted semantics into a new owner.
7. Verify the design's source/owner alignment and document integrity, teach the resulting decisions and limitations, then close or truthfully preserve unresolved design/ownership gaps. Hand off implementation requirements without starting Build.

The cycle record owns dated reasoning, walkthrough results and learning. A plan coordinates the work; a justified ADR owns any accepted structural method. Avoid creating a second permanent design owner merely to store the same contract.

## Review cases and proof boundary

| Case/variation | What the design walkthrough must demonstrate |
| --- | --- |
| HTTPX supplied evidence, reference adapter text and illustrative Docker capture | Retain the useful removal fact while distinguishing source/reference version, target installed binding, activation and capture authority; illustrative success cannot become current pipeline compatibility. Unused workflow/constraint evidence stays recoverable. Evidence merely present in the corpus/workspace cannot be credited as examined or supporting unless the trace establishes that use. Scoped zero observations cannot establish global absence. |
| Pytest release facts cited to a target-pin diff | A valid/delivered reference can fail support. Correct summary assertions outside a claims list also require attribution/evaluation; captured success cannot establish installed/executed pytest or unconditional proceed. A completed stage/report can still leave feasible decision-critical investigation undone. |
| Native command-completion witness versus unresolved environment/conditional selection | Preserve the existing sufficient domain proof and unsupported branches. The Investigator cannot reclassify command completion as later exercise or compatibility, or discard markers/extras to manufacture reachability. |
| Support-drop claim followed by an exact target declaration, and unavailable/conflicting follow-up | An observation can refine a specific proposition through its evaluator; an acquisition failure, empty result, scoped negative evidence and semantic conflict remain distinct. |
| Candidate refinement and stale proposal | Show the original candidate, triggering observation, successor and affected evaluations. A request based on an earlier state cannot silently apply to a changed PR/scope/capability state. Later annotations must not silently alter the identity basis of the original retained observation. |
| Bounded context, saved report and incomplete retained history | Distinguish omission from source absence and explain what can be recovered. Offline report opening stays offline and cannot claim continuation/replay from missing inputs. Report validity/completeness cannot authorize a recommendation. The canonical Workspace must be sufficient for its admitted recovery contract rather than depending on an obsolete fixed-snapshot path. |

HTTPX/pytest are inspected known-case research evidence, not unseen acceptance tests or a product oracle. Existing product paths supply different evidence strengths and failure variations. Use the same interface/ownership reasoning across them; reject a design that works only by case-specific assumptions.

Design verification is source/owner tracing, contract/flow walkthroughs and documentation checks. It establishes a reviewed design proposal and its unresolved boundaries, not implemented recovery, automatic semantic validation, model quality, target compatibility, independent usefulness or a policy winner. Product/model/installed/hosted tests are unnecessary for documentation-only preparation; later Build owns executable proof.

## Modification boundary, completion and stop line

Allowed: this plan, the cycle record, necessary live-memory/audit-lifecycle reconciliation, and a justified focused architecture proposal or real specification delta for review. Do not edit product/experiment source, tests, prompts, schemas, defaults or runtime configuration in this cycle.

Completion requires the ten design areas to have explicit ownership/interface decisions or precisely bounded unresolved method-dependent questions; review cases must expose no unexplained authority promotion or retention loss. A missing central composition/update/admission decision prevents closure as a complete design. Preserve learning gaps honestly in E.

Do not select a framework/LangGraph, model, single/multiple agents, interpretation stages, persistence technology, concrete Investigator policy, exact expanded tool set or broader execution authority. Retain `source-only-api-change-v2` and its frozen reviewed FAILED/REVISE baseline; this cycle neither disposes of it nor promotes it as the workspace architecture.

Main's workspace design and the independent repaired Fixed-versus-Agent research must converge through a later explicit integration decision: map the selected mechanism to the reviewed interface, resolve mismatches, agree semantic/variation/authority/retention proof and migration, and only then select a bounded Build. The completed `cde0ea99` comparison supplies interface pressure and mechanism evidence but does not select a winner or become a product owner. Reconcile the inherited [scheduled mechanism-evaluation obligation](../audits/scheduled/README.md) at that mechanism/integration boundary rather than bypassing or activating it here.
