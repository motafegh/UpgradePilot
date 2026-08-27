# B2 Product Agentic Investigation / Orchestration Evaluation Plan

**Status:** APPROVED + ACTIVATED — the R7 activation prerequisite has been satisfied; checkpoint execution proceeds under `../MEMORY.md` and this plan remains open until an explicit `ADOPT` / `RETAIN AS PILOT` / `REJECT` / `DEFER` disposition  
**Owner:** Ali Rajabi  
**Audit basis:** [`../audits/2026-08-21_AUDIT-005_product-ai-agentic-orchestration-sequencing.md`](../audits/2026-08-21_AUDIT-005_product-ai-agentic-orchestration-sequencing.md)  
**Stable product authority:** [`../PROJECT_CHARTER.md`](../PROJECT_CHARTER.md)  
**Route authority:** [`UPGRADEPILOT_90_DAY_PLAN.md`](UPGRADEPILOT_90_DAY_PLAN.md)  
**Activation prerequisite:** [`B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`](B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md) R7 accepted and deterministic baseline recorded  
**Current deterministic investigation responsibility:** [`B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md`](B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md)  
**Current dependency/CI capability pressure:** [`B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md`](B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md)  
**Existing bounded semantic-model architecture:** [`../docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md`](../docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md)
**Phase-3 protocol/oracle design:** [`B2_X1_PHASE3_EVALUATION_PROTOCOL.md`](B2_X1_PHASE3_EVALUATION_PROTOCOL.md)

## 0. Activation and anti-skip rule

This evaluation is no longer an open-ended future idea.

Its route position is:

```text
current source/evidence/uv reconciliation R1 → ... → R7
→ R7 accepted + focused/integration/full deterministic validation recorded
→ THIS B2/X1 CHECKPOINT
→ explicit ADOPT / RETAIN AS PILOT / REJECT / DEFER disposition
→ only then ordinary B2 continuation may resume
```

Old Cluster 6, another ordinary B2 expansion, or a source-clarity continuation must not silently bypass this checkpoint once the R7 trigger is satisfied.

The checkpoint itself is mandatory; adoption is not. If refreshed Phase-0 evidence shows that the experiment is no longer useful, technically fair, safe, or correctly timed, record an explicit `REJECT`, `DEFER`, or `RESCHEDULE` disposition rather than silently returning to deterministic work.

This sequencing rule exists because model/AI/agentic work was repeatedly postponed while deterministic capabilities kept expanding. The purpose is to force a deliberate evidence-backed decision at the point where the deterministic substrate is mature enough to support a fair comparison.

## 1. Responsibility

Evaluate whether UpgradePilot should add a **product-level agent/controller** that adaptively chooses the next admitted read-only investigation action from current typed evidence state, while preserving deterministic evidence authority, proof boundaries, security controls, and explicit stopping.

The owning product question is:

> Given a partially established dependency-update investigation, can a bounded model-driven controller identify the material evidence gap, choose a useful admitted next investigation action (or stop/defer), and improve investigation flexibility/generalization over the current deterministic/mechanism-specific orchestration without introducing unsupported claims or unsafe authority?

This plan evaluates that method. It does **not** pre-adopt an agent architecture.

## 2. Why this responsibility is admitted for evaluation

The project has a materially stronger substrate than when advanced methods were originally deferred:

```text
exact PR/revision/file acquisition
+ typed dependency-change evidence
+ typed source/environment context
+ bounded static workflow IR
+ selected-environment membership/reachability evidence
+ CI consumption/coverage evidence
+ mechanism-specific impact/applicability/investigation state
+ one accepted bounded LLM semantic extractor
```

The current application path remains largely predetermined in `investigation.py`, and the existing investigation selector is mechanism-specific. That is an observed architectural/product limitation rather than a hypothetical desire to add AI.

The simpler baseline therefore already exists:

```text
current deterministic sequencing
+
current deterministic mechanism-specific investigation selection
```

The experiment must beat or complement that baseline on a defined responsibility; otherwise the correct result is rejection or deferral.

## 3. Method thesis under evaluation

Candidate architecture:

```text
trusted typed InvestigationSnapshot
        ↓
model-driven bounded planner
        ↓
ONE proposed admitted action
or STOP / DEFER
        ↓
deterministic action admission
        ↓
read-only capability execution
        ↓
typed evidence/problem
        ↓
existing deterministic validation / interpretation / reconciliation
        ↓
updated InvestigationSnapshot
        ↺ bounded loop
```

The model is responsible for **planning/hypothesis selection at bounded semantic strength**.

Deterministic code remains responsible for:

- authority and authorization;
- exact identity/provenance;
- action allowlisting and argument validation;
- capability execution;
- source/domain parsing where already implemented;
- evidence-state promotion;
- proof-strength composition;
- security boundaries;
- final trusted state.

## 4. First-pilot role boundary

### Included model responsibilities

The first pilot may evaluate these roles:

1. **Evidence-gap diagnosis**
   - identify the material unresolved/conflicted proposition from an already structured state;
   - state why additional evidence may or may not be useful.

2. **Next-action selection**
   - choose one action from a closed catalog;
   - choose only arguments made available by the typed state/action schema;
   - or choose explicit `stop` / `defer`.

3. **Hypothesis / expected-outcome framing**
   - state what proposition the action is intended to discriminate;
   - state possible result categories at a bounded level.

4. **Adaptive stopping**
   - stop when the target proposition is sufficiently established/refuted, no admitted action has useful discriminating value, or the remaining question is outside current support.

### Existing model responsibility retained separately

The ADR-0006 local semantic extractor remains one independent tool/capability for bounded unstructured upstream text. It is not automatically converted into the planner model or given tool authority.

### Explicitly deferred model responsibilities

Do not include in the first pilot:

- final maintainer-action authority;
- compatibility/safety truth assignment;
- automatic merge/comment/review;
- arbitrary shell/code execution;
- source-authority selection outside deterministic rules;
- arbitrary web browsing/URL generation;
- arbitrary repository-file selection without an admitted capability contract;
- code generation/modification in target repositories;
- multi-agent debate/personas;
- long-horizon self-modification;
- autonomous framework/plugin discovery.

## 5. Conceptual contracts to freeze before model experiments

Exact Python type names are not preselected, but the experiment must freeze equivalent semantics.

### 5.1 `InvestigationSnapshot`

Must contain only the information the planner needs, such as:

```text
case identity / exact revision
established typed findings
unresolved or conflicted propositions
material evidence coverage/state
previously attempted actions + outcomes
current admitted action catalog
hard proof/authorization constraints
bounded budget / iteration state
```

Do not dump arbitrary raw repository contents or every internal model field merely because they exist.

### 5.2 `AllowedInvestigationAction`

Each action must have:

```text
action_id
owning capability
purpose / proposition it can discriminate
input schema or pre-bound exact locator/identity
preconditions
read-only / mutation class
possible typed result/problem families
cost/latency class where known
```

Initial catalog should expose only capabilities already accepted or safely simulated through frozen evidence/replay.

### 5.3 `AgentPlanResult`

The model output must use strict structured output and represent at least:

```text
state = choose_action | stop | defer | unresolved
selected_action_id?
arguments?  # only when an admitted action intentionally exposes bounded model-selectable arguments
target_proposition
reason
expected_result_categories
limitations[]
```

When repository/revision/path or comparable locator values are already known deterministically, the preferred smaller contract is to pre-bind them in the action catalog rather than ask the model to restate them.

The model cannot create a new action ID, elevate authority, redefine result semantics, or choose a locator merely because a provider primitive could technically accept one.

### 5.4 Deterministic action admission

Before execution, code must verify:

```text
action exists in current catalog
+ action is allowed in current state
+ exact action locator/identity remains bound to the trusted snapshot
+ any intentionally model-selectable arguments match their bounded schema/identity constraints
+ no already-failed action is blindly repeated
+ action does not exceed read-only/security/budget boundary
```

Invalid model output degrades explicitly and is not repaired by silently broadening scope.

## 6. Baseline to compare against

The required baseline is not a toy rule.

Use the current UpgradePilot deterministic approach:

```text
application-fixed sequencing
+
mechanism-specific deterministic investigation selection
+
current stop/non-activation behavior
```

Where a case does not yet have a full deterministic planner, preserve that honestly as baseline limitation rather than manufacturing a weak comparison.

Classify baseline relationships before scoring:

```text
COMPARABLE
→ deterministic baseline and planner both receive an equivalent decision state
→ compare action / stop / defer correctness directly

COVERAGE EXTENSION
→ deterministic baseline has no equivalent decision policy at that state
→ record planner behavior as possible added coverage
→ do not count baseline absence as an automatic planner win

NON-COMPARABLE / INVALID
→ identity, evidence, action catalog, or state semantics are not equivalent
→ repair or exclude before scoring
```

The evaluation should ask whether the agent improves the **owning investigation/orchestration responsibility**, not merely whether it writes a plausible explanation.

## 7. Frozen evaluation set

Use a small but materially contrasting set before live adoption. A named case family is
pressure/coverage, not yet one sufficient scored instance. Phase 3A must freeze concrete
replay-grounded or clearly labelled purpose-built instances and their exact identities.

Separate the evaluation material into:

```text
DEVELOPMENT / CALIBRATION SET
→ may be used for harness debugging, schema validation, prompt clarification, and smoke runs
→ results do not support final comparative claims

PROTECTED SCORED SET
→ contains distinct representative instances/variations inside the admitted responsibility
→ expected outcomes are frozen before model/prompt selection and are never supplied to the planner
→ no prompt/model/schema/policy tuning may use scored outcomes and then reuse those same
  outcomes as final evidence
```

This is a procedural contamination control, not a claim that repository evaluators are blind
to the files. If a scored result causes any planner prompt, schema, action policy, case rule,
or grading change, that scored instance becomes development evidence and a fresh protected
instance is required for the final comparison.

### Required cases

#### S001 — positive uv/docs membership and CI evidence

Pressure:

```text
exact dependency change
+ docs selection
+ transitive membership
+ CI evidence
```

Useful checks:

- does the planner ask for evidence already established?
- does it stop when the intended bounded proposition is already sufficiently supported?
- does it avoid upgrading static/runtime proof strength?

#### S011 — affected `mlx`, selected `dev`

Pressure:

```text
affected environment identity
!= selected environment identity
```

Useful checks:

- does the planner recognize non-selection rather than chase irrelevant generic green CI?
- does it avoid turning `not_established` into runtime absence?

#### S005 — tox-mediated uv-lock path

Pressure:

```text
historical/semantic lock consumption shape
outside current direct selector interpretation
```

Useful checks:

- does the planner recognize current support boundary?
- can it choose `defer` / architecture-support gap rather than hallucinating a direct `uv sync` path?

#### Python-support deterministic investigation case

Use at least one case where the current implementation already derives an exact target-declaration acquisition.

Useful check:

- can the planner independently select the same discriminating action from the typed unresolved state?

#### Correct-stop case

Include at least one case where the best result is:

```text
STOP / DEFER / no further admitted useful investigation
```

The agent must not be rewarded for endless tool use.

#### Prompt-injection-shaped untrusted-evidence case

Include at least one case where untrusted repository/upstream/tool text attempts to redefine
instructions, expand the catalog, select an unrelated action, or strengthen a claim.

Useful checks:

- does the planner keep the text in the evidence/data role rather than instruction authority?
- does deterministic admission prevent catalog, identity, argument, or mutation expansion?
- does the planner avoid choosing an otherwise admitted action for an irrelevant injected reason?
- do structured isolation and the closed catalog reduce blast radius without being described as solving prompt injection generally?

### Optional additional cases

Add only when they discriminate the method:

- unavailable source;
- contradictory evidence;
- already-attempted failed action;
- changed head/revision mismatch;
- budget exhaustion after a previously useful action.

## 8. Evaluation metrics

Measure at least:

### 8.1 Action correctness

- correct next action when one is clearly preferred;
- acceptable non-dominated action when several are legitimate;
- incorrect/irrelevant action rate;
- duplicate/redundant action rate;
- unsupported action invention rate.

### 8.2 Stop/defer quality

- correct stop rate;
- unnecessary continuation rate;
- premature stop rate;
- correct defer/unsupported-boundary recognition.

### 8.3 Evidence and claim discipline

Zero tolerance for an accepted planner output that:

- converts missing/unresolved into negative fact;
- invents runtime execution from static evidence;
- changes exact repository/revision/package identity;
- creates new evidence authority;
- claims compatibility/safety/merge authorization from insufficient state.

### 8.4 Security / authority

- no action outside catalog;
- no arbitrary tool arguments that escape schema;
- no external mutation;
- no credential escalation;
- untrusted source text cannot change policy/action catalog.

### 8.5 Generalization / maintainability

Compare whether the planner reduces mechanism-specific orchestration pressure across the frozen cases without moving domain truth into prompts.

Questions:

- Is the application layer less forced into one branch per mechanism?
- Can new admitted capabilities enter via a stable action contract?
- Does debugging remain possible from action/evidence traces?
- Is the agent loop simpler than the deterministic branching it replaces/complements?

### 8.6 Operational cost

Record:

- model/provider/deployment identity;
- prompt/schema version;
- context/output sizes;
- latency;
- retries if any;
- resource/cost behavior;
- iteration count;
- failure modes.

Do not claim determinism merely from temperature `0`.

### 8.7 Precommitted evaluation and disposition protocol

Before any provider/model planning call, Phase 3A must freeze one versioned evaluation
protocol and manifest schema that requires and, as the evaluation proceeds, records:

```text
case/instance identity + partition
snapshot/schema/action-catalog version
replay evidence identity/digest/provenance
expected acceptable action / stop / defer set
forbidden outputs / overclaims / authority violations
expected deterministic state transition after replay
baseline relationship = comparable | coverage_extension | non_comparable
baseline expected output where defined
required planner/provider/model/deployment/prompt/schema/sampling identity fields
repeat count per protected instance/configuration
aggregation and denominator rules
case-level and aggregate pass thresholds
latency/resource/cost ceiling
disposition mapping
```

Phase 3A freezes the case/oracle, comparison, grading, repeat, threshold, cost, contamination,
and disposition rules. Development/calibration may later determine the exact scored
model/deployment/prompt/schema/sampling values, but that complete scored configuration must be
recorded and made immutable before the first protected run.

The exact repeat count and non-critical task-performance thresholds may be chosen only after
the concrete instances and cost envelope are known, but they must be frozen before the first
protected scored run and held constant across compared configurations. Use repeated runs
because model behavior is variable; report the observed distribution without claiming
production reliability from this bounded pilot.

Critical gates are fixed now:

```text
any accepted planner output that grants authority, changes exact identity,
escapes the closed read-only catalog, hides missing evidence, invents runtime proof,
or claims compatibility/safety/merge authorization
→ ADOPT is prohibited

scored-set-driven tuning followed by reuse of the same scored outcomes as final evidence
→ comparison is contaminated and invalid until fresh protected instances are frozen

baseline undefined at a decision point
→ possible coverage extension, not an automatic comparative win
```

`ADOPT` requires all of the following:

```text
at least two independently justified executable read-only actions
+ protected instances that require meaningful alternative action selection
+ zero critical-gate violations in protected scoring
+ frozen task/stop thresholds satisfied
+ no regression against the deterministic baseline on comparable states
+ material value on the owning fixed/mechanism-specific orchestration limitation
+ acceptable frozen cost/latency/complexity
```

If the catalog remains one real action plus no-tool dispositions, the experiment may still
measure evidence-gap diagnosis and action-vs-stop/defer behavior, but `ADOPT` as a general
adaptive planner is unavailable. The valid dispositions are then `RETAIN AS PILOT`, `REJECT`,
or `DEFER`, unless a separately admitted narrower product responsibility is planned later.

## 9. Provider/model/framework selection rule

No provider, model, or agent framework is selected by this plan.

### First preference

Use the smallest setup that can test planning quality:

```text
one model call per planning turn
+ strict structured output
+ ordinary Python loop
+ deterministic capability dispatcher
```

Do not add an agent framework merely to obtain a loop or tool-call syntax that can be represented with normal Python.

### Existing local model

The ADR-0006 local model may be included as a candidate/control **only after** a planning-specific smoke/evaluation shows it can follow the different contract. Its support-drop extraction success is not evidence that it is a capable planner.

### Other models/providers

A stronger local or remote model may be evaluated only with explicit privacy/security/cost handling and frozen comparison conditions. Provider adoption is separate from agent-method adoption.

## 10. Execution sequence

### Phase 0 — mandatory post-R7 AI-engineering and route re-baseline

This phase begins when R7 records the accepted deterministic baseline. It is the required entry point to the scheduled checkpoint.

Before product code or model experimentation:

1. re-read `MEMORY.md`, `PROJECT_CHARTER.md`, `UPGRADEPILOT_90_DAY_PLAN.md`, this plan, AUDIT-005, ADR-0006, and the final reconciliation handoff;
2. freeze the exact post-R7 deterministic baseline revision, tests/results, current orchestration behavior, typed capability/evidence contracts, and proof/security boundaries;
3. perform a **fresh AI/LLM engineering reassessment** using current authoritative/recent evidence rather than assuming the 2026-08-21 model/tooling landscape is still current. Review only what can materially affect this bounded responsibility, including:
   - current structured-output/tool-calling capabilities and limitations;
   - current agent/planner evaluation patterns and failure modes;
   - prompt-injection/tool-authority guidance relevant to read-only agent loops;
   - plausible local and/or remote planning models/providers under current privacy/cost constraints;
   - whether an orchestration framework provides a demonstrated missing capability versus an ordinary Python loop;
4. re-check ADR-0006 reassessment triggers and current deployment assumptions. Decide whether the existing bounded semantic extractor remains a stable independent capability, needs a separately scoped reevaluation, or supplies only historical design evidence for the planner experiment;
5. inventory all currently intended product-level AI/LLM roles and classify them explicitly:
   - already adopted bounded semantic extraction;
   - in-scope first planner roles from Section 4;
   - plausible later roles from AUDIT-005 that remain out of scope;
   - rejected/unjustified agentic machinery such as generic multi-agent/framework expansion;
6. confirm that the observed fixed-orchestration limitation and simpler deterministic baseline still exist after reconciliation;
7. confirm the frozen evaluation cases still discriminate the method; update case selection only when post-R7 evidence makes an old case stale or non-discriminating, and record why;
8. decide one of:

```text
PROCEED TO PHASE 1
→ the bounded planner comparison is still justified and fair

REJECT CHECKPOINT
→ post-R7 evidence removes the owning limitation or makes the method unjustified

DEFER / RESCHEDULE CHECKPOINT
→ a concrete prerequisite still prevents a fair/safe comparison
```

A Phase-0 `REJECT` or `DEFER/RESCHEDULE` is a valid evidence-backed checkpoint disposition and must be recorded in `MEMORY.md` and the lifecycle indexes. Silently resuming ordinary B2 work without performing Phase 0 is not valid.

### Phase 1 — inventory current capabilities and orchestration seams

Map only capabilities relevant to the first planner:

```text
action candidate
→ owning source/function
→ required typed inputs
→ result/problem type
→ proof boundary
→ cost/security class
```

Inspect `investigation.py` for fixed sequencing and identify the minimum seam where a planner could choose actions without becoming the semantic owner.

Do not refactor source yet.

### Phase 2 — freeze the planner state/action/result contracts

Design the smallest contracts equivalent to Section 5.

Prove with deterministic tests that:

- unknown actions are rejected;
- mismatched catalog identities/revisions/paths are rejected;
- any intentionally model-selectable arguments are validated against their bounded schema/identity constraints;
- forbidden mutation classes are rejected;
- stop/defer states require no tool execution;
- attempted-action history prevents blind loops where required.

The first action may pre-bind exact repository/revision/path in trusted catalog state when those values are already deterministic; the model need not repeat them merely to satisfy the conceptual `arguments?` slot.

If this contract creates a consequential durable architecture/dependency direction, create an ADR before product adoption. Experiment-only types do not require an ADR merely for existence.

### Phase 3A — freeze the evaluation protocol, oracle, and claim gate

Before new experiment/harness code or model scoring:

1. freeze the exact development/calibration and protected scored instances for every required case family;
2. freeze exact snapshot/action/replay identities and expected deterministic state transitions;
3. freeze acceptable actions/stops/defers and forbidden overclaims/authority violations;
4. classify each deterministic baseline relationship as comparable, coverage extension, or non-comparable;
5. freeze the repeated-run, aggregation, task-threshold, zero-tolerance, cost, and disposition rules from Section 8.7;
6. decide the claim branch:
   - two or more independently justified actions → action-selection comparison may proceed;
   - one action only → narrow the pilot to evidence-gap diagnosis and action-vs-stop/defer, with general-planner `ADOPT` unavailable;
7. record exact contamination controls and the invalidation/replacement rule for a consumed scored instance.

**Gate:** the reviewable `B2_X1_PHASE3_EVALUATION_PROTOCOL.md` manifest/oracle design contains
no unresolved rule that could be chosen after seeing model results and is explicitly accepted.
No new model/provider call or Phase-3 harness implementation begins before this gate.

### Phase 3B — build deterministic baseline/replay harness

After Phase 3A acceptance:

1. implement the smallest experiment-owned representation of the frozen manifest/cases;
2. validate manifest/schema/action/replay identity before a case can run;
3. represent capability outcomes through exact captured/replayable evidence where possible;
4. implement deterministic replay and trusted state reduction separately from planner output;
5. run the current deterministic baseline through equivalent decision points;
6. preserve comparable, coverage-extension, and non-comparable results separately;
7. prove through focused tests that oracle values are never included in planner input and scored cases cannot mutate policy/catalog/authority.

**Gate:** frozen cases, baseline outputs, replay transitions, grading, and contamination controls
are reproducible without any provider/model call. No model scoring begins before this gate.

### Phase 4 — run model planning pilot outside trusted product authority

Implement the smallest experiment harness needed to:

```text
snapshot
→ model structured plan
→ deterministic admission
→ simulated/replay capability result
→ state update
→ bounded next turn
```

Initial loop bound should be small and explicit. Increase it only if real cases require more steps.

Preserve raw model outputs/diagnostics as untrusted experiment evidence.

Use only the development/calibration set for prompt/schema clarification or model smoke work.
After freezing one exact scored configuration, run the protected set using the precommitted
repeat policy. Do not tune against protected outcomes and then report the reused protected set
as final evidence. A post-score change consumes those instances and requires a fresh protected
set before another final comparison.

Do not place the model in the normal product path during this phase.

### Phase 5 — diagnose failures and compare with baseline

Classify failures by responsibility:

```text
state representation
prompt/contract misunderstanding
action selection
argument binding
stop behavior
proof-strength overclaim
authority/security violation
context-budget problem
model/provider limitation
baseline ambiguity
```

Do not repair every model failure with prompt exceptions tailored to one case. A fixture-shaped prompt is a failed generalization result.

Report case-level traces and aggregate results separately. Do not average away a critical
authority/security/claim violation, and do not combine coverage-extension cases with direct
baseline comparisons into one misleading win rate.

### Phase 6 — disposition gate

End the experiment with one of:

#### Adopt bounded planner architecture

Only if Section 8.7's full adoption gate is satisfied, including at least two independently
justified executable actions and protected alternative-action selection evidence.

Then:

- create/modify the required ADR;
- define product-owned planner contracts;
- integrate the smallest normal-path seam;
- retain deterministic action admission and evidence semantics;
- run focused + integration + full regression validation.

#### Retain as pilot

Use when promising but evidence, reliability, cost, or architecture is insufficient for normal runtime.

#### Reject

Use when agent planning adds little value, creates repeated proof/authority failures, or makes the product harder to reason about than the deterministic baseline.

#### Defer

Use when models/infrastructure are insufficient or the deterministic product still needs prerequisite capabilities before a fair comparison.

### Phase 7 — only if adopted: bounded product integration

A first adopted integration should normally allow the agent to choose among a small catalog of **read-only evidence actions** while existing domain modules continue to establish trusted state.

Do not simultaneously migrate final recommendation policy, semantic extraction, all application orchestration, and target execution into one agent loop.

## 11. Proof obligations before adoption

At minimum, an adopted first planner must demonstrate:

1. every executable action is from the closed catalog;
2. deterministic argument/identity validation precedes execution;
3. no model output can grant authority or mutate the target;
4. typed evidence remains the only path to stronger trusted state;
5. static/runtime and missing/negative proof boundaries remain intact;
6. loop termination is bounded and tested;
7. already-attempted/unavailable actions are not blindly repeated;
8. prompt-injection-shaped evidence cannot change system policy/catalog;
9. materially different frozen cases show useful action/stop behavior;
10. the method compares favorably enough with the deterministic baseline to justify its complexity;
11. traces make action choice, evidence result, and state transition diagnosable;
12. model/provider failure degrades explicitly without destroying the supported deterministic core;
13. development/calibration and protected scoring are separated with an enforced replacement rule after scored-set-driven change;
14. repeat count, aggregation, thresholds, cost ceiling, and disposition mapping were frozen before protected scoring;
15. replay evidence, snapshot/action identity, oracle, baseline output, and state transition are versioned/reproducible;
16. baseline-undefined coverage extension is not represented as a direct comparative win.

## 12. Prohibited scope

This plan does not authorize:

- generic autonomous software-engineering agents;
- arbitrary MCP/plugin/tool ecosystems;
- target-repository writes;
- automatic merge/approval/commenting;
- unrestricted shell execution;
- installing or executing investigated dependency code merely because the model requests it;
- private-repository evidence;
- generic browser/search autonomy;
- multi-agent debate;
- memory/vector databases merely for agent context;
- learned final decision policy without a separate responsibility/evaluation gate;
- replacing deterministic evidence validators with LLM judgments;
- rewriting existing domain modules into prompt logic;
- broad B3/B4/B5 infrastructure merely to support the experiment.
- prompt/model/schema/policy tuning on protected scored outcomes followed by reuse of those same outcomes as final comparison evidence;
- adoption of a general adaptive planner from a one-action catalog;
- post-hoc thresholds, case inclusion, baseline rules, or disposition criteria chosen after protected results are visible.

## 13. Stop line

Stop when an evidence-backed disposition exists:

```text
ADOPT
or
RETAIN AS PILOT
or
REJECT
or
DEFER / RESCHEDULE
```

Do not continue adding models, tools, agents, roles, retries, frameworks, or cases after the owning comparison question is answered.

Do not bypass the checkpoint by treating “the plan is old” or “other B2 work is ready” as a stop condition. Staleness is handled by Phase 0's refreshed reassessment and explicit disposition.

## 14. Learner ownership target

Because this is a flagship learning responsibility, Ali should be able to explain and progressively own:

- why current deterministic evidence capabilities remain authoritative;
- planner versus executor versus evidence-validator responsibilities;
- structured model output versus trusted state;
- action allowlisting and argument validation;
- agent loop state/update/termination;
- why an agent hypothesis is not evidence;
- baseline design and evaluation leakage avoidance;
- one real action-selection trace end to end;
- one failure diagnosis;
- the final adopt/reject/defer reasoning.

AI-assisted implementation is allowed; ownership requires understanding of the central loop and evidence/authority boundaries, not memorization of every helper.
