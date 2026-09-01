# B2/X1 R4-A4 — Pre-Implementation Design and LbD Entry

**Date:** 2026-09-01  
**Mode:** Learning-by-Doing + Planning/Design  
**Scope:** experiment-owned ordinary-Python R4-A4 transition/update/trace responsibility  
**Implementation:** STOPPED until the bounded A4 design decisions below are resolved  
**Product runtime integration:** not authorized

## 1. Controlling route

Primary plan:

`plans/B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`

Learning-depth companion:

`plans/B2_X1_R4_LBD_LEARNING_DEPTH_AND_REENTRY_MAP.md`

Procedure:

```text
UP-SKILL:upgradepilot-planning-design
+ UP-SKILL:upgradepilot-learning-by-doing
```

No new A4 plan is created. The selected implementation plan already owns the R4-A4 sequence/proof/stop line, and the learning-depth companion already owns the concepts to learn when they become material.

## 2. Entry evidence

The ordinary-Python seam before A4 is already established far enough to design the next transition responsibility:

```text
A1
→ bounded model-visible planner context + strict decision contract

A3
→ bounded local LM Studio request/response

A2
→ fresh deterministic rebinding/admission

real S001 composition
→ actual UpgradePilot product state feeds the planner boundary

live S001 proof
→ ACTION_SELECTED: acquire_exact_target_python_declaration
→ A2 admitted_action
→ capability_executed: False
```

Focused A1/A2/A3/composition family: 40/40 PASS at the recorded pre-A4 checkpoint.

A4 begins exactly after the admitted action/no-tool branch. It must not reopen the already-proved A1/A2/A3 responsibilities.

## 3. Mental model established in LbD

Current working model:

```text
A1 = OBSERVE
→ what bounded trusted state may the model see?

A3 = DECIDE
→ what investigation, if any, does the model propose next?

A2 = AUTHORIZE
→ is that proposal still currently permitted and exactly rebound to trusted authority?

A4 = ACT + INTERPRET + TRANSITION + TRACE
→ what actually happens after admission/no-tool, and what is the next trusted state?
```

For real S001:

```text
unresolved target-Python evidence gap
→ planner selects acquire_exact_target_python_declaration
→ A2 admits the exact trusted action
→ A4 reuses the existing target capability/domain path
→ new trusted investigation state
```

## 4. Important reuse boundary

A4 must **not** reimplement the existing target-side capability or Python-support domain semantics.

Existing product behavior already contains the vertical capability/domain path:

```text
repository_client.get_exact_head_text_file(...)
→ interpret_target_python_declaration(...)
→ TargetPythonDeclaration | TargetPythonDeclarationProblem
→ evaluate_target_python_relevance(...)
→ evaluate_python_support_drop_impact(...)
```

The new agentic responsibility is different:

```text
planner decides WHETHER the bounded investigation is useful now
→ A2 decides whether it is still authorized
→ A4 connects the admitted action to the existing HOW
→ existing domain owners interpret the result
→ A4 carries the resulting trusted state forward
```

The LLM does not choose repository, revision, path, parser, result family, or domain interpretation.

## 5. State-transition model established so far

Prefer immutable transition semantics:

```text
STATE 0
+ admitted/no-tool transition
+ execution/domain result when applicable
→ STATE 1
```

`STATE 0` remains unchanged. `STATE 1` represents the new current trusted state.

Reason:

```text
before state remains inspectable
→ exact change can be compared
→ transition reasoning can be explained
→ trace/replay is simpler and less ambiguous
```

Keep two responsibilities distinct:

```text
InvestigationState
→ what is true/current NOW

TransitionTrace
→ how and why we moved from one state to the next
```

Do not make every current-state object contain the entire historical trace by default.

## 6. Already-decided A4 constraints

Do not reopen these unless contrary evidence appears:

### Budget spending

R2 already decided:

```text
planning_budget.remaining_investigations
→ spent when fresh-admitted execution actually begins
```

Therefore A4 should implement that accepted timing rather than choose a new timing by preference.

### Product/runtime boundary

```text
R4-A remains experiment-owned
product runtime integration remains unauthorized
```

### Persistence boundary

Use the smallest trace/state representation justified by the experiment. Do not introduce a database, event sourcing, generalized workflow persistence, async orchestration, LangGraph, or a generic rule engine in A4 merely for future possibility.

### Bounded cross-case design pressure

S001 is the concrete implementation and teaching anchor for the first A4 vertical slice, but it is not sufficient by itself to freeze consequential A4 state/transition semantics.

For each material A4 design decision, use this proportional rule:

```text
1. understand the responsibility through S001
2. propose the smallest design that solves the real S001 responsibility
3. select only 1–3 existing real cases that are materially different for that decision
4. use those cases as design pressure / counterexamples
5. ask whether the proposed design still represents the same responsibility without case-specific assumptions
6. if yes, keep the smaller design
7. if no, refine only enough to cover the demonstrated real variation
8. implement the first bounded vertical slice on S001 unless later evidence changes that anchor
```

Case selection is **decision-specific**, not a standing requirement to reread the whole simulation corpus. Prefer cases that discriminate the exact open question—for example, a successful evidence result versus an already-attempted typed problem result for consumed-action semantics, or an action case versus a genuine no-tool case for routing/trace semantics.

This rule exists to obtain minimum useful generality from demonstrated real variation while avoiding both S001 overfitting and speculative generalization.

Do not:

```text
scan every historical case before each decision
→ not required

implement all pressure cases in the first A4 slice
→ not required

add generic abstractions for hypothetical future cases
→ not justified
```

## 7. Current unresolved design questions

These are the real pre-implementation decisions to resolve through LbD.

### D1 — smallest `InvestigationState`

Determine which current trusted facts A4 must carry between planner turns.

Candidate responsibilities include only what the next turn actually needs, such as:

```text
current product/domain assessment/propositions
consumed action IDs
remaining investigation budget
trusted target/repository identity needed by admission/execution
possibly the currently acquired typed evidence/results when they are required to derive or reuse trusted state
```

Do not duplicate complete `PublicPullRequestInvestigation` blindly and do not collapse current state into planner-visible context.

### D2 — typed execution/domain result ownership

Decide whether a typed result such as:

```text
TargetPythonDeclaration
TargetPythonDeclarationProblem
```

belongs in current `InvestigationState`, transition trace, or both by reference/field when required.

Decision criterion:

```text
what must be available to establish/reuse the next trusted domain state?
vs
what only needs to explain/replay the transition?
```

Do not store raw evidence merely because it exists.

### D3 — consumed-action semantics

Define when an action becomes consumed relative to execution start/result.

The likely invariant to test is that an exact investigation should not be repeatedly selected merely because its result was unfavorable or unresolved. But the precise rule must distinguish:

```text
fresh-admitted execution actually began
operational failure before meaningful attempt
valid typed domain/evidence problem result
successful evidence result
```

Apply the bounded cross-case pressure rule here: S001 supplies the successful-evidence path, while an existing repeat-guard/problem-outcome case should pressure-test whether a valid typed problem result still consumes the exact investigation without falsely establishing the target proposition.

This remains open until we trace the existing result/failure boundaries precisely.

### D4 — no-tool transition

Define the smallest state/trace behavior for:

```text
QUESTION_SETTLED
KNOWN_INVESTIGATION_OUTSIDE_CURRENT_BOUNDARY
NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
```

No-tool must execute no capability. It still needs a coherent transition/trace outcome without inventing a fake action result.

Apply the bounded cross-case pressure rule using one or more existing genuine no-tool cases only when they discriminate the exact routing/trace decision; do not broaden into full product-simulation review.

### D5 — execution seam

Find the smallest experiment-owned callable/seam that can execute **only the already-admitted action** by reusing existing product capabilities, without rerunning `investigate_public_pull_request()` from the beginning and without moving product-owned semantics into `experiments/`.

This is likely the first source-placement/design question that will drive implementation.

### D6 — trace/replay minimum

Define only enough deterministic trace to answer:

```text
what state entered the transition?
what decision/admission branch occurred?
what action/result occurred, if any?
what state resulted?
why can the transition be reproduced/compared?
```

Do not design a generalized event-sourcing system.

## 8. First implementation candidate — not yet authorized by this design record

Once D1–D6 are sufficiently resolved, the smallest ordinary-Python A4 increment should likely prove one real vertical transition:

```text
S001 pre-target state
→ admitted acquire_exact_target_python_declaration
→ existing target acquisition/interpreter/domain evaluation
→ immutable next investigation state
→ consumed/budget update according to accepted semantics
→ one deterministic transition trace
→ STOP before automatic multi-turn looping if not yet needed
```

The exact source/type shape remains intentionally undecided until the design questions above are resolved.

## 9. Learning targets for this slice

Learn only as they become real in the design/implementation:

```text
state machine / transition model
planner state vs execution state
immutable state replacement
execution result vs domain interpretation
consumed-action semantics
trace/event record design
replay/deterministic comparison
operational failure vs typed domain/evidence problem
```

Defer:

```text
event sourcing / database persistence
async/concurrency
large orchestration frameworks
generic state-machine framework
advanced replay infrastructure
```

## 10. Proof and stop line

Before source implementation, A4 design is ready only when:

```text
smallest current-state responsibility is clear
+ typed execution/domain result ownership is clear enough
+ consumed-action semantics are explicit
+ no-tool behavior is explicit
+ existing target/domain capability reuse seam is identified
+ minimum trace/replay contract is clear
+ consequential A4 decisions have survived the smallest materially different real-case pressure needed to rule out S001-specific assumptions
```

Then hand off from Planning/Design to Build/Implement for one bounded vertical increment.

Until then:

```text
NO A4 source implementation
NO product runtime integration
NO generalized agent loop
NO persistence/framework expansion
NO broad case-corpus review merely for completeness
```

This working memory preserves the dated A4 design/LbD entry. `MEMORY.md` remains the sole live-position owner.