# UpgradePilot Product Decision-Model Reconciliation Working Record

**Date opened:** 2026-08-06  
**Last discussion sync:** 2026-08-09  
**Status:** Active design discussion; Conversation A closed; Conversation B active; applicability-proposition semantics accepted; evidence-sufficiency reasoning next  
**Purpose:** Preserve the current whole-product decision-model position, important rationale, active hypotheses, open questions, stop lines, and eventual accepted repository changes without turning this file into an append-only transcript.  
**Live-state owner:** `../MEMORY.md` remains the sole owner of current project position and exact implementation continuation.  
**Pre-consolidation snapshot:** commit `e158fe041597ecb6176f4d5dab6b11961f30c8e1` preserves an earlier chronological/repetitive form of this record in Git history.

## 1. Why this reconciliation exists

UpgradePilot completed the bounded Target-Python Support Relevance responsibility through the normal live path. That implementation now has materially stronger evidence identity, provenance, grounding, target relevance, and explicit failure/unresolved behavior than when the earlier transparent-decision documents and product-simulation conclusions were written.

The next active implementation plan pointed toward a Transparent Decision Method, but the repository audit showed that implementing the old decision framing immediately could encode stale or underspecified concepts, especially:

- a too-direct `evidence → action` mapping;
- historical simulation actions treated too much like machine truth;
- insufficient separation between upstream change, target impact, applicability, evidence, and final action;
- undefined repository-specific semantics around labels such as `merge after normal review`;
- missing first-class treatment of investigation selection and stopping;
- unclear policy, trust, identity/freshness, and human-authority boundaries.

Therefore implementation of the decision/recommendation layer remains intentionally paused while the minimum necessary whole-product semantics are reconciled.

This pause is **not** authorization for open-ended architecture work. The goal is just enough semantic stability for the next correct product or implementation decision, followed by implementation/evaluation feedback.

---

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

Historical/discovery/challenge evidence considered includes:

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

The reconciliation preserves:

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

Do not force every discussion result into an enum, schema, class hierarchy, Boolean-expression engine, graph implementation, or framework before the domain relationship has earned that representation.

---

## 3. Current whole-product discussion model

The old conceptual shortcut was too compressed:

```text
evidence
→ action
```

The current discussion model is:

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
derive candidate-specific target/revision/context applicability propositions
↓
evaluate propositions against scoped evidence
    ├── established
    ├── refuted
    ├── unresolved
    └── genuinely conflicted
↓
combine only as much as necessary according to the candidate's logical structure
↓
candidate applicability knowledge state
    ├── established applicable
    ├── established not applicable
    ├── unresolved
    └── conflicted
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

This remains a **discussion/domain model**, not an approved runtime pipeline or schema.

A central emerging product insight remains that UpgradePilot may be more accurately understood as an **evidence-driven impact and investigation system** than as a five-label classifier. The historical five action families may survive as a later projection, but that is not yet decided.

---

## 4. Conversation A — accepted technical-impact model

### 4.1 Impact-candidate definition

> **A technical impact candidate is a target-relevant proposition that the proposed dependency transition could cause or enable a technical consequence through a technical relationship with the target under relevant activation conditions.**

The accepted domain relationship is:

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

`Impact candidate` names the **whole proposition**, not another intermediate event. `Consequence` is one component: the possible target-side technical difference.

### 4.2 Upstream change is not target impact

```text
upstream change
!=
target impact
```

Example:

```text
Soup Sieve drops Python 3.8
→ candidate concern for Python 3.8 consumers
→ Pydantic declares requires-python >=3.10
→ that bounded support-drop concern is outside the declared target range
```

This closes one impact path only. It does not prove global compatibility, upgrade safety, CI sufficiency, or mergeability.

### 4.3 Exposure is target relevance, not ownership

Exposure is a **target-relevant relationship/pathway**, not merely a file, directory, subsystem, direct call, or target-owned code location.

Preserve:

```text
target relevance
!=
target ownership of the technically affected code
```

A target may be materially connected because it selects, composes, configures, registers, executes, or otherwise participates in a dependency/framework/plugin/environment graph even when the incompatible interaction occurs wholly inside dependencies or externally loaded plugin code.

Exposure and activation remain conceptually distinct, but real cases show they may be discovered from overlapping facts or tightly coupled in one runtime relationship. This conceptual distinction does **not** require separate scanners/classes/evidence channels.

### 4.4 One version transition may yield multiple candidates

```text
one dependency version transition
!=
one technical impact candidate
```

Reasoning shape:

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
```

For example, an urllib3 1.x → 2.x transition can contain independent API-removal, Python-support, OpenSSL/native-environment, TLS/hostname, and other runtime changes. Those mechanisms must not be collapsed into one aggregate `urllib3_2_risk` proposition merely because they occur in one release interval.

### 4.5 Materiality

Materiality is decision-relative:

```text
severity != materiality
likelihood != materiality
interesting != material
material != harmful
```

A useful test is:

> If this impact were present versus absent, could a material investigation state, required check, uncertainty, or maintainer-facing result change?

If not, it normally should not consume deeper investigation.

### 4.6 Candidate exposure abstractions remain hypotheses

Possible reusable coupling roots remain hypotheses only:

1. execution/control-flow coupling;
2. declarative/interpreted coupling;
3. constraint/environment coupling;
4. data/artifact-contract coupling.

Exposure may also be multi-hop/graph-shaped. None of this authorizes a graph database, final exposure enum, or runtime hierarchy.

---

## 5. Conversation B — current applicability model

### 5.1 Applicability evaluates a proposition, not a vague risk label

Applicability is evaluated for **one mechanism-specific impact candidate** against **one exact target/revision/context**.

The core question is:

> Are the candidate-specific target/revision/context propositions required for the candidate's relevant exposure and activation sufficiently supported or refuted within the supported evidence boundary?

Preserve reality versus system knowledge:

```text
REAL-WORLD PROPOSITION
Does this impact candidate apply to this exact target/revision/context?

        ↓

UPGRADEPILOT JUSTIFICATION STATE
What is the system justified in claiming from the supported evidence?
```

Current knowledge-state semantics:

```text
ESTABLISHED APPLICABLE
The candidate's required applicability propositions are sufficiently established
for at least one complete viable applicability path.

ESTABLISHED NOT APPLICABLE
The evidence sufficiently eliminates every viable applicability path,
for example by refuting a proposition necessary across all remaining paths
or by separately closing all alternatives.

UNRESOLVED
A material proposition required to decide applicability cannot currently be
established or refuted within the supported evidence boundary.

CONFLICTED
Credible evidence about the same properly scoped applicability proposition
remains genuinely contradictory after identity, revision, semantic scope,
and relevant observation-time differences have been reconciled.
```

Hard protections:

```text
applicable != consequence proven
not applicable != evidence missing
unresolved != negative evidence
dependency/framework presence != activation established
target relevance != target ownership
different revision/time/scope observations != automatically conflicted
```

### 5.2 Necessary and sufficient conditions

For Conversation B, a **proposition** is a target/revision/context statement that evidence can establish, refute, leave unresolved, or place in genuine conflict.

A **necessary applicability proposition** is a proposition whose truth is required for a particular candidate path to remain viable.

If a candidate path is:

```text
A AND B AND C
```

then refuting any one of `A`, `B`, or `C` closes that path.

But real candidate structure may contain alternatives:

```text
A AND (B OR C)
```

In that case, refuting `B` alone does not close the candidate because `C` may still keep a viable path open.

Therefore the accepted rule is:

> **A proposition refutation supports candidate-level non-applicability only when that refutation eliminates every remaining viable applicability path, either because the proposition is necessary across those paths or because all alternatives are independently closed.**

This avoids the dangerous shortcut:

```text
found one inactive condition
→ whole candidate not applicable
```

when an alternate valid activation path exists.

### 5.3 Candidate structure determines composition

Applicability logic belongs to the **specific impact candidate**, not the dependency as a whole.

Kedro/Pluggy illustrates why. One particular wrapper-semantics candidate might depend on propositions such as:

- affected Pluggy version selected;
- relevant plugin installed;
- entry point discovered/registered;
- affected wrapper/hook implementation present;
- relevant lifecycle event reached;
- changed dispatch/result/exception semantic actually involved.

Another Pluggy mechanism may require a different subset or structure.

Accepted rule:

> **The upstream mechanism, exposure path, activation conditions, and possible consequence determine which applicability propositions are necessary and how they compose. UpgradePilot must not impose one universal checklist per dependency/framework.**

This accepts compositional semantics but does **not** authorize a universal Boolean-expression engine, AST, rules language, or schema yet.

### 5.4 Positive applicability

For a simple conjunction:

```text
A AND B AND C
```

positive applicability requires sufficient evidence establishing all propositions needed for a complete viable path.

For alternatives:

```text
A AND (B OR C)
```

positive applicability requires `A` plus at least one sufficiently established alternative (`B` or `C`).

Thus:

```text
candidate applicable
!=
all imaginable target facts proven
```

UpgradePilot should establish only the propositions needed to justify a complete candidate path.

`Established applicable` still does **not** mean:

- consequence observed;
- consequence certain to occur;
- severity proven;
- compatibility globally disproven;
- merge/defer decided.

It means the candidate is sufficiently target-relevant to remain active for further reasoning/investigation.

### 5.5 Bounded non-applicability

`Established not applicable` requires **real refutation**, not search failure.

For a candidate to be closed negatively, the evidence must establish enough falsehood to eliminate every viable applicability path.

Canonical S001 example:

```text
candidate:
Soup Sieve dropping Python 3.8 support could affect Pydantic's supported Python environments

necessary proposition:
Pydantic admits Python 3.8

exact evidence:
requires-python >=3.10

→ proposition refuted
→ no Python-3.8 activation path remains
→ candidate established not applicable
```

This is strong negative evidence because the authoritative target declaration directly bounds the relevant support set. It is not merely failure to find a Python-3.8 reference.

### 5.6 Absence of evidence versus evidence of absence

Preserve:

```text
ABSENCE OF EVIDENCE
!=
EVIDENCE OF ABSENCE
```

Examples:

```text
"I searched the README and did not find Python 3.8"
```

normally does not establish that Python 3.8 is unsupported.

Whereas:

```text
exact authoritative requires-python >=3.10
```

directly excludes Python 3.8 from the declared installation range.

Negative conclusions generally require a stronger observation boundary than positive discoveries.

### 5.7 Supported evidence boundary and unresolved state

Buildtest is the canonical unresolved example:

```text
urllib3 2.x OpenSSL/native-environment constraint established
+ target external HPC runtime pathway established
+ exact historical target SSL implementation/version not established
```

Therefore:

```text
activation proposition = unresolved
→ candidate applicability = unresolved
```

The correct conclusion is not `not applicable` because no evidence establishes that the historical SSL version was outside the affected range.

`Unresolved` is always relative to a **supported evidence boundary**. It means UpgradePilot cannot currently justify true or false using evidence it is supported and justified to acquire/use. It does not mean the proposition is unknowable in principle.

### 5.8 Evidence-sufficiency criteria accepted at the reasoning level

Before evidence can establish or refute an applicability proposition, judge at least four dimensions:

#### Scope

Does the evidence describe the same object being evaluated?

Check where relevant:

- exact dependency transition;
- exact PR/proposal identity;
- exact target/base/head revision;
- exact environment/context;
- same semantic proposition;
- relevant observation-time boundary.

Evidence from current `main` does not automatically prove facts about a historical PR head.

#### Authority

Why is this source trustworthy for this particular proposition?

Possible authorities depend on the proposition and can include exact target declarations, lockfiles, source at immutable revision, authoritative upstream release material, actual execution records, or exact environment metadata.

Authority is proposition-relative; there is no universal source ranking that answers every question.

#### Discriminating power

Does the evidence actually answer the proposition?

Examples:

```text
"CI ran on Linux"
```

is usually insufficient to answer:

```text
"Was OpenSSL <1.1.1?"
```

Likewise:

```text
"Kedro imports Pluggy"
```

does not establish:

```text
"An affected wrapper implementation was installed, registered, and exercised."
```

Relevant evidence is not necessarily discriminating evidence.

#### Completeness / observation boundary for negative claims

Negative claims often require evidence that the relevant search/observation space was complete enough to justify absence.

Examples:

- an exact authoritative version specifier can create a bounded set/range suitable for deterministic exclusion;
- a complete installed-entry-point inventory may support absence of a specific plugin in that environment;
- grepping target source usually cannot prove absence of externally installed plugins.

This creates the next open question around **open-world versus closed-world reasoning** and what counts as a sufficient observation boundary.

These four dimensions are accepted as evidence-sufficiency reasoning criteria. They are **not** a final score, formula, schema, or universal ranking system.

### 5.9 Conflict belongs at proposition level

Before declaring `conflicted`, normalize:

- proposition identity;
- target/proposal identity;
- revision;
- semantic scope;
- environment/context;
- observation time where material;
- evidence authority/credibility.

Example:

```text
base revision says Python >=3.9
head revision says Python >=3.10
```

is not automatically conflict; the observations describe different revisions.

Only after normalization, if credible evidence about the **same scoped proposition** genuinely supports incompatible truth values, should the proposition be `conflicted`.

---

## 6. Decision-relevant context outside technical impact

Preserve:

```text
TARGET TECHNICAL IMPACT
!=
ALL DECISION-RELEVANT INFORMATION
```

### 6.1 Trust / authority context

Examples:

- package-to-upstream provenance;
- source authority;
- conflicting authoritative sources;
- grounding/corroboration quality;
- unavailable or unsupported evidence acquisition.

These affect what UpgradePilot is justified in claiming. They are not automatically target technical impacts.

### 6.2 Identity / revision / observation / freshness context

Proposal identity controls the object being assessed. A later dependency release does not silently replace the exact proposed transition.

Target evidence should be bound to exact immutable revisions where available. Mutable external facts are observations of a source/world-state at acquisition time.

Preserve:

```text
historically valid observation
!=
necessarily sufficient for a later current decision
```

This does not imply continuous monitoring; exact freshness/recheck rules remain deferred.

### 6.3 Policy / governance / licensing context

Repository or organizational rules may constrain action without changing technical truth, including license/compliance restrictions, required human/security review, required CI checks, release freezes, approval ownership, and repository-specific risk rules.

### 6.4 Security can span multiple roles

Do not use `security` as one flat category.

- vulnerable behavior that reaches an exposed target path can be technical impact;
- unverified publisher/package identity may be trust/provenance context;
- mandatory security review may be repository policy.

The proposition determines the role.

---

## 7. Case-derived evidence that currently matters

Historical cases and parallel challenge cases remain evidence, not labels.

### S001 — Soup Sieve / Pydantic

```text
Soup Sieve Python 3.8 support drop introduced in 2.8
+ Pydantic exact-head requires-python >=3.10
→ support-drop concern outside declared Python range
```

Conversation-B lesson:

```text
necessary proposition: target admits Python 3.8
exact authoritative evidence: requires-python >=3.10
→ proposition refuted
→ candidate not applicable
```

This is the canonical bounded-refutation case.

### S003 — dependency/peer constraints

Impact may occur through dependency graph/resolution constraints rather than direct runtime calls. Installability is a target-relevant technical property.

### S004 — transparent baseline

Coarse evidence can sometimes be sufficient after authority-critical assumptions are confirmed. Deeper analysis must earn its cost.

### S005 — activation and target relevance

Reusable pattern:

```text
upstream statement/change
→ activation condition
→ target configuration/source/usage relationship
→ evidence/coverage
→ unresolved question OR bounded closure
```

### S006 — qldebugger / Pydantic validator semantics

```text
upstream validator behavior change
→ exposure: target participates in Pydantic validator/framework semantics
→ activation: affected dependency version + non-string handler input
→ consequence: observable exception-contract change
→ evidence: source/tests/workflow/differential reproduction
```

Lesson: broad test/CI coverage is not the same as discriminating coverage of the affected behavior path.

### Challenge Pass 02 — parallel stress tests

Sources:

- `agent/product-simulation-case-screening-01:product-simulation/CHALLENGE_CASE_SCREENING_02.md`
- `agent/product-simulation-case-screening-01:product-simulation/DECISION_MODEL_HANDOFF_CHALLENGE_PASS_02_2026-08-07.md`
- handoff commit `1992c865a96b99b807392ee2c27d866b40c2a130`

These remain non-controlling evidence.

#### C201 — pip-audit / CacheControl / Requests / urllib3

```text
pip-audit
→ CacheControl
→ Requests / urllib3 response machinery
→ CacheControl assumption on urllib3.HTTPResponse.strict
```

Lesson:

```text
target relevance != target ownership
```

A target-relevant incompatibility may occur several dependency edges away from target-owned source.

#### C202 — Kedro / Pluggy

Representative path:

```text
Kedro registers contracts/plugins
→ Pluggy discovers/registers implementations
→ Kedro reaches lifecycle hook
→ Pluggy dispatches implementations/wrappers
→ plugin-owned code executes
→ result/exception returns through Pluggy
```

Lesson:

```text
Pluggy present != affected wrapper semantics activated
```

Applicability is compositional and candidate-specific.

#### C203 — Buildtest / urllib3 environment

```text
environment pathway established
+ upstream OpenSSL constraint established
+ exact historical target SSL implementation unknown
→ applicability unresolved
```

Canonical lesson:

```text
missing activation evidence != not applicable
```

#### Build/codegen comparator

```text
grpcio-tools
→ generation execution
→ generated Python source
→ committed/package artifact
→ later runtime consumption
```

Together the challenge evidence covers multi-hop dependency interaction, framework/plugin inverted control, artifact mediation, and environment/native-runtime mediation without requiring new fixed categories.

---

## 8. Decisions and provisional conclusions

Numbering remains stable for Git-history traceability.

### D-001 — Use one reconciliation record
**Accepted 2026-08-06.** Preserve this whole-product reconciliation in one working-memory file before modifying controlling artifacts or implementing the next decision layer.

### D-002 — Stage boundaries do not constrain whole-product reasoning
**Accepted 2026-08-06.** B2/B3/B4 may later control implementation sequence, not what the correct whole-product model may contain.

### D-003 — Old artifacts are evidence, not automatic authority
**Accepted 2026-08-06.** Historical simulations, drafts, proposals, and later challenge-screening artifacts must be evaluated against current implementation and current product goals rather than inherited as machine truth.

### D-004 — Upstream change is not itself target impact
**Provisional design conclusion.** A target-relevant relationship/path must be established.

### D-005 — Preserve impact candidate versus target applicability
**Provisional design conclusion.** A credible possible impact is not target-applicable until the relevant target-specific applicability/activation propositions are sufficiently established. Non-applicability closes only that bounded candidate/path.

### D-006 — Activation condition is central
**Provisional design conclusion.** Activation is the condition that must hold in the target/context for a particular impact candidate to matter.

### D-007 — Dependency impact and unrelated repository condition remain distinguishable
**Provisional design conclusion.** Failing CI or another repository condition does not become dependency impact without causal evidence.

### D-008 — Materiality is decision-relative
**Provisional design conclusion.** Severity, likelihood, interestingness, harm, and materiality are distinct.

### D-009 — Control variation through domain abstractions, not case rules
**Provisional design conclusion.** Normalize recurring relationships and predicates rather than multiplying fixture-specific rules. Preserve value/state/structural variation as different problems.

### D-010 — Do not freeze a flat impact enum
**Provisional design conclusion.** `API / security / platform / performance / CI / build` mixes change mechanism, exposure, consequence, and evidence.

### D-011 — CI/tests/source/config/metadata are not automatically impacts
**Provisional design conclusion.** Their semantic role is proposition-relative.

### D-012 — Exposure is a target-relevant relationship/pathway
**Provisional design conclusion.** Exposure is not merely a repository location and does not require target ownership of affected code.

### D-013 — Role is contextual
**Provisional design conclusion.** The same subsystem/artifact may be exposure in one proposition and evidence in another.

### D-014 — Technical target impact is not all decision-relevant information
**Provisional design conclusion.** Trust/authority, currentness/supersession, policy/governance/licensing, and similar concerns may affect claims/actions without themselves being technical target impacts.

### D-015 — Proposal identity controls the assessed object; mutable external evidence is time-bounded observation
**Provisional design conclusion.** Later releases do not silently replace the proposal. Correctly scoped observations remain historically valid even if the world later changes, though they may stop being sufficient for a current decision.

### D-016 — Reconciliation is bounded by decision need
**Accepted process decision 2026-08-07.** Resolve questions now only when failing to do so risks the next correct product/architecture/evidence-contract/implementation decision.

### D-017 — Impact candidate is the complete technical proposition
**Accepted domain decision 2026-08-08.** Preserve upstream change, exposure relationship/path, activation condition(s), and possible target consequence as distinct roles. `Impact candidate` names the proposition connecting them. No runtime class/enum/schema is authorized by this decision.

### D-018 — Conversation A is sufficiently closed
**Accepted process/design decision 2026-08-08.** No remaining A ambiguity was found capable of making Conversation B fundamentally wrong. Taxonomy/representation details remain deferred.

### D-019 — Challenge Pass 02 is Conversation-B pressure-test evidence; A remains closed
**Accepted process/design decision 2026-08-09.** The parallel challenge artifacts strengthen the exposure/path and impact-candidate model and do not reveal a foundational contradiction requiring A to reopen.

### D-020 — Applicability is per mechanism-specific impact candidate
**Accepted domain decision 2026-08-09.** One version transition may yield zero, one, or multiple mechanisms/candidates. Applicability is evaluated independently per candidate.

### D-021 — Target relevance does not require target ownership; presence does not establish activation
**Accepted domain decision 2026-08-09.** Material interaction may occur in transitive dependencies, framework machinery, dynamic plugins, generated artifacts, or environment/native-runtime substrates. Dependency/framework presence alone is insufficient to establish activation.

### D-022 — Applicability knowledge-state semantics
**Accepted domain decision 2026-08-09.** Use the conceptual states `established applicable`, `established not applicable`, `unresolved`, and `conflicted` with the boundaries defined in Section 5. These describe what evidence justifies UpgradePilot in claiming, not four metaphysical states of software reality. No runtime enum/schema is yet authorized.

### D-023 — Exposure and activation are conceptually distinct without requiring separate evidence machinery
**Accepted domain/process decision 2026-08-09.** They answer different questions, but one fact may help establish both. Do not prematurely require separate scanners/classes/channels.

### D-024 — Applicability is proposition-based
**Accepted domain decision 2026-08-09.** UpgradePilot should evaluate explicit target/revision/context propositions derived from the mechanism-specific impact candidate rather than infer applicability from vague labels such as `dependency used`, `risk present`, or `CI touches dependency`.

**Why:** evidence can establish/refute concrete propositions; it cannot reliably justify an abstract applicability label without exposing the statements on which that label depends. This preserves traceability and separates domain relationships from evidence evaluation.

### D-025 — Candidate structure determines necessary propositions and logical composition
**Accepted domain decision 2026-08-09.** Necessary applicability propositions and their conjunction/alternative structure derive from the specific upstream mechanism, target-relevant path, activation conditions, and consequence. They are not a universal dependency/framework checklist.

**Why:** S001 is structurally simple, while Kedro/Pluggy can require dynamic plugin/registration/lifecycle conditions and may contain alternative activation paths. A universal checklist would either over-constrain simple cases or miss real complex paths.

**Non-commitment:** this accepts logical composition semantically but does not authorize a Boolean AST, rule language, planner schema, or generalized expression engine.

### D-026 — Positive applicability requires a sufficiently established complete viable path
**Accepted domain decision 2026-08-09.** `Established applicable` requires sufficient evidence for the propositions needed to establish at least one complete candidate path. It does not require proving every imaginable target fact or every alternative path.

**Why:** for `A AND (B OR C)`, evidence for `A + B` can be sufficient even if `C` is unknown. Requiring all alternatives would create unnecessary investigation and violate the project's conditional-stopping discipline.

**Boundary:** applicability still does not prove the consequence occurred or determine maintainer action.

### D-027 — Non-applicability requires elimination of every viable applicability path
**Accepted domain decision 2026-08-09.** Candidate-level `established not applicable` requires sufficient refutation to eliminate every viable path. This may occur by refuting a proposition necessary across all remaining paths or by independently closing all alternatives.

**Why:** in `A AND (B OR C)`, refuting `B` alone cannot justify non-applicability while `C` remains viable. This prevents premature negative closure and preserves correctness under compositional activation.

### D-028 — Missing evidence is unresolved; negative evidence requires genuine refutation within an adequate observation boundary
**Accepted domain decision 2026-08-09.** Failure to observe or discover a proposition does not by itself refute it. Negative closure requires evidence that directly discriminates the proposition and, when absence is claimed, an observation boundary complete enough to justify that absence.

**Why:** S001's exact `requires-python >=3.10` directly excludes Python 3.8; Buildtest's unknown historical OpenSSL version does not exclude the affected range; grepping target source cannot prove absence of externally installed plugins.

This decision establishes the principle but leaves the exact open-world/closed-world sufficiency boundary as the next active question.

### D-029 — Evidence sufficiency is proposition-relative and judged by scope, authority, discriminating power, and negative-claim completeness
**Accepted reasoning decision 2026-08-09.** Evidence used to establish/refute an applicability proposition should be evaluated for:

1. **scope** — same proposal/revision/context/proposition/time boundary;
2. **authority** — justified source for that proposition;
3. **discriminating power** — actually answers the proposition rather than merely correlating with it;
4. **completeness/observation boundary** where a negative claim depends on absence.

**Why:** a Linux CI label does not answer an exact OpenSSL-version proposition; a Pluggy import does not prove an affected wrapper is registered; an exact target version declaration can directly exclude a runtime range.

**Non-commitment:** these are reasoning criteria, not a numeric score, universal source ranking, or final sufficiency formula.

### D-030 — Conflict is proposition-scoped after identity/scope/time normalization
**Accepted domain decision 2026-08-09.** `Conflicted` requires credible evidence that genuinely disagrees about the same scoped proposition after proposal identity, target revision, semantic scope, environment/context, and relevant observation-time differences are reconciled.

**Why:** base and head revisions can legitimately contain different declarations; historical and current observations can differ because the world changed. Treating these as contradictions would manufacture false conflict.

---

## 9. Active hypotheses — not final architecture

### H1 — Impact/investigation may be more central than five-class recommendation
The product may be better represented as evidence-driven impact/investigation reasoning with later synthesis rather than as a primary five-label classifier.

### H2 — Action classes may become a projection
Historical action families may survive as maintainer-facing summaries rather than the central internal model.

### H3 — “Normal review” may not be UpgradePilot-owned
Without explicit repository policy, `normal review` is too repository-specific to assume as a universal runtime action.

### H4 — Targeted investigation is a core value proposition
A major product advantage may be choosing what decision-relevant question matters next, what evidence/check can discriminate it, and when not to investigate further.

### H5 — Historical simulations remain evidence, not labels
S001–S006 and challenge cases should challenge the model; historical actions must not become silent ground truth.

### H6 — Current Python-support implementation is one proven impact slice
It demonstrates one real change → target evidence → bounded relevance/closure path but is not a universal implementation template.

### H7 — Flat impact taxonomy is probably wrong
A multidimensional model appears more general and less prone to combinatorial rule growth.

### H8 — Technical exposure may compress into a small number of coupling/contract relationships
Execution/control-flow, declarative/interpreted, constraint/environment, and data/artifact-contract are candidate roots only.

### H9 — Exposure can be multi-hop/graph-shaped
Impact paths may traverse intermediate components; this is a domain observation, not an implementation commitment.

### H10 — Technical exposure is only one subset of the larger decision model
The larger synthesis likely also needs trust/authority, identity/freshness/supersession, policy/governance/licensing, and possibly other decision context.

### H11 — Do not inflate identity/freshness into continuous temporal monitoring
Prefer exact identity/revision binding, observation boundaries, materially justified freshness/supersession checks, and decision-time reconstruction.

### H12 — Use just-enough design
Avoid ambiguous premature implementation and architecture paralysis. Stop conceptual work once semantic stability is sufficient for the next correct decision and seek implementation/evaluation feedback.

### H13 — Multi-hop traversal needs a decision-relative stopping boundary
Challenge Pass 02 proves that target relevance may require more than one dependency edge. It does not yet establish how far traversal should continue. This belongs partly to B/C.

### H14 — Candidate-specific activation can be compositional
Applicability may require conjunctive and alternative propositions. Exact runtime logical representation remains deferred.

---

## 10. Important corrections and rejected shortcuts

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
→ rejected
```

```text
potential impact is a separate event between upstream change and exposure
→ rejected; impact candidate is the complete proposition
```

```text
one version transition = one aggregate impact candidate
→ rejected
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
one failed activation branch = candidate not applicable
→ rejected when another viable activation path remains
```

```text
positive applicability requires proving every alternative path
→ rejected; one sufficiently established complete viable path is enough
```

```text
relevant evidence = sufficient evidence
→ rejected; scope/authority/discriminating power matter
```

```text
evidence from different revisions/times/scopes = automatically conflicted
→ rejected
```

```text
reconciliation should completely model the domain before coding resumes
→ rejected; use decision-completeness and implementation feedback
```

---

## 11. Four reconciliation conversations and stop lines

### Conversation A — Dependency-update impact/problem model

**Question:** What can count as technical impact/concern, and what should `impact` mean?

**Status:** **CLOSED 2026-08-08.**

A closed because:

1. technical impact has a usable boundary;
2. upstream change, exposure, activation, consequence, impact candidate, applicability, and evidence are distinguishable enough for the next design step;
3. neighboring trust/policy/identity concerns are not silently collapsed into technical impact;
4. the model survives S001/S003/S004/S005/S006 and Challenge Pass 02 stress tests;
5. remaining taxonomy/representation details can safely be deferred;
6. no remaining ambiguity was found capable of making B fundamentally wrong.

### Conversation B — Applicability and investigation activation

**Question:** How does UpgradePilot determine whether a possible impact actually matters to this exact target/revision/context?

**Status:** **ACTIVE — proposition-based applicability and composition semantics accepted; evidence-sufficiency/open-vs-closed-world boundary is next.**

B can close when:

1. applicability propositions and activation conditions have coherent positive/negative/unresolved/conflicted semantics;
2. candidate-specific necessary propositions and alternative paths can be reasoned about without a universal checklist;
3. supported evidence can establish/refute propositions without converting absence into negative evidence;
4. the evidence boundary for strong negative claims is coherent enough for the next design step;
5. conflict is proposition-scoped after identity/revision/scope/time normalization;
6. deterministic-versus-semantic evidence boundaries are clear enough for implementation/design selection;
7. direct, multi-hop, dynamic-plugin, artifact-mediated, and environment-mediated cases do not expose a foundational contradiction.

B does **not** require every ecosystem inspection technique, package manager, configuration grammar, final logical-expression schema, final negative-evidence proof system, or graph traversal implementation.

### Conversation C — Best next investigation/check

**Question:** When material uncertainty remains, what additional evidence/check is worth acquiring, executing, or recommending?

C can close when UpgradePilot has a bounded general method for identifying a decision-relevant unresolved question, selecting/recommending a discriminating investigation, and recognizing when no supported additional check is worth doing.

### Conversation D — Sufficiency, stopping, and maintainer-facing result

**Question:** When does UpgradePilot know enough to stop, and what exactly should it tell the maintainer?

D can close when evidence sufficiency, unresolved/conflicting state, stopping, repository-policy interaction, and maintainer-facing synthesis are coherent enough to revise the outward product contract and choose implementation responsibilities.

### Implementation handoff check

After every conversation ask:

> Has further conceptual discussion become lower-value than implementing or evaluating what we already understand?

Current judgment still favors continuing B because the evidence boundary needed for legitimate negative/refutation claims is foundational to any correct decision contract. No runtime representation is yet justified merely from the semantics accepted so far.

---

## 12. Cross-cutting questions to preserve

1. **Product value** — what does UpgradePilot add beyond competent manual browsing?
2. **Scale/repeatability** — which benefits emerge from consistent repeated execution?
3. **Authority** — what is authoritative, attributed, grounded, corroborated, contradictory, or unresolved?
4. **Negative evidence** — what can absence/non-observation establish, and within what boundary?
5. **Repository policy** — which conclusion depends on repository-specific norms rather than engineering fact?
6. **Identity/freshness/decision time** — which exact object/world-state does a claim describe?
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
19. **Path completeness** — before negative closure, have all viable applicability alternatives actually been eliminated?
20. **Evidence discrimination** — does the evidence answer the proposition or merely correlate with it?

---

## 13. Deliberately deferred questions

Do not solve these merely to make the model look complete:

- final runtime applicability-state vocabulary/enum/schema;
- universal Boolean/logical-expression representation;
- arbitrary/general LLM semantics for all upstream changes;
- exact Targeted Check Planner ranking or Value-of-Information method;
- repository-policy schema;
- exact freshness/recheck/rerun durations and triggers;
- whether changed PR head restarts, supersedes, or preserves both analyses;
- whether identity/freshness deserves a dedicated subsystem;
- final whole-product sufficiency formula;
- final maintainer-facing action vocabulary;
- whether historical five action classes survive unchanged;
- complete technical-impact/exposure taxonomy;
- graph data structure/database choices;
- exact multi-hop graph traversal/stopping implementation;
- exhaustive negative-evidence proof methods across ecosystems;
- implementation sequence and ADR changes.

---

## 14. Final repository-change register

**Status:** Pending reconciliation.

When enough of A–D is settled, reassess exactly what must be retained, amended, superseded, archived, or newly created. Candidate controlling files to reassess later include:

- `PROJECT_CHARTER.md`
- `README.md`
- `plans/UPGRADEPILOT_90_DAY_PLAN.md`
- `plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md`
- applicable files under `docs/specifications/`
- possibly a new ADR if a consequential decision architecture/method is accepted
- `MEMORY.md` for final live continuation
- source/tests only after an implementation responsibility is selected.

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

---

## 15. Exact current continuation

Continue with **Conversation B — Applicability and investigation activation**.

The proposition-based applicability method, necessary/alternative-path semantics, and high-level evidence-quality criteria are now accepted. Do **not** reopen Conversation A and do **not** implement enums/classes/rules/schema yet.

### Next smallest foundational question

> **When can UpgradePilot legitimately treat non-observation or absence as evidence that an applicability proposition is false, rather than merely unresolved?**

This is the practical **open-world versus closed-world / evidence-boundary** problem.

Use these anchors:

### Anchor 1 — S001: authoritative bounded exclusion

```text
proposition:
Pydantic admits Python 3.8

evidence:
exact-head requires-python >=3.10

→ the authoritative declaration directly excludes Python 3.8
→ proposition refuted
```

Questions:

- What makes this evidence boundary sufficiently closed for the proposition?
- Which part is explicit declaration versus deterministic inference?

### Anchor 2 — Buildtest: open environment uncertainty

```text
proposition:
historical target environment uses an affected OpenSSL version

evidence:
external HPC environment known
exact SSL implementation/version unknown

→ unresolved
```

Questions:

- What evidence would turn this into established true or false?
- When is environment inventory sufficiently complete?

### Anchor 3 — Kedro/Pluggy: external/dynamic population

```text
proposition:
no affected plugin/wrapper path exists
```

Questions:

- Why is target-source grep insufficient?
- Would a complete installed-entry-point inventory at the exact environment/revision create an adequate closed boundary?
- What still must be known about registration and lifecycle reachability?

### Anchor 4 — pip-audit multi-hop path

```text
proposition:
no target-relevant path reaches the incompatible CacheControl/urllib3 interaction
```

Questions:

- What graph/dependency evidence would be complete enough to support such a negative claim?
- When should inability to establish a path stay unresolved instead of becoming no-path evidence?

### Immediate B learning/design tasks

Determine only what the next correct design step requires:

1. practical meaning of **open-world** versus **closed-world** reasoning in UpgradePilot;
2. when explicit authoritative exclusion is sufficient negative evidence;
3. when a complete inventory/search can legitimately support absence;
4. when search non-observation must remain unresolved;
5. how deterministic inference can transform authoritative evidence without overclaiming;
6. where bounded semantic interpretation may assist evidence understanding without giving an LLM authority to manufacture absence/refutation;
7. whether, after this boundary is stable, implementation/evaluation becomes more valuable than further B theory.

Do not design a universal negative-evidence engine or enumerate every ecosystem-specific inspection technique. Apply the decision-need test from Section 2.