# B2/X1 EvidenceGapPlanner R2 — Model-Visible Context

**Date:** 2026-08-30  
**Status:** ACTIVE R2 WORKING MEMORY  
**Plan:** `../plans/B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`  
**Responsibility:** decide and justify the exact trusted context projected into the `EvidenceGapPlanner` request without serializing whole product state, starving the model of discriminating evidence, or transferring authority to the model.

## 1. Current R2 state

R0/R1 are complete. Current vocabulary:

```text
EvidenceGapPlanner
→ EvidenceGapDecision
→ EvidenceGapDecisionKind
```

Preferred decision semantics:

```text
ACTION_SELECTED
QUESTION_SETTLED
KNOWN_INVESTIGATION_NOT_ADMITTED
NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
```

Historical experiment fields remain evidence only; progressive R2 slices supersede them where explicitly decided.

## 2. R2 decision rule

For every model-visible field ask:

```text
what reasoning does this enable?
is that reasoning part of EvidenceGapPlanner responsibility?
is the fact trusted before the model?
is the same meaning better represented elsewhere?
does exposing it add discriminating context or only trace/authority metadata?
what authority remains deterministic even when the model sees it?
```

Do not equate:

```text
important product/system state = model-visible state
```

and do not equate:

```text
safe compact context = proposition labels only
```

The planner request is an explicit observation/projection of trusted state plus selected structured planning evidence.

---

## 3. Decided — dependency transition

Model-visible:

```text
dependency_transition:
    normalized_package
    old_version
    proposed_version
```

Use canonical `normalized_package`, not source-presentation `package`.

Do not automatically project `source_evidence` or `limitations` from `DependencyVersionChange`.

---

## 4. Decided — target/case identity

Keep these trusted but model-hidden:

```text
repository
pull_number
immutable revision
```

They remain available for traceability, replay, exact acquisition, action binding, freshness and admission.

Reasoning principle:

```text
critical execution identity
!= useful model reasoning feature
```

Repository identity additionally risks inviting stale pretrained project knowledge instead of admitted evidence.

---

## 5. Decided — planning question

Model-visible:

```text
planning_question: str
```

It owns only the bounded decision-relevant uncertainty for the current planner turn.

It must not duplicate:

- repository/PR/revision identity;
- dependency-transition fields;
- proposition lists;
- planning-evidence summaries;
- expected action/disposition;
- oracle/evaluator hints;
- raw evidence.

Detailed owner: `2026-08-30_B2-X1-EvidenceGapPlanner-R2-planning-question.md`.

A future question-formulation agent remains a separate hypothesis only when selecting among several legitimate questions becomes materially non-trivial.

---

## 6. Decided — proposition projection

Model-visible proposition fields:

```text
key
state
evidence_coverage
evidence_owner
detail
```

Do not add experiment-only `origin` or `raw_external_text` fields to the base first-seam proposition contract.

`detail` must remain intentionally admitted bounded project/domain-interpreted text; whole-object serialization is not authorization for arbitrary future text.

Detailed owner: `2026-08-30_B2-X1-EvidenceGapPlanner-R2-proposition-projection.md`.

---

## 7. Decided — propositions are the state spine, not the whole reasoning input

UpgradePilot already retains useful structured evidence distinctions that can be lost by label-only projection.

Use the working concept:

**`EvidenceGapPlanningEvidence`**

Definition:

> a bounded project-owned structured projection of already-acquired/interpreted evidence whose mechanism, limitation, witness, reason, or unresolved condition can materially change which evidence gap or capability has the highest discriminating value for the current planning question.

Relationship:

```text
PropositionAssessment
→ what is established/refuted/unresolved/conflicted and with what coverage

EvidenceGapPlanningEvidence
→ selected evidence shape/details that can change what investigation is useful next
```

Examples may include question-relevant structured CI consumption/direct-exercise states, reachability/witness paths, target-Python interpretation, upstream mechanism facts, environment conditions, bounded change-scope facts and deterministically interpreted command semantics.

### Three evidence levels

```text
LEVEL 1
proposition state

LEVEL 2
selected EvidenceGapPlanningEvidence

LEVEL 3
raw evidence: logs/YAML/changelog/source/diff/lockfile/raw command
```

Current default:

```text
model gets Level 1 + selected Level 2
Level 3 stays outside by default
```

Raw/near-raw evidence may be reconsidered later only when a real responsibility proves its need.

---

## 8. Decided — planner-visible history is consumed investigations

Historical prototype:

```text
attempted_actions:
    action_id
    outcome = completed | problem | rejected
```

Evidence-refined first-seam concept:

```text
consumed_actions:
    action_id[]
```

An action is planner-visible as consumed only after:

```text
model proposes
→ deterministic admission accepts
→ bounded execution responsibility runs
→ trusted typed domain result or typed domain/evidence problem exists
→ propositions/planning evidence update
→ action recorded as consumed for the bounded state
```

Do **not** record as consumed merely because:

- a model proposal was rejected;
- an action became stale before execution;
- provider transport timed out / rate-limited / failed operationally;
- an untrusted provider response never became valid domain evidence.

Findings belong in propositions / `EvidenceGapPlanningEvidence`, not free-form history prose.

Transport retry remains deterministic provider/executor policy, not a model replanning loop.

Detailed owner: `2026-08-30_B2-X1-EvidenceGapPlanner-R2-action-history-and-retry-boundary.md`.

---

## 9. Active next decision — planning budget envelope

Historical `remaining_steps` is too vague as durable vocabulary.

First-seam candidate:

```text
planning_budget:
    remaining_investigations: int
```

Starting lifecycle hypothesis:

```text
model proposal
→ no investigation budget spent

admission accepted
→ not yet spent

fresh pre-execution revalidation passes
→ execution begins
→ spend one investigation unit

internal deterministic provider retries
→ no additional semantic investigation units
```

Why start here:

- rejected proposals should not consume investigation budget;
- admitted actions may become stale before execution;
- a real execution can consume resources even if no useful result is ultimately produced;
- HTTP/provider retry attempts are operational attempts inside one investigation responsibility, not automatically new planner decisions.

### Budget is likely multi-dimensional later

Do not force all resources into one scalar.

Potential future planner-visible dimensions:

```text
remaining_investigations
remaining_time_seconds
remaining_external_cost
other bounded resource envelope
```

A new model-visible dimension earns inclusion only when:

1. it is actually bounded/measured;
2. admitted capabilities materially differ on it;
3. the planner can use it to choose better discriminating work;
4. capability descriptors contain trustworthy cost/latency/resource information.

Keep operational controls separate:

```text
request timeout
retry count
backoff
rate-limit policy
provider-specific limits
```

Those belong to deterministic execution policy unless later evidence changes the owner.

---

## 10. Revised candidate `EvidenceGapPlannerContext`

```text
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
    # optional time/cost/resource dimensions only when earned

allowed_actions
    planner-useful bounded capability descriptors
```

Trusted/model-hidden by default:

```text
repository
pull_number
revision
exact action locators
raw provider/source objects
full execution/audit trace
provider retry counters/timeouts
oracle/evaluator metadata
```

---

## 11. Remaining R2 decisions

1. finish/freeze the planning-budget lifecycle and first-seam schema;
2. decide model-visible capability descriptor vs deterministic-only metadata;
3. decide whether any first-seam capability resource profile is useful enough to expose;
4. construct final field/owner/why-visible/why-hidden table;
5. render representative request projections and close R2.

Do not implement the final coherent agent seam until R2 is unambiguous enough for R3/R4.

---

## 12. Framework-learning amendment for later R4

The active plan now explicitly authorizes:

```text
R4-A ordinary-Python reference/control implementation
R4-B same bounded responsibility implemented with LangGraph
R4-C smaller LangChain agent/tool/middleware learning slice
R4-D real comparison
```

This is not framework tourism and not automatic adoption.

Learning value is legitimate when attached to the real UpgradePilot responsibility and compared against a real baseline.

Current conceptual mapping to learn later:

```text
our trusted workflow state → LangGraph State
planner/admission/execution/update responsibilities → nodes
continue/stop routing → edges / conditional edges
replanning → graph loop
replay/fault tolerance learning → persistence/checkpoints
lifecycle hooks/tool abstractions → LangChain middleware/tools where useful
```

Framework adoption remains a separate evidence-backed product/architecture decision.

---

## 13. LbD concepts earned so far in R2

- canonical vs presentation identity;
- full system state vs model observation;
- bounded objective formulation;
- proposition state vs evidence coverage;
- evidence-owner/uncertainty location;
- structured planning evidence vs raw evidence;
- information compression vs information loss;
- action lifecycle and consumed history;
- idempotency;
- transport retry vs semantic replanning;
- TOCTOU/pre-execution freshness;
- semantic planning budget vs operational resource limits;
- framework learning vs framework adoption.
