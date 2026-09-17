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

Current decision state:

```text
A1 exact strengthened proposition     DECIDED
A2 eligibility state model            DECIDED
A3 canonical occurrence identity      OPEN — next
A4 first admitted positive structure  OPEN — next
A5 negative/unresolved structures     OPEN
A6 runtime-correlation composition     OPEN
A7 proof matrix                        OPEN
```

### A1 — Exact strengthened proposition — DECIDED

Cycle 3 may strengthen only these bounded propositions:

```text
exact static dependency-consumption occurrence
→ runtime-correlated dependency-consumption occurrence

exact static direct changed-package exercise occurrence
→ runtime-correlated direct-exercise occurrence
```

The strengthening remains occurrence-relative. It means the exact admitted static occurrence has enough independently justified structure/profile evidence plus exact correlated runtime-step evidence to support the bounded runtime proposition.

It must **not** silently strengthen into any of the following:

```text
exact installed dependency version
selected wheel / sdist identity
package compatibility
complete target-behavior exercise
test-suite completeness
update safety
maintainer action
```

#### A1 rationale

The evidence layers establish different propositions and must remain separate:

```text
parser/static evidence
→ a real static command occurrence exists and has known structure

runtime correlation
→ an exact static GitHub Actions step is matched to an exact runtime step

Cycle 3 eligibility
→ decides whether that step-level runtime result may legitimately strengthen
  this particular internal static occurrence
```

A successful enclosing step is therefore not itself proof that every internal parsed command executed or succeeded. Cycle 3 only bridges that gap when the occurrence structure and execution profile independently justify the inference.

This preserves the accepted core distinction:

```text
static command exists
!= command executed
!= command succeeded
```

### A2 — Eligibility state model — DECIDED

Use an explicit three-way runtime-strengthening eligibility model:

```text
eligible
→ the bounded structure + execution-profile rule positively permits
  correlated step evidence to strengthen this exact occurrence

ineligible
→ the structure/profile relationship is understood and positively does
  not justify that strengthening for this occurrence

unresolved
→ there is insufficient trustworthy parser, structure, or execution-profile
  evidence to decide the stronger proposition safely
```

Do not overload the existing static evidence states to encode this new proposition.

#### A2 rationale

The distinction between `ineligible` and `unresolved` is semantically important:

```text
conditional/path-dependent command
→ ineligible when the structure is understood:
   step success can occur without the command executing

short-circuit alternative
→ ineligible when the structure is understood:
   source presence does not imply execution

material parser ambiguity/error
→ unresolved:
   the structure needed for the eligibility decision is not trustworthy

unresolved shell/execution profile
→ unresolved:
   wrapper/runtime semantics needed for the inference are not established

custom shell template
→ unresolved by default unless a later bounded rule independently
   establishes the required execution semantics
```

`ineligible` therefore means **we understand enough to know that this evidence relationship does not justify strengthening**. `unresolved` means **we do not possess enough trustworthy facts to decide the stronger relationship**.

#### Learning-by-Doing reasoning captured

The first discriminating example compared:

```yaml
# Case A
- run: |
    pip install -r requirements.txt
```

with:

```yaml
# Case B
- run: |
    if false; then
        pip install -r requirements.txt
    fi
    echo done
```

Ali correctly identified the core structural distinction: Case A is straightforward while Case B is conditional. The refined engineering rule is that straightforward/top-level structure is a necessary input to the first positive class, while a conditional occurrence is path-dependent and therefore cannot inherit successful enclosing-step evidence merely from step success.

A second independent requirement remains the **execution profile**: even a straightforward occurrence may be strengthened only when GitHub's wrapper/execution semantics are sufficiently established for the inference being made.

### A3 — Canonical identity carried into runtime strengthening — OPEN / NEXT

The runtime-strengthening decision must operate on the **specific static occurrence**, not merely the enclosing `(job_key, step_source_index)`.

Current Cycle-2 evidence already preserves more than the existing runtime bridge consumes:

```text
outer job/step identity
+ StaticCommandLocation when earned
+ structural_context
```

The current bridge discards the occurrence-level information by reducing supported evidence to `(job_key, step_source_index)` before runtime classification.

The next design questions are:

1. What is the **minimum occurrence-level evidence object** the runtime-strengthening classifier should receive?
2. Can the existing `StaticDependencyConsumptionEvidence` and `DirectPackageInvocationEvidence` carry everything needed, or is a small dedicated eligibility input/result justified?
3. Where should the effective shell/execution profile be attached or recovered so that the classifier does not need to reparse/rederive unrelated static evidence?
4. How do we preserve `StaticCommandLocation` only when it is genuinely earned and avoid inventing inner identity for unresolved step-scoped evidence?
5. Which layer should own the eligibility decision so parser details remain private and runtime correlation remains identity-only?

### A4 — First admitted positive structure — OPEN / NEXT

Decide the precise first eligibility rule for `straightforward_top_level` occurrences.

Current conservative candidate:

```text
cleanly analyzable run step
+ exact target StaticCommandLocation
+ target occurrence is straightforward_top_level
+ first admitted execution profile
+ exact correlated runtime step
+ no continue-on-error masking
+ completed/success runtime result
→ eligible for bounded runtime strengthening
```

The immediate questions are:

1. Should the first positive class require the **entire run block to contain exactly one parsed command occurrence**, or may one eligible occurrence coexist with other top-level commands?
2. If several top-level commands exist, what exact wrapper semantics are needed before a successful step proves the target occurrence executed/succeeded?
3. Which current execution profiles are positively admitted first:
   - GitHub built-in/default Bash/sh;
   - GitHub built-in/default PowerShell/pwsh;
   - GitHub built-in CMD;
   - container-default sh;
   - custom shell templates?
4. Should `custom_shell_template` remain unresolved even when its syntax family is known?
5. What is the smallest first positive set that is useful without pushing Cycle 3 toward shell control-flow simulation?

Current design preference, not yet accepted: begin with the smallest provable positive class, potentially **one straightforward parsed command in the whole run block**, and broaden later only when execution-profile evidence proves additional shapes safely.

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

The Cycle-2 evidence objects already preserve occurrence-level identity/structure that the current runtime bridge discards:

```text
StaticDependencyConsumptionEvidence
→ command_location
→ structural_context

DirectPackageInvocationEvidence
→ command_location
→ structural_context
```

This makes the likely Cycle-3 correction narrower than a new command-identity architecture: preserve and evaluate the existing richer occurrence evidence through the runtime-strengthening boundary instead of reducing it prematurely to step identity.

This remains a design finding, not yet an implementation decision about exact class/function shape.

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

A1 and A2 are now decided. Continue Phase A with A3/A4 before implementation:

```text
1. determine the minimum occurrence-level identity/evidence passed into runtime strengthening;
2. determine where execution_profile joins that occurrence evidence without duplicating parser responsibility;
3. decide the first admitted straightforward_top_level positive class;
4. decide whether the first class is restricted to exactly one parsed command per run block;
5. characterize which built-in/default execution profiles actually justify that first positive inference;
6. then classify A5 negative vs unresolved shapes;
7. compose A6 and the A7 proof matrix from those decisions;
8. only after the complete Phase-A contract is accepted, hand off to implementation.
```

The next Learning-by-Doing reasoning question is:

> Even if a two-command built-in Bash run block may be provable under GitHub's wrapper semantics, why might deliberately admitting only a single straightforward parsed command in the first Cycle-3 positive class still be the better engineering boundary?

`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`
