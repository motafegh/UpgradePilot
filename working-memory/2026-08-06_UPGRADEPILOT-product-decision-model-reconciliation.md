# UpgradePilot Product Decision-Model Reconciliation Working Record

**Date opened:** 2026-08-06  
**Last discussion sync:** 2026-08-10  
**Status:** Active whole-product reconciliation; Conversation A closed; Conversation B closed; Conversation C active  
**Purpose:** Preserve the whole-product decision-model position, rationale, accepted decisions, provisional conclusions, active hypotheses, open questions, stop lines, and eventual repository-change implications in one progressive record.  
**Live-state owner:** `../MEMORY.md` remains the sole owner of current project position and exact implementation continuation.  
**Historical snapshots:** Git history preserves earlier chronological/repetitive forms, including pre-consolidation commit `e158fe041597ecb6176f4d5dab6b11961f30c8e1` and the temporary Conversation-C exploration note that was later consolidated back into this record.

---

## 1. Why this reconciliation exists

UpgradePilot completed the bounded Target-Python Support Relevance responsibility through the normal live path. That implementation now has materially stronger evidence identity, provenance, grounding, target relevance, and explicit failure/unresolved behavior than when the earlier transparent-decision documents and product-simulation conclusions were written.

The next implementation plan points toward a Transparent Decision Method, but implementing the old framing directly risks encoding stale or underspecified concepts:

- `evidence → action` shortcutting;
- historical simulation actions treated as machine truth;
- insufficient separation among upstream change, target impact, applicability, evidence, investigation, sufficiency, and final action;
- undefined repository-specific meaning of labels such as `merge after normal review`;
- missing first-class investigation selection and stopping;
- unclear policy, trust, identity/freshness, model-authority, and human-authority boundaries.

Implementation of the general decision/recommendation layer therefore remains intentionally paused while the necessary whole-product semantics are reconciled.

The process rule is:

```text
real evidence
→ identify foundational ambiguity
→ resolve useful semantics
→ implement / evaluate when useful
→ learn from behavior
→ refine
```

Do not force discussion results into enums, schemas, class hierarchies, Boolean-expression engines, graph implementations, scoring systems, planners, or frameworks before the domain relationship earns that representation.

### 1.1 Broad exploration is allowed; premature commitment is not

The anti-overdesign/decision-need discipline is not a brevity rule.

Broad technical exploration is appropriate when it materially helps to expose blind spots, compare plausible models, test structurally different cases, map future responsibilities/boundaries, or understand implementation consequences before they become expensive commitments.

Preserve:

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

The project should distinguish accepted, provisional, exploratory, hypothetical, rejected, deferred, and unverified ideas rather than suppressing useful exploration.

---

## 2. Authority and evidence discipline

Active/normative material includes the charter, README, 90-day plan, Transparent Decision Method plan, `MEMORY.md`, applicable specifications, and `AGENTS.md`.

Historical/discovery/challenge material includes product simulations, earlier B2 working records, S006, Challenge Screening Pass 02 and its handoff on `agent/product-simulation-case-screening-01`, and the non-controlling product-ambition proposal.

Historical simulations, proposals, drafts, and parallel challenge artifacts are design/challenge evidence, not automatic authority. Source/tests remain the authority for implemented behavior.

Stable principles:

```text
observation
!= interpretation
!= evidence quality
!= decision
```

and where relevant:

```text
source/raw evidence
→ parsed/normalized evidence
→ attributed claim or deterministic interpretation
→ grounding/corroboration/conflict state
→ finding or decision input
→ bounded output
```

Preserve exact proposal, dependency, version, source, revision, context, and relevant observation-time identity. Keep source authority/provenance separate from semantic meaning. Keep missing, inaccessible, stale, conflicting, invalid, unsupported, not-applicable, and unresolved distinguishable when material. Model output cannot assign its own source authority, evidence completeness, safety, or final maintainer action.

Repository policy and residual-risk acceptance remain human/repository responsibilities unless explicitly represented through trustworthy policy evidence.

---

## 3. Current whole-product discussion model

```text
public dependency-update PR
↓
exact proposal + dependency/version + base/head identity
↓
authoritative upstream changes relevant to the exact transition
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
combine only as required by candidate logic
↓
candidate applicability knowledge state
    ├── established applicable
    ├── established not applicable
    ├── unresolved
    └── conflicted
↓
remaining decision-relevant uncertainty
↓
identify discriminating target(s)
↓
next useful investigation/check/sequence
OR justified no-further-check
↓
new observation/evidence returns to proposition evaluation
↓
sufficiency / stopping
↓
combine with non-impact decision context
↓
maintainer-facing synthesis
```

This is a discussion/domain model, not an approved runtime pipeline/schema.

A central product hypothesis remains that UpgradePilot may be better understood as an **evidence-driven impact and investigation system** than as a primary five-label classifier. Historical action families may survive later as a projection; undecided.

---

# Conversation A — Dependency-update impact/problem model

## 4. Status and accepted technical-impact model

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

`Impact candidate` is the complete proposition, not a separate event between change and exposure.

### 4.2 Boundaries

```text
upstream change != target impact
```

```text
target relevance != target ownership of affected code
```

Exposure is a target-relevant relationship/pathway and may be direct, multi-hop, framework-mediated, plugin-mediated, artifact-mediated, environment-mediated, or dependency-owned.

Exposure and activation are conceptually distinct but can be evidenced by overlapping facts; this does not imply separate scanners/classes.

```text
one version transition != one impact candidate
```

A transition may yield zero, one, or multiple mechanism-specific candidates.

Materiality is decision-relative:

```text
severity != materiality
likelihood != materiality
interesting != material
material != harmful
```

Candidate exposure roots and graph-like representation remain hypotheses, not runtime commitments.

### 4.3 Conversation-A closure

A closed because the impact boundary, exposure/activation distinction, technical-impact versus neighboring non-impact context, and representative direct/multi-hop/dynamic/artifact/environment cases were coherent enough that no remaining ambiguity threatened Conversation B.

A closure does not claim a complete exposure taxonomy, graph runtime, enum/schema, or universal ecosystem model.

---

# Conversation B — Applicability and investigation activation

## 5. Applicability model

**Status:** **CLOSED 2026-08-09 after explicit semantic-heavy pressure test and closure review.**

Applicability is evaluated for **one mechanism-specific impact candidate** against **one exact target/revision/context**.

The system evaluates explicit propositions that evidence can establish, refute, leave unresolved, or place in genuine conflict.

### 5.1 Knowledge-state semantics

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

### 5.2 Necessary/sufficient propositions and candidate logic

For:

```text
A AND B AND C
```

refuting one necessary proposition closes that path.

For:

```text
A AND (B OR C)
```

refuting `B` alone does not close the candidate while `C` remains viable.

Therefore:

> Candidate-level non-applicability requires elimination of every viable applicability path, either by refuting a proposition necessary across all remaining paths or by separately closing all alternatives.

Positive applicability requires sufficient evidence for at least one complete viable path. It does not require proving every alternative.

Candidate structure determines necessary propositions and composition. No universal dependency checklist or Boolean engine is authorized.

### 5.3 Evidence sufficiency

Evidence for a proposition is judged at least by:

1. scope/identity/context/time alignment;
2. source authority;
3. discriminating power;
4. completeness/observation boundary where negative inference depends on absence.

Relevant evidence is not automatically sufficient evidence.

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

does not prove an affected wrapper is installed, registered, executed, or semantically dependent on the changed behavior.

### 5.4 Open-world / closed-world boundary

Open-world reasoning is the safe default:

```text
not observed
→ unresolved
```

unless proposition-local completeness justifies:

```text
not present in complete relevant set
→ refuted / absent within that set
```

Do not classify a whole repository/environment globally open or closed. Closed-world reasoning is local to a scoped proposition/universe of discourse.

Strong negative-evidence patterns currently recognized, without claiming exhaustiveness:

1. explicit authoritative exclusion;
2. complete bounded inventory;
3. deterministic derivation from authoritative facts.

Completeness is itself an evidence claim. Search failure alone cannot manufacture absence. An LLM cannot manufacture completeness, closed-world coverage, absence, or refutation through confidence.

### 5.5 Deterministic versus semantic responsibility boundary

Source identity/authority precedes semantic interpretation.

```text
source identity / provenance / proposal binding
        ↓
semantic interpretation
```

LLM output is an attributed claim/proposition, not a self-authorizing applicability verdict.

Prefer deterministic decision procedures where reliable: version/specifier membership, identity, source-span/changed-file membership, resolved dependency edges, inventory membership, explicit configuration/set relations, etc.

Preserve:

```text
deterministic transformation != authoritative evidence
```

and:

```text
authoritative evidence != necessarily deterministic interpretation
```

Bounded semantic evaluation is allowed when no practical deterministic procedure captures the required software meaning, but it must remain evidence-bound, grounded/reconstructable where practical, attributed, uncertainty-preserving, and unable to self-assign completeness/authority.

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

Candidate applicability composition should be mechanical once proposition states and logic are explicit.

Preferred design direction:

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

This is a design principle, not authorization for a universal `PropositionEvaluator`, rule engine, or module layout.

Applicability authority stops before repository policy, safety, residual-risk acceptance, merge/defer, or other maintainer action.

---

## 6. Conversation-B semantic-heavy pressure test — Kedro / Pluggy

Challenge Pass 02 C202 uses `kedro-org/kedro#2782`:

```text
pluggy ~=1.0
→ pluggy ~=1.2
```

Frozen PR head:

```text
6c8d716ad5a6e863d339b7574b66d3a841f0f92c
```

Recorded evidence establishes real Kedro Pluggy manager construction, `kedro.hooks` entry-point loading, lifecycle hook dispatch, and therefore Pluggy-mediated discovery/registration/ordering/wrapper/result/exception pathways. These facts establish a control pathway, not activation of every Pluggy semantic change.

Representative candidate:

```text
UPSTREAM MECHANISM
Pluggy wrapper/result/exception behavior changes
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

Representative propositions:

```text
P1 — affected Pluggy version selected
P2 — relevant hook-dispatch path exists
P3 — implementation using affected wrapper mechanism exists
P4 — implementation registered/participating
P5 — relevant lifecycle hook reachable in required sense
P6 — implementation actually relies on the specific changed wrapper/result/exception property
```

This is a pressure-test decomposition, not a universal Pluggy schema.

The test established the important distinction:

```text
uses dependency
!=
participates in affected mechanism
!=
relies on specific changed property
```

`Mechanism alignment` is useful descriptive reasoning language for the changed-property ↔ target-behavior relation, but not an authorized runtime field/category.

For semantic-heavy P6, exact upstream evidence + exact implementation evidence + exact identity/context + grounded/reconstructable semantic relation may support a claim. Vague model intuition such as `this looks affected` is insufficient.

If:

```text
P1..P5 = established
P6 = unresolved
```

then candidate applicability remains unresolved. The model does not collapse merely because P6 lacks a cheap deterministic oracle.

Conversely, if a complete exact context refutes a necessary earlier proposition such as affected implementation presence/registration, deeper P6 analysis can be pruned.

### 6.1 Conversation-B closure review

**Result: PASS — Conversation B CLOSED.**

Closure criteria passed for:

- coherent applicability knowledge states;
- candidate-specific necessary/alternative propositions;
- positive and bounded negative evidence semantics;
- open-world/closed-world boundaries;
- proposition-scoped conflict;
- deterministic-versus-semantic/model-authority responsibilities;
- semantic-heavy proposition handling without opaque LLM verdict;
- representative S001, Buildtest, pip-audit, Kedro/Pluggy, and build/codegen topologies.

B closure does not claim a final runtime enum/schema, Boolean language, universal semantic evaluator, exhaustive negative-evidence system, graph traversal implementation, complete check-selection system, or final maintainer-facing action semantics.

Remaining questions are now primarily:

```text
UNRESOLVED MATERIAL PROPOSITION
↓
where exactly is the uncertainty?
↓
what additional evidence/check could discriminate it?
↓
is that investigation worth doing?
```

That is Conversation C.

---

# Conversation C — Best next investigation / targeted-check selection

## 7. Status and problem

**Status:** **ACTIVE.**

Conversation C asks:

> **What acquisition, analysis, execution, or observation could materially improve UpgradePilot's justified knowledge about a materially unresolved proposition, and which investigation or investigation sequence is worth pursuing?**

C does not own proposition truth. It reasons about what evidence/check is worth acquiring/executing/recommending, then returns the resulting observations to Conversation-B proposition-evaluation semantics.

```text
B:
What proposition state is justified?

C:
What should we investigate to improve that state?
```

### 7.1 Working vocabulary — conceptual only

**Evidence source:** object/system capable of supplying information, e.g. exact source, lockfile/resolution metadata, CI log, runtime environment, authoritative docs, tests, package metadata, issue/maintainer discussion, installed-package/entry-point inventory.

**Investigation:** deliberate evidence-acquisition, analysis, or execution activity aimed at a specific unresolved question.

**Check:** a more bounded operation with an explicit input/question/result boundary.

**Observation/result:** what the investigation/check actually produces.

```text
SOURCE
↓
INVESTIGATION / CHECK
↓
OBSERVATION
↓
EVIDENCE INTERPRETATION / VALIDATION
↓
PROPOSITION EVALUATION
```

These are working domain distinctions, not accepted runtime types.

---

## 8. Discriminating investigation and sufficient discrimination

A relevant investigation is not automatically useful.

Buildtest example:

```text
unresolved proposition:
historical exact environment used OpenSSL <1.1.1
```

`CI ran on Perlmutter` is relevant but does not discriminate `<1.1.1` versus `>=1.1.1`. Exact authentic `ssl.OPENSSL_VERSION` would be much more discriminating.

### 8.1 Provisional working definition — discriminating investigation

> **A discriminating investigation is a bounded, supported evidence-acquisition, analysis, or execution step whose plausible outcomes can materially change the justified state of a specific unresolved proposition or another explicitly identified downstream decision-relevant state.**

Important qualities:

- bounded question/observation target;
- supported capability/authority/safety boundary;
- proposition-specific rather than generic `investigate more`;
- plausible outcomes considered before execution;
- materially decision-relevant rather than merely interesting;
- value measured in justified knowledge/state movement, not model confidence.

### 8.2 Directional discrimination

A check need not discriminate symmetrically.

Finding one exact affected wrapper may strongly establish existence/participation, while failure to find one may remain weak negative evidence if coverage is incomplete.

Therefore conceptually ask:

```text
What could a positive result justify?
What could a negative result justify?
What could an ambiguous/no-result outcome justify?
```

rather than assigning one generic discrimination score.

### 8.3 Information gain versus decision-relevant information gain

Value of Information (VoI) is a useful conceptual reference, but no numerical VoI optimizer is authorized.

Preserve:

```text
information gain
!=
decision-relevant information gain
```

A large body of history may add lots of information but little decision value; one narrow observation may radically change applicability or prune a path.

### 8.4 Resolution versus reduction

`Sufficiently discriminating` does not mean one check must fully resolve the proposition.

Distinguish:

```text
RESOLUTION
unresolved
→ established / refuted
```

from:

```text
REDUCTION
broad unresolved space
→ narrower unresolved space / fewer viable paths / fewer required checks
```

Useful state movement may include:

```text
unresolved → established/refuted
broad unresolved → narrower bounded unresolved
several viable paths → fewer viable paths
expensive downstream check → pruned
unclear next question → precise next target
open/incomplete evidence universe → sufficiently closed bounded universe
apparent conflict → normalized or confirmed genuine conflict
```

Thus sufficient discrimination is relative to **decision-relevant progress**, not only immediate proposition closure.

### 8.5 Discriminating target

Working term:

> **Discriminating target** — the missing fact, relation, observation, or counterfactual outcome whose resolution could materially change the proposition state or downstream investigation state.

Examples:

```text
Buildtest:
exact historical SSL implementation/version
```

```text
Kedro:
changed Pluggy property ↔ exact implementation behavior dependence
```

```text
pip-audit:
exact resolved transitive dependency/path relationship
```

Preferred investigation-generation reasoning:

```text
unresolved proposition
↓
why is it unresolved?
↓
what exact missing fact/relation would discriminate it?
↓
discriminating target
↓
candidate investigations capable of observing/testing that target
```

This is more precise than selecting tools from the broad dependency topic.

### 8.6 `Unresolved` alone is insufficient C input

Conversation C needs the **uncertainty location/reason**, not only the B-level state.

Examples:

```text
missing exact environment fact
semantic mechanism alignment ambiguous
external inventory incomplete
runtime reachability unobserved
credible evidence genuinely conflicted
```

Provisional relationship:

```text
UNRESOLVED PROPOSITION
+
UNCERTAINTY LOCATION / REASON
→ investigation-generation input
```

No runtime uncertainty-reason enum is authorized.

### 8.7 Sharpened provisional definition — sufficiently discriminating

> **An admissible investigation is sufficiently discriminating when its plausible, evidentially usable outcomes have a realistic ability to materially advance the current decision state—by establishing/refuting a proposition, narrowing its unresolved scope, closing or activating a viable candidate path, resolving a material conflict or coverage gap, pruning downstream work, or materially changing what investigation or stopping decision is justified next.**

Whether it should actually be selected additionally depends on feasibility, authority, scope alignment, safety, coverage, cost, latency, invasiveness, reproducibility, pruning potential, and its relationship to alternative/complementary investigations.

This is still exploratory/provisional C language, not yet promoted into a final accepted decision.

---

## 9. Investigation dimensions and admissibility versus preference

Candidate investigations may differ along multiple dimensions:

- discriminating direction/power;
- scope alignment;
- authority/evidential quality;
- coverage/completeness relevance;
- capability/feasibility;
- cost;
- latency;
- invasiveness;
- security/safety risk;
- reproducibility;
- pruning power;
- complementarity with other checks.

No numeric formula/score/universal ranking is authorized.

### 9.1 Admissibility first

A powerful check should first pass hard boundaries before being compared with alternatives.

Conceptual questions:

```text
Does it target a material unresolved proposition/discriminating target?
Can the result be bound to exact identity/context?
Can the result become admissible evidence?
Is the capability actually available/supported?
Is execution within security/safety/authority boundaries?
Is the check sufficiently scoped to interpret its result?
```

If not, reject it rather than assigning it a lower score.

Then compare softer preference dimensions among admissible investigations.

This is analogous to constrained optimization conceptually:

```text
choose useful investigation
subject to hard safety / authority / capability / scope constraints
```

No mathematical optimizer is implied.

### 9.2 Feasibility and discrimination are separate

An ideal observation may be unavailable. Exact historical SSL metadata may be perfectly discriminating but impossible to recover. A dynamic experiment may discriminate well but be inadmissible because it executes untrusted code outside approved isolation.

High theoretical discrimination cannot override impossibility or hard safety/authority boundaries.

---

## 10. Sequencing, pruning, complementarity, and escalation

Investigations may form adaptive sequences rather than a flat list.

Example:

```text
I1 — establish exact implementation/environment presence
↓
enough to close/establish a necessary proposition?
├── yes → stop/prune this branch
└── no
    ↓
I2 — exact tests/docs + bounded semantic comparison
↓
sufficiently clear?
├── yes → return evidence to B evaluation
└── no
    ↓
I3 — targeted dynamic/differential execution if justified
```

### 10.1 Conditional investigation plan

Working meaning:

> A plan in which later investigations are activated only when earlier observations leave material uncertainty that those later checks can still discriminate.

This preserves:

```text
do not execute work whose prerequisite question is already resolved
```

### 10.2 Branch pruning is first-class investigation value

If a low-cost check refutes a necessary upstream proposition, an entire candidate path may close and deeper semantic/dynamic investigation becomes irrelevant.

Therefore investigation value depends partly on candidate/path logic from Conversation B.

A check can be sufficiently discriminating because it resolves an upstream gate whose outcome prunes downstream work even if it never directly answers a later proposition.

### 10.3 Complementarity

Two individually partial investigations may jointly discriminate better than either alone.

Example:

```text
source inspection
+
runtime trace
```

Source may establish possible/intended structure while trace establishes actual execution.

Therefore C may select an investigation set or conditional sequence, not always one check.

### 10.4 Static/dynamic and observational/interventional lenses

These are exploratory lenses, not taxonomies.

**Static:** source/AST, dependency graph, metadata/lockfile/config, docs.

**Dynamic:** unit/integration/import test, runtime trace, build, resolver simulation, differential execution.

```text
dynamic != universally stronger
static != universally weaker
```

**Observational:** inspect existing facts.

**Interventional:** deliberately alter/execute something to observe consequences.

Because dependency upgrades are counterfactual, interventional checks can sometimes provide especially useful causal discrimination.

### 10.5 Differential testing

Differential testing compares the same target/context/inputs under old versus proposed dependency behavior:

```text
same target revision
same relevant environment
same input/context
old dependency
vs
proposed dependency
```

It can strongly discriminate a candidate but remains limited by path coverage, environment fidelity, nondeterminism, mechanism attribution, setup cost, and execution risk.

A promising escalation pattern to pressure-test is:

```text
authoritative/static evidence
↓
bounded semantic analysis
↓
sufficiently clear?
├── yes → return evidence to B
└── no
    ↓
consider targeted dynamic/differential discriminator
```

This is not accepted as a universal rule.

### 10.6 Semantic confidence is not semantic sufficiency

For semantic-heavy investigations, model confidence cannot be the sufficiency criterion.

Potential sufficiency considerations include exact upstream-property binding, exact target/plugin implementation binding, a clear semantic relationship, few/no materially plausible alternative interpretations, reconstructable reasoning, and corroborating tests/docs/behavior where needed.

```text
semantic confidence
!=
semantic sufficiency
```

If materially plausible interpretations remain, preserve unresolved.

---

## 11. Investigation generation, validation, and authority boundaries

A semantic model may be useful for proposing candidate investigations, but model generation alone cannot establish that a proposed check is supported, correctly scoped, authoritative enough, safe, non-redundant, worth its cost/invasiveness, or preferred.

Current conceptual responsibility split:

```text
semantic reasoning
→ propose candidate investigations

capability / evidence / safety reasoning
→ validate feasibility, scope, authority, execution boundary

selection reasoning
→ determine which investigation(s), if any, are worth pursuing
```

No runtime modules/classes are authorized by this exploration.

Hard safety/authority constraints are non-tradeable: a high-discrimination check does not become acceptable merely because it promises information value.

---

## 12. Investigation-selection failure modes

Design against:

```text
evidence hoarding
cheapest-first dogma
strongest-test dogma
tool-driven investigation
fixed source→tests→CI→docs checklist
confirmation-seeking only
LLM curiosity explosion
unsafe autonomous execution
redundant evidence
infinite uncertainty chasing
```

The unresolved proposition and uncertainty location should drive the investigation—not available tools, generic checklists, or a desire to eliminate uncertainty at any cost.

---

## 13. Two legitimate Conversation-C outcomes

Conversation C success is not only `find another check`.

Two valid outcomes are:

```text
A. useful next investigation / investigation sequence identified
```

or:

```text
B. no additional supported investigation is currently justified
```

The second may occur when checks are non-discriminating, unsupported, unsafe, disproportionately costly, impossible to scope authoritatively, infeasible, or incapable of materially changing downstream decision state.

This does **not** turn unresolved into not-applicable. It preserves unresolved and explicitly records that no further justified check is currently available/worth doing. The maintainer-facing meaning belongs partly to Conversation D.

---

## 14. Conversation-C case anchors

### 14.1 Kedro / Pluggy

Unresolved semantic-heavy proposition:

```text
Does exact implementation I rely on changed Pluggy wrapper/result/exception semantic X?
```

Candidate investigations: exact implementation/environment inspection, exact tests/docs, bounded semantic comparison, targeted runtime trace, differential old/new execution.

Pressure points: structural viability versus mechanism alignment, semantic ambiguity, conditional pruning, static/dynamic complementarity, model proposal versus execution authority.

### 14.2 Buildtest / OpenSSL

Unresolved environment proposition:

```text
Did exact historical environment use OpenSSL <1.1.1?
```

Candidate investigations: historical environment/module manifest, authentic logged `ssl.OPENSSL_VERSION`, reproducible frozen environment reconstruction, weaker current docs/source searches as comparators.

Pressure points: exact-time scope, authority, direct observation versus expensive reconstruction, feasibility, and justified no-further-check if authoritative historical evidence no longer exists.

### 14.3 pip-audit / CacheControl / urllib3

Potential proposition:

```text
Does exact resolution R contain a target-relevant path to the incompatible CacheControl/urllib3 interaction?
```

Candidate investigations: exact resolved graph construction, intermediary version verification, exact contract/mechanism verification; target-source grep is deliberately weak comparison evidence.

Pressure points: graph completeness, structural path existence versus semantic mechanism alignment, multi-hop traversal/pruning.

---

## 15. Current broad Conversation-C reasoning flow

```text
MATERIAL UNRESOLVED PROPOSITION
        ↓
identify uncertainty location / reason
        ↓
identify discriminating target(s)
        ↓
generate candidate investigations/checks
        ↓
ADMISSIBILITY GATE
    scope / identity
    authority
    capability / feasibility
    safety / security
    interpretability
        ↓
for admissible candidates consider:
    discrimination direction/power
    coverage
    cost / latency
    invasiveness
    reproducibility
    pruning power
    complementarity
        ↓
consider ordering / conditional activation / escalation
        ↓
choose sufficiently useful investigation / investigation set
OR
justify no-further-check
        ↓
acquire observation/evidence
        ↓
return to Conversation-B proposition evaluation semantics
        ↓
repeat only while material uncertainty and justified useful investigation remain
```

This is a discussion/design model only.

### 15.1 Broader provisional selection principle

The earlier phrase `smallest sufficiently discriminating investigation` remains useful as an anti-overanalysis heuristic but must not mean `always choose the single cheapest check`.

Current broader provisional principle:

> **Prefer the lower-cost/lower-risk admissible investigation or conditional investigation sequence that provides sufficient decision-relevant discrimination, while allowing stronger or complementary checks when they materially improve coverage, authority, causal/semantic discrimination, or downstream pruning.**

No numerical Value-of-Information score, planner class, universal ranking formula, or fixed investigation taxonomy is authorized.

---

## 16. Comparing and sequencing admissible investigations — provisional exploration

The current problem is no longer only whether an investigation is admissible or sufficiently discriminating. Several investigations may all pass those tests while differing materially in cost, discrimination, pruning leverage, complementarity, invasiveness, and downstream consequences.

### 16.1 Dominance and Pareto reasoning

Working concept:

> **Investigation A dominates investigation B for one exact proposition/context when A is no worse than B on all material comparison dimensions and is materially better on at least one, without introducing a compensating disadvantage.**

Dominance is proposition-relative, not a global property of a tool. Static inspection may dominate dynamic execution for one exact declarative proposition while dynamic execution may be the stronger discriminator for an actual-behavior counterfactual.

When no option dominates because one is cheaper/safer while another is more discriminating or broader, a genuine trade-off remains.

**Pareto dominance** is useful reasoning language: clearly dominated candidates can be removed without inventing numeric scores. The remaining non-dominated options form a conceptual comparison frontier; no Pareto optimizer/runtime structure is authorized.

### 16.2 Compare conditional strategies, not only isolated checks

The strongest individual check may not be the best investigation strategy.

```text
Plan A:
run expensive differential test immediately

Plan B:
run cheap authoritative structural check
↓
if it closes/prunes the path → stop
otherwise → run differential test
```

Plan B may be preferable because it preserves access to the stronger check while sometimes avoiding it entirely.

Therefore the useful comparison unit can be a **conditional investigation strategy/policy**, not merely one check.

Working definition:

> **A conditional investigation policy is a bounded rule for selecting the next admissible investigation based on the current proposition/candidate state and observations already obtained.**

This is conceptual only; no planner/policy runtime is authorized.

### 16.3 Logical position and pruning leverage

Investigation order should consider candidate logic.

For:

```text
A AND (B OR C)
```

refuting `A` closes the whole candidate while refuting `B` still leaves the `C` route viable. Therefore an investigation of a shared necessary gate can have greater pruning leverage than a branch-local check even if both are similarly cheap.

Useful reasoning term:

> **Shared-gate leverage** — how much of the remaining candidate/path structure depends on the proposition being investigated.

This is not an authorized runtime field.

Investigation order therefore need not equal logical order or cheapest-first order. A later-looking proposition may deserve earlier investigation when its result has materially greater pruning/decision leverage.

### 16.4 Complementarity versus redundancy

Two individually partial investigations can jointly discriminate better than either alone.

```text
source semantics
+
runtime participation trace
```

may jointly establish more than either source alone.

Distinguish:

```text
semantic redundancy
```

from:

```text
evidentially useful corroboration
```

A second source can still be valuable when it improves authority, scope, coverage, conflict resolution, or reproducibility even if it appears to support the same broad claim.

Complementarity may be **serial** (the first check determines whether the second is activated) or **parallel** (independent evidence sources are jointly useful).

### 16.5 Escalation must be earned and observation-driven

Working principle:

> Move to a stronger, more costly, more invasive, or more execution-heavy investigation only when a specific material uncertainty remains and the stronger investigation can discriminate that remaining uncertainty.

Not:

```text
previous check did not say safe
→ automatically escalate
```

Instead:

```text
observation
↓
material uncertainty remains at location X
↓
next check specifically targets X
```

Potential pattern:

```text
metadata/static evidence
↓
source/semantic analysis
↓
ambiguity remains?
├── no → return to B
└── yes
    ↓
targeted runtime/differential check if admissible
```

This remains a pattern to pressure-test, not a universal ladder.

Escalation can also terminate in:

```text
remain unresolved
+
no justified further investigation
```

when the next stronger check is unsafe, infeasible, unauthoritative, non-reproducible, disproportionate, or insufficiently discriminating.

### 16.6 Hard constraints are non-compensatory

A hard safety/authority/scope/capability failure cannot be offset by excellent discrimination or low cost.

Conceptually:

```text
excellent discrimination
+
unacceptable execution boundary
→ inadmissible
```

Potential hard gates include wrong target/revision identity, inability to bind evidence to the proposition, unsupported capability, prohibited/unsafe execution, or unacceptable credential/data exposure.

Other dimensions—cost, latency, degree of discrimination, coverage, reproducibility, pruning, complementarity—may be softer trade-offs depending on context.

The hard/soft split itself may be context-sensitive and is not frozen as taxonomy.

### 16.7 Qualitative comparison rather than fake precision

Possible comparison language, not runtime enums:

```text
dominates
strongly preferred
conditionally preferred
complementary
escalation-only
redundant
inadmissible
```

This permits justified comparison without invented probabilities or arbitrary utility scores.

Parts of the process may behave lexicographically:

```text
unsafe / unauthorized / wrong-scope
→ reject before preference comparison
```

but a universal lexicographic ranking of all soft dimensions is not accepted.

### 16.8 Adaptive planning and bounded lookahead

Investigation planning should react to observations:

```text
plan before observation
!=
plan after observation
```

because new evidence changes candidate viability, uncertainty location, required checks, and downstream paths.

However precomputing every possible branch risks **state-space explosion**.

Working bounded-lookahead principle:

> Consider enough downstream consequences to understand pruning, escalation, and complementarity, choose only the next justified investigation or small conditional bundle, then re-evaluate after the observation.

This resembles adaptive/receding-horizon planning conceptually, but UpgradePilot does not need a general decision-tree/planning framework to use the principle.

### 16.9 Strong provisional comparison/sequence principles to pressure-test

1. hard admissibility constraints precede preference comparison;
2. clearly dominated investigations should be removed;
3. investigation quality is proposition/candidate-relative, not tool-relative;
4. candidate logical structure matters because checks can prune paths;
5. conditional sequences/policies may be a better comparison unit than isolated checks;
6. investigation planning should adapt to observations;
7. stronger/more invasive checks require explicit escalation justification;
8. complementary/corroborating evidence can outrank one supposedly strongest source;
9. uncertainty need not be eliminated at any cost;
10. bounded lookahead is preferred to constructing a complete investigation tree.

These remain **provisional** until pressure-tested. No new accepted D-decision is created yet.

---

## 17. Conversation-C pressure-test checkpoint and exact continuation

The next step is to pressure-test Sections 8–16 rather than add more abstractions immediately.

The first pressure test should deliberately challenge the tempting heuristic:

```text
cheap structural check first
→ semantic/dynamic check later
```

Select a structurally realistic case where the cheapest structural investigation is admissible and relevant but **not obviously the best first move** because another investigation has materially stronger direct discrimination, shared-gate leverage, causal value, or pruning power.

The pressure test should ask:

1. do admissibility gates still behave correctly?;
2. does dominance/Pareto reasoning remove only genuinely inferior options?;
3. can the model prefer a non-cheapest first investigation without a numeric score?;
4. does candidate logic/pruning leverage explain the ordering?;
5. do complementarity and escalation remain coherent?;
6. can the plan adapt after each observation without constructing a giant decision tree?;
7. do hard safety/authority boundaries remain non-compensatory?;
8. can the outcome legitimately be `no further justified investigation`?;
9. does the result return cleanly to Conversation-B proposition evaluation rather than creating a second applicability engine?;
10. does the test expose any foundational flaw requiring C semantics to change?

Use an existing challenge/product-simulation case if it provides the needed topology; otherwise use another real dependency-update case only if it exposes a genuinely new design dimension.

Do not yet promote the provisional comparison principles to accepted decisions merely because they sound coherent.

---

## 18. Decisions and provisional conclusions

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

### D-015 — Proposal identity controls assessed object; mutable evidence is time-bounded observation
**Provisional design conclusion.** Later releases do not silently replace the proposal. Correctly scoped observations remain historically valid even when the world later changes.

### D-016 — Reconciliation is bounded by decision need
**Accepted process decision 2026-08-07.** Resolve questions when they materially affect product/architecture/evidence-contract/implementation correctness or useful future-system design coverage; defer when detail adds ceremony without meaningful design value.

### D-017 — Impact candidate is the complete technical proposition
**Accepted domain decision 2026-08-08.** Upstream change + exposure/path + activation conditions + possible consequence form the candidate. No runtime class/enum/schema implied.

### D-018 — Conversation A sufficiently closed
**Accepted 2026-08-08.** No remaining A ambiguity was found capable of making B fundamentally wrong.

### D-019 — Challenge Pass 02 is B pressure-test evidence; A remains closed
**Accepted 2026-08-09.** Parallel challenge artifacts strengthen rather than contradict A.

### D-020 — Applicability is per mechanism-specific candidate
**Accepted 2026-08-09.** One transition may yield zero/one/multiple candidates; applicability is independent per candidate.

### D-021 — Target relevance does not require target ownership; presence does not establish activation
**Accepted 2026-08-09.** Material interaction may occur in dependencies/frameworks/plugins/artifacts/environments. Presence alone is insufficient.

### D-022 — Applicability knowledge-state semantics
**Accepted 2026-08-09.** Preserve `established applicable`, `established not applicable`, `unresolved`, `conflicted` as conceptual justification states. No runtime enum/schema yet.

### D-023 — Exposure and activation conceptually distinct without mandatory separate evidence machinery
**Accepted 2026-08-09.** One fact may help establish both; do not prematurely split scanners/classes/channels.

### D-024 — Applicability is proposition-based
**Accepted 2026-08-09.** Evaluate explicit target/revision/context propositions rather than vague labels.

### D-025 — Candidate structure determines necessary propositions and composition
**Accepted 2026-08-09.** Necessary propositions and conjunction/alternatives derive from the candidate, not a universal checklist.

### D-026 — Positive applicability requires one sufficiently established complete viable path
**Accepted 2026-08-09.** One complete admissible path can suffice.

### D-027 — Non-applicability requires elimination of every viable path
**Accepted 2026-08-09.** Refuting one branch is insufficient while another viable branch remains.

### D-028 — Missing evidence is unresolved; negative evidence requires genuine refutation within an adequate boundary
**Accepted 2026-08-09.** Failure to observe does not itself refute.

### D-029 — Evidence sufficiency is proposition-relative
**Accepted 2026-08-09.** Judge scope, authority, discrimination, and completeness where absence matters.

### D-030 — Conflict is proposition-scoped after identity/scope/time normalization
**Accepted 2026-08-09.** Only genuinely incompatible credible evidence about the same normalized proposition is conflict.

### D-031 — Open-world reasoning is the safe default
**Accepted 2026-08-09.** Without justified completeness, non-observation remains unresolved.

### D-032 — Closed-world reasoning is local to a scoped proposition
**Accepted 2026-08-09.** Repositories/environments are not globally closed-world objects.

### D-033 — Negative evidence may use authoritative exclusion, complete bounded inventory, or deterministic derivation
**Accepted 2026-08-09.** Strong patterns, not exhaustive taxonomy.

### D-034 — Claims must not exceed justified universe of discourse
**Accepted 2026-08-09.** Bound claims to exact population/environment/graph/source set whose completeness is justified.

### D-035 — Completeness is itself an evidence claim
**Accepted 2026-08-09.** Absence can refute only after relevant coverage is justified.

### D-036 — LLM semantic interpretation cannot manufacture completeness, absence, or refutation
**Accepted 2026-08-09.** Semantic confidence cannot create evidence coverage.

### D-037 — Source identity and authority independently precede semantic interpretation
**Accepted 2026-08-09.** Semantic interpretation consumes bound evidence rather than establishing its provenance.

### D-038 — LLM semantic output is attributed claim/proposition, not self-authorizing applicability verdict
**Accepted 2026-08-09.** Model interpretation remains derived evidence reasoning.

### D-039 — Prefer deterministic decision procedures where reliable
**Accepted 2026-08-09.** Mechanical procedures own bounded questions where practical.

### D-040 — Deterministic transformation and evidence authority remain separate dimensions
**Accepted 2026-08-09.** Determinism does not create provenance; authority does not eliminate semantic interpretation needs.

### D-041 — Bounded semantic proposition evaluation allowed where deterministic evaluation is impractical
**Accepted 2026-08-09.** Semantic evaluation must remain evidence-bound, grounded, and uncertainty-preserving.

### D-042 — Evidence-boundary completeness owned by evidence/coverage reasoning, not model intuition
**Accepted 2026-08-09.** Models may interpret observed evidence but cannot declare omitted worlds complete.

### D-043 — Proposition knowledge state assigned by bounded evaluation over admitted evidence
**Accepted 2026-08-09.** State preserves evidence/authority/coverage basis rather than model confidence.

### D-044 — Candidate applicability composition should be deterministic once proposition logic is explicit
**Accepted 2026-08-09.** Mechanical composition preferred after proposition states are explicit.

### D-045 — Proposition formulation is high-impact semantic responsibility and must remain explicit/grounded
**Accepted 2026-08-09.** Hidden omission/overconstraint can corrupt applicability.

### D-046 — Prefer deterministic shell around bounded semantic reasoning
**Accepted design principle 2026-08-09.** Use LLMs for hard meaning while identity, coverage, mechanical inference, and composition stay inspectable.

### D-047 — Applicability authority stops before maintainer action
**Accepted 2026-08-09.** Applicability does not own final safety/policy/residual-risk/merge-defer decisions.

### D-048 — Semantic-heavy applicability may legitimately remain unresolved
**Accepted 2026-08-09.** If changed-property ↔ target-behavior relation cannot be sufficiently grounded, remain unresolved rather than emitting probabilistic-looking applicability verdict.

### D-049 — Distinguish dependency use, affected-mechanism participation, and reliance on changed property
**Accepted 2026-08-09.** Preserve `uses dependency != participates in affected mechanism != relies on specific changed property`. `Mechanism alignment` remains descriptive reasoning language only.

### D-050 — Conversation B closes after semantic-heavy pressure test
**Accepted 2026-08-09.** Explicit closure review passed; remaining unknowns concern investigation/evidence techniques or runtime representation rather than applicability meaning.

### D-051 — Continue reconciliation with Conversation C before general decision-layer implementation
**Accepted 2026-08-09.** Investigation selection is the immediate missing semantic link between unresolved applicability and later sufficiency/action. Re-run implementation-handoff check at C closure.

### D-052 — Preserve broad design exploration; decision-need limits commitments/ceremony, not useful reasoning breadth
**Accepted 2026-08-09.** Broad technically deep exploration may improve design coverage; acceptance, universality claims, and implementation commitments remain evidence-bounded.

---

## 19. Active hypotheses — not final architecture

- **H1:** impact/investigation may be more central than five-class recommendation.
- **H2:** historical action classes may survive later as maintainer-facing projection.
- **H3:** `normal review` may not be UpgradePilot-owned without repository policy.
- **H4:** targeted investigation likely core product value.
- **H5:** simulations/challenge cases remain evidence, not labels.
- **H6:** current Python-support implementation is one proven slice, not universal template.
- **H7:** flat impact taxonomy probably wrong.
- **H8:** exposure may compress into reusable coupling/contract roots.
- **H9:** exposure may be multi-hop/graph-shaped without graph implementation.
- **H10:** technical exposure is one subset of larger decision context including trust/identity/policy.
- **H11:** identity/freshness should not inflate into continuous monitoring.
- **H12:** use just-enough design and implementation feedback without suppressing useful exploration.
- **H13:** multi-hop traversal needs decision-relative stopping boundary, now partly a C/D issue.
- **H14:** candidate activation may be compositional; exact runtime logical representation deferred.
- **H15:** deterministic-shell/bounded-semantic-core may become broader implementation pattern; no module layout accepted.
- **H16:** investigation selection may be best modeled as admissibility constraints followed by qualitative comparison/conditional sequencing rather than one global numeric score.
- **H17:** structural viability checks may commonly precede expensive semantic/dynamic checks because of pruning value, but this is not yet a universal rule.
- **H18:** conditional/adaptive investigation policies with bounded lookahead may provide a better conceptual model than static ranked checklists, but this must survive pressure testing without requiring a general planning engine.

---

## 20. Rejected shortcuts

```text
upstream change = target impact
anything decision-relevant = technical impact
flat API/security/platform/performance/CI impact taxonomy
historical simulation action = machine truth
newer release silently replaces exact proposal
all exposure is direct source/API use
one version transition = one aggregate impact candidate
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
deterministic procedure required for every semantic proposition
candidate applicability should be re-decided by free-form LLM after proposition states known
semantic participation = reliance on every changed property
applicability evaluator = maintainer decision authority
broad exploration = premature architecture commitment
uncertain → collect everything
cheapest check = automatically best check
strongest possible test = automatically best check
tool availability determines investigation question
fixed source→tests→CI→docs checklist for every candidate
LLM-generated investigation = authorized/safe/preferred investigation
high model confidence = semantic sufficiency
high information volume = high decision value
high discrimination can override hard safety/authority constraints
static check = always first check
logical proposition order = investigation order
corroborating evidence = automatically redundant
one strongest investigation = always better than adaptive sequence
uncertainty requires escalation until certainty
complete future investigation tree must be planned before acting
unresolved must always be eliminated
reconciliation must completely model the domain before implementation
```

---

## 21. Four reconciliation conversations and stop lines

### Conversation A — Dependency-update impact/problem model
**CLOSED 2026-08-08.**

### Conversation B — Applicability and investigation activation
**CLOSED 2026-08-09.**

### Conversation C — Best next investigation/check
**ACTIVE.**

C can close when UpgradePilot has a bounded general method for:

1. identifying exact decision-relevant unresolved proposition/question and uncertainty location;
2. identifying discriminating target(s);
3. generating candidate investigations/checks capable of discriminating them;
4. distinguishing merely interesting evidence from decision-relevant state movement;
5. separating hard admissibility from softer preference;
6. comparing/sequencing sufficiently discriminating investigations without fake precision;
7. recognizing when no supported additional investigation is worth doing;
8. preserving authority/safety boundaries for model-proposed investigations;
9. handling direct, semantic-heavy, environment, dynamic-plugin, artifact, and multi-hop cases without fixture-specific rules.

C does not require autonomous debugging, arbitrary test generation/execution, universal repository experimentation, numerical VoI optimization, final planner schema, or every ecosystem inspection technique.

### Conversation D — Sufficiency, stopping, and maintainer-facing result

Define when enough evidence exists to stop, how unresolved/conflicting state and repository policy interact, and what maintainer-facing synthesis is justified.

### Implementation handoff check

After every conversation ask:

> Has further conceptual discussion become lower-value than implementing or evaluating what we already understand?

This check detects diminishing design value; it does not require artificially narrow discussion.

B-closure judgment: continue to C. Re-run at C closure.

---

## 22. Cross-cutting questions to preserve

- product value and repeatability;
- authority/provenance/grounding/conflict;
- negative evidence and observation boundaries;
- repository-policy boundary;
- identity/freshness/decision time;
- LLM/model role and authority;
- stopping/actionability;
- generality and human authority;
- explainability and complexity control;
- concern topology/design economy;
- candidate granularity/ownership independence;
- applicability knowledge state;
- path completeness/evidence discrimination;
- claim scope/universe-of-discourse discipline;
- semantic-claim grounding/uncertainty;
- deterministic decision-procedure preference;
- proposition-formulation completeness/overconstraint risk;
- mechanism alignment;
- investigation value relative to uncertainty location;
- admissibility versus preference;
- directional discrimination;
- dominance/Pareto reasoning;
- logical pruning/shared-gate leverage;
- complementarity/corroboration;
- escalation and non-compensatory hard constraints;
- adaptive policies and bounded lookahead;
- static/dynamic and observational/interventional evidence;
- design breadth without unsupported universality claims.

---

## 23. Deliberately deferred questions

Do not solve merely for completeness:

- final runtime applicability enum/schema;
- universal Boolean/logical-expression representation;
- arbitrary/general LLM semantics for all upstream changes;
- numerical Targeted Check Planner / VoI ranking;
- final planner/ranking schema;
- universal investigation taxonomy;
- autonomous executor;
- repository-policy schema;
- exact freshness/recheck/rerun triggers;
- changed-head restart/supersession semantics;
- dedicated identity/freshness subsystem;
- final whole-product sufficiency formula;
- final maintainer-facing action vocabulary;
- whether historical five action classes survive unchanged;
- complete exposure taxonomy;
- graph database/data-structure choices;
- exact multi-hop traversal implementation;
- exhaustive negative-evidence proof methods;
- universal evidence-completeness engine;
- universal semantic proposition evaluator;
- concrete `PropositionEvaluator`/rule-engine class design;
- exact deterministic-shell module boundaries;
- general adaptive-planner/decision-tree machinery;
- implementation sequence and ADR changes.

---

## 24. Final repository-change register

**Status:** Pending reconciliation.

After sufficient A–D closure, reassess only stable owners that actually require change, potentially:

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

## 25. Exact current continuation

Continue **Conversation C — Best next investigation/check**.

Conversations A and B are closed. Do not reopen them unless a new real case exposes a foundational contradiction.

Discussion may remain broad/technically deep where it improves future-system coverage. Keep exploratory possibilities separate from accepted semantics, universality claims, and implementation commitments.

The comparison/sequencing model in Sections 8–16 is now sufficiently developed to pressure-test rather than extend abstractly.

The exact next action is:

> **Run a pressure test in which the cheapest/most obvious structural investigation is admissible and relevant but is not clearly the best first move, and determine whether dominance, logical pruning leverage, complementarity, escalation, hard constraints, adaptive sequencing, and bounded lookahead select a better investigation path without numeric scoring.**

Prefer an existing real challenge/product-simulation case if one has the required topology. Add another real dependency-update case only if necessary to expose this design dimension.

After that test, explicitly decide which C principles survive, which need revision, and whether another structurally different pressure test is required before C closure.

---

## 26. Conversation-C Pressure Test 1 — C01 artifact-mediated code generation

**Date:** 2026-08-10  
**Status:** Completed pressure test; provisional C comparison/sequence model survived with two material refinements; Conversation C remains active.

### 26.1 Why this case was selected

The existing challenge case `dominodatalab/container-runtime-interface-api#101` changes:

```text
grpcio-tools ~=1.73
→
grpcio-tools ~=1.80
```

at frozen PR head:

```text
034f0a82e2c06526212353a1258f59f159538914
```

Exact target evidence establishes:

- `grpcio-tools` is a development dependency;
- `bin/update-proto.sh` invokes `python -m grpc_tools.protoc` against vendored `.proto` definitions;
- the invocation writes Python, typing, and gRPC artifacts under `src/cri_api`;
- generated artifacts are committed/package source;
- ordinary CircleCI jobs install development dependencies and run lint/tests/build/publish paths but do not explicitly invoke `bin/update-proto.sh`;
- the Dependabot PR itself changes only the `grpcio-tools` requirement.

This makes the dependency transition artifact-mediated rather than an ordinary target-runtime call path.

### 26.2 Candidate and discriminating target

Representative candidate:

```text
UPSTREAM MECHANISM
grpcio-tools / bundled protoc generation behavior changes
+
EXPOSURE
target invokes grpc_tools.protoc on frozen vendored CRI proto inputs/options
+
ACTIVATION
the regeneration process is executed using the proposed generator context
+
POSSIBLE CONSEQUENCE
generated committed Python/gRPC/typing artifacts differ in a target-relevant way
```

Representative propositions:

```text
P1 — proposed generator selected in generation context
P2 — exact target generation path exists
P3 — target inputs/options reach grpc_tools.protoc
P4 — generated outputs become target/package artifacts
P5 — old vs proposed generation produces different relevant artifacts
P6 — any difference is materially relevant to runtime/API/typing/build behavior
```

P1–P4 are structurally strong. The central unresolved proposition for this pressure test is P5.

Discriminating target:

> **With the same relevant target inputs/options, does the old-versus-proposed generation world produce a different relevant generated-artifact set?**

### 26.3 Competing investigations

Three representative options were compared:

```text
I1 — more target-structure inspection
I2 — upstream release/source semantic inspection across 1.73→1.80
I3 — controlled old/new regeneration and generated-artifact diff
```

I1 is cheap/safe/reproducible but has diminishing discrimination because the generation structure is already established.

I2 is useful for mechanism explanation and may identify relevant generator changes, but remains directionally weak: finding an upstream change does not establish that these target inputs differ, and failure to find an obvious change does not establish identical target outputs.

I3 is more expensive/invasive but directly targets P5 and can have high pruning leverage.

### 26.4 Why non-cheapest I3 can be the best first substantive investigation

I3 does not Pareto-dominate I2 because I2 remains cheaper/safer. The real trade-off therefore survives dominance filtering.

However P5 is a high-leverage gate:

```text
P5 refuted
→ no target-specific generated-artifact difference
→ P6 and deeper consequence/mechanism investigation are unnecessary for this candidate path
```

Therefore a controlled regeneration comparison can be qualitatively preferred without fake numeric scoring:

```text
I2:
low cost
+ moderate/one-sided discrimination
+ limited direct pruning

I3:
moderate cost
+ direct bilateral discrimination
+ exact target specificity
+ high pruning leverage
```

This pressure test rejects any universal rule that static/structural or cheapest evidence must precede a direct interventional check.

### 26.5 Minimal experiment pre-flight

A dynamic comparison is admissible only after a narrow pre-flight establishes that it can be performed safely, reproducibly, and with a meaningful contrast.

```text
MINIMAL EXPERIMENT PRE-FLIGHT
↓
Can we construct a safe, reproducible, correctly scoped old/new contrast?
├── no → dynamic investigation inadmissible; use another route or remain unresolved
└── yes → targeted differential regeneration
```

This pre-flight is not broad source analysis. It exists to validate experiment scope/execution conditions.

### 26.6 Contrast validity — new provisional refinement

The exact target generation path invokes `grpc_tools.protoc`, `--mypy_out`, post-processing, and formatting. Old/new dependency resolution could also alter `protobuf`, `mypy-protobuf`, formatter/tooling versions, or other transitive environment state.

Therefore:

```text
target-specific experiment
!=
automatically valid experiment
```

Working term:

> **Contrast validity** — whether an old-versus-new comparison actually represents the distinction asked by the proposition, with other materially relevant differences controlled or explicitly accounted for.

Two legitimate counterfactual questions must remain distinguishable:

```text
PROPOSAL-LEVEL EFFECT
What happens to the target when the actual dependency constraint changes and the environment resolves accordingly?
```

versus:

```text
MECHANISM ATTRIBUTION
Did grpcio-tools's own changed generator behavior cause the observed artifact difference?
```

The first may legitimately include transitive resolver changes as part of the real proposal world. The second requires tighter causal control.

Preserve:

```text
decision-relevant discrimination
!=
causal attribution
```

`Contrast validity` remains provisional C language, not a runtime field/schema.

### 26.7 Observation-dependent plan

A valid differential regeneration can produce materially different next states:

```text
O1 — relevant outputs identical
→ P5 refuted within the admitted contrast
→ artifact-difference path closes
→ deeper P6/upstream/runtime investigation pruned

O2 — relevant outputs differ
→ P5 established/supported within the admitted contrast
→ P6 activates
→ inspect exact diff + targeted upstream mechanism + target-relevant consequences

O3 — proposed generation fails while old succeeds
→ strong direct evidence of a generation/build-time consequence within valid contrast
→ mechanism explanation/remediation may follow

O4 — experiment unstable/confounded
→ result is not admissible evidence for P5
→ refine contrast, choose another investigation, or remain unresolved
```

This strongly supports adaptive planning and bounded lookahead: only enough future branching is needed to justify the next check, then the plan should be recomputed after the observation.

### 26.8 Post-execution evidence validation

Admissibility before execution is necessary but not sufficient. A completed check can still fail evidential validation because the result is unstable, confounded, out-of-scope, or cannot be attributed to the proposition being tested.

Therefore:

```text
investigation executed successfully
!=
result is admissible evidence
```

This refines C's validation boundary without creating a second applicability engine.

### 26.9 Investigation results may feed candidate refinement

The earlier broad flow primarily returned investigation observations to Conversation-B proposition evaluation. This pressure test shows another legitimate feedback path.

If a differential result reveals that the observed difference is caused by a materially different mechanism than the candidate originally represented, the result may expose:

```text
incomplete/wrong candidate formulation
```

or:

```text
new mechanism-specific impact candidate
```

Therefore the product discussion flow should allow:

```text
INVESTIGATION RESULT
↓
does it bear on the current proposition as formulated?
├── yes → return to B proposition evaluation
└── reveals different mechanism / bad formulation
    → refine/formulate candidate
    → derive/evaluate propositions again
```

This does not reopen Conversation A's semantics; it makes the whole-product flow iterative rather than rigidly one-way.

### 26.10 Pressure-test verdict against provisional principles

```text
1. hard admissibility before preference                      PASS
2. remove only clearly dominated investigations             PASS
3. proposition-relative investigation quality               PASS STRONGLY
4. candidate logic/pruning affects ordering                 PASS STRONGLY
5. conditional sequence may beat isolated-check ranking     PASS
6. adaptive planning                                        PASS STRONGLY
7. stronger investigation must earn activation              PASS WITH REFINEMENT
8. complementarity/corroboration                             PASS
9. uncertainty need not be eliminated                       PASS
10. bounded lookahead                                        PASS STRONGLY
```

Refinement to item 7:

> A dynamic/interventional check does not always belong at the end of `static → semantic → dynamic`. When a direct experiment targets the decisive shared gate with much greater decision leverage, it may be the first substantive investigation after only the minimum pre-flight needed to make it admissible and valid.

### 26.11 Pressure-test result

**Pressure Test 1 result: PASS with refinements.**

No foundational contradiction was found in the Conversation-C comparison/sequencing model.

Two material provisional refinements were exposed:

1. **contrast validity** for interventional/differential checks;
2. **feedback from investigation observations to candidate refinement/generation** when the observed mechanism differs from the one originally formulated.

Do not yet promote the full C model or these refinements to accepted D-decisions. A complementary pressure test is still required against a case where the ideal discriminating evidence may be unavailable and increasingly expensive reconstruction may legitimately end in unresolved/no-further-investigation.

### 26.12 Updated exact continuation

Run **Conversation-C Pressure Test 2 — C203 Buildtest/OpenSSL**.

Primary focus:

```text
ideal historical observation may be unavailable
↓
weaker current/contextual evidence exists
↓
reconstruction options become progressively more costly or less authoritative
↓
decide whether to investigate, reconstruct, narrow the proposition, or stop unresolved
```

Pressure-test specifically:

- feasibility versus theoretical discrimination;
- historical identity/time authority;
- reconstruction fidelity and evidential status;
- dominance and qualitative comparison when no ideal check is feasible;
- whether weaker evidence can narrow but not resolve;
- escalation stopping;
- justified `unresolved + no further supported investigation`;
- whether the new contrast-validity concept helps or overfits the code-generation case;
- whether C and D stopping concerns can remain separated cleanly enough for C closure.
