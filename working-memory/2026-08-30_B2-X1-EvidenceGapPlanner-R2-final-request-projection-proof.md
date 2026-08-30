# B2/X1 EvidenceGapPlanner R2 — Final Request-Projection Proof

**Date:** 2026-08-30  
**Status:** R2 COMPLETE / PASS — field-level decisions integrate coherently; one output-semantic issue handed to R3  
**Plan:** `../plans/B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`  
**Parent R2 memory:** `2026-08-30_B2-X1-EvidenceGapPlanner-R2-model-visible-context.md`

## 1. Purpose

R2 designed each model-visible context slice independently. This final synthesis asks whether those decisions still form one coherent `EvidenceGapPlanner` observation when assembled together.

The proof is design/integration evidence, not runtime/model-quality proof. No new planner implementation, LM Studio call, GitHub acquisition, capability execution, product mutation, or protected scoring is performed here.

## 2. Brief meaning of a no-tool state

A **no-tool state** is a valid planner turn where no investigation action should execute now.

It is an umbrella concept, not one semantic outcome.

Historical E5 distinguished:

```text
stop
→ bounded question sufficiently settled / no further justified work

defer
→ useful next investigation is known, but outside current admitted action/support boundary

unresolved
→ state remains materially non-final and no admitted or known outside investigation is justified
```

Current candidate vocabulary expresses those meanings more explicitly as:

```text
QUESTION_SETTLED
KNOWN_INVESTIGATION_NOT_ADMITTED
NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
```

Therefore:

```text
no tool selected
!= planner failure
!= no budget
!= empty action catalog by definition
```

It means the planner deliberately concludes that none of the currently relevant actions should execute on this turn, and the decision kind explains why.

## 3. Final model-visible context candidate

```text
EvidenceGapPlannerContext

planning_question

dependency_transition
    normalized_package
    old_version
    proposed_version

propositions[]
    key
    state
    evidence_coverage
    evidence_owner
    detail

planning_evidence[]
    EvidenceGapPlanningEvidence
    # bounded structured, question-relevant evidence only

consumed_actions[]
    action_id

planning_budget
    remaining_investigations

allowed_actions[]
    EvidenceGapActionDescriptor
        action_id
        purpose
        target_proposition
        evidence_yield

output_schema / provider structured-output contract
```

Trusted but model-hidden by default:

```text
repository
pull_number
immutable revision
source presentation package spelling
raw source/provider objects
raw changelog / logs / YAML / diffs / lockfiles / arbitrary source
exact action repository/revision/path/command locator
exact action preconditions
mutation policy
exact Python result-family/class contract
current coarse cost_class
provider timeout/retry/backoff policy
full proposal/admission/execution trace
oracle/evaluator/protected-set metadata
```

## 4. Field / owner / visibility / authority table

| Context element | Trusted owner before model | Model-visible? | Why visible | Important hidden authority |
|---|---|---:|---|---|
| `planning_question` | project/orchestration question owner | yes | defines the bounded uncertainty this turn advances | question ID/trace identity; future question formulation authority |
| `dependency_transition.normalized_package` | `DependencyVersionChange` | yes | canonical dependency identity for reasoning | source spelling, source evidence, normalization/promotion authority |
| `old_version` / `proposed_version` | `DependencyVersionChange` | yes | exact trusted transition semantics | extraction/consensus proof |
| proposition `key` | domain proposition owner | yes | stable semantic identity / action targeting | proposition creation authority |
| proposition `state` | domain evaluator | yes | epistemic status | proof composition |
| `evidence_coverage` | domain evaluator | yes | missing evidence vs unresolved despite sufficient evidence | coverage rules |
| `evidence_owner` | domain evaluator | yes | bounded location/domain of the gap | exact source/provider locator |
| proposition `detail` | bounded project/domain interpretation | yes | explains state distinctions not captured by enums | arbitrary/raw external text remains excluded |
| `EvidenceGapPlanningEvidence` | selected projection from trusted domain evidence | selectively | mechanism/witness/limitation detail can change investigation value | raw Level-3 evidence and exact acquisition authority |
| `consumed_actions` | orchestration/system history | yes, IDs only | tells planner which semantic investigation has already been meaningfully consumed | full execution/audit trace and provider retry history |
| `planning_budget.remaining_investigations` | orchestration budget owner | yes | bounds remaining semantic investigation opportunities | provider retry/timeouts; future time/cost dimensions until earned |
| action `action_id` | trusted action catalog | yes | exact selection token | catalog creation/binding authority |
| action `purpose` | trusted action catalog | yes | tells what uncertainty the action advances | authorization |
| action `target_proposition` | trusted action catalog | yes | explicit semantic link to evidence gap | fresh precondition enforcement |
| action `evidence_yield` | trusted action catalog projection | yes | tells what useful evidence the action can contribute | exact result classes/validation |
| output schema | experiment/provider boundary | yes to provider/model request | machine-readable decision contract | semantic correctness and execution admission |

## 5. Representative request A — real S001 action state

This is the strongest concrete first-seam action state.

```text
planning_question:
    What additional admitted investigation, if any, is useful for determining
    whether the established upstream Python support drop intersects the target's
    declared Python range?

dependency_transition:
    normalized_package: soupsieve
    old_version: 2.6
    proposed_version: 2.8.4

propositions:
  - key: dependency_change_established
    state: established
    evidence_coverage: sufficient
    evidence_owner: dependency.change
    detail: Soup Sieve 2.6 -> 2.8.4 is the trusted changed dependency.

  - key: upstream_python_support_drop_established
    state: established
    evidence_coverage: sufficient
    evidence_owner: upstream.python
    detail: Soup Sieve dropped Python 3.8 in crossed release 2.8.

  - key: exact_target_python_declaration_established
    state: unresolved
    evidence_coverage: insufficient
    evidence_owner: target.python
    detail: The exact-head target declaration has not yet been acquired.

  - key: declared_python_range_intersects_dropped_line
    state: unresolved
    evidence_coverage: insufficient
    evidence_owner: target.python
    detail: This proposition depends on exact target declaration evidence.

  - key: selected_environment_dependency_consumption_established
    state: established
    evidence_coverage: sufficient
    evidence_owner: dependency.ci
    detail: Exact-head selected-environment static dependency consumption is established.

planning_evidence:
  - evidence_kind: dependency_ci_consumption
    consumption_state: supported
    reachability_kind: transitive
    witness_path:
      - mkdocs-llmstxt
      - beautifulsoup4
      - soupsieve
    limitation: Static consumption evidence does not itself establish runtime compatibility.

consumed_actions: []

planning_budget:
    remaining_investigations: 1

allowed_actions:
  - action_id: acquire_exact_target_python_declaration
    purpose: Acquire the exact target Python declaration needed to advance the unresolved Python-support question.
    target_proposition: exact_target_python_declaration_established
    evidence_yield: Exact target Python declaration evidence or a typed target-declaration problem.
```

### S001 projection inspection

Passes:

- no repository / PR / SHA enters model context;
- no target file path enters model context;
- no raw changelog prose enters model context;
- no workflow YAML / raw command / lockfile enters model context;
- dependency transition uses canonical identity;
- Level-2 CI evidence adds real information beyond the proposition label by preserving transitive reachability and witness path;
- action descriptor tells the model what it can learn without exposing execution authority.

One small intentional redundancy remains acceptable:

```text
planning question references the established upstream support drop
+
proposition state carries the authoritative fact
```

The question uses the concept only to define the bounded uncertainty; it does not repeat raw evidence or exact source detail.

## 6. Representative request B — real S004 no-tool / settled state

Product-simulation scenario identity establishes the transition as:

```text
pytest 9.0.2 -> 9.0.3
```

Representative model observation:

```text
planning_question:
    Does the current bounded evidence state require any further investigation
    to answer whether the pytest update has an unresolved decision-critical authority gap?

dependency_transition:
    normalized_package: pytest
    old_version: 9.0.2
    proposed_version: 9.0.3

propositions:
  - key: direct_pytest_development_role_established
    state: established
    evidence_coverage: sufficient
    evidence_owner: dependency.role
    detail: pytest is established as a direct development dependency.

  - key: changed_requirements_installed_by_owning_test_path
    state: established
    evidence_coverage: sufficient
    evidence_owner: dependency.ci
    detail: The owning test path installs the changed requirements state.

  - key: exact_head_relevant_pytest_ci_established
    state: established
    evidence_coverage: sufficient
    evidence_owner: dependency.ci
    detail: Relevant exact-head pytest CI evidence is established.

  - key: official_drop_in_bugfix_status_established
    state: established
    evidence_coverage: sufficient
    evidence_owner: upstream.release
    detail: Official upstream evidence establishes the update as a drop-in bug-fix release.

  - key: decision_critical_contradiction_or_gap_present
    state: refuted
    evidence_coverage: sufficient
    evidence_owner: investigation.stopping
    detail: No decision-critical contradiction or authority gap remains for this question.

planning_evidence: []
consumed_actions: []

planning_budget:
    remaining_investigations: 1

allowed_actions: []
```

Expected current semantic meaning:

```text
QUESTION_SETTLED
```

Important lesson:

```text
remaining_investigations = 1
!= investigation must happen
```

Budget is permission/constraint, not a reason to create work.

## 7. No-tool meanings retained beyond S004

Historical E5 also gives two additional development controls that R3 should preserve semantically:

### Known useful investigation exists but is not admitted

S006:

```text
cross-version target exception behavior
→ unresolved / insufficient

discriminating two-version check
→ identified

current admitted action catalog
→ cannot execute that responsibility
```

Current semantic candidate:

```text
KNOWN_INVESTIGATION_NOT_ADMITTED
```

### Genuine conflict with no justified action

Conflict control:

```text
dependency_ci_coverage_established
→ conflicted / sufficient

no admitted action
no identified outside capability
```

Current semantic candidate:

```text
NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
```

Thus no-tool is an explicit epistemic/planning branch, not an error path.

## 8. Representative request C — why selected Level-2 planning evidence matters

Compare S001 without and with the selected CI evidence.

### Proposition-only form

```text
selected_environment_dependency_consumption_established
→ established / sufficient
```

### Level-2 enriched form

```text
consumption_state: supported
reachability_kind: transitive
witness_path:
    mkdocs-llmstxt
    → beautifulsoup4
    → soupsieve
limitation:
    static consumption != runtime compatibility
```

The second form tells a future multi-action planner **how** the dependency is evidenced and what the evidence does not prove. That can matter when choosing among resolver inspection, stronger direct exercise, or behavioral reproduction.

Therefore R2 keeps propositions as the decision-state spine while allowing selected structured evidence to preserve decision-relevant shape.

## 9. Representative request D — consumed-action / no-blind-repeat state

Historical transfer evidence contains `d-repeat-stop`:

```text
exact_target_python_declaration_established
→ unresolved / insufficient

A1 already produced a stable typed result/problem
remaining investigation opportunity exists
→ do not blindly run A1 again
```

Evidence-refined request shape should be closer to:

```text
planning_question:
    What additional admitted investigation, if any, is useful for establishing
    the target's exact Python declaration from the current evidence state?

dependency_transition:
    normalized_package: soupsieve
    old_version: 2.6
    proposed_version: 2.8.4

propositions:
  - key: exact_target_python_declaration_established
    state: unresolved
    evidence_coverage: insufficient
    evidence_owner: target.python
    detail: The previously consumed exact-declaration investigation did not establish a usable exact declaration.

planning_evidence:
  - evidence_kind: target_python_declaration_problem
    meaning: A stable typed target-declaration problem was produced by the consumed action.
    limitation: Repeating the same immutable investigation is not expected to add information without a changed trusted condition.

consumed_actions:
  - acquire_exact_target_python_declaration

planning_budget:
    remaining_investigations: 1

allowed_actions: []
```

The consumed action is absent from the current offered action catalog. Deterministic admission still retains the repeat guard as defense-in-depth if stale/concurrent state causes a previously offered action to be proposed.

## 10. Important integration finding handed to R3

The historical case is named `d-repeat-stop` and historical `stop` semantics included both:

```text
question sufficiently settled
OR
no further justified work remains
```

But R1's current candidate vocabulary narrowed `stop` to:

```text
QUESTION_SETTLED
```

The consumed-action repeat state above is **not settled**:

```text
proposition remains unresolved
+
A1 is consumed
+
no currently justified action remains
```

Therefore it should not be forced into `QUESTION_SETTLED` merely because historical v2 called it `stop`.

R3 must explicitly reconcile this historical overloading. Strong current candidate mapping is:

```text
S004 clean settled state
→ QUESTION_SETTLED

S006 known outside investigation
→ KNOWN_INVESTIGATION_NOT_ADMITTED

conflicted state with no justified action
→ NO_JUSTIFIED_INVESTIGATION_IDENTIFIED

consumed-A1 unresolved state with no justified remaining action
→ likely NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
```

This is an output-semantic issue, not an R2 input-projection failure.

## 11. Duplicate / leakage / starvation audit

### Duplicate information

Acceptable:

- planning question may reference the semantic uncertainty already represented in propositions because it defines the bounded task;
- action `target_proposition` intentionally repeats a proposition key as an explicit relational link.

Avoid:

- repeating exact evidence detail in both question prose and planning evidence;
- repeating action preconditions already owned by trusted catalog/admission;
- echoing exact result class names when `evidence_yield` communicates the planning meaning.

### Authority leakage

None required in candidate shape:

```text
repository / PR / SHA / path / exact command
→ hidden

preconditions / mutation policy / result classes
→ hidden
```

### Raw evidence leakage

None required in candidate shape.

Structured witness paths and interpreted limitations are Level-2 evidence, not wholesale raw source content.

### Context starvation

Not observed in the representative shapes:

- proposition state carries decision spine;
- selected Level-2 evidence can preserve mechanism/witness limitations;
- action descriptor communicates information yield;
- consumed history and budget communicate loop state.

### Evaluator/oracle leakage

Case keys such as `p-s001-action`, expected decision kinds, expected action IDs and protected/development labels remain outside model context.

## 12. Budget-sensitive multi-action proof deliberately deferred

R2 does **not** fabricate a second action merely to demonstrate a cost-aware request.

Current first seam has no real competing action set with trustworthy timing/cost measurements.

Decision:

```text
planning_budget.remaining_investigations
→ included now

measured time/cost/resource tradeoff proof
→ deferred until real independently admitted competing actions exist
```

R4/R5 should collect telemetry before quantitative planner resource profiles are designed.

## 13. R2 final decision

**PASS.**

The integrated request contract is coherent enough to implement experimentally.

R2 establishes:

```text
bounded question
+ canonical dependency transition
+ typed proposition state
+ selected structured planning evidence
+ consumed semantic history
+ semantic investigation budget
+ semantic action descriptors
→ bounded model observation
```

without requiring:

```text
whole product object serialization
raw evidence dumping
repository/pretrained-project identity
model-authored locators
model-owned preconditions/authorization
coarse provider failure history
fabricated multi-action cost optimization
```

## 14. R3 handoff

R3 is now the live next stage.

Its first responsibility is not merely JSON syntax. It must reconcile the **decision semantics** before freezing the schema, especially:

1. whether `QUESTION_SETTLED` is strictly settled-only;
2. how consumed/no-further-action unresolved states map relative to `NO_JUSTIFIED_INVESTIGATION_IDENTIFIED`;
3. whether `KNOWN_INVESTIGATION_NOT_ADMITTED` cleanly covers useful outside-capability states;
4. whether the final output needs only:
   - `decision_kind`;
   - `action_id | null`;
   - bounded explanation;
5. which historical model echoes (`target_proposition`, expected-result categories, limitations) should be removed because trusted action/context owners already carry them.

No R4 implementation should begin until R3 freezes this output/admission contract.

## 15. LbD concepts earned in final R2 synthesis

- context architecture integration testing;
- valid no-tool/abstention states;
- budget as permission vs reason for action;
- semantic history vs available action space;
- evidence yield vs implementation result class;
- defense-in-depth admission vs model-facing catalog filtering;
- cross-stage semantic regression detection;
- why integration can reveal an output problem even when each input field looked correct alone.
