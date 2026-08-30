# B2/X1 EvidenceGapPlanner R2 — Planning Question Boundary

**Date:** 2026-08-30  
**Status:** R2 SLICE COMPLETE — planning-question boundary decided  
**Plan:** `../plans/B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`  
**Parent R2 memory:** `2026-08-30_B2-X1-EvidenceGapPlanner-R2-model-visible-context.md`

## 1. Why this slice exists

The `EvidenceGapPlanner` should not receive a vague mission such as "investigate this dependency update" and should not be allowed to invent its own top-level objective in the current first seam.

The accepted Product Decision Model already requires investigation reasoning to start from a **material non-final proposition state plus the location/reason of uncertainty or conflict**, then identify a **discriminating target** and select a justified investigation, preserve non-dominated alternatives, or stop when no useful investigation remains.

Therefore the planning question is the bounded uncertainty owner for one planner turn.

## 2. Decision

Keep one model-visible `planning_question` as concise project-owned text.

Current first-seam shape:

```text
planning_question: str
```

The model does **not** need a model-visible question ID, repository identity, pull-request number, commit revision, evaluator case key, or oracle label.

The system may retain a deterministic internal question key/type later for traceability, logging, replay, routing, or future question-admission logic, but that metadata is not currently justified as model reasoning context.

## 3. What the planning question owns

The planning question should answer:

> What exact bounded investigation uncertainty is this planner turn trying to advance?

It should define the decision-relevant target at the right semantic level, for example:

```text
What additional admitted investigation, if any, is useful for determining whether the established upstream Python support drop intersects the target's declared Python range?
```

The question is allowed to refer to already-defined semantic concepts such as:

- established upstream mechanism;
- target declared range;
- behavioral impact;
- dependency consumption;
- unresolved decision-critical authority gap;
- other accepted product-domain concepts.

It should not duplicate the full evidence state.

## 4. What the planning question must not own

Do not use the planning question to smuggle in context that already belongs in structured planner state.

Avoid embedding:

```text
repository / PR / revision identity
normalized package / old / proposed versions when already in dependency_transition
long lists of proposition states
CI result summaries already represented in EvidenceGapPlanningEvidence
raw changelog or source prose
raw commands / workflow YAML / diffs
allowed-action locators
expected action ID
expected no-tool disposition
oracle / evaluator hints
```

The question should not be written to steer the model toward the expected answer.

Bad shape:

```text
Because the exact target Python declaration is unresolved and the correct next action is to read pyproject.toml, what should you do?
```

Better shape:

```text
What additional admitted investigation, if any, is useful for determining whether the established upstream Python support drop intersects the target's declared Python range?
```

The structured context then carries the actual proposition/evidence state and action space.

## 5. Relationship to structured planner context

The current separation is:

```text
planning_question
→ defines which bounded uncertainty/responsibility is being advanced

propositions
→ define what is established / refuted / unresolved / conflicted
  and evidence coverage

EvidenceGapPlanningEvidence
→ supplies selected structured evidence shape, mechanism, witness,
  limitation, reason, or unresolved condition when planning-relevant

dependency_transition
→ supplies canonical package/version transition context

allowed_actions
→ supplies the current closed evidence-gathering capability space

attempt_history / budget
→ supplies bounded loop/history state
```

The question therefore acts as a **context-selection anchor**. It helps determine which propositions, which planning-evidence items, and which admitted capabilities are relevant enough to enter the model observation.

## 6. Question quality rules

A good first-seam planning question should be:

1. **bounded** — one investigation uncertainty/responsibility, not the whole dependency update;
2. **decision-relevant** — resolving it could change a material proposition or investigation state;
3. **outcome-neutral** — does not reveal the expected action/disposition;
4. **evidence-compatible** — can be answered from the supplied typed state plus admitted capability space;
5. **non-duplicative** — does not restate structured facts just to make the prompt self-contained;
6. **identity-light** — omits target/provider identifiers that do not improve reasoning;
7. **authority-safe** — does not ask the model to establish repository/source truth, invent locators, or own final compatibility/safety/maintainer decisions.

## 7. Why this is better than the historical question style

Historical S001 wording included named project/package context directly in prose:

```text
Given the grounded Soup Sieve Python-support change and the current target/CI evidence,
what additional admitted investigation, if any, is useful for determining whether the
dropped Python line intersects Pydantic's exact-head declared Python range?
```

The evidence-refined contract now has dedicated owners for those facts:

```text
SoupSieve/version identity
→ dependency_transition

support-drop semantics / CI distinctions
→ propositions + EvidenceGapPlanningEvidence

Pydantic repository / exact revision
→ deterministic hidden system state
```

Therefore future questions can be shorter and more reusable without losing evidence.

## 8. Future question-formulation agent hypothesis — retained, not activated

A separate future LLM/agent responsibility may become justified if the system eventually has:

```text
many material non-final propositions
+ several mechanism-specific candidates
+ multiple plausible bounded investigation questions
+ dependencies/prerequisites between those questions
+ history, cost, budget, or information-value trade-offs
```

At that point a separate component could potentially perform:

```text
trusted evidence / candidate state
→ propose one or more bounded investigation-question candidates
→ deterministic question validation/admission/prioritization
→ selected planning question
→ EvidenceGapPlanner
```

Working conceptual name only, not frozen:

```text
InvestigationQuestionFormulator
```

This responsibility would answer:

> Which bounded uncertainty is worth turning into the next planning problem?

while `EvidenceGapPlanner` answers:

> Given the already-admitted planning question, which evidence gap/capability should be pursued next, or should no capability execute?

Do **not** merge these responsibilities now. Current questions are sufficiently known/project-owned, so adding a question-formulation agent would manufacture complexity before a real selection problem exists.

## 9. Reactivation trigger for question formulation

Revisit the separate question-formulation responsibility only when a fixed deterministic question owner becomes materially brittle or semantically contextual because multiple legitimate questions compete for attention.

Useful evidence would include cases where:

- several unresolved propositions are independently material;
- the most valuable question changes with current evidence/history/budget;
- question order is not equivalent to proposition order;
- simple fixed routing repeatedly chooses dominated or irrelevant questions;
- semantic relationships between candidates make question formulation materially non-trivial.

## 10. LbD concepts earned in this slice

- objective/task formulation vs action planning;
- system state vs model observation;
- context-selection anchor;
- decision-relevant uncertainty;
- outcome leakage / oracle leakage;
- separation of question formulation from evidence-gap planning;
- future agent decomposition based on responsibility rather than framework fashion.

## 11. Next R2 slice

Continue with proposition projection fields:

```text
key
state
evidence_coverage
detail
evidence_owner
origin
```

The next question is not whether propositions are useful—they are already the decision-state spine—but **which fields genuinely improve planner reasoning and which are only internal provenance/trace metadata**.
