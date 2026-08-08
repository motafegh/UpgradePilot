# UpgradePilot Product Decision-Model Reconciliation Working Record

**Date opened:** 2026-08-06  
**Last discussion sync:** 2026-08-09  
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
- parallel branch `agent/product-simulation-case-screening-01`, especially:
  - S006 and `DECISION_MODEL_HANDOFF_2026-08-07.md`;
  - `product-simulation/CHALLENGE_CASE_SCREENING_02.md`;
  - `product-simulation/DECISION_MODEL_HANDOFF_CHALLENGE_PASS_02_2026-08-07.md`;
  - handoff commit `1992c865a96b99b807392ee2c27d866b40c2a130`;
- non-controlling `proposals/2026-07-20_UPGRADEPILOT_PRODUCT_AMBITION_AND_ENHANCEMENT_PROPOSAL.md`.

Historical simulations, proposals, old drafts, and parallel challenge-screening artifacts are **design/challenge evidence**, not automatic authority for the new model. Source/tests remain the authority for implemented behavior.

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
authoritative upstream changes relevant to that exact proposed transition
↓
zero or more material mechanism-specific technical impact candidates
    ├── upstream change mechanism
    ├── target-relevant exposure relationship/path
    ├── activation condition(s)
    └── possible target-relevant consequence
↓
for each impact candidate:
exact target/revision/context evidence
↓
applicability evaluation
    ├── established applicable
    ├── established not applicable
    ├── unresolved
    └── conflicted
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

This is a **discussion model**, not an approved runtime pipeline or schema.

Conversation A accepted that an `impact candidate` is the complete technical proposition connecting an upstream change to a possible target consequence through exposure and activation conditions; it is not another event inserted between change and exposure.

Conversation B now additionally preserves that one proposed dependency version transition may fan out into **multiple mechanism-specific impact candidates**, and applicability is evaluated **per impact candidate**, not once for the version transition as a whole.

A central emerging product insight is that UpgradePilot may be more accurately understood as an **evidence-driven impact and investigation system** than as a five-label classifier. The historical five action families may survive as a later projection, but that is not yet decided.

## 4. Current technical-impact and applicability model

### 4.1 Working impact-candidate definition

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

### 4.3 Impact candidate, exposure, activation, and consequence

Conversation A accepts this domain relationship:

```text
UPSTREAM CHANGE
What changed in the dependency?

        +

EXPOSURE
Through what target-relevant relationship/path
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

Exposure is a **relationship/pathway**, not merely a file, directory, subsystem, direct call, or target-owned code location.

Preserve explicitly:

```text
target relevance
!=
target ownership of the technically affected code
```

A target may be materially connected because it selects, composes, configures, registers, executes, or otherwise participates in a dependency/framework/plugin/environment graph even when the incompatible interaction itself occurs wholly inside dependencies or externally loaded plugin code.

The same subsystem/artifact can have different roles depending on the proposition. For a runtime dependency, tests/CI may be evidence; if pytest itself is the changed dependency, test execution can be part of the exposure while the resulting execution record is evidence.

Exposure and activation remain conceptually distinct, but real cases show they may be discovered from overlapping facts or tightly coupled in one runtime relationship. The conceptual distinction does **not** require separate scanners, classes, or evidence sources.

This accepted relationship is currently a **domain model**, not authorization to create runtime classes, enums, schemas, or a fixed serialized representation.

### 4.4 Version transitions fan out before target applicability reasoning

Challenge Pass 02 strengthens an important boundary:

```text
one dependency version transition
!=
one technical impact candidate
```

A safer reasoning shape is:

```text
exact proposed transition
↓
authoritative candidate upstream change mechanisms
↓
for each material mechanism:
    target-relevant exposure/path
    + activation condition(s)
    + possible consequence
    = mechanism-specific impact candidate
↓
for each impact candidate:
    applicability evaluation
```

For example, an urllib3 1.x → 2.x transition can contain independent API-removal, Python-support, OpenSSL/native-environment, TLS/hostname, and other runtime changes. Those mechanisms should not be collapsed into one aggregate `urllib3_2_risk` proposition merely because they occur in one release interval.

### 4.5 Conversation-B applicability working semantics

Applicability is evaluated for **one specific impact candidate** against **one exact target/revision/context**.

The core question is:

> Are the target-specific relationship and required activation propositions for this impact candidate sufficiently established or refuted within the supported evidence boundary?

Preserve the distinction between reality and UpgradePilot's justified knowledge state:

```text
REAL-WORLD PROPOSITION
Does this impact candidate apply to this exact target/revision/context?

        ↓

UPGRADEPILOT JUSTIFICATION STATE
What is the system justified in claiming from the supported evidence?
```

Current domain semantics:

```text
ESTABLISHED APPLICABLE
The required target-specific applicability propositions are sufficiently established.

ESTABLISHED NOT APPLICABLE
At least one necessary applicability proposition is sufficiently refuted,
closing only that bounded impact path.

UNRESOLVED
A material required applicability proposition cannot currently be
established or refuted within the supported evidence boundary.

CONFLICTED
Credible evidence about the same properly scoped applicability proposition
remains genuinely contradictory after identity, revision, semantic scope,
and relevant observation-time differences have been accounted for.
```

Hard protections:

```text
applicable
!=
consequence proven
```

```text
not applicable
!=
evidence missing
```

```text
dependency/framework presence
!=
activation established
```

```text
unresolved
!=
negative evidence
```

```text
different revision/time/scope observations
!=
automatically conflicted
```

`Applicable` means the candidate is sufficiently target-relevant to remain active for further reasoning/investigation. It does not prove that the possible consequence occurred, will occur, or is severe enough to determine action.

`Not applicable` requires supported negative evidence about at least one **necessary** proposition. Failure to find evidence for a condition is not by itself sufficient.

`Unresolved` is explicitly bounded to the evidence UpgradePilot is currently justified and supported to obtain/use. It does not claim that the proposition is unknowable in principle.

`Conflicted` is stronger than ordinary uncertainty. Before declaring conflict, normalize identity, target revision, semantic proposition, evidence scope, and observation time so that apparently different facts are not mistaken for contradiction.

These are domain semantics only. Final runtime vocabulary and representation remain deferred until the distinctions earn implementation.

### 4.6 Candidate exposure abstractions — still hypotheses

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

### 4.7 Materiality

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

Historical cases and parallel challenge cases remain evidence, not labels.

### S001 — Soup Sieve / Pydantic

Current live path proves one bounded concern:

```text
Soup Sieve Python 3.8 support drop introduced in 2.8
+ Pydantic exact-head requires-python >=3.10
→ support-drop concern outside declared Python range
```

CI dependency exercise remains `unresolved / dependency_exercise_not_proven`.

Conversation-B lesson:

```text
necessary activation proposition:
target admits Python 3.8

exact target evidence:
requires-python >=3.10

→ necessary proposition refuted
→ this impact candidate is not applicable
```

This closes one concern without proving global safety, compatibility, CI sufficiency, or reproducing the old manual `merge after normal review` label.

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

### Challenge Pass 02 — parallel stress-test evidence

Source artifacts:

- `agent/product-simulation-case-screening-01:product-simulation/CHALLENGE_CASE_SCREENING_02.md`
- `agent/product-simulation-case-screening-01:product-simulation/DECISION_MODEL_HANDOFF_CHALLENGE_PASS_02_2026-08-07.md`
- handoff commit `1992c865a96b99b807392ee2c27d866b40c2a130`

The handoff reviewed an older main baseline and remains non-controlling. It is consumed here as challenge evidence against the newer accepted A model and active B model.

#### C201 — pip-audit / CacheControl / Requests / urllib3

Material path:

```text
pip-audit
→ CacheControl
→ Requests / urllib3 response machinery
→ CacheControl assumption on urllib3.HTTPResponse.strict
```

Lesson:

```text
target relevance
!=
target ownership of the incompatible code
```

The actual incompatible interaction can exist several dependency edges away from target-owned source while remaining materially target-relevant because the target selects/composes that dependency graph.

This supports multi-hop/path reasoning and does not require reopening Conversation A or adding a new ownership concept.

#### C202 — Kedro / Pluggy dynamic hooks

At the exact historical target revision, Kedro constructs Pluggy's manager, loads `kedro.hooks` entry-point plugins, registers hooks, reaches lifecycle events, and allows Pluggy dispatch/result/exception semantics to mediate plugin-owned code.

A representative relationship is:

```text
Kedro registers contracts/plugins
→ Pluggy discovers/registers plugin implementations
→ Kedro reaches lifecycle hook
→ Pluggy dispatches implementations/wrappers
→ plugin-owned code executes
→ result/exception flows through Pluggy
→ Kedro execution continues
```

Conversation-B lesson:

```text
Pluggy present
!=
affected wrapper semantics activated
```

Applicability for a specific Pluggy mechanism may depend on candidate-specific propositions such as:

- affected version selected;
- relevant plugin installed;
- entry point discovered/registered;
- affected hook/wrapper present;
- relevant lifecycle event reached;
- changed dispatch/result/exception semantics actually relied upon.

Not every impact candidate requires every condition. The candidate defines what is necessary.

#### C203 — Buildtest / urllib3 environment pathway

Established:

```text
urllib3 2.x has an OpenSSL/native-environment support boundary
+ target runs in an externally managed NERSC/Perlmutter environment
+ target loads python/3.9-anaconda-2021.11
```

Not established:

```text
exact historical SSL implementation/version linked into that target environment
```

Therefore:

```text
environment pathway exists
+ upstream environment constraint exists
+ exact target activation unresolved
→ applicability unresolved for that mechanism
```

This is a canonical Conversation-B pressure test for:

```text
missing activation evidence
!=
not applicable
```

It also demonstrates that environment applicability may require an independent evidence path rather than inference from source or broad CI labels.

#### Existing build/codegen comparator

The prior `dominodatalab/container-runtime-interface-api#101` candidate remains useful:

```text
grpcio-tools
→ generation execution
→ generated Python source
→ committed/package artifact
→ later runtime consumption
```

Together the challenge evidence covers several topologies without forcing them into new accepted categories:

- multi-hop dependency interaction;
- plugin/framework inverted control;
- build/code-generation artifact mediation;
- environment/native-runtime mediation.

### Pass-02 bounded contribution

Challenge Pass 02 does **not** reopen Conversation A. It materially supports A's accepted exposure/path and impact-candidate model while adding B pressure around:

1. per-impact-candidate applicability;
2. target relevance without target ownership;
3. dynamic activation conditions;
4. unresolved environment activation;
5. multi-hop relevance and later stopping/traversal boundaries.

The last item remains partly a Conversation-B/Conversation-C problem rather than a reason to expand A.

## 7. Decisions and provisional conclusions

The numbering is intentionally retained so prior Git history remains easy to trace.

### D-001 — Use one reconciliation record
**Accepted 2026-08-06.** Preserve this whole-product reconciliation in one working-memory file before modifying controlling artifacts or implementing the next decision layer.

### D-002 — Stage boundaries do not constrain whole-product reasoning
**Accepted 2026-08-06.** B2/B3/B4 may later control implementation sequence, not what the correct whole-product model may contain.

### D-003 — Old artifacts are evidence, not automatic authority
**Accepted 2026-08-06.** Historical simulations, drafts, proposals, and later challenge-screening artifacts must be evaluated against current implementation and current product goals rather than inherited as machine truth.

### D-004 — Upstream change is not itself target impact
**Provisional design conclusion.** A separate target relationship/path must be established.

### D-005 — Preserve potential impact versus target applicability
**Provisional design conclusion.** A credible possible impact is not target-applicable until the relevant target-specific applicability/activation propositions are sufficiently established. Non-applicability closes only that bounded path.

### D-006 — Activation condition is central
**Provisional design conclusion.** Activation is the condition that must hold in the target/context for a particular impact candidate to matter.

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

### D-012 — Exposure is a target-relevant relationship/pathway
**Provisional design conclusion.** Exposure asks how changed dependency behavior could reach or matter to the target; it is not merely a repository location and does not require target ownership of the affected code.

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

### D-019 — Challenge Pass 02 is accepted as Conversation-B pressure-test evidence; A remains closed
**Accepted process/design decision 2026-08-09.** `CHALLENGE_CASE_SCREENING_02.md`, its handoff, and commit `1992c865...` are useful non-controlling evidence. They strengthen the accepted exposure/path and impact-candidate model and do not reveal a foundational contradiction requiring Conversation A to reopen.

### D-020 — Applicability is evaluated per mechanism-specific impact candidate
**Accepted domain decision 2026-08-09.** One exact dependency version transition may yield zero, one, or multiple material upstream change mechanisms, each producing its own impact candidate. Applicability is evaluated independently per candidate rather than as one aggregate property of the version transition.

### D-021 — Target relevance does not require target ownership, and dependency presence does not establish activation
**Accepted domain decision 2026-08-09.** A materially affected interaction may occur in transitive dependencies, framework machinery, dynamically loaded plugins, generated artifacts, or environment/native-runtime substrates. Target relevance follows the technical relationship/path, not code ownership. Merely proving that a dependency/framework is present is insufficient to establish the candidate-specific activation conditions.

### D-022 — Conversation-B applicability knowledge-state semantics
**Accepted domain decision 2026-08-09.** For one impact candidate and one exact target/revision/context:

- `established applicable` means required applicability propositions are sufficiently established;
- `established not applicable` means at least one necessary proposition is sufficiently refuted;
- `unresolved` means a material required proposition cannot currently be established or refuted within the supported evidence boundary;
- `conflicted` means credible evidence about the same properly scoped proposition remains genuinely contradictory after identity, revision, scope, and relevant observation-time differences are reconciled.

These semantics also preserve:

```text
applicable != consequence proven
not applicable != evidence missing
unresolved != negative evidence
```

No runtime enum/schema is authorized by this decision.

### D-023 — Exposure and activation are conceptually distinct without requiring physically separate evidence paths
**Accepted domain/process decision 2026-08-09.** A relationship/path and the condition that activates its relevance answer different questions, but a real fact can help establish both. The domain distinction must not be converted prematurely into mandatory separate scanners, classes, or evidence channels.

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
S001–S006 and later challenge cases should challenge the model; their historical actions must not become silent ground truth.

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

### H13 — Multi-hop traversal needs a decision-relative stopping boundary
Challenge Pass 02 proves that target relevance may require more than one dependency edge. It does not yet establish how far the system should traverse. The stopping rule should likely depend on whether further traversal can still change applicability, investigation choice, uncertainty, or confidence. This belongs partly to B/C and remains open.

### H14 — Candidate-specific activation can be compositional
Kedro/Pluggy suggests applicability may require several conjunctive or alternative propositions about version selection, plugin presence, registration, lifecycle reachability, and changed semantics. Exact logical composition rules should be learned from candidate structure rather than frozen as a universal schema now.

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
→ rejected; framework/declarative/constraint/data, environment, artifact, and multi-hop relationships matter
```

```text
reconciliation should completely model the domain before coding resumes
→ rejected; use decision-completeness and implementation feedback
```

```text
potential impact is a separate event between upstream change and exposure
→ rejected; impact candidate is the complete proposition
```

```text
one version transition = one aggregate impact candidate
→ rejected; transitions may fan out into mechanism-specific candidates
```

```text
target relevance requires target-owned affected code
→ rejected
```

```text
dependency/framework presence = activation
→ rejected
```

```text
missing evidence = not applicable
→ rejected
```

```text
evidence from different revisions/times/scopes = automatically conflicted
→ rejected
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
4. the model remains coherent across S001, S003, S004, S005, S006, later Challenge Pass 02 stress tests, and recorded counterexamples;
5. remaining taxonomy and representation questions can safely be deferred;
6. no remaining ambiguity was found that would make Conversation B fundamentally wrong.

A does **not** claim a complete taxonomy, every ecosystem/security/build/platform case, final graph model, exposure enum, policy schema, temporal implementation, package-manager universality, or final runtime classes.

Closure review classification:

```text
ACCEPTED FORWARD SEMANTICS
upstream change
+ target-relevant exposure relationship/path
+ activation condition(s)
+ possible consequence
= impact candidate

NEXT QUESTION
Does this impact candidate actually apply to this exact target/revision/context,
and what evidence justifies that state?
```

### Conversation B — Applicability and investigation activation

**Question:** How does UpgradePilot determine whether a possible impact actually matters to this exact target/revision/context?

**Status:** **ACTIVE — foundational applicability-state semantics accepted; necessary-proposition/evidence sufficiency reasoning is next.**

B can close when:

1. applicability propositions and activation conditions have coherent positive/negative/unresolved/conflicted semantics;
2. the system can identify which propositions are **necessary** for a given impact candidate without assuming dependency presence equals activation;
3. supported evidence can establish or refute those propositions without converting absence of evidence into negative evidence;
4. conflict is scoped to genuinely contradictory credible evidence about the same proposition after identity/revision/time normalization;
5. deterministic-versus-semantic evidence boundaries are clear enough for the next implementation/design decision;
6. representative direct, multi-hop, dynamic-plugin, artifact-mediated, and environment-mediated cases do not expose a foundational contradiction.

B does **not** require every repository inspection technique, language ecosystem, package manager, configuration grammar, final logical-expression schema, or graph traversal implementation.

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

Current judgment still favors continuing Conversation B because the meaning of candidate-specific necessary propositions and the evidence needed to establish/refute them is the next foundational dependency of a correct decision contract. No new runtime representation is yet justified merely from the accepted semantics.

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
16. **Candidate granularity** — are multiple upstream mechanisms being incorrectly collapsed into one impact candidate?
17. **Ownership independence** — is target relevance being incorrectly inferred from code ownership/directness?
18. **Applicability knowledge state** — are we describing software reality or only what current evidence justifies us in claiming?

## 12. Deliberately deferred questions

Do not solve these merely to make the model look complete:

- final runtime applicability-state vocabulary/enum/schema;
- detailed negative-evidence proof methods beyond what B's next decision requires;
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
- universal logical-expression representation for activation conditions;
- exact multi-hop graph traversal/stopping implementation;
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

The foundational knowledge-state vocabulary is now sufficiently clear for the next question. Do **not** reopen Conversation A and do **not** implement enums/classes/schema yet.

### Next smallest foundational question

> **For one mechanism-specific impact candidate, which target/context propositions are actually necessary for applicability, and what evidence is sufficient to establish or refute each proposition without confusing missing evidence with negative evidence?**

Use this reasoning shape:

```text
mechanism-specific impact candidate
├── upstream change mechanism
├── target-relevant exposure/path
├── candidate-specific necessary activation/applicability propositions
└── possible consequence
        ↓
exact target/revision/context evidence
        ↓
for each necessary proposition:
    established / refuted / unresolved / genuinely conflicted
        ↓
combine only as much as needed to justify
candidate applicability or bounded non-applicability
```

Pressure-test the discussion with four contrasting anchors:

### Anchor 1 — S001: supported bounded refutation

```text
necessary proposition:
target admits Python 3.8

exact evidence:
Pydantic requires-python >=3.10

→ proposition refuted
→ candidate not applicable
```

Question: what makes this negative evidence strong enough rather than merely absence of Python-3.8 evidence?

### Anchor 2 — Buildtest: unresolved activation

```text
environment pathway established
+ upstream OpenSSL constraint established
+ exact historical target SSL implementation unknown

→ activation proposition unresolved
```

Question: what is the supported evidence boundary, and why is this not `not applicable`?

### Anchor 3 — Kedro/Pluggy: compositional activation

Potential applicability may depend on some combination of:

- affected Pluggy version selected;
- relevant plugin installed;
- entry-point discovery/registration;
- affected hook/wrapper implementation present;
- relevant lifecycle event reached;
- affected dispatch/result/exception semantics relied upon.

Question: how do we identify which propositions are actually **necessary** for one specific impact candidate rather than treating every plausible runtime fact as mandatory?

### Anchor 4 — pip-audit: multi-hop target relevance

```text
pip-audit
→ CacheControl
→ Requests / urllib3 machinery
→ CacheControl assumption on urllib3.HTTPResponse.strict
```

Question: what evidence is needed to establish a target-relevant multi-hop path when the incompatible interaction is not target-owned?

### B discussion tasks after the next question

Determine only what is needed for the next correct design step:

1. meaning of a candidate-specific **necessary applicability proposition**;
2. what qualifies as sufficient positive evidence;
3. what qualifies as sufficient bounded negative evidence/refutation;
4. how the supported evidence boundary controls `unresolved`;
5. when apparent disagreement becomes genuine `conflicted` after identity/scope/time normalization;
6. which evaluations can remain deterministic and where bounded semantic interpretation may be necessary without granting an LLM authority over final applicability;
7. whether further conceptual work remains more valuable than a bounded implementation/evaluation after these semantics are stable.

Do not enumerate every ecosystem-specific inspection technique and do not design runtime logical-expression structures yet. Apply the decision-need test from Section 2.