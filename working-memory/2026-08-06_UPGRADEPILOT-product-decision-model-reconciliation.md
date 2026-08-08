# UpgradePilot Product Decision-Model Reconciliation Working Record

**Date opened:** 2026-08-06  
**Last discussion sync:** 2026-08-08  
**Status:** Active design discussion; Conversation A closed; Conversation B active; no final whole-product model yet  
**Purpose:** Preserve the current whole-product decision-model position, important rationale, active hypotheses, open questions, stop lines, and eventual accepted repository changes without turning this file into an append-only transcript.  
**Live-state owner:** `../MEMORY.md` remains the sole owner of current project position and exact implementation continuation.  
**Pre-consolidation snapshot:** commit `e158fe041597ecb6176f4d5dab6b11961f30c8e1` preserves the more chronological/repetitive form of this record in Git history.

## 1. Why this reconciliation exists

UpgradePilot completed the bounded Target-Python Support Relevance responsibility through the normal live path. That implementation now has materially stronger evidence identity, provenance, grounding, target relevance, and explicit failure/unresolved behavior than when the earlier transparent-decision documents and product-simulation conclusions were written.

The next active implementation plan pointed toward a Transparent Decision Method, but the repository audit showed that implementing the old decision framing immediately could encode stale or underspecified concepts, especially:

- a too-direct `evidence → action` mapping;
- historical simulation actions treated too much like machine truth;
- insufficient separation between upstream change, target impact, applicability, evidence, and final action;
- undefined repository-specific semantics around labels such as `merge after normal review`;
- missing first-class treatment of investigation selection and stopping;
- unclear policy, trust, identity/freshness, and human-authority boundaries.

Therefore implementation of the decision/recommendation layer is intentionally paused while the minimum necessary whole-product semantics are reconciled.

This pause is **not** authorization for open-ended architecture work. The goal is just enough semantic stability for the next correct product or implementation decision, followed by implementation/evaluation feedback.

## 2. Authority, evidence, and discussion discipline

### 2.1 Repository authority

Active/normative material considered during this reconciliation includes:

- `PROJECT_CHARTER.md`
- `README.md`
- `plans/UPGRADEPILOT_90_DAY_PLAN.md`
- `plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md`
- `MEMORY.md`
- `docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`
- `docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`
- `docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md`
- `AGENTS.md`

Historical/discovery evidence considered includes:

- `product-simulation/TRANSPARENT_BASELINE_SPECIFICATION.md`
- `product-simulation/D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md`
- `product-simulation/SCENARIO_COVERAGE.md`
- S003/S004/S005 post-case syntheses
- `product-simulation/RUNTIME_ARTIFACT_SPECIFICATION.md`
- `working-memory/2026-07-28_B2-transparent-decision-method.md`
- `working-memory/2026-07-28_B2-decision-evidence-map-and-contract-draft.md`
- parallel branch evidence from `agent/product-simulation-case-screening-01`, especially S006 and `DECISION_MODEL_HANDOFF_2026-08-07.md`
- non-controlling `proposals/2026-07-20_UPGRADEPILOT_PRODUCT_AMBITION_AND_ENHANCEMENT_PROPOSAL.md`

Historical simulations, proposals, and old drafts are **design evidence**, not automatic authority for the new model. Source/tests remain the authority for implemented behavior.

### 2.2 Stable principles retained

The reconciliation continues to preserve these strong principles:

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

Also retained:

- exact proposal, dependency, version, source, revision, and relevant observation-time identity matter;
- source authority/provenance and semantic meaning are separate responsibilities;
- missing, inaccessible, stale, conflicting, invalid, unsupported, not-applicable, and unresolved states should remain distinguishable where material;
- model/LLM output cannot assign its own authority or final decision effect;
- absence of a model-derived claim is not evidence that no relevant risk exists;
- conditional activation/non-activation are first-class results;
- repository policy and residual-risk acceptance remain human/repository responsibilities unless explicitly represented through trustworthy policy evidence;
- investigation should stop when additional supported work cannot materially change uncertainty location, required checks, action constraints, or another decision-relevant result.

### 2.3 Anti-overdesign rule

Reconciliation is bounded by **decision need**, not theoretical completeness.

```text
new conceptual question
↓
Would the answer materially change the next
product / architecture / evidence-contract / implementation decision?
├── yes → resolve now
└── no  → record/defer until a real case or implementation need activates it
```

Prefer:

```text
real evidence
→ identify foundational ambiguity
→ resolve only necessary semantics
→ implement / evaluate
→ learn from behavior
→ refine
```

Do not force every discussion result into an enum, schema, class hierarchy, graph implementation, or framework before the domain relationship has earned that representation.

## 3. Current whole-product position

The old conceptual shortcut was too compressed:

```text
evidence
→ action
```

The current discussion model is richer:

```text
public dependency-update PR
↓
exact proposal + dependency/version + base/head identity
↓
upstream changes relevant to that exact proposed transition
↓
material technical impact candidate(s)
    ├── upstream change mechanism
    ├── target exposure relationship/path
    ├── activation condition(s)
    └── possible target-relevant consequence
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

This is a **discussion model**, not an approved runtime pipeline or schema. Conversation A has now accepted that an `impact candidate` is the complete technical proposition connecting an upstream change to a possible target consequence through exposure and activation conditions; it is not another event inserted between change and exposure.

A central emerging product insight is that UpgradePilot may be more accurately understood as an **evidence-driven impact and investigation system** than as a five-label classifier. The historical five action families may survive as a later projection, but that is not yet decided.

## 4. Current technical-impact model

### 4.1 Working definition

> **A technical impact candidate is a target-relevant proposition that the proposed dependency transition could cause or enable a technical consequence through a technical relationship with the target under relevant activation conditions.**

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
- test/development-tool behavior when the changed dependency is technically coupled to that path?

If yes, there is a plausible technical-impact candidate. Conversation B owns the question of whether that candidate is actually applicable to the exact target/revision/context.

### 4.2 Upstream change is not target impact

A dependency can change upstream without materially affecting the target.

```text
upstream change
!=
target impact
```

Example already implemented:

```text
Soup Sieve drops Python 3.8
→ candidate concern for Python 3.8 consumers
→ Pydantic declares requires-python >=3.10
→ that bounded support-drop concern is outside the declared target range
```

This closes one impact path only. It does not prove global compatibility, upgrade safety, CI sufficiency, or mergeability.

### 4.3 Impact candidate, exposure, activation, consequence, applicability, evidence

Conversation A accepts this domain relationship:

```text
UPSTREAM CHANGE
What changed in the dependency?

        +

EXPOSURE
Through what target-owned or target-relevant relationship/path
could that changed behavior/property reach or matter to the target?

        +

ACTIVATION CONDITION(S)
What must be true for that relationship to become materially relevant?

        +

POSSIBLE CONSEQUENCE
What target-relevant technical property could differ if activated?

        =

IMPACT CANDIDATE
The complete proposition connecting the upstream change to a possible
target consequence through the exposure and activation conditions.
```

`Impact candidate` therefore names the **whole proposition**, not a separate intermediate event. `Consequence` is one component of that proposition: the possible target-side technical difference.

For evaluation, keep these additional questions distinct:

```text
APPLICABILITY
Do the relevant activation conditions actually hold for this exact target/context?

EVIDENCE / COVERAGE
What observations support, refute, cover, conflict with,
or leave the proposition unresolved?
```

Exposure is a **relationship/pathway**, not merely a file, directory, subsystem, or direct call.

The same subsystem/artifact can have different roles depending on the proposition. For a runtime dependency, tests/CI may be evidence; if pytest itself is the changed dependency, test execution can be part of the exposure while the resulting execution record is evidence.

This accepted relationship is currently a **domain model**, not authorization to create runtime classes, enums, schemas, or a fixed serialized representation.

### 4.4 Candidate exposure abstractions — still hypotheses

Many concrete exposure forms may reduce to a smaller set of software couplings/contracts:

```text
1. execution / control-flow coupling
   direct calls, callbacks, framework lifecycle, inheritance,
   decorators, plugins/hooks

2. declarative / interpreted coupling
   configuration, annotations/declarations, dependency-interpreted metadata

3. constraint / environment coupling
   version ranges, peer constraints, runtime support,
   platform/architecture/compiler/system requirements

4. data / artifact-contract coupling
   serialization/data shape, protocols, generated code,
   files/build artifacts
```

These are **not accepted exposure types** and must not yet become enums/classes.

Exposure can also be multi-hop:

```text
target
→ intermediate framework/adapter/dependency A
→ changed dependency B
```

This makes graph-like reasoning potentially useful conceptually, but does not imply a graph database or approved graph runtime architecture.

### 4.5 Materiality

Materiality is decision-relative, not equivalent to severity or likelihood.

```text
severity != materiality
likelihood != materiality
interesting != material
material != harmful
```

A useful counterfactual test is:

> If this impact were present versus absent, could a material investigation state, required check, uncertainty, or maintainer-facing result change?

If not, it normally should not consume deeper investigation.

## 5. Decision-relevant context outside technical impact

A major accepted boundary is:

```text
TARGET TECHNICAL IMPACT
!=
ALL DECISION-RELEVANT INFORMATION
```

Do not broaden `impact` until it means anything that matters.

### 5.1 Trust / authority context

Examples:

- package-to-upstream provenance;
- source authority;
- conflicting authoritative sources;
- grounding/corroboration quality;
- unavailable or unsupported evidence acquisition.

These affect what UpgradePilot is justified in claiming. They are not automatically target technical impacts.

If provenance fails, the correct shape may be:

```text
technical impact/applicability: unresolved
because authoritative upstream association is unresolved
```

not:

```text
technical impact = provenance failure
```

### 5.2 Identity / revision / observation / freshness context

Proposal identity controls the object being assessed.

If a PR proposes:

```text
foo 1.9 → 2.0
```

and `2.1` appears while analysis runs, UpgradePilot does not silently change the assessment to `1.9 → 2.1`. `2.1` may become relevant evidence about `2.0` if, for example, it explicitly fixes a regression introduced in `2.0`.

Target repository evidence should be bound to exact immutable revisions where available, especially PR base/head SHAs.

Mutable external facts are observations of a source/world-state at acquisition time:

```text
12:30 — PyPI reports 2.0 not yanked
12:31 — 2.0 becomes yanked
```

The 12:30 observation does not become historically false. Instead the world state changed.

Preserve:

```text
historically valid observation
!=
necessarily sufficient for a later current decision
```

Keep four questions distinct:

```text
IDENTITY
What exact proposal/revision/version transition is being assessed?

OBSERVATION BOUNDARY
For mutable external facts, what source/state was observed and when?

FRESHNESS / SUPERSESSION
Does the result still correspond to the object/world-state that now needs a decision?

DECISION-TIME EVALUATION
When evaluating a past result, what evidence was actually available then?
```

This does **not** imply continuous monitoring. Exact recheck/rerun/freshness rules remain deferred.

### 5.3 Policy / governance / licensing context

Repository or organizational rules may constrain action without changing technical truth.

Examples:

- license/compliance restrictions;
- required human/security review;
- required CI checks;
- release freezes;
- approval ownership;
- repository-specific risk rules.

A license transition can be objectively described, while whether it is acceptable depends on policy/compliance context. Policy activation can resemble technical activation structurally, but the domains must not be collapsed merely because both use predicates.

### 5.4 Security can span multiple roles

Do not use `security` as one flat category.

- vulnerable behavior that reaches an exposed target path can be technical impact;
- unverified publisher/package identity may be trust/provenance context;
- mandatory security review may be repository policy.

The proposition determines the role.

## 6. Case-derived evidence that currently matters

Historical cases remain evidence, not labels. Preserve the lessons that materially constrain the model:

### S001 — Soup Sieve / Pydantic

Current live path proves one bounded concern:

```text
Soup Sieve Python 3.8 support drop introduced in 2.8
+ Pydantic exact-head requires-python >=3.10
→ support-drop concern outside declared Python range
```

CI dependency exercise remains `unresolved / dependency_exercise_not_proven`.

Lesson: non-applicability can close one concern without proving global safety or reproducing the old manual `merge after normal review` label.

### S003 — dependency/peer constraint family

Lesson: impact may occur through dependency graph/resolution constraints rather than direct runtime calls. Installability is a target-relevant technical property.

### S004 / transparent baseline

Lesson: coarse evidence can sometimes be sufficient after authority-critical assumptions are confirmed. Deeper analysis must earn its cost; the transparent baseline remains a comparator, not the architecture.

### S005 — activation and target relevance

Reusable reasoning pattern:

```text
upstream statement/change
→ activation condition
→ target configuration/source/usage relationship
→ evidence/coverage
→ unresolved question OR bounded closure
```

Lesson: cautionary upstream evidence is not automatically target-applicable.

### S006 — qldebugger / Pydantic validator semantics

Useful conceptual mapping:

```text
upstream validator behavior change
→ exposure: target participates in Pydantic validator/framework semantics
→ activation: affected dependency version + non-string handler input
→ consequence: observable exception contract changes
→ evidence: source/tests/workflow/differential reproduction
```

Additional lessons:

- dependency version selection can be an activation condition rather than exposure itself;
- broad test/CI coverage is not the same as discriminating coverage of the affected behavior path;
- the same subsystem can be exposure in one proposition and evidence in another;
- the S006 evaluation had oracle-isolation limitations, so it supports traceability/check-design reasoning but not autonomous-planner reliability claims.

## 7. Decisions and provisional conclusions

The numbering is intentionally retained so prior Git history remains easy to trace.

### D-001 — Use one reconciliation record
**Accepted 2026-08-06.** Preserve this whole-product reconciliation in one working-memory file before modifying controlling artifacts or implementing the next decision layer.

### D-002 — Stage boundaries do not constrain whole-product reasoning
**Accepted 2026-08-06.** B2/B3/B4 may later control implementation sequence, not what the correct whole-product model may contain.

### D-003 — Old artifacts are evidence, not automatic authority
**Accepted 2026-08-06.** Historical simulations, drafts, and proposals must be evaluated against current implementation and current product goals.

### D-004 — Upstream change is not itself target impact
**Provisional design conclusion.** A separate target relationship/path must be established.

### D-005 — Preserve potential impact versus target applicability
**Provisional design conclusion.** A credible possible impact is not target-applicable until the relevant activation condition intersects the exact target/context. Non-applicability closes only that bounded path.

### D-006 — Activation condition is central
**Provisional design conclusion.** Activation is the condition that must hold in the target for a potential upstream change to matter.

### D-007 — Dependency impact and unrelated PR/repository condition remain distinguishable
**Provisional design conclusion.** Failing CI or another repository condition does not become dependency impact without causal evidence.

### D-008 — Materiality is decision-relative
**Provisional design conclusion.** Severity, likelihood, interestingness, harm, and materiality are distinct. Material questions are those capable of changing meaningful investigation or maintainer-facing state.

### D-009 — Control variation through domain abstractions, not case rules
**Provisional design conclusion.** Normalize many concrete values/forms into stable contracts, focused predicates/evaluators, composition rules, conditional pruning, and bounded semantic states. Preserve value/state/structural variation as different problems. Related learning: `../learning/concepts/managing-combinatorial-complexity-in-upgradepilot.md`.

### D-010 — Do not freeze a flat impact enum
**Provisional design conclusion.** `API / security / platform / performance / CI / build` mixes change mechanism, exposure, consequence, and evidence. Separate dimensions first.

### D-011 — CI/tests/source/config/metadata are not automatically impacts
**Provisional design conclusion.** They often provide evidence about an impact proposition. Their role is contextual.

### D-012 — Exposure is a target relationship/pathway
**Provisional design conclusion.** Exposure asks how changed dependency behavior could reach or matter to the target; it is not merely a repository location.

### D-013 — Role is contextual
**Provisional design conclusion.** The same subsystem/artifact may be exposure in one proposition and evidence in another.

### D-014 — Technical target impact is not all decision-relevant information
**Provisional design conclusion.** Trust/authority, currentness/supersession, policy/governance/licensing, and similar concerns may materially affect claims/actions without themselves being technical target impacts.

### D-015 — Proposal identity controls the assessed object; mutable external evidence is time-bounded observation
**Provisional design conclusion.** Later releases do not silently replace the proposal. Correctly scoped past observations remain historically valid even if external state later changes, though they may cease to be sufficient for a current claim. Continuous monitoring is not implied.

### D-016 — Reconciliation is bounded by decision need, not theoretical completeness
**Accepted process decision 2026-08-07.** Resolve questions now only when failing to do so risks the next correct product/architecture/evidence-contract/implementation decision. Each conversation has a stop line and must reconsider implementation/evaluation at closure.

### D-017 — Impact candidate is the complete technical proposition, not an intermediate event
**Accepted domain decision 2026-08-08.** Preserve upstream change, exposure relationship/path, activation condition(s), and possible target consequence as distinct roles. `Impact candidate` names the complete proposition connecting those roles. `Consequence` is the possible target-side technical difference; `impact candidate` is not another event inserted between upstream change and exposure. This decision defines domain semantics only and does not yet authorize runtime classes, enums, schemas, or serialization contracts.

### D-018 — Conversation A is sufficiently closed for Conversation B
**Accepted process/design decision 2026-08-08.** The explicit Conversation-A closure review found no remaining foundational ambiguity capable of making the applicability model fundamentally wrong. Remaining taxonomy, exposure-root, graph-representation, policy, temporal, and runtime-structure questions are either hypotheses or deliberately deferred until decision need or implementation evidence activates them.

## 8. Active hypotheses — not final architecture

### H1 — Impact/investigation may be more central than five-class recommendation
The product may be better represented as evidence-driven impact/investigation reasoning with later synthesis rather than as a primary five-label classifier.

### H2 — Action classes may become a projection
The historical action families may survive as maintainer-facing summaries rather than the central internal model.

### H3 — “Normal review” may not be UpgradePilot-owned
Without explicit repository policy, `normal review` is too repository-specific to assume as a clean universal runtime action.

### H4 — Targeted investigation is a core value proposition
A major product advantage may be choosing what decision-relevant question matters next, what evidence/check can discriminate it, and when not to investigate further.

### H5 — Historical simulations remain evidence, not labels
S001–S006 should challenge the model; their historical actions must not become silent ground truth.

### H6 — Current Python-support implementation is one proven impact slice
It demonstrates one real change → activation/target evidence → relevance/closure path but is not a universal implementation template.

### H7 — Flat impact taxonomy is probably wrong
A multidimensional model appears more general and less prone to combinatorial rule growth.

### H8 — Technical exposure may compress into a small number of coupling/contract relationships
Execution/control-flow, declarative/interpreted, constraint/environment, and data/artifact-contract are current candidate roots only.

### H9 — Exposure can be multi-hop/graph-shaped
Impact paths may traverse intermediate components; this is a domain observation, not an implementation commitment.

### H10 — Technical exposure is only one subset of the larger decision model
The larger synthesis likely also needs trust/authority, identity/freshness/supersession, policy/governance/licensing, and possibly other decision context. Exact dimensions remain open.

### H11 — Do not inflate identity/freshness into continuous temporal monitoring
Prefer exact identity/revision binding, observation boundaries, materially justified freshness/supersession checks, and decision-time reconstruction over a broad speculative temporal subsystem.

### H12 — Use just-enough design
Avoid both ambiguous premature implementation and architecture paralysis. Stop conceptual work once semantic stability is sufficient for the next correct decision and seek implementation/evaluation feedback.

## 9. Important corrections and rejected shortcuts

Keep these because they prevent regression into earlier assumptions:

```text
upstream change = target impact
→ rejected
```

```text
anything decision-relevant = technical impact
→ rejected
```

```text
API / security / platform / performance / CI as one flat impact taxonomy
→ rejected as conceptually mixed
```

```text
CI/test/source/config artifact has one permanent role
→ rejected; role is proposition-relative
```

```text
historical simulation action = machine truth
→ rejected
```

```text
merge/proceed to “normal review” is universally defined
→ challenged; repository-specific semantics remain unresolved
```

```text
temporal reasoning = continuously monitor and chase newest versions
→ rejected
```

```text
newer dependency release silently replaces exact PR proposal
→ rejected
```

```text
all exposure is direct source/API use
→ rejected; framework/declarative/constraint/data and multi-hop relationships matter
```

```text
reconciliation should completely model the domain before coding resumes
→ rejected; use decision-completeness and implementation feedback
```

```text
potential impact is a separate event between upstream change and exposure
→ rejected; impact candidate is the complete proposition
```

## 10. Four reconciliation conversations and stop lines

These are decision checkpoints, not research programs.

### Conversation A — Dependency-update impact/problem model

**Question:** What can count as technical impact/concern, and what should `impact` mean?

**Status:** **CLOSED 2026-08-08.**

A closed after the explicit review established:

1. technical impact has a usable boundary;
2. upstream change, exposure, activation condition, possible consequence, impact candidate, applicability, and evidence have distinct enough roles for the next design step;
3. neighboring trust/authority, identity/freshness, policy/governance/licensing, and unrelated repository conditions are not silently collapsed into technical impact;
4. the model remains coherent across S001, S003, S004, S005, S006, and the recorded counterexamples;
5. remaining taxonomy and representation questions can safely be deferred;
6. no remaining ambiguity was found that would make Conversation B fundamentally wrong.

A does **not** claim a complete taxonomy, every ecosystem/security/build/platform case, final graph model, exposure enum, policy schema, temporal implementation, package-manager universality, or final runtime classes.

Closure review classification:

```text
ACCEPTED FORWARD SEMANTICS
upstream change
+ exposure relationship/path
+ activation condition(s)
+ possible consequence
= impact candidate

NEXT QUESTION
Does this impact candidate actually apply to this exact target/revision/context,
and what evidence justifies that state?
```

### Conversation B — Applicability and investigation activation

**Question:** How does UpgradePilot determine whether a possible impact actually matters to this exact target/revision/context?

**Status:** **ACTIVE.**

B can close when applicability propositions and activation conditions have clear positive/negative/unresolved/conflicted semantics and deterministic-versus-semantic evidence boundaries.

B does **not** require every repository inspection technique, language ecosystem, package manager, or configuration grammar.

### Conversation C — Best next investigation/check

**Question:** When material uncertainty remains, what additional evidence/check is worth acquiring, executing, or recommending?

C can close when UpgradePilot has a bounded general method for identifying a decision-relevant unresolved question, selecting/recommending a discriminating investigation, and recognizing when no supported additional check is worth doing.

C does **not** require autonomous debugging, universal test generation, or arbitrary repository experimentation.

### Conversation D — Sufficiency, stopping, and maintainer-facing result

**Question:** When does UpgradePilot know enough to stop, and what exactly should it tell the maintainer?

D can close when evidence sufficiency, unresolved/conflicting state, stopping, repository-policy interaction, and maintainer-facing synthesis are coherent enough to revise the outward product contract and choose implementation responsibilities.

D does **not** require modeling every organization's policy or every future maintainer workflow.

### Implementation handoff check after every conversation

Ask:

> Has further conceptual discussion become lower-value than implementing or evaluating what we already understand?

Possible next moves are continued conceptual work, bounded implementation/evaluation, or a focused real/simulated case that challenges the model. There is no rule that A–D must all become theoretically complete before implementation can resume.

Conversation A closure currently favors continuing into B because applicability semantics are the next foundational dependency of a correct decision contract, while the accepted A model does not yet require a new runtime representation by itself.

## 11. Cross-cutting questions to preserve

Throughout A–D, continue checking:

1. **Product value** — what does UpgradePilot add beyond competent manual browsing?
2. **Scale/repeatability** — which benefits emerge from consistent repeated execution?
3. **Authority** — what is authoritative, attributed, grounded, corroborated, contradictory, or unresolved?
4. **Negative evidence** — what can absence/non-observation establish, and within what boundary?
5. **Repository policy** — which conclusion depends on repository-specific norms rather than engineering fact?
6. **Identity/freshness/decision time** — which exact object/world-state does a claim describe, and when does later state change current applicability rather than historical validity?
7. **Model role** — where may an LLM interpret semantics without owning authority/applicability/action?
8. **Stopping** — when does more analysis stop adding material value?
9. **Actionability** — can the system name a concrete next question/check rather than only assign risk?
10. **Generality** — does the method survive changed repositories/packages/cases?
11. **Human authority** — which judgments remain explicitly maintainer-owned?
12. **Explainability** — can material conclusions be traced to exact evidence and transformation boundaries?
13. **Complexity control** — are we modeling stable relationships or multiplying case-specific rules?
14. **Concern topology** — technical target impact versus trust/policy/identity/governance/other context?
15. **Design economy** — is this question necessary for the next correct decision or safely deferrable?

## 12. Deliberately deferred questions

Do not solve these merely to make the model look complete:

- exact applicability-state vocabulary beyond what Conversation B requires;
- detailed negative-evidence proof methods;
- arbitrary/general LLM semantics for all upstream changes;
- exact Targeted Check Planner ranking or Value-of-Information method;
- repository-policy schema;
- exact freshness/recheck/rerun durations and triggers;
- whether changed PR head restarts, supersedes, or preserves both analyses;
- whether identity/freshness deserves a dedicated subsystem;
- final sufficiency formula/rules;
- final maintainer-facing action vocabulary;
- whether historical five action classes survive unchanged;
- complete technical-impact/exposure taxonomy;
- graph data structure/database choices;
- final runtime classes/enums/schema;
- implementation sequence and ADR changes.

## 13. Final repository-change register

**Status:** Pending reconciliation.

When enough of A–D is settled, reassess exactly what must be retained, amended, superseded, archived, or newly created. Candidate controlling files to reassess later include:

- `PROJECT_CHARTER.md`
- `README.md`
- `plans/UPGRADEPILOT_90_DAY_PLAN.md`
- `plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md`
- applicable files under `docs/specifications/`
- possibly a new ADR if a consequential decision architecture/method is accepted
- `MEMORY.md` for the final live continuation
- source/tests only after an implementation responsibility is selected

The eventual reconciliation closure must preserve:

1. accepted problem/impact model;
2. applicability/activation model;
3. investigation/check-selection model;
4. sufficiency/stopping model;
5. maintainer-facing synthesis/action model;
6. terminology decisions;
7. repository-policy boundary;
8. identity/freshness/decision-time boundary;
9. LLM/model authority boundary;
10. required controlling-artifact changes;
11. implementation/test/evaluation implications;
12. explicit non-goals and rejected alternatives.

## 14. Exact current continuation

Continue with **Conversation B — Applicability and investigation activation**.

Start with the smallest foundational question:

> **For one specific impact candidate and one exact target/revision/context, what proposition is UpgradePilot trying to establish when it says that candidate is applicable, not applicable, unresolved, or conflicted?**

Use the accepted Conversation-A structure:

```text
impact candidate
├── upstream change
├── exposure relationship/path
├── activation condition(s)
└── possible consequence
        ↓
exact target/revision/context evidence
        ↓
applicability evaluation
```

The first purpose of Conversation B is to define the meaning and boundaries of that applicability evaluation before choosing runtime states, repository inspection techniques, or implementation structures.

Then determine:

1. what must be true for positive applicability;
2. what evidence is sufficient for bounded non-applicability;
3. when missing/unsupported evidence remains unresolved rather than negative;
4. how genuine authoritative contradiction differs from ordinary uncertainty;
5. which parts can be deterministic and where semantic interpretation may be needed without granting an LLM authority over final applicability.

Do not begin by designing enums/classes or enumerating every ecosystem-specific inspection technique. Apply the decision-need test from Section 2.