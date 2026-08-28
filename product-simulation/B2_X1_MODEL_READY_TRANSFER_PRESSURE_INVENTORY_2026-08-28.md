# B2/X1 Model-Ready Transfer Pressure Inventory

**Date:** 2026-08-28  
**Status:** PRODUCT-SIMULATION EVALUATION INVENTORY — no product adoption, implementation authorization, or live-state ownership  
**Evaluated main revision:** `a5928939dbfe96f289b309cc03dca477361ed7dd`  
**Workspace:** `product-simulation/`  

## 1. Purpose

This inventory is the smallest pre-job product-simulation check needed before selecting a new
simulation responsibility.

It asks:

> Which materially different planning/investigation behaviors already discovered by the
> product-simulation corpus are adequately represented by the current B2/X1 model-ready boundary,
> which are only partially represented, which still deserve near-term pressure testing, and which
> are outside the current planner claim?

The purpose is **not** to enlarge B2/X1 merely because the simulation corpus contains more cases.
The purpose is to prevent two opposite errors:

```text
UNDER-PRESSURE
→ treat ACTION vs one easy STOP case as proof that harder planning semantics transfer

OVER-EXPANSION
→ pull every historical simulation lesson into the current one-action planner
  even when it belongs to candidate discovery, future capabilities, or maintainer judgment
```

This file evaluates transfer pressure. It does not change `MEMORY.md`, the accepted Phase-3A
protocol, the X1 plan, product source, experiment source, or any target repository.

## 2. Authority and evidence boundary

The evaluated current-main state says:

```text
Phase 3B-1 model-ready development path implemented
+ local execution / LM Studio evidence pending
+ Learning-Only mastery pause active
```

Current implementation therefore exists as GitHub source/diff evidence, but the accumulated new
offline tests/compile checks have not yet been executed in the normal WSL environment and no local
planner-model call has been made. This inventory does not promote implementation existence into
runtime PASS or planner-quality evidence.

The accepted B2/X1 claim remains intentionally narrow:

```text
trusted planning question + typed InvestigationSnapshot
→ model proposes one pre-admitted action OR stop | defer | unresolved
→ deterministic admission retains authority
```

Only `acquire_exact_target_python_declaration` is currently independently justified as an
executable planner action. General alternative-action selection, arbitrary tool choice, final
compatibility/safety truth, and maintainer action remain outside the first pilot.

Historical product-simulation findings remain discovery/evaluation evidence. They are not current
product schema or automatic implementation authority.

## 3. Current model-ready boundary observed

The current minimum development path already represents several important boundaries correctly.

### 3.1 Basic action selection — represented

`d-a1-smoke` gives the model one unresolved target-Python proposition and one pre-bound useful A1
action.

```text
material evidence gap
+ one admitted discriminating action
→ choose_action(A1)
```

The real protected S001 builder preserves the richer real-case version of the same planning shape.

### 3.2 Basic stopping — represented

Real S004 is used as the development STOP control.

```text
decision-critical authority facts established
+ contradiction/gap refuted
+ no useful action required
+ remaining_steps still available
→ stop
```

This already protects an important invariant: remaining step budget is not itself permission or a
reason to keep investigating.

### 3.3 Authority and request boundaries — represented

The current harness/runner already provides:

- closed/pre-bound action identity;
- strict structured output;
- strict parsing before semantic admission;
- deterministic `admit_agent_plan(...)` authority;
- request projection rather than whole evaluator-object serialization;
- evaluator/oracle/partition metadata exclusion;
- `case_key` exclusion after discovering that human-readable case labels could leak answers;
- development/protected separation;
- local-only LM Studio transport preparation with the existing no-proxy owner;
- semantic model errors remaining observable rather than being silently repaired by retries.

These are real current strengths and should not be re-designed from product simulation without a
concrete failure.

## 4. Cross-case transfer classification

The classifications below distinguish **protocol representation** from **current minimal smoke
execution**. A behavior can be accepted in the frozen protocol while still not being exercised by
the current four-call Phase-4A development path.

### 4.1 COVERED — enough for the current minimum model-ready smoke

#### S001 / `d-a1-smoke` — useful admitted action

**Classification:** `COVERED`

The current representation directly exercises the simple case where one proposition is materially
unresolved and A1 has discriminating value.

No additional simulation work is required before the early development smoke merely to prove that
this planning shape exists.

#### S004 — resolved question with unused budget

**Classification:** `COVERED`

The current development STOP case directly carries the historical S004 stopping lesson into the
model-ready path.

No extra STOP case is required merely to increase case count before the first smoke.

#### Oracle/label leakage and deterministic authority

**Classification:** `COVERED AT CURRENT BOUNDARY`

The request renderer explicitly projects admitted planner-facing state and omits evaluator-only
answer-bearing metadata. The model also cannot change repository/revision/path authority by
inventing tool arguments.

Further simulation should reopen this only if a new request field, action type, replay mechanism,
or real model output exposes a new contamination/authority path.

### 4.2 PARTIAL — accepted by the protocol, not yet meaningfully exercised by the minimal smoke

#### S005 / S006 / S012 — DEFER because useful evidence lies outside the admitted capability set

**Classification:** `PARTIAL — HIGH-VALUE TRANSFER PRESSURE`

These cases carry a planning distinction that is harder than the current S004 STOP control:

```text
material question remains unresolved
+ further evidence/check could be useful in principle
+ current closed action catalog cannot perform that capability
→ defer
```

The accepted protocol already represents this family, including protected S005/S012 and the
development S006-derived defer case. Therefore this is **not a missing protocol concept** and does
not justify inventing another action.

However, the current minimal Phase-4A runner uses only `d-a1-smoke` and `d-s004-stop`. It therefore
does not yet show whether an actual model can distinguish:

```text
STOP
→ owned question sufficiently resolved; no useful continuation needed

DEFER
→ owned question still matters, but the useful capability is outside current authority/catalog
```

This is a strong candidate for the next product-simulation transfer evaluation after the pre-job
inventory.

#### S008 / S011 — STOP while adjacent propositions remain unresolved

**Classification:** `PARTIAL — HIGH-VALUE TRANSFER PRESSURE`

These cases expose another harder no-tool shape:

```text
some nearby facts remain unresolved
BUT
owned planning question is already sufficiently resolved
→ stop
```

That is materially different from the easy S004 control, where the decision-critical state is
cleanly resolved.

The pressure is important because a weak planner heuristic could behave as:

```text
any unresolved proposition exists
→ continue investigating
```

That heuristic would over-investigate and violate the planning-question boundary.

The accepted protected protocol already contains real S008/S011 STOP decisions, so no new scenario
is required to represent the semantics. What remains unproven is model-level transfer under the
later protected route, not a reason to enlarge the current four-call smoke pre-emptively.

#### Synthetic unresolved / prompt-injection control

**Classification:** `PARTIAL — PROTOCOL REPRESENTED, MINIMAL SMOKE NOT EXERCISING IT`

The accepted protocol includes an unresolved/security control. This is enough to keep
`unresolved` distinct from `stop` and `defer` in the accepted evaluation design.

The current minimum smoke does not need to expand merely to exercise every final disposition before
we learn whether the local model can follow the basic action/STOP contract.

### 4.3 LATER LOOP/ARCHITECTURE PRESSURE — materially different from the current request smoke

#### S001 post-action replay / repeated state

**Classification:** `PARTIAL — LATER EXECUTION-LOOP PRESSURE`

The accepted protocol contains S001 post-action replay and the development material includes a
repeat/stop shape. This establishes that planning must be re-evaluated after trusted state changes.

But the current Phase-4A smoke deliberately performs no capability execution. Therefore it does not
yet prove the full transition:

```text
choose action
→ execute/read result
→ deterministic interpretation/state update
→ reconstruct next planning turn
→ stop or continue
```

This is appropriate for the current smoke scope. It becomes important before claiming a useful
planner loop rather than isolated decision capability.

#### S007 transfer lesson — selected action becomes stale before execution

**Classification:** `MISSING AS A TRANSITION PRESSURE, NOT A CURRENT PHASE-4A BLOCKER`

S007 produced a stronger lesson than ordinary post-action replay:

```text
T1: question unresolved
→ investigation/action is selected

T2: before that selected action executes,
    stronger/new trusted evidence resolves the owned question

therefore
→ revalidate/prune the previously selected action
→ do not execute merely because it was selected earlier
```

This is distinct from:

```text
action executes successfully
→ result changes state
→ next planner turn stops
```

It is also distinct from retry-after-failure.

The current request → model plan → deterministic admission smoke does not need to solve this before
its first development calls, because no capability execution occurs there. But this is a genuine
future product/loop pressure: **selection must not become permanent authorization**.

The proportionate future form is a small S007-derived state-transition/controlled-variant pressure
test, not a new numbered scenario and not a generic workflow engine.

#### Failed acquisition / blind retry

**Classification:** `PARTIAL / FUTURE EXECUTION-LOOP PRESSURE`

`InvestigationSnapshot` can preserve attempted actions, and accepted evaluation material already
contains repeated-state concepts. The remaining important distinction for a real loop is:

```text
capability already attempted and failed/unavailable
→ do not blindly choose the same action again
unless new state makes retry independently useful
```

This is not required for the current no-execution Phase-4A smoke. Revisit when real action execution
and repeated planning turns become active responsibilities.

### 4.4 OUTSIDE THE CURRENT X1 CLAIM — do not pull these into the pilot merely because simulation found them

#### S010 — multi-mechanism discovery completeness

**Classification:** `OUTSIDE CURRENT X1 CLAIM`

S010 teaches that one discovered impact mechanism does not prove discovery completeness. The
current planner, however, receives an already-defined planning question and typed propositions; it
is not the owner of broad upstream mechanism discovery or candidate enumeration.

Do not add discovery tools, search actions, or general alternative-action planning to X1 to cover
S010 unless normal product work later establishes that responsibility.

#### S009 — repository-purpose / publication-context alignment

**Classification:** `OUTSIDE CURRENT X1 CLAIM`

S009 shows that repository-purpose/provenance context can contradict a proposed update without
proving technical incompatibility. That is valuable product evidence, but it is not currently an
owned action-selection responsibility of the one-action target-Python planner seam.

Do not force S009 into the current action space.

#### S006 dynamic differential as a new executable action

**Classification:** `OUTSIDE CURRENT ACTION CATALOG`

S006 demonstrates that a targeted dynamic differential can be useful when static evidence is
insufficient. The accepted protocol correctly uses this as a DEFER-style pressure because no such
capability is currently admitted.

That is better evidence discipline than fabricating a second action to make the planner look more
general.

#### General multi-action planning, arbitrary tools, maintainer action

**Classification:** `OUTSIDE CURRENT X1 CLAIM`

The existing corpus does not justify silently expanding this checkpoint into:

- arbitrary source/tool selection;
- action ranking across invented capabilities;
- generic browser/shell autonomy;
- compatibility or safety truth owned by the model;
- final merge/review/comment decisions;
- multi-agent orchestration;
- MCP/RAG/framework adoption merely for exposure.

These remain future possibilities only when a concrete responsibility and evidence justify them.

## 5. Inventory findings

### F-01 — No product-simulation blocker to the intentionally small Phase-4A development smoke

**Type:** finding

The current four-call development smoke is appropriately narrow for its purpose: expose basic
transport/schema/planner-contract behavior early rather than complete the whole protected evaluator
first.

The existing product-simulation corpus does **not** justify delaying that smoke to add more actions,
more cases, a generic loop, or a larger framework.

This does not authorize resuming the currently paused main build; the normal live-state owner and
Ali's explicit build-resume instruction still control that boundary.

### F-02 — The strongest next simulation question is no-tool disposition discrimination

**Type:** recommendation candidate

The most useful near-term transfer question is:

> Can the current planner representation distinguish `stop`, `defer`, and `unresolved` for the
> right reasons when real states contain unresolved evidence, unavailable useful capabilities,
> or adjacent questions that are outside the owned planning question?

Existing S005/S006/S008/S011/S012 plus the accepted synthetic unresolved control already provide
enough evidence variety. No S013 is justified for this question.

### F-03 — Selected-action staleness is a separate later architecture pressure

**Type:** finding / future handoff candidate

S007's pre-execution revalidation lesson is not equivalent to S001 post-action replay. It should
remain visible as a later pressure before UpgradePilot claims an execution-capable planner loop or
product integration.

It is not a blocker for the current no-execution development smoke.

### F-04 — Several valuable simulation lessons are deliberately outside current X1 ownership

**Type:** finding

S009 repository-purpose reasoning and S010 multi-mechanism discovery completeness are valuable, but
pulling them into the current planner would enlarge the method under evaluation and weaken the
comparison.

The correct current result is explicit exclusion, not implementation backlog creation.

### F-05 — The accepted protocol is broader than the current minimal runner by design

**Type:** observation

The accepted Phase-3A protocol already protects the harder final distinctions: real DEFER cases,
STOP with unresolved adjacent facts, unresolved/security pressure, and S001 post-action replay.
The current Phase-4A runner intentionally samples only a development action case and real S004 STOP.

Therefore:

```text
minimal smoke coverage < accepted protected protocol coverage
```

is currently intentional sequencing, not evidence of a protocol gap.

## 6. Recommended product-simulation continuation

If Ali selects the next simulation portion after this inventory, the highest-value first job is:

### No-Tool Disposition Transfer Evaluation

Use existing evidence rather than creating a new numbered scenario.

Primary real anchors:

```text
S005 → DEFER
S006-derived development case → DEFER
S008 → STOP despite adjacent unresolved facts
S011 → STOP despite unresolved runtime compatibility outside the owned question
S012 → DEFER because artifact-history evidence matters but capability is outside catalog
synthetic accepted control → UNRESOLVED / adversarial-data pressure
```

Evaluate the representation/reasoning distinction, not model quality that has not yet been
observed.

A useful output would separate:

```text
planning question ownership
→ materially unresolved proposition
→ whether more evidence can change the owned question
→ whether an admitted capability exists
→ STOP vs DEFER vs UNRESOLVED
→ claim limits
```

Only after that transfer evaluation should we decide whether any controlled variant, evaluator
handoff, or main-project change is justified.

### Secondary later job

Before any future execution-capable planner loop/product integration claim, run an S007-derived
**selected-action staleness / pre-execution revalidation** pressure test.

Do not start that now merely because it is known; its consequence becomes material when action
execution/loop integration becomes an active responsibility.

## 7. Explicit non-actions

This inventory does **not** justify:

- creating S013;
- modifying the accepted Phase-3A protocol;
- adding a second planner action;
- broadening the Phase-4A development smoke before observing the current candidate;
- changing `src/upgradepilot/`;
- resuming paused main implementation from product simulation;
- adding an agent framework, MCP, RAG, generic memory, browser autonomy, or multi-agent design;
- rewriting historical S001–S012 evidence to match current X1 terminology.

## 8. Stop boundary

This pre-job inventory is complete when it can answer:

1. what the current model-ready boundary already covers;
2. what harder corpus semantics remain only partially exercised;
3. which gap is most discriminating for product simulation next;
4. which attractive topics are outside the current X1 claim;
5. whether a new scenario or new action is currently justified.

Those questions are now answered.

**Inventory disposition:**

```text
CURRENT MINIMUM X1 SMOKE
→ no simulation blocker identified

NEXT PRODUCT-SIMULATION PRESSURE
→ no-tool disposition transfer using existing cases

LATER LOOP PRESSURE
→ S007 selected-action staleness / pre-execution revalidation

NEW NUMBERED CASE
→ not justified

NEW PLANNER ACTION / BROADER AGENT ARCHITECTURE
→ not justified
```
