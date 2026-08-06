# UpgradePilot Product Decision-Model Reconciliation Working Record

**Date opened:** 2026-08-06  
**Status:** Active design discussion; no final product-model decision yet  
**Purpose:** Preserve the current whole-product decision-model audit, debates, alternatives, discoveries, and eventual accepted changes before modifying controlling product artifacts or implementing the next decision layer.  
**Live-state owner:** `../MEMORY.md` remains the sole owner of current project position and exact continuation.

## 1. Why this record exists

UpgradePilot has just completed the bounded Target-Python Support Relevance responsibility through the normal live product path. The implementation now has materially stronger evidence, authority, grounding, relevance, and failure behavior than when the earlier transparent-decision documents and product-simulation conclusions were written.

Before implementing a maintainer-decision method, Ali and the AI assistant agreed to step back and examine the whole product model rather than mechanically inheriting historical action labels or decision assumptions.

This record exists so that the discussion does not remain only in chat and does not drift across sessions. It should preserve:

- observations from current repository controls and historical discovery evidence;
- hypotheses and competing product models;
- Ali's questions, objections, and design intuitions;
- technical pushback where appropriate;
- distinctions between historical evidence and active controlling intent;
- unresolved questions;
- decisions only when actually accepted;
- the final repository changes required after the design is settled.

This is a **working-memory evidence and design record**, not a new controlling specification, ADR, charter, or implementation plan.

## 2. Discussion discipline

During this reconciliation:

1. Do not treat stage names such as B2/B3/B4 as limits on whole-product reasoning. Stage boundaries may later control implementation sequence, but they must not prevent designing the right product model.
2. Do not inherit historical simulation outcomes, action labels, report schemas, or prior decision drafts merely because they were previously accepted for discovery work.
3. Do not discard historical artifacts either. Treat them as evidence of earlier observations, contrasts, and useful patterns.
4. Separate:
   - stable principle;
   - historical discovery;
   - current implementation truth;
   - proposal/hypothesis;
   - accepted new decision.
5. Do not modify the charter, route, active decision plan, specifications, ADRs, or source behavior until the discussion has produced a sufficiently coherent accepted model.
6. When a final product-model decision is accepted, record exactly which active files must be retained, amended, superseded, archived, or newly created.
7. Preserve disagreement and rejected alternatives when they materially explain the final design.

## 3. Repository material inspected at opening

The opening audit considered the active controls and relevant historical/proposal evidence most likely to shape the decision model:

### Active controlling or normative material

- `PROJECT_CHARTER.md`
- `README.md`
- `plans/UPGRADEPILOT_90_DAY_PLAN.md`
- `plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md`
- `MEMORY.md`
- `docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`
- `docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`
- `docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md`
- `AGENTS.md`

### Historical discovery/design evidence

- `product-simulation/TRANSPARENT_BASELINE_SPECIFICATION.md`
- `product-simulation/D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md`
- `product-simulation/SCENARIO_COVERAGE.md`
- `product-simulation/S003_POST_CASE_SYNTHESIS.md`
- `product-simulation/S004_POST_CASE_SYNTHESIS.md`
- `product-simulation/S005_POST_CASE_SYNTHESIS.md`
- `product-simulation/RUNTIME_ARTIFACT_SPECIFICATION.md`
- `working-memory/2026-07-28_B2-transparent-decision-method.md`
- `working-memory/2026-07-28_B2-decision-evidence-map-and-contract-draft.md`

### Non-controlling future proposal

- `proposals/2026-07-20_UPGRADEPILOT_PRODUCT_AMBITION_AND_ENHANCEMENT_PROPOSAL.md`

The source/tests remain the authority for implemented behavior. The most recent implemented milestone is preserved separately in `2026-08-05_B2-step-7f-normal-path-live-s001-proof.md` and `MEMORY.md`.

## 4. Opening audit — major discoveries

### 4.1 Stable principles that still appear sound

The strongest existing product principles remain valuable and should not be casually discarded:

```text
observation
!= interpretation
!= evidence quality
!= decision
```

and, where applicable:

```text
source/raw evidence
→ parsed/normalized evidence
→ attributed claim or deterministic interpretation
→ grounding/corroboration/conflict state
→ finding or decision input
→ bounded output
```

Other stable principles that remain strong:

- exact proposal, dependency, version, source, time, and revision identity matter;
- provenance/authority and semantic meaning are separate responsibilities;
- missing, inaccessible, stale, conflicting, invalid, rejected, unsupported, and not-applicable states must remain distinguishable where relevant;
- model output cannot assign its own authority or permitted decision effect;
- absence of a model-derived claim is not evidence that no relevant risk exists;
- conditional analysis and explicit non-activation are first-class results;
- investigation should stop when further supported work cannot materially change action, uncertainty location, required checks, or another decision-relevant result;
- repository policy and residual-risk acceptance remain human/repository responsibilities unless explicitly represented through trustworthy policy evidence.

### 4.2 The repository already contains part of the future problem map

Historical D1/S003–S005 discovery work identified many recurring or conditional dependency-update problem families, including:

- advisory/exploitability questions;
- adapter or framework compatibility;
- upstream activation-condition mapping;
- target source/configuration relevance;
- dependency role and execution path;
- CI dependency identity and execution authority;
- matrix/repeated execution comparison;
- causal failure attribution;
- semantic-version and peer-range compatibility;
- dynamic or isolated reproduction;
- environment/platform/native/compiler/toolchain concerns;
- stopping and investigation-cost/value reasoning;
- dependency-update assessment versus repository/PR action divergence.

These are not final product categories merely because simulations observed them, but they are valuable discovery evidence and should inform the new map.

### 4.3 A highly reusable historical reasoning pattern was discovered

S005 articulated a pattern that aligns closely with the current implementation direction:

```text
upstream statement/change
→ activation condition
→ target configuration/source/usage surface
→ execution or evidence coverage
→ unresolved question OR closure
```

The recently completed Target-Python milestone now implements one real instance of this shape:

```text
upstream Python support drop
→ affected Python line
→ exact target requires-python declaration
→ deterministic applicability/relevance result
```

This suggests that the distinctive middle of UpgradePilot may be better modeled around **impact, activation, applicability, coverage, uncertainty, and investigation** than around a five-class action mapping alone.

### 4.4 The active five-action framing may be too early or too coarse

The active charter and README currently frame the supported product decision as:

1. merge after normal review;
2. run targeted checks;
3. investigate or block;
4. defer;
5. abstain.

The current transparent-decision plan is organized around preserving these broad meanings.

The discussion has identified a deeper problem: even replacing `merge_after_normal_review` with `proceed_to_normal_review` may still embed undefined repository-specific semantics. “Normal review” differs materially between repositories and is not currently modeled as a stable UpgradePilot-owned process.

Therefore the question is no longer merely **what should the first action be renamed?** It is:

> Should these five action classes remain the primary product contract at all, or should they become one projection of a richer investigation/decision state?

No answer is accepted yet.

### 4.5 The historical July decision-contract draft is useful but stale

The July 28 draft already proposed a richer result containing concepts such as:

- maintainer action;
- evidence readiness;
- decisive/supporting reasons;
- unresolved questions;
- conflicting evidence;
- required checks;
- inactive investigations;
- stopping reason;
- claim limits;
- rerun conditions.

It also proposed `proceed_to_normal_review` as a clearer label.

However, the current discussion has already challenged the underlying “normal review” concept, and the draft predates the completed Target-Python relevance architecture, local semantic-grounding boundary, current source topology, and recent live integration lessons. It should therefore be treated as design evidence rather than a contract to implement unchanged.

### 4.6 Historical case actions are not current machine truth

The product-simulation scenario register historically recorded actions such as S001 `merge after normal review`.

The current real product path is stricter. For S001 it now establishes:

```text
CI dependency exercise:
unresolved / dependency_exercise_not_proven

upstream support-drop claim:
grounded Python 3.8 drop introduced in Soup Sieve 2.8

target declaration:
requires-python >=3.10

relevance:
outside_declared_python_range
```

This proves one material concern is outside the target declaration. It does **not** reproduce the historical manual decision label, and the historical label must not be treated as an automatic training/validation truth for the new machine.

This is a major calibration lesson: improved evidence standards can invalidate or narrow earlier human/AI simulation assumptions without making the historical work useless.

### 4.7 The transparent baseline remains a comparator, not the product architecture

The simulation transparent baseline intentionally uses only coarse features such as:

```text
version category
+ overall CI conclusion
+ dependency directness
+ literal release-note keywords
→ coarse action
```

S004 showed that this baseline may sometimes be sufficient after authority-critical assumptions are confirmed. S005 showed that it can be wrong in the cautious direction when release-note caution does not activate on the target.

Therefore the baseline remains valuable for comparison, stopping, and measuring whether deeper analysis adds decision value. It should not shape the full product merely because it already produces five action labels.

### 4.8 The non-controlling ambition proposal contains ideas newly worth reconsidering

The 2026-07-20 product-ambition proposal is explicitly non-controlling, but several of its concepts align strongly with what the current implementation has now demonstrated:

- an Upgrade Impact Graph or equivalent impact model;
- a Decision-Time Machine / temporal evidence model;
- a Targeted Check Planner;
- Maintainer Policy Profiles;
- multidimensional uncertainty;
- an Evidence Sufficiency Engine;
- counterfactual explanations.

These are not adopted requirements. However, the proposal's higher-level product identity — an evidence-driven dependency-update decision laboratory and maintainer investigation system — may now fit the observed system better than a simple evidence-to-five-class mapping.

The discussion must evaluate these ideas independently rather than adopting them because they were proposed earlier.

### 4.9 The likely missing middle of the active product model

A major opening hypothesis is that active documents currently compress too much between “evidence” and “decision.”

A richer conceptual sequence may be:

```text
EVIDENCE
↓
POTENTIAL IMPACTS / CONCERNS
↓
ACTIVATION CONDITIONS
↓
TARGET APPLICABILITY
↓
COVERAGE / CONTRADICTIONS / UNCERTAINTY
↓
OPEN DECISION-RELEVANT QUESTIONS
↓
BEST NEXT INVESTIGATION OR CHECK
↓
STOPPING / SUFFICIENCY
↓
MAINTAINER-FACING OUTPUT / ACTION
```

This is a hypothesis for discussion, not an accepted architecture.

## 5. Why implementation should pause during this reconciliation

The next active plan currently points toward a Transparent Decision Method. The recent implementation progress has materially changed the evidence available to that method and exposed assumptions that were not visible when the plan was written.

Implementing the old decision draft immediately risks encoding stale concepts such as:

- action labels whose operational meaning is not owned by UpgradePilot;
- overreliance on historical simulation decisions;
- insufficient separation between impact analysis and final action;
- a too-direct evidence-to-action mapping;
- missing first-class treatment of investigation selection and stopping;
- unclear repository-policy sensitivity.

Therefore, no new decision/recommendation source behavior should be implemented until this reconciliation reaches a coherent accepted model.

## 6. Four major product-model conversations

The discussion will proceed through four connected questions. These are deliberately whole-product questions rather than stage-limited implementation tasks.

### Conversation A — Dependency-update impact/problem model

> What major classes of impact, incompatibility, uncertainty, or concern can a dependency update introduce, and what should “impact” mean in UpgradePilot?

Topics likely to include:

- runtime/language/platform support;
- API and behavioral changes;
- dependency/constraint/peer relationships;
- security/advisory effects;
- target usage and configuration;
- CI/test/environment coverage;
- supply-chain/source/provenance concerns;
- temporal and policy sensitivity;
- failures unrelated to the dependency update;
- unknown/unsupported impact classes.

The goal is not to create an exhaustive checklist. It is to find a product-meaningful taxonomy or model that supports selective investigation.

### Conversation B — Applicability and investigation activation

> How should UpgradePilot determine which possible impacts actually matter to this exact repository, revision, dependency path, environment, and policy?

Potential structure:

```text
upstream/change signal
→ activation condition
→ target surface/path
→ evidence of presence/absence/uncertainty
→ activate, close, or leave unresolved
```

This conversation must distinguish deterministic evidence, semantic interpretation, bounded negative evidence, conflicts, and model-assisted extraction.

### Conversation C — Best next investigation/check

> When material uncertainty remains, how should UpgradePilot decide what additional evidence or check is worth acquiring, executing, or recommending?

Questions include:

- what makes an unresolved question decision-relevant;
- when another investigation can actually discriminate between materially different outcomes;
- targeted check versus broad testing;
- expected information value and cost/latency;
- when no available supported check is useful;
- whether UpgradePilot recommends a check, performs a safe read-only investigation, or stops.

### Conversation D — Sufficiency, stopping, and maintainer-facing result

> When does UpgradePilot know enough to stop, and what exactly should it tell the maintainer?

This is where the project should finally settle:

- evidence sufficiency relative to claims/actions;
- contradictions and unresolved states;
- stopping conditions;
- counterfactual/rerun conditions;
- repository-policy sensitivity;
- whether one or more decision dimensions are needed;
- what action vocabulary, if any, is primary;
- how “no additional UpgradePilot-specific action” should be represented;
- whether the five charter action families survive, change, or become a projection of richer state.

## 7. Cross-cutting questions to preserve throughout all four conversations

These questions should not be lost while discussing individual categories:

1. **Product value:** What does UpgradePilot add beyond a competent maintainer manually opening a few pages?
2. **Scale/repeatability:** Which benefits emerge from consistent repeated execution across many dependency PRs?
3. **Authority:** Which facts are authoritative, attributed, merely grounded, corroborated, contradictory, or unresolved?
4. **Negative evidence:** What can absence/search/CI non-observation actually establish, and with what boundary?
5. **Repository policy:** Which decision depends on repository-specific policy rather than universal engineering fact?
6. **Temporal validity:** What was knowable at the decision point, and what evidence appeared later?
7. **Model role:** Where can an LLM interpret natural-language source content without owning authority, applicability, or final action?
8. **Stopping:** When does more analysis stop adding material value?
9. **Actionability:** Can the system name a concrete next question/check rather than only assigning risk?
10. **Generality:** Would the method still make sense on a changed package/repository/case, or is it silently an S001/S004/S005 detector?
11. **Human authority:** Which judgments must remain explicitly with maintainers?
12. **Explainability:** Can every material conclusion be traced to exact evidence and transformation boundaries?

## 8. Current hypotheses — not decisions

The following hypotheses are explicitly open to challenge:

### H1 — Impact/investigation may be more central than five-class recommendation

UpgradePilot may be better represented as an evidence-driven impact and investigation system whose final action is derived from richer state, rather than as a classifier whose primary task is to map evidence into five labels.

### H2 — Action classes may become a projection

The historical action families may remain useful as maintainer-facing summaries, but they may not be sufficient as the central internal decision model.

### H3 — “Normal review” may not be an UpgradePilot-owned concept

Unless repository policy is explicitly modeled, UpgradePilot may be unable to define “normal review” precisely enough for it to be a clean primary runtime action.

### H4 — Targeted investigation is a core value proposition

A major product advantage may be deciding **what question matters next**, **what evidence/check can answer it**, and **when not to investigate further**, rather than merely automating manual evidence collection.

### H5 — Existing historical simulations remain design evidence, not labels

S001–S005 should be replayed/reasoned against the new model when appropriate, but their historical action outputs must not silently become ground truth.

### H6 — Current implementation is one proven impact slice

The completed Python-support relevance path may serve as a concrete prototype for a wider impact/applicability architecture:

```text
upstream change
→ activation dimension
→ exact target evidence
→ applicability/relevance
→ closure or unresolved state
```

This does not mean every future impact should use the same source code structure or LLM method.

## 9. Decisions accepted so far

### D-001 — Create and use this reconciliation record

**Accepted:** 2026-08-06

Preserve the whole-product design discussion in one dated working-memory record before modifying controlling artifacts or implementing the next decision layer.

### D-002 — Do not use stage boundaries to constrain whole-product reasoning

**Accepted:** 2026-08-06

B2/B3/B4 and other route stages may later determine implementation order and proof gates. They do not prevent discussing or designing the best whole-product model during this reconciliation.

### D-003 — Audit old documents as evidence, not automatic authority for new design

**Accepted:** 2026-08-06

Historical simulations, old decision drafts, and proposals may contain valuable discoveries or misleading assumptions. Each must be evaluated against the current implemented evidence model and present product goals.

No other substantive product-model decision is accepted yet.

## 10. Open decision log

Append material discussions here progressively using this pattern:

### YYYY-MM-DD — <topic>

**Question**  
What exactly are we trying to decide?

**Existing evidence / prior assumptions**  
What do current implementation, controlling docs, historical cases, or proposals suggest?

**Ali's position / questions**  
What concern, alternative, or intuition was raised?

**Technical analysis / pushback**  
What follows technically, including disagreement where justified?

**Alternatives considered**  
What credible models or choices were compared?

**Current conclusion**  
Accepted / rejected / deferred / still open.

**Effect**  
What later question, document, architecture, implementation, test, or learning work changes because of this?

## 11. Final decisions and repository-change register

**Status:** Pending reconciliation.

When the four conversations reach sufficient closure, this section must contain:

1. accepted whole-product problem/impact model;
2. accepted applicability/activation model;
3. accepted investigation/check-selection model;
4. accepted sufficiency/stopping model;
5. accepted maintainer-facing output/action model;
6. terminology decisions;
7. repository-policy boundary;
8. temporal/decision-time boundary;
9. model/LLM authority boundary;
10. required changes to controlling artifacts;
11. required new or superseding specifications/ADRs;
12. implementation responsibilities and sequence;
13. test/evaluation implications;
14. historical files that remain evidence only;
15. explicit non-goals and rejected alternatives.

Potential files to reassess after decisions — **not authorized for modification yet**:

- `PROJECT_CHARTER.md`
- `README.md`
- `plans/UPGRADEPILOT_90_DAY_PLAN.md`
- `plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md`
- applicable files under `docs/specifications/`
- possibly a new ADR if a consequential decision architecture/method is accepted
- `MEMORY.md` for final live continuation
- source/tests only after product/model decisions are accepted and implementation is selected

## 12. Immediate continuation

Begin **Conversation A — Dependency-update impact/problem model**.

Start from the whole dependency-update problem rather than from the existing five action labels:

> What can actually go wrong, change, become uncertain, or become newly relevant when a dependency is updated, and which of those distinctions are useful enough for UpgradePilot to model?

Do not try to finalize the entire taxonomy in one pass. Build it in connected chunks, challenge overlaps and missing categories, and use real examples such as S001/S003/S004/S005 when they clarify rather than constrain the model.
