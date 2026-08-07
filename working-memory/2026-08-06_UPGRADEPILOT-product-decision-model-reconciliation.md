# UpgradePilot Product Decision-Model Reconciliation Working Record

**Date opened:** 2026-08-06  
**Last discussion sync:** 2026-08-07  
**Status:** Active design discussion; Conversation A nearing closure review; no final whole-product model yet  
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
9. Bound reconciliation by **decision need**, not theoretical completeness. A conceptual question is discussed now only when its answer is necessary to make the next product, architecture, evidence-contract, or implementation decision correctly.
10. When a question is interesting but not decision-blocking, record or defer it rather than allowing it to open another unbounded design branch.
11. After each major conversation, explicitly ask whether further conceptual work is now lower-value than implementing, evaluating, or testing the model against real evidence.
12. Prefer the project loop:

```text
real evidence
→ identify foundational ambiguity
→ resolve only the necessary semantics
→ implement / evaluate
→ learn from behavior
→ refine
```

over either premature coding or prolonged architecture without feedback.

A practical discuss-now/defer test is:

```text
new conceptual question
↓
Would the answer materially change the next
product / architecture / evidence-contract / implementation decision?
├── yes → resolve now
└── no  → record/defer until a real case or implementation need activates it
```

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

### Parallel non-controlling simulation evidence reviewed during this discussion

The parallel branch `agent/product-simulation-case-screening-01` was reviewed after it synchronized with `main` commit `093c762e88ef70c6a66e5a09575765cf8c0e9d27`.

Relevant branch evidence includes:

- `product-simulation/PRODUCT_SIMULATION_RECALIBRATION_2026-08-06.md`;
- `product-simulation/CASE_SELECTION_FRAMEWORK_V2.md`;
- `product-simulation/S006_POST_CASE_SYNTHESIS.md`;
- `product-simulation/DECISION_MODEL_HANDOFF_2026-08-07.md`.

The latest reviewed branch handoff commit was `0206cfd3caa99657ac49947167e313794a38d035` (`Add product-simulation handoff for exposure-surface discussion`). These artifacts remain simulation/discovery evidence only; they do not settle the reconciliation.

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

This pause is not authorization for open-ended architecture work. Once a conversation has enough semantic stability to support the next correct implementation or evaluation step, implementation feedback should be reconsidered rather than waiting for theoretical completeness across the whole future product.

## 6. Four major product-model conversations

The discussion proceeds through four connected questions. These are deliberately whole-product questions rather than stage-limited implementation tasks.

### Conversation A — Dependency-update impact/problem model

> What major classes of impact, incompatibility, uncertainty, or concern can a dependency update introduce, and what should “impact” mean in UpgradePilot?

Current status: **nearing closure review.** Foundational impact/materiality semantics are provisionally accepted; exposure has been separated from activation/consequence/evidence; technical impact has been bounded from trust/authority, identity/freshness, policy/governance/licensing, and other non-impact decision context. One semantic-compression question remains before an explicit A closure review.

### Conversation B — Applicability and investigation activation

> How should UpgradePilot determine which possible impacts actually matter to this exact repository, revision, dependency path, environment, and policy?

Likely shape:

```text
potential impact
→ activation condition
→ exact target relationship/evidence
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

### 6.1 Conversation stop discipline

The four conversations are **decision checkpoints**, not research programs. They stop when enough domain structure exists to make the next product or implementation decision correctly.

#### Conversation A stop line

A can close when:

1. technical impact has a usable boundary;
2. upstream change, exposure, activation, consequence, applicability, and evidence are distinguishable enough for the next design step;
3. important neighboring non-impact concerns are not being misclassified as technical impact;
4. the model survives representative current/historical cases without fixture-specific distortion;
5. unresolved details can safely be deferred;
6. no remaining ambiguity would make the next applicability model fundamentally wrong.

A does **not** require:

- a complete impact taxonomy;
- every ecosystem/platform/security/build case;
- final graph representation;
- final exposure enum or type hierarchy;
- detailed policy/compliance architecture;
- detailed temporal/freshness implementation;
- universal package-manager behavior;
- final runtime schema/classes.

Current A closure sequence:

```text
1. clarify whether upstream change / potential impact / consequence
   are genuinely distinct concepts or contain avoidable redundancy
↓
2. perform Conversation-A closure review
↓
3. if coherent → move to Conversation B
↓
4. if a genuine foundational contradiction appears
   → resolve only that contradiction
   → rerun A closure review
```

#### Conversation B stop line

B can close when the model can represent and reason about target applicability with clear activation propositions, meaningful positive/negative/unresolved/conflicted states, and explicit deterministic-versus-semantic evidence boundaries.

B does **not** require learning or implementing every possible repository inspection method, language ecosystem, package manager, or configuration grammar.

#### Conversation C stop line

C can close when UpgradePilot has a sufficiently general bounded method for identifying a decision-relevant unresolved question, selecting or recommending a discriminating investigation/check, and recognizing when no supported additional check is worth doing.

C does **not** require solving autonomous debugging, universal test generation, or arbitrary repository experimentation.

#### Conversation D stop line

D can close when evidence sufficiency, stopping, unresolved/conflicting state, repository-policy interaction, and maintainer-facing synthesis are coherent enough to revise the outward product contract and choose the next implementation responsibilities.

D does **not** require modeling every organization's policy or predicting every future maintainer workflow.

#### Implementation handoff check after every conversation

At the end of A, B, C, and D ask:

> Has further conceptual discussion become lower-value than implementing or evaluating what we already understand?

Possible outcome:

```text
continue conceptual work
OR
resume a bounded implementation/evaluation responsibility
OR
run a focused real/simulated case to challenge the model
```

Do not impose a rule that all four conversations must be theoretically complete before any implementation can resume.

## 7. Cross-cutting questions to preserve throughout all four conversations

1. **Product value:** What does UpgradePilot add beyond a competent maintainer manually opening a few pages?
2. **Scale/repeatability:** Which benefits emerge from consistent repeated execution across many dependency PRs?
3. **Authority:** Which facts are authoritative, attributed, merely grounded, corroborated, contradictory, or unresolved?
4. **Negative evidence:** What can absence/search/CI non-observation actually establish, and with what boundary?
5. **Repository policy:** Which decision depends on repository-specific policy rather than universal engineering fact?
6. **Identity/freshness/decision time:** Which exact proposal/revision/world-state does a claim describe, when was mutable external evidence observed, and when must current-state mismatch or later evidence change the result's applicability rather than its historical validity?
7. **Model role:** Where can an LLM interpret natural-language source content without owning authority, applicability, or final action?
8. **Stopping:** When does more analysis stop adding material value?
9. **Actionability:** Can the system name a concrete next question/check rather than only assigning risk?
10. **Generality:** Would the method still make sense on a changed package/repository/case, or is it silently an S001/S004/S005 detector?
11. **Human authority:** Which judgments must remain explicitly with maintainers?
12. **Explainability:** Can every material conclusion be traced to exact evidence and transformation boundaries?
13. **Complexity control:** Are we modeling stable domain relationships, or accidentally multiplying case/package-specific rules?
14. **Concern topology:** Does a concern require a technical target-impact path, or can it be decision-relevant through trust, policy, time, provenance, governance, or other non-runtime relationships?
15. **Design economy:** Is the current question necessary for the next correct decision, or is it a deferrable future concern that would create architecture without evidence?

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

### H8 — Technical exposure may compress into a small number of coupling/contract relationships

Many concrete exposure forms may be manifestations of a smaller set of stable relationships rather than independent top-level categories.

Current working candidates are:

```text
1. execution / control-flow coupling
   target and dependency participate in each other's execution;

2. declarative / interpreted coupling
   one side interprets declarations/configuration owned by the other;

3. constraint / environment coupling
   compatibility depends on simultaneously satisfiable versions,
   platforms, runtimes, dependencies, or environmental requirements;

4. data / artifact-contract coupling
   target and dependency exchange, produce, consume, or rely upon
   structured data or artifacts under a shared contract.
```

These are **not accepted exposure types** and must not be frozen into enums/classes yet. Their value is that direct calls, callbacks, inheritance, decorators, framework hooks, plugin loading, configuration, version constraints, generated artifacts, schemas, protocols, and similar concrete forms may be composable instances of fewer root relationships.

### H9 — Exposure can be multi-hop and graph-shaped

A changed dependency may affect the target through an intermediate component:

```text
target
→ framework / adapter / direct dependency A
→ changed dependency B
```

Therefore exposure may sometimes be better represented as a path of relationships rather than a single target attribute. This makes an impact-graph mental model potentially useful, but does **not** imply a graph database or approved graph runtime architecture.

### H10 — Technical exposure may be only one subset of the larger decision model

Some material dependency-update concerns may matter without changed dependency behavior reaching target code or runtime through a conventional technical exposure path.

Candidate challenge classes include:

- source/provenance or package-identity degradation;
- supply-chain trust changes;
- licensing changes;
- yank/supersession/current-state mismatch;
- repository policy requirements;
- governance or human-acceptance conditions.

The discussion currently favors keeping **technical target impact** narrower than **all decision-relevant information**, but the exact surrounding dimensions and their boundaries remain open.

### H11 — Do not inflate identity/freshness into continuous temporal monitoring

The product may need precise handling of time-varying state without becoming a continuous ecosystem monitor.

A narrower working decomposition is:

```text
exact identity / revision binding
+ observation boundary for mutable external state
+ freshness / supersession checks where materially required
+ decision-time reconstruction for historical evaluation
```

This is preferable, for now, to assuming one broad `temporal subsystem` or continuously chasing newer releases and ecosystem changes.

### H12 — The reconciliation must use just-enough design

The current conceptual work is justified only while it removes ambiguity that would otherwise encode the wrong product model. The process must avoid both extremes:

```text
too little design
→ ambiguous semantics
→ case-specific patches / rewrites
```

and:

```text
too much design
→ speculative taxonomy / architecture
→ weak implementation feedback
→ architecture paralysis
```

The preferred boundary is **just enough semantic stability for the next correct decision**, followed by implementation/evaluation feedback where useful.

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
2. target exposure relationship/path — where/how could the target encounter it?
3. activation condition — what must be true for it to matter?
4. possible consequence — what could happen if activated?
5. target applicability — does the condition hold here?
6. evidence/coverage state — what supports, refutes, covers, conflicts with, or leaves the impact unresolved?
```

Materiality, uncertainty, repository-policy relevance, trust, identity/freshness, and current-state relationship may later be additional dimensions. These are conceptual domain dimensions, not approved runtime fields yet.

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

A tooling dependency may make CI/test behavior itself an exposure relationship, so roles remain contextual; nevertheless, evidence and impact must not be collapsed by default.

### D-012 — Treat exposure as a target relationship/pathway, not merely a repository location

**Provisional design conclusion accepted for continued discussion:** 2026-08-07

For technical target impact reasoning, exposure answers:

> Through what target-owned or target-relevant relationship/pathway could the changed dependency behavior reach or matter to the target?

Do not reduce exposure to a file, directory, subsystem, or direct function call. Relevant forms can include direct calls, framework lifecycle, callbacks, decorators, inheritance, plugin hooks, declarations/configuration, dependency constraints, runtime/environment compatibility, data contracts, generated artifacts, and indirect/transitive paths.

Keep the conceptual questions separate:

```text
where/how is the target connected?  → exposure
what must become true?              → activation
what may happen if activated?       → consequence
how do we know?                      → evidence / coverage
```

### D-013 — Role is contextual; the same subsystem/artifact can serve different reasoning roles

**Provisional design conclusion accepted for continued discussion:** 2026-08-07

Do not globally classify repository subsystems such as `tests`, `CI`, configuration, or build machinery as only exposure or only evidence.

Example contrast:

```text
runtime dependency behavior
→ target source/framework integration can be exposure
→ tests/CI can be evidence about that exposure
```

while:

```text
pytest is the changed dependency
→ test execution itself can be the exposure relationship
→ the resulting execution record can simultaneously provide evidence
```

Role is relative to the proposition being evaluated.

### D-014 — Technical target impact is not the same as all decision-relevant information

**Provisional design conclusion accepted for continued discussion:** 2026-08-07

Technical impact should describe effects the dependency update can have on the target through behavior, compatibility, environment, data/artifact, build/install, security, performance, or similar technical relationships.

Do not force every material concern into that model merely to preserve one elegant abstraction. Provenance/authority, current or superseded proposal/release state, licensing, repository policy, governance, and similar conditions may materially affect what UpgradePilot can claim or what a maintainer must consider without themselves being technical target impacts.

This establishes the boundary:

```text
TARGET TECHNICAL IMPACT
!=
ALL DECISION-RELEVANT INFORMATION
```

The exact surrounding dimensions and synthesis model remain open.

### D-015 — Proposal identity controls the assessed object; mutable external evidence is time-bounded observation

**Provisional design conclusion accepted for continued discussion:** 2026-08-07

UpgradePilot assesses the exact proposal it acquired, not whichever dependency release happens to become newest while analysis is running.

For a proposal such as:

```text
foo 1.9 → 2.0
```

later discovery of `2.1` does not silently change the assessment to `1.9 → 2.1`. The later release may become relevant evidence about `2.0`—for example if it explicitly fixes a regression introduced in `2.0`—but proposal identity remains controlled by the exact PR/revision being assessed.

Target repository evidence is bound to exact immutable revision identity where available, especially the PR base/head commit SHAs. Mutable external facts such as package yank state, upstream metadata, advisory state, or current PR state are observations made against an explicit source/world state at acquisition time.

Preserve this distinction:

```text
historically valid observation
!=
necessarily sufficient for a later current decision
```

If PyPI reports at 12:30 that version `2.0` is not yanked and at 12:31 the release becomes yanked, the 12:30 observation does not become false. Instead the world state changed. A result that claims to describe the current PR/current release state may therefore require a bounded freshness or identity recheck before finalization or rerun, but this does **not** imply continuous monitoring.

Do not yet decide:

- which external sources require final rechecks;
- freshness durations;
- automatic rerun policy;
- whether a changed PR head should restart, supersede, or preserve both analyses;
- whether these responsibilities warrant one dedicated temporal subsystem.

### D-016 — Reconciliation is bounded by decision need, not theoretical completeness

**Accepted process decision for this reconciliation:** 2026-08-07

Resolve a conceptual question now only when failing to resolve it would materially risk the next product, architecture, evidence-contract, or implementation decision. Otherwise record/defer it until a real case or implementation need activates it.

Do not treat A–D as open-ended research stages. Each conversation has explicit stop conditions, and each closure triggers a reassessment of whether implementation/evaluation has become more valuable than further design.

This process decision exists specifically to prevent two failure modes:

```text
premature implementation
→ ambiguous semantics hard-coded into source
```

and:

```text
architecture paralysis
→ speculative completeness pursued without implementation feedback
```

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
Exposure must be defined independently rather than inferred from a flat category label.

### 2026-08-07 — Exposure versus activation, consequence, and evidence

**Question**  
What makes something a target exposure rather than an activation condition, a consequence, or an evidence source?

**Existing evidence / examples**  
Direct API removal, Soup Sieve/Python support, pytest configuration, dependency constraints, and the parallel S006 qldebugger/Pydantic validator case were compared.

S006 offered a particularly useful distinction:

```text
upstream Pydantic validator behavior change
→ exposure: qldebugger participates in Pydantic validator/framework semantics
→ activation layer: affected dependency version + non-string handler input
→ consequence: observable exception contract changes
→ evidence: target tests, workflow configuration, differential reproduction
```

**Current conclusion**  
Exposure is best treated provisionally as the target-side relationship/pathway through which changed dependency behavior can matter. Activation, consequence, and evidence remain separate questions.

**Effect**  
The discussion should seek stable relationship types rather than a list of repository locations.

### 2026-08-07 — Can many exposure surfaces collapse into a few fundamental couplings?

**Question**  
Are source/API, framework, plugin, configuration, dependency graph, runtime, build, data, protocol, generated-artifact, test, and CI surfaces actually independent categories?

**Technical analysis**  
The discussion introduced **coupling** as the deeper software-engineering relationship: two components are connected such that a change in one can matter to the other.

Several concrete forms appear reducible to candidate root relationships:

```text
execution / control-flow coupling
- direct calls
- callbacks
- framework lifecycle
- inheritance
- decorators
- plugins/hooks

declarative / interpreted coupling
- configuration
- annotations/declarations
- dependency-interpreted target metadata

constraint / environment coupling
- version ranges
- peer constraints
- runtime support
- platform/architecture/compiler/system requirements

data / artifact-contract coupling
- serialization/data shape
- protocols
- generated code
- files/build artifacts
```

**Current conclusion**  
Strong working hypothesis only. These relationships are promising abstractions but have not been accepted as a final taxonomy, schema, enum, or exact count.

**Effect**  
Future cases should test whether the proposed roots are genuinely reusable and whether some must merge, split, or disappear.

### 2026-08-07 — Multi-hop exposure and contract reasoning

**Question**  
Can a changed dependency affect the target without direct target-to-dependency use?

**Current conclusion**  
Yes conceptually and empirically through adapters/frameworks/transitive dependency paths. Exposure may be a composed path:

```text
target
→ intermediate component A
→ changed dependency B
```

A useful supporting concept is **contract**: an assumption one component relies on another to satisfy. Relevant contracts may include API, callback, configuration, exception, data, version, runtime-support, and binary/environment contracts.

**Effect**  
Do not assume exposure is a single field or direct edge. Graph-like reasoning may become useful, but no graph implementation is accepted.

### 2026-08-07 — Does every material dependency concern require technical target exposure?

**Question**  
Can provenance, supply-chain trust, licensing, yank/supersession, repository policy, governance, or similar conditions materially affect the maintainer decision even when changed dependency behavior does not “reach” target code/runtime?

**Current conclusion**  
Provisionally, yes: decision-relevant information is broader than technical target impact. Do not force trust/authority, proposal/release current-state, licensing, policy, or governance into the technical impact model merely because they can affect a final action.

**Effect**  
Conversation A should define the boundary of technical impact and surrounding decision dimensions rather than search for one universal `impact` umbrella.

### 2026-08-07 — Identity, observation time, freshness, and supersession clarification

**Question**  
Does temporal reasoning mean UpgradePilot must continuously follow whatever happens after a PR is acquired, or chase newer package versions that appear during analysis?

**Current conclusion**  
No. Proposal identity and exact target revision control the assessed object. Immutable target evidence can be bound to exact base/head SHAs. Mutable external evidence is an observation of a source/world state at acquisition time.

A later world-state change does not retroactively falsify an earlier correctly scoped observation:

```text
12:30 — PyPI reports 2.0 not yanked
12:31 — 2.0 becomes yanked
```

Both can be true as observations of different states. The question becomes whether the earlier evidence remains sufficient for a result that claims to be current.

Likewise:

```text
PR proposes 1.9 → 2.0
2.1 appears while analysis runs
```

`2.1` does not silently replace the proposal. It may provide additional evidence about `2.0` if materially relevant.

**Effect**  
Do not use “temporal model” as shorthand for continuous monitoring. Preserve the narrower responsibilities of identity/revision binding, observation boundary, materially justified freshness/supersession checks, and decision-time reconstruction for historical evaluation.

### 2026-08-07 — What belongs inside technical impact versus outside decision context?

**Question**  
What should count as technical impact, and what should remain a separate concern even when it materially changes investigation or maintainer action?

**Current conclusion**  
Use the working boundary:

> **Technical impact is a target-relevant technical difference that the proposed dependency transition could cause or enable through a technical relationship with the target.**

Candidate technical properties include execution/runtime behavior, installability/resolution, build behavior, supported runtime/platform environment, data/artifact contracts, performance/resource behavior, security behavior, and test/development-tool behavior when the changed dependency participates technically in those paths.

Do not classify the following as technical impact merely because they matter:

- source/provenance or evidence-authority failure;
- proposal/head/current-state mismatch;
- yank/supersession state by itself;
- licensing/compliance policy;
- repository review/approval requirements;
- general governance or risk-tolerance rules.

A useful diagnostic is the **subject of the claim**:

```text
target technical behavior/property
→ technical impact

source/evidence authority
→ trust / evidence context

analysis object/currentness
→ identity / freshness context

repository/organization rule
→ policy / governance context
```

These surrounding concepts may block a claim, keep a technical impact unresolved, trigger another investigation, or constrain final action without themselves becoming technical impacts.

**Effect**  
Conversation A no longer needs to search for one universal `impact` umbrella. The remaining task is semantic compression inside the technical-impact chain itself.

### 2026-08-07 — How long should reconciliation continue before it becomes over-design?

**Question**  
Is the current depth still technically justified, and what prevents Conversation A or the entire reconciliation from becoming an open-ended architecture exercise?

**Current conclusion**  
The reconciliation has been justified because it exposed concrete semantic defects that would otherwise have been encoded in the next decision implementation. However, the risk of over-design is now rising, so explicit stop conditions are required.

The correct standard is **just enough design**:

```text
resolve ambiguity that would make the next decision wrong
↓
stop once the next model/implementation step is semantically safe
↓
return to implementation/evaluation feedback
```

not complete theoretical coverage of the dependency-update domain.

**Effect**  
Conversation A gets one focused semantic-cleanup question followed by an explicit closure review. B–D are also bounded by decision-completeness rather than exhaustive domain coverage.

## 11. Current conceptual map and onboarding checkpoint

### 11.1 Where we are

```text
Conversation A — What could matter?              NEARING CLOSURE REVIEW
Conversation B — Does it matter here?            NOT YET STARTED PROPERLY
Conversation C — What should we investigate?     NOT YET STARTED
Conversation D — Do we know enough / output?     NOT YET STARTED
```

Conversation A has provisionally established:

- upstream change is not itself target impact;
- potential impact is distinct from target applicability;
- activation conditions are central;
- materiality is decision-relative;
- severity, likelihood, materiality, and interestingness are different dimensions;
- real-world variation should be controlled through reusable domain abstractions rather than package/case rules;
- a flat impact taxonomy is probably wrong;
- exposure, activation, consequence, and evidence are separate conceptual roles;
- technical exposure is a target relationship/pathway, not merely a repository location;
- the same subsystem/artifact may play different roles depending on the proposition being evaluated;
- technical target impact is not the same as all decision-relevant information;
- technical impact has a working boundary around target-relevant technical differences caused/enabled through target technical relationships;
- provenance/authority, currentness, licensing/policy/governance, and similar concerns should not be relabeled as technical impact merely because they can change action;
- proposal identity controls the exact upgrade being assessed;
- target repository evidence should be bound to exact revision identity where possible;
- mutable external evidence is time-bounded observation rather than a timeless fact;
- later ecosystem changes do not retroactively invalidate correctly scoped earlier observations, but may affect whether those observations remain sufficient for a current result;
- reconciliation itself must stop at decision-completeness rather than theoretical completeness.

Current strong hypotheses, not accepted architecture:

- many technical exposure forms may compress into execution/control-flow, declarative/interpreted, constraint/environment, and data/artifact-contract couplings;
- exposure can be multi-hop/transitive and therefore graph-shaped;
- the larger decision model likely needs dimensions outside technical impact, potentially including trust/authority, identity/freshness/supersession, policy/governance/licensing, and other decision context;
- identity/freshness responsibilities should remain narrow unless real evidence justifies a broader temporal architecture;
- the current chain may still contain redundant concepts around `upstream change`, `potential impact`, and `consequence`, which must be cleaned up before A closes.

### 11.2 Current technical-impact reasoning sketch

```text
public dependency-update PR
↓
exact proposal + dependency/version + base/head identity
↓
upstream changes relevant to that exact proposed transition
↓
for each material technical candidate:
    change mechanism
    + target exposure relationship/path
    + activation condition(s)
    + possible consequence
↓
exact target/context evidence
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
combine with non-impact decision context
↓
maintainer-facing synthesis
```

This is a discussion model, not an approved pipeline or schema. The exact role of `potential impact` inside this chain is the remaining A cleanup question.

### 11.3 Current exposure mental model

For technical target impact, ask four different questions:

```text
EXPOSURE
Through what target-owned or target-relevant relationship/path
could the changed dependency behavior matter?

ACTIVATION
What condition(s) must hold for that relationship to become materially relevant?

CONSEQUENCE
What could happen if the relevant conditions hold?

EVIDENCE / COVERAGE
What observations support, refute, cover, conflict with,
or leave that proposition unresolved?
```

Candidate root couplings remain hypotheses:

```text
execution / control-flow

declarative / interpreted

constraint / environment

data / artifact contract
```

Do not freeze them into a runtime type system yet.

### 11.4 Current technical-impact boundary

Working definition:

> **Technical impact is a target-relevant technical difference that the proposed dependency transition could cause or enable through a technical relationship with the target.**

A useful counterfactual test is:

```text
Target + old dependency
vs
Target + proposed dependency
```

Could a target-relevant technical property differ, such as:

- execution/runtime behavior;
- installability or dependency resolution;
- build behavior;
- supported runtime/platform/environment;
- data/schema/protocol/generated-artifact behavior;
- performance/resource behavior;
- security behavior;
- test/development tooling behavior when technically coupled?

If yes, there is a plausible technical-impact candidate.

Do not confuse technical impact with:

```text
evidence/source authority
analysis identity/currentness
release-state facts by themselves
repository policy/governance
licensing/compliance rules
human approval/risk tolerance
```

Those may influence whether a technical claim is justified, whether a result is still current, or what action is allowed, without becoming technical impact themselves.

### 11.5 Current identity / observation mental model

Keep four questions distinct:

```text
IDENTITY
What exact proposal, repository revision, dependency, and version transition are being assessed?

OBSERVATION BOUNDARY
For mutable external facts, what source/state was observed and when?

FRESHNESS / SUPERSESSION
Does the result still correspond to the object/world-state that now needs a decision?

DECISION-TIME EVALUATION
When evaluating a past result, what evidence was actually available at that decision point?
```

Default principle:

```text
proposal identity controls the assessed transition

later versions may inform the assessment
but do not silently replace the proposal

correctly scoped past evidence remains historically valid
but may cease to be sufficient for a current claim
```

No continuous monitoring requirement is implied.

### 11.6 Immediate Conversation-A question

Only one planned semantic-cleanup question remains before A closure review:

> **Within technical impact itself, what is the difference between the upstream change, the potential impact, and the consequence—and do we actually need all three as separate domain concepts?**

Current chain under review:

```text
upstream change mechanism
→ potential impact
→ exposure relationship/path
→ activation condition
→ consequence
```

The purpose is not to open a new topic. It is to remove avoidable conceptual redundancy before the model is handed to Conversation B.

### 11.7 Conversation-A closure review after that question

After the semantic-cleanup discussion, explicitly review:

1. What has A actually accepted?
2. What remains a hypothesis?
3. What is deliberately deferred?
4. Does the model explain S001–S006 and relevant counterexamples without fixture-specific distortion?
5. Is any remaining ambiguity capable of making Conversation B's applicability model fundamentally wrong?

If no foundational contradiction remains, **close Conversation A and move to B**.

### 11.8 Questions deliberately deferred to later conversations

Do not prematurely solve these while closing A:

- exact applicability state vocabulary;
- how negative evidence proves bounded absence;
- detailed LLM role for arbitrary upstream change semantics;
- targeted-check ranking or Value of Information method;
- repository-policy schema;
- exact freshness/recheck/rerun policy;
- final sufficiency rules;
- final maintainer-facing action vocabulary;
- whether the historical five action classes survive;
- final runtime classes/enums/schema;
- complete technical-impact/exposure taxonomy;
- graph data structure/database choices;
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
8. identity/freshness/decision-time boundary;
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

Continue **Conversation A — Dependency-update impact/problem model** with one final planned semantic-cleanup discussion:

> **Within technical impact itself, what is the difference between the upstream change, the potential impact, and the consequence—and do we actually need all three as separate domain concepts?**

Then run the explicit **Conversation-A closure review** from Section 11.7.

If the review passes, move to **Conversation B — Applicability and investigation activation**. If a genuine foundational contradiction appears, resolve only that contradiction and rerun the closure review.

Do not open additional Conversation-A branches merely because they are interesting. Apply the discuss-now/defer test from Section 2 and preserve implementation/evaluation feedback as the next source of learning once semantic stability is sufficient.