# Bounded LLM-Assisted Maintainer Decision and Report Synthesis — Design Proposal

**Recorded:** 2026-09-10  
**Status:** Candidate / non-controlling proposal. This document does not admit an LLM synthesis method, change the Charter outcome semantics, authorize source/test implementation, select LangGraph, or change live project continuation.  
**Repository snapshot:** `main@409fcc8ee5459f2f126f3b485a70249616198b26` (`docs: add synthesis design investigation proposal`)  
**Primary design responsibility:** evaluate whether UpgradePilot should eventually use a bounded LLM-assisted final synthesis responsibility after heterogeneous investigation has completed, while preserving deterministic authority, evidence provenance, uncertainty, and Charter claim limits.  
**Primary precursor:** [`2026-09-10_OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_INVESTIGATION.md`](2026-09-10_OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_INVESTIGATION.md)  
**Relevant experimental precedent:** the paused bounded `EvidenceGapPlanner` ordinary-Python and LangGraph experiments under [`../experiments/`](../experiments/) and their R4 working memories/proposals.  
**Mutation boundary:** creation of this proposal only. No source, tests, specifications, plans, working memory, `MEMORY.md`, or other repository owner is changed by this proposal.

`UP-SKILL:upgradepilot-planning-design`

---

## 1. Executive proposal

UpgradePilot should **seriously evaluate a separate final decision/synthesis responsibility in which an LLM performs bounded semantic synthesis over already-earned investigation evidence**, but the LLM should not become the authority that decides what UpgradePilot is allowed to claim or recommend.

The strongest current candidate architecture is:

```text
completed typed investigation state
+ provenance / authority / reliability metadata
+ accepted synthesis semantics
↓
DETERMINISTIC DECISION PROJECTION
↓
DETERMINISTIC PERMISSION ENVELOPE
  - actions currently permitted
  - actions currently prohibited/unavailable
  - mandatory uncertainties/conflicts
  - required checks
  - claim limits
  - reliability constraints
↓
BOUNDED LLM DECISION SYNTHESIZER
  - choose one permitted primary Charter action
  - identify decisive evidence-backed reasons
  - preserve material residual uncertainty
  - prioritize supporting checks/reasons
  - propose maintainer-facing explanation structure
↓
DETERMINISTIC RESULT VALIDATION
  - selected action was permitted
  - cited evidence/provenance exists
  - mandatory uncertainty/checks were not omitted
  - prohibited claims/actions were not introduced
  - required structured contract is valid
↓
VALIDATED SYNTHESIS RESULT
↓
MAINTAINER REPORT / CLI / API PRESENTATION
```

This architecture deliberately combines two strengths:

```text
deterministic code
→ owns authority, hard constraints, admissibility, provenance, and claim boundaries

LLM
→ owns bounded cross-evidence reasoning, prioritization, explanation, and selection among already-permitted alternatives
```

The proposal is **not** to replace the current transparent deterministic synthesis baseline. The current baseline remains necessary because the Charter explicitly requires a deterministic bounded recommendation/abstention and because technology admission requires an observed limitation plus comparative evidence before a model-based method is adopted.

The proposal is instead:

> complete enough deterministic semantic work to establish the trusted decision boundary and a credible baseline; then run a bounded comparison asking whether an LLM-assisted synthesizer produces materially better maintainer decisions and reports without violating those deterministic boundaries.

This is consistent with the Charter's explicit allowance for later experiments with grounded LLM synthesis while preserving the requirement that advanced methods earn admission.

---

## 2. Relationship to current controlling work

This proposal does not supersede or rewrite:

- [`../PROJECT_CHARTER.md`](../PROJECT_CHARTER.md);
- [`../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md);
- [`../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md);
- [`../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md);
- current mechanism-specific candidate/applicability/investigation owners;
- `MEMORY.md` as the sole owner of live continuation.

The Charter outcome vocabulary remains exactly:

```text
merge after normal review
run targeted checks
investigate or block
defer
abstain
```

This proposal does not redefine those labels.

The current synthesis plan's deterministic-first requirement remains useful and should be read as an **evaluation baseline/admission gate**, not automatically as evidence that the permanent synthesis method must be a hand-authored decision tree forever.

The preceding synthesis investigation already established important design pressure:

- sufficiency is action-relative;
- mechanism-local negative evidence is not global negative evidence;
- favorable action needs positive permission, not absence of a known problem;
- `run targeted checks` requires a concrete discriminating check;
- `investigate` and `block` may deserve internal distinction;
- `defer` requires a real future/pending condition;
- some producer-integrity defects must constrain permission upstream rather than be repaired by synthesis;
- one primary action plus secondary reasons/checks is preferable to mechanism voting or a universal severity score.

The LLM-assisted architecture proposed here **depends on those findings** rather than bypassing them.

---

## 3. Why a separate synthesis system is worth considering

The current final responsibility is not merely a local mapping such as:

```text
artifact applicable -> block
python not applicable -> merge
CI unresolved -> defer
```

The real input contains heterogeneous proof states, competing concerns, unresolved propositions, reliability restrictions, mechanism-local scope, contextual evidence, possible maintainer checks, and claim limitations.

A growing deterministic implementation could eventually accumulate:

```text
many cross-product conditions
+ precedence rules
+ presentation ordering rules
+ special handling for combinations
+ duplicated explanation templates
+ implicit severity assumptions
```

That may remain the correct solution. But it is also a credible observed design pressure that should be tested rather than assumed away.

An LLM may add value specifically where the responsibility requires **bounded semantic composition**:

1. deciding which already-permitted action is most useful when several are technically defensible;
2. relating evidence from different mechanism families without reducing them to a numeric score;
3. distinguishing decisive reasons from supporting context;
4. preserving a blocker while also surfacing a useful secondary targeted check;
5. explaining why an unresolved state means check, investigate, defer, or abstain under the accepted semantics;
6. deciding what the maintainer needs to see first versus what remains supporting trace evidence;
7. producing a compact uncertainty-aware narrative from a larger typed evidence set.

Those are credible model-synthesis responsibilities. They are not evidence that the model should own action authority.

---

## 4. Core architectural principle: semantic reasoning is not execution or claim authority

The paused `EvidenceGapPlanner` experiments provide a strong precedent:

```text
trusted internal state
→ explicit bounded model projection
→ untrusted structured model proposal
→ deterministic rebinding/admission against current trusted state
→ admitted action/effect
```

See, among other evidence:

- [`../experiments/evidence_gap_planner_model_boundary.py`](../experiments/evidence_gap_planner_model_boundary.py);
- [`../experiments/evidence_gap_action_admission.py`](../experiments/evidence_gap_action_admission.py);
- [`../experiments/langgraph/evidence_gap_workflow.py`](../experiments/langgraph/evidence_gap_workflow.py);
- [`2026-09-03_B2_X1_R4B_CORRECTED_LANGGRAPH_INDEPENDENT_RESEARCH_AND_DESIGN_PROPOSAL.md`](2026-09-03_B2_X1_R4B_CORRECTED_LANGGRAPH_INDEPENDENT_RESEARCH_AND_DESIGN_PROPOSAL.md);
- [`../working-memory/2026-09-03_1804_B2-X1-R4B-comparison-boundary-reframe.md`](../working-memory/2026-09-03_1804_B2-X1-R4B-comparison-boundary-reframe.md);
- [`../working-memory/2026-09-04_1904_B2-X1-R4B-architecture-freeze-and-build-entry.md`](../working-memory/2026-09-04_1904_B2-X1-R4B-architecture-freeze-and-build-entry.md).

The final decision synthesizer should reuse the **architectural lesson**, not necessarily the exact experiment types or topology:

```text
model may reason within a bounded observation
model output is a proposal
model cannot create new authority
model cannot redefine hidden trusted facts
model cannot silently make a prohibited action permissible
model cannot erase uncertainty required by deterministic evidence semantics
```

This proposal therefore treats model synthesis and deterministic decision authority as separate responsibilities.

---

## 5. Keep EvidenceGapPlanner and final DecisionSynthesizer separate

The two responsibilities are related but materially different.

### EvidenceGapPlanner

Question:

> What bounded evidence should UpgradePilot investigate next?

Its output concerns epistemic continuation and optional bounded investigation action.

### Maintainer DecisionSynthesizer

Question:

> Given the investigation state that now exists, what bounded maintainer-facing action and explanation are justified?

Its output concerns the Charter-facing recommendation/report.

Therefore:

```text
investigation continuation decision
!=
maintainer action decision
```

and:

```text
no further justified UpgradePilot investigation
!=
overall evidence sufficient for a favorable maintainer action
```

They may share a design pattern—bounded observation, structured model proposal, deterministic validation—but they should not be collapsed into one universal agent or generic planner.

A future workflow may compose them, but their semantic contracts should remain independently inspectable.

---

## 6. Proposed responsibility decomposition

### 6.1 `DecisionEvidenceBundle` — bounded synthesis projection

The LLM should not receive the entire `PublicPullRequestInvestigation` object simply because it is available.

A dedicated projection should expose only decision-relevant semantic state, for example conceptually:

```text
identity
  repository
  PR
  exact head/base revision
  dependency transition

material findings
  mechanism/candidate identity
  applicability/consequence state
  proof strength
  source/evidence references
  authority/origin class

uncertainty/conflict
  unresolved propositions
  conflicting evidence
  unsupported methods
  unavailable/unreachable evidence

context
  admitted CI/repository facts that can affect action

continuation/check information
  concrete discriminating maintainer checks
  known external pending condition when established

reliability constraints
  evidence whose producer integrity restricts action permission

claim limits
  facts UpgradePilot must not claim from this state
```

This should be a **semantic projection**, not serialization of every raw upstream object, log, file, model message, or provider payload.

Raw evidence remains available through provenance references where needed.

### 6.2 `DecisionPermissionEnvelope` — deterministic authority

Before model synthesis, deterministic code should establish the exact decision authority available at that state.

Conceptually:

```text
permitted_primary_actions
prohibited_or_unavailable_actions
mandatory_uncertainties
mandatory_conflicts
required_checks
required_rerun_conditions
claim_limits
reliability/provenance constraints
```

Example:

```text
permitted:
  run targeted checks
  investigate or block

unavailable:
  merge after normal review
  defer

mandatory uncertainty:
  exact target wheel compatibility unresolved

required check:
  establish exact target wheel compatibility

claim limit:
  sdist existence does not establish successful source installation
```

The LLM can choose and explain within this envelope. It cannot widen the envelope.

### 6.3 `DecisionSynthesisProposal` — structured LLM output

The first experiment should use a strict structured output rather than free-form prose as the semantic result.

A candidate conceptual result:

```text
primary_action
internal_sub_disposition?       # e.g. investigate vs block if later accepted
primary_reason_refs[]
supporting_reason_refs[]
material_uncertainty_refs[]
required_check_refs[]
report_priority[]
explanation
```

The model should reference evidence/reason/check identifiers from the supplied projection rather than inventing factual claims.

The model may decide:

- which permitted action is the best primary recommendation;
- which evidence is decisive versus supporting;
- how multiple reasons interact;
- what should be surfaced first in the maintainer report;
- how to explain the result in bounded language.

The model may not decide:

- whether a prohibited action becomes allowed;
- source/revision identity;
- whether missing evidence should count as negative evidence;
- whether model-origin evidence becomes independently authoritative;
- whether a known reliability defect can be ignored;
- whether a required uncertainty/check may be omitted;
- whether UpgradePilot can claim objective safety.

---

## 7. Deterministic validation after the LLM

A valid structured model response is still untrusted.

The deterministic validator should reject or downgrade outputs that violate the supplied authority envelope.

At minimum it should validate:

```text
selected action ∈ permitted_primary_actions
all referenced evidence/reason/check IDs exist
all mandatory uncertainty/conflict references remain represented
all required checks remain represented when applicable
no unavailable/prohibited action is implied as the current recommendation
no source/revision/provenance fact was invented
no unsupported safety/certainty claim is encoded
structured cross-field invariants hold
```

The validator should not attempt to determine whether the model's prose is philosophically persuasive. It should protect enforceable semantic and authority constraints.

Unexpected model/provider failures must remain distinguishable from valid semantic abstention.

---

## 8. Decision synthesis and report synthesis are related but not identical

There are two separate user-facing responsibilities:

```text
A. Decision synthesis
   What Charter-facing maintainer action is justified?

B. Report synthesis
   What should the maintainer see first, why, and at what level of detail?
```

The LLM is potentially valuable for both, but they should remain conceptually separable.

### First credible implementation shape

Do **not** start with two LLM agents or two independent model calls merely because the responsibilities are distinct.

The smallest experiment can ask one bounded structured model call to return:

```text
validated action proposal
+
decisive/supporting reason references
+
report-priority ordering
+
bounded explanation
```

Then deterministic rendering can present the validated structure.

Only if evidence later shows that decision quality and report-quality optimization conflict materially should a separate presentation model/pass be evaluated.

This avoids premature multi-agent architecture.

---

## 9. Interaction with current action-semantics findings

The LLM does not solve unresolved semantics by itself.

### `merge after normal review`

Until positive permission prerequisites are accepted and enforceable, the permission envelope should simply omit this action.

The model must not infer favorable permission from:

- no known concern;
- one non-applicable mechanism;
- no artifact candidate;
- green CI;
- absence of a model-extracted claim.

If later admitted, its bounded meaning should remain compatible with the current pressure-tested interpretation: no additional UpgradePilot-specific escalation is justified, so the PR returns to ordinary maintainer review—not “UpgradePilot proves this is safe.”

### `run targeted checks`

The envelope should permit this only when a concrete decision-relevant proposition remains unresolved and a concrete discriminating maintainer check is available.

The model can explain why that check is decision-relevant and how it interacts with other findings, but it should not invent a generic “test more” recommendation.

### `investigate or block`

If the project later accepts an internal distinction such as:

```text
investigate
→ broader evidence gathering is still required

block
→ evidence is already sufficient to stop ordinary progression until a stated condition changes
```

then deterministic semantics should determine which sub-dispositions are admissible. The model may select or explain among those admissible states where multiple remain credible.

### `defer`

The model must not manufacture temporal semantics from generic uncertainty.

Until the input contains an explicit future/pending condition and rerun trigger, `defer` can remain unavailable.

### `abstain`

The model may propose abstention when it is permitted because UpgradePilot lacks sufficient authority/method/domain coverage for a more specific recommendation.

Operational/provider failures that prevent synthesis from obtaining a valid input remain a separate application/failure contract question; they should not be automatically relabeled as semantic abstention by the LLM.

---

## 10. Why the deterministic baseline is still required

The current synthesis plan should still establish the smallest transparent deterministic baseline.

That baseline gives the project four things the LLM experiment needs:

1. **semantic authority** — accepted action permission/prohibition rules;
2. **comparison baseline** — evidence that the LLM actually improves something rather than merely sounding better;
3. **fallback behavior** — a bounded product method remains available if the model/provider is unavailable or rejected;
4. **technology-admission evidence** — the exact limitation of transparent deterministic synthesis can be measured.

The comparison should therefore be:

```text
same accepted evidence inputs
same Charter action semantics
same claim limits
same reliability constraints
same evaluation cases

A. transparent deterministic synthesis baseline
vs
B. bounded LLM-assisted synthesis inside deterministic permission/validation boundaries
```

The comparison should not require identical internal representations or identical wording.

---

## 11. Bounded experiment hypothesis

### Hypothesis

A grounded LLM-assisted synthesizer can produce **more useful and better-calibrated maintainer decisions/reports across heterogeneous evidence combinations** than the transparent deterministic baseline while preserving deterministic action authority, provenance, uncertainty, and claim limits.

### Potential success dimensions

Evaluate at least:

- correct Charter action relative to an accepted case rubric;
- no prohibited stronger action;
- preservation of decisive uncertainty/conflict;
- required-check correctness;
- evidence-reference/grounding correctness;
- no invented factual claims;
- no objective-safety overclaim;
- quality of decisive-reason selection;
- usefulness of prioritization for a maintainer;
- stability under irrelevant evidence ordering;
- robustness across materially different mechanism combinations;
- model/provider failure behavior;
- implementation/maintenance complexity relative to baseline;
- latency/cost only to the depth material for this product.

### A credible success result

The LLM method should not be considered successful merely because its prose is nicer.

It should demonstrate something such as:

```text
materially better cross-evidence action/reason selection or report usefulness
+
no meaningful regression in authority/grounding/uncertainty discipline
+
acceptable operational cost/failure behavior
```

### Rejection conditions

Reject or retain only as a disposable experiment if it:

- frequently chooses prohibited actions;
- drops required uncertainties/checks;
- invents evidence or claims;
- requires a complex validator that effectively re-implements the entire decision system after the model;
- behaves materially inconsistently under equivalent evidence;
- only improves wording rather than decision usefulness;
- costs substantially more complexity/latency than the value demonstrated;
- makes deterministic synthesis already sufficient for the responsibility.

A negative result is valid project evidence.

---

## 12. Pressure cases for the future comparison

The LLM-assisted method should be tested against the same high-information combinations identified by the current synthesis investigation, including at least:

1. artifact serviceability candidate + exact target wheel compatibility unresolved;
2. the same targeted-check gap plus an independent established Python-support concern;
3. published wheel loss + sdist exists + source-build/install viability unresolved;
4. several mechanism-local negative results but no accepted discovery-coverage basis for favorable action;
5. the same negative results after accepted positive coverage/integrity/context prerequisites are satisfied;
6. `supported_not_correlated` CI without another material concern;
7. `no_successful_ci` without explicit pending semantics;
8. a genuinely producer-established pending external condition if such a state is later admitted;
9. package acquisition failure without retry/future-condition semantics;
10. unsupported Python comparison-method state with available target evidence;
11. conflicting or unsupported dependency transition;
12. evidence affected by a known producer-integrity limitation;
13. independent blocker plus a useful secondary check;
14. unresolved state with a concrete check;
15. unresolved state without a concrete check but with meaningful broader investigation;
16. unresolved/out-of-method state with neither useful investigation nor future condition, forcing abstention.

The test corpus should contain meaningful semantic contrasts, not one prompt per known fixture.

---

## 13. Model-visible information and hidden authority

The EvidenceGapPlanner experiment established a useful discipline: model-visible semantic context and hidden execution authority are not the same thing.

The final synthesizer should preserve the same discipline.

### Model-visible

Potentially visible:

- bounded dependency transition;
- normalized mechanism findings;
- provenance identifiers and interpreted evidence summaries;
- proof/authority class;
- unresolved propositions;
- admitted contextual facts;
- permission envelope;
- claim limits;
- permitted actions and their operational meanings;
- concrete required checks;
- any accepted future-condition/rerun semantics.

### Not model-authoritative

The model must not become the owner of:

- canonical repository/revision identity;
- evidence freshness/validity enforcement;
- accepted mechanism applicability semantics;
- producer-integrity correction;
- action permission construction;
- hidden security/credential state;
- mutation/execution authority;
- accepted Charter/specification semantics.

The projection must be explicit so adding a field to an internal source type does not automatically expose it to the model.

---

## 14. Provenance and model-grounding requirements

The LLM should reason over **attributed semantic evidence**, not anonymous prose.

Every material model-visible finding should preserve enough identity to support:

```text
what proposition/finding this is
which mechanism/owner produced it
which evidence/provenance supports it
what proof/authority class it carries
what limitation accompanies it
```

The model's explanation should reference those identifiers.

A model-generated synthesis statement does not become factual evidence merely because it is fluent or structured.

The final report should remain able to distinguish:

```text
source observation
product interpretation
model-assisted synthesis
final validated recommendation
```

This distinction is especially important where upstream evidence itself already involved model-derived interpretation and deterministic grounding. Final synthesis must not erase that origin and accidentally upgrade a model-derived premise into independent truth.

---

## 15. Failure and fallback behavior

The first experiment should explicitly pressure at least:

- provider request failure;
- malformed/invalid structured output;
- model selects an unavailable action;
- model references nonexistent evidence;
- model omits mandatory uncertainty/checks;
- model emits unsupported safety language;
- model explanation conflicts with its structured action;
- model output is semantically valid but low quality.

Possible first fallback policy to evaluate:

```text
invalid/unavailable LLM synthesis
→ do not silently repair it into a stronger recommendation
→ expose model-synthesis failure distinctly
→ fall back to the deterministic baseline result when that baseline independently has a valid result
```

If the deterministic baseline itself abstains, the model may not override that abstention unless the accepted permission envelope independently permits a stronger action.

Automatic retries should not be added by default. If evaluation shows transient structured-output/provider errors materially dominate otherwise good behavior, a bounded retry policy can be considered separately.

---

## 16. LangGraph / workflow-engine position

This proposal does **not** currently justify LangGraph for final synthesis.

If the first responsibility is simply:

```text
project semantic evidence
→ compute deterministic permission envelope
→ one structured model call
→ deterministic validate
→ render
```

ordinary Python composition is the simpler credible implementation.

LangGraph or another workflow engine becomes a serious candidate only if observed product pressure later requires meaningful orchestration such as:

```text
initial synthesis
→ detect unresolved contradiction
→ request a bounded additional investigation
→ reacquire/revalidate authority
→ resume synthesis
→ optional human interrupt/approval
→ final result
```

or durable recovery, repeated planning, multiple effectful investigation branches, or other workflow responsibilities that materially exceed ordinary Python composition.

The paused R4 LangGraph work remains valuable architecture/evaluation evidence, but it is not automatic justification for using the framework here.

---

## 17. Relationship to report rendering

The eventual human-readable output should be driven from the validated synthesis result, not from unconstrained free-form model prose.

A useful report shape might expose:

```text
Primary recommendation
Why this is the primary recommendation
What evidence established it
What remains uncertain or conflicting
Required targeted checks / next condition
Important supporting findings
What UpgradePilot is not claiming
Provenance / trace links
```

The model may help prioritize and phrase these sections, but the machine-readable validated result should remain sufficient to reconstruct the semantic recommendation without trusting prose formatting.

This protects CLI/API/report consistency.

---

## 18. Important open design questions

This proposal intentionally leaves several decisions open until the current synthesis semantics are accepted and the deterministic baseline exists.

1. What exact positive permission envelope is required before `merge after normal review` may be offered?
2. Will `investigate or block` remain one external Charter action with one internal sub-disposition, or will the first synthesis contract avoid the distinction?
3. What producer-owned state can legitimately establish `defer` and its rerun trigger?
4. What candidate-discovery/coverage declaration is sufficient for favorable action?
5. Which repository/context facts are genuinely decision-bearing rather than report context?
6. Should the LLM choose among all deterministically permitted actions, or should deterministic logic sometimes designate exactly one action and use the LLM only for reasons/report priority?
7. How much explanation should be structured versus free text?
8. What evidence identifier/provenance projection is smallest but sufficient for grounded synthesis?
9. What is the correct fallback when the LLM proposal is invalid but the deterministic baseline can act?
10. What evaluation rubric can compare decision usefulness without pretending there is objective ground-truth safety for every PR?
11. Does a second dedicated report/presentation model pass ever add enough value to justify the added complexity?
12. What exact observed limitation of the deterministic baseline would be strong enough to activate this experiment under Charter technology-admission rules?

These are future design/evaluation questions, not implementation permissions.

---

## 19. Recommended staged decision sequence

If this proposal is reviewed favorably, the smallest responsible route is:

### Stage A — finish semantic authority first

Accept the first-version synthesis semantics at the correct specification owner:

- action meanings;
- positive prerequisites;
- prohibited stronger actions;
- targeted-check semantics;
- investigation/block distinction if adopted;
- defer future-condition semantics;
- abstention boundary;
- reliability/provenance constraints;
- first-version unavailable actions.

### Stage B — build the transparent deterministic baseline

Implement and prove the current synthesis plan's smallest deterministic method.

The goal is not to prove deterministic rules are permanently superior. The goal is to establish a real product baseline and expose its actual limitations.

### Stage C — record the observed limitation

Do not activate an LLM experiment from preference alone.

Identify concrete baseline pressure such as:

- brittle cross-mechanism composition;
- poor reason prioritization;
- excessive deterministic rule complexity;
- materially worse maintainer usefulness on controlled evaluations;
- inability to generalize decision/report synthesis without fixture-shaped logic.

### Stage D — admit the smallest LLM synthesis experiment

Use ordinary Python first unless workflow pressure independently justifies something larger.

Implement:

```text
bounded evidence projection
+ deterministic permission envelope
+ one structured model synthesis call
+ deterministic validation
+ validated report rendering
```

### Stage E — compare and decide

Use frozen evaluation cases/rubrics and decide explicitly:

```text
adopt
retain as experimental/pilot
reject
or defer
```

If adopted, promote only the accepted stable semantics/method to the proper specification/ADR owners. The experiment/proposal remains provenance.

---

## 20. Explicit non-goals / things not yet to build

This proposal does **not** authorize or recommend building now:

- a generic LLM judge;
- autonomous maintainer actions;
- automatic merge/approval/commenting;
- one universal risk/confidence score;
- a generic policy/rule engine;
- one agent per evidence mechanism;
- multi-agent debate;
- planner + critic + judge chains;
- LangGraph for final synthesis without observed orchestration pressure;
- persistence/checkpointing/HITL merely because agent frameworks support them;
- broad prompt-driven access to raw repository contents;
- vector databases/RAG infrastructure without a demonstrated evidence-retrieval need;
- automatic new investigation actions invented by the final synthesizer;
- LLM repair of upstream evidence-integrity defects;
- LLM authority to override deterministic action restrictions;
- a second report-generation model pass before the one-call baseline proves insufficient;
- promotion of this proposal's semantics into project truth without review.

---

## 21. Candidate architecture in one view

```text
                         TRUSTED / DETERMINISTIC

PublicPullRequestInvestigation + mechanism results + context + problems
                              │
                              ▼
                    DecisionEvidenceBundle
                              │
                              ▼
                  DecisionPermissionEnvelope
             ┌────────────────┼─────────────────┐
             │ permitted       │ mandatory       │ prohibited
             │ actions         │ limits/checks   │ actions
             └────────────────┼─────────────────┘
                              │
                              ▼
                         MODEL BOUNDARY

                  structured LLM synthesis
                   action + reason refs
                 uncertainty + check refs
                    report priorities
                              │
                              ▼
                         UNTRUSTED RESULT

                              │
                              ▼
                    deterministic validator
                              │
                ┌─────────────┴─────────────┐
                │ valid                     │ invalid
                ▼                           ▼
       ValidatedDecisionSynthesis     model-synthesis failure
                │                           │
                ▼                           └─> deterministic fallback
       deterministic/report renderer
                │
                ▼
       maintainer-facing decision report
```

The central design thesis is:

> **Use the LLM where UpgradePilot needs bounded semantic composition and human-oriented prioritization; keep deterministic code responsible for what conclusions/actions are epistemically and operationally allowed.**

---

## 22. Final recommendation

This proposal should be kept as a **candidate future synthesis method and experiment direction**, not immediately promoted into the active implementation plan.

The current synthesis work should continue far enough to establish the accepted semantic/permission boundary and transparent deterministic baseline. That work is not wasted if an LLM method later wins; it becomes the trusted authority envelope, fallback, evaluation baseline, and technology-admission evidence that make the LLM method defensible.

The paused `EvidenceGapPlanner` work provides a particularly valuable reusable architectural lesson:

```text
bounded model observation
+
model proposal rather than authority
+
trusted deterministic validation/admission
+
explicit failure semantics
```

The final maintainer synthesis responsibility appears to be a strong second place to test that pattern—this time not for choosing what evidence to investigate next, but for composing already-earned evidence into a bounded maintainer recommendation and uncertainty-aware report.

No source implementation, LangGraph adoption, specification promotion, plan replacement, or live-route change is justified by this proposal alone.
