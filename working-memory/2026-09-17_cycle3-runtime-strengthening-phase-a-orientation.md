# Cycle 3 Phase A — Runtime-Strengthening Eligibility Orientation / Design Working Memory

**Date:** 2026-09-17  
**Session status:** ACTIVE — orientation/design only  
**Responsibility:** define the bounded occurrence-level rule that determines when exact correlated GitHub Actions step success may strengthen a static command occurrence  
**Operation mode:** Planning / Learning-by-Doing pre-implementation orientation; do not modify product source/tests until the Phase-A contract is accepted  
**Predecessor:** [`2026-09-16_cycle2-phase-d-integrated-learning-plan.md`](2026-09-16_cycle2-phase-d-integrated-learning-plan.md) — Cycle 2 D/E closed; remaining deep-dive learning explicitly deferred  
**Selected implementation plan:** [`../plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md`](../plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md)  
**Architecture owner:** [`../docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md`](../docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md)

## 1. Entry state

Closed foundation available to Cycle 3:

```text
Cycle 1
→ effective shell context
→ parser-backed command analysis
→ parser-neutral occurrences / typed atoms / structural context

Cycle 2
→ canonical StaticCommandLocation
→ dependency/project/invocation consumers
→ one-analysis / one-traversal composition
→ bounded static ordered_after | not_after | unresolved
```

Cycle 3 owns the next distinct proposition:

```text
static command occurrence
+ structural/control-flow context
+ effective execution profile
+ exact correlated runtime step evidence
→ may step-level runtime success strengthen this specific command occurrence?
```

It must preserve:

```text
static command exists
!= command executed
!= command succeeded
```

## 2. Current implementation pressure

Current `src/upgradepilot/ci/dependency_exercise.py` keeps static consumption/direct exercise separate from runtime evidence, but the runtime strengthening handoff currently reduces supported static evidence to step-level locations:

```text
(job_key, step_source_index)
```

Then `_classify_runtime_step_execution(...)`:

1. finds the correlated runtime step;
2. verifies the static location is a `RunStepDefinition`;
3. rejects visible/dynamic `continue-on-error` masking;
4. if the correlated runtime step is `completed/success`, returns runtime evidence as supported.

The current classifier therefore reasons primarily about the **enclosing step**, not the exact internal parsed command occurrence.

That creates the known Cycle-3 pressure. Example:

```yaml
- run: |
    if false; then
        pip install -r requirements-dev.txt
    fi
    echo done
```

Cycle 1 may correctly establish a real static `pip install` occurrence inside conditional structure. Cycle 2 may correctly preserve the static declaration. If the enclosing run step succeeds because only `echo done` executes, whole-step success must not automatically strengthen the conditional `pip install` occurrence to executed/succeeded consumption.

The same issue applies to short-circuit/path-dependent invocation shapes and to execution profiles whose wrapper semantics do not justify the inference.

## 3. Accepted architecture constraints

ADR-0009 already decides the following:

- runtime correlation remains CI-owned composition;
- parser structure and effective shell/execution-profile facts are inputs, not runtime truth by themselves;
- successful step evidence may strengthen only command occurrences whose static structure **and** execution profile independently justify the inference;
- conditional, short-circuit, parser-ambiguous, execution-profile-ambiguous, or unsupported shapes must remain static-only/unresolved at the stronger runtime proposition;
- runtime logs are not the primary correction mechanism.

The implementation plan selects a conservative first positive class:

```text
cleanly parsed straightforward top-level command occurrence
+ established syntax family
+ established execution profile
+ exact correlated step success
+ no continue-on-error masking
→ candidate for bounded runtime strengthening
```

Additional linear/chain shapes are not required unless evidence proves the exact implication needed.

## 4. Phase-A design questions

Phase A should resolve these before implementation.

### A1 — Exact strengthened proposition

Define precisely what Cycle 3 is allowed to strengthen.

Candidate distinction:

```text
static dependency consumption declaration
→ runtime-correlated consumption occurrence

static direct changed-package exercise
→ runtime-correlated direct exercise occurrence
```

Do not silently upgrade to exact installed version, selected wheel, package compatibility, or target behavior success.

### A2 — Eligibility state model

Select the smallest explicit state model needed to distinguish at least:

```text
eligible for strengthening
not eligible / path-dependent
unresolved / insufficient execution-profile or parser evidence
```

Do not overload existing static states to encode this new proposition.

### A3 — Canonical identity carried into runtime strengthening

The runtime-strengthening decision must operate on the **specific static occurrence**, not merely the enclosing `(job_key, step_source_index)`.

Determine the minimum identity/evidence object required to preserve:

- outer workflow/job/step identity;
- inner `StaticCommandLocation` when earned;
- structural context;
- effective shell/execution profile;
- static evidence mechanism/proposition.

Do not fabricate inner identity for unresolved step-scoped evidence.

### A4 — First admitted positive structure

Decide the precise first eligibility rule for `straightforward_top_level` occurrences.

Questions to settle:

- whether one eligible occurrence may coexist with other top-level commands in the same run block;
- whether eligibility differs by shell family/execution profile;
- what wrapper-level behavior is actually established for GitHub built-in/default Bash, PowerShell, and CMD profiles;
- how custom shell templates are treated even when syntax family is recognized.

Prefer a smaller positive set over speculative generalization.

### A5 — Negative/unresolved structures

At minimum preserve non-strengthening for:

```text
conditional
short_circuit
loop
pipeline
function_or_block
nested_or_subshell
material parser uncertainty
execution-profile uncertainty
```

Classify which are definitely ineligible versus unresolved; do not conflate the two if the distinction matters downstream.

### A6 — Runtime correlation composition

Determine where the eligibility check belongs relative to:

```text
static evidence classification
→ workflow runtime correlation
→ continue-on-error guard
→ occurrence eligibility
→ runtime evidence result
```

The design should remove the current accidental implication:

```text
supported static evidence somewhere in step
+ step success
→ supported runtime occurrence
```

without weakening the already-proven exact run/job/step correlation boundary.

### A7 — Proof matrix

Before implementation, define representative proofs for at least:

Positive:

```text
straightforward admitted command
+ supported execution profile
+ exact correlated completed/success step
+ no continue-on-error masking
→ runtime strengthening supported
```

Negative/unresolved:

```text
if false; then pip install ...; fi; echo done
true || pip install ...
pipeline/nested occurrence
parser/material ambiguity
custom or unresolved execution profile
continue-on-error true/dynamic
runtime step failed/not completed
runtime correlation unresolved
```

Proof must show both the strengthened claim and explicit non-claims.

## 5. Initial source/test map

Primary current implementation owners:

```text
src/upgradepilot/ci/dependency_exercise.py
src/upgradepilot/ci/workflow_runtime_correlation.py
src/upgradepilot/github/workflow_command_analysis.py
src/upgradepilot/github/workflow_command_shell.py
src/upgradepilot/github/workflow_command_location.py
src/upgradepilot/ci/workflow_commands.py
src/upgradepilot/ci/static_command_order.py
```

Likely proof owners to inspect before implementation:

```text
tests/test_ci_dependency_coverage.py
tests/test_workflow_runtime_correlation.py
tests/test_github_workflow_command_analysis.py
tests/test_ci_static_direct_exercise_order.py
```

Add narrower tests only when Phase-A analysis shows they are needed.

## 6. Immediate technical observation

The current step-level handoff is visible in two helpers:

```text
_supported_consumption_locations(...)
_supported_direct_exercise_locations(...)
```

Both deduplicate to `(job_key, step_source_index)` before `_classify_runtime_step_execution(...)` evaluates successful runtime correlation.

This is the main seam Cycle 3 must redesign or constrain. The new design should preserve the exact occurrence/structure/profile facts needed for eligibility instead of throwing them away before runtime composition.

This is an orientation finding, not yet an implementation decision about exact class/function shape.

## 7. Stop line

Cycle 3 must not expand into:

- arbitrary GitHub expression evaluation;
- matrix expansion or reusable-workflow execution;
- general shell control-flow simulation/CFG construction;
- command-log parsing as the primary execution ledger;
- exact installed dependency version/wheel evidence;
- package behavioral compatibility;
- Python/custom-interpreter command analysis;
- maintainer-action enablement.

If a broader responsibility becomes necessary, return it to planning rather than absorbing it into runtime strengthening.

## 8. Immediate next action

Begin Phase A with the **current runtime bridge**, not implementation:

```text
1. trace workflow_runtime_correlation output and guarantees;
2. trace effective execution-profile states from workflow_command_shell;
3. reproduce the precise conditional/short-circuit overclaim pressure against current dependency_exercise composition;
4. decide A1–A7 as one bounded runtime-strengthening contract;
5. only then authorize implementation.
```

The first learning/design question is practical:

> For a static dependency-consumption occurrence inside a conditional branch, what exact additional facts would be required before a successful enclosing GitHub Actions step could legitimately strengthen that occurrence—and which of those facts do we already possess versus still lack?

`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`