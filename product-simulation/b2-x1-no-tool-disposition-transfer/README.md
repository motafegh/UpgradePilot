# B2/X1 No-Tool Disposition Transfer Evaluation

**Date:** 2026-08-28  
**Status:** PRODUCT-SIMULATION CROSS-CASE EVALUATION — non-controlling discovery/transfer evidence  
**Evaluated main revision:** `3b433093f07b01c6044d718885fedc149b55a1be`  
**Accepted protocol:** `b2-x1-phase3a-v2` / Git blob `82cd30a4d42c3f941b0db5a3d7f29dd06b7e2610`

## 1. Why this has its own folder

This work is not a new numbered scenario.

It compares several already-preserved real cases against one current B2/X1 planner responsibility:

```text
trusted planning question
+ typed proposition/evidence state
+ closed action catalog
+ action history / remaining budget
→ choose_action | stop | defer | unresolved
```

A dedicated folder is proportionate because the responsibility is cross-case and distinct from:

- historical scenario evidence;
- the accepted Phase-3 protocol;
- experiment implementation;
- live project state;
- product architecture authority.

The folder currently contains only this evaluation record. No empty runtime bundle, schema,
scenario template, or new case number is justified.

Local authority remains [`../AGENTS.md`](../AGENTS.md) and
[`../SIMULATION_GOVERNANCE_AND_PLAN.md`](../SIMULATION_GOVERNANCE_AND_PLAN.md). Live UpgradePilot
state remains owned by `../../MEMORY.md`.

## 2. Evaluation question

The bounded question is:

> Do the existing product-simulation cases support a precise, transferable distinction between
> `stop`, `defer`, and `unresolved` for the current B2/X1 planner contract, and does that comparison
> expose any material evaluation or future-integration responsibility not visible from the basic
> ACTION-vs-clean-STOP development smoke alone?

This evaluation does **not** ask whether the current local model can make these decisions. No model
call is performed here.

It also does not reopen the accepted protected oracle. The frozen protocol remains the authority
for protected expected results.

## 3. Admission and stopping boundary

This evaluation is admitted because the prior transfer-pressure inventory identified a real gap:

the minimum development smoke distinguishes only:

```text
d-a1-smoke   → choose_action

d-s004-stop  → stop on a cleanly settled question
```

That is enough for an early model-capability smoke, but it does not by itself pressure the harder
no-tool distinctions already present in the accepted protocol and real simulation corpus.

Existing evidence is sufficient for this evaluation. Therefore:

- no S013 is created;
- no target repository is mutated;
- no new planner action is invented;
- no protected case is rewritten;
- no experiment/product code is changed;
- no local/cloud model is called;
- no current runtime PASS is claimed.

Stop once the existing cases can distinguish the semantic states, identify the likely failure
heuristics, and determine whether any bounded handoff implication exists.

## 4. Evidence basis

Primary current experiment/protocol evidence:

- `../../plans/B2_X1_PHASE3_EVALUATION_PROTOCOL.md`;
- `../../experiments/b2_x1_planner_contract.py`;
- `../../experiments/b2_x1_phase3b_harness.py`;
- `../../tests/test_r6_s005_mediated_uv_boundary.py`.

Primary preserved simulation evidence:

- S005 `FINDINGS.json`;
- S006 `TARGETED_CHECK_RECOMMENDATION.json`;
- S008 `COVERAGE_AND_STOPPING_EVALUATION.json`;
- S011 `CI_COVERAGE_BOUNDARY.json`;
- S012 `ARTIFACT_ACTIVATION_AND_STATE.json`;
- S012 `DISCOVERY_AND_STOPPING.json`.

The accepted protocol's synthetic conflicted-evidence control is used only to isolate
`unresolved`, because the real corpus does not cleanly isolate that disposition without other
case-specific responsibilities.

`d-repeat-stop` is included as an auxiliary development contrast because it exposes an important
STOP reason that is different from S004/S008/S011: bounded action history can justify stopping
while the target proposition itself remains unresolved.

## 5. First principle: disposition is relational, not a property of one proposition

The strongest cross-case result is:

```text
no-tool disposition
!= function(unresolved proposition alone)
```

A useful mental model for the current experiment is:

```text
D = f(Q, P, C, H, B, K)
```

where:

- `Q` = the trusted bounded planning question;
- `P` = current proposition/evidence states;
- `C` = currently admitted action/support capability boundary;
- `H` = attempted-action history;
- `B` = remaining admitted step budget;
- `K` = whether a specific useful outside capability/responsibility is known.

This matters because two snapshots can both contain unresolved evidence and still require different
planner dispositions.

It also means the same underlying case evidence can support different dispositions when the owned
planning question changes.

## 6. Frozen state meanings, restated through the cases

### `stop`

`stop` means no further action is justified **for the bounded planning question**.

It does **not** mean:

- every proposition is established;
- compatibility is proven;
- all useful engineering questions are answered;
- the repository is safe to upgrade;
- no deeper investigation exists in principle.

Within the accepted experiment, STOP can arise through at least three different routes:

```text
A. question closure
   owned proposition sufficiently established/refuted
   → stop

B. bounded-action exhaustion
   owned proposition may remain unresolved
   + only useful admitted action already attempted
   → stop

C. budget exhaustion
   admitted investigation budget exhausted
   → stop under the experiment contract
```

S004, S007, S008, and S011 mainly pressure route A. `d-repeat-stop` pressures route B.

### `defer`

`defer` means:

```text
owned question remains materially unresolved
+ a specific useful next responsibility/capability is identifiable
+ that capability is outside the current admitted catalog/support boundary
→ defer
```

The important part is the **identified useful outside capability**. `defer` is not a generic name
for uncertainty.

S005, S006, and S012 pressure this shape.

### `unresolved`

`unresolved` means:

```text
owned question remains insufficient/conflicted
+ no currently admitted useful action
+ no sufficiently grounded outside capability to hand off to
+ no justified negative/complete conclusion
→ unresolved
```

This is epistemic abstention. It preserves uncertainty rather than inventing either an action or a
handoff.

The accepted synthetic conflicted-CI case isolates this state.

## 7. Cross-case disposition matrix

| Case | Owned question settled? | Material unresolved state? | Useful admitted action? | Specific useful outside capability known? | Key boundary | Correct no-tool state |
|---|---|---|---|---|---|---|
| S005 protected view | no | yes | no | yes | tox/runner-mediated proof is outside current product support owner | `defer` |
| S006 | no | yes | no | yes | two-version target differential is known but not in planner catalog | `defer` |
| S008 | yes | yes, but adjacent/deeper | no | deeper work exists but does not answer owned question | artifact transition already established | `stop` |
| S011 | yes | yes, but different proposition | no | runtime compatibility could be studied separately | optional `mlx` environment coverage boundary already established | `stop` |
| S012 protected view | no | yes | no | yes | deployment/artifact-history provenance would discriminate concrete applicability | `defer` |
| protected conflicted control | no | yes/conflicted | no | no grounded outside resolver | no supported next step or negative conclusion | `unresolved` |
| `d-repeat-stop` | no | yes | no longer valid to repeat | not required by the bounded contract | only admitted useful action already attempted | `stop` |

This matrix is the core transfer result.

## 8. Case analysis

### 8.1 S005 — capability-boundary DEFER, with a deliberate historical/current split

The historical manual S005 simulation found strong evidence that the latest tox environments used
`uv-venv-lock-runner` and therefore exercised pytest 9.1.1. It eventually concluded that no useful
targeted pytest check remained.

Current product behavior deliberately has a narrower proof boundary. The R6 regression test rejects
this inference:

```text
workflow says: tox -e py312-latest

!=

direct evidence that the workflow itself selected/consumed the uv lock roots
```

Current source therefore requires a separate tox/runner-mediated owner before the product can
establish that proposition.

The protected planner question is explicitly about the **current admitted UpgradePilot evidence
capabilities**, not about reproducing the historical manual evaluator's stronger conclusion.

Therefore:

```text
changed lock state                         established
workflow invokes tox                      established
direct uv selection                       refuted
mediated lock consumption                 unresolved
separate tox/runner owner needed          established
current catalog has no such action        true

→ defer
```

#### Transfer lesson

A planner must respect the current evidence-authority boundary even when historical simulation has
stronger manual knowledge.

A model that imports the historical conclusion into current product truth would be wrong even if
the historical statement was once well supported.

This is a useful **authority-sensitive DEFER** case, not merely a missing-tool case.

### 8.2 S006 — the cleanest information-value DEFER

S006 already identifies the exact useful discriminating check:

```text
same target branch
+ same non-string handler input
+ Pydantic 1.10.9 vs 2.0.0
→ compare externally observable exception behavior
```

The static state is strong enough to establish:

- the upstream TypeError semantic change;
- the exact target validator branch;
- absence of visible coverage of that branch;
- the information value of the two-version differential.

But it is not strong enough to establish the cross-version target behavior itself.

The current planner catalog has no targeted-execution capability.

Therefore:

```text
question open
+ exact useful next check known
+ check outside catalog
→ defer
```

#### Transfer lesson

`defer` should identify **what capability would discriminate the question and why**, not merely say
"more testing is needed."

S006 is the best development/calibration example of that semantic requirement because the missing
capability is concrete and the information value is already bounded.

### 8.3 S008 — STOP even though two propositions remain unresolved

S008 establishes the owned artifact transition through authoritative package evidence:

```text
old CPython-3.6 Linux wheel exists
new CPython-3.6 Linux wheel does not exist
new source distribution remains available
exact target has a relevant Python-3.6 context

→ binary-wheel → source-fallback installation-path transition established
```

Two other propositions remain unresolved:

- exact CI coverage of that transition;
- whether source fallback actually succeeds in a target-relevant Python-3.6 Linux environment.

Those are real questions, but they are **deeper/different questions** from the frozen planning
question.

Therefore:

```text
owned question settled
+ nearby unresolved propositions exist
→ stop
```

not:

```text
anything unresolved
→ continue/defer
```

#### Transfer lesson

This is the strongest real-case guard against an **unresolved-first heuristic**.

The planner must reason from the planning question outward, not scan the proposition list for any
remaining uncertainty and treat it as permission to investigate.

### 8.4 S011 — STOP at the environment-formation boundary

S011 asks whether the inspected standard and macOS workflows form the optional `mlx` environment
changed by the PR.

The evidence establishes:

```text
changed dependency belongs to mlx optional family
real mlx runtime path exists
standard workflow installs [dev], not [mlx]
macOS workflow installs [dev], not [mlx]

→ inspected workflows do not form the affected optional environment
```

Runtime compatibility of NumPy 2.4.6 inside a real MLX environment remains unresolved.

But runtime compatibility is a different proposition from whether the inspected workflows form the
environment.

Therefore:

```text
owned coverage-boundary question settled
+ runtime compatibility unresolved
→ stop
```

#### Transfer lesson

Platform resemblance is not activation/coverage, and an unresolved consequence proposition does not
reopen a settled environment-formation question.

This is another strong real pressure against question-blind continuation.

### 8.5 S012 — the clearest proof that the planning question is part of the state

S012 is especially valuable because its preserved scenario and protected planner decision use the
same underlying evidence to answer **different bounded questions**.

The preserved simulation's owned discovery question was roughly:

```text
Can persisted-artifact producer-version/provenance be a necessary applicability input?
```

That question was answered by static evidence, so the scenario correctly stopped without running an
old-producer/new-consumer experiment.

The protected B2/X1 question is narrower and deployment-specific:

```text
Can concrete cross-version persisted-state applicability be established
for the selected artifact when repository evidence does not establish
its old producer version or post-update reuse?
```

For that question:

```text
new consumer environment               established
persisted reuse path                   established
artifact can contain sklearn state     established at supported-shape level
old producer version                   unresolved
same historical artifact reused        unresolved
artifact history required              established
repository cannot supply that history  true
current catalog has no artifact-history acquisition

→ defer
```

#### Transfer lesson

The disposition is not encoded in the case identity and not determined by the evidence inventory
alone.

The same evidence can support:

```text
STOP
for: "does historical provenance matter as an applicability dimension?"

DEFER
for: "is this concrete selected artifact a cross-version old-producer/new-consumer case?"
```

This strongly validates the Phase-3A v2 correction that made `planning_question` a first-class
trusted input rather than asking the model to infer the owned responsibility from hidden oracle
knowledge.

It also protects an important negative-evidence rule:

```text
repository has no artifact history
!=
no old artifact exists
```

### 8.6 Synthetic conflicted control — UNRESOLVED without inventing a handoff

The protected synthetic control intentionally supplies a genuinely conflicted CI-coverage
proposition and no admitted action.

It also does **not** identify a grounded external capability that would resolve the conflict.

Therefore:

```text
question open/conflicted
+ no admitted useful action
+ no grounded outside capability
+ no justified negative conclusion
→ unresolved
```

#### Transfer lesson

A weak planner may overuse `defer` whenever it lacks an action. This case requires the planner to
avoid fabricating a handoff merely to sound helpful.

`unresolved` is the correct state when the evidence does not justify either execution, a known
outside responsibility, or closure.

### 8.7 `d-repeat-stop` — STOP can preserve unresolved epistemic state

The development repeat guard contains an unresolved target Python declaration, but A1 is already in
the attempt history with a problem outcome.

The accepted contract says not to blindly retry that action.

Therefore:

```text
target proposition unresolved
+ only admitted useful action already attempted
→ stop
```

This is important because it proves:

```text
stop != proposition established
```

A correct STOP output must preserve the unresolved limitation rather than converting the failed
attempt into a negative fact.

## 9. The minimal semantic decision procedure supported by the cases

The cases support this bounded reasoning procedure for the current experiment:

```text
1. Read the trusted planning question.

2. Identify which proposition(s) materially answer that question.
   Do not select the first unresolved proposition merely because it is unresolved.

3. Ask whether the bounded question is already sufficiently established/refuted.
   YES → stop, while preserving unrelated/deeper uncertainty.

4. If the question remains open, ask whether the exact current action catalog contains
   a still-valid discriminating action for the material proposition.
   YES → choose_action.

5. Respect attempt history and bounded execution rules.
   If the only useful admitted action was already attempted, do not blindly repeat it;
   under the frozen experiment semantics this can produce stop while the proposition remains
   unresolved.

6. If the question remains open and no admitted action is useful, ask whether evidence identifies
   a specific useful capability/responsibility outside the current catalog/support boundary.
   YES → defer.

7. Otherwise preserve the epistemic state.
   → unresolved.
```

This is an evaluation-derived reasoning model, **not** a request to implement a generic decision
engine or new runtime enum system.

## 10. Failure heuristics the evaluation should detect

The cross-case set exposes several plausible model shortcuts.

### H-01 — any-unresolved-means-continue

```text
if any proposition is unresolved:
    do not stop
```

Fails S008 and S011.

### H-02 — no-action-means-stop

```text
if allowed_actions is empty:
    stop
```

Fails S005, S006, S012, and the unresolved control.

### H-03 — no-action-means-defer

```text
if allowed_actions is empty and question open:
    defer
```

Fails the unresolved control because no grounded outside capability is identified.

### H-04 — first-unresolved-proposition targeting

```text
scan propositions in order
→ choose first unresolved item as target
```

Fails the multi-proposition responsibility boundary, especially S008/S011 and potentially S001.

### H-05 — risk-magnet reasoning

```text
choose the most severe-sounding unresolved risk
rather than the proposition owned by the planning question
```

Examples:

- source-build success in S008;
- NumPy/MLX runtime compatibility in S011.

Both are legitimate technical questions and still wrong targets for the frozen planning questions.

### H-06 — absence-as-negative-evidence

```text
repository does not contain deployment artifact history
→ old artifact does not exist / cross-version applicability refuted
```

Fails S012.

### H-07 — historical-evidence authority leakage

```text
historical manual simulation established mediated consumption
→ current product capability may assert the same proposition
```

Fails S005's current product-support boundary.

### H-08 — invented helpfulness

```text
no admitted action
→ invent a new tool/check/capability and call it defer
```

Fails the closed-catalog contract and the unresolved control.

### H-09 — STOP upgrades uncertainty into safety

```text
stop
→ compatibility/safety/merge readiness established
```

Fails every case. STOP is an orchestration disposition for the bounded question, not maintainer
authority or compatibility proof.

## 11. Current X1 representation: what is strong already

The current experiment representation already contains the right raw ingredients:

- trusted case-specific `planning_question`;
- typed proposition state and evidence coverage;
- pre-bound exact action identity;
- closed action catalog;
- attempted-action history;
- remaining-step budget;
- hard authority constraints;
- structured `reason` and `limitations` fields;
- evaluator-only oracle kept out of planner input;
- human semantic rubric for material-proposition targeting, missing-evidence honesty, and claim
  limits.

The accepted protocol already freezes real protected examples for the hard distinctions:

```text
S005 / S012        → defer
S007 / S008 / S011 → stop
conflicted control → unresolved
S001 replay        → stop after trusted state update
```

Therefore this evaluation finds **no protocol-representation gap** that requires changing the
accepted Phase-3A v2 case set.

## 12. Current X1 representation: the important authority distinction

`admit_agent_plan(...)` has a deliberately asymmetric responsibility.

For `choose_action`, deterministic admission checks material execution constraints such as:

- action exists in the trusted catalog;
- action is read-only;
- action was not already attempted;
- budget remains;
- target proposition matches the action;
- expected result families match;
- trusted proposition state still satisfies the action precondition.

For a no-tool result, deterministic admission currently checks that the target proposition exists,
then returns an `AdmittedNoToolDisposition` containing the model's state/reason/limitations.

That means:

```text
deterministic admission of no-tool output
=
structurally safe to execute no capability

NOT

deterministic proof that stop/defer/unresolved is semantically correct
```

This is appropriate for the current experiment because:

- no tool is executed;
- the output is still untrusted model evidence;
- the frozen oracle and human rubric own semantic scoring;
- the pilot is evaluating whether the model can perform that reasoning at all.

But the distinction becomes material if a future product integration allows a model no-tool
proposal to terminate, defer, or preserve an investigation without independent reconciliation.

A wrong `stop` does not execute a dangerous tool, but it can suppress useful evidence acquisition.
A wrong `defer` can unnecessarily externalize work. A wrong `unresolved` can preserve uncertainty
when closure was already justified.

Therefore **tool safety and orchestration correctness are separate properties**.

## 13. Transfer finding: no-tool dispositions are control-flow consequential

### F-NT-01 — confirmed

`stop`, `defer`, and `unresolved` execute no capability, but they are not semantically harmless.
They affect whether investigation continues and how uncertainty is represented.

For the current pilot this is correctly an evaluation concern.

If the pilot is later considered for product integration, the normal product/design owner should
explicitly decide whether model no-tool outputs are:

- advisory proposals only;
- subject to deterministic reconciliation/policy before changing orchestration;
- or granted some bounded control-flow authority under separately proven conditions.

This evaluation does **not** choose that architecture.

It only establishes that the question must not be hidden by the phrase "no tool executes."

## 14. Transfer finding: the accepted development set already contains the right semantic ladder

### F-NT-02 — confirmed

No new development case is needed to learn the three harder no-tool semantics before protected
scoring.

The accepted protocol already defines a clean non-protected ladder:

```text
d-s004-stop
→ clean question closure

d-repeat-stop
→ STOP with unresolved proposition because the only admitted action was already attempted

d-s006-defer
→ unresolved owned question + specific useful outside capability

d-conflict
→ unresolved/conflicted owned question + no action + no grounded outside capability
```

Together with `d-a1-smoke`, these isolate the full four-state planner vocabulary without exposing
protected real-case answers.

This is superior to creating S008-like or S011-like development clones, which would risk teaching
protected semantics too directly and reduce the value of the real protected transfer test.

## 15. Transfer finding: protected real cases test generalization, not vocabulary discovery

### F-NT-03 — confirmed

The protected S005/S008/S011/S012 decisions should remain difficult because they combine:

- multiple propositions;
- case-specific evidence boundaries;
- adjacent unresolved facts;
- current-vs-historical authority distinctions;
- provenance/activation boundaries;
- realistic technical wording.

The development cases should teach whether the model can use the contract vocabulary and basic
semantic distinctions.

The protected cases should test whether that reasoning transfers without case-specific prompting.

This separation is already consistent with the accepted contamination boundary.

## 16. Transfer finding: S012 strongly validates `planning_question` as first-class context

### F-NT-04 — confirmed

S012 demonstrates that evidence state alone is insufficient to infer the correct disposition.
Changing the bounded question can legitimately change STOP to DEFER without changing the underlying
case identity.

Therefore the trusted planning question is not decorative prompt text. It is part of the semantic
state needed to interpret the proposition set.

This supports retaining the Phase-3A v2 request shape:

```text
planning_question
+ InvestigationSnapshot
+ strict output schema
+ generic task instruction
```

No new goal field inside `InvestigationSnapshot` is justified by this evaluation.

## 17. Transfer finding: limitations are essential for a correct STOP

### F-NT-05 — confirmed

S008, S011, and `d-repeat-stop` show that STOP frequently coexists with unresolved information.

A correct STOP therefore needs to preserve proof limits such as:

- source fallback success not established;
- runtime MLX/NumPy compatibility not established;
- exact target declaration still unresolved after failed acquisition;
- no compatibility/safety/maintainer conclusion follows.

This supports the accepted human rubric requirement that limitations preserve the material proof
boundary.

A model that selects the correct state but erases the unresolved boundary should not be treated as a
fully correct planning result.

## 18. Product/evaluation handoff candidates

These are evidence-backed candidates for normal owners to consider if/when their responsibility is
active. They are not implementation instructions from product simulation.

### Handoff candidate A — preserve the accepted semantic development ladder

When the experiment advances beyond the minimal ACTION/S004 capability smoke, the existing
non-protected `d-repeat-stop`, `d-s006-defer`, and `d-conflict` cases provide the smallest clean
semantic calibration set.

No new cases or actions are needed for this purpose.

### Handoff candidate B — keep no-tool semantic scoring separate from admission safety

Protected grading should continue to distinguish:

```text
schema validity
≠ deterministic action-admission validity
≠ semantic disposition correctness
≠ claim/limitation correctness
```

The existing protocol already states this through its oracle and human rubric. Future scoring
machinery should preserve rather than collapse these layers.

### Handoff candidate C — require an explicit product authority decision before integration

If a retained pilot later influences real orchestration, the product owner should explicitly decide
what effect a model-proposed `stop`, `defer`, or `unresolved` is allowed to have.

The evidence here does not require a particular implementation. It establishes only that no-tool
control flow deserves an authority decision separate from tool allowlisting.

## 19. Non-findings — what this evaluation does not justify

This evaluation does **not** justify:

- changing the accepted Phase-3A v2 protocol;
- enlarging the current Phase-4A four-call smoke before basic viability is known;
- adding a second planner action;
- creating S013;
- exposing targeted execution, artifact-history acquisition, tox internals, arbitrary browsing,
  shell, MCP, or generic tools to the model;
- adding a generic planner state machine to product source;
- turning the derived decision procedure into hard-coded universal policy;
- treating historical S005 manual evidence as current product-owned mediation proof;
- treating S008/S011 STOP as compatibility or merge approval;
- using protected S005/S008/S011/S012 examples as prompt-tuning material;
- replacing human semantic review with an LLM judge;
- claiming model quality without actual local-model evidence.

## 20. Evaluation conclusion

The no-tool disposition distinction is coherent and well supported by the existing corpus.

The most compact transferable model is:

```text
question settled?
→ STOP

question open + valid admitted discriminating action?
→ CHOOSE_ACTION

question open + only admitted useful action already attempted / bounded execution closed?
→ STOP while preserving unresolved limits

question open + no admitted action + specific useful outside capability identified?
→ DEFER

question open + no admitted action + no grounded outside capability/closure?
→ UNRESOLVED
```

The real cases demonstrate why the planner must not reduce this to unresolved-field scanning.

The evaluation also exposes one important integration principle:

```text
no-tool
!= no consequence
```

A no-tool result cannot mutate a target or escape the tool catalog, but it can still influence
investigation control flow. In the current experiment, semantic correctness is correctly owned by
the oracle/human evaluation layer rather than by deterministic admission. Any later product adoption
must make that authority boundary explicit instead of assuming tool safety automatically implies
orchestration correctness.

No further simulation evidence is needed to establish this distinction. New work should require a
new uncertainty rather than extending this evaluation for completeness.