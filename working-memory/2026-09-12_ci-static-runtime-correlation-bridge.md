# CI Static↔Runtime Correlation Bridge — Working Memory

**Date:** 2026-09-12  
**Session status:** ACTIVE  
**Primary mode:** Planning/Design + Learning-by-Doing  
**Parent selected plan:** [`../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)  
**Previous:** [`2026-09-11_ci-run-job-attempt-coherence-enhancement.md`](2026-09-11_ci-run-job-attempt-coherence-enhancement.md)

## Starting point

The previous cycle repaired and proved exact GitHub Actions run/job attempt coherence. It also established that UpgradePilot already owns two distinct evidence layers:

```text
STATIC WORKFLOW EVIDENCE
→ exact PR-head workflow definition
→ jobs / strategy / ordered steps / commands / conditions

RUNTIME ACTIONS EVIDENCE
→ exact workflow run + attempt
→ runtime jobs
→ runtime step summaries / status / conclusion
```

`src/upgradepilot/ci/dependency_exercise.py` deliberately does not correlate those layers. Its strongest current result remains `supported_not_correlated` when successful exact-head runtime CI and supported static dependency consumption coexist.

The missing responsibility is therefore not another generic CI subsystem. It is a bounded correlation responsibility:

```text
static workflow job/step
+
exact-attempt runtime job/step
→ correlated | unresolved/not safely correlatable
```

Only a sound positive correlation may later permit the dependency-CI interpreter to strengthen an execution claim.

## New cycle — exact A-phase responsibility

Determine the **smallest sound static↔runtime correlation contract** UpgradePilot can admit from the evidence it already acquires, before considering job logs or any new runtime data source.

The investigation must answer, in order:

1. Under what bounded conditions can one static workflow job be tied to one runtime `WorkflowJob`?
2. After job correlation is established, under what bounded conditions can one static workflow step be tied to one runtime `WorkflowStep`?
3. What explicit unresolved states are required for matrices, reusable workflows, dynamic/duplicate names, skipped/conditional steps, generated action steps, or other ambiguous shapes?
4. What exact stronger proposition would a successful bridge establish, and what stronger claims would still remain unsupported?
5. Only if existing step summaries cannot support the needed proposition, what precise evidence gap would justify a later read-only job-log slice?

## Current source facts entering A

### Static provider

`src/upgradepilot/github/workflow_definition.py` already preserves:

- `StepsJobDefinition.key` — static `jobs.<job_id>`;
- static job `name` when present;
- `strategy`, including matrix structure as a bounded static value;
- ordered job `source_index`;
- ordered `RunStepDefinition.source_index` / `UsesStepDefinition.source_index`;
- step `name` when present;
- `run:` command for run steps;
- conditions and selected other static execution fields.

`tests/test_github_workflow_definition.py` proves that ordered multi-job structure, literal/dynamic values, matrix strategy structure, ordered steps, and reusable-workflow jobs are preserved rather than flattened.

### Runtime provider

`src/upgradepilot/github/actions.py` preserves:

```text
WorkflowRun:
  run_id
  workflow_id
  head_sha
  run_attempt
  status / conclusion

WorkflowJob:
  job_id
  run_id
  name
  head_sha
  status / conclusion
  optional steps

WorkflowStep:
  number
  name
  status / conclusion
```

Job acquisition is now bound to `(run_id, run_attempt)` and validated against the frozen PR head.

### Existing CI consumer boundary

`src/upgradepilot/ci/dependency_exercise.py` currently uses runtime run/job success plus separately derived static dependency consumption/exercise. It does not inspect runtime steps to correlate a static dependency-related step to execution.

## Initial A findings

### 1. Keep three responsibilities separate

Selected architecture baseline:

```text
STATIC EVIDENCE
        +
RUNTIME EVIDENCE
        ↓
CORRELATION EVIDENCE
        ↓
DEPENDENCY-CI INTERPRETATION
```

Do not collapse static declarations, runtime observations, and correlation conclusions into one authority-bearing object.

### 2. Correlate jobs before steps

A step-level claim depends on knowing which runtime job corresponds to the owning static job. Therefore the first design problem is job correlation.

### 3. Name and ordinal alone are insufficient universal identity

- static/runtime display names are not universal unique keys;
- static `source_index` and runtime step `number` live in different coordinate systems because GitHub adds execution steps around user-declared workflow steps;
- duplicate display names are possible;
- dynamic expressions can prevent literal name resolution.

### 4. Matrix and reusable-workflow shapes are explicit pressure cases

One static matrix job can expand to multiple runtime jobs. A reusable-workflow job delegates execution to another workflow boundary. Neither should be silently forced through a one-static-job↔one-runtime-job assumption.

The first positive admission rule should therefore be designed from a simpler ordinary steps-job shape, while unsupported/ambiguous structures remain explicit unresolved results.

### 5. Logs remain deferred

Do not parse job logs in this A phase. A later log-evidence slice becomes justified only if this design establishes a concrete useful proposition that current runtime summaries cannot discriminate.

## Acceptance intent for A

A is complete when we can state, with source/API evidence:

```text
positive correlation conditions
+ explicit ambiguity/unresolved conditions
+ correct owner/layer for the bridge
+ exact proposition earned by successful correlation
+ proof/test strategy for a later Build slice
+ explicit non-goals
```

A does **not** require implementing the bridge.

## Current design questions

The immediate discriminating questions are:

1. For a non-matrix ordinary steps job, is there a documented/stable relationship between static job identity/name and the runtime job record strong enough for positive correlation?
2. Can ordered runtime step summaries plus literal unique step names support a bounded positive step correlation once the job is known, or does GitHub-generated step behavior leave material ambiguity?
3. Should the correlation result live as a new CI-domain evidence type, with GitHub provider types remaining factual-only?

The third question currently leans **yes** under earliest-sufficient-owner reasoning: GitHub provider objects should remain factual acquisition records; cross-source static↔runtime composition is a CI-domain proposition. A must still verify that against current consumers and accepted semantics before selection.

## Learning-by-Doing state

```text
Slice: CI static↔runtime correlation bridge

A — CURRENT:
    establish the smallest sound correlation contract, owner/layer, ambiguity states,
    exact earned claim, and later proof strategy from current static/runtime evidence.

B — NOT STARTED:
    no implementation authorized until A resolves the material design questions.

C — NOT STARTED
D — NOT STARTED
E — NOT STARTED
```

## Scope exclusions

Do not yet:

- parse/download job logs;
- add exact wheel/version installation semantics;
- reconstruct target environments;
- enable `run targeted checks`;
- change maintainer-action synthesis;
- redesign CLI/reporting;
- force matrix/reusable-workflow support into the first bridge;
- modify product source/tests before A resolves the correlation contract.

`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`
