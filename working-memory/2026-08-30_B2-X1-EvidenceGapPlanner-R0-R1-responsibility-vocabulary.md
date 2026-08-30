# B2/X1 EvidenceGapPlanner R0–R1 — Re-anchor and Responsibility Vocabulary

**Date:** 2026-08-30  
**Plan:** `../plans/B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`  
**Responsibility:** preserve the first executed Learning-by-Doing slice of the post-research EvidenceGapPlanner plan: re-anchor current evidence and freeze responsibility-oriented working vocabulary before implementation

## 1. Continuity

This record continues from:

1. `../MEMORY.md` — live position;
2. `2026-08-30_B2-X1-planner-responsibility-input-naming-and-next-route.md` — immediate pre-plan design/learning state;
3. `../plans/B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md` — selected bounded execution plan;
4. E1–E5 records and `2026-08-28_B2-X1-evidence-first-strict-design-reconciliation.md` — experimental evidence;
5. `2026-08-28_B2-X1-product-simulation-capability-research-response.md` — completed capability/value research.

Historical experiment names remain evidence, not naming authority.

---

## 2. R0 result — PASS

Current `main` still matches the post-research entry assumptions needed by this plan:

- E1–E5 are complete;
- product-simulation capability research is complete and integrated;
- no product `src/upgradepilot` EvidenceGapPlanner integration exists or is authorized yet;
- the current active planner contract remains experiment-owned under `experiments/`;
- historical v2 remains consumed as a final protected scorecard for the reconciled candidate;
- no second independently justified capability has yet earned LLM-owned selection;
- richer multi-action planner value therefore remains unproven rather than disproven.

The current experiment still uses generic/prototype terms including:

```text
PlannerPlanState
AgentPlanResult
InvestigationSnapshot
```

and historical state values:

```text
choose_action
stop
defer
unresolved
```

These names must not be retained merely because existing experiments/tests use them.

---

## 3. R1 responsibility decision

### Component working name

**`EvidenceGapPlanner`**

Responsibility sentence:

> Given one bounded UpgradePilot planning question, trusted typed evidence state, trusted attempt history/budget, and a closed set of admitted investigation capabilities, decide which material evidence gap should be addressed next by selecting one useful admitted capability, or explicitly decide why no capability should execute now.

Why this name currently passes the Naming Clarity recall test:

- `EvidenceGap` identifies the object of reasoning: what important evidence is still missing/conflicted/settled relative to the bounded question;
- `Planner` communicates that the component chooses/prioritizes a next investigation step rather than extracting semantic truth or executing the capability itself;
- it is materially narrower than `Planner` or `InvestigationPlanner` inside a product whose overall responsibility is investigation;
- it does not artificially narrow future actions to file acquisition only: resolver checks, bounded behavior checks, provenance acquisition, and other admitted investigations can still fit if later justified.

This remains an experiment/design working name until product integration is separately authorized, but it is the preferred vocabulary for the remaining X1 plan.

### Model result working name

**`EvidenceGapDecision`**

This names the model proposal itself rather than implying trusted authority. Deterministic parsing/admission still decides whether an action may execute and trusted domain code still owns resulting evidence/state.

---

## 4. Decision-state vocabulary

E5 established four materially different decision meanings when the action path is included:

```text
choose one admitted action
bounded question is settled
known useful investigation exists but is outside current admitted capability boundary
question remains non-final and no justified resolving investigation is currently identified
```

The historical short values are useful experimental provenance but are too ambiguous for the preferred active vocabulary, especially because `unresolved` is already a proposition/evidence state elsewhere in UpgradePilot.

### Preferred working decision kind

**`EvidenceGapDecisionKind`**

Candidate values to carry forward into R3 contract design:

```text
ACTION_SELECTED
QUESTION_SETTLED
KNOWN_INVESTIGATION_NOT_ADMITTED
NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
```

Semantic mapping from historical experiment vocabulary:

```text
choose_action
→ ACTION_SELECTED

stop
→ QUESTION_SETTLED

defer
→ KNOWN_INVESTIGATION_NOT_ADMITTED

unresolved
→ NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
```

### Why these values

#### `ACTION_SELECTED`

The planner selected one member of the trusted admitted action catalog. The value does not authorize execution by itself.

#### `QUESTION_SETTLED`

The bounded planning question has sufficient evidence for the current responsibility and additional investigation is not justified merely because adjacent facts or budget remain.

This is more expressive than `STOP`, which does not say what is stopping or why.

#### `KNOWN_INVESTIGATION_NOT_ADMITTED`

A useful next investigation is known, but no corresponding capability is currently admitted/available inside the planner's trusted action boundary.

This preserves the important E5 `defer` semantics without using a generic project-wide word whose reason is implicit.

It must not be confused with a transient network/provider failure of an already admitted action; retry/executor ownership remains a later separate concern.

#### `NO_JUSTIFIED_INVESTIGATION_IDENTIFIED`

The bounded question remains materially unresolved/conflicted/non-final, but the current state does not identify a justified admitted action or known outside investigation that would resolve it.

The word `identified` is intentional: it avoids claiming that no possible investigation exists in reality.

This is different from proposition state `unresolved` and therefore avoids semantic collision.

---

## 5. Representation deliberately left to R3

R1 freezes the **working vocabulary and meanings**, not the final wire/schema shape.

R3 must still decide whether these meanings are represented as:

- one `EvidenceGapDecisionKind` enum with optional `selected_action_id`;
- a tagged union of action-selection and no-tool decision types;
- another equally clear structured representation.

The representation must preserve the semantics above and remain compatible with deterministic admission/rebinding.

Do not keep the historical six-field `AgentPlanResult` shape merely for compatibility if R3 evidence shows trusted metadata can remain outside model ownership.

---

## 6. Learning closure

### Responsibility-oriented naming

A component name should identify **what it owns**, not merely that it uses AI or participates in investigation.

```text
Planner
→ too broad

InvestigationPlanner
→ still broad inside UpgradePilot

EvidenceGapPlanner
→ says the model reasons about unresolved evidence needs and next investigation choice
```

### Type + member naming

A short enum member can be acceptable when the domain type supplies enough meaning, but in this case the historical members `stop`, `defer`, and especially `unresolved` collide with other UpgradePilot concepts. More explicit decision-kind names reduce interpretation burden in source, logs, tests, and future multi-turn traces.

### Experiment vocabulary is not product authority

Existing code/tests establish what the experiment currently uses. They do not prove those names are the best durable API. Naming is being corrected before implementation rather than preserved through inertia.

---

## 7. Proof limits

R0/R1 do **not** prove:

- that `EvidenceGapPlanner` should enter product runtime;
- that the new names improve model quality;
- that a general adaptive planner is superior to deterministic sequencing;
- that the final JSON/schema representation is decided;
- that multi-action planning is now justified.

They establish a clearer responsibility/vocabulary for the next experiment-owned design/build stages.

---

## 8. Next bounded stage

Proceed to **R2 — exact model-visible context/input contract**.

R2 must decide field-by-field what the model receives and why, including:

- bounded planning question;
- repository / PR / immutable revision context;
- structured dependency transition (`package`, `old_version`, `proposed_version`);
- proposition fields and bounded detail;
- attempt history and outcome categories;
- remaining budget;
- model-visible subset of trusted action descriptors;
- fields explicitly excluded from the first seam.

For every candidate field apply:

```text
what planner reasoning does this enable?
why can deterministic/domain code not omit it from model context?
what authority remains outside the model even if the field is visible?
what concrete case/evidence demonstrates the need?
```

Do not add fields solely because they are available in product objects.
