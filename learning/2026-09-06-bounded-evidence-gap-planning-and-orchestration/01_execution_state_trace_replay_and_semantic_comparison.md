# Bounded Evidence-Gap Execution, State Consequences, Trace/Replay, and Semantic Comparison

**Learning-artifact date:** 2026-09-06  
**Source/test/framework evidence horizon:** `main@d9c637b6df4d9449683d7f67d8859a4e18fd132f`  
**Roadmap coordination:** Group 12 of `../../plans/UPGRADEPILOT_WHOLE_PROJECT_LEARNING_ARTIFACT_ROADMAP_PLAN.md`, extended immediately before authoring at commit `9e0c4f05ab11c4412672813b5ad0b2da3b8d003d`  
**Artifact role:** new frozen learning snapshot that **complements** the September 1 EvidenceGapPlanner notes and the September 2 target-Python evidence note; it does not rewrite those historical snapshots  
**Target depth:** **must master / own** execution-state semantics, authority/effect boundaries, semantic-vs-operational outcome meaning, trace/replay, and framework-neutral comparison; understand exact Python/dataclass/test syntax operationally

This note answers two connected questions:

> **After an evidence-gap action has been proposed and deterministically admitted, how does UpgradePilot execute one bounded investigation and update trusted state honestly?**

and later:

> **How can that ordinary-Python behavior be compared fairly with a different orchestration architecture without forcing both implementations to share the same internal classes or control flow?**

The shortest mental model is:

```text
proposal
→ current deterministic authority
→ one bounded effect
→ semantic result OR operational failure
→ deterministic state consequence
→ inspectable trace
→ replay without external re-execution

then, for implementation comparison:

implementation A ─→ semantic projection ─┐
                                        ├→ compare accepted behavior
implementation B ─→ semantic projection ─┘
```

---

## 1. Why this artifact exists

The September 1 planner learning snapshots deliberately stopped before the complete execution/update responsibility. They already taught:

```text
bounded model observation
→ local model call
→ untrusted structured decision
→ fresh deterministic action admission
```

They did **not** yet teach the complete next responsibility:

```text
already-admitted action
→ external acquisition
→ product/domain interpretation
→ next trusted orchestration state
→ proof of the transition
```

That missing slice was later implemented in ordinary Python and became the control/reference for the LangGraph comparison.

The target-Python interpretation itself is already taught separately in:

`../2026-09-02-target-python-evidence-resolution/01_TARGET_PYTHON_EVIDENCE_RESOLUTION_CHAIN.md`

This note therefore focuses on the **orchestration/state/proof responsibility around that product-owned capability**, not on reteaching Python specifier semantics.

---

## 2. The ordinary-Python execution responsibility

Current source:

```text
experiments/evidence_gap_investigation_transition.py
```

The central function is:

```python
run_evidence_gap_transition(...)
```

It starts **after deterministic action admission**.

That boundary matters:

```text
model decision
!= execution authority

run_evidence_gap_transition(...)
!= action admission
```

For an action-selected path, the intended control flow is:

```text
EvidenceGapInvestigationState
+
EvidenceGapDecision
+
AdmittedInvestigationAction
+
repository client
        ↓
exact authorized repository read
        ↓
interpret_target_python_declaration(...)
        ↓
semantic/domain result
        ↓
evaluate_target_python_relevance(...)
        ↓
evaluate_python_support_drop_impact(...)
        ↓
new immutable EvidenceGapInvestigationState
        ↓
EvidenceGapTransitionTrace
```

For a no-action decision:

```text
no external effect
→ only bounded continuation status changes
→ transition trace still records before/decision/after
```

The module intentionally supports only the one currently admitted real investigation capability:

```text
acquire_exact_target_python_declaration
```

A generic executor registry was deferred because there was no second real action demonstrating that such an abstraction was needed.

### Learning principle

> **Do not generalize the execution mechanism before product capability diversity earns the abstraction.**

---

## 3. The evolving state is small on purpose

`EvidenceGapInvestigationState` carries only the bounded orchestration facts needed across one planner/execution loop:

```text
python_support_assessment
consumed_actions
remaining_investigations
continuation_status
```

This is not a copy of all product evidence.

The product/domain assessment remains product-owned. The experiment adds only the orchestration state it genuinely needs.

The class is a frozen dataclass, and state updates use `dataclasses.replace(...)` rather than mutating the old value in place.

Conceptually:

```text
before_state
→ deterministic consequence
→ new after_state
```

not:

```text
shared object
→ mutate several fields invisibly
→ hope callers know what changed
```

### Why immutability helped here

It made three things easier to reason about:

- exact before/after proof;
- trace recording;
- deterministic replay comparison.

Immutability is useful here because it supports the actual proof responsibility. It is not a rule that every UpgradePilot object must always be immutable.

---

## 4. The most important state semantics

The execution work exposed one of the most important distinctions in the planner experiment:

```text
budget spent
!=
action consumed
```

The outcome determines both independently.

### 4.1 Valid semantic result

Examples:

```text
TargetPythonDeclaration(state="available", requires_python=...)
```

or a typed target-domain problem such as:

```text
requires_python_absent
```

These are both **valid semantic outcomes** of performing the admitted investigation.

Current consequence:

```text
external investigation occurred
→ budget decreases by 1
→ action becomes consumed
→ target/domain assessment is reevaluated from the semantic result
```

Why consume the action even when the semantic result is unresolved?

Because the investigation successfully answered:

> What does the exact target evidence say under this admitted method?

The answer can legitimately be “the declaration is absent/unresolved.” Repeating the same exact read does not become useful merely because the semantic answer was inconvenient.

### 4.2 Expected operational acquisition failure

Examples:

```text
GitHubAcquisitionError(reason="timeout")
GitHubResponseError(...)
```

Current consequence:

```text
attempt consumed the bounded investigation budget
→ remaining budget decreases by 1
→ action is NOT marked consumed
→ domain assessment remains unchanged
→ operational failure is preserved in the trace
```

The failure did not produce valid target evidence, so the system must not pretend that the semantic question was answered.

### 4.3 No-action decision

Examples:

```text
QUESTION_SETTLED
KNOWN_INVESTIGATION_OUTSIDE_CURRENT_BOUNDARY
NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
```

Current consequence:

```text
no external acquisition
→ no budget spend
→ no action consumption
→ product/domain assessment unchanged
→ continuation status changes deterministically
```

### 4.4 Fresh authority rejection

This happens **before** the execution-transition function.

Examples include:

```text
action already consumed
budget exhausted
action identity stale
action no longer actionable
```

Consequence:

```text
model proposal exists
→ current deterministic authority rejects it
→ no external effect
→ current trusted baseline remains authoritative
```

This protects the time-of-check-to-time-of-use boundary:

```text
useful when model observed state at planning time
!=
automatically executable after the model returns
```

---

## 5. Semantic problem vs operational failure

This distinction is easy to lose and should be retained permanently.

```text
valid semantic/domain problem
!=
operational/provider failure
```

A target result such as:

```text
requires_python_absent
```

means:

> The admitted exact evidence was acquired and interpreted, and its semantic state is that no usable declaration was established.

A timeout means:

> The evidence acquisition did not complete, so the target proposition was not semantically resolved by this attempt.

That difference drives state consequences:

```text
semantic result
→ consume action
→ update/re-evaluate domain state

operational failure
→ do not consume action
→ preserve domain state
```

The same principle later had to be preserved during implementation comparison: provider/model failures were not allowed to reuse repository operational-failure fields merely because both were “errors.”

### Transfer lesson

When designing agentic systems, classify failures by **what responsibility failed**, not by whether the final path was unhappy.

---

## 6. `EvidenceGapTransitionTrace`: proof of one transition

The ordinary-Python control records:

```text
before_state
decision
admitted_action | None
execution_result | None
operational_failure | None
after_state
```

The trace therefore answers:

```text
what state did we start from?
what did the model propose?
what exact action had already been admitted?
what did execution actually produce?
what state consequence followed?
```

It is more than a debug log because its fields participate in deterministic reconstruction.

But it is not product persistence and it is not event sourcing for the whole application.

---

## 7. Replay is reconstruction, not re-execution

Current function:

```python
replay_evidence_gap_transition(trace)
```

Replay consumes the already-recorded transition facts and derives the expected after-state again.

It deliberately does **not** call:

```text
LM Studio
GitHub
```

Mental model:

```text
recorded decision + recorded execution outcome + recorded before state
→ deterministic consequence logic
→ reconstructed after state
```

Then the test can assert:

```python
replay_evidence_gap_transition(trace) == trace.after_state
```

### Keep these terms separate

```text
trace
→ what happened in one transition

replay
→ reconstruct deterministic consequences from recorded facts

re-execution
→ perform external/model work again
```

These are not interchangeable.

---

## 8. The focused ordinary-Python tests

Current test owner:

```text
experiments/tests/test_evidence_gap_investigation_transition.py
```

The seven focused tests protect discriminating propositions rather than every line of implementation.

Important cases include:

```text
valid target result
→ domain updated
→ action consumed
→ budget spent
→ replay equivalent

typed target problem
→ still valid semantic result
→ action consumed
→ domain reevaluated

timeout
→ operational failure
→ budget spent
→ action not consumed
→ domain unchanged

untrusted provider response
→ operational failure
→ not semantic evidence

explicit no-action outcomes
→ no effect
→ only continuation status changes

action execution without prior admission
→ rejected

terminal state attempting another transition
→ rejected
```

The complete ordinary-Python focused family later reached:

```text
47/47 PASS
```

That proof includes the earlier planner/model/admission/composition responsibilities as well as execution/state transition.

---

## 9. Real pydantic ordinary-Python transition

Representative real case:

```text
repository: pydantic/pydantic
pull request: #13432
dependency: soupsieve 2.6 → 2.8.4
upstream Python-support drop: Python 3.8
selected investigation: acquire_exact_target_python_declaration
```

The real ordinary-Python control established:

```text
ACTION_SELECTED
→ deterministic current admission
→ exact PR-head pyproject.toml read
→ requires-python >=3.10
→ dropped Python 3.8 outside target declared range
→ applicability established_not_applicable
→ remaining investigations 1 → 0
→ action added to consumed_actions
→ deterministic replay equivalent
```

This was important because it moved the experiment beyond mocked fixtures while still staying outside product-runtime integration.

### What this did not prove

```text
one pydantic case
!= general planner quality
!= multi-action generality
!= production reliability
!= automatic multi-turn orchestration
!= framework adoption
```

---

## 10. The next comparison problem: different architecture, same responsibility

After the ordinary-Python control was complete, LangGraph was implemented independently.

That immediately creates a comparison problem:

```text
ordinary Python has:
EvidenceGapInvestigationState
EvidenceGapTransitionTrace
functions / branches

LangGraph has:
graph-owned State
node outcomes
routing
final graph result
```

A bad comparison would require:

```text
ordinary-Python internal object == LangGraph internal object
```

That would reward architectural copying rather than semantic correctness.

The adopted comparison rule became:

> **Compare the accepted externally meaningful semantics, not implementation representation.**

---

## 11. `EvidenceGapSemanticProjection`

Current comparison owner:

```text
experiments/evidence_gap_implementation_semantic_comparison.py
```

Both implementations are projected into one small evaluation-only representation:

```text
EvidenceGapSemanticProjection
```

It includes only behavior relevant to the bounded responsibility:

```text
planner outcome
action id
authority status / rejection reason
whether an external effect was attempted
outcome kind
remaining investigation budget
consumed actions
continuation status
investigation semantic state
target relevance state
final applicability state
operational failure type / reason
```

It intentionally does **not** compare:

```text
node count
function count
state class identity
trace class identity
module layout
exact explanation wording
```

### Central equation

```text
semantic equivalence
!=
implementation equality
```

This pattern is transferable to:

- legacy-vs-rewrite comparisons;
- framework migrations;
- parser replacements;
- service/backend migrations;
- alternative orchestration engines.

---

## 12. Why the projection is evaluation machinery, not product state

`EvidenceGapSemanticProjection` imports both implementation result families because it sits **outside** them as a comparison bridge.

Its job is:

```text
implementation-specific result
→ normalized accepted semantics
```

It is not a new product-domain model and should not become the runtime state merely because it is convenient for tests.

This ownership distinction prevents test/comparison convenience from becoming architecture authority.

---

## 13. The four controlled semantic comparison scenarios

Current test owner:

```text
experiments/tests/test_evidence_gap_implementation_semantic_comparison.py
```

The comparison intentionally uses four discriminating cases.

### Case 1 — no action

```text
QUESTION_SETTLED
→ no authority needed
→ no repository effect
→ same continuation consequence
```

Question answered:

> Do both implementations mean the same thing when planning terminates without execution?

### Case 2 — fresh current-state rejection

```text
model proposes action
→ current state says action already consumed
→ authority rejects
→ no repository effect
→ current baseline preserved
```

Question answered:

> Do both implementations protect the same post-model execution-authority boundary?

### Case 3 — authorized semantic success

Both receive the same controlled file:

```toml
[project]
name = "demo"
requires-python = ">=3.10"
```

Question answered:

> Given the same admitted effect and semantic evidence, do both produce the same target relevance, applicability, budget, consumption and continuation consequences?

### Case 4 — expected repository timeout

Both receive the same `GitHubAcquisitionError(reason="timeout")`.

Question answered:

> Do both distinguish operational failure from semantic evidence and apply the same budget/consumption/domain consequence?

Observed result:

```text
4/4 PASS
```

---

## 14. One subtle comparison correction worth retaining

While the comparison projection was being built, provider/model problems were initially at risk of being represented using repository operational-failure fields.

That would have collapsed two different responsibilities:

```text
planner/provider failed before usable decision
!=
repository acquisition failed after an authorized action
```

The projection was corrected before the comparison tests were finalized.

This is a useful general lesson:

> **Normalization should remove irrelevant representation differences, not erase meaningful semantic distinctions.**

A common comparison model is valuable only if it remains semantically honest.

---

## 15. Controlled proof vs real smoke proof

These prove different things.

### Controlled tests

Good for:

```text
hold inputs constant
force rare failure branches
prove forbidden calls do not occur
compare exact semantic consequences
run quickly/repeatedly
```

### Real smoke

Good for:

```text
real provider/model wiring
real repository acquisition
real product-owned case/evidence
real import/runtime/dependency integration
```

Therefore:

```text
controlled semantic comparison PASS
+
real smoke PASS
```

is stronger than either one alone.

But even both together remain bounded evidence, not production-readiness proof.

---

## 16. Engineering progression worth remembering

The learning value is not the exact historical labels. It is the change in understanding:

```text
planner/model/admission seam existed
→ but execution/state consequence was still missing

bounded ordinary-Python transition added
→ semantic vs operational consequences became explicit
→ trace/replay created deterministic proof

ordinary Python became a real control/reference
→ framework comparison became meaningful

independent LangGraph representation appeared
→ raw internal equality was no longer a valid oracle

framework-neutral semantic projection added
→ architectures could stay different while accepted behavior stayed comparable
```

The transferable lesson is:

> **First make one implementation semantically complete enough to serve as evidence. Then compare another implementation through a shared behavioral contract, not by turning the first implementation into the second one's architecture specification.**

---

## 17. What to master vs what to look up

### Must master / own

```text
proposal != execution authority
post-model current-state authorization
budget spent != action consumed
semantic result != operational failure
no-action has explicit lifecycle semantics
immutable before → after transition reasoning
trace != replay != re-execution
semantic equivalence != implementation equality
comparison projection is evaluation machinery, not product truth
controlled proof != real smoke proof
```

### Understand operationally

```text
frozen dataclasses
dataclasses.replace(...)
Literal / union result types
Mock call assertions
try/except → typed operational failure
one-transition state machine
framework-neutral projection helpers
```

### Lookup-level

```text
exact dataclass/typing syntax
all unittest fixture construction
JSON diagnostic rendering details
provider library internals
```

### Deferred deliberately

```text
persistent event sourcing
concurrent transitions
multi-action executor registry
durable workflow recovery
automatic multi-turn planner loop
```

Those require a real product responsibility before deeper study/building.

---

## 18. Proof boundaries at this snapshot

Established:

```text
ordinary-Python bounded execution/state transition is implemented
focused transition tests are green
combined ordinary-Python family reached 47/47 PASS
real pydantic ordinary-Python transition succeeded
trace replay reconstructs deterministic after-state without external I/O
ordinary Python and LangGraph match on four controlled semantic scenarios
comparison does not require shared internal representations
```

Not established:

```text
every possible branch across both implementations is equivalent
multi-action planning quality
automatic replanning
product-runtime integration
production reliability
framework superiority
```

---

## 19. Fast relearning route

When returning weeks later:

```text
1. Recall: budget spent != action consumed.
2. Open EvidenceGapInvestigationState + run_evidence_gap_transition(...).
3. Trace one semantic success and one timeout through after-state rules.
4. Open EvidenceGapTransitionTrace + replay_evidence_gap_transition(...).
5. Explain trace vs replay vs re-execution.
6. Open EvidenceGapSemanticProjection.
7. Read the four semantic-comparison test names and state the proposition each protects.
8. Explain why internal state/topology equality would be a bad framework-comparison oracle.
```

---

## 20. Ownership / transfer questions

Without looking at the note:

1. Why does a typed `requires_python_absent` result consume the action while a GitHub timeout does not?
2. Why does the timeout still spend investigation budget?
3. What would be dangerous about calling GitHub again during replay?
4. Why is a trace useful even when tests are green?
5. Which fields belong in a semantic comparison projection, and which implementation details should be excluded?
6. If a new framework uses tasks instead of graph nodes, how would you compare it fairly with the current implementations?
7. Why would using `EvidenceGapSemanticProjection` as product runtime state be an ownership mistake?

Transfer exercise:

> Imagine a future second investigation action produces a valid semantic result that still leaves its target proposition unresolved. Decide independently whether the action should be consumed, whether budget should be spent, and what evidence you would need before generalizing the current rule.

---

## 21. Source, test, and history anchors

Current source/test anchors at the pinned horizon:

```text
experiments/evidence_gap_investigation_transition.py
experiments/tests/test_evidence_gap_investigation_transition.py

experiments/evidence_gap_implementation_semantic_comparison.py
experiments/tests/test_evidence_gap_implementation_semantic_comparison.py
```

Prerequisite/reuse learning snapshots:

```text
learning/2026-09-01-b2-x1-r4-evidence-gap-planner/
learning/2026-09-02-target-python-evidence-resolution/
```

Directly relevant historical evidence:

```text
working-memory/2026-09-02_B2-X1-R4A4-runtime-lbd-and-reconciliation-closure.md
working-memory/2026-09-06_B2-X1-R4B6-controlled-semantic-comparison-build.md
```

The old execution-coordinate names above are preserved only because they are exact historical filenames. They are not current learning vocabulary.

This artifact is a frozen educational snapshot. It does not authorize product/framework integration and does not claim learner mastery merely because the note exists.
