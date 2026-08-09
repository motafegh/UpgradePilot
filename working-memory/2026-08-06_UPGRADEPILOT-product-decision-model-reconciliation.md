# UpgradePilot Product Decision-Model Reconciliation Working Record

**Date opened:** 2026-08-06  
**Last discussion sync:** 2026-08-09  
**Status:** Active whole-product reconciliation; Conversation A closed; Conversation B closed after semantic-heavy pressure test; Conversation C active  
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
→ resolve necessary semantics
→ implement / evaluate when useful
→ learn from behavior
→ refine
```

Do not force discussion results into enums, schemas, class hierarchies, Boolean-expression engines, graph implementations, or frameworks before the domain relationship earns that representation.

### 1.1 Exploration breadth versus premature commitment

The anti-overdesign/decision-need discipline must **not** be interpreted as a requirement to keep discussion artificially narrow, short, or prematurely convergent.

Broad exploration is appropriate when it materially helps to:

- expose design blind spots or missing dimensions;
- compare plausible alternative models;
- test whether the emerging design survives structurally different cases;
- map possible future system responsibilities and boundaries;
- identify implementation consequences before those consequences become expensive commitments;
- understand where apparent generality is real versus merely untested.

The controlling distinction is:

```text
broad exploration
!=
premature architecture commitment
```

and:

```text
considering a possibility
!=
claiming universal coverage
!=
authorizing implementation
```

Therefore discussion may remain broad and technically deep where useful. The project should mark what is accepted, provisional, hypothetical, deferred, or unverified rather than suppressing useful exploration merely to reduce discussion length.

The decision-need rule remains a guard against pointless ceremony, fake completeness, and unnecessary implementation commitments—not against thoughtful system design.

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

**Status:** **CLOSED 2026-08-09 after explicit semantic-heavy pressure test and closure review.**

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

does not prove an affected wrapper is installed, registered, exercised, or semantically dependent on the changed behavior.

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

### 7.1 Source authority and identity precede semantic interpretation

Before interpreting what evidence means, UpgradePilot must establish what the evidence is and what exact object it describes where that can be determined independently.

```text
source identity / provenance / proposal binding
        ↓
semantic interpretation
```

Semantic confidence cannot repair analysis of the wrong source/revision/dependency.

### 7.2 Semantic interpretation produces attributed claims, not self-authorizing verdicts

LLMs may assist with natural-language release notes, upstream change mechanisms, framework/plugin relationships, candidate proposition formulation, and code semantics where no practical simple deterministic procedure exists.

But semantic output remains:

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

### 7.3 Prefer deterministic decision procedures where reliable

A **decision procedure** is a defined method that answers a bounded question according to explicit rules.

Reliable mechanical procedures should normally own questions such as version/specifier membership, exact identity, exact changed-file/source-span membership, resolved dependency edges, inventory membership, and explicit configuration/set relations.

Deterministic logic is preferred there because it is repeatable, inspectable, testable, and traceable.

### 7.4 Deterministic transformation is not source authority

Preserve:

```text
deterministic transformation != authoritative evidence
```

and:

```text
authoritative evidence != necessarily deterministic interpretation
```

Provenance and interpretation solve different problems.

### 7.5 Semantic proposition evaluation is allowed where deterministic evaluation is not practical

Bounded semantic evaluation may contribute to a proposition when no practical deterministic procedure adequately captures the software meaning, but it must remain:

- tied to exact evidence;
- attributed as interpretation;
- grounded/reconstructable where practical;
- uncertainty-preserving;
- incapable of self-assigning authority or completeness;
- incapable of converting unsupported ambiguity into established/refuted merely through confidence.

### 7.6 Evidence-boundary completeness is not a semantic-model responsibility

Whether the observed universe is complete enough belongs to evidence acquisition/provenance/coverage reasoning.

A model can interpret observed evidence but cannot make omitted plugins, dependency branches, environments, or runtime state disappear through confidence.

### 7.7 Proposition knowledge state comes from bounded evaluation over admitted evidence

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

Unsupported or insufficiently grounded model output cannot by itself upgrade a proposition from unresolved.

This is a responsibility boundary, not authorization for a runtime `PropositionEvaluator` class.

### 7.8 Candidate applicability composition should be deterministic once proposition logic is explicit

When candidate structure and proposition states are known, applicability composition should normally be mechanical.

For example:

```text
A AND (B OR C)

A = established
B = refuted
C = established
→ candidate established applicable through A+C
```

No runtime Boolean engine is authorized merely by accepting this responsibility boundary.

### 7.9 Proposition formulation is itself a high-impact semantic responsibility

Semantic assistance may help derive candidate-specific propositions, but the propositions must remain explicit, candidate-specific, grounded, and reviewable.

Omitting a necessary proposition can create false applicability; inventing an unnecessary proposition can create false non-applicability or needless investigation.

### 7.10 Prefer a deterministic shell around bounded semantic reasoning

Current direction, without runtime commitment:

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

If no adequate validation exists, preserve uncertainty rather than invent certainty.

### 7.11 Applicability authority stops before maintainer action

```text
applicability evaluation
!=
maintainer decision
```

Applicability does not own final safety, repository-policy compliance, residual-risk acceptance, or merge/defer action.

---

## 8. Conversation-B semantic-heavy pressure test — Kedro / Pluggy

### 8.1 Why this test was selected

Challenge Pass 02 C202 uses `kedro-org/kedro#2782`, whose exact target change is:

```text
pluggy ~=1.0
→ pluggy ~=1.2
```

Frozen PR head:

```text
6c8d716ad5a6e863d339b7574b66d3a841f0f92c
```

The recorded upstream evidence establishes a changed Pluggy wrapper/dispatch/result/exception semantic in the proposed interval. Exact Kedro-head evidence establishes that Kedro:

- constructs `PluginManager`;
- defines/uses the `kedro.hooks` entry-point namespace;
- loads setuptools entry-point plugins;
- dispatches lifecycle hooks such as `before_pipeline_run`, `on_pipeline_error`, and `after_pipeline_run`;
- therefore participates in real Pluggy discovery, registration, dispatch, ordering, wrapper, result, and exception pathways.

These facts establish the **control pathway**, not the target-specific activation of every Pluggy semantic change.

### 8.2 Mechanism-specific candidate used for the pressure test

```text
UPSTREAM MECHANISM
Pluggy wrapper/result/exception behavior changes across the proposed transition

+

EXPOSURE
Kedro executes lifecycle hooks through Pluggy-managed dispatch

+

ACTIVATION
an exact participating implementation uses/depends on the affected wrapper semantic

+

POSSIBLE CONSEQUENCE
hook execution/result/exception behavior can differ
```

This is intentionally narrower than:

```text
Pluggy changed
+ Kedro uses Pluggy
→ impact
```

### 8.3 Candidate-specific propositions

A representative decomposition for this candidate is:

```text
P1 — the affected Pluggy version is selected in the exact context
P2 — a relevant Pluggy hook-dispatch path exists in the exact target revision
P3 — an implementation using the affected wrapper mechanism exists in the exact context
P4 — that implementation is registered/participating in the relevant manager/path
P5 — the relevant lifecycle hook is reachable in the required sense
P6 — that implementation actually relies on the specific wrapper/result/exception property that changed
```

This is a pressure-test decomposition, not a universal Pluggy schema. Another mechanism may require different propositions.

### 8.4 What can be mechanical versus semantic

The case cleanly separates responsibilities:

- **P1** can normally use deterministic exact-version/resolution evidence.
- **P2** is strongly supported by exact target source showing Pluggy manager construction, entry-point loading, and hook dispatch.
- **P3/P4** may use exact environment/package/entry-point/registration evidence, but target-source inspection alone cannot close an external plugin universe.
- **P5** must distinguish architectural reachability from proof that one exact execution actually reached the hook; the evidence requirement depends on the proposition wording.
- **P6** is the semantic-heavy proposition: detecting `wrapper=True` or general Pluggy participation does not automatically prove reliance on the particular changed result/exception behavior.

### 8.5 Mechanism alignment

The pressure test exposes a useful semantic distinction:

```text
uses dependency
!=
participates in affected mechanism
!=
relies on specific changed property
```

For this case:

```text
Kedro uses Pluggy
```

is weaker than:

```text
an exact implementation participates in wrapper semantics
```

which is still weaker than:

```text
that implementation depends on the particular wrapper/result/exception property changed by the transition
```

**Working principle:** applicability may require **mechanism alignment** between the specific upstream property that changed and the specific target/plugin behavior that depends on it. `Mechanism alignment` is currently descriptive reasoning language, not an authorized runtime field/type/category.

### 8.6 How a semantic claim becomes admissible

A model may produce a grounded claim such as:

```text
Exact implementation I appears to rely on changed semantic X because
its before/after-yield behavior consumes, transforms, or propagates the
result/exception in a way described by the exact upstream change evidence.
```

For that claim to influence proposition state, retain:

- exact upstream semantic evidence;
- exact implementation evidence;
- exact target/plugin/revision/context identity;
- the attributed semantic relation being asserted;
- grounding/source reconstruction where practical;
- deterministic corroboration where available;
- uncertainty when the relation remains ambiguous.

A vague model statement such as `this looks affected` is not sufficient.

Corroborating documentation/tests/comments or a discriminating old-versus-new execution can strengthen the proposition, but Conversation B does not require every semantic proposition to be experimentally reproduced.

### 8.7 Correct behavior under unresolved semantic evidence

Suppose:

```text
P1 = established
P2 = established
P3 = established
P4 = established
P5 = established
P6 = unresolved
```

and the candidate requires all six.

Then:

```text
candidate applicability = unresolved
```

not `probably applicable`, not `not applicable`, and not `safe`.

This is the key pressure-test result: **the model does not collapse when a proposition lacks a cheap deterministic decision procedure. It preserves the semantic uncertainty explicitly.**

That unresolved proposition then becomes an appropriate input to Conversation C: what discriminating evidence/check, if any, is worth acquiring next?

### 8.8 Conditional pruning still works

If an exact, complete context establishes that no implementation using the affected wrapper mechanism is installed/registered, then a necessary proposition such as P3/P4 can be refuted and the bounded candidate can close without deeper P6 semantic analysis.

This preserves the earlier principle that deeper semantic investigation must earn its cost.

### 8.9 Pressure-test conclusion

The Kedro/Pluggy test did **not** require any foundational change to the B model.

It did not require UpgradePilot to:

- let an LLM own source authority;
- let an LLM invent evidence completeness;
- let an LLM directly own proposition/applicability truth;
- pretend every semantic proposition has a deterministic procedure;
- force ambiguous semantics into true/false;
- create a Pluggy-specific applicability architecture.

The accepted responsibility shape remains coherent:

```text
deterministic/authoritative evidence where available
+
bounded semantic interpretation where genuinely necessary
+
explicit candidate-specific proposition
+
grounding / uncertainty preservation
+
bounded proposition knowledge state
+
deterministic candidate composition
```

---

## 9. Conversation-B closure review

**Closure review date:** 2026-08-09  
**Result:** **PASS — Conversation B CLOSED.**

### 9.1 Closure criteria review

1. **Applicability knowledge states coherent — PASS.**  
   `established applicable`, `established not applicable`, `unresolved`, and `conflicted` have distinct evidence/justification semantics.

2. **Candidate-specific necessary propositions and alternative paths coherent — PASS.**  
   Conjunctive/alternative activation can be reasoned about without a universal dependency checklist or runtime Boolean engine.

3. **Positive and bounded negative evidence semantics coherent — PASS.**  
   One complete viable path can establish applicability; every viable path must be eliminated for candidate-level non-applicability.

4. **Open-world/closed-world boundary coherent — PASS.**  
   Non-observation defaults to unresolved unless proposition-local completeness is justified; claims stay inside their supported universe of discourse.

5. **Conflict semantics coherent — PASS.**  
   Conflict is proposition-scoped after identity/revision/context/scope/time normalization.

6. **Deterministic-versus-semantic responsibility boundary coherent — PASS.**  
   Deterministic procedures own bounded questions where reliable; semantic interpretation may handle genuine meaning problems but cannot self-assign authority/completeness/final verdicts.

7. **Semantic-heavy proposition survives without opaque model verdict — PASS.**  
   Kedro/Pluggy P6 can legitimately remain unresolved and be handed to a later investigation-selection responsibility.

8. **Representative topology pressure tests reveal no foundational contradiction — PASS.**  
   S001, Buildtest, pip-audit, Kedro/Pluggy, and the build/codegen comparator cover deterministic support-range, environment-mediated, multi-hop, dynamic/inverted-control, semantic-heavy, and artifact-mediated cases sufficiently for B's purpose.

### 9.2 What B closure does not claim

B does **not** claim:

- a final applicability enum/schema;
- a universal Boolean/rule language;
- universal semantic proposition evaluation;
- exhaustive negative-evidence methods;
- every ecosystem inspection technique;
- exact graph traversal architecture;
- final runtime module/class boundaries;
- complete investigation/check selection;
- final sufficiency/stopping or maintainer-facing action semantics.

Those are either deferred implementation questions or belong to Conversations C/D.

### 9.3 Why B closes now

No remaining question was found that would make the accepted applicability/evidence/model-authority semantics fundamentally wrong.

Remaining questions are now primarily:

```text
UNRESOLVED MATERIAL PROPOSITION
↓
what additional evidence/check could discriminate it?
↓
is that investigation worth doing?
```

That is Conversation C, not a reason to keep expanding Conversation B.

---

## 10. Decisions and provisional conclusions

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
**Accepted process decision 2026-08-07.** Resolve questions when they materially affect product/architecture/evidence-contract/implementation correctness or useful future-system design coverage; defer only when further detail adds ceremony without meaningful design value.

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

### D-025 — Candidate structure determines necessary propositions and composition
**Accepted domain decision 2026-08-09.** Necessary propositions and conjunction/alternative structure derive from the candidate, not a universal checklist.

### D-026 — Positive applicability requires one sufficiently established complete viable path
**Accepted domain decision 2026-08-09.** One complete admissible path is sufficient; every alternative need not be established.

### D-027 — Non-applicability requires elimination of every viable path
**Accepted domain decision 2026-08-09.** Refuting one branch is insufficient while another viable branch remains.

### D-028 — Missing evidence is unresolved; negative evidence requires genuine refutation within an adequate observation boundary
**Accepted domain decision 2026-08-09.** Failure to observe does not itself refute.

### D-029 — Evidence sufficiency is proposition-relative
**Accepted reasoning decision 2026-08-09.** Judge scope, authority, discriminating power, and completeness where absence matters.

### D-030 — Conflict is proposition-scoped after identity/scope/time normalization
**Accepted domain decision 2026-08-09.** Only genuinely incompatible credible evidence about the same normalized proposition is conflict.

### D-031 — Open-world reasoning is the safe default
**Accepted domain/evidence decision 2026-08-09.** Without justified completeness, non-observation remains unresolved.

### D-032 — Closed-world reasoning is local to a scoped proposition
**Accepted domain/evidence decision 2026-08-09.** Repositories/environments are not globally closed-world objects.

### D-033 — Negative evidence may use authoritative exclusion, complete bounded inventory, or deterministic derivation
**Accepted reasoning decision 2026-08-09.** These are strong patterns, not an exhaustive taxonomy.

### D-034 — Claims must not exceed the justified universe of discourse
**Accepted domain/evidence decision 2026-08-09.** Bound claims to the exact population/environment/graph/source set whose completeness is justified.

### D-035 — Completeness is itself an evidence claim
**Accepted reasoning decision 2026-08-09.** Absence can refute only after the relevant observation coverage is justified.

### D-036 — LLM semantic interpretation cannot manufacture completeness, absence, or refutation
**Accepted model-authority decision 2026-08-09.** Semantic confidence cannot create evidence coverage.

### D-037 — Source identity and authority are independent prerequisites to semantic interpretation
**Accepted evidence-authority decision 2026-08-09.** Semantic interpretation consumes bound evidence rather than establishing its own provenance.

### D-038 — LLM semantic output is an attributed claim/proposition, not a self-authorizing applicability verdict
**Accepted model-role decision 2026-08-09.** Model interpretation remains derived evidence reasoning.

### D-039 — Prefer deterministic decision procedures for propositions that admit them
**Accepted evaluation decision 2026-08-09.** Reliable mechanical procedures own bounded questions where practical.

### D-040 — Deterministic transformation and evidence authority remain separate dimensions
**Accepted evidence decision 2026-08-09.** Determinism does not create provenance; authority does not eliminate semantic interpretation needs.

### D-041 — Bounded semantic proposition evaluation is allowed where deterministic evaluation is not practical
**Accepted model/evaluation decision 2026-08-09.** Semantic evaluation must remain evidence-bound, grounded, and uncertainty-preserving.

### D-042 — Evidence-boundary completeness is owned by evidence/coverage reasoning, not model intuition
**Accepted model-authority decision 2026-08-09.** Models may interpret observed evidence but cannot declare omitted worlds complete.

### D-043 — Proposition knowledge state should be assigned by bounded evaluation over admitted evidence
**Accepted evaluation-responsibility decision 2026-08-09.** Final proposition state preserves the evidence/authority/coverage basis rather than reducing to model confidence.

### D-044 — Candidate applicability composition should be deterministic once proposition logic is explicit
**Accepted domain/evaluation decision 2026-08-09.** Mechanical composition is preferred after proposition states are explicit.

### D-045 — Proposition formulation is a high-impact semantic responsibility and must remain explicit/grounded
**Accepted model/design decision 2026-08-09.** Hidden proposition omission/overconstraint can corrupt applicability.

### D-046 — Prefer a deterministic shell around bounded semantic reasoning
**Accepted design principle 2026-08-09.** Use LLMs for hard meaning while keeping identity, coverage, mechanical inference, and composition inspectable.

### D-047 — Applicability authority stops before maintainer action
**Accepted authority-boundary decision 2026-08-09.** Applicability does not own final safety/policy/residual-risk/merge-defer decisions.

### D-048 — Semantic-heavy applicability may legitimately remain unresolved
**Accepted domain/evaluation decision 2026-08-09.** When the exact changed-property-to-target-behavior relation cannot be sufficiently grounded, the semantic-heavy proposition remains unresolved rather than being converted to a probabilistic-looking applicability verdict.

**Why:** Kedro/Pluggy demonstrates that real software semantics do not always admit a cheap deterministic oracle; uncertainty preservation is the correct product behavior and creates a precise investigation question for Conversation C.

### D-049 — Distinguish dependency use, affected-mechanism participation, and reliance on the changed property
**Accepted domain reasoning decision 2026-08-09.** Preserve:

```text
uses dependency
!= participates in affected mechanism
!= relies on specific changed property
```

**Why:** proving Kedro uses Pluggy and even proving wrapper participation does not automatically establish that the implementation depends on the exact wrapper/result/exception property changed by the transition. Applicability requires sufficient semantic alignment between the upstream mechanism and target behavior.

`Mechanism alignment` is descriptive reasoning language only; no runtime field/category is authorized.

### D-050 — Conversation B closes after the semantic-heavy pressure test
**Accepted process/design decision 2026-08-09.** The explicit closure review passed all B criteria. No remaining ambiguity was found that would make the applicability/evidence/model-authority semantics fundamentally wrong.

**Why:** remaining unknowns concern how to obtain/select additional discriminating evidence, ecosystem-specific techniques, or runtime representation—not the meaning of applicability itself.

### D-051 — Continue reconciliation with Conversation C rather than implementing the decision layer immediately
**Accepted process decision 2026-08-09.** After the B handoff check, move to **Conversation C — Best next investigation/check** before selecting the next implementation responsibility.

**Why:** unresolved applicability is now intentionally capable of naming a precise missing proposition, but UpgradePilot still lacks the stable product semantics for deciding which additional evidence/check is worth acquiring or recommending and when deeper investigation is unnecessary. Implementing a general decision/recommendation layer before that boundary risks recreating the old `evidence → action` shortcut or encoding ad hoc check-selection rules.

This does **not** require completing C/D theoretically before any implementation. Run the implementation-handoff check again at C closure.

### D-052 — Preserve broad design exploration; decision-need limits commitments/ceremony, not useful reasoning breadth
**Accepted process decision 2026-08-09.** UpgradePilot's reconciliation may deliberately use broad, technically deep exploration when doing so improves future-system coverage, exposes blind spots, tests generality, or clarifies implementation consequences.

**Why:** artificially narrowing discussion can hide important structural cases before implementation. The project should instead distinguish exploration from commitment: possibilities may be considered broadly while accepted semantics, claims of generality/universality, and implementation decisions remain evidence-bounded and explicit.

**Boundary:** this does not authorize endless theory, fake completeness, or architecture for hypothetical cases with no design value. It clarifies that D-016 is a complexity/commitment guard, not a brevity rule.

---

## 11. Active hypotheses — not final architecture

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
- **H12:** use just-enough design and implementation feedback without suppressing useful exploration.
- **H13:** multi-hop traversal needs a decision-relative stopping boundary, now primarily a Conversation-C question.
- **H14:** candidate-specific activation may be compositional; exact runtime logical representation remains deferred.
- **H15:** deterministic-shell/bounded-semantic-core may become a broader implementation pattern, but no concrete runtime module boundary is accepted.

---

## 12. Rejected shortcuts

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
semantic participation = reliance on every changed property
applicability evaluator = maintainer decision authority
broad exploration = premature architecture commitment
reconciliation must completely model the domain before implementation
```

---

## 13. Four reconciliation conversations and stop lines

### Conversation A — Dependency-update impact/problem model

**Status:** **CLOSED 2026-08-08.**

A has a usable impact boundary, survives representative cases, separates neighboring concerns, and leaves only safely deferrable taxonomy/representation details.

### Conversation B — Applicability and investigation activation

**Status:** **CLOSED 2026-08-09.**

B established coherent proposition-based applicability, evidence sufficiency/negative-evidence boundaries, open-world discipline, model-authority responsibilities, and deterministic/semantic composition semantics. The semantic-heavy Kedro/Pluggy pressure test passed without foundational contradiction.

### Conversation C — Best next investigation/check

**Status:** **ACTIVE.**

**Question:** When material uncertainty remains, what additional evidence/check is worth acquiring, executing, or recommending?

C can close when UpgradePilot has a bounded general method for:

1. identifying the exact decision-relevant unresolved proposition/question;
2. identifying candidate evidence/checks capable of discriminating that proposition;
3. distinguishing checks that can change the decision state from merely interesting evidence;
4. choosing/recommending a sufficiently discriminating supported investigation without defaulting to maximum analysis;
5. recognizing when no supported additional check is worth doing;
6. preserving authority/safety boundaries for model-proposed investigations;
7. handling direct, semantic-heavy, environment, dynamic-plugin, and multi-hop cases without fixture-specific rules.

C does **not** require autonomous debugging, arbitrary test generation/execution, universal repository experimentation, a numerical Value-of-Information optimizer, or every ecosystem inspection method.

### Conversation D — Sufficiency, stopping, and maintainer-facing result

Define when enough evidence exists to stop, how unresolved/conflicting state and repository policy interact, and what maintainer-facing synthesis is justified.

### Implementation handoff check

After every conversation ask:

> Has further conceptual discussion become lower-value than implementing or evaluating what we already understand?

This check does not require discussion to be artificially narrow. It exists to detect when new discussion no longer improves meaningful design coverage or correctness.

**B-closure judgment:** continue to C before selecting a general decision-layer implementation responsibility, because investigation selection is now the immediate missing semantic link between unresolved applicability and later sufficiency/action. Re-run this check at C closure.

---

## 14. Cross-cutting questions to preserve

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
- proposition-formulation completeness/overconstraint risk;
- mechanism alignment between changed upstream property and target behavior;
- investigation value relative to the unresolved proposition;
- design-coverage breadth without unsupported universality claims.

---

## 15. Deliberately deferred questions

Do not solve merely for completeness:

- final runtime applicability enum/schema;
- universal Boolean/logical-expression representation;
- arbitrary/general LLM semantics for all upstream changes;
- exact numerical Targeted Check Planner/Value-of-Information ranking;
- repository-policy schema;
- exact freshness/recheck/rerun triggers;
- changed-head restart/supersession semantics;
- dedicated identity/freshness subsystem;
- final whole-product sufficiency formula;
- final maintainer-facing action vocabulary;
- whether historical five action classes survive unchanged;
- complete exposure taxonomy;
- graph database/data structure choices;
- exact multi-hop traversal implementation;
- exhaustive negative-evidence proof methods across ecosystems;
- universal evidence-completeness engine;
- universal semantic proposition evaluator;
- concrete runtime `PropositionEvaluator`/rule-engine class design;
- exact deterministic-shell module boundaries;
- implementation sequence and ADR changes.

---

## 16. Final repository-change register

**Status:** Pending reconciliation.

After sufficient A–D closure, reassess only the stable owners that actually require change, potentially including:

- `PROJECT_CHARTER.md`;
- `README.md`;
- `plans/UPGRADEPILOT_90_DAY_PLAN.md`;
- `plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md`;
- applicable specifications;
- possibly an ADR for consequential accepted architecture/method;
- `MEMORY.md` for live continuation;
- source/tests only after an implementation responsibility is selected.

Do not modify these merely because they are candidates.

---

## 17. Exact current continuation

Continue **Conversation C — Best next investigation/check**.

Conversations A and B are closed. Do not reopen them unless a new real case exposes a foundational contradiction.

Discussion may remain broad and technically deep when doing so improves future-system coverage. Keep exploratory possibilities clearly separate from accepted semantics, universality claims, and implementation commitments.

The next active question is:

> **Given one materially unresolved applicability proposition, what makes an additional evidence source/check genuinely useful, and how should UpgradePilot choose among possible investigations rather than merely collect more evidence?**

Use the unresolved Kedro/Pluggy semantic-heavy proposition as the first anchor:

```text
P6:
Does the exact participating implementation rely on the specific
Pluggy wrapper/result/exception property changed by the transition?

current state:
unresolved because the changed-property → implementation-behavior relation
has not been sufficiently grounded
```

Potential investigations might include exact plugin source inspection, exact documentation/tests, a targeted semantic comparison, or a discriminating old-versus-new execution. The purpose of C is **not** to immediately choose one. First determine the general selection semantics:

```text
unresolved proposition
↓
what evidence would discriminate true vs false?
↓
candidate investigations/checks
↓
which are supported / authoritative / sufficiently scoped?
↓
which could materially change applicability or later decision state?
↓
select sufficiently useful investigation(s)
OR
justified no-further-check result
```

### First Conversation-C learning/design tasks

1. define **discriminating investigation/check** in practical UpgradePilot terms;
2. distinguish `more evidence` from `evidence capable of changing the unresolved proposition state`;
3. distinguish information gain from decision relevance/materiality;
4. determine minimum criteria for a candidate investigation to be admissible/supported;
5. explore how to compare investigation value, cost, risk, invasiveness, coverage, sequencing, and complementarity without prematurely forcing a numeric scoring model;
6. determine when an LLM may propose investigations without owning their safety/authority/value;
7. pressure-test the method against Kedro/Pluggy, Buildtest/OpenSSL, pip-audit multi-hop, and other structurally useful cases if they expose new design dimensions;
8. at C closure, run the implementation-handoff check again.
