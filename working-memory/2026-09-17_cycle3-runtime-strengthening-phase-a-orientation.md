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

The implementation plan selects a conservative first positive direction:

```text
cleanly parsed straightforward top-level command occurrence
+ established syntax family
+ established execution profile
+ exact correlated step success
+ no continue-on-error masking
→ candidate for bounded runtime strengthening
```

Additional linear/chain shapes are not required by the written baseline unless evidence proves the exact implication needed. This plan remains important coordination evidence, but Phase A may refine the route when stronger product/engineering reasoning justifies it without violating the accepted architecture or scope.

## 4. Phase-A design questions

Current decision state:

```text
A1 exact strengthened proposition     DECIDED
A2 eligibility state model            DECIDED
A3 canonical occurrence handoff       DECIDED
A4 first admitted positive family     ACTIVE / OPEN
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

Ali correctly identified the core structural distinction: Case A is straightforward while Case B is conditional. The refined engineering rule is that straightforward/top-level structure is a necessary input to the first positive family, while a conditional occurrence is path-dependent and therefore cannot inherit successful enclosing-step evidence merely from step success.

A second independent requirement remains the **execution profile**: even a straightforward occurrence may be strengthened only when GitHub's wrapper/execution semantics are sufficiently established for the inference being made.

### A3 — Canonical occurrence handoff into runtime strengthening — DECIDED

Introduce one narrow **CI-owned runtime-strengthening candidate/input** for a specific static command occurrence rather than passing the full static dependency-consumption or direct-invocation evidence objects into the eligibility classifier.

Conceptually the handoff preserves/references only the facts the runtime-strengthening responsibility needs:

```text
outer job + step identity
+ canonical StaticCommandLocation
+ structural_context
+ effective execution_profile
+ minimum whole-step command-analysis shape required by A4
+ static proposition kind being strengthened
```

The exact class/type/function spelling remains an implementation detail for the Build phase. Phase A locks the responsibility and information boundary, not the final identifier name.

#### A3 identity rule

`StaticCommandLocation` remains the **single canonical inner command identity**. Cycle 3 must not create a second command-identity scheme.

The runtime-strengthening input therefore **references/composes existing provider-owned facts** rather than redefining them:

```text
StaticCommandLocation
→ exact parser-neutral static occurrence identity

structural_context
→ parser-backed structure fact

execution_profile
→ effective-shell/provider fact

job / step identity
→ static workflow-definition fact

static proposition kind
→ CI/domain composition fact
```

None of these facts independently proves execution or success.

#### A3 rationale

The current one-traversal static path already has the full `StaticCommandAnalysis` at the point consumption/project-environment/direct-invocation evidence is created. That analysis already contains the resolved shell context, including `execution_profile`, while exact occurrences already carry canonical location and structural context.

Therefore Cycle 3 should preserve the **small subset needed for later eligibility** at this existing composition point. It should not discard those facts and later reparse the script or re-resolve shell context inside `dependency_exercise.py`.

This yields the bounded flow:

```text
one StaticCommandAnalysis
→ static domain interpretation
→ narrow occurrence-level runtime-strengthening candidate
→ exact step correlation
→ eligibility/runtime composition
```

This keeps one-analysis/one-traversal ownership from Cycle 2 and avoids duplicate static interpretation.

#### Rejected A3 alternative

Do **not** make the runtime-strengthening classifier consume `StaticDependencyConsumptionEvidence` / `DirectPackageInvocationEvidence` directly as its primary contract.

Reason:

- those objects own richer static domain propositions and carry many fields irrelevant to eligibility;
- runtime strengthening would become coupled to dependency/reachability-specific details;
- adding `execution_profile`, whole-step shape, and future eligibility metadata directly to those objects would blur static-domain evidence with the distinct Cycle-3 runtime bridge;
- the eligibility layer should remain equally usable for the two A1 propositions without learning all of each producer's internals.

A dedicated narrow handoff is therefore the simpler ownership boundary despite introducing one small composition type.

#### Explicit non-responsibilities of the A3 handoff

The handoff must **not**:

- create a second command identity;
- contain or own the runtime result itself;
- decide `eligible | ineligible | unresolved` merely by existing;
- duplicate dependency reachability/source details;
- expose Tree-sitter nodes;
- reparse the workflow command;
- re-resolve effective shell context later;
- claim that the command executed or succeeded.

Runtime correlation remains identity-only at the outer job/step boundary; occurrence eligibility remains a separate CI composition responsibility.

### Session correction — product-faithful boundedness and decision readiness

During A4 discussion, Ali raised a material concern with the proposed **“exactly one parsed command in the entire run block”** first rule: repeated preference for the smallest provable implementation could unintentionally reduce useful UpgradePilot behavior simply because the smaller slice is easier to build and pass.

This correction is accepted as a durable operating principle and has been promoted to root `AGENTS.md`, `OPERATING_GUIDE.md`, and live `MEMORY.md`.

For this session it means:

```text
written plan / accepted boundary
→ important starting route and constraint evidence
→ not a command to preserve a weaker local design when better evidence/reasoning emerges

bounded slice
→ must remain connected to the real product responsibility
→ must state what useful capability/evidence is omitted or deferred
→ must not optimize merely for implementation ease or test passing

consequential unfamiliar decision
→ AI first supplies the minimum decision-relevant technical model
→ explains gains / losses / deferrals / future expansion cost
→ gives a reasoned engineering recommendation when warranted
→ then asks Ali to challenge/select at an informed boundary
```

This does **not** authorize arbitrary scope expansion or bypass accepted specifications/ADRs/stop lines. A materially better route that changes the selected plan/design must be returned to the proper owner and recorded before implementation.

### A4 — First admitted positive family — ACTIVE / OPEN

A4 is **not** now framed as “one command versus everything else.” It asks:

> For which exact static structural shapes and established GitHub execution profiles does successful completion of the correlated step logically justify strengthening this specific target occurrence?

The earlier one-command rule remains a valuable baseline proof case:

```text
cleanly analyzable run step
+ one exact straightforward_top_level target occurrence
+ admitted execution profile
+ exact correlated runtime step
+ no continue-on-error masking
+ completed/success runtime result
→ strong candidate for eligibility
```

But **“the whole run block must contain exactly one parsed command” is not accepted as the product rule**. It would exclude ordinary straight-line multi-command CI scripts without first establishing that such exclusion is necessary.

A4 must evaluate a product-faithful positive family, including whether cases such as this can be supported safely:

```yaml
- shell: bash
  run: |
    echo preparing
    pip install -r requirements.txt
    pytest
```

The relevant question is not merely command count. It is whether the target occurrence is on an execution-mandatory straight-line path **and** whether the established execution profile makes successful enclosing-step completion strong enough to establish the bounded target proposition.

Immediate A4 questions:

1. What exact structural facts already emitted by `workflow_command_analysis.py` distinguish a mandatory straight-line target from path-dependent/nested targets?
2. Does the current `straightforward_top_level` / `linear_chain` representation contain enough relation information for ordinary multi-command scripts, or is one additional bounded step-level shape fact needed?
3. Which execution profiles positively justify failure/success propagation for the required inference:
   - GitHub built-in/default Bash/sh;
   - GitHub built-in/default PowerShell/pwsh;
   - GitHub built-in CMD;
   - container-default sh;
   - custom shell templates?
4. Which common CI cases would be lost if the first rule admitted only one-command run blocks, and is that loss technically justified?
5. Can a useful multi-command positive family be proven **without** building a general shell CFG/control-flow simulator?
6. Which combinations are definitely `ineligible` versus merely `unresolved`?

Current design stance:

```text
prefer the smallest PROVEN family
!= prefer the smallest IMPLEMENTABLE case
```

The selected family should be no broader than the evidence earns and no narrower than is justified by product/proof constraints.

#### A4 investigation checkpoint — current IR is not yet sufficient for eligibility

Source + current execution-semantics review established four material facts:

1. **Existing identity/order facts are useful but insufficient by themselves.**
   `StaticCommandOccurrence.source_order` can identify the first parsed occurrence, and
   `structural_context` distinguishes several important path-dependent structures. That is
   enough to express candidates, but not yet enough to prove the runtime-strengthening rule.

2. **Bash negation is currently an uncovered structural case.**
   Tree-sitter Bash exposes a named `negated_command` structure, while the current
   `_structural_context(...)` mapping does not tag it. Bash `errexit` (`-e`) explicitly
   does not exit when a command status is inverted with `!`. Therefore a command such as
   `! python -m pip install ...` must not accidentally remain
   `straightforward_top_level` for runtime-strengthening purposes.

3. **Current `short_circuit` loses a proof-relevant distinction.**
   Bash `&&` and `||` are both currently mapped to `short_circuit`, although their
   success implications differ. A successful `A || B` does not prove that B executed, nor
   that A succeeded. A successful terminal/unmasked `A && B` can provide a stronger
   relation: both sides must have executed successfully for that list to succeed. Any future
   positive use still has to account for surrounding structure/status masking and negation.

4. **Generic newline/separator `linear_chain` is not sufficient proof of per-command success.**
   GitHub's built-in/default Bash/sh profiles use fail-fast behavior, but the script can
   contain shell-state/control operations such as `set +e`, sourcing, or early termination
   that defeat a naive “linear + step success ⇒ every command succeeded” rule. PowerShell
   documents fail-fast only “when possible” and appends the final native
   `LASTEXITCODE`; CMD explicitly does not provide general fail-fast behavior. Therefore
   one cross-shell `linear_chain` rule would overclaim.

Product pressure confirms this is not academic. Real product-simulation evidence includes:

```yaml
# S002 — ordinary multi-command install step
run: |
  python -m pip install --no-cache-dir --upgrade pip -r requirements.txt
  python -m pip install ruff
```

and S004 includes multi-line Bash plus a sourced virtual environment and an `&&` install
chain. A permanent one-command-only policy would therefore lose runtime-strengthening
coverage for real current cases; however admitting all linear chains would be unsound.

The resulting A4 design direction is:

```text
do not add a general shell CFG/interpreter

instead:
→ refine the parser-neutral relation surface only where runtime proof needs it
→ distinguish status inversion / proof-relevant chain operator semantics
→ keep generic path-dependent or status-masked shapes non-strengthenable
→ characterize positive families per execution profile
→ make lost/deferred real-case coverage explicit
```

The next decision is whether the smallest adequate IR refinement should be:

```text
A. additional structural tags only
   e.g. status_inverted + and_chain/or_chain distinction

or

B. one small parser-neutral static relation dedicated to how an occurrence contributes
   to the containing run-step result, while still remaining purely static and
   execution-profile-independent
```

No implementation is authorized yet; this checkpoint only establishes why A4 cannot be
correctly decided from the current `straightforward_top_level | linear_chain | short_circuit`
tags alone.

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
straightforward admitted command/family
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

The proof matrix must include representative ordinary multi-command cases if A4 admits them, and must show both the strengthened claim and explicit non-claims.

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

Cycle 2 already preserves the exact occurrence identity/structure, and the one-traversal command-analysis point already owns `execution_profile`. A3 therefore locks the Cycle-3 correction as a **narrow occurrence-level handoff/composition**, not a new parser, new command identity, or later re-derivation path.

The implementation shape should preserve those facts before the current reduction to step identity occurs.

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

A1, A2, and A3 are decided. Continue Phase A with A4 before implementation:

```text
1. decide the smallest parser-neutral A4 relation refinement needed for runtime proof;
2. ensure the refinement covers status inversion and preserves the && versus || proof distinction without becoming a general CFG;
3. characterize the positive family separately for Bash/sh, PowerShell, CMD, container-default sh, and custom templates;
4. test the selected family against S002/S004-style real multi-command pressure and state lost/deferred coverage explicitly;
5. lock A4 only when the positive family is both proof-sound and product-faithful;
6. classify A5 negative vs unresolved structures;
7. compose A6 runtime-correlation ordering from the locked A1–A5 semantics;
8. define the A7 proof matrix;
9. only after the complete Phase-A contract is accepted, hand off to implementation.
```

Next Learning-by-Doing orientation should first teach the small set of concepts needed to decide A4—especially **straight-line execution**, **path dependence**, and **execution-profile failure propagation**—then compare concrete UpgradePilot-relevant script shapes rather than asking Ali to choose between unexplained abstractions.

`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`