# Lifecycle host, material validity and execution truth

**Educational snapshot:** repository horizon **`5187f40ba974341eb29d765363f093922a881803`**, 2026-10-16. The production Stage 3 host implementation and tests are present unchanged at this horizon. Stage 3 engineering/Verification and its deferred D ownership review are closed; this note preserves that verified mechanism for later relearning.

**Responsibility:** understand how UpgradePilot records why work was requested, whether it was currently allowed to execute, what actually happened, and whether the original material can still be used later—without letting the generic host become a domain evaluator or maintainer-action owner.

## Core mental model

Stage 1–2 answered:

> How do we retain native owner results and recover them later?

Stage 3 answers a different question:

> How do we retain the lifecycle around new investigative work and decide whether historical work is still usable/executable now?

The production flow is:

```text
owner/admitted purpose
        ↓
CapabilityRequest
        ↓
current admission decision
        ↓
durable ExecutionAttempt(intent_recorded)
        ↓
external capability interaction
        ↓
CapabilityObservation
or ExecutionInterruption
        ↓
qualified native owner reassessment when admitted
        ↓
EvaluationOutcome + new immutable Workspace revision
```

Four concepts must remain separate:

```text
ORIGINAL BASIS
what historical material/method/scope the record depended on

CURRENT MATERIAL VALIDITY
whether that historical basis still matches the present state

CURRENT EXECUTION AUTHORITY
whether the host is presently allowed to perform the capability/effects

PUBLICATION PREDECESSOR
which immutable Workspace revision a writer is extending
```

These are related, but none is a substitute for another.

## 1. Lifecycle records are facts, not execution policy

Start with [`lifecycle_records.py`](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/src/upgradepilot/workspace/lifecycle_records.py).

Important retained values include:

```text
DiscoveryObjective
InvestigationNeed
CapabilityRequest
RequestAdmission
ExecutionAttempt
CapabilityObservation
ExecutionInterruption
EvaluationOutcome
ConsumerView
ViewDelivery
ObservableUse
AttributedProposal
ContentCitation
ProceduralTermination
StoppingProposal
```

The names are intentionally specific because each answers a different historical question.

For example:

```text
RequestAdmission(admitted)
```

means the request was admitted under the authority/policy that existed at that historical point.

It does **not** mean:

```text
this recovered admission may execute again now
```

Likewise:

```text
ProceduralTermination(completed)
```

means the run reached its procedural completion state.

It does **not** establish:

```text
investigation adequate
upgrade safe
maintainer action permitted
```

The module-level contract states this directly: request/admission/attempt/observation/evaluation are distinct facts, and historical admission grants no current capability authority.

## 2. The generic host owns orchestration and current execution authority

Open [`lifecycle_host.py`](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/src/upgradepilot/workspace/lifecycle_host.py).

`InvestigationWorkspaceHost` owns:

- installed trusted capabilities and their declared effects;
- current execution authority for the exact target;
- request admission/rejection;
- publication of intent before capability execution;
- observations/interruption states;
- lifecycle history publication;
- current material-basis checks;
- view/proposal/use bookkeeping;
- invocation of an explicitly admitted native evaluator.

It does **not** own the semantic meaning of CI, Python compatibility, source claims, adequacy or maintainer action.

A `HostCapability` is installed by trusted composition. A request, proposal, file or recovered lifecycle record cannot install a capability.

That gives this boundary:

```text
consumer/model may ask or propose
        ↓
host may coordinate/admit/execute
        ↓
qualified domain owner establishes semantic result
```

not:

```text
consumer/model proposal
→ host promotes it to product truth
```

## 3. Current authority is present-time state

`ExecutionAuthority` binds:

```text
exact target
allowed capability names
allowed effects
```

Before execution, `_execution_refusal(...)` checks:

- current host authority exists;
- authority still belongs to the current exact target;
- capability is installed and authorized;
- declared capability effects are within current allowed effects;
- the request's material basis is still valid.

So even a historically admitted request can be blocked later.

This is why recovery clears live authority and live admission receipts. `restore(...)` reconstructs history, then sets current execution authority to `None` and clears `_live_admissions`.

Therefore:

```text
historical admission
!= current permission to execute
```

## 4. Original basis is immutable historical provenance

Every lifecycle record is tied to an original basis revision and native material references.

That historical basis is not rewritten when the Workspace advances.

Suppose request Q was created from native records A/B/C at revision R5. Later the Workspace reaches R8.

The correct question is not:

```text
R5 != R8
→ stale
```

The correct question is:

```text
are A/B/C and the exact target/scope/method/capability bindings still equivalent in the current state?
```

This distinction is implemented by [`material_validity.py`](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/src/upgradepilot/workspace/material_validity.py).

## 5. Material validity is dependency-relative, not revision-relative

`native_material_closure(...)` follows the actual retained native input references for the roots a lifecycle record depends on.

`validate_current_material_basis(...)` then compares:

```text
exact target
scope
capability availability
method identity
transitive referenced native material
```

Possible states are:

```text
valid
stale
unsupported
```

### Valid

Unrelated same-target progress occurred, but the lifecycle record's actual material closure and method/scope/capability bindings are unchanged.

### Stale

Examples:

```text
target changed
scope changed
method changed
material changed
```

### Unsupported

Examples:

```text
capability unavailable
method unavailable
original material missing
```

The function deliberately says:

```text
revision inequality is not staleness
```

That is one of the central Stage 3 invariants.

## 6. Material validity still does not grant execution authority

A request can have:

```text
material validity = valid
```

while:

```text
current execution authority = unavailable
```

For example, the exact historical target/material may still be intact but the host no longer authorizes repository reads.

Conversely, broad current authority does not rescue stale material. A request whose actual premise changed is not safe to execute merely because the capability remains allowed.

So:

```text
valid basis
!= authorized execution
```

and:

```text
authorized capability
!= valid historical request
```

The host requires both.

## 7. Intent-before-effect preserves execution truth

The most important execution ordering is inside `execute_admission(...)`.

For an admitted request the host first publishes:

```text
ExecutionAttempt(
    state="intent_recorded"
)
```

Only after that publication is established does it proceed toward the external capability.

If a durable store is configured, the host also rereads the just-published head before the effect. A changed publication head blocks execution for explicit reconciliation; it is not silently merged or retried.

Then current authority/material is checked again immediately before capability entry.

The ordering is:

```text
admit request
→ durably publish attempt intent
→ recheck publication/current authority/material
→ external capability
```

This is not exactly-once execution. It is truthful bookkeeping across two systems that can fail independently.

## 8. `not_started` and completion unknown are different facts

`ExecutionInterruption` has a `completion` field:

```text
not_started
unknown
```

These meanings are intentionally different.

### Known `not_started`

The host has positive evidence that the external capability was not entered—for example authority was withdrawn after intent publication but before the provider call.

### Completion unknown

The capability may have been entered, but no completed observation was durably retained. An unexpected exception or interruption after entry can leave this state.

### Completed observation/problem

If the capability returns a bounded `problem` result and the host retains it as a `CapabilityObservation`, completion is known. A domain problem is not the same as unknown execution.

Compact model:

```text
intent_recorded
        ↓
 ┌──────┼───────────────┐
 │      │               │
not_started   completion_unknown   observation retained
                                  observed/empty/
                                  scoped_negative/problem
```

These distinctions matter because retry policy depends on what is actually known.

## 9. Previous attempt means no automatic retry

Once a request has an execution attempt, the host refuses automatic duplicate execution with:

```text
request_already_attempted_no_automatic_retry
```

A completion-unknown attempt therefore stays ambiguous until separately reconciled.

Historical admission or old intent does not grant permission to try again.

This prevents:

```text
exception
→ assume nothing happened
→ automatically repeat external effect
```

The system preserves uncertainty instead.

## 10. The real Python-support path is the first production caller

The generic host is demonstrated in the normal product flow inside [`investigation.py`](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/src/upgradepilot/investigation.py).

A grounded upstream Python-support claim can produce an unresolved exact-target applicability assessment. The native selector then identifies a need to inspect the target repository's declaration.

The real flow is:

```text
native Python-support pre-assessment
        ↓
native investigation selection
        ↓
publish partial native progress
        ↓
InvestigationNeed
        ↓
repository-read CapabilityRequest
        ↓
RequestAdmission
        ↓
ExecutionAttempt(intent_recorded)
        ↓
exact-head repository read
        ↓
CapabilityObservation
        ↓
existing target Python interpreter
        ↓
existing target relevance owner
        ↓
existing Python-support impact owner
        ↓
EvaluationOutcome(evaluated)
        ↓
new native boundary / Workspace successor
```

The generic host never decides whether the Python declaration makes the update applicable.

It retains the provider response and then calls the existing native/domain owners with their full required inputs.

This is why the Python-support path is a **production proof case**, not the definition of the host architecture.

## 11. Partial capture is the whole coherent unfinished native state

Before the selected repository read, orchestration calls:

```text
native_capture.partial_snapshot()
```

and publishes that native progress into the host.

This partial boundary contains all coherent native material truthfully established so far. It is not a lifecycle request record and it does not claim normal investigation completion.

This distinction mattered during Stage 3 implementation because a recorded downstream result initially referred to a pending placeholder input whose identity later refreshed.

The repair made pending input references refresh **before** recording the dependent result, while executed results retain the exact inputs they actually used.

General lesson:

> **An unfinished native boundary may evolve coherently; an already executed native fact must not be silently rebound to newer premises.**

## 12. Observations are not semantic conclusions

`CapabilityObservation` records outcomes such as:

```text
observed
empty
scoped_negative
problem
```

It records what happened under the admitted capability scope.

For the repository-read adapter, a successful read may retain the actual returned source content. But:

```text
source read succeeded
!= Python compatibility established
```

and:

```text
scoped_negative
!= global absence
```

The host retains the observation first. A qualified native owner performs the later interpretation/evaluation.

If that native evaluator fails, the actual source observation remains inspectable rather than disappearing with the failed interpretation.

## 13. Native evaluation is explicit owner activity

`evaluate_native(...)` receives an explicitly installed `LifecycleMethodIdentity` and a callback that supplies the native owner's real full inputs.

Before evaluation, the host checks current material validity and method availability.

Possible retained outcomes include:

```text
evaluated
unsupported
failed
stale
```

If evaluation succeeds, the host retains the new native assessment and its material closure.

If it fails, the host records `failed` and does not invent an assessment.

The host bookkeeping therefore never substitutes for semantic ownership.

## 14. Proposal authority remains weaker than native truth

The host can retain:

```text
AttributedProposal
StoppingProposal
ContentCitation
```

But `evaluate_proposal(...)` currently records:

```text
unsupported
```

because there is no admitted generic semantic/conflict/adequacy evaluator.

This is a deliberate boundary.

A future Investigator may say:

```text
"This upgrade is safe."
```

The system may preserve that as an attributed proposal.

Without the correct evaluator/synthesis owner, it must **not** become:

```text
established product truth
or maintainer action permission
```

The important rule is not that an LLM cannot utter decision-like language. The rule is that its statement remains a proposal until a qualified owner establishes stronger meaning.

## 15. Stopping proposal, procedural finish and adequacy are separate

Three states that can look similar in ordinary conversation must stay distinct:

```text
StoppingProposal
→ somebody proposes that investigation should stop

ProceduralTermination(completed)
→ the run's procedure ended normally

Investigation adequacy
→ enough justified evidence exists for the decision question
```

Stage 3 implements the first two lifecycle concepts.

It does **not** provide a generic adequacy evaluator.

The normal orchestration explicitly terminates with detail equivalent to:

```text
normal procedural completion;
investigation adequacy is not established
```

That is the correct product truth.

## 16. Recovery restores history, not live permission

When a host restores a retained schema-2 checkpoint, it reconstructs lifecycle history and native bases.

It does not reinstall execution authority or mark historical admissions as live.

The guarded recovery tests actively attempt to execute recovered admitted requests and require:

```text
historical_or_consumed_admission
```

The historical record remains true:

```text
this request was admitted then
```

while present execution truth remains:

```text
no current live admission exists now
```

Therefore:

```text
recovery
!= continuation
!= retry
!= replay
```

Continuation requires a separately invoked operation that revalidates current bindings and authority.

## 17. Basis, validity, authority and predecessor — one comparison table

| Concept | Main question | Owned by | What it does not establish |
| --- | --- | --- | --- |
| Original basis | What exact historical material/method/scope did this lifecycle record depend on? | retained lifecycle/native references | current usability or permission |
| Current material validity | Does that original dependency set still match the present target/material/method/capability? | material-validity + host composition | execution permission or semantic truth |
| Current execution authority | May this capability/effect execute now on this exact target? | trusted host authority | historical material freshness or domain conclusion |
| Publication predecessor | Which immutable Workspace revision is this publication extending? | persistence/host publication | evidence validity, semantic staleness or capability permission |

The system becomes unsafe if any two columns are collapsed.

## 18. Important engineering corrections

### Pending-input identity refresh

Making partial capture explicit exposed closure errors: recorded downstream relevance material referred to a pending placeholder whose identity changed afterward.

The repair refreshes pending input references before dependent records are captured. Executed records still keep their original input IDs.

**Lesson:** mutable progress and immutable historical facts need different update rules.

### Installed-test child environment

The first full Stage 3 run had 13 failures only because child-process test helpers relied on the parent's discovery `sys.path`. Focused tests accidentally hid this by using `tests:src`.

The child launchers were repaired to pass only the test fixture path plus inherited allowed paths. Product validation was not weakened.

**Lesson:** a focused test environment can accidentally provide imports that production/installed execution does not have. Fresh installed proof must control process import boundaries independently.

### Rejected request must keep its original basis

A stale-request rejection initially tried to publish the rejection against current native references. That lost the historical relationship between the request and its original premises.

The repair retains the rejection on the request's original basis.

**Lesson:** even a refusal has provenance. A rejection about historical work must not silently rebind that work to today's state.

## 19. Stage 3 verification and proof boundary

[`test_workspace_host_integration.py`](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/tests/test_workspace_host_integration.py) covers the real normal path plus explicitly labelled generic/delayed/defensive controls.

Final Stage 3 verification recorded:

- **25 focused host tests PASS**;
- **875/875 checkout tests PASS**;
- **875/875 fresh noneditable installed tests PASS**;
- all **92 source/installed Python hashes match**;
- normal selected-read flow proves intent is published before provider entry;
- provider acquisition occurs once;
- native impact owner runs pre/post under the real path;
- overlap, unresolved, unavailable and empty provider outcomes retain distinct meanings;
- native evaluator failure retains the actual source observation;
- 16 guarded cold readers restore historical state with live execution refused;
- 4 normal-path publisher children are process-killed around intent/observation/evaluation boundaries;
- archived-reader controls preserve old supported meanings and explicitly refuse the new observation codec where unsupported.

This proves the admitted generic-host/native integration and its execution-state distinctions.

It does **not** prove:

```text
model usefulness
generic semantic competence
generic adequacy evaluation
exactly-once external effects
power-loss durability
replay
user-facing continuation
full native-family migration
report/synthesis cutover
positive maintainer action permission
```

## 20. What to own versus what to look up

### Must master / own

- original basis versus current material validity;
- material validity versus current execution authority;
- both of those versus publication predecessor;
- intent-before-effect;
- `not_started` versus completion unknown versus completed observation/problem;
- no automatic retry after an attempt;
- recovery versus continuation/retry/replay;
- generic host coordination versus domain semantic ownership;
- proposal/stop/procedural completion versus adequacy/action permission.

### Understand operationally

- host capability/effect registration;
- material-closure traversal;
- method/capability/scope change classification;
- historical-admission refusal after restore;
- native evaluator handoff;
- partial native publication around lifecycle events.

### Lookup level

- exact lifecycle codec layouts/versions;
- every host error string;
- all process-kill helper details;
- incidental dataclass/UUID/storage mechanics.

### Deferred deliberately

- generic semantic/adequacy evaluators;
- future Investigator policy/runtime;
- multi-agent orchestration;
- user-facing continuation/replay;
- direct report/synthesis migration.

## Fast relearning route

1. Recreate the four-way distinction: **basis / validity / authority / predecessor**.
2. Open `validate_current_material_basis(...)`; explain why revision inequality alone is insufficient.
3. Open `execute_admission(...)`; trace intent publication, rechecks and external entry.
4. Explain `not_started`, `completion_unknown` and a completed `problem` observation.
5. Trace the real Python-support caller in `investigation.py` from native selection through host read to native reassessment.
6. Finish by explaining why a recovered admitted request cannot execute and why `completed` does not mean adequate.

## Transfer questions

1. Revision R8 adds unrelated CI evidence after a repository-read request was created at R5. Target, scope, method and the request's native material closure are unchanged. Must the request automatically become stale? Why not?
2. The request's basis remains valid, but repository-read authority is removed. What historical facts remain valid and what operation must be refused?
3. Intent was durably recorded; authority disappears before provider entry. How should completion be recorded, and why is that stronger than generic "unknown"?
4. The provider may have been entered, then the process crashes before an observation is retained. Why is automatic retry unsafe?
5. A future Investigator proposes "safe to merge" and cites delivered source correctly. Which owner boundary prevents that from becoming maintainer action permission merely because the host retained it?

## Primary anchors

- [`lifecycle_records.py`](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/src/upgradepilot/workspace/lifecycle_records.py)
- [`lifecycle_host.py`](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/src/upgradepilot/workspace/lifecycle_host.py)
- [`material_validity.py`](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/src/upgradepilot/workspace/material_validity.py)
- [normal production caller in `investigation.py`](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/src/upgradepilot/investigation.py)
- [`test_workspace_host_integration.py`](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/tests/test_workspace_host_integration.py)
- [Stage 3 implementation/proof cycle](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/working-memory/2026-10-13_2030_workspace-lifecycle-admission-and-material-basis_lbd-cycle.md)
- [Stage 3 completed D learning companion](https://github.com/motafegh/UpgradePilot/blob/5187f40ba974341eb29d765363f093922a881803/working-memory/2026-10-15_stage3-deferred-d-learning-todo.md)

`UP-SKILL:upgradepilot-learning-artifact`
