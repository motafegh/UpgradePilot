# B2/X1 EvidenceGapPlanner R2 — Model-Visible Context

**Date:** 2026-08-30  
**Status:** R2 COMPLETE / PASS  
**Plan:** `../plans/B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`  
**Responsibility:** decide and justify the exact trusted context projected into the `EvidenceGapPlanner` model request without serializing whole product state, starving the model of discriminating evidence, or transferring deterministic authority.

## 1. R2 governing rule

For every candidate model-visible field ask:

```text
what reasoning does this enable?
is that reasoning part of EvidenceGapPlanner responsibility?
is the fact already trusted before the model?
is the same meaning represented better elsewhere?
does it add discriminating context or only duplicate trace/authority metadata?
what remains deterministic even if the model sees it?
```

Do not equate important system state with model-visible state, and do not equate safe bounded context with label-only context.

## 2. Final evidence-refined model observation

```text
EvidenceGapPlannerContext

planning_question

dependency_transition
    normalized_package
    old_version
    proposed_version

propositions
    key
    state
    evidence_coverage
    evidence_owner
    bounded detail

planning_evidence
    EvidenceGapPlanningEvidence[]

consumed_actions
    action_id[]

planning_budget
    remaining_investigations

allowed_actions
    EvidenceGapActionDescriptor[]
        action_id
        purpose
        target_proposition
        evidence_yield

output_schema / structured-output contract
```

Trusted but model-hidden by default:

```text
repository
pull_number
immutable revision
exact action locators
exact action preconditions
mutation policy
exact result-family/class contract
provider/executor retry policy
full execution/audit trace
raw source/provider objects
oracle/evaluator metadata
```

## 3. Decided R2 slices

### Planning question

One concise project-owned bounded question is model-visible. It defines the uncertainty being advanced, not repository identity, evidence recap, expected action/disposition, or oracle hints.

Future question formulation may become a separate LLM/agent responsibility only when question selection itself becomes materially non-trivial.

Detailed owner: `2026-08-30_B2-X1-EvidenceGapPlanner-R2-planning-question.md`.

### Dependency transition

Pass:

```text
normalized_package
old_version
proposed_version
```

Use canonical normalized identity rather than source presentation spelling.

### Target/case identity

Repository / PR / immutable revision remain trusted for acquisition, trace, binding, freshness, admission and replay but stay outside the current model observation.

### Proposition projection

Pass:

```text
key
state
evidence_coverage
evidence_owner
detail
```

Do not add experiment-only `origin` or `raw_external_text` to the base first-seam contract.

Detailed owner: `2026-08-30_B2-X1-EvidenceGapPlanner-R2-proposition-projection.md`.

### `EvidenceGapPlanningEvidence`

Propositions are the decision-state spine, not the whole reasoning input.

Use selected structured question-relevant evidence when mechanism/witness/limitation/reason/unresolved-condition detail can change which investigation is useful.

```text
Level 1 = proposition state
Level 2 = selected EvidenceGapPlanningEvidence
Level 3 = raw evidence

current model observation = Level 1 + selected Level 2
Level 3 stays outside by default
```

### Consumed-action history

Use:

```text
consumed_actions: [action_id]
```

Consumed means an admitted bounded investigation produced a trusted typed result/problem for the bounded state.

Admission rejection, pre-execution staleness and transient provider failures are not automatically consumed investigations. Findings update propositions/planning evidence. Transport retries remain deterministic provider/executor policy.

Detailed owner: `2026-08-30_B2-X1-EvidenceGapPlanner-R2-action-history-and-retry-boundary.md`.

### Planning budget

Use:

```text
planning_budget:
    remaining_investigations: int
```

Spend one unit when fresh-admitted bounded execution actually begins. Internal deterministic provider retries do not spend extra semantic investigation units.

```text
execution begins
→ budget spent

trusted typed result/problem
→ action consumed
```

Future time/cost/resource dimensions enter model-visible budget only after real competing actions, real bounds and trustworthy measurements make them decision-relevant.

Detailed owner: `2026-08-30_B2-X1-EvidenceGapPlanner-R2-planning-budget-envelope.md`.

### Allowed action descriptor

Use:

```text
EvidenceGapActionDescriptor
    action_id
    purpose
    target_proposition
    evidence_yield
```

The planner sees enough to understand which evidence gap the action advances and what useful evidence it can produce.

Keep hidden:

```text
repository / revision / path
required proposition state/coverage
mutation_class
exact result_families / Python class names
current cost_class
provider/executor metadata
```

Deterministic catalog/admission owns current admissibility and exact execution binding.

Detailed owner: `2026-08-30_B2-X1-EvidenceGapPlanner-R2-capability-descriptor-boundary.md`.

## 4. Final synthesis / projection proof — PASS

Detailed owner:

`2026-08-30_B2-X1-EvidenceGapPlanner-R2-final-request-projection-proof.md`

The integrated contract was inspected using:

- real S001 action state;
- real S004 no-tool / settled state;
- S001 structured Level-2 CI reachability/witness evidence;
- consumed-action / no-blind-repeat state.

Result:

```text
bounded question
+ canonical dependency transition
+ typed propositions
+ selected structured planning evidence
+ consumed semantic history
+ semantic investigation budget
+ semantic action descriptors
→ coherent bounded model observation
```

The projection did not require repository/PR/SHA identity, raw changelog/log/YAML/diff/lockfile data, exact action locators/preconditions/result classes, evaluator/oracle metadata, or fabricated multi-action cost optimization.

## 5. No-tool state meaning retained

A no-tool state is a valid planner turn in which no investigation action should execute now. It is an umbrella branch, not one semantic outcome.

Current candidate meanings:

```text
QUESTION_SETTLED
→ bounded question is sufficiently settled

KNOWN_INVESTIGATION_NOT_ADMITTED
→ a useful next investigation is known but outside the admitted action/support boundary

NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
→ state remains non-final but no justified admitted or known outside investigation is identified
```

No-tool does not mean planner failure, empty budget, or necessarily an empty catalog.

## 6. R3 handoff — active next stage

R2 integration exposed one important output-semantic issue:

Historical `stop` semantics included both:

```text
question sufficiently settled
OR
no further justified work remains
```

But current candidate `QUESTION_SETTLED` is narrower.

The historical consumed-action `d-repeat-stop` state remains unresolved and should therefore not be forced into `QUESTION_SETTLED`; it likely belongs under `NO_JUSTIFIED_INVESTIGATION_IDENTIFIED` if no justified action remains.

R3 must reconcile this before freezing the output schema.

R3 also decides whether the final output needs only:

```text
decision_kind
action_id | null
explanation
```

and whether historical echoes such as `target_proposition`, expected-result categories and limitations should be removed because trusted context/action owners already carry those meanings.

No R4 implementation should begin until R3 freezes the output/admission contract.

## 7. Raw/default exclusions retained

Do not pass wholesale merely because UpgradePilot stores them:

- raw changelog/release-note prose;
- full GitHub Actions logs/payloads;
- full workflow YAML;
- whole diffs/source files;
- complete lockfiles/dependency graphs;
- whole nested domain/evidence objects;
- raw command text by default;
- evaluator/oracle/protected-set/grading metadata;
- exact provider/action locator data;
- verbose policy strings whose behavior is structurally enforced.

These are defaults, not permanent bans. A later responsibility may earn bounded raw/near-raw evidence explicitly.

## 8. Framework relationship

R2 is framework-independent.

During R4 the same R2 semantics must be preserved in both the ordinary-Python reference implementation and LangGraph implementation. LangGraph/LangChain convenience must not silently broaden model authority or erase this projection boundary.

## 9. LbD concepts earned through R2

- canonical identity vs presentation spelling;
- full system state vs model observation;
- context engineering / projection;
- proposition state vs supporting planning evidence;
- information compression vs information loss;
- raw evidence vs interpreted evidence;
- action space vs execution authority;
- general capability vs pre-bound action instance;
- semantic evidence yield vs implementation result classes;
- model memory vs trusted consumed-action state;
- semantic retry vs transport retry;
- planning budget vs operational resource policy;
- telemetry before cost-aware optimization;
- no-tool/abstention as a valid planning branch;
- cross-stage integration testing revealing semantic drift;
- framework-independent agent-state design.
