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
A4 strengthened proposition          DECIDED — R2 runtime-correlated support
A4 positive eligibility family        ACTIVE / OPEN
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

#### A4 provisional positive-family direction — accepted for continued design

Ali reviewed the A4 explanation and accepted the current direction as sufficient to continue,
with deeper shell/runtime details intentionally deferred to the implementation/Learning-by-Doing
stage where they become responsibility-bearing.

Current provisional family:

```text
P1 — sole straightforward occurrence
→ clean ordinary top-level target
→ admitted execution profile
→ exact successful runtime step
→ no continue-on-error masking
→ candidate eligible

P2 — first ordinary top-level Bash/sh occurrence in a multi-command run block
→ source_order == 0
→ no conditional / loop / pipeline / short-circuit / nested / function /
   status-inversion / asynchronous masking around the target
→ GitHub Bash/sh profile whose wrapper semantics positively justify fail-fast
→ exact successful runtime step
→ no continue-on-error masking
→ candidate eligible
```

P2 exists to retain meaningful current product coverage such as S002 without admitting all
`linear_chain` occurrences. S004-style sourced-environment + `&&` shapes remain deferred
until their stronger relation semantics are independently justified.

This is **not yet A4 CLOSED**. One remaining proof-boundary caveat must be resolved first:
whether shell startup/environment state (especially `BASH_ENV`) can invalidate the premise
that GitHub's Bash wrapper semantics alone are sufficient to infer target execution/success.

Learning state:

- Ali has operational understanding sufficient to continue A4 design;
- detailed Bash startup, `errexit`, status inversion, and chain semantics are not claimed as
  mastered and should be taught from the actual implementation/proof when those details become
  directly responsibility-bearing;
- do not use the deferred depth as a reason to lower the engineering proof bar.

#### A4 startup/environment reassessment trigger — MATERIAL / OPEN

The remaining `BASH_ENV` caveat was investigated against current GitHub Actions and Bash
semantics and is material enough that P1/P2 must **not** yet be locked as exact
command-execution/success proof.

Authoritative semantics establish:

```text
GitHub built-in/default Bash
→ runner invokes a temporary script with documented Bash fail-fast flags

but

non-interactive Bash
→ reads and executes $BASH_ENV before the script body when BASH_ENV is present
```

GitHub Actions also permits an earlier step to write environment variables to `GITHUB_ENV`;
those values become available to later steps. `BASH_ENV` is not one of the documented
`GITHUB_*` / `RUNNER_*` protected names, and GitHub's documented special block is
`NODE_OPTIONS`, not `BASH_ENV`.

Therefore a valid workflow can conceptually have:

```yaml
- run: |
    echo 'exit 0' > /tmp/prelude
    echo 'BASH_ENV=/tmp/prelude' >> "$GITHUB_ENV"

- run: |
    python -m pip install -r requirements.txt
```

The second step may be reported successful while Bash exits from the startup file before
executing the parsed `pip install` command. A startup file could also modify shell options
before the script body. This breaks the strict implication:

```text
ordinary first/sole Bash command
+ built-in GitHub Bash wrapper
+ successful step
→ exact target command definitely executed/succeeded
```

This is not merely a malicious hypothetical. `BASH_ENV` is a real shell-startup mechanism
and is explicitly treated by public CI/security tooling as a pre-step execution/environment
vector. The project must therefore not hide it behind a normal-case assumption if the owned
proposition is exact command execution/success.

Current provider IR also does not model workflow/job/step `env`, and even adding visible
`env` fields would not fully close the gap because earlier `run` or `uses` steps may
mutate later-step environment through runner files such as `GITHUB_ENV`.

This activates the selected plan/ADR reassessment pressure:

```text
if step-level runtime strengthening remains materially unsound
for the bounded first supported structures
→ reassess the design rather than add ad-hoc positive rules
```

and:

```text
if runtime strengthening actually requires command-level runtime evidence
rather than a bounded static relation to step success
→ return to Planning/Design
```

Phase A is already in Planning/Design, so no implementation rollback is needed.

##### Consequence for the provisional P1/P2 family

P1/P2 remain useful **structural candidates**, but they are no longer accepted as sufficient
for the stronger exact-execution/success proposition.

Do not respond by:

- adding a visible-`BASH_ENV` check and pretending it proves the complete runtime environment;
- treating absence from current workflow IR as evidence of absence;
- marking all preceding actions as safe without exact action/environment evidence;
- introducing broad action-source execution/environment simulation;
- falling back to runtime logs as a primary execution ledger without a separately accepted
  evidence architecture.

##### Next design question

Before A4 can close, decide which proposition UpgradePilot actually needs and can support:

```text
Route R1 — strict occurrence execution/success
→ requires evidence strong enough to establish the exact inner command actually ran/succeeded;
  current step-success + static-structure path is insufficient in the general case.

Route R2 — weaker occurrence-relative runtime association/support
→ exact static occurrence + exact successful owning runtime step + bounded structure/profile
  relationship is retained as stronger contextual evidence,
  but explicitly does NOT claim direct observation/proof of inner-command execution.

Route R3 — narrowly sanitized execution class
→ admit only workflows/environments whose startup/runtime mutation surface is independently
  bounded strongly enough for strict inference;
  likely much narrower and may lose substantial ordinary product coverage.
```

The next step is to compare R1/R2/R3 against the actual downstream CI-coverage proposition and
the Product Decision Model before changing A1, A4, or the implementation plan.

#### A4 proposition selection — DECIDED: R2 runtime-correlated support

After tracing the three reassessment routes into the actual CI coverage consumer,
`PublicPullRequestInvestigation`, the Product Decision Model, and the parent synthesis plan,
Cycle 3 selects **R2**.

The owned strengthened proposition is:

```text
exact supported static command occurrence
+ runtime-strengthening-eligible static structure
+ established execution profile
+ exact correlated completed/successful owning runtime step
+ no visible continue-on-error masking
→ supported runtime-correlated occurrence
```

This is **stronger than static declaration alone**, because the exact owning GitHub Actions
step is known to have completed successfully and the occurrence's static structure/profile
makes that runtime result relevant to the occurrence.

It is deliberately **not** direct command-execution observation. The result must not be
described as proving:

```text
the exact inner command definitely executed
the exact inner command definitely succeeded
the exact dependency version was installed
a particular wheel/sdist was selected
compatibility or complete behavior was proven
the update is safe
a maintainer action is justified
```

##### Why R2 was selected

**R1 — strict inner-command execution/success** was rejected for this cycle because the current
evidence path cannot honestly establish it in the general admitted environment. Step success
is step-level evidence; startup/environment effects such as `BASH_ENV` demonstrate that
static command structure + successful step does not universally equal direct observation of
the inner command. Making R1 trustworthy would require a different/broader evidence
responsibility such as command-level runtime observability, which is outside the current
Cycle-3 boundary.

**R3 — narrowly sanitized execution class** was not selected because proving a sufficiently
closed startup/runtime environment would require materially broader environment/action
modeling while excluding many ordinary workflows. That cost is not justified by the current
downstream product need.

**R2** matches the product's actual current semantics. The parent synthesis plan already
defines `supported_runtime_correlated` as a supported static consuming step safely related
to an exact runtime step that GitHub reports completed/successfully, while explicitly
withholding stronger installed-version/artifact/compatibility/action claims.

##### Product effect

Cycle 3 therefore acts as a **runtime-evidence quality gate**:

```text
static supported occurrence
        ↓
inspect structural context + execution profile
        ↓
eligible?
  yes → exact successful runtime step may strengthen to runtime-correlated support
  no  → preserve static evidence without runtime strengthening
  unknown → preserve unresolved strengthening state
```

Example:

```yaml
run: pip install -r requirements.txt
```

may qualify for stronger runtime-correlated support when the remaining A4 structure/profile
conditions are satisfied.

But:

```yaml
run: |
  if false; then
    pip install -r requirements.txt
  fi
  pytest
```

keeps the `pip install` as useful static evidence while its `conditional` structure prevents
the successful enclosing step from strengthening that occurrence.

##### A1 reconciliation

No A1 redesign is required. A1 already selected the bounded
`runtime-correlated dependency-consumption/direct-exercise occurrence` proposition. R2
clarifies its exact meaning and non-claims; it does not replace it with direct execution proof.

##### Remaining A4 work

A4 is **not fully closed yet**. The proposition is now locked, but the eligibility family still
needs a small bounded refinement:

1. identify the exact structural contexts that are positively eligible for R2;
2. classify known path-dependent structures as ineligible versus unresolved;
3. resolve small missing structural distinctions such as status inversion where they affect
   the gate;
4. characterize the relevant execution-profile matrix without over-modeling shell runtime;
5. then move directly into A5/A6/A7.

Detailed shell mechanics are intentionally deferred to implementation-time Learning-by-Doing
except where they are required to make the remaining eligibility decision sound.

#### A4 eligibility investigation checkpoint — structural taxonomy audit

With R2 fixed, the current parser IR, pinned grammar versions, GitHub runner wrapper source,
and real product-simulation workflows were re-audited specifically for the eligibility gate.

##### What can be reused unchanged

The current parser already exposes useful occurrence-level categories for:

```text
conditional
loop
pipeline
short_circuit
function_or_block
nested_or_subshell
linear_chain
straightforward_top_level
```

These facts are parser-neutral and already flow with canonical command identity. Cycle 3 does
not need a new shell CFG or a second command-analysis system.

##### Important interpretation correction

`straightforward_top_level` currently means:

```text
none of the structural tags implemented by the adapter fired
```

It does **not yet** mean:

```text
all R2-relevant execution/status structure has been positively ruled out
```

That distinction matters because the Bash adapter currently misses several grammar structures
that can make step-level success misleading for a specific inner occurrence.

##### Confirmed Bash structural gaps against pinned tree-sitter-bash 0.25.1

1. **Status inversion — `! command`**

The pinned Bash grammar exposes a named `negated_command` node. Current UpgradePilot Bash
mapping does not inspect that ancestor. An inner command under `!` can therefore currently
fall through to `straightforward_top_level`.

This is material because Bash status inversion changes how command status contributes to the
containing script/result and also interacts with `errexit`.

Required bounded refinement: preserve a parser-neutral status-inversion/non-positive context
before allowing R2 eligibility.

2. **Asynchronous command — `command &`**

The pinned grammar represents `&` as a statement terminator rather than a named command
ancestor. Current structural tagging therefore does not expose that an otherwise ordinary
command was launched asynchronously.

Bash may continue without waiting for that command, and the asynchronous list itself can
produce successful status independently of the command's eventual result.

Required bounded refinement: detect asynchronous termination/relationship at the parser
adapter boundary rather than treating such an occurrence as ordinary straightforward/linear
structure.

3. **Process substitution — `<(command)` / `>(command)`**

The pinned grammar exposes `process_substitution`, and commands can occur underneath it.
Current Bash `nested_or_subshell` tagging checks `subshell` and `command_substitution`
but not `process_substitution`.

Process substitution executes the nested process asynchronously relative to the surrounding
command, so it must not be eligible as if it were an ordinary top-level occurrence.

Required bounded refinement: include process-substitution command occurrences in the
nested/asynchronous non-positive family.

4. **Brace/compound block — `{ command1; command2; }`**

The pinned grammar exposes `compound_statement`. Current static structure vocabulary already
uses the label `function_or_block`, but the Bash mapper currently checks only
`function_definition`, not a top-level brace compound statement.

For a top-level brace block, nested commands can therefore currently receive
`straightforward_top_level` even though they live inside a compound structure whose overall
status/order relationship is not represented by that tag.

Required bounded refinement: map relevant Bash compound-block ancestry into the existing
block/non-positive structural family unless/until a narrower positive relation is separately
proven.

##### Short-circuit precision

The current Bash `short_circuit` tag intentionally merges `&&` and `||`, although the
pinned grammar preserves the concrete operator. That information is proof-relevant if Cycle 3
ever wants to admit selected chain positions.

For the first R2 family, however, **operator splitting is not required if all short-circuit
occurrences remain non-positive**. Therefore do not expand the IR merely to distinguish
`&&` from `||` unless the selected first family actually needs it.

##### Execution-profile evidence from current GitHub runner source

Current `actions/runner` source confirms these built-in/default wrapper facts:

```text
bash        → --noprofile --norc -e -o pipefail {0}
sh          → -e {0}
pwsh/PS     → prepend $ErrorActionPreference='stop'
              + append final LASTEXITCODE propagation
cmd         → /D /E:ON /V:OFF /S /C ...
```

Default non-Windows execution locates Bash when available but applies the `sh` argument
profile (`-e`), while container/default sh remains a distinct profile.

These facts justify profile-aware R2 classification; they do not convert R2 into direct
command-execution proof.

##### Real-case pressure

Current product-simulation evidence gives a useful minimum-generalization target:

```text
S001
→ mostly one-command install/exercise steps
→ straightforward baseline coverage

S002
→ two ordinary commands in one Bash run block
→ changed-dependency install is source_order 0
→ important pressure to support a first straight-line Bash/sh occurrence

S004
→ environment activation/source command + && install chain
→ materially harder relation
→ safe to defer initially if re-entry evidence is stated
```

Therefore the first R2 family should aim to retain S001 + S002 without pretending S004's
stronger shell relation has already been modeled.

##### Current working recommendation — not yet locked

A proportionate first family is trending toward:

```text
P1
sole ordinary straightforward occurrence
+ analyzable step
+ admitted built-in/default execution profile
→ positive R2 candidate

P2
first ordinary top-level/straight-line occurrence
+ Bash/sh fail-fast execution profile
+ none of the R2-defeating structural contexts
→ positive R2 candidate
```

while initially leaving later linear occurrences, short-circuit chains, pipelines, compound
blocks, nested/process-substitution occurrences, status inversion, and asynchronous commands
outside the positive family.

This remains an investigation result rather than an accepted A4 family until PowerShell/CMD
singleton behavior and the final eligible/ineligible/unresolved distinction are reconciled.

#### A4 eligibility investigation checkpoint — positive whole-step proof is required

Further grammar/source review exposed a more general limitation than the individual missing
tags:

```text
StaticCommandOccurrence.source_order
→ order among collected command nodes

but

source_order
!= order among every shell statement/control construct in the script
```

The current collectors intentionally collect only the family-specific ordinary command node
(`command` for Bash/PowerShell, `cmd` for CMD). Other statements remain represented in the
parser tree but do not receive command-occurrence ordinals.

Concrete examples:

- PowerShell has `flow_control_statement` nodes for `return`, `exit`, etc. A target command
  can therefore be `source_order == 0` even when an earlier control-flow statement exists.
- CMD has distinct `goto_stmt` and `exit_stmt` nodes that are not `cmd` occurrences. A
  target can again be the first collected command without being the first executable statement.
- PowerShell also has commands nested under `try`, `trap`, classes/script blocks, and other
  constructs not comprehensively covered by the current negative structural tags.
- Bash top-level brace `compound_statement` similarly contains commands while not itself
  being an ordinary command occurrence.

Therefore these rules would be unsound as the sole A4 basis:

```text
source_order == 0
→ first executable statement          # false in general

one command occurrence in analysis
→ whole script is one simple command  # false in general

no known negative tag
→ positively straightforward          # false until adapter coverage is exhaustive
```

##### Selected design direction from this investigation

For R2 eligibility, prefer a **small positive provider-owned whole-step structural fact** over
an ever-growing downstream blacklist.

Conceptually, the parser adapter should be able to establish only the bounded shapes Cycle 3
actually needs, for example:

```text
sole ordinary top-level command statement

first ordinary top-level command statement
in a top-level sequential Bash/sh script

other / complex / not positively established
```

Exact field/type names remain Build-phase details. The important invariant is:

```text
positive eligibility
→ earned from an explicitly recognized parser shape

not

positive eligibility
→ inferred because no currently-known bad tag happened to fire
```

This is still parser-neutral downstream. Tree-sitter nodes remain private inside the adapter.
It is not a control-flow graph and does not simulate shell execution.

This direction fits A3's already-accepted handoff requirement for the
`minimum whole-step command-analysis shape required by A4`.

##### Proposed first positive R2 family

**P1 — sole ordinary top-level command**

```text
cleanly analyzable step
+ exact target is the sole ordinary top-level command statement
+ no enclosing conditional/nesting/status inversion/asynchronous relation
+ built-in/default admitted execution profile
+ exact correlated completed/success runtime step
+ no visible continue-on-error masking
→ eligible for R2 runtime-correlated support
```

P1 can be admitted across the established built-in/default Bash/sh, PowerShell/pwsh, and CMD
profiles once the adapter positively establishes the whole-step shape. It does not claim
direct observation of the inner command.

Custom shell templates remain unresolved because their wrapper semantics are intentionally
distinct.

**P2 — first ordinary top-level Bash/sh command in a sequential script**

```text
cleanly analyzable Bash-family step
+ exact target is positively established as the first top-level ordinary command statement
+ GitHub built-in/default Bash/sh profile with fail-fast -e semantics
+ target itself is outside -e exception/status-masking structures
+ exact correlated completed/success runtime step
+ no visible continue-on-error masking
→ eligible for R2 runtime-correlated support
```

P2 is justified because the target occurs before later script statements can alter fail-fast
behavior, and the admitted GitHub Bash/sh profiles establish `-e` at shell invocation. R2
still remains runtime-correlated support rather than direct command-level observation.

P2 covers the real S002 install shape without admitting arbitrary later linear occurrences.

##### Deferred positive extensions

Do not absorb these into the first family merely because they can be reasoned about:

- later commands in a generic linear chain;
- `&&` chains;
- pipelines, including explicit-Bash `pipefail` cases;
- brace/compound blocks;
- richer PowerShell/CMD sequences.

Some of these can eventually be positive. For example, a final pure `A && B` relation has
different success semantics from `A || B`, and an explicit Bash pipeline with `pipefail`
has stronger status propagation than default `sh`. But current parser-neutral IR does not
preserve the exact status-contribution relation required to admit those cases safely.

S004 is the concrete re-entry pressure:

```text
. ./generate/bin/activate && pip install ...
```

Supporting that shape later should be driven by an operator/position-aware bounded
status-contribution relation, not by weakening the current `short_circuit` prohibition.

##### Emerging A5 classification

The investigation supports this initial classification:

```text
INELIGIBLE when the known relationship positively allows step success
without useful support for the target:
- conditional target
- loop-body target
- function body / deferred block target
- command/process substitution or other nested asynchronous target
- status-inverted target
- explicitly asynchronous/background target
- OR-chain target once || is positively identified

UNRESOLVED when current facts are insufficient because a potentially positive relation
has been collapsed or the profile/parse boundary is not established:
- current generic short_circuit tag (&& and || collapsed)
- current generic pipeline tag where position/profile matter
- later generic linear-chain occurrences
- complex/other structure not positively recognized
- parse/material ambiguity
- unresolved/unsupported execution profile for this proposition
- custom shell template
```

A straightforward positive whole-step P1 shape and the bounded Bash/sh P2 shape are the
proposed eligible family.

This classification is not yet marked accepted; it is the result to teach/review before
locking A4/A5.

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
1. keep R2 fixed as the exact runtime-strengthened proposition and non-proof boundary;
2. decide the smallest parser-neutral structural refinement needed for the R2 eligibility gate;
3. classify the first positive family and the ineligible/unresolved structures without a general CFG;
4. characterize the relevant execution profiles only to the depth required by R2;
5. test the selected family against S002/S004-style real multi-command pressure and state lost/deferred coverage explicitly;
6. close A4, then classify/finalize A5;
7. compose A6 runtime-correlation ordering from the locked A1–A5 semantics;
8. define the A7 proof matrix;
9. only after the complete Phase-A contract is accepted, hand off to implementation.
```

Next Learning-by-Doing orientation should first teach the small set of concepts needed to decide A4—especially **straight-line execution**, **path dependence**, and **execution-profile failure propagation**—then compare concrete UpgradePilot-relevant script shapes rather than asking Ali to choose between unexplained abstractions.

`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`