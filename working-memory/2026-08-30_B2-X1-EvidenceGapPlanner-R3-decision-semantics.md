# B2/X1 EvidenceGapPlanner R3 — Decision Semantics

**Date:** 2026-08-30  
**Status:** R3 SEMANTIC SLICE COMPLETE — decision-kind meanings frozen before wire/schema design  
**Plan:** `../plans/B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`  
**Previous stage:** R2 COMPLETE / PASS

## 1. Question

What semantic decisions may `EvidenceGapPlanner` make before we choose the exact JSON/schema representation?

Do not let historical short names or historical schema fields determine the new semantic contract.

## 2. Historical evidence

Historical planner vocabulary:

```text
choose_action
stop
defer
unresolved
```

E5 clarified that no-tool is not one meaning:

```text
stop
→ bounded question sufficiently settled / no further justified work

defer
→ useful next investigation is known but outside current admitted action/support boundary

unresolved
→ evidence remains non-final and no supported action or known outside capability is justified
```

R2 final synthesis exposed an important historical overload:

`d-repeat-stop` still has a materially unresolved proposition, but the already-consumed A1 investigation should not be repeated. Calling that state `QUESTION_SETTLED` would be semantically false.

Therefore historical `stop` does not map one-to-one to the evidence-refined vocabulary.

## 3. Final candidate decision kinds for the current seam

Use:

```text
ACTION_SELECTED
QUESTION_SETTLED
KNOWN_INVESTIGATION_OUTSIDE_CURRENT_BOUNDARY
NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
```

This supersedes the R1 working name:

```text
KNOWN_INVESTIGATION_NOT_ADMITTED
```

because `not admitted` collides linguistically with the separate deterministic admission lifecycle. A useful outside-boundary investigation may be identified before any concrete action proposal is submitted to admission.

## 4. Exact meanings

### `ACTION_SELECTED`

Meaning:

> One currently offered `EvidenceGapActionDescriptor` has useful discriminating value for the bounded planning question, so the model proposes that exact `action_id` for fresh deterministic admission.

Properties:

- requires one selected `action_id`;
- selection is a proposal, never execution authority;
- the model does not redefine target proposition, locator, preconditions, mutation policy, result classes or execution arguments;
- deterministic code must rebind and revalidate the exact hidden action before execution.

### `QUESTION_SETTLED`

Meaning:

> The current trusted evidence state is sufficient for the bounded planning question such that no additional investigation is justified merely to answer that question.

Properties:

- no action ID;
- not a synonym for `budget exhausted`;
- not a synonym for `the useful action was already consumed`;
- not a synonym for `we do not currently know what to do`;
- S004 is the current clean development example.

### `KNOWN_INVESTIGATION_OUTSIDE_CURRENT_BOUNDARY`

Meaning:

> The bounded question remains materially non-final, and a specific useful investigation/responsibility is identifiable, but UpgradePilot does not currently expose that investigation as an admitted action inside this planner boundary.

Properties:

- no action ID;
- corresponds to the useful semantic core of historical `defer`;
- S006's identified discriminating two-version behavioral check is the current development example;
- does not mean a currently offered action was selected and then rejected by deterministic admission;
- does not mean a transient provider failure;
- does not mean a consumed action should simply be repeated;
- future outside-boundary examples may include useful behavioral reproduction or another independently justified capability before a safe/admitted executor exists.

Why the name changed from `KNOWN_INVESTIGATION_NOT_ADMITTED`:

```text
"not admitted"
→ sounds like deterministic admission already rejected a concrete action

"outside current boundary"
→ says the useful investigation exists conceptually but is not part of this planner's current action space
```

This is a naming/ownership clarification, not a new product capability.

### `NO_JUSTIFIED_INVESTIGATION_IDENTIFIED`

Meaning:

> The bounded question remains materially non-final, but the current trusted state does not identify a useful currently offered action or a specific useful investigation outside the current boundary.

Properties:

- no action ID;
- covers genuine conflict/uncertainty with no justified next investigation;
- may also cover a consumed-action state where the previous action cannot usefully be repeated and no different justified investigation is identified;
- does not claim no investigation exists anywhere in reality; it only states what the current trusted state identifies.

Current examples:

```text
d-conflict
→ conflicted evidence + no admitted/known outside resolving capability
→ NO_JUSTIFIED_INVESTIGATION_IDENTIFIED

d-repeat-stop (evidence-refined interpretation)
→ proposition remains unresolved
→ A1 consumed / no useful repeat
→ no different justified investigation identified
→ NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
```

## 5. Historical mapping is intentionally non-bijective

```text
choose_action
→ ACTION_SELECTED

defer
→ KNOWN_INVESTIGATION_OUTSIDE_CURRENT_BOUNDARY

unresolved
→ NO_JUSTIFIED_INVESTIGATION_IDENTIFIED

historical stop
→ QUESTION_SETTLED
   when the bounded question is actually settled

historical stop
→ NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
   when the question remains unresolved but no justified work remains identifiable
```

Therefore the new contract should not preserve historical case names/expected labels mechanically.

## 6. No-tool remains an umbrella branch

```text
NO-TOOL
├── QUESTION_SETTLED
├── KNOWN_INVESTIGATION_OUTSIDE_CURRENT_BOUNDARY
└── NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
```

This is valuable because:

```text
action_id = null
```

alone cannot explain whether:

- the question is done;
- a known useful investigation exists but is outside the current planner boundary; or
- the question remains open with no justified investigation currently identified.

Those states imply different future behavior, product reporting, evaluation meaning and possible reactivation triggers.

## 7. Budget exhaustion is not a model decision kind

Do not add a first-seam model value such as:

```text
BUDGET_EXHAUSTED
```

The planning budget is trusted orchestration/control state, not an epistemic conclusion.

If:

```text
remaining_investigations <= 0
```

then deterministic orchestration should normally prevent a new investigation execution and may avoid an unnecessary planner call entirely.

A future product may expose a separate orchestration/status result for a blocked/exhausted run, but that should not be confused with what the LLM believes about the evidence question.

This keeps:

```text
planner semantic decision
!= orchestration resource status
```

## 8. Provider/execution failure is not a decision kind

Do not add model decision kinds for:

```text
timeout
rate limit
transport error
untrusted provider response
```

Those remain provider/executor/control-plane states.

After deterministic handling, a later planner turn should receive the resulting trusted proposition/planning-evidence/catalog state—not raw transport failure as a substitute for semantic decision state.

## 9. Decision kind does not grant truth or authority

Even no-tool decisions remain model reasoning outputs.

```text
QUESTION_SETTLED
!= final compatibility/safety/merge truth

ACTION_SELECTED
!= execution authorization
```

The decision is interpreted inside the bounded EvidenceGapPlanner responsibility only.

## 10. R3 next slice — wire shape + admission

Now freeze the smallest structured representation and deterministic admission behavior.

Strong candidate:

```text
EvidenceGapDecision
    decision_kind
    action_id | null
    explanation
```

Questions for the next slice:

1. fixed three-field object vs tagged-union schema;
2. `ACTION_SELECTED` must require non-null action ID;
3. all no-tool kinds must require null/no action ID;
4. remove historical model echoes:
   - `target_proposition`;
   - `expected_result_categories`;
   - `limitations`;
5. define fresh deterministic admission/rebinding checks without relying on model-echoed authority metadata;
6. decide the clean separation between:
   - parsing/shape validity;
   - no-tool semantic result;
   - action admission;
   - admission problem/control-plane result.

No R4 implementation begins until that contract passes.

## 11. LbD concepts earned

- semantic enum design before wire/schema design;
- overloaded historical state vs responsibility-oriented state;
- no-tool/abstention taxonomy;
- epistemic state vs orchestration/control state;
- semantic defer vs deterministic admission rejection;
- why naming collisions reveal ownership ambiguity;
- non-bijective migration from historical vocabulary;
- keeping provider failure outside planner semantics.
