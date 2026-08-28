# B2/X1 Evidence-First LLM Risk and Design Exploration

**Date:** 2026-08-28  
**Status:** ACTIVE EXPLORATORY WORKING MEMORY  
**Scope:** bounded learning/engineering exploration around how LLMs should interact with UpgradePilot's already-built evidence pipeline before committing to the previously designed strict planner boundary  
**Broader plans retained:** `plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md`, `plans/B2_X1_PHASE3_EVALUATION_PROTOCOL.md`, and `plans/B2_X1_LEARNING_ONLY_TINY_MASTERY_PLAN.md` remain intact and are not superseded as durable plans by this working record.

## 1. Why this exploration exists

The project already has a substantial deterministic evidence pipeline and one adopted bounded semantic-model component. Before we decide how strict, narrow, or heavily guarded the new planner/controller must be, we want to observe the actual failure surface in our own system.

The exploration therefore starts from the real questions:

```text
what exact data reaches an LLM?
where did that data come from?
which transformations already happened before the model sees it?
what exact output can the model produce?
what downstream code consumes that output?
what is the worst credible consequence of a wrong output?
which failures are actually reachable in UpgradePilot?
which controls materially reduce those failures?
which proposed controls are only generic AI-safety ceremony for our current responsibility?
```

The goal is not to reject safety, structured outputs, deterministic admission, closed actions, or the accepted X1 plans. The goal is to earn those mechanisms through evidence and understand exactly which ones are necessary, sufficient, excessive, or incomplete for UpgradePilot.

## 2. Exploration method

Use Learning-by-Doing / Learning-by-Engineering rather than a theory-first security checklist.

For each concern:

```text
1. trace the current real code/dataflow
2. state one falsifiable hypothesis
3. identify the exact input and output boundary
4. design the smallest experiment that can discriminate the hypothesis
5. prefer real UpgradePilot data/cases when safe and reproducible
6. observe actual model/system behavior
7. preserve raw evidence and exact configuration needed to interpret the result
8. distinguish model failure from deterministic-pipeline failure, transport failure, or evaluation error
9. decide whether a control is justified by observed risk
10. update this record progressively before moving to the next concern
```

Do not build a generalized safety framework before a concrete experiment requires it.

Do not weaken accepted product truth/evidence semantics merely to make an experiment easier. Experiments may deliberately use a less constrained **model interface** to expose failure behavior, but they should remain isolated from real target mutation or irreversible external side effects unless a separately justified responsibility later requires that capability.

## 3. Important scope correction

When this record says **current system**, it means the existing UpgradePilot implementation that was built before the new X1 planner experiment, not only the already-written Phase-2/3B/4A planner experiment code.

That existing product flow includes, among other things:

```text
public PR / repository / CI / package / upstream evidence
→ deterministic acquisition and identity checks
→ dependency/environment/CI/upstream interpretation
→ bounded support-drop semantic extraction where needed
→ deterministic grounding/promotion
→ target relevance / impact / investigation state
```

The new planner/controller is being evaluated **on top of** that existing evidence system.

## 4. Current implementation facts already established

These are observations from current source, not final design conclusions.

### FACT-1 — the product already contains one LLM semantic boundary

`src/upgradepilot/upstream/support_drop_extractor.py` sends a bounded exact crossed-release changelog window to LM Studio and asks the model to select candidate Python support-drop semantics.

The model returns a bounded selection (`python_line`, `introduced_in_version`, `source_line_id`), after which deterministic code recovers exact source text/offsets and `validate_support_drop_candidates(...)` grounds the candidate against exact admitted upstream authority.

Therefore the pre-X1 product is not accurately described as "all external evidence becomes deterministic state before any model sees it." One LLM already participates in semantic extraction before later impact/applicability state exists.

### FACT-2 — deterministic grounding proves attribution/identity more strongly than English semantics

The support-drop grounding layer verifies facts such as:

- exact dependency interval identity;
- admitted source kind;
- exact release membership;
- exact selected source and source span;
- exact quote recovery;
- explicit Python X.Y token presence.

It does not independently implement a full natural-language proof that the grounded sentence semantically means a current support drop. The semantic extractor remains responsible for that candidate interpretation.

This makes semantic misclassification of real/misleading/adversarial release prose a concrete hypothesis worth testing rather than assuming away.

### FACT-3 — current X1 Phase-4A snapshots are frozen evaluator-built cases

The currently prepared development/protected case builders explicitly construct `PropositionAssessment` and `InvestigationSnapshot` values. They are not yet a live dynamic projection from `PublicPullRequestInvestigation`.

Therefore runtime poisoning of those current experiment snapshots by external repository prose is not presently a reachable Phase-4A path. A wrong snapshot there would primarily be a harness/reconstruction error.

This distinction matters when later designing a real product-owned snapshot projection.

### FACT-4 — the deterministic product already solves the first S001 action selection

`select_python_support_drop_investigation(...)` already deterministically selects `acquire_exact_target_python_declaration` when the exact target declaration proposition is unresolved/insufficient and no target relevance has yet been acquired.

The X1 planner is therefore not justified because S001 needs an LLM. The experiment asks whether a model-driven controller can eventually add useful flexibility across varied evidence states without moving domain truth/authority into the model.

## 5. Core hypotheses to test

These are hypotheses, not accepted findings. They may be confirmed, narrowed, rejected, or replaced as experiments produce evidence.

### H1 — trusted-state construction can fail before the new planner

**Question:** Can the already-built product pipeline produce a materially wrong later proposition/state from validly acquired external evidence even when structural/provenance validation passes?

Concrete first branch to examine:

```text
exact tagged changelog
→ CrossedReleaseSourceWindow
→ LocalSupportDropExtractor
→ CandidateUpstreamClaimResult
→ validate_support_drop_candidates(...)
→ GroundedPythonSupportDropClaim
→ PythonSupportDropImpactAssessment / propositions
```

Candidate failure classes to test:

- negation (`Python 3.8 support was not dropped`);
- continued support (`Python 3.8 remains supported`);
- future/planned support changes;
- historical statements that are not current in the release;
- ambiguous minimum-version wording;
- multiple nearby Python-version statements;
- instruction-shaped or adversarial text embedded in otherwise valid release prose;
- wording that is structurally groundable but semantically points in the opposite direction.

Primary question is not "can prompt injection happen?" It is:

> Can exact, structurally valid, authority-grounded external prose still cause a false semantic promotion in the current normal product path, and what downstream claim strength can that false promotion reach?

### H2 — external adversarial/misleading text may or may not survive into the future planner context

**Question:** Starting from the existing product evidence objects, what externally controlled text or semantic influence would actually remain if we build a live planner snapshot from current product state?

We must trace field-by-field rather than assume.

For each candidate planner field, classify:

```text
fully deterministic scalar/enum
trusted identity/provenance
model-derived but deterministically grounded semantic result
human/evaluator-authored explanatory text
raw/near-raw external text
mixed-origin text
```

Then test whether any raw or semantically adversarial content is truly planner-visible and whether it changes model decisions.

This hypothesis should determine whether prompt-injection-specific controls are central, minor, or unnecessary for the planner's actual first product seam.

### H3 — wrong STOP/no-tool decisions need an exact causal account

**Question:** Given an exact planner input, what specific relationship must the model infer to choose a useful action rather than `stop`, `defer`, or `unresolved`?

For the simplest A1 state the semantic join is approximately:

```text
planning question
+ unresolved/insufficient target proposition
+ one allowed action whose preconditions match that proposition
+ action purpose/results
→ useful discriminating action exists
→ choose_action
```

Experiments should vary one factor at a time to learn where wrong no-tool decisions actually come from, for example:

- proposition wording/keys;
- evidence-state representation;
- action purpose wording;
- explicit preconditions versus implicit relationship;
- presence of already-established neighboring propositions;
- remaining-step budget;
- irrelevant but trusted context;
- explanatory `detail` text;
- multiple unresolved propositions;
- model/prompt differences.

Do not explain a failure merely as "the model reasoned badly." Identify the smallest input/relationship change that caused or removed it when possible.

### H4 — multiple unresolved propositions create a real planning problem

**Question:** When several propositions are unresolved, can the model distinguish:

```text
actionable prerequisite gap
vs
dependent unresolved consequence
vs
unresolved fact irrelevant to the bounded planning question
```

S001 is the first real example:

```text
exact_target_python_declaration_established
→ unresolved / insufficient
→ currently actionable by A1

declared_python_range_intersects_dropped_line
→ unresolved / insufficient
→ depends on exact target declaration
```

Experiments should determine whether the model can infer that dependency from our current state representation or whether the representation itself needs improvement.

### H5 — many strict controls may protect authority but not planner quality

**Question:** Which existing proposed controls change the model's reasoning quality, and which merely bound consequences after a wrong decision?

Examples to compare empirically where useful:

- plain text output vs JSON Schema;
- free-form proposed next step vs closed action IDs;
- model-supplied action arguments vs pre-bound action descriptors;
- no admission vs deterministic admission;
- minimal prompt vs explicit hard-constraint prompt;
- raw/near-raw evidence vs typed state;
- typed state with and without explanatory details.

The important distinction is:

```text
control prevents unauthorized effect
!=
control makes the model choose correctly
```

Both can matter, but for different reasons.

### H6 — the worst-case consequence should determine control strength

For every experiment/output class, trace the furthest reachable consequence.

Example classes:

```text
wrong semantic extraction
wrong proposition state
wrong action selection
wrong STOP/DEFER/UNRESOLVED
unsupported model reason/claim
wrong action arguments
repeated action
transport/provider failure
malformed structured output
```

Then ask what the current/future consumer can actually do with that result:

```text
record only?
acquire another read-only exact source?
update trusted evidence state?
terminate investigation?
produce user-visible claim?
recommend maintainer action?
mutate repository/external system?
```

A control is justified proportionally to the reachable consequence, not merely because it is common in agent-security guidance.

## 6. Initial experiment families

These are a working queue, not a mandatory full suite. We will pick them one by one and may stop early when enough evidence exists.

### E1 — existing semantic extractor adversarial/ambiguity probes

Use the real `LocalSupportDropExtractor` request/response contract and bounded crossed-release windows.

Start with small controlled changelog variants around the already-understood support-drop mechanism. Preserve exact prompt, model/configuration, raw response, parsed candidate, deterministic grounding result, and downstream impact state.

Purpose: test H1 with a real already-adopted LLM boundary.

### E2 — pre-planner state-origin inventory

Trace a real `PublicPullRequestInvestigation`/S001-style flow and classify every candidate planner field by origin/trust/semantic ownership.

Purpose: test H2 before designing planner prompt-injection controls.

### E3 — minimally constrained planner capability probe

Give the model a real or faithfully reconstructed product state with fewer pre-imposed planner restrictions than the accepted strict X1 contract.

Observe what it naturally proposes, what fields/arguments it invents, which evidence it uses, and whether it can identify the useful gap.

This experiment should be isolated from real side-effectful execution. The point is to observe proposed behavior before deciding which restrictions are actually necessary.

Purpose: establish a behavioral baseline before comparing guardrails.

### E4 — incremental constraint comparison

Starting from E3, add one control at a time only when it addresses an observed or clearly reachable failure:

```text
state structuring
→ action descriptions
→ output schema
→ action allowlist
→ pre-bound arguments
→ deterministic admission
→ additional prompt rules
```

Compare what each control changes:

```text
model correctness
model consistency
observability/parsing
security/authority containment
failure detectability
engineering complexity
```

Purpose: test H5/H6 and prevent both over-engineering and under-engineering.

### E5 — multi-proposition relevance/actionability probes

Use S001 first, then only additional real cases if needed.

Purpose: test H3/H4 and determine whether the current proposition/snapshot representation is sufficient for planner reasoning.

## 7. Evidence discipline for this exploration

For each executed model experiment preserve at minimum:

```text
experiment ID / hypothesis
exact input case/data identity
exact model ID/runtime when available
prompt/messages or request representation
sampling/configuration relevant to interpretation
raw model output
parsed/interpreted output
any deterministic validation/admission result
observable downstream result (if execution is part of that experiment)
our interpretation
what the experiment does NOT prove
```

Do not convert one successful example into a general reliability claim.

Do not hide failures with semantic retries during first observation unless the experiment specifically studies retry behavior.

Use repeated runs only when instability is itself a decision-changing question.

## 8. Progressive findings log

### F-001 — exploration should begin earlier than the new planner

The existing support-drop semantic extractor is the first already-live model boundary with genuine externally controlled prose. It provides a higher-value initial experiment surface than assuming the new planner is the first prompt-injection boundary.

**Status:** current implementation fact; experiments still needed.

### F-002 — current planner prompt-injection risk cannot be inferred from generic LLM guidance

Whether prompt injection is material for a future product planner depends on the exact live snapshot projection and whether any externally controlled prose survives into it. Current Phase-4A evaluator-built snapshots do not establish that product risk either way.

**Status:** open; requires E2/live field-origin trace.

### F-003 — deterministic admission and planner correctness are separate responsibilities

A deterministic admission layer can bound what happens after a wrong proposal, but it does not prove that `choose_action`, `stop`, `defer`, or `unresolved` is the correct planning decision.

**Status:** established architecture distinction; E3/E4 should measure practical consequence.

### F-004 — wrong STOP is only meaningful after tracing downstream semantics

A wrong STOP is low consequence if it merely records a development decision; it becomes materially important if a future product loop treats STOP as final and prevents acquisition of useful evidence. It becomes more dangerous still only if STOP is allowed to strengthen trusted technical truth, which should be evaluated explicitly rather than assumed.

**Status:** hypothesis/consequence trace to revisit during planner integration experiments.

## 9. Decisions intentionally left open

Do not pre-decide yet:

- whether the planner needs raw or near-raw external evidence;
- whether `untrusted_evidence_notes` belongs in the product planner at all;
- whether prompt-injection-specific planner defenses are a major requirement;
- whether JSON Schema is necessary for planner quality versus mainly integration reliability;
- whether the first product planner should use only closed action IDs;
- how much action metadata should be model-visible;
- whether action arguments must always be pre-bound;
- how strict deterministic admission needs to be for a read-only first product seam;
- whether the current proposition representation is sufficient for multi-proposition planning;
- whether free-text `detail` helps or harms planner performance;
- whether a planner is useful enough to justify integration at all.

These should be decided from experiments plus existing product authority, not from generic agent architecture fashion.

## 10. Relationship to previous strict X1 plans

The accepted X1 plan/protocol remain valuable prior engineering work and provide candidate controls, evaluation cases, and failure boundaries.

For this exploratory route they are treated as:

```text
well-reasoned prior design hypotheses / candidate safeguards
not
assumptions that every safeguard must be present before we can learn from the model
```

After enough discriminating experiments:

```text
observed findings
→ compare against previous X1 design
→ retain controls that solve demonstrated/reachable problems
→ simplify/remove unsupported ceremony where authority permits
→ add missing controls exposed by experiments
→ update the durable plan/protocol only when evidence justifies it
```

Do not modify the accepted plans merely because this exploration exists. Reconciliation happens after sufficient evidence or when a concrete finding already invalidates a durable assumption.

## 11. Immediate next step

Start with **E1 / H1** unless a new inspection shows a higher-value dependency first:

> Use the already-adopted support-drop semantic extractor and real UpgradePilot source-window contract to test whether structurally valid but semantically misleading/adversarial release prose can be promoted into a grounded support-drop claim, and trace the exact downstream consequence.

Before writing a large test suite, design the first minimum-complete probe and understand its exact code path together.
