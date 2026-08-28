# B2/X1 Action-Failure and Retry-Boundary Transfer Evaluation

**Date:** 2026-08-28  
**Status:** PRODUCT-SIMULATION CROSS-LAYER EVALUATION — non-controlling discovery/transfer evidence  
**Evaluated main revision:** `5af853d0ebe3e510c33a3b94c1d14bd8106f8b28`  
**Primary current evidence:** Phase-1 A1 seam inventory, planner contract/tests, GitHub acquisition taxonomy, target-Python interpretation  
**Related transfer assets:** `../b2-x1-no-tool-disposition-transfer/README.md`, `../b2-x1-pre-execution-action-staleness/README.md`

## 1. Evaluation question

This bounded evaluation asks:

> When the one admitted planner action has already been attempted and did not yield the desired success evidence, which failures should block model-level repetition, and which failures may still justify a deterministic transport/execution retry owned outside the planner?

The purpose is to avoid two opposite errors:

```text
BLIND RETRY
model keeps selecting the same action because the proposition is still unresolved

OVER-SUPPRESSION
one transient transport failure is collapsed into "problem"
→ planner/executor permanently refuses a retry that could still acquire the exact evidence
```

This evaluation does not implement retries, expand the action catalog, or change current planner semantics during the Learning-Only pause.

---

## 2. Why this is a separate pressure from pre-execution staleness

Pre-execution staleness asks:

```text
action was valid at T1
+ state changed before execution
→ is action still useful/actionable?
```

This evaluation asks:

```text
action execution/acquisition was attempted
→ what kind of failure/problem occurred?
→ should that same planner action be considered consumed?
```

Both concern lifecycle correctness, but the causal mechanism is different.

---

## 3. Current planner repeat guard

`AttemptedInvestigationAction` currently records only:

```text
action_id
outcome = completed | problem | rejected
```

`admit_agent_plan(...)` then rejects a selected action if **any** attempted-action record already contains that action ID.

The current focused test makes the pilot intent explicit:

```text
attempted A1 outcome = problem
+ planner selects A1 again
→ admission problem: action_already_attempted
```

This is a strong guard against **blind model-level repetition**.

It is deliberately simple for the one-action pilot.

---

## 4. Phase-1 intent confirms the repeat guard is deliberate

The Phase-1 seam inventory describes A1 as an immutable exact-file read:

```text
same immutable repository + head SHA + fixed path
→ repeat read is logically idempotent
```

but immediately adds:

```text
attempt history should still prevent blind redundant retries
after an available/problem result
```

This separates two ideas that must not be conflated:

```text
idempotent
!=
worth repeating indefinitely
```

A read can be safe to repeat while still being useless to repeat after a definitive result.

---

## 5. Current result family is not the same as provider transport failure

The A1 action declares deterministic result families:

```text
TargetPythonDeclaration
TargetPythonDeclarationProblem
```

The target-Python interpreter defines typed problem states:

```text
file_unavailable
malformed_toml
project_table_absent
requires_python_absent
invalid_requires_python
```

These are domain/evidence outcomes about the exact target declaration boundary.

They are materially different from low-level provider transport failures.

---

## 6. GitHub provider taxonomy preserves important failure distinctions

The GitHub provider boundary distinguishes acquisition failures before a usable successful body exists.

`GitHubAcquisitionError.reason` includes:

```text
timeout
transport_error
not_found_or_inaccessible
forbidden_or_rate_limited
http_error
```

It also has `GitHubResponseError` for successful HTTP responses whose returned data cannot be trusted as GitHub evidence.

The repository-file owner treats these categories differently.

### 6.1 `not_found_or_inaccessible`

For an exact repository file, this category is converted into:

```text
UnavailableRepositoryFile
```

which then becomes:

```text
TargetPythonDeclarationProblem(state="file_unavailable")
```

So this becomes typed evidence/problem state at the target-Python boundary.

### 6.2 timeout / transport / rate-limit / other HTTP acquisition failure

These are **not** converted into `UnavailableRepositoryFile` by `GitHubRepositoryClient._get_exact_repository_text_file(...)`.

They propagate as acquisition exceptions.

Therefore:

```text
GitHub request failed operationally
!=
exact target file is semantically unavailable/malformed/missing declaration
```

### 6.3 untrusted successful response

Malformed/untrustworthy GitHub response shape/encoding/path data becomes `GitHubResponseError`.

Again:

```text
provider response cannot be trusted
!=
target declaration proposition refuted
```

This existing failure taxonomy is a strong product foundation and should not be flattened at future planner-execution integration.

---

## 7. Core transfer invariant

The bounded transfer principle is:

> **Planner action history should prevent blind semantic repetition of an already-consumed investigation, while deterministic execution may separately own bounded retries for transient operational failures that never became a valid action result/evidence update.**

In compact form:

```text
planner selects action A once
        ↓
deterministic executor attempts A
        ↓
classify outcome

VALID SUCCESS / TYPED DOMAIN PROBLEM
→ action attempt becomes part of trusted history
→ do not ask model to blindly select A again

TRANSIENT TRANSPORT/ACQUISITION FAILURE
→ no evidence proposition should be fabricated from failure
→ deterministic executor may apply bounded provider-specific retry policy if authorized
→ model need not re-plan merely to say "try same HTTP GET again"

UNTRUSTED/MALFORMED PROVIDER RESPONSE
→ fail closed
→ preserve source/acquisition problem separately
→ retry policy, if any, remains deterministic and evidence-bounded
```

This keeps planning and transport concerns at the correct owners.

---

## 8. Standard engineering concepts directly relevant here

### 8.1 Idempotency

A1 reads an immutable repository revision/path, so repeating the same read should not mutate target state.

That makes a bounded transport retry technically safer than retrying a mutation.

But idempotency is only a **safety property** of repeating the operation. It does not prove retry is useful.

### 8.2 Transient vs permanent/domain failure

A timeout and a missing `[project].requires-python` declaration are not the same failure class.

One may be transient operational inability to acquire evidence.
The other is a successful acquisition followed by a stable domain interpretation result.

### 8.3 Transport retry vs semantic retry

```text
transport retry
→ repeat same bounded request because delivery/acquisition failed

semantic retry
→ ask model/planner again because previous reasoning/action result was unsatisfactory
```

The first can often remain deterministic.
The second risks hiding model/planner weakness or creating loops.

### 8.4 Backoff / rate-limit handling

Rate limiting is a recognizable provider concern that may eventually justify `Retry-After`, bounded backoff, or deferred execution.

No current evidence requires implementing such a policy in X1 now.

---

## 9. Why model-driven "retry the same action" is the wrong first abstraction

Suppose A1 encounters a timeout.

A weak design could do:

```text
executor reports generic problem
→ snapshot still unresolved
→ model sees A1 again
→ model selects A1 again
→ repeat until budget exhausted
```

That wastes model calls and moves transport policy into an untrusted planner.

A cleaner separation is:

```text
model selected A1 once
→ deterministic executor owns one bounded attempt policy
→ operational retry, if authorized, happens inside that execution responsibility
→ only resulting typed evidence/problem is returned to planner state
```

This is conceptually similar to tool-call middleware/retry wrappers used in agent systems, but UpgradePilot does not need a framework merely to preserve the responsibility split.

---

## 10. Important current limitation: planner attempt outcome is coarse

`AttemptedInvestigationAction.outcome` currently has only:

```text
completed
problem
rejected
```

That is adequate for the current pilot's simple no-blind-repeat contract.

But it is **not by itself sufficient** to encode a complete future retry policy.

If future integration writes all of these into `outcome="problem"`:

```text
typed file unavailable
malformed target TOML
network timeout
rate limit
provider transport failure
untrusted response shape
```

then the snapshot would lose distinctions the lower provider/domain layers already preserve.

This evaluation therefore finds a future integration pressure:

> Do not collapse lower-layer failure taxonomy into one planner history label if that collapse changes whether execution should be retried, deferred, or treated as stable evidence/problem state.

This does **not** request new enum values now.

---

## 11. Relationship to `d-repeat-stop`

The accepted development case `d-repeat-stop` says:

```text
exact_target_python_declaration_established
→ unresolved / insufficient

A1 available
A1 already attempted = problem
remaining_steps = 1
→ expected stop
```

For the current evaluation contract, this is useful because it proves:

```text
remaining unresolved
+
remaining budget
!=
permission to blindly repeat the same action
```

The case should remain.

Its meaning should be interpreted narrowly:

> the planner must not reselect an action already represented as an attempted problem in trusted action history.

It should **not** be generalized into:

> every provider transport failure in a future executor permanently consumes all retry opportunity.

---

## 12. Current source suggests a natural owner split

A future executor can preserve three levels:

### Level A — provider acquisition

Owns:

- HTTP/network failure classification;
- timeout/rate-limit semantics;
- response trust/shape;
- optional bounded transport retry policy if later authorized.

### Level B — domain action execution/result interpretation

Owns:

- `RepositoryTextFile | UnavailableRepositoryFile`;
- `TargetPythonDeclaration | TargetPythonDeclarationProblem`;
- promotion into proposition/evidence state.

### Level C — planner history

Owns only the fact needed for future planning:

- which admitted investigation was already meaningfully attempted/consumed;
- enough bounded outcome information to prevent blind repetition without erasing decision-relevant failure distinctions.

The exact future data model is not selected here.

---

## 13. Failure heuristics this pressure exposes

### H-RY-01 — all failures are tool results

```text
timeout
→ TargetPythonDeclarationProblem
```

Wrong under current source ownership. Timeout is acquisition failure, not target-declaration evidence.

### H-RY-02 — all `problem` outcomes are retryable

```text
requires-python absent
→ just run A1 again
```

Repeating the same immutable file read adds no information unless some external condition meaningfully changed.

### H-RY-03 — all `problem` outcomes are permanently non-retryable

```text
rate limit once
→ never retry exact read
```

Potentially over-suppresses a transient provider condition if future execution policy admits a bounded retry.

### H-RY-04 — let the model manage HTTP retries

Moves deterministic transport behavior into untrusted reasoning and spends planner budget/model calls on a provider concern.

### H-RY-05 — idempotent means unlimited retries are harmless

Idempotency prevents mutation side effects; it does not prevent cost, latency, rate-limit amplification, or redundant investigation.

### H-RY-06 — acquisition failure means proposition negative

```text
could not fetch file
→ target does not declare Python range
```

Violates evidence doctrine.

---

## 14. Current Phase-4A responsibility and stop line

The current Phase-4A development smoke performs no planner-selected capability execution.

Therefore:

- no A1 GitHub request is executed by the smoke;
- no attempt-history transition is produced from real capability execution;
- no executor transport retry policy is currently needed for the smoke;
- model request transport and action execution transport remain different responsibilities.

Do not delay Phase-4A to implement executor retries.

---

## 15. Future minimal implementation pressure

When product/experiment work reaches actual A1 execution, the smallest useful design question is:

> What exact outcome boundary causes an action to enter planner-visible `attempted_actions`, and which operational failures remain inside deterministic executor retry/failure handling instead?

A proportionate future test matrix could distinguish:

```text
A1 success
→ completed / proposition updates

exact file unavailable or domain declaration problem
→ stable typed problem / action consumed for same immutable state

timeout / transport error
→ acquisition failure, no false proposition update
→ bounded deterministic retry/defer policy if explicitly designed

rate limited
→ acquisition failure with provider-specific handling

untrusted successful response
→ fail closed as source/response problem
```

No implementation is authorized by this simulation record.

---

## 16. Transfer findings

### F-RY-01 — CONFIRMED

Current no-blind-repeat admission is a sound pilot guard and should not be weakened merely because A1 is idempotent.

### F-RY-02 — CONFIRMED

The lower GitHub/target-Python layers already preserve a more useful failure taxonomy than the planner's coarse `problem` history label.

Future integration should not destroy those distinctions when they materially affect retry/defer/evidence semantics.

### F-RY-03 — CONFIRMED

Transient transport retry is better owned by deterministic provider/executor policy than by repeated model selection of the same action.

### F-RY-04 — CONFIRMED

A typed target-declaration problem and a transport/acquisition failure must not be treated as equivalent evidence states.

### F-RY-05 — NO CURRENT BLOCKER

The current Phase-4A smoke executes no planner capability, so executor retry semantics are future integration pressure rather than a blocker now.

---

## 17. Methods and barriers

### M/B-RY-01 — no real planner executor exists yet

The current experiment stops at deterministic admission and development evidence. This evaluation therefore traces existing provider/domain owners rather than pretending an execution loop already exists.

### M/B-RY-02 — no new scenario required

The real A1 source path and existing provider taxonomy already answer the ownership question. A new public scenario would add case count without materially increasing discrimination.

### M/B-RY-03 — no local runtime validation in this session

Current source/tests are inspected from GitHub. No WSL tests were executed, so the findings are source/evidence-transfer conclusions rather than fresh runtime validation.

### M/B-RY-04 — moving main remained a repository-maintenance pressure

`main` advanced again during the prior S007 slice with Build-Skill routing refinements. That governance change did not alter this evaluation's action boundary, but the simulation branch was synchronized before this follow-on analysis so current governance remained in force.

---

## 18. Claim limits

This evaluation does not establish:

- an exact retry count;
- exponential-backoff parameters;
- mandatory `Retry-After` handling;
- new planner outcome enums;
- a production executor API;
- automatic retries for every idempotent action;
- that all 404/inaccessible responses are permanently stable across time/permissions;
- planner reliability;
- runtime compatibility or safety;
- maintainer action.

---

## 19. Stopping decision

The bounded question is sufficiently answered.

```text
current planner repeat guard
→ correctly prevents blind model-level action repetition

current provider/domain taxonomy
→ already distinguishes semantic/evidence problems from operational acquisition failures

future integration duty
→ preserve that distinction when mapping execution outcome into planner history
→ keep transient transport retry, if any, deterministic and bounded

current Phase-4A
→ no action execution
→ no retry implementation blocker
```

No further retry machinery or scenario is justified at this stage.
