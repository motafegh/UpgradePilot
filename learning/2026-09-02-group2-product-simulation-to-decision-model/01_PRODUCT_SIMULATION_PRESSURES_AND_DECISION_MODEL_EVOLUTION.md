# Group 2 — Product Simulation Pressures and Decision-Model Evolution

**Learning-artifact date:** 2026-09-02  
**Evidence horizon:** `main@8f25bcb4e158f4f6e779ce63c264957f97e44771`  
**Refinement:** 2026-09-02 proportionality edit; evidence horizon and engineering scope unchanged  
**Roadmap responsibility:** Group 2 from `../../plans/UPGRADEPILOT_WHOLE_PROJECT_LEARNING_ARTIFACT_ROADMAP_PLAN.md`  
**Artifact role:** primary Group-2 historical pressure → current decision-model evolution note  
**Target depth:** **must master / own** the decision-model concepts and why they were needed; use the companion for focused case transfer  
**Companion:** [`02_REPRESENTATIVE_CASES_AND_TRANSFER_PATTERNS.md`](02_REPRESENTATIVE_CASES_AND_TRANSFER_PATTERNS.md)

This note answers one question:

> **How did real UpgradePilot product-simulation pressure turn a coarse evidence-to-action idea into the current impact-candidate → applicability → discriminating-investigation model?**

Product-simulation records are historical discovery/pressure evidence. Current accepted semantics are owned by the current Charter/specifications; current implementation truth remains source/tests/observed evidence. This distinction is stated once here and assumed throughout.

---

## 1. The simulation method and why the transparent baseline mattered

Product simulation used real dependency-update cases to challenge simple decision behavior before freezing product responsibilities:

```text
real case + exact evidence/uncertainty
→ restricted transparent baseline
→ deeper target-specific investigation
→ compare action, authority, uncertainty, actionability, and cost
→ identify repeated responsibilities / contradicted shortcuts
→ pressure-test them across different cases
→ promote only stable accepted semantics to durable owners
```

The transparent baseline deliberately saw only:

1. version-change category;
2. overall current CI conclusion;
3. dependency directness;
4. literal release-note keyword signals.

It was a comparator, not the intended final engine. Its value was methodological: deeper analysis had to **earn** its extra cost rather than win by definition.

That immediately exposed a key distinction:

> The broad action can stay the same while decision-support quality changes materially.

S001–S003 all demonstrated this in different ways: S001/S002 showed that target relationship and CI authority require more than coarse labels, while S003 showed that even failing CI must be decomposed to the exact failed responsibility and competing cause. The detailed historical mechanics remain in the original scenario records and the companion matrix rather than being repeated here.

Primary anchors:

- [`TRANSPARENT_BASELINE_SPECIFICATION.md`](../../product-simulation/TRANSPARENT_BASELINE_SPECIFICATION.md)
- [`S001_S002_CROSS_CASE_ARTIFACT_REVIEW.md`](../../product-simulation/S001_S002_CROSS_CASE_ARTIFACT_REVIEW.md)
- [`S003_POST_CASE_SYNTHESIS.md`](../../product-simulation/S003_POST_CASE_SYNTHESIS.md)

---

## 2. S004 and S005 established two opposite but equally important controls

### S004 — deeper investigation must be able to stop

S004 was deliberately selected as a baseline-sufficient control. The baseline and full investigation both selected `merge_after_normal_review`, but the useful result was the stopping proof:

```text
changed dependency really belongs to the owning path
+ exact proposed dependency is exercised
+ relevant exact-head checks pass
+ upstream information is coherent
+ no decision-critical contradiction or gap remains
→ do not activate deeper conditional investigations
→ stop
```

This did **not** establish `patch + green CI = safe`. It established that non-activation and justified stopping are affirmative technical results when the authority-critical questions have actually closed.

### S005 — exact evidence must also be allowed to weaken coarse caution

The baseline saw literal `breaking` / removal / deprecation signals and selected `run_targeted_checks`. The full investigation mapped the upstream statements to concrete activation conditions, checked the exact target surfaces and lock-backed matrix execution, and found no remaining target-specific question that justified another check.

The full action became `merge_after_normal_review`.

The durable lesson was:

```text
upstream statement
→ changed mechanism
→ activation condition
→ exact target surface
→ scoped evidence/coverage
→ unresolved question OR closure
```

A cautious heuristic is not trustworthy if exact evidence can only make the system more cautious and can never remove an unsupported gate.

Primary anchors:

- [`S004_POST_CASE_SYNTHESIS.md`](../../product-simulation/S004_POST_CASE_SYNTHESIS.md)
- [`S005_POST_CASE_SYNTHESIS.md`](../../product-simulation/S005_POST_CASE_SYNTHESIS.md)
- [`D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md`](../../product-simulation/D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md)

---

## 3. The missing intermediate object: the technical impact candidate

The early evidence-to-action framing had a conceptual gap:

```text
dependency changed
→ ???
→ target-specific technical conclusion
```

The later reconciliation introduced a mechanism-specific **technical impact candidate**:

```text
UPSTREAM CHANGE MECHANISM
+
TARGET-RELEVANT EXPOSURE / PATH
+
ACTIVATION CONDITION(S)
+
POSSIBLE TARGET-RELEVANT CONSEQUENCE
=
TECHNICAL IMPACT CANDIDATE
```

The important word is **candidate**. Candidate formulation must not self-authorize truth:

- describing an exposure does not establish that exposure;
- naming an activation condition does not establish that it is active;
- naming a possible consequence does not establish that the consequence occurred.

S006 was especially useful here because a Pydantic validator behavior change reached qldebugger through framework/declarative integration. Dependency-version selection helped activate the changed behavior, but the **target exposure** was the validator/framework integration itself. Tests/CI then served as evidence about that path.

That pressure helped prevent universal shortcuts such as “dependency present = target exposed” or one fixed exposure taxonomy.

Primary anchor:

- [`DECISION_MODEL_HANDOFF_2026-08-07.md`](../../product-simulation/DECISION_MODEL_HANDOFF_2026-08-07.md)

---

## 4. Applicability became proposition-based rather than a vague relevance score

Once a candidate exists, UpgradePilot evaluates whether that candidate applies to one exact target/revision/context.

The accepted candidate-level knowledge states are:

- **established applicable**;
- **established not applicable**;
- **unresolved**;
- **conflicted**.

Important boundaries:

```text
applicable != consequence proven
not applicable != missing evidence
unresolved != negative evidence
dependency/framework present != activation established
```

Candidate structure determines the propositions and paths that matter. For example:

```text
A AND B AND C
```

allows one necessary proposition to eliminate that path when refuted, while:

```text
A AND (B OR C)
```

cannot be closed merely because `B` is refuted while `C` remains viable.

The project deliberately does **not** infer from this that it needs a universal Boolean AST, SAT engine, rule engine, or graph engine. The semantic requirement is smaller: represent only the explicit logic required by the admitted candidate.

S001 later became a clean illustration: a specific upstream Python-support-drop candidate could be refuted against the target's declared Python range without pretending that every other possible update concern was settled.

Primary anchors:

- [`IMPACT_INVESTIGATION_COVERAGE_REBASE_2026-08-06.md`](../../product-simulation/IMPACT_INVESTIGATION_COVERAGE_REBASE_2026-08-06.md)
- [`UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`](../../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md)

---

## 5. Negative conclusions forced three separate coverage questions

Open-world reasoning is the default:

```text
not observed
→ unresolved / not established within admitted scope
```

A stronger negative conclusion needs a justified bounded universe or another sufficiently strong negative-evidence path.

The post-Conversation-C audit and later pressure tests made three different proof obligations explicit.

### 5.1 Evidence coverage

> Did the admitted evidence sufficiently cover proposition `P`?

This controls whether non-observation can support a negative proposition within a bounded scope.

### 5.2 Path-model coverage

> Did the candidate represent the material alternative applicability paths before claiming every viable path was eliminated?

A model of `A AND B` cannot claim closure if a material alternative `C` belonging to the same candidate was omitted.

### 5.3 Candidate-discovery coverage

> Did discovery identify enough material mechanism-specific candidates before making a broader transition-level claim?

Therefore:

```text
evidence completeness
!= path-model completeness
!= candidate-discovery completeness
```

and:

```text
all discovered candidates not applicable
!= transition proven to have no material target impact
```

unless discovery coverage for that stronger claim is independently justified.

S008 and S009 helped expose this distinction: a narrow mechanism can be fully resolved while broader transition discovery remains open, and material repository context may matter without being forced into the technical-candidate taxonomy. S010 later supplied a stronger real transfer case where one transition contained at least two independently grounded mechanisms.

Primary anchors:

- [`CANDIDATE_DISCOVERY_COVERAGE_PRESSURE_TEST_01.md`](../../product-simulation/CANDIDATE_DISCOVERY_COVERAGE_PRESSURE_TEST_01.md)
- [`S010_POST_CASE_SYNTHESIS.md`](../../product-simulation/S010_POST_CASE_SYNTHESIS.md)
- [`AUDIT-003`](../../audits/2026-08-10_AUDIT-003_post-conversation-c-product-decision-model.md)

---

## 6. Investigation selection became discrimination, not evidence accumulation

Once a material proposition remains unresolved or genuinely conflicted, the question is not simply “what else can we collect?”

The accepted reasoning asks:

```text
where exactly is the uncertainty/conflict?
→ what missing fact, relation, observation, or counterfactual outcome could materially change the state?
→ which supported investigation can discriminate that target?
```

That missing decision-relevant fact/observation is the **discriminating target**.

### S006 — dynamic execution was worth doing

Static evidence could identify the Pydantic behavior change and the exact target branch, but it could not settle the changed exception behavior. A bounded old/new differential reproduction activated precisely that branch with interpretable outcomes.

This shows why dynamic execution can be the best investigation **for a behavioral proposition** without implying that dynamic evidence is globally stronger.

### S007 — an investigation can lose value before execution

A resolver dry-run initially had plausible discriminating value. Stronger authoritative package/build evidence later established an empty compatible-version intersection for the owned package-family proposition.

The planned execution became redundant:

```text
check useful at T1
+ new admitted evidence at T2 resolves the proposition
→ recompute value
→ do not execute for procedural completeness
```

This established an important adaptive property: investigation selection is conditional on the **current evidence state**, not fixed when a plan is first generated.

Primary anchors:

- [`CONVERSATION_C_INVESTIGATION_SELECTION_PRESSURE_TEST_01.md`](../../product-simulation/CONVERSATION_C_INVESTIGATION_SELECTION_PRESSURE_TEST_01.md)
- [`CONVERSATION_C_HANDOFF_S007_2026-08-09.md`](../../product-simulation/CONVERSATION_C_HANDOFF_S007_2026-08-09.md)

---

## 7. “No next investigation” has different knowledge meanings

Cross-case pressure exposed three materially different stopping reasons:

1. **Resolved** — the proposition is settled, so another check is redundant. S007 is the clearest example.
2. **Path pruned** — a necessary proposition is refuted, so deeper work cannot change that candidate path. S001-style Python-support non-intersection is a clean example.
3. **Still unresolved, but no justified investigation remains** — available checks lack adequate scope, authority, discrimination, feasibility, or proportionality.

These may eventually share one presentation surface such as `no next check`, but they must not collapse into the same knowledge state.

The third endpoint is especially important:

```text
unresolved or conflicted
+
no further justified investigation
```

is valid and must not be rewritten as `not applicable`, `safe`, or overall evidence sufficiency.

---

## 8. Investigation execution and investigation evidence are also separate

A command can run successfully and still fail as evidence for the owned proposition.

Result meaning depends on identity, scope/context, temporal fidelity, contrast validity, reconstruction fidelity, authority/provenance, and what the observation actually supports.

Examples:

- a modern reproduction of a historical environment is not automatically exact historical evidence;
- a broad passing test suite may be non-discriminating if it never activates the implicated branch;
- an acquisition/execution failure is a source/check problem, not automatic proposition refutation.

This is why the accepted model validates result identity and evidential meaning **before** proposition reevaluation.

---

## 9. Later cases widened the mechanism space without forcing universal machinery

Later simulation work mattered most as transfer/adversarial evidence.

- **S010:** one transition can contain multiple independent mechanisms with different target handling states; first valid candidate found does not establish discovery completeness.
- **S011:** optional dependency declaration, environment formation, runtime activation, and behavior coverage are separate propositions. A platform-labelled workflow can be irrelevant to an optional dependency family it never installs.
- **S012:** current repository/current environment can be incomplete target context when the application intentionally persists state across dependency-version boundaries; producer-version provenance may become a necessary applicability input.

These cases strengthened the semantic model without justifying one universal optional-dependency engine, temporal engine, provenance graph, candidate taxonomy, or artifact schema.

Detailed S011/S012 transfer reasoning remains in the companion because those mechanisms add genuinely new target-context shapes.

Primary anchors:

- [`S010_POST_CASE_SYNTHESIS.md`](../../product-simulation/S010_POST_CASE_SYNTHESIS.md)
- [`S011_POST_CASE_SYNTHESIS.md`](../../product-simulation/S011_POST_CASE_SYNTHESIS.md)
- [`S012_POST_CASE_SYNTHESIS.md`](../../product-simulation/S012_POST_CASE_SYNTHESIS.md)

---

## 10. Current accepted reasoning spine

The Product Decision Model specification now condenses the pressure above into this framework-independent semantic flow:

```text
PUBLIC DEPENDENCY-UPDATE PR
↓
EXACT PROPOSAL / TARGET / DEPENDENCY / VERSION / REVISION IDENTITY
↓
ADMITTED EVIDENCE ABOUT THE EXACT TRANSITION
↓
ZERO OR MORE MECHANISM-SPECIFIC TECHNICAL IMPACT CANDIDATES
↓
CANDIDATE COMPONENTS KEEP THEIR EVIDENTIAL STATUS
↓
DERIVE CANDIDATE-SPECIFIC APPLICABILITY PROPOSITIONS / PATHS
↓
EVALUATE PROPOSITIONS
    established / refuted / unresolved / conflicted
↓
COMPOSE ONLY THE EXPLICIT LOGIC REQUIRED BY THE CANDIDATE
↓
CANDIDATE KNOWLEDGE STATE
    established applicable
    established not applicable
    unresolved
    conflicted
↓
IF MATERIAL NON-FINAL STATE REMAINS
    locate uncertainty/conflict
    → identify discriminating target
    → select justified investigation / small conditional sequence
       OR preserve non-dominated alternatives
       OR stop because no further justified investigation exists
↓
OBSERVATION / RESULT
↓
VALIDATE RESULT IDENTITY / SCOPE / CONTEXT / CONTRAST / EVIDENTIAL MEANING
↓
REEVALUATE CURRENT PROPOSITION
OR REFINE / SUPERSEDE CANDIDATE WITH LINEAGE
↓
REPEAT ONLY WHILE MATERIAL NON-FINAL STATE REMAINS
AND A JUSTIFIED USEFUL INVESTIGATION EXISTS
↓
INVESTIGATION STOP
↓
LATER OVERALL SUFFICIENCY / POLICY / MAINTAINER-FACING SYNTHESIS
```

The final boundary matters:

```text
epistemically useful investigation
!= UpgradePilot-authorized execution
!= maintainer-facing check recommendation
```

Candidate applicability/investigation does not silently own later maintainer policy.

---

## 11. How historical pressure became current accepted knowledge

The promotion path was roughly:

```text
S001–S005 simulation discovery
→ D1 repeated responsibilities / contradicted assumptions
→ impact/applicability/investigation rebase
→ S006/S007 and other pressure tests
→ post-Conversation-C audit and bounded amendments
→ accepted Product Decision Model specification
```

That arrow matters. Use the current specification for **what the accepted semantics are**; use simulations/audit/history for **why those semantics were needed and what simpler ideas failed under pressure**.

Older learning snapshots remain useful for deeper theory rather than being copied here:

- [`2026-08-10-seven-concept-foundation-pre-a-c-implementation.md`](../2026-08-10-seven-concept-foundation-pre-a-c-implementation.md)
- [`2026-08-10-product-decision-model-a-b-c-mastery-note.md`](../2026-08-10-product-decision-model-a-b-c-mastery-note.md)

---

## 12. Proof and non-proof boundaries

The simulation corpus and accepted semantic model do **not** establish:

- representative frequency of dependency-update failure modes;
- complete candidate recall;
- target safety or production readiness;
- final production schemas/persistence architecture;
- that every conditional investigation belongs in every case;
- that dynamic testing is globally stronger than static evidence;
- that LLM/agent planning is required;
- that more evidence always improves a decision;
- that historical case actions are universal maintainer policy;
- learner mastery from AI-authored scenario completion.

The cases are contrasting engineering evidence, not an oracle corpus.

---

## 13. Study depth and fast relearning

### Must master / own

Be able to explain and apply:

- technical candidate vs established applicability;
- proposition/path reasoning and open-world negative-evidence discipline;
- the three coverage questions;
- discriminating vs merely relevant evidence;
- adaptive investigation value and the three stopping meanings;
- result execution vs valid evidential meaning;
- candidate-level closure vs broader transition-level claims.

### Operational / lookup

Know why S004, S005, S006, S007, S010, S011, and S012 were distinct pressure cases. Exact run IDs, historical artifact layouts, audit IDs, and package-specific details are lookup-level.

### Fast relearning route

1. Re-read Sections **2, 5, and 6** for the strongest design pressures.
2. Redraw Section **10** from memory.
3. Use the companion matrix, then revisit detailed S004–S007 or S011/S012 only where transfer is fuzzy.
4. Use the older seven-concept note for deeper theory rather than expanding this artifact.

---

## 14. Primary evidence anchors

Current accepted owner:

- [`UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`](../../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md)

Historical simulation / synthesis / pressure evidence:

- [`TRANSPARENT_BASELINE_SPECIFICATION.md`](../../product-simulation/TRANSPARENT_BASELINE_SPECIFICATION.md)
- [`SCENARIO_COVERAGE.md`](../../product-simulation/SCENARIO_COVERAGE.md)
- [`S001_S002_CROSS_CASE_ARTIFACT_REVIEW.md`](../../product-simulation/S001_S002_CROSS_CASE_ARTIFACT_REVIEW.md)
- [`S003_POST_CASE_SYNTHESIS.md`](../../product-simulation/S003_POST_CASE_SYNTHESIS.md)
- [`S004_POST_CASE_SYNTHESIS.md`](../../product-simulation/S004_POST_CASE_SYNTHESIS.md)
- [`S005_POST_CASE_SYNTHESIS.md`](../../product-simulation/S005_POST_CASE_SYNTHESIS.md)
- [`D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md`](../../product-simulation/D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md)
- [`IMPACT_INVESTIGATION_COVERAGE_REBASE_2026-08-06.md`](../../product-simulation/IMPACT_INVESTIGATION_COVERAGE_REBASE_2026-08-06.md)
- [`DECISION_MODEL_HANDOFF_2026-08-07.md`](../../product-simulation/DECISION_MODEL_HANDOFF_2026-08-07.md)
- [`CONVERSATION_C_INVESTIGATION_SELECTION_PRESSURE_TEST_01.md`](../../product-simulation/CONVERSATION_C_INVESTIGATION_SELECTION_PRESSURE_TEST_01.md)
- [`CONVERSATION_C_HANDOFF_S007_2026-08-09.md`](../../product-simulation/CONVERSATION_C_HANDOFF_S007_2026-08-09.md)
- [`CANDIDATE_DISCOVERY_COVERAGE_PRESSURE_TEST_01.md`](../../product-simulation/CANDIDATE_DISCOVERY_COVERAGE_PRESSURE_TEST_01.md)
- [`S010_POST_CASE_SYNTHESIS.md`](../../product-simulation/S010_POST_CASE_SYNTHESIS.md)
- [`S011_POST_CASE_SYNTHESIS.md`](../../product-simulation/S011_POST_CASE_SYNTHESIS.md)
- [`S012_POST_CASE_SYNTHESIS.md`](../../product-simulation/S012_POST_CASE_SYNTHESIS.md)
- [`AUDIT-003`](../../audits/2026-08-10_AUDIT-003_post-conversation-c-product-decision-model.md)

No new Audit was required for this proportionality refinement; the engineering claims and evidence horizon were not changed.