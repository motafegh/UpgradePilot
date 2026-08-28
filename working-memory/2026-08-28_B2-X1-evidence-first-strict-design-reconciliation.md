# B2/X1 Evidence-First Strict-Design Reconciliation

**Date:** 2026-08-28  
**Status:** INITIAL RECONCILIATION COMPLETE — FIRST-SEAM CANDIDATE NARROWED; FRESH EVALUATION PROTOCOL REQUIRED BEFORE FINAL PILOT DISPOSITION  
**Parent exploration:** `2026-08-28_B2-X1-evidence-first-llm-risk-and-design-exploration.md`  
**Evidence records:** E1 support-drop semantic probes; E2 state-origin/projection; E3 minimally constrained S001 planner; E4 incremental controls/admission; E5 no-tool dispositions  
**Historical accepted plan/protocol retained:** `../plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md`, `../plans/B2_X1_PHASE3_EVALUATION_PROTOCOL.md` (`b2-x1-phase3a-v2`)

## 1. Why reconciliation is now justified

The evidence-first route was created to avoid either blindly preserving every earlier guardrail or removing controls by intuition.

The initial discriminating sequence is now complete enough for the first planner seam:

```text
E1
→ current support-drop semantic boundary handled selected negation/future/instruction-shaped probes
→ deterministic grounding still does not independently prove English semantics

E2
→ real S001 nested assessment carries raw changelog prose
→ small proposition/action projection does not
→ semantic carryover remains distinct from raw-text carryover

E3
→ typed real S001 state alone was enough for correct next-gap reasoning

E4.1
→ adding one trusted action descriptor produced exact action-id binding

E4.2
→ adding JSON Schema preserved the decision and made output machine-readable

E4.3
→ deterministic admission admitted the valid proposal and rejected unknown/stale proposals

E5
→ STOP / DEFER / UNRESOLVED remained correctly distinguishable with only disposition + explanation
```

The purpose of this record is therefore not another design brainstorm. It classifies the prior strict design against observed evidence.

## 2. Reconciliation rule

Use four dispositions:

```text
RETAIN
→ evidence-backed or clearly required by reachable consequence

SIMPLIFY
→ responsibility is real, but the old representation makes the model carry redundant fields/authority

DEFER
→ potentially useful, but not yet required or evidenced for the first seam

REMOVE FROM FIRST SEAM
→ current projection/authority design makes this unnecessary at the first planner boundary
```

This classification applies to the **first bounded planner seam**, not every possible future planner.

## 3. RETAIN

### 3.1 Trusted bounded planning question

**Disposition: RETAIN.**

The model needs to know which responsibility it is advancing. E3/E5 both relied on a bounded planning question to distinguish material gaps from adjacent unresolved facts.

The question remains trusted configuration and must not contain the oracle/expected answer.

### 3.2 Typed proposition projection

**Disposition: RETAIN.**

E2/E3 directly support using typed proposition state instead of serializing the whole product object graph.

This projection:

- keeps the planner focused on epistemic state;
- avoids the observed raw tagged-changelog quote at the first seam;
- still preserves semantic carryover honestly when a prior model influenced a proposition.

### 3.3 Closed trusted action catalog

**Disposition: RETAIN.**

E4.1 showed a concrete role:

```text
correct conceptual reasoning
+ trusted action descriptor
→ exact known capability identity
```

The catalog remains deterministic authority. The model may select an action ID but may not create executable authority.

### 3.4 Pre-bound exact action identity/locator

**Disposition: RETAIN internally.**

Repository, immutable revision, path, mutation class, result families, target proposition, cost class, and action preconditions remain deterministic action-owner state.

Whether every one of these fields must remain **model-visible** is not established; see DEFER. But they must not become model-created authority.

### 3.5 Minimal JSON Schema structured output

**Disposition: RETAIN, simplified shape.**

E4.2 demonstrated a real integration benefit: the same correct decision arrived in directly parseable typed form.

Do not credit JSON Schema with reasoning quality. Its responsibility is output shape / parsing reliability.

### 3.6 Deterministic admission before capability execution

**Disposition: RETAIN.**

E4.3 directly demonstrated:

```text
unknown action ID
→ reject

previously-correct action against stale trusted state
→ reject

current valid proposal
→ admit exact read-only capability
```

Admission therefore earns execution-time catalog/state/precondition revalidation.

### 3.7 STOP / DEFER / UNRESOLVED semantic distinction

**Disposition: RETAIN.**

E5 showed that all three meanings are operationally distinct and model-understandable:

```text
STOP
→ bounded question settled / no more justified work

DEFER
→ useful next responsibility known but outside current action/support boundary

UNRESOLVED
→ evidence remains insufficient/conflicted with no justified supported or identified outside capability
```

Collapsing them to a single null action would lose useful loop state.

### 3.8 Attempt history and remaining-step/budget state

**Disposition: RETAIN as trusted state.**

The old protocol contains repeat-stop and budget semantics. E4.3 establishes the value of fresh-state revalidation, and these fields are needed to prevent blind repeat/exhausted execution even if they have not all been separately pressure-tested in E3–E5.

### 3.9 Oracle isolation / protected-vs-development separation

**Disposition: RETAIN.**

This is evaluation validity, not planner safety ceremony. Expected outputs, protected labels, and grader metadata must remain outside model input.

### 3.10 Local-only no-proxy model transport

**Disposition: RETAIN for this checkpoint.**

It is the selected deployment/evaluation boundary and has already prevented real ambient-proxy contamination. It is not a model-reasoning guardrail.

## 4. SIMPLIFY

### 4.1 Model result object

**Old shape:**

```text
state
selected_action_id
target_proposition
reason
expected_result_categories[]
limitations[]
```

**Disposition: SIMPLIFY.**

E4.2/E4.3 showed that the model does not need to echo trusted action metadata in order to select and safely admit an action. E5 showed no-tool semantics can remain explicit without those fields.

Evidence-backed candidate first-seam output:

```text
state = choose_action | stop | defer | unresolved
action_id = trusted action ID | null
explanation = non-empty text
```

Structural rule:

```text
choose_action
→ action_id must be non-null

stop | defer | unresolved
→ action_id must be null
```

Trusted code rebinds action-owned target proposition/result families/locator/preconditions after action lookup.

This three-field representation is preferred over two unrelated schemas because it preserves one stable parser/record while remaining substantially smaller than the old result object.

### 4.2 Model echo of target proposition

**Disposition: REMOVE FROM MODEL OUTPUT / rebind deterministically.**

The action already owns its target proposition. E4.3 successfully rebound it before admission.

No evidence currently shows value in asking the model to repeat the same identifier so deterministic code can compare the echo.

### 4.3 Model echo of expected result families

**Disposition: REMOVE FROM MODEL OUTPUT / rebind deterministically.**

The action owner already defines `TargetPythonDeclaration | TargetPythonDeclarationProblem` for A1. The model choosing an action does not need authority to redefine or restate those families.

### 4.4 Model-emitted limitations array

**Disposition: REMOVE FROM FIRST-SEAM OUTPUT.**

Proof limits remain important, but current evidence does not show that a model-authored limitations list is the right authority or necessary integration field.

Prefer deterministic/product-owned proof-strength boundaries plus one bounded model explanation. Human/evaluation review can still reject an explanation that overclaims.

### 4.5 Human semantic review rubric

**Disposition: SIMPLIFY, not remove.**

The old seven-item reason/limitations rubric mixes semantic correctness, proof boundaries, and metadata/authority checks that deterministic design now prevents structurally.

A future fresh protected protocol should keep only decision-changing semantic checks, for example:

1. correct state/action for the planning question;
2. explanation identifies the material evidence gap or stopping reason;
3. missing/conflicted evidence is not converted into a stronger fact;
4. explanation does not claim runtime/safety/merge/mutation authority outside the seam.

Exact rubric belongs to the fresh protocol, not this working record.

## 5. REMOVE FROM FIRST SEAM

### 5.1 Raw / near-raw upstream evidence in planner input

**Disposition: REMOVE FROM FIRST SEAM.**

E2 showed the first S001 planner decision can be projected without raw tagged-changelog prose.

Do not serialize the nested `PythonSupportDropImpactAssessment` or source quotes merely because they exist internally.

### 5.2 `untrusted_evidence_notes` as a normal first-seam planner field

**Disposition: REMOVE FROM FIRST SEAM.**

The initial strict contract deliberately added this field to pressure prompt-injection behavior. E2 showed that the known upstream raw-text route can be eliminated by projection before the planner.

Keeping a synthetic untrusted-text channel merely to test whether the model resists it would manufacture exposure that the first product seam does not need.

If a later planner responsibility genuinely needs raw/near-raw evidence, reassess then.

### 5.3 Synthetic prompt-injection protected case as a first-seam quality requirement

**Disposition: REMOVE / replace with deterministic projection regression.**

The correct first-seam control is now:

```text
product object graph may contain raw external text
→ planner projection must not
```

That is better verified deterministically than by injecting an artificial hostile note into a field the first seam should not carry.

Prompt-injection remains relevant at earlier/later model boundaries when raw external text is genuinely present, especially the existing support-drop extractor.

### 5.4 Planner-visible hard-constraint tuple

**Disposition: REMOVE FROM FIRST-SEAM MODEL INPUT; retain underlying invariants deterministically/systemically.**

E3/E4/E5 succeeded without the full `InvestigationSnapshot.hard_constraints` list being sent as planner state.

Important invariants do not disappear:

- model output is not authority;
- read-only catalog for first pilot;
- exact source identity remains deterministic;
- compatibility/safety/maintainer action remain outside planner authority.

But these are better enforced by action construction, admission, execution ownership, product proof boundaries, and a short generic system instruction than by repeating a policy tuple in every planner snapshot.

## 6. DEFER

### 6.1 Exact planner-facing action descriptor projection

**Disposition: DEFER optimization.**

E4.1 supplied the full trusted action descriptor and succeeded. It did not isolate which descriptor fields were necessary for model selection.

For now retain the existing trusted descriptor projection when evaluating the candidate seam. Do not spend another experiment merely minimizing tokens unless context size/clarity becomes a real issue.

Internally, all locator/action metadata stays pre-bound regardless of model visibility.

### 6.2 Proposition `origin` / `raw_external_text` metadata visibility

**Disposition: DEFER optimization.**

E3 included origin metadata and succeeded. Evidence does not establish whether those fields improve reasoning. Keep or remove only when a concrete request-size/trust-reasoning question makes it decision-changing.

### 6.3 Multi-action selection

**Disposition: DEFER until a second real independently justified action exists.**

Do not invent a second capability for agent aesthetics. The current evidence supports one-action-vs-no-tool planning only.

### 6.4 Model retries / semantic retries / routing / frameworks

**Disposition: DEFER.**

No current failure requires them. First-response evidence should remain observable.

### 6.5 Production integration

**Disposition: DEFER.**

E3–E5 establish component behavior, not sufficient product value/generalization/reliability for adoption.

## 7. Reconciled candidate first-seam flow

```text
TRUSTED PRODUCT / EVALUATION STATE
planning_question
repository / pull / immutable revision as needed for trace
ordered typed propositions
attempted action summary
remaining step budget
closed trusted action descriptors
        ↓
SMALL MODEL REQUEST
short generic planner instruction
no raw upstream source prose
no evaluator/oracle metadata
no synthetic untrusted-note channel
        ↓
MINIMAL STRICT STRUCTURED OUTPUT
state = choose_action | stop | defer | unresolved
action_id = string | null
explanation = string
        ↓
DETERMINISTIC PARSE
shape/state/action-nullability rules
        ↓
IF choose_action
trusted action lookup
→ rebind target proposition / result families / locator / mutation class / preconditions
→ deterministic admission against fresh state/history/budget
→ exact read-only capability or rejection
        ↓
IF stop/defer/unresolved
no capability execution
→ preserve explicit disposition + explanation as untrusted planner evidence
        ↓
DETERMINISTIC DOMAIN LOGIC
owns acquisition, interpretation, evidence promotion, proof strength, and trusted state update
```

## 8. What the old strict design got right

The earlier work was not wasted. Several of its central instincts survived direct testing:

- typed state rather than arbitrary raw evidence;
- closed pre-bound action authority;
- model proposal separate from execution authority;
- structured output;
- deterministic admission;
- explicit no-tool states;
- oracle isolation;
- development/protected separation;
- local bounded inference;
- no product truth/safety/merge authority in the planner.

The evidence-first route mainly **separated responsibilities and removed redundant model burden**, rather than overturning the architecture.

## 9. What the evidence changed

The important changes are narrower and practical:

1. raw upstream text is not inevitable at the planner seam; projection can remove it;
2. prompt-injection-specific planner machinery should not be built around a synthetic raw-text channel that the first seam does not require;
3. the model does not need to echo trusted action metadata;
4. JSON Schema is justified for integration shape, not reasoning quality;
5. deterministic admission is justified for fresh authority/state revalidation;
6. STOP/DEFER/UNRESOLVED should remain, but can live in a much smaller output contract;
7. the first product seam should not expose a verbose hard-constraint tuple when deterministic structure already enforces those invariants.

## 10. Evaluation protocol consequence — v2 protected set is consumed for final scoring

`b2-x1-phase3a-v2` states that protected outcomes may not be used to tune a configuration and then be reused as final evidence.

During the evidence-first exploration we deliberately used S001—the protocol's key protected action identity/state—to learn about:

- minimally constrained reasoning;
- closed action binding;
- JSON Schema shape;
- deterministic admission;
- candidate output simplification.

The candidate request/result contract also changed materially from the v2 strict `AgentPlanResult` shape.

Therefore:

```text
v2 remains valid historical accepted engineering work
but
v2 is no longer an uncontaminated final protected scorecard for the reconciled candidate
```

Do **not** edit v2 in place and pretend the protected boundary remained intact.

If the checkpoint continues to a final planner-quality disposition, create a fresh `v3` evaluation protocol with fresh protected material/configuration rules appropriate to the reconciled candidate.

## 11. What a fresh v3 should preserve versus shrink

A v3 protocol should preserve:

- development vs protected separation;
- oracle isolation;
- fresh real-case-first protected material;
- at least one action decision if a fresh real action case can be justified;
- STOP / DEFER / UNRESOLVED coverage;
- deterministic admission/authority zero-tolerance;
- raw-output preservation;
- bounded repeated observations sufficient to expose obvious instability;
- explicit comparison/disposition rule.

It should reconsider rather than copy automatically:

- the old six-field model result;
- synthetic injection-note cases at the planner seam;
- 24 protected calls / 22-of-24 threshold;
- seven-item limitations-heavy human rubric;
- mandatory planner-visible hard-constraint tuple;
- manifest/telemetry detail that does not change the bounded pilot decision.

The exact v3 case count/repeat threshold should be chosen only after fresh protected candidates are inventoried. Do not select numbers merely to look rigorous.

## 12. Current disposition

The evidence currently supports:

```text
FIRST-SEAM DESIGN
→ promising and materially simpler than the original strict model-output contract

PRODUCT ADOPTION
→ NOT YET JUSTIFIED

ORIGINAL V2 FINAL SCORING
→ NOT VALID FOR THE RECONCILED CANDIDATE DUE TO DELIBERATE PROTECTED-S001 USE / CONTRACT CHANGE

NEXT RESPONSIBILITY
→ design the smallest fresh v3 protected evaluation needed to decide RETAIN AS PILOT / REJECT / DEFER
```

No product `src/upgradepilot` integration should begin before that disposition.
