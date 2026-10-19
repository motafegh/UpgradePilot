# Investigator product-direction proposal — strategic review and finalization

Date: October 20, 2026 (Asia/Tehran). Initial operation: Repository Audit / Review; subsequent explicitly requested finalization: Planning/Design with source-backed review.
Inspected main: `766fe8a7`, fast-forwarded from `b2948711` after an explicit user request to pull the other assistant's proposal and assess the project direction before deciding further work.
Subject: [responsibility-decomposition proposal](../proposals/2026-10-19_INVESTIGATOR_RESPONSIBILITY_DECOMPOSITION_AND_PRODUCT_DIRECTION_PROPOSAL.md).
Previous evidence: [completed comparison/source review](evidence/2026-10-19-investigator-evidence-first-build/COMPARISON_REVIEW.md).

## Initial review horizon — scope, authorization and proportionality

Ali asks to pause further development, analyze whether the increasingly deep path is appropriate, review the new proposal and then decide. Authorization is Git synchronization and source/evidence-backed review. No proposal acceptance, plan/specification/source/test change, model loading or inference is selected. The unrelated October 3 untracked audit draft remains untouched.

The pull adds only the 1,105-line proposal. This review record is the sole new writing for the review; the proposal and controlling owners remain unchanged. It is a dated, non-controlling examination rather than a second plan or live-state owner. MEMORY.md alone owns any subsequently selected direction.

Continuous-context adaptation: Ali has just received the completed negative comparison and explicitly requests strategic review before another decision. Compress A1/A2 gate repetition for this read-only operation; no implementation choice is being accepted through that adaptation. The durable record is initialized after the proposal's first full reading, once its cross-owner strategic scope is established; it preserves that actual inspection path rather than claiming the file existed before review began. Previous learner D/E debt remains separate.

## Cycle status and orientation map

- A0 — DONE: Git/current live owner, proposal, Charter and relevant evidence/architecture owners reconciled; exact pulled delta verified.
- A1 — DONE at directed review depth: current comparison completed mechanically but failed all four semantic cases; the earlier deterministic-baseline suggestion is a recommendation under review, not accepted strategy.
- A2 — DONE at review scope: distinguish numerical/source evidence, accepted trust architecture, current implementation gaps, causal hypotheses and choices about the cheapest useful next step.
- B — DONE: initial proposal reviewed and, after Ali explicitly requested finalization, fully revised in place with adjudication of all seven additional suggestions. See the dated continuation below.
- Verification gate — GREEN for the bounded review: numerical/source/ownership and record-integrity checks pass; causal and method-selection uncertainties remain explicit. No inference or test rerun selected.
- D — CURRENT: written evidence-backed explanation and decision-relevant trade-offs supplied; learner ownership unassessed.
- E — PENDING: joint direction decision; no automatic next plan or implementation.
- C — CONTINUOUS: preserve material findings and limits here.

## Inspection route and proof horizon

The full proposal, its authority declarations, exact main experiment records, Charter, Product Decision Model, Minimum Useful Generality, ADR-0012 and current Workspace/action source are inspected. The cited research is read directly from local Git at `cde0ea9906fa37e4184962d0ba65577e4d62396e` and the named research ref resolved to `253b48de20b475eada48810d193bd420c51aa7d4`; it is not merged. Its mechanical/source-review records are separate historical evidence with known-case, reviewer and policy-cost limitations. Old experiment/source-review outcomes remain immutable.

Current executable facts: `WorkspaceHost.evaluate_proposal` records unsupported because no semantic proposal/conflict/adequacy evaluator is admitted. `MaintainerAction` supports only abstain. The existing Workspace already retains attributed proposals, evaluations and content citations. Those facts must not be confused with a complete domain-level proposition evaluator or model recommendation authority.

`UP-SKILL:upgradepilot-repository-audit` and `UP-SKILL:upgradepilot-working-memory` apply.

## Review conclusion

**Recommend conditional acceptance of the broad direction, with qualifications before adopting its immediate plan/sequence.** Its evidence/trust principles mostly reaffirm accepted architecture. Its numerical account is sound. Closing repetitive instruction tuning and maintaining the now-working experiment infrastructure are reasonable engineering decisions. Neither the causal diagnosis nor the prescribed next method is established by those results.

The project is right to require evidence/authority separation. The unresolved question is whether the next engineering increment purchases a useful general capability at acceptable cost. More layers, more records or more careful abstention alone would not establish that. My previous recommendation to design a deterministic baseline is therefore an option to justify at a bounded decision gate, not a deduction from the failed model outputs.

## Confirmed evidence and good parts to retain

| Inspected record | Reconciled observation | Limit |
| --- | --- | --- |
| Research `cde0ea99` mechanical/source-review records | Eight complete final reports; zero advice-ready. Agent consumes less input/time in all four paired assignments. | Two exposed cases, one sample per arm/deployment, differing stage overhead; no general efficiency or model-ranking result. |
| Research Gemma HTTPX Agent delivered-line list | Target TestClient source lines were delivered, including the actual instantiation site. | Acquisition value is distinct from successful interpretation or product usefulness. |
| Main reference accounting/adjudication | Five known calls; 66,920 input/4,373 generated; 0/4 adequate. | The four cases are related development fixtures, not four independent product domains. |
| Main candidate accounting/review and original response/input hashes | Five known calls; 67,590 input/5,833 generated; 0/4 adequate; 33.39% more generation and 22.77% more prediction time. | Descriptive single-cohort comparison, AI-assisted/source-aware and unblinded. |
| Current source-pair receipts and delivered new signature | Inputs 8,039/8,033 tokens; new Client retains cert at L647, contradicting the old-caller report. | These are smaller packets, not a minimal-context capability control. |

Research numerical checks use the actual eight structured assignment rows: Agent input reductions 10.53/12.46/44.28/37.02% and elapsed reductions 6.76/17.49/55.76/48.90%, respectively. They support the proposal's scoped descriptive claim; they are not pooled with main semantic outcomes. The research Fixed policy already has upstream, consumer/applicability, environment/CI and challenge stages, including sixteen stage candidates and four incomplete stages. This matters to interpreting any future multi-role claim.

Keep the proposal's distinction between a role and an agent; no framework/swarm is justified. Keep original evidence and method attribution, relevant counterevidence, dynamic/unresolved cases, protected qualification and separate action authority. Keep the warning against fixture hardcoding and against growing research infrastructure merely because more edge cases can be polished.

## Material findings and recommended qualifications

### 1. Correct the architectural diagnosis and distinguish it from a causal hypothesis

**Affected proposal:** §§1,7,19,23.

The product is not currently an admitted monolithic LLM-to-maintainer-action system. [WorkspaceHost](../src/upgradepilot/workspace/lifecycle_host.py) `evaluate_proposal` at L750 records unsupported when no semantic evaluator is admitted. The [experiment adapter](../experiments/investigator_workspace_adapter.py) actually calls that owner for reports and stop proposals. [Maintainer synthesis](../src/upgradepilot/maintainer_action.py) permits only abstain; [report projection](../src/upgradepilot/report_projection.py) invokes it. These are implemented boundaries, not just future promises.

The missing semantic evaluator is a real capability gap. Model outputs in experiments still fail source interpretation. Those facts do not demonstrate that an overloaded architecture caused the failures, or that splitting the same model into roles will repair them. The latest source-pair task already removes autonomous discovery, and the older Fixed method already has several stages. Neither is an isolated test of the proposed new role structure.

**Recommended change:** describe the proposal as implementing missing capabilities within the accepted hybrid architecture. Label overload/attention/task-composition as hypotheses. Retain authority separation because Core/ADR semantics require it, independently of whether it improves model competence. Replace the implication that production previously granted unilateral model recommendation authority.

### 2. Select a bounded first decision rather than accept the whole staged programme

**Affected proposal:** §§11–13,18.3,21.

A general mechanical baseline is credible, but these failures do not select it over every cheaper diagnostic or existing-owner improvement. The old Qwen research result concerns its own deployment/policy/tasks; it does not settle a different bounded interpretation control. Conversely, no new model run follows merely because the current candidate failed.

**Recommended change:** accept a small design/feasibility gate that names the exact product question, alternatives, engineering ceiling, any model-call ceiling, proof and stop/reject conditions. The output may select the baseline, narrow it, choose another discriminating control, or stop it. Do not make a parser, generic proposition framework, validator model, protected campaign and discovery reconnection a committed seven-stage backlog. The first implementation must earn its own authorization/result.

### 3. State which failures the source-relation baseline addresses and which remain

**Affected proposal:** §§5.7,8.2,11,15.1.

Signature/call extraction could remove a demonstrated HTTPX burden. It does not automatically repair glyphsLib's promotion of native unresolved state into confirmed coverage, invalid semantic attribution, candidate discovery or useful action synthesis. More structured inputs can still be misinterpreted; the CI packet already contains typed native assessments.

**Recommended change:** name the first responsibility as captured source-fact/relation extraction, with an explicit downstream use and residual limitations. Do not present success of that slice as resolution of interpretation generally. Require a before/after example of the useful maintainer-facing finding it would enable, through existing owners.

### 4. Tighten the first grammar and binding contract without demanding a full static analyzer

**Affected proposal:** §§8.3,11.1–11.4.

The illustrative accepted-keyword set difference is not a complete Python call-compatibility rule. Declared parameter kinds, positional-only/keyword-only parameters, defaults, bound receivers, variable keyword acceptance and argument expansion affect what can be concluded. A textual `super()` call does not independently establish an effective callee across arbitrary MRO/dynamic behavior. Partial captures may not be parsable complete definitions.

The proposal already lists many unresolved dynamic cases; that is good. The next design should turn those caveats into the actual admitted input/output boundary. A narrow syntactic baseline need not solve arbitrary dispatch, aliasing, decorators or runtime behavior.

**Recommended change:** distinguish declared syntax from effective acceptance/execution, identify who supplies/establishes caller/callee correspondence, and preserve it as a premise if unproved. Define the real source/capture form the normal producer supplies. Human selection of corresponding snippets may be legitimate diagnostic preparation; it must not be described as an automated PR-to-binding capability. Existing Minimum Useful Generality/GEN-002 applies to the responsibility actually claimed.

### 5. Reuse existing authority owners and state the exact missing evaluator

**Affected proposal:** §§8–9,12.2,15.2.

The existing [lifecycle records](../src/upgradepilot/workspace/lifecycle_records.py) already retain attributed proposals, citations and evaluation outcomes. These records do not themselves implement the Product Decision Model's domain-level established/refuted/unresolved/conflicted evaluator. Conversely, a native deterministic fact does not need a redundant generic LLM evaluation before use. ADR-0012 explicitly protects that distinction.

**Recommended change:** add a compact implemented-versus-missing map before proposing types. Treat the six layers as responsibilities, not mandatory new modules/processes/storage records. Identify the first specific proposition/evaluation owner and reuse native assessed state. Clarify the rejection phrase about downstream reparsing: needing a duplicated competing extractor is a problem; consulting original evidence for audit or discriminating validation is not inherently a failed baseline.

### 6. Move product usefulness and engineering cost earlier

**Affected proposal:** §§12,14–16,17.

The proposed final maintainer example is useful, but postponing usefulness checks until method qualification risks another long internally rigorous programme. The Charter accepts supported core progress without requiring a successful agent method. Current synthesis still being abstain-only is a concrete reason to state the incremental user benefit precisely; it is not permission to weaken action semantics.

**Recommended change:** before a new subsystem, predeclare the maintainer question, supported conditional finding/next evidence, expected advantage over an existing transparent baseline, and total engineering/model limits. Review a thin end-to-end development result early. Independent usefulness/protected acceptance still remains later; early product-value testing must not be mislabelled as final acceptance. Permit no-value/too-costly outcomes to stop the increment.

### 7. Keep semantic qualification discriminating and preserve sampling limits

**Affected proposal:** §§4.4,5.4,9.4,15.3–15.4.

The small packets being around 8k tokens rules out an explanation restricted to the 22k–25k cases; it does not isolate context pressure, report/citation burden, task composition, deployment or stochastic variation as causes. Smaller role contexts and a validator are plausible hypotheses, not demonstrated remedies. The older staged Fixed results should be explicit counterpressure against assuming extra roles suffice.

**Recommended change:** describe the goal as the only intentional model-facing method change; retain the existing fresh IDs/timing observations and one-sample/AI-assisted-review limits. A later evaluator comparison must retain supported findings as well as reject false propositions and preserve justified unknowns. Agreement, blanket rejection, always-unresolved and generic abstention must not pass as useful validation. A second model's agreement is not independent evidential corroboration merely because it is another call.

## Proposed bounded decision for Ali to consider

Retain UpgradePilot's already accepted hybrid evidence/authority architecture and the maintenance posture for the now-working experiment controls. Close repetitive tuning of the completed instruction-only trial. Treat responsibility decomposition as a justified design direction and its benefit to model performance as an untested hypothesis. Admit only a bounded next design/feasibility decision: identify the earliest sufficient owner of one useful mechanical source relation, the real source/binding inputs, the minimum handoff to existing evaluation/reporting, alternatives, generality/unresolved proof, explicit cost ceilings and a visible maintainer benefit. The gate may select, narrow or reject that baseline; it does not select the later model/agent/discovery stages or permit product adoption. Preserve all previous experiments and learning debt.

This is a proposed decision text, not an accepted owner change. The proposal remains byte-identical at SHA256 `54ccf59a925afd6842d78b6b26d992593c753543dc60ad61a88f8fcd4f71e00b`.

## Verification and limitations

The pulled change is exactly one proposal, with no code/control changes. Read all 1,105 lines; inspect the accepted owners and source symbols cited above. Verify the eight research assignment costs and source-review denominator from immutable Git records; verify the main accounting deltas and all four original response/input hashes; inspect the current new-signature source establishing cert remains present. Main semantic outcomes are the existing source-audited records, not a newly run experiment or a broader independent human review. No tests, target code, model clients or predictions are executed; no source parser or product evaluator is built or activated. The old 135 provider calls/private reasoning are not replayed or comprehensively re-audited in this review. No current-model-market survey or model ranking is claimed.

## D/E handoff

The crucial distinction for discussion is trust architecture versus capability diagnosis versus product-method selection. The architecture is accepted and its attribution/unsupported-evaluation/action guards are implemented; a domain-level semantic evaluator remains missing. The causal diagnosis remains partly unresolved, and method selection needs a bounded cost/value decision. The correct lesson is neither to discard all earned engineering nor to assume another layer is progress. Written feedback supplies that model. Ali's acceptance/challenge and learner ownership remain unassessed; E and any selected next work remain pending. The proposal, specifications, plans, source and MEMORY.md are not changed by this review.


## October 20 continuation — authorized final proposal revision

Ali asks to check seven additional ideas, finalize, and write the full final proposal based on everything. This explicitly expands the initial read-only review to proposal writing and necessary state reconciliation, not implementation, comparison execution, strategy acceptance or inference. Continue this same coherent artifact-review responsibility; do not create a competing proposal or cycle.

Apply `UP-SKILL:upgradepilot-planning-design` and continue `UP-SKILL:upgradepilot-working-memory`. Continuous-context A1/A2 compression is proportionate: the review model and qualifications were already presented, and Ali explicitly requests the final writing. Teach the corrected product-comparison/consumer/evidence model while preparing the artifact; do not claim learner ownership from that instruction. The normal repeated orientation stop would delay the explicitly requested reviewable artifact without changing its proof or authority. No Build, experiment, trust or external-target boundary is waived.

### Additional source checks and adjudication

Read product-simulation/AGENTS.md before the local simulation owners. Inspect the baseline v0.1 rules/dimensions, simulation navigation, S006 artifact/identity/coverage explanation and synthesis, and the bounded implemented-foundation transfer evaluation. Search executable owners for the named simulation comparator; no matching complete six-case product-comparison harness is identified by that search. Existing S001 real-flow proofs and narrower post-implementation evaluations prevent an honest claim that product evaluation never happened. S006 explicitly uses a different bundle and preserves evaluator oracle exposure. Therefore accept early product comparison as a priority, but condition CPU-only/no-model replay on actual retained inputs, normal producer reachability and fair denominator. No new evaluation was run and no full per-case replay inventory is claimed.

Inspect current PropositionState/PropositionAssessment/applicability composition and the action/report owners. Read the synthesis specification's exact targeted-check permission and producer-reachability requirements. Accept existing proposition semantics as the starting point, concrete consumer and code-home decisions before Build. Reject the assertion that there is no consumer: reports consume synthesis. Do not force a positive action or add a generic producer without demonstrating need.

Accept deterministic-first derivation and source checks with independent expectations/counterexamples; same algorithm twice is not independent proof. A semantic reviewer needs the proposition/evidence but can be blind to proposer identity/preferred verdict. Measure supported positive retention, false acceptance/rejection, justified unknowns and costs. Agreement alone cannot establish truth. Reject suggestion (g)'s impossibility and no-model-quality-risk claims: the negative evidence does not isolate those causes.

### Artifact and owner changes

Rewrite the existing proposal in place, incorporating the initial seven review qualifications plus additional suggestions (a)–(g). It now puts product-value/comparison readiness first; maps implemented versus missing responsibility; defines one proposed six-active-hour, zero-inference design gate; requires consumer/representation/code-home decisions; treats source extraction as one selectable alternative; qualifies grammar/binding/generality; gives discriminating validation and protected-method freeze rules; and makes later roles/actions/discovery conditional rather than a committed programme. Six hours is a proposed future cap, not measured effort for this revision. Proposal remains non-controlling/finalized for decision.

Reconcile MEMORY.md to the actual proposal-finalization handoff, without selecting the proposed next gate. Reconcile original comparison session/B wording to execution discontinued/incomplete-inconclusive and completed evidence publication. This is administrative reconciliation of the existing immutable-result/no-resume rule, not a claim the full original B objective succeeded or that learner D/E closed. Append the reason to that original cycle; preserve dated history,3/1/8 outcomes, unknown usage, control debt and every frozen artifact. No experiment plan, accepted specification, source/test, original review/result or retention index changes. The unrelated October 3 draft remains untouched.

### D/E and remaining decision

The important ownership distinction is now explicit in the artifact: accepted trust architecture, unproved capability diagnosis, product comparison readiness, useful consumer and method selection are separate. Deterministic-first does not imply deterministic-only; a report consumer does not imply action permission; an incomplete experiment's execution ending does not discharge learner D/E. Written explanation is provided, learner ownership remains unassessed. E and acceptance/selection of any next planning responsibility remain pending.

### Final revision verification

Four intended Markdown documents change: owning proposal, live MEMORY.md, this progression record and the original comparison cycle's execution-disposition reconciliation. Check all 106 local links and the one linked anchor across those documents, balanced fences, final newlines and `git diff --check`: pass. Proposal is 291 lines, SHA256 `d6d13d43c42de5a1d6a9562f7629e486b9e1b7c0c83d2da015a60bcc9c255065`. The initial byte-identical hash above remains the earlier review horizon, not the final revision identity.

Diff-scope assertion confirms no product/experiment/test/tool source, accepted plan/specification/ADR, frozen input/output/result, original evidence review or retention index changes. No runtime tests are rerun for this documentation-only responsibility. No new case readiness inventory, CPU comparison, target code execution, model load or prediction is claimed. Source-backed inspection supports the qualifications; selection of a method and its effectiveness remain unproved. Publish this coherent increment under Ali's standing in-scope commit/push instruction; preserve the unrelated untracked draft. D/E remain pending as described above.


## October 20 — direction acceptance and plan-writing handoff

After publication at f7b01bde, Ali explicitly accepts the bounded direction, asks for the next step, receives the readiness/comparison/consumer/selection sequence and six-hour/no-model boundary, then directs writing the plan. The strategic selection question is resolved to that limited extent; learner D/E ownership remains unassessed. Preserve all earlier proposed/unaccepted wording as its dated horizon. Update the proposal's acceptance metadata/plan reference and live MEMORY.md; do not retroactively treat the initial review or finalization as implementation acceptance. The recorded finalization hash d6d13d43c42de5a1d6a9562f7629e486b9e1b7c0c83d2da015a60bcc9c255065 remains the f7b01bde horizon, before this acceptance annotation.

[The new investigation-planning cycle](2026-10-20_product-value-and-baseline-feasibility-investigation-planning_lbd-cycle.md) owns preparation of the compact [investigation plan](../plans/PRODUCT_VALUE_AND_TRANSPARENT_BASELINE_FEASIBILITY_INVESTIGATION_PLAN.md). That writing instruction does not execute the investigation or select its eventual implementation/experiment. No previous result or learner debt is erased.
