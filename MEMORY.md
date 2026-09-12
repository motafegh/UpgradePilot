# UpgradePilot Current Memory

**Last updated:** 2026-09-12  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position

- **Current responsibility:** B-phase Build for the bounded CI static↔runtime correlation bridge. A is complete and selected the smallest sound correlation contract from existing exact-workflow static evidence plus existing exact-attempt runtime job/step evidence.
- **Mode:** Learning-by-Doing; hand off from completed Planning/Design A into Build/Implement B. B is ready but not yet started in source/tests.
- **Selected parent plan:** `plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`.
- **Active working memory:** `working-memory/2026-09-12_ci-static-runtime-correlation-bridge.md`.
- **Previous working memory:** `working-memory/2026-09-11_ci-run-job-attempt-coherence-enhancement.md`.
- **Repository route:** continue directly on `main` unless Ali later requests otherwise.
- **Framework status:** ordinary-Python / LangGraph / LangChain comparison remains closed; no framework re-entry is justified.

## Maintainer-action synthesis state retained

The first deterministic maintainer-action evaluator remains implemented at its admitted abstention-only boundary:

```text
PublicPullRequestInvestigation
→ synthesize_maintainer_action(...)
→ MaintainerActionSynthesis(action="abstain")
```

Established proof at that checkpoint:

```text
focused synthesis tests   2  OK
full repository suite   530  OK
```

No non-abstention action, CLI/application integration, complete report projection, persistence, or objective-safety claim is implemented.

`run targeted checks` remains paused. UpgradePilot is first strengthening its own read-only CI evidence path before deciding whether a maintainer-performed check is justified.

## CI run/job attempt coherence — previous cycle closed

The mixed-rerun-attempt defect is repaired. Job acquisition now uses the exact captured run attempt:

```text
frozen PR head SHA
+ exact workflow run ID
+ exact run attempt
+ jobs acquired from that same attempt
→ coherent factual CI execution evidence
```

Implementation commits:

```text
2cd930afee6127d9f3bfd2fb4492e16f9ec85261  fix: bind workflow jobs to captured run attempt
e01785e7364e015365d9a676792e0f70e9431a17  test: prove workflow job attempt binding
```

Validation on Ali's WSL environment:

```text
focused provider tests      9  OK
nearest CI/application     31  OK
full deterministic suite  533  OK
```

That Learning-by-Doing cycle is CLOSED A→E.

## CI static↔runtime correlation bridge — A complete

UpgradePilot already has:

```text
STATIC WORKFLOW EVIDENCE
→ exact PR-head jobs / strategy / ordered steps / commands / conditions

RUNTIME ACTIONS EVIDENCE
→ exact run + attempt / runtime jobs / runtime step status + conclusion
```

Current `ci/dependency_exercise.py` deliberately keeps them uncorrelated and can return `supported_not_correlated`.

A selected a third CI-domain responsibility:

```text
STATIC EVIDENCE
        +
RUNTIME EVIDENCE
        ↓
CORRELATION EVIDENCE
        ↓
DEPENDENCY-CI INTERPRETATION
```

GitHub provider objects remain factual-only. Correlation is owned by CI because it is a cross-source proposition.

### Job correlation contract selected for first Build

Positive correlation is admitted only for an unambiguous ordinary workflow class:

```text
exact workflow revision == run head
+ exact-attempt jobs already acquired
+ valid WorkflowDefinition
+ all jobs are ordinary StepsJobDefinition
+ no strategy/matrix, reusable job or JobProblem
+ every static job has explicit literal non-expression name
+ static names unique
+ runtime names unique
+ static-name set == runtime-name set
→ one static job key ↔ one runtime job ID
```

Matrix, reusable, dynamic/missing/duplicate-name, or job-set-mismatch shapes remain explicit unresolved results.

A historical real UpgradePilot run established the matrix pressure directly: one static job named `Python ${{ matrix.python-version }}` produced runtime jobs `Python 3.12`, `Python 3.13`, and `Python 3.14`.

### Step correlation contract selected for first Build

Inside an already-correlated job:

```text
no StepProblem
+ all user-declared steps have explicit literal non-expression unique names
+ runtime steps present
+ runtime step numbers unique/ordered
+ every static name appears exactly once at runtime
+ static name sequence is an ordered runtime subsequence
→ static step source_index ↔ runtime step number
```

Runtime-only `Set up job`, `Post ...`, and `Complete job` records are allowed as extra steps. Static source index is never equated directly to runtime step number.

The same real UpgradePilot run showed exactly this shape: user-declared names remained ordered while GitHub inserted setup/post/completion steps and runtime number gaps.

### Correlation is not execution-success policy

Identity and result interpretation remain separate.

A correlated runtime step may be success/failure/cancelled/skipped. A positive successful-step interpretation requires at least:

```text
runtime status == completed
runtime conclusion == success
```

and static `continue-on-error` must be absent or literal false before success is treated as an unmasked successful outcome. GitHub documents that `continue-on-error` can produce conclusion `success` after underlying outcome `failure`.

### Exact claim boundary

The bridge may establish:

```text
for this exact PR head/run attempt,
this statically identified user-defined run step
corresponds to this runtime step,
and GitHub reports this status/conclusion
```

It does **not** establish exact dependency/version installation, shell-segment success, selected/downloaded wheel, wheel compatibility, behavioral compatibility, complete CI coverage, proposal safety, or a maintainer action.

The separate static command-recognition reliability concern remains unchanged.

### Logs remain deferred

No job-log acquisition/parsing is needed for B. Existing step summaries are sufficient for the admitted correlation + step-result proposition.

Logs may be reconsidered only in a later independently justified slice when the selected proposition requires facts such as exact resolved version, downloaded artifact/wheel, or command/output details unavailable from step summaries.

## B handoff

B should:

1. add the smallest CI-domain workflow static↔runtime correlation representation/evaluator;
2. use existing static/runtime provider data — no new GitHub request;
3. integrate correlation into dependency CI coverage so successful correlated static consumption is distinguishable from `supported_not_correlated`;
4. preserve explicit unresolved states/reasons;
5. update downstream assumptions that currently treat `supported_not_correlated` as the only supported CI state, without changing maintainer-action permissions;
6. validate focused correlation cases, nearest CI/investigation regressions, then the full deterministic suite.

Expected proof pressure includes ordinary positive jobs/steps, GitHub-generated extra steps, number gaps, matrix/reusable/dynamic/duplicate/mismatch unresolved cases, skipped/failure outcomes, and `continue-on-error` masking.

No specification/ADR change is selected for this bounded implementation: existing Core/Generality invariants already own separation, provenance, unresolved behavior and minimum useful generality.

## Relevant remaining trust restrictions

1. requirements/constraints patch-to-frozen-head correspondence is not established;
2. static command recognition can produce false-positive direct-requirements evidence from unsupported shell text;
3. run/job attempt coherence is repaired and proven;
4. static dependency declarations are not yet correlated to runtime step execution — B is selected to address this at the bounded named-workflow class only.

## Immediate continuation — canonical LbD cycle

```text
Slice: CI static↔runtime correlation bridge

A — DONE:
    selected job/step correlation contract, owner/layer, unresolved cases, exact claim limits,
    real GitHub/UpgradePilot pressure evidence, no-log boundary and Build proof strategy.

B — READY / NOT STARTED:
    implement the bounded CI correlation evaluator and integrate the stronger technical
    evidence state without adding logs, wheel semantics or maintainer-action permissions.

C — NOT STARTED
D — NOT STARTED
E — NOT STARTED
```

Do not in B parse logs, add wheel-serviceability semantics, reconstruct target environments beyond existing behavior, enable `run targeted checks`, add non-abstention maintainer actions, or redesign CLI/reporting.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`  
`UP-SKILL:upgradepilot-planning-design`
