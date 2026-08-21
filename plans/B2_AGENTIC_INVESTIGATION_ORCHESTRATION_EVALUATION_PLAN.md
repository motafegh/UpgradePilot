# B2 Product Agentic Investigation / Orchestration Evaluation Plan

**Status:** Approved bounded evaluation plan; live activation remains owned only by `../MEMORY.md`  
**Owner:** Ali Rajabi  
**Audit basis:** [`../audits/2026-08-21_AUDIT-005_product-ai-agentic-orchestration-sequencing.md`](../audits/2026-08-21_AUDIT-005_product-ai-agentic-orchestration-sequencing.md)  
**Stable product authority:** [`../PROJECT_CHARTER.md`](../PROJECT_CHARTER.md)  
**Route authority:** [`UPGRADEPILOT_90_DAY_PLAN.md`](UPGRADEPILOT_90_DAY_PLAN.md)  
**Current deterministic investigation responsibility:** [`B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md`](B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md)  
**Current dependency/CI capability pressure:** [`B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md`](B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md)  
**Existing bounded semantic-model architecture:** [`../docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md`](../docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md)

## 1. Responsibility

Evaluate whether UpgradePilot should add a **product-level agent/controller** that adaptively chooses the next admitted read-only investigation action from current typed evidence state, while preserving deterministic evidence authority, proof boundaries, security controls, and explicit stopping.

The owning product question is:

> Given a partially established dependency-update investigation, can a bounded model-driven controller identify the material evidence gap, choose a useful admitted next investigation action (or stop/defer), and improve investigation flexibility/generalization over the current deterministic/mechanism-specific orchestration without introducing unsupported claims or unsafe authority?

This plan evaluates that method. It does **not** pre-adopt an agent architecture.

## 2. Why this responsibility is now admitted for evaluation

The project now has a materially stronger substrate than when advanced methods were originally deferred:

```text
exact PR/revision/file acquisition
+ typed dependency-change evidence
+ typed source/environment context
+ bounded static workflow IR
+ selected-environment membership
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
input schema
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
arguments? 
target_proposition
reason
expected_result_categories
limitations[]
```

The model cannot create a new action ID, elevate authority, or redefine result semantics.

### 5.4 Deterministic action admission

Before execution, code must verify:

```text
action exists in current catalog
+ action is allowed in current state
+ arguments match exact schema/identity constraints
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

The evaluation should ask whether the agent improves the **owning investigation/orchestration responsibility**, not merely whether it writes a plausible explanation.

## 7. Frozen evaluation set

Use a small but materially contrasting set before live adoption.

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

### Optional additional cases

Add only when they discriminate the method:

- unavailable source;
- contradictory evidence;
- already-attempted failed action;
- changed head/revision mismatch;
- prompt-injection-shaped untrusted source text contained inside evidence.

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

### Phase 0 — route/admission reconciliation before product code

Before implementation or model experimentation:

1. re-read `MEMORY.md`, `PROJECT_CHARTER.md`, `UPGRADEPILOT_90_DAY_PLAN.md`, this plan, and AUDIT-005;
2. confirm the active learning route has reached its intended handoff;
3. resolve the current X1 sequencing issue explicitly rather than silently running an early agentic experiment against the controlling route;
4. update the route only if the user-selected priority remains and the experiment is still justified by current source/state;
5. freeze the exact baseline revision and current deterministic orchestration behavior.

This phase may end the plan early if later evidence makes the experiment unnecessary or wrongly timed.

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
- mismatched identities/revisions are rejected;
- invalid arguments are rejected;
- forbidden mutation classes are rejected;
- stop/defer states require no tool execution;
- attempted-action history prevents blind loops where required.

If this contract creates a consequential durable architecture/dependency direction, create an ADR before product adoption. Experiment-only types do not require an ADR merely for existence.

### Phase 3 — build deterministic baseline/replay harness

Before model scoring:

1. freeze the evaluation cases;
2. freeze expected acceptable actions/stops and forbidden overclaims;
3. represent tool outcomes through captured/replayable evidence where possible;
4. run the current deterministic baseline through equivalent decision points;
5. record where baseline behavior is fully defined versus mechanism-specific/missing.

The evaluation oracle must be frozen before model tuning on the scored set.

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

### Phase 6 — disposition gate

End the experiment with one of:

#### Adopt bounded planner architecture

Only if comparative evidence supports material value and safe authority boundaries.

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
12. model/provider failure degrades explicitly without destroying the supported deterministic core.

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

## 13. Stop line

Stop when an evidence-backed disposition exists:

```text
ADOPT
or
RETAIN AS PILOT
or
REJECT
or
DEFER
```

Do not continue adding models, tools, agents, roles, retries, frameworks, or cases after the owning comparison question is answered.

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
