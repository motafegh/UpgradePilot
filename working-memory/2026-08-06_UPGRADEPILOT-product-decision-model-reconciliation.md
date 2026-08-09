# UpgradePilot Product Decision-Model Reconciliation Working Record

**Date opened:** 2026-08-06  
**Last discussion sync:** 2026-08-09  
**Status:** Active design discussion; Conversation A closed; Conversation B active; applicability, evidence-boundary, and deterministic-versus-semantic responsibility semantics accepted; semantic-heavy pressure test and B closure review next  
**Purpose:** Preserve the current whole-product decision-model position, important rationale, accepted decisions, active hypotheses, open questions, stop lines, and eventual repository-change implications without becoming an append-only transcript.  
**Live-state owner:** `../MEMORY.md` remains the sole owner of current project position and exact implementation continuation.  
**Pre-consolidation snapshot:** commit `e158fe041597ecb6176f4d5dab6b11961f30c8e1` preserves an earlier chronological/repetitive form of this record in Git history.

---

## 1. Why this reconciliation exists

UpgradePilot completed the bounded Target-Python Support Relevance responsibility through the normal live path. That implementation now has materially stronger evidence identity, provenance, grounding, target relevance, and explicit failure/unresolved behavior than when the earlier transparent-decision documents and product-simulation conclusions were written.

The next active implementation plan points toward a Transparent Decision Method, but implementing the old decision framing immediately could encode stale or underspecified concepts, especially:

- a too-direct `evidence → action` mapping;
- historical simulation actions treated too much like machine truth;
- insufficient separation between upstream change, target impact, applicability, evidence, and final action;
- undefined repository-specific semantics around labels such as `merge after normal review`;
- missing first-class treatment of investigation selection and stopping;
- unclear policy, trust, identity/freshness, and human-authority boundaries.

Implementation of the decision/recommendation layer therefore remains intentionally paused while the **minimum necessary** whole-product semantics are reconciled.

This is not authorization for open-ended architecture work. The rule remains:

```text
real evidence
→ identify foundational ambiguity
→ resolve only necessary semantics
→ implement / evaluate
→ learn from behavior
→ refine
```

Do not force discussion results into enums, schemas, class hierarchies, Boolean-expression engines, graph implementations, or frameworks before the domain relationship earns that representation.

---

## 2. Authority and evidence discipline

Active/normative material includes the charter, README, 90-day plan, Transparent Decision Method plan, `MEMORY.md`, applicable specifications, and `AGENTS.md`.

Historical/discovery/challenge evidence includes prior product simulations, earlier B2 working records, S006, Challenge Screening Pass 02 and its handoff on `agent/product-simulation-case-screening-01`, and the non-controlling product-ambition proposal.

Historical simulations, proposals, old drafts, and parallel challenge artifacts are **design/challenge evidence**, not automatic authority. Source/tests remain the authority for implemented behavior.

Stable principles:

```text
observation
!= interpretation
!= evidence quality
!= decision
```

and, where relevant:

```text
source/raw evidence
→ parsed/normalized evidence
→ attributed claim or deterministic interpretation
→ grounding/corroboration/conflict state
→ finding or decision input
→ bounded output
```

Also preserve:

- exact proposal, dependency, version, source, revision, context, and relevant observation-time identity;
- source authority/provenance separately from semantic meaning;
- missing, inaccessible, stale, conflicting, invalid, unsupported, not-applicable, and unresolved where materially different;
- model/LLM output cannot assign its own authority or final decision effect;
- absence of a model-derived claim is not evidence that no relevant risk exists;
- repository policy and residual-risk acceptance remain human/repository responsibilities unless explicitly represented by trustworthy policy evidence;
- investigation should stop when more supported work cannot materially change uncertainty location, required checks, action constraints, or another decision-relevant result.

---

## 3. Current whole-product discussion model

```text
public dependency-update PR
↓
exact proposal + dependency/version + base/head identity
↓
authoritative upstream changes relevant to that exact transition
↓
zero or more mechanism-specific technical impact candidates
    ├── upstream change mechanism
    ├── target-relevant exposure relationship/path
    ├── activation condition(s)
    └── possible target-relevant consequence
↓
for each candidate:
derive candidate-specific target/revision/context applicability propositions
↓
evaluate propositions against scoped evidence
    ├── established
    ├── refuted
    ├── unresolved
    └── genuinely conflicted
↓
combine only as required by the candidate's logical structure
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

This is a **discussion/domain model**, not an approved runtime pipeline or schema.

A central emerging product insight remains that UpgradePilot may be better understood as an **evidence-driven impact and investigation system** than as a primary five-label classifier. Historical action families may survive as a later projection; that remains undecided.

---

## 4. Conversation A — accepted technical-impact model

**Status:** **CLOSED 2026-08-08.**

### 4.1 Impact candidate

> **A technical impact candidate is a target-relevant proposition that the proposed dependency transition could cause or enable a technical consequence through a technical relationship with the target under relevant activation conditions.**

```text
UPSTREAM CHANGE
+
TARGET-RELEVANT EXPOSURE/PATH
+
ACTIVATION CONDITION(S)
+
POSSIBLE TARGET CONSEQUENCE
=
IMPACT CANDIDATE
```

`Impact candidate` is the whole proposition, not an event inserted between change and exposure.

### 4.2 Boundaries accepted in A

```text
upstream change != target impact
```

```text
target relevance != target ownership of affected code
```

Exposure is a target-relevant relationship/pathway, which may be direct, multi-hop, framework-mediated, plugin-mediated, artifact-mediated, environment-mediated, or dependency-owned.

Exposure and activation are conceptually distinct but can be evidenced by overlapping facts; this does not imply separate scanners/classes.

```text
one version transition != one impact candidate
```

A transition may contain multiple mechanism-specific candidates, each evaluated independently.

Materiality is decision-relative:

```text
severity != materiality
likelihood != materiality
interesting != material
material != harmful
```

Candidate exposure roots and graph-like representation remain hypotheses, not runtime commitments.

---

## 5. Conversation B — accepted applicability model

**Status:** **ACTIVE.**

### 5.1 Applicability is proposition-based

Applicability is evaluated for **one mechanism-specific impact candidate** against **one exact target/revision/context**.

The system evaluates explicit propositions that evidence can establish, refute, leave unresolved, or place in genuine conflict.

```text
REAL-WORLD QUESTION
Does this candidate apply?

        ↓

UPGRADEPILOT KNOWLEDGE/JUSTIFICATION STATE
What is the system justified in claiming from supported evidence?
```

Knowledge-state semantics:

```text
ESTABLISHED APPLICABLE
At least one complete viable applicability path is sufficiently established.

ESTABLISHED NOT APPLICABLE
Every viable applicability path is sufficiently eliminated.

UNRESOLVED
A material proposition needed to decide applicability cannot currently be
established or refuted within the supported evidence boundary.

CONFLICTED
Credible evidence about the same properly scoped proposition remains
incompatible after identity/revision/context/scope/time normalization.
```

Hard protections:

```text
applicable != consequence proven
not applicable != evidence missing
unresolved != negative evidence
dependency/framework presence != activation established
target relevance != target ownership
different revisions/times/scopes != automatically conflicted
```

### 5.2 Necessary and sufficient propositions

A necessary proposition is one whose truth is required for a candidate path to remain viable.

For:

```text
A AND B AND C
```

refuting any one closes that path.

For:

```text
A AND (B OR C)
```

refuting `B` alone does not close the candidate while `C` remains viable.

Therefore:

> **Candidate-level non-applicability requires elimination of every viable applicability path, either by refuting a proposition necessary across all remaining paths or by separately closing all alternatives.**

Positive applicability requires sufficient evidence for at least one complete viable path; it does not require proving every alternative.

Candidate structure determines which propositions are necessary and how they compose. There is no universal dependency/framework checklist.

This is accepted **semantically** only. No Boolean AST, rule language, planner schema, or generalized expression engine is authorized yet.

### 5.3 Evidence-sufficiency criteria

Evidence for a proposition is judged at least by:

1. **scope** — same proposal/revision/context/proposition and relevant time boundary;
2. **authority** — justified source for this proposition;
3. **discriminating power** — actually distinguishes true from false for this proposition;
4. **completeness/observation boundary** when a negative claim depends on absence.

Relevant evidence is not automatically sufficient evidence.

Examples:

```text
CI ran on Linux
```

does not answer:

```text
Was OpenSSL <1.1.1?
```

and:

```text
Kedro imports Pluggy
```

does not prove an affected wrapper is installed, registered, and exercised.

### 5.4 Absence of evidence versus evidence of absence

```text
ABSENCE OF EVIDENCE
!=
EVIDENCE OF ABSENCE
```

S001 is the canonical bounded refutation:

```text
proposition:
Pydantic admits Python 3.8

authoritative exact-head evidence:
requires-python >=3.10

→ deterministic membership evaluation excludes Python 3.8
→ proposition refuted
→ candidate not applicable
```

Buildtest is the canonical unresolved case:

```text
OpenSSL/native-environment pathway established
+ upstream constraint established
+ exact historical SSL implementation/version unknown
→ activation proposition unresolved
```

A target-source grep cannot establish absence of externally installed Kedro plugins. Failure to locate a multi-hop path in an incomplete dependency view cannot establish that no path exists.

---

## 6. Conversation B — accepted evidence-boundary / open-world decisions

The open-world versus closed-world boundary is now stable enough for the next design step.

### 6.1 Open-world reasoning is the safe default

When UpgradePilot has not justified completeness of the relevant evidence universe, non-observation remains **unknown/unresolved**, not false.

```text
not observed
→ unresolved
```

unless a proposition-specific boundary justifies:

```text
not present in complete relevant set
→ refuted / absent within that set
```

### 6.2 Closed-world reasoning is local and proposition-specific

Do not classify an entire repository, source type, or environment as globally “closed.” A boundary is sufficiently closed only for a particular proposition and scope.

`requires-python >=3.10` can close the question of Python-3.8 membership in the declared target range while saying essentially nothing about an OpenSSL-version proposition.

### 6.3 Negative evidence has three currently accepted forms

Without claiming exhaustiveness:

1. **explicit authoritative exclusion**;
2. **complete bounded inventory**;
3. **deterministic derivation from authoritative facts**.

The exact proof methods remain ecosystem-specific and deferred.

### 6.4 Search failure alone is not negative evidence

A complete repository/source search may support a bounded claim such as:

```text
no direct call to X exists in all tracked parsed source files at revision R
```

if the search is complete for that proposition.

It does not automatically establish:

```text
target behavior can never reach X
```

because dynamic import, reflection, configuration, framework callbacks, plugins, generated code, dependency-owned interactions, or runtime/environment state may bypass the inspected source boundary.

### 6.5 Bound claims to the observed universe of discourse

**Universe of discourse** means the bounded set of objects/states a proposition talks about.

Prefer:

```text
No affected plugin was present in exact evaluated environment E,
based on complete installed-entry-point inventory.
```

over:

```text
No affected plugin exists.
```

Prefer:

```text
No affected path exists in exact resolved graph G for environment E/extras X.
```

over:

```text
No incompatible dependency path exists.
```

Sometimes narrowing the proposition to a universe UpgradePilot can actually evaluate is more correct than seeking an unjustified global conclusion.

### 6.6 Completeness must itself be justified

Before absence can refute a proposition, UpgradePilot must justify why the observation covers the relevant universe.

Potentially adequate scoped boundaries include authoritative declarations defining an allowed set/range, complete resolved dependency graphs, complete installed package/entry-point inventories for frozen environments, complete tracked-source AST inventories for source-limited propositions, and exact/reproducible environment metadata.

### 6.7 Deterministic inference may derive bounded negative facts

```text
trusted authoritative fact
+
deterministic transformation/evaluation
→ justified derived fact
```

The transformation must preserve the source's scope and meaning rather than broaden it.

### 6.8 An LLM cannot manufacture closed-world completeness or absence

A model may assist with bounded semantic interpretation, but completeness/absence/refutation must be justified by authoritative and/or deterministic evidence boundaries.

Completeness is a property of evidence coverage and scope, not semantic confidence.

---

## 7. Conversation B — accepted deterministic/semantic responsibility boundary

The latest discussion resolves the responsibility split enough to justify one final semantic-heavy pressure test before a B closure review.

### 7.1 Source authority and identity precede semantic interpretation

Before interpreting what evidence means, UpgradePilot must establish what the evidence is and what exact object it describes where that can be determined independently.

```text
source identity / provenance / proposal binding
        ↓
semantic interpretation
```

not:

```text
LLM recognizes something plausible
→ therefore source is authoritative
```

**Why:** perfect interpretation of the wrong source/revision/dependency is still wrong. Semantic confidence cannot repair identity or provenance failure.

### 7.2 Semantic interpretation produces attributed claims, not self-authorizing verdicts

LLMs may be used where meaning is difficult to recover mechanically, for example:

- interpreting natural-language release notes;
- proposing upstream change mechanisms;
- identifying target relationships that may be framework/plugin/contract mediated;
- helping formulate candidate-specific applicability propositions;
- interpreting source behavior where no practical simple deterministic procedure exists.

But the semantic output should remain conceptually:

```text
exact evidence
→ bounded semantic interpretation
→ attributed claim/proposition
```

not:

```text
LLM says applicable
→ applicability truth
```

**Why:** interpretation is one layer of evidence reasoning; it does not assign its own authority, coverage completeness, or final decision effect.

### 7.3 Prefer deterministic decision procedures where they are reliable

A **decision procedure** is a defined method that answers a bounded question according to explicit rules.

Where a proposition admits a reliable deterministic procedure, that procedure should normally own the evaluation instead of an LLM.

Examples include:

- version/specifier membership;
- exact SHA/revision identity;
- exact changed-file membership;
- exact-source-span reconstruction;
- resolved dependency-edge membership;
- package/repository provenance agreement when explicit evidence supports it;
- exact inventory membership;
- configuration equality/intersection/set membership.

**Why:** deterministic logic is repeatable, inspectable, testable, and traceable. Using semantic inference where a strong mechanical procedure exists adds unnecessary uncertainty.

### 7.4 Deterministic transformation is not the same as source authority

Preserve:

```text
deterministic transformation != authoritative evidence
```

and:

```text
authoritative evidence != necessarily deterministic interpretation
```

A parser can deterministically extract a claim from an untrustworthy source, while authoritative prose may still require semantic interpretation.

**Why:** authority/provenance and semantic/technical interpretation are separate evidence dimensions and must not be collapsed.

### 7.5 Semantic proposition evaluation is allowed when deterministic evaluation is not practical

Some propositions may be inherently or economically semantic, for example:

```text
Does this target/plugin rely on the Pluggy wrapper behavior changed by the transition?
```

There may be no cheap general deterministic rule that answers this correctly across arbitrary code/framework behavior.

Bounded semantic evaluation may therefore contribute to proposition evaluation, but it must remain:

- tied to exact evidence;
- attributed as interpretation rather than raw fact;
- grounded/reconstructable where practical;
- uncertainty-preserving;
- incapable of self-assigning source authority or evidence completeness;
- incapable of converting unsupported ambiguity into established/refuted merely through confidence.

**Why:** forbidding semantic reasoning entirely would make UpgradePilot too weak for real software semantics, while allowing unconstrained model verdicts would destroy evidence discipline.

### 7.6 Evidence-boundary completeness is not a semantic-model responsibility

Whether the observed universe is complete enough for a claim belongs to evidence acquisition/provenance/coverage reasoning, not model intuition.

Example:

```text
LLM found no affected Kedro wrapper in target source
```

cannot establish absence if external installed entry-point plugins were outside the observed universe.

**Why:** completeness describes what was observed and what was omitted; it is not a meaning judgment that semantic confidence can supply.

### 7.7 Proposition knowledge state should be assigned by a bounded evaluator over admitted evidence

Conceptually:

```text
admitted authoritative observations
+ deterministic derived facts
+ grounded semantic claims where needed
+ conflict normalization
+ evidence-boundary state
        ↓
BOUNDED PROPOSITION EVALUATION
        ↓
established / refuted / unresolved / conflicted
```

The final proposition state must not reduce to:

```text
LLM.generate("is this proposition true?")
```

Unsupported or insufficiently grounded model output remains non-authoritative and cannot by itself upgrade a proposition from unresolved.

**Why:** the product must preserve why the state is justified: exact evidence, authority, coverage, deterministic facts, semantic interpretation, and unresolved/conflict boundaries.

This is a domain/responsibility decision, not authorization for a new `PropositionEvaluator` class or framework yet.

### 7.8 Candidate applicability composition should be deterministic once proposition logic is explicit

When the candidate's applicability structure and proposition states are known, composition should normally be mechanical.

For example:

```text
A AND (B OR C)

A = established
B = refuted
C = established
→ candidate established applicable through A+C
```

or:

```text
A = established
B = refuted
C = unresolved
→ candidate unresolved
```

**Why:** once semantic ambiguity has been reduced to explicit proposition states and candidate structure, asking an LLM to improvise logical composition would add uncertainty without product value.

No runtime Boolean engine is authorized by this decision; only the responsibility boundary is accepted.

### 7.9 Proposition formulation is itself a high-impact semantic responsibility

Deriving propositions such as:

```text
affected version selected
relevant plugin installed
entry point registered
lifecycle event reached
changed wrapper semantic relied upon
```

can require understanding the upstream mechanism and target/framework behavior.

Therefore LLM/semantic assistance may help propose the proposition structure, but the propositions must remain explicit, candidate-specific, grounded, and reviewable.

**Why:** omitting a genuinely necessary proposition can create false applicability; inventing an unnecessary proposition can create false non-applicability or needless investigation. Proposition formulation is too consequential to remain hidden inside an opaque model verdict.

### 7.10 Prefer a deterministic shell around bounded semantic reasoning

Current architectural direction, without runtime commitment:

```text
deterministic evidence acquisition / identity / scope
        ↓
bounded semantic interpretation where needed
        ↓
grounding / reconstruction / deterministic validation where possible
        ↓
bounded proposition evaluation
        ↓
deterministic candidate composition where structure is explicit
```

This is a design principle rather than a claim that every semantic statement must have a deterministic oracle.

If no adequate validation exists, preserve uncertainty rather than invent deterministic certainty.

### 7.11 Applicability authority stops before maintainer action

Even a fully established candidate applicability state does not own:

- final upgrade safety;
- repository-policy compliance;
- residual-risk acceptance;
- `merge`, `defer`, or other maintainer action.

Those belong to later synthesis, repository policy, and human authority.

```text
applicability evaluation
!=
maintainer decision
```

---

## 8. Case anchors retained for B

### S001 — Soup Sieve / Pydantic

```text
Soup Sieve drops Python 3.8
+ exact-head Pydantic requires-python >=3.10
→ necessary proposition refuted
→ bounded candidate not applicable
```

Use for authoritative upstream evidence, bounded semantic candidate extraction, exact-source reconstruction, deterministic validation, and deterministic target-range applicability.

### Buildtest / urllib3 environment

```text
OpenSSL pathway exists
+ upstream constraint exists
+ exact historical SSL implementation unknown
→ unresolved
```

Use for the rule that semantic plausibility cannot replace missing authoritative environment evidence.

### Kedro / Pluggy

```text
Kedro
→ Pluggy entry-point discovery/registration
→ lifecycle dispatch
→ external plugin-owned code
```

Use for candidate-specific compositional activation and for testing propositions whose meaning may require semantic interpretation. Target source alone cannot close the plugin universe.

### pip-audit / CacheControl / Requests / urllib3

```text
pip-audit
→ CacheControl
→ Requests / urllib3
→ CacheControl assumption on urllib3.HTTPResponse.strict
```

Use for multi-hop target relevance, graph completeness, and the split between deterministic dependency relationships and semantic interpretation of changed contracts.

### Build/codegen comparator

```text
grpcio-tools
→ generation execution
→ generated artifact
→ later runtime consumption
```

Use for temporally staged/artifact-mediated applicability.

---

## 9. Decisions and provisional conclusions

Numbering remains stable for Git-history traceability.

### D-001 — Use one reconciliation record
**Accepted 2026-08-06.** Preserve this whole-product reconciliation in one working-memory file before modifying controlling artifacts or implementing the next decision layer.

### D-002 — Stage boundaries do not constrain whole-product reasoning
**Accepted 2026-08-06.** B2/B3/B4 may later control implementation sequence, not what the correct whole-product model may contain.

### D-003 — Old artifacts are evidence, not automatic authority
**Accepted 2026-08-06.** Historical simulations, drafts, proposals, and challenge-screening artifacts are evaluated against current implementation/product goals rather than inherited as machine truth.

### D-004 — Upstream change is not itself target impact
**Provisional design conclusion.** A target-relevant relationship/path must be established.

### D-005 — Preserve impact candidate versus target applicability
**Provisional design conclusion.** A credible possible impact is not target-applicable until candidate-specific target propositions are sufficiently established. Non-applicability closes only that bounded candidate/path.

### D-006 — Activation condition is central
**Provisional design conclusion.** Activation is the condition that must hold in the exact target/context for a candidate to matter.

### D-007 — Dependency impact and unrelated repository condition remain distinguishable
**Provisional design conclusion.** Failing CI or another repository condition does not become dependency impact without causal evidence.

### D-008 — Materiality is decision-relative
**Provisional design conclusion.** Severity, likelihood, interestingness, harm, and materiality are distinct.

### D-009 — Control variation through domain abstractions, not case rules
**Provisional design conclusion.** Normalize recurring relationships/predicates rather than multiplying fixture-specific rules.

### D-010 — Do not freeze a flat impact enum
**Provisional design conclusion.** API/security/platform/performance/CI/build mixes mechanisms, exposure, consequence, and evidence.

### D-011 — CI/tests/source/config/metadata are not automatically impacts
**Provisional design conclusion.** Their semantic role is proposition-relative.

### D-012 — Exposure is a target-relevant relationship/pathway
**Provisional design conclusion.** Exposure is not merely repository location and does not require target ownership.

### D-013 — Role is contextual
**Provisional design conclusion.** The same subsystem/artifact may be exposure in one proposition and evidence in another.

### D-014 — Technical target impact is not all decision-relevant information
**Provisional design conclusion.** Trust/authority, identity/freshness, policy/governance/licensing and similar concerns may affect claims/actions without themselves being technical target impacts.

### D-015 — Proposal identity controls the assessed object; mutable evidence is time-bounded observation
**Provisional design conclusion.** Later releases do not silently replace the proposal. Correctly scoped observations remain historically valid even when the world later changes.

### D-016 — Reconciliation is bounded by decision need
**Accepted process decision 2026-08-07.** Resolve questions now only when failing to do so risks the next correct product/architecture/evidence-contract/implementation decision.

### D-017 — Impact candidate is the complete technical proposition
**Accepted domain decision 2026-08-08.** Upstream change + exposure/path + activation condition(s) + possible consequence form the candidate. No runtime class/enum/schema is implied.

### D-018 — Conversation A is sufficiently closed
**Accepted process/design decision 2026-08-08.** No remaining A ambiguity was found capable of making B fundamentally wrong.

### D-019 — Challenge Pass 02 is B pressure-test evidence; A remains closed
**Accepted process/design decision 2026-08-09.** The parallel challenge artifacts strengthen rather than contradict A.

### D-020 — Applicability is per mechanism-specific candidate
**Accepted domain decision 2026-08-09.** One transition may yield zero/one/multiple candidates; applicability is evaluated independently per candidate.

### D-021 — Target relevance does not require target ownership; presence does not establish activation
**Accepted domain decision 2026-08-09.** Material interaction may occur in dependencies/frameworks/plugins/artifacts/environments. Dependency presence alone is insufficient.

### D-022 — Applicability knowledge-state semantics
**Accepted domain decision 2026-08-09.** Preserve `established applicable`, `established not applicable`, `unresolved`, and `conflicted` as conceptual justification states. No runtime enum/schema yet.

### D-023 — Exposure and activation are conceptually distinct without mandatory separate evidence machinery
**Accepted domain/process decision 2026-08-09.** One fact may help establish both; do not prematurely split scanners/classes/channels.

### D-024 — Applicability is proposition-based
**Accepted domain decision 2026-08-09.** Evaluate explicit target/revision/context propositions rather than vague labels.

**Why:** evidence can establish/refute propositions; traceability is lost when an abstract applicability label hides the statements it depends on.

### D-025 — Candidate structure determines necessary propositions and composition
**Accepted domain decision 2026-08-09.** Necessary propositions and conjunction/alternative structure derive from the candidate, not a universal checklist.

**Why:** simple S001 and dynamic Kedro/Pluggy require different structures. No Boolean engine is authorized yet.

### D-026 — Positive applicability requires one sufficiently established complete viable path
**Accepted domain decision 2026-08-09.** For `A AND (B OR C)`, `A+B` may be enough even if `C` is unknown.

**Why:** proving every alternative wastes investigation and violates conditional stopping.

### D-027 — Non-applicability requires elimination of every viable path
**Accepted domain decision 2026-08-09.** Refuting one branch is insufficient while another viable branch remains.

**Why:** prevents premature negative closure under compositional activation.

### D-028 — Missing evidence is unresolved; negative evidence requires genuine refutation within an adequate observation boundary
**Accepted domain decision 2026-08-09.** Failure to observe does not by itself refute. Absence claims require sufficient coverage.

**Why:** S001 explicitly excludes Python 3.8; Buildtest lacks exact SSL evidence; source grep cannot exclude external plugins.

### D-029 — Evidence sufficiency is proposition-relative
**Accepted reasoning decision 2026-08-09.** Judge scope, authority, discriminating power, and completeness where negative claims depend on absence.

**Why:** evidence that is relevant but non-discriminating cannot justify the proposition.

### D-030 — Conflict is proposition-scoped after identity/scope/time normalization
**Accepted domain decision 2026-08-09.** Only genuinely incompatible credible evidence about the same normalized proposition is conflict.

### D-031 — Open-world reasoning is the safe default
**Accepted domain/evidence decision 2026-08-09.** When completeness of the relevant evidence universe is not justified, non-observation remains unresolved rather than false.

**Why:** software relevance can escape a local source boundary through dependencies, dynamic plugins, generated artifacts, runtime environments, configuration, reflection, and multi-hop interactions.

### D-032 — Closed-world reasoning is local to a scoped proposition
**Accepted domain/evidence decision 2026-08-09.** A source or inventory is “closed enough” only relative to a defined proposition/universe; repositories and environments are not globally closed-world objects.

**Why:** `requires-python >=3.10` can close Python-3.8 membership while providing no closure for an OpenSSL-version proposition.

### D-033 — Negative evidence may use authoritative exclusion, complete bounded inventory, or deterministic derivation
**Accepted reasoning decision 2026-08-09.** These are currently recognized strong patterns, not an exhaustive taxonomy.

**Why:** they provide a defensible bridge from observed evidence to bounded falsehood/absence without treating search failure as truth.

### D-034 — Claims must not exceed the justified universe of discourse
**Accepted domain/evidence decision 2026-08-09.** Negative claims should be bounded to the exact population/environment/graph/source set whose completeness is justified.

**Why:** `no affected plugin in exact environment E` can be defensible where `no affected plugin exists` is not.

### D-035 — Completeness is itself an evidence claim
**Accepted reasoning decision 2026-08-09.** Before absence can refute a proposition, UpgradePilot must justify why its inventory/search/declaration covers the relevant universe.

**Why:** exhaustive tracked-source analysis can close a tracked-source proposition but not automatically runtime reachability; partial dependency/environment views cannot prove global absence.

### D-036 — LLM semantic interpretation cannot manufacture completeness, absence, or refutation
**Accepted model-authority decision 2026-08-09.** An LLM may help interpret bounded semantic evidence or propose candidate propositions, but completeness and negative closure must be justified through authoritative/deterministic evidence boundaries.

**Why:** closed-world completeness is a property of evidence coverage and scope, not semantic confidence.

### D-037 — Source identity and authority are independent prerequisites to semantic interpretation
**Accepted evidence-authority decision 2026-08-09.** Where identity/provenance can be established independently, semantic interpretation consumes that bound evidence rather than establishing its own authority.

**Why:** semantic correctness cannot repair analysis of the wrong source, revision, package, or proposal.

### D-038 — LLM semantic output is an attributed claim/proposition, not a self-authorizing applicability verdict
**Accepted model-role decision 2026-08-09.** LLMs may interpret natural-language or code semantics and help formulate candidate propositions, but the output remains derived interpretation tied to exact evidence.

**Why:** this preserves `observation != interpretation != evidence quality != decision` and keeps model confidence separate from authority.

### D-039 — Prefer deterministic decision procedures for propositions that admit them
**Accepted evaluation decision 2026-08-09.** Reliable mechanical procedures should own bounded questions such as version membership, exact identity, inventory membership, resolved dependency edges, and exact configuration/set relationships.

**Why:** these procedures are repeatable, testable, inspectable, and avoid unnecessary semantic uncertainty.

### D-040 — Deterministic transformation and evidence authority remain separate dimensions
**Accepted evidence decision 2026-08-09.** Deterministically deriving a fact does not make the source authoritative; authoritative evidence may still require semantic interpretation.

**Why:** provenance and interpretation solve different problems and neither substitutes for the other.

### D-041 — Bounded semantic proposition evaluation is allowed where deterministic evaluation is not practical
**Accepted model/evaluation decision 2026-08-09.** Some software-semantic propositions may require model-assisted interpretation, but such evaluation must remain exact-evidence-bound, attributed, grounded/reconstructable where practical, and uncertainty-preserving.

**Why:** forbidding semantic reasoning entirely would miss real framework/contract behavior; unconstrained model verdicts would destroy evidence discipline.

### D-042 — Evidence-boundary completeness is owned by evidence/coverage reasoning, not model intuition
**Accepted model-authority decision 2026-08-09.** A model may interpret observed evidence but cannot declare that the relevant universe was completely observed.

**Why:** completeness is about coverage/scope and omitted possibilities, not semantic meaning.

### D-043 — Proposition knowledge state should be assigned by bounded evaluation over admitted evidence
**Accepted evaluation-responsibility decision 2026-08-09.** The conceptual proposition evaluator combines admitted authoritative observations, deterministic derived facts, grounded semantic claims where needed, normalized conflict, and evidence-boundary state to justify `established`, `refuted`, `unresolved`, or `conflicted`.

**Why:** the final state must preserve why it is justified rather than reduce to `LLM says true/false`. This is a responsibility boundary, not authorization for a runtime evaluator class.

### D-044 — Candidate applicability composition should be deterministic once proposition logic is explicit
**Accepted domain/evaluation decision 2026-08-09.** Once candidate structure and proposition states are explicit, candidate applicability should be mechanically composed rather than re-decided semantically.

**Why:** deterministic composition adds traceability and avoids unnecessary uncertainty after semantic ambiguity has already been isolated into propositions.

### D-045 — Proposition formulation is a high-impact semantic responsibility and must remain explicit/grounded
**Accepted model/design decision 2026-08-09.** Semantic assistance may propose candidate-specific necessary propositions and paths, but they must be explicit, grounded, traceable, and reviewable.

**Why:** omitting a necessary proposition can create false applicability; inventing an unnecessary one can create false non-applicability or needless investigation.

### D-046 — Prefer a deterministic shell around bounded semantic reasoning
**Accepted design principle 2026-08-09.** Current direction is deterministic evidence acquisition/identity/scope around bounded semantic interpretation, followed by grounding/validation and deterministic downstream composition where possible.

**Why:** this uses LLMs where meaning is genuinely difficult while keeping authority, coverage, mechanical inference, and composition inspectable. It does not require every semantic claim to have a deterministic oracle.

### D-047 — Applicability authority stops before maintainer action
**Accepted authority-boundary decision 2026-08-09.** Applicability evaluation does not own final upgrade safety, policy compliance, residual-risk acceptance, or merge/defer action.

**Why:** those depend on broader decision context, repository policy, and human authority that Conversation B intentionally does not collapse into technical applicability.

---

## 10. Active hypotheses — not final architecture

- **H1:** impact/investigation may be more central than five-class recommendation.
- **H2:** historical action classes may survive as a later maintainer-facing projection.
- **H3:** `normal review` may not be UpgradePilot-owned without repository policy.
- **H4:** targeted investigation is likely a core value proposition.
- **H5:** simulations/challenge cases remain evidence, not labels.
- **H6:** current Python-support implementation is one proven slice, not a universal template.
- **H7:** flat impact taxonomy is probably wrong.
- **H8:** exposure may compress into a small number of reusable coupling/contract roots.
- **H9:** exposure can be multi-hop/graph-shaped without implying graph implementation.
- **H10:** technical exposure is one subset of a larger decision model that also needs trust/identity/policy context.
- **H11:** identity/freshness should not inflate into continuous monitoring.
- **H12:** use just-enough design and implementation feedback.
- **H13:** multi-hop traversal needs a decision-relative stopping boundary, partly B/C.
- **H14:** candidate-specific activation may be compositional; exact runtime logical representation remains deferred.
- **H15:** the deterministic-shell/bounded-semantic-core principle may become a broader implementation architecture pattern, but no concrete runtime module boundary is yet accepted.

---

## 11. Rejected shortcuts

```text
upstream change = target impact
anything decision-relevant = technical impact
flat API/security/platform/performance/CI impact taxonomy
historical simulation action = machine truth
newer dependency release silently replaces exact proposal
all exposure is direct source/API use
potential impact is an intermediate event
a version transition has one aggregate impact candidate
target relevance requires target-owned affected code
dependency/framework presence = activation
missing evidence = not applicable
one failed activation branch = candidate not applicable
positive applicability requires every alternative path
relevant evidence = sufficient evidence
different revisions/times/scopes = automatically conflicted
repository/source search failure = global absence
LLM confidence = evidence-boundary completeness
LLM semantic interpretation = source authority
LLM generated proposition = established proposition
LLM direct applicability verdict = authoritative applicability state
deterministic transformation = authoritative source
deterministic procedure required for every semantic software proposition
candidate applicability should be re-decided by an LLM after proposition states are known
applicability evaluator = maintainer decision authority
reconciliation must completely model the domain before implementation
```

---

## 12. Four reconciliation conversations and stop lines

### Conversation A — Dependency-update impact/problem model

**Status:** **CLOSED 2026-08-08.**

A has a usable impact boundary, survives representative cases, separates neighboring concerns, and leaves only safely deferrable taxonomy/representation details.

### Conversation B — Applicability and investigation activation

**Status:** **ACTIVE — proposition/composition/evidence-boundary and deterministic-versus-semantic responsibility semantics accepted; one semantic-heavy pressure test and explicit closure review remain.**

B can close when:

1. applicability knowledge states are coherent;
2. candidate-specific necessary propositions/alternative paths are coherent;
3. positive and bounded negative evidence semantics are coherent;
4. open-world/closed-world evidence boundaries are coherent enough for the next design step;
5. conflict is proposition-scoped after identity/context/time normalization;
6. deterministic-versus-semantic evaluation responsibilities and model-authority boundaries are coherent;
7. one genuinely semantic-heavy proposition can be handled without collapsing back into `LLM says true/false`;
8. representative direct, multi-hop, dynamic-plugin, artifact-mediated, and environment-mediated cases reveal no foundational contradiction.

B does **not** require every ecosystem inspection technique, final logical-expression schema, exhaustive negative-evidence proof system, graph-traversal implementation, universal semantic evaluator, or final runtime module layout.

### Conversation C — Best next investigation/check

When material uncertainty remains, identify the decision-relevant unresolved question, select/recommend a discriminating investigation, and recognize when no supported additional check is worth doing.

### Conversation D — Sufficiency, stopping, and maintainer-facing result

Define when enough evidence exists to stop, how unresolved/conflicting state and repository policy interact, and what maintainer-facing synthesis is justified.

### Implementation handoff check

After every conversation ask:

> Has further conceptual discussion become lower-value than implementing or evaluating what we already understand?

Current judgment: perform one bounded semantic-heavy applicability pressure test. If the responsibility model survives it without foundational ambiguity, run the explicit Conversation-B closure review immediately rather than continuing open-ended B theory.

---

## 13. Cross-cutting questions to preserve

- product value and repeatability;
- authority/provenance/grounding/conflict;
- negative evidence and observation boundaries;
- repository-policy boundary;
- identity/freshness/decision time;
- LLM/model role and authority;
- stopping/actionability;
- generality and human authority;
- explainability and complexity control;
- concern topology and design economy;
- candidate granularity and ownership independence;
- applicability knowledge state;
- path completeness and evidence discrimination;
- claim scope/universe-of-discourse discipline;
- semantic-claim grounding and uncertainty;
- deterministic decision-procedure preference where available;
- proposition-formulation completeness/overconstraint risk.

---

## 14. Deliberately deferred questions

Do not solve merely for completeness:

- final runtime applicability enum/schema;
- universal Boolean/logical-expression representation;
- arbitrary/general LLM semantics for all upstream changes;
- exact Targeted Check Planner/Value-of-Information ranking;
- repository-policy schema;
- exact freshness/recheck/rerun triggers;
- changed-head restart/supersession semantics;
- dedicated identity/freshness subsystem;
- final whole-product sufficiency formula;
- final maintainer-facing action vocabulary;
- whether historical five action classes survive unchanged;
- complete exposure taxonomy;
- graph database/data structure choices;
- exact multi-hop traversal/stopping implementation;
- exhaustive negative-evidence proof methods across ecosystems;
- universal evidence-completeness engine;
- universal semantic proposition evaluator;
- concrete runtime `PropositionEvaluator`/rule-engine class design;
- exact deterministic-shell module boundaries;
- implementation sequence and ADR changes.

---

## 15. Final repository-change register

**Status:** Pending reconciliation.

After sufficient A–D closure, reassess only the stable owners that actually require change, potentially including:

- `PROJECT_CHARTER.md`;
- `README.md`;
- `plans/UPGRADEPILOT_90_DAY_PLAN.md`;
- `plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md`;
- applicable specifications;
- possibly an ADR for consequential accepted architecture/method;
- `MEMORY.md` for final live continuation;
- source/tests only after an implementation responsibility is selected.

Do not modify these merely because they are candidates.

---

## 16. Exact current continuation

Continue **Conversation B — Applicability and investigation activation**.

The impact model, proposition-based applicability model, candidate composition semantics, knowledge states, evidence-boundary discipline, and deterministic-versus-semantic responsibility model are now sufficiently stable for a final bounded pressure test.

Do **not** reopen Conversation A. Do **not** implement enums/classes/rule languages/evidence engines yet.

### Next smallest bounded test

Pressure-test a genuinely semantic-heavy Kedro/Pluggy proposition:

> **For the exact target/plugin/revision/context, does the relevant implementation rely on the Pluggy wrapper/result/exception behavior changed by the proposed transition?**

The purpose is not to solve every Pluggy case. The purpose is to verify that UpgradePilot can handle a proposition that may not admit a cheap deterministic decision procedure without collapsing back into an opaque model verdict.

Use this responsibility shape:

```text
exact source / plugin / revision / environment evidence
        ↓
source identity / provenance / scope binding
        ↓
bounded semantic interpretation of the changed behavior and target relationship
        ↓
explicit attributed proposition/claim
        ↓
grounding / source reconstruction / deterministic corroboration where available
        ↓
evidence-boundary and uncertainty assessment
        ↓
bounded proposition knowledge state
        ↓
deterministic candidate composition with other required propositions
```

### Questions to answer in the pressure test

1. What exact proposition are we evaluating, and is its scope narrow enough to be evidence-grounded?
2. Which evidence is authoritative observation versus semantic interpretation?
3. What can be deterministically established about plugin presence, registration, lifecycle reachability, version selection, or source structure?
4. Which remaining relationship truly requires semantic interpretation?
5. What grounding/corroboration makes that semantic claim admissible?
6. Under what evidence conditions can the proposition be `established` or `refuted`?
7. When must semantic ambiguity remain `unresolved` rather than being converted into a confident model verdict?
8. Does proposition state then compose cleanly and deterministically into candidate applicability?

### After the pressure test

Run an explicit **Conversation-B closure review** immediately.

The closure review should ask:

- Did the semantic-heavy case reveal any foundational ambiguity in applicability, evidence sufficiency, model authority, or composition?
- Are remaining issues implementation techniques/taxonomies rather than semantic blockers?
- Is further B theory now lower-value than implementation/evaluation or moving to Conversation C?

If no foundational contradiction appears, close B and perform the implementation-handoff decision instead of extending the discussion by default.