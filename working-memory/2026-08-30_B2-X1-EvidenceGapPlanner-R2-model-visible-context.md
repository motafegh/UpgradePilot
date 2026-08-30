# B2/X1 EvidenceGapPlanner R2 — Model-Visible Context

**Date:** 2026-08-30  
**Status:** ACTIVE R2 WORKING MEMORY  
**Plan:** `../plans/B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`  
**Responsibility:** decide and justify the exact trusted context projected into the `EvidenceGapPlanner` model request, without serializing whole product state, starving the model of discriminating evidence, or inventing model authority.

## 1. Entry state

R0/R1 are complete. Current working vocabulary:

```text
EvidenceGapPlanner
→ EvidenceGapDecision
→ EvidenceGapDecisionKind
```

Preferred decision semantics currently are:

```text
ACTION_SELECTED
QUESTION_SETTLED
KNOWN_INVESTIGATION_NOT_ADMITTED
NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
```

Historical experiment request fields remain evidence only; they are not retention authority.

## 2. R2 decision rule

For every candidate model-visible field ask:

```text
what exact reasoning does this enable?
is that reasoning part of EvidenceGapPlanner responsibility?
is this fact already trusted before the model?
is the same meaning already represented more appropriately elsewhere?
does exposing it add useful discriminating context or only duplicate trace/authority metadata?
what remains deterministic even if the model can see the value?
```

Do not equate:

```text
important product state
=
model-visible state
```

and do not equate:

```text
safe compact model context
=
proposition labels only
```

The planner request is an explicit projection of trusted state and selected structured evidence.

## 3. Dependency transition — decided

Trusted source owner: `src/upgradepilot/dependency/change.py::DependencyVersionChange`.

That product type preserves both:

```text
package
→ source spelling / presentation form

normalized_package
→ canonical cross-source identity used for comparison/agreement
```

### Decision

Use the canonical identity in planner context:

```text
dependency_transition:
    normalized_package
    old_version
    proposed_version
```

Do **not** include `package` merely to preserve source spelling.

### Why

- `EvidenceGapPlanner` reasons about one trusted dependency transition, not presentation spelling.
- UpgradePilot already uses normalized package identity across downstream dependency/environment reasoning.
- One canonical identity avoids giving cosmetic spelling variation semantic weight.
- The model does not create or normalize this identity; deterministic product code remains authoritative.
- This is an identity-consistency/context-quality decision, not primarily a parsing/performance optimization.

### Explicit non-fields from `DependencyVersionChange`

Do not automatically project:

```text
package
source_evidence
limitations
```

Those remain with their existing evidence/product owners unless a later planner reasoning requirement specifically earns them.

## 4. Target/case identity — decided

The historical Phase-3B request renderer exposed:

```text
repository
pull_number
revision
```

while deliberately excluding evaluator/development/protected `case_key` and oracle metadata.

R2 now applies the same principle more strictly:

```text
system-important trace/execution identity
!=
model-visible reasoning context
```

### Decision

Keep these fields in trusted system/evaluator/executor state but omit them from the first-seam model projection:

```text
repository
pull_number
immutable revision
```

### Why

#### `pull_number`

Useful for traceability, UI, replay and provider acquisition, but the number itself adds essentially no evidence-gap reasoning value.

#### `revision`

Critical for exact evidence identity, stale-state checking, action binding, admission and replay, but a 40-character commit SHA does not materially help the model choose which evidence gap to resolve.

#### `repository`

Unlike the other two, a repository name can carry semantic associations from model pretraining. For the current bounded responsibility that is a liability rather than a demonstrated benefit: the planner should reason from admitted UpgradePilot evidence instead of remembering potentially stale facts about a named project.

### Authority flow after omission

Omitting target identity from model context does not remove it from the system:

```text
EvidenceGapDecision.action_id
→ trusted action lookup
→ deterministic repository / revision / path / capability metadata
→ fresh admission
→ exact bounded execution
```

## 5. R2 refinement — propositions are the state spine, not the whole reasoning input

The current deterministic product retains evidence richer than proposition labels. CI is the clearest example.

`DependencyCICoverageResult` and `WorkflowDependencyCoverageResult` preserve distinctions such as:

```text
CI aggregate state / reason / detail
successful exact-head runtime evidence
static dependency consumption
stronger direct package exercise
```

`StaticDependencyConsumptionEvidence` can additionally preserve:

```text
mechanism
reachability_kind
witness_path
conditional_candidate_path
unresolved_conditions
```

Therefore R2 rejects both extremes:

```text
RAW-EVIDENCE DUMP
→ full logs / YAML / diffs / lockfiles / source into model

LABEL-ONLY STARVATION
→ only established/refuted/unresolved/sufficient/insufficient
```

The current target is a middle layer:

```text
typed proposition state
+
selected question-relevant structured evidence
```

## 6. New planner-facing evidence layer — `EvidenceGapPlanningEvidence`

### Working name

Use **`EvidenceGapPlanningEvidence`** as the R2 working name for one or more bounded structured evidence items exposed specifically because their details can affect evidence-gap selection.

This is more expressive than:

```text
EvidenceSummary
→ too generic / sounds mainly textual and lossy

EvidenceWitness
→ too narrow; useful planning evidence is not always a witness path
```

`EvidenceGapPlanningEvidence` communicates the exact responsibility: evidence selected for the `EvidenceGapPlanner` decision boundary.

Do not freeze a concrete dataclass merely because the concept now has a name. R2 first freezes semantics and projection rules; R4 later implements the smallest coherent representation.

### Definition

`EvidenceGapPlanningEvidence` is:

> a bounded, project-owned structured projection of already-acquired/interpreted evidence whose details can materially change which evidence gap or admitted capability has the highest discriminating value for the current planning question.

It is **not**:

- raw evidence storage;
- a generic evidence database;
- a second proposition system;
- model-generated truth;
- a vehicle for copying arbitrary external prose into the prompt.

### Relationship to propositions

```text
PropositionAssessment
→ what is currently established / refuted / unresolved / conflicted
  and whether the evidence coverage is sufficient

EvidenceGapPlanningEvidence
→ selected structured facts explaining the evidence shape,
  mechanism, limitation, witness, or unresolved condition
  when those details can change planning
```

The planner should normally reason from both when the planning question warrants it.

## 7. Candidate evidence families for `EvidenceGapPlanningEvidence`

These are evidence-backed examples from current UpgradePilot state. They are not a requirement to expose every field on every request.

### 7.1 CI / dependency-consumption evidence

Potential planner-visible structured facts:

```text
ci_coverage_state
ci_reason

consumption_state
consumption_reason
consumption_mechanism

direct_exercise_state
direct_exercise_reason

reachability_kind
witness_path
conditional_candidate_path
unresolved_conditions
```

Why useful:

```text
successful CI
!= changed dependency consumed
!= changed package directly exercised
```

A planner choosing between more CI evidence, behavioral reproduction, or another investigation may need those distinctions.

Normally deterministic-only unless a concrete reasoning need appears:

```text
workflow_revision
workflow path as exact locator
job identifiers
step/segment indexes
provider run/job payloads
```

### 7.2 Target Python evidence

Potential bounded structured form:

```text
target_python_declaration_state
declared_python_range
```

Prefer the interpreted declaration/range over whole `pyproject.toml` content.

### 7.3 Upstream semantic evidence

Potential bounded structured form when relevant:

```text
mechanism: python_support_drop
python_line
introduced_in_version
grounding_state
```

Prefer grounded typed meaning over raw changelog prose for the current seam.

### 7.4 uv / environment evidence

Potential useful planning facts:

```text
reachability_state
reachability_kind
witness_path
conditional_candidate_path
unresolved_conditions
```

These can reveal whether the useful next gap is, for example, resolving an environment/marker condition rather than re-investigating package presence.

### 7.5 Changed-file / change-scope evidence

Do not pass the complete diff by default. If the planning question needs change topology, project a bounded structured fact such as:

```text
dependency_source_changed
target_source_changed
workflow_definition_changed
```

Only add a field when the deterministic product has actually established its meaning.

### 7.6 Commands

Current CI evidence preserves exact command strings, but raw commands are repository-controlled text and can reopen the untrusted-text channel E2 avoided.

Default rule:

```text
raw command
→ deterministic parser/interpreter
→ structured command meaning
→ planner when useful
```

For example:

```text
operation: environment_install
manager: uv
selected_group: docs
```

Do not make raw command text model-visible merely because it is available. Reconsider only if exact command semantics cannot be represented adequately and a real planning responsibility proves the need.

## 8. Three evidence levels — retained R2 mental model

### Level 1 — proposition state

```text
exact_target_python_declaration
→ unresolved / insufficient
```

Answers:

> What do we currently know about a decision-relevant proposition?

### Level 2 — `EvidenceGapPlanningEvidence`

```text
CI dependency consumption
→ supported
→ mechanism = project_environment
→ reachability = transitive
→ direct exercise = not established
```

Answers:

> What bounded evidence shape, mechanism, limitation or witness could affect what investigation is useful next?

### Level 3 — raw evidence

```text
workflow YAML
CI logs
changelog prose
source code
lockfile
diff
raw command text
```

Answers:

> What was the underlying source material?

### Current first-seam default

```text
Level 1
+
selected Level 2

Level 3 stays outside model context by default
```

## 9. Selection rule for planning evidence

Do **not** expose every available evidence record.

A structured evidence item earns model visibility only when:

1. it is already admitted/interpreted by a deterministic or separately authorized semantic owner;
2. it is relevant to the bounded planning question;
3. its structured details add discriminating planning information beyond the proposition state alone;
4. its exact source/provider identity is not required for the model to perform the reasoning;
5. exposing it does not silently transfer evidence truth, execution authority, or final decision authority to the model.

When a bounded project-authored `reason` or `detail` is exposed, it must remain a controlled explanation of already interpreted evidence, not an arbitrary copy of external source prose.

## 10. Revised candidate model-visible context

Current R2 candidate:

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
    bounded detail
    # evidence_owner/origin still under review

planning_evidence
    EvidenceGapPlanningEvidence[]
    # selected structured question-relevant evidence only

attempted_actions
    action_id
    outcome

remaining_budget

allowed_actions
    planner-useful bounded capability descriptors
```

Trusted but model-hidden:

```text
repository
pull_number
revision
exact action locators
raw source/provider objects
oracle/evaluator metadata
```

## 11. Explicit raw/default exclusions

Do not pass wholesale merely because UpgradePilot records them:

- raw release notes/changelog text;
- full GitHub Actions logs/payloads;
- full workflow YAML;
- complete changed-file diffs;
- arbitrary source files;
- complete lockfiles/dependency graphs;
- whole impact-assessment/domain object graphs;
- raw command text by default;
- evaluator case labels/oracles/expected answers;
- grading/protected-set metadata;
- synthetic untrusted-note channels created only for pressure testing;
- verbose policy strings whose behavior is already structurally enforced.

These are defaults, not permanent bans. A later responsibility may earn selected raw/near-raw evidence through explicit evidence.

## 12. Why this matters for LLM value

A proposition-only state can collapse a rich investigation into something close to a fixed selector:

```text
A established
B unresolved
C unresolved
→ choose B action
```

Selected Level-2 evidence can create real planning distinctions without surrendering authority, for example:

```text
CI successful
+ changed dependency statically consumed
+ consumption is transitive
+ direct exercise not established
+ behavioral compatibility unresolved
+ budget = 1
+ several admitted capabilities
→ decide which remaining evidence has highest discriminating value
```

This does not by itself prove adaptive-planner value; it creates a context representation capable of supporting such value when real multi-capability states emerge.

## 13. Remaining R2 decisions

Continue field-by-field through:

1. bounded `planning_question` ownership and whether any structured question identity/type is useful;
2. proposition fields:
   - `key`;
   - `state`;
   - `evidence_coverage`;
   - `detail`;
   - `evidence_owner`;
   - semantic `origin` if any;
3. exact schema/shape of `EvidenceGapPlanningEvidence` only as far as required for the first coherent experiment;
4. trusted attempted-action history and outcome semantics;
5. remaining budget;
6. model-visible capability descriptor vs deterministic-only action metadata;
7. final explicit projection/exclusion table.

Do not implement the final experiment contract until R2 is complete enough to make this boundary unambiguous.

## 14. LbD concepts earned in this slice

- canonical identity vs presentation spelling;
- full system state vs model observation;
- context engineering / request projection;
- proposition state vs supporting structured evidence;
- information compression vs information loss;
- raw evidence vs interpreted evidence;
- model-context sufficiency vs context dumping;
- untrusted text channels;
- evidence authority vs reasoning visibility.
