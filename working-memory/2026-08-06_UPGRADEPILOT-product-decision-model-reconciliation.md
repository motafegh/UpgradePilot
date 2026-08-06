# UpgradePilot Product Decision-Model Reconciliation Working Record

**Date opened:** 2026-08-06  
**Last discussion sync:** 2026-08-06  
**Status:** Active design discussion; Conversation A in progress; no final whole-product model yet  
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
   - provisional discussion conclusion;
   - accepted new decision.
5. Do not modify the charter, route, active decision plan, specifications, ADRs, or source behavior until the discussion has produced a sufficiently coherent accepted model.
6. When a final product-model decision is accepted, record exactly which active files must be retained, amended, superseded, archived, or newly created.
7. Preserve disagreement and rejected alternatives when they materially explain the final design.
8. Do not force every discussion conclusion immediately into a source enum, schema, class hierarchy, or implementation pattern. First settle the domain model and relationships.

## 3. Repository material inspected at opening

The opening audit considered the active controls and relevant historical/proposal evidence most likely to shape the decision model.

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
- source authority/provenance and semantic meaning are separate responsibilities;
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

The completed Target-Python milestone now implements one real instance of this shape:

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

The discussion identified a deeper problem: even replacing `merge_after_normal_review` with `proceed_to_normal_review` may still embed undefined repository-specific semantics. “Normal review” differs materially between repositories and is not currently modeled as a stable UpgradePilot-owned process.

Therefore the question is no longer merely **what should the first action be renamed?** It is:

> Should these five action classes remain the primary product contract at all, or should they become one projection of a richer investigation/decision state?

No final answer is accepted yet.

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

The discussion has since strengthened this hypothesis and refined the likely middle into impact-specific reasoning rather than a direct evidence-to-action mapping.

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

The discussion proceeds through four connected questions. These are deliberately whole-product questions rather than stage-limited implementation tasks.

### Conversation A — Dependency-update impact/problem model

> What major classes of impact, incompatibility, uncertainty, or concern can a dependency update introduce, and what should “impact” mean in UpgradePilot?

Current status: **in progress; foundational semantics and materiality are provisionally accepted; exposure-surface mapping is next.**

### Conversation B — Applicability and investigation activation

> How should UpgradePilot determine which possible impacts actually matter to this exact repository, revision, dependency path, environment, and policy?

Likely shape:

```text
potential impact
→ activation condition
→ exact target surface/evidence
→ presence / absence / uncertainty
→ applicable / not applicable / unresolved / conflicted
```

This conversation must distinguish deterministic evidence, semantic interpretation, bounded negative evidence, conflicts, and model-assisted extraction.

### Conversation C — Best next investigation/check

> When material uncertainty remains, how should UpgradePilot decide what additional evidence or check is worth acquiring, executing, or recommending?

Questions include:

- what makes an unresolved question decision-relevant;
- when another investigation can discriminate between materially different outcomes;
- targeted check versus broad testing;
- expected information value and cost/latency;
- when no available supported check is useful;
- whether UpgradePilot performs a safe investigation, recommends a check, or stops.

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
13. **Complexity control:** Are we modeling stable domain relationships, or accidentally multiplying case/package-specific rules?

## 8. Current hypotheses — not final decisions

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

This does not mean every future impact should use the same source-code structure or LLM method.

### H7 — A flat impact taxonomy is probably the wrong final model

A list such as `API / security / platform / performance / CI` mixes distinct dimensions such as change mechanism, target exposure, consequence, and evidence. A multidimensional model appears more general and less prone to combinatorial rule growth.

## 9. Decisions and provisional conclusions accepted so far

### D-001 — Create and use this reconciliation record

**Accepted:** 2026-08-06

Preserve the whole-product design discussion in one dated working-memory record before modifying controlling artifacts or implementing the next decision layer.

### D-002 — Do not use stage boundaries to constrain whole-product reasoning

**Accepted:** 2026-08-06

B2/B3/B4 and other route stages may later determine implementation order and proof gates. They do not prevent discussing or designing the best whole-product model during this reconciliation.

### D-003 — Audit old documents as evidence, not automatic authority for new design

**Accepted:** 2026-08-06

Historical simulations, old decision drafts, and proposals may contain valuable discoveries or misleading assumptions. Each must be evaluated against the current implemented evidence model and present product goals.

### D-004 — Upstream change is not itself target impact

**Provisional design conclusion accepted for continued discussion:** 2026-08-06

A dependency can change upstream without that change materially affecting the target repository. UpgradePilot must not collapse:

```text
upstream change
=
target impact
```

The target relationship must be established separately.

### D-005 — Preserve potential impact versus target applicability

**Provisional design conclusion accepted for continued discussion:** 2026-08-06

A potential impact is a credible mechanism by which an upstream change could affect a consumer/target. It becomes target-applicable only when the relevant activation condition intersects the exact repository/context. Non-applicability closes only that bounded impact path; it does not establish global compatibility or safety.

### D-006 — Activation condition is a central domain concept

**Provisional design conclusion accepted for continued discussion:** 2026-08-06

An **activation condition** is the condition that must hold in the target for a potential upstream change to matter.

Examples:

```text
Python 3.8 support removed
→ activation condition: target requires/supports Python 3.8

API foo() removed
→ activation condition: target reaches/uses foo()

behavior changes under --doctest-modules
→ activation condition: target enables the affected doctest mode/context
```

The condition may later be established, refuted, remain unresolved, or be unsupported by the available method.

### D-007 — Dependency impact and unrelated PR/repository condition must remain distinguishable

**Provisional design conclusion accepted for continued discussion:** 2026-08-06

A PR can have conditions that affect handling without being caused by the dependency update. For example, failing CI does not by itself prove a negative dependency impact. The future model must preserve the distinction between:

```text
dependency-update impact/assessment
```

and

```text
PR/repository condition or action constraint
```

until evidence justifies linking them causally.

### D-008 — Materiality is decision-relative, not equivalent to severity or likelihood

**Provisional design conclusion accepted for continued discussion:** 2026-08-06

A potential impact is material when resolving whether it applies could materially change what the maintainer needs to know, investigate, verify, or act on, including important uncertainty or the maintainer-facing result.

Preserve these distinctions:

```text
severity != materiality
likelihood != materiality
interesting != material
material != harmful
```

A severe upstream change may be immaterial to a target whose activation condition is absent; a subtle change may be highly material when it intersects critical target behavior.

A useful conceptual test is counterfactual:

> If this impact were present versus absent, could a material investigation state, required check, uncertainty, or maintainer-facing result change?

If not, it normally should not consume deeper investigation.

### D-009 — Control variation through domain abstractions, not case-specific rules

**Provisional design conclusion accepted for continued discussion:** 2026-08-06

Real-world values such as repository names, package names, versions, PR numbers, API symbols, and commit SHAs may be effectively unbounded. That does not require one rule per value.

Prefer:

```text
many external values/forms
→ representation-specific acquisition/extraction
→ validation + normalization
→ stable domain concepts
→ focused evaluators/predicates
→ general composition rules
→ conditional activation/pruning
→ bounded semantic states
```

Distinguish:

- **value variation** — many concrete values, normally data;
- **state variation** — a smaller set of meaningful semantic states;
- **structural variation** — genuinely different representations/mechanisms that may require specialized adapters/extractors before converging on shared domain contracts.

Related reusable learning is preserved in:

- `../learning/concepts/managing-combinatorial-complexity-in-upgradepilot.md`

### D-010 — Do not force one flat impact-category enum yet

**Provisional design conclusion accepted for continued discussion:** 2026-08-06

The earlier list of API, behavior, platform, dependency, build, security, performance, CI, and similar categories mixes different conceptual layers. Do not freeze it directly as one `ImpactKind` or equivalent.

The emerging model should separate at least these dimensions:

```text
1. upstream change mechanism — what changed?
2. target exposure surface — where could the target encounter it?
3. activation condition — what must be true for it to matter?
4. possible consequence — what could happen if activated?
5. target applicability — does the condition hold here?
6. evidence/coverage state — what supports, refutes, covers, conflicts with, or leaves the impact unresolved?
```

Materiality, uncertainty, and repository-policy relevance may later be additional dimensions. These are conceptual domain dimensions, not approved runtime fields yet.

### D-011 — Evidence such as CI is not automatically an impact

**Provisional design conclusion accepted for continued discussion:** 2026-08-06

CI, tests, source/configuration inspection, package metadata, and upstream documents often provide **evidence about an impact proposition** rather than constituting the impact itself.

Example:

```text
API removed
→ target uses API
→ CI exercises affected path
→ pass/fail result provides evidence about consequence/coverage
```

A tooling dependency may make CI/test behavior itself an exposure surface, so roles remain contextual; nevertheless, evidence and impact must not be collapsed by default.

## 10. Conversation-A discussion log

### 2026-08-06 — What should “impact” mean?

**Question**  
Should UpgradePilot reason directly from an upstream change to a PR decision, or distinguish the target-specific path through which that change matters?

**Current conclusion**  
Use an impact lifecycle rather than treating upstream change as target consequence:

```text
upstream change
→ potential impact
→ activation condition
→ target applicability
→ evidence/coverage
→ bounded closure or unresolved/conflicted state
```

A dependency update can have negative, neutral, beneficial, or uncertain consequences. “Problem” is therefore too narrow as the primary concept.

**Effect**  
The future decision model should reason over multiple impact paths and their states before synthesizing a maintainer-facing result.

### 2026-08-06 — What makes an impact material?

**Question**  
How can UpgradePilot avoid investigating every upstream change while still preserving important ones?

**Current conclusion**  
Materiality is relative to whether resolving an impact can change something decision-relevant. Use activation and counterfactual reasoning to prune paths that cannot materially alter the investigation, uncertainty, required checks, or final result.

**Effect**  
Materiality and stopping share one principle: spend work only on questions capable of changing a meaningful result.

### 2026-08-06 — How can the project handle huge numbers of packages, versions, cases, and combinations?

**Question**  
Does real-world variation imply an unmanageable number of handwritten rules?

**Current conclusion**  
No. The architecture should compress concrete variation into stable domain abstractions, normalize representation differences, decompose independent responsibilities, use general predicates/composition rules, prune inactive branches, preserve finite semantic states, and allow unsupported/unresolved outcomes.

**Effect**  
Future impact-map design should search for stable relationships under many concrete cases, not package- or fixture-specific branches.

### 2026-08-06 — Flat taxonomy versus multidimensional impact model

**Question**  
Should API, security, platform, performance, CI, dependency relationships, build, and similar concepts become one list of impact types?

**Current conclusion**  
Probably not. The list mixes what changed, where the target encounters it, what consequence may follow, and what evidence observes it. Separate those dimensions before deciding any eventual runtime representation.

**Effect**  
The next task is to define the **target exposure surfaces** cleanly enough to test this multidimensional model.

## 11. Current conceptual map and onboarding checkpoint

### 11.1 Where we are

```text
Conversation A — What could matter?              IN PROGRESS
Conversation B — Does it matter here?            NOT YET STARTED PROPERLY
Conversation C — What should we investigate?     NOT YET STARTED
Conversation D — Do we know enough / output?     NOT YET STARTED
```

Conversation A has already established the provisional concepts of upstream change versus target impact, potential versus applicable impact, activation conditions, decision-relative materiality, complexity control through reusable abstractions, and the need for a multidimensional rather than flat taxonomy.

### 11.2 Current whole-product reasoning sketch

```text
public dependency-update PR
↓
exact dependency/version identity
↓
upstream changes
↓
for each material candidate:
    change mechanism
    + potential target exposure
    + activation condition
    + possible consequence
↓
exact target evidence
↓
applicable / not applicable / unresolved / conflicted
↓
evidence / coverage / contradiction state
↓
remaining decision-relevant questions
↓
next useful investigation/check OR justified non-activation
↓
sufficiency / stopping
↓
policy-aware maintainer-facing synthesis
```

This is a discussion model, not an approved pipeline or schema.

### 11.3 Immediate unanswered question

> **What are the major target exposure surfaces through which an upstream dependency change can actually reach or matter to a repository?**

The next discussion should define and challenge candidate surfaces such as:

- source/API usage;
- configuration;
- dependency resolution/installation;
- runtime/language/platform environments;
- data/protocol boundaries;
- tests and development tooling;
- CI/build/release execution;
- generated artifacts or other mediated paths.

Do not accept this candidate list yet. The purpose of the next discussion is to determine whether these are truly distinct exposure surfaces, whether some are consequences/evidence rather than exposure, and what important surfaces are missing.

### 11.4 Questions deliberately deferred to later conversations

Do not prematurely solve these while defining exposure surfaces:

- exact applicability state vocabulary;
- how negative evidence proves bounded absence;
- detailed LLM role for arbitrary upstream change semantics;
- targeted-check ranking or Value of Information method;
- repository-policy schema;
- final sufficiency rules;
- final maintainer-facing action vocabulary;
- whether the historical five action classes survive;
- final runtime classes/enums/schema;
- implementation sequence and ADR changes.

## 12. Final decisions and repository-change register

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

## 13. Immediate continuation

Continue **Conversation A — Dependency-update impact/problem model** from the current checkpoint.

Next question:

> **What are the major target exposure surfaces through which an upstream dependency change can actually reach or matter to a repository?**

Continue in small connected teaching/design chunks. Challenge overlaps, distinguish exposure from consequence and evidence, and use real project cases only to clarify general domain relationships rather than constrain them.