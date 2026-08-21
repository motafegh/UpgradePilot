# AUDIT-005 — Product AI / Agentic Orchestration and Sequencing Reassessment

**Date:** 2026-08-21  
**Inspected revision:** `2b413869feb65e69b5081eefb7dcab193019c7eb`  
**Trigger:** reassess whether UpgradePilot's narrow current LLM use is a necessary product limit or whether product-level AI/agentic orchestration has been deferred too far  
**Disposition:** advance a bounded product-level agentic investigation/orchestration evaluation after the active learning route, before resuming the previously queued ordinary B2 continuation  
**Authority:** non-controlling audit evidence; `MEMORY.md` owns live selection, plans own execution, and accepted specifications/ADRs/source/tests own behavior and architecture

## 1. Question and scope

The concrete question is:

> UpgradePilot currently uses a local LLM only for a highly bounded upstream semantic-extraction role. Is broader AI/agentic product behavior absent because the current product cannot or should not use it, or because the project deliberately prioritized deterministic evidence capabilities and has not yet built the agent/controller layer?

This audit inspects:

- the stable Charter and 90-day route;
- current B2 investigation and dependency/CI plans;
- the accepted bounded local semantic extractor;
- the older LLM reevaluation plan;
- product-ambition material concerning targeted investigation;
- coding-agent governance material, to distinguish project-development agents from product-runtime agents;
- the current `investigation.py` orchestration shape.

This audit does **not** select a provider/model/framework, authorize autonomous external mutation, or declare that an agentic method is already better than the deterministic baseline.

## 2. Current implementation observation

### 2.1 Current product LLM role is real but deliberately narrow

ADR-0006 and `src/upgradepilot/upstream/support_drop_extractor.py` implement:

```text
CrossedReleaseSourceWindow
→ one local LM Studio structured-output request
→ untrusted semantic candidate selection
→ deterministic exact-source recovery / validation
→ grounded support-drop claim or explicit problem
```

The model does not own source authority, target relevance, compatibility, safety, maintainer action, tool execution, or external mutation.

This is therefore not "no AI". It is **one evaluated semantic responsibility with a narrow authority boundary**.

### 2.2 Current application orchestration is mostly predetermined Python control flow

`investigate_public_pull_request(...)` currently sequences provider/domain capabilities directly in application code. The Python-support path includes one deterministic mechanism-specific investigation selector:

```text
impact assessment
→ select_python_support_drop_investigation(...)
→ exact target declaration acquisition
→ relevance evaluation
→ impact reevaluation
```

The current runtime does not maintain a general product-level investigation state from which an LLM/agent chooses among multiple admitted evidence actions and iterates until a stop condition.

This is the central architectural gap relevant to the user's question.

## 3. Existing documents already anticipate part of the idea

### 3.1 Product ambition already describes an adaptive investigation system

The 2026-07-20 product-ambition proposal describes a stronger product that:

```text
reconstructs evidence
→ determines whether current evidence is sufficient
→ selects the next most valuable investigation step
→ produces a reproducible recommendation and decision trace
```

Its Targeted Check Planner further proposes unresolved evidence → candidate checks → uncertainty addressed → expected information value → ranked checks.

This material is non-controlling, but it proves that adaptive investigation was not absent from the product imagination.

### 3.2 The active B2 impact plan already owns deterministic investigation selection

`B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md` already requires:

```text
material unresolved/conflicted proposition
→ discriminating target
→ selected investigation / conditional sequence / justified stop
→ observation
→ reevaluation
```

It intentionally rejects a generic investigation planner as baseline architecture and keeps the current implementation small and mechanism-specific.

Therefore a future agent/controller would not invent a new product question. It would be an alternative/generalizing method for an already accepted investigation responsibility.

### 3.3 The existing local-LLM reevaluation plan is not the right owner

`B2_LOCAL_LLM_SEMANTIC_EXTRACTION_REEVALUATION_PLAN.md` explicitly limits the model to candidate semantic extraction and forbids tool calls, evidence-authority selection, evidence-sufficiency decisions, stopping decisions, and maintainer actions.

Stretching that plan into an agentic controller would destroy its bounded responsibility.

### 3.4 The agent-governance plan is a different kind of agent

`UPGRADEPILOT_AGENT_GOVERNANCE_REFINEMENT_AND_EVALUATION_PLAN.md` concerns coding agents/AI assistants operating **on the UpgradePilot repository**. It explicitly excludes product runtime behavior.

It must not be cited as evidence that UpgradePilot already contains a product-runtime agent architecture.

## 4. Sequencing conflict found

The controlling 90-day route currently places:

```text
B2
→ B3
→ B4
→ B5
→ X1 evidence-gated experiments
```

and X1 explicitly includes model/graph/agentic experiments.

That sequence was a rational protection against premature advanced-method adoption while the deterministic product lacked a credible baseline.

The situation has materially changed:

- B2 now has substantial exact evidence acquisition and typed domain results;
- dependency/environment/CI capabilities through Cluster 5 are implemented and validated;
- the application already exposes a concrete deterministic investigation-selection seam;
- the bounded local semantic extractor has already demonstrated how model output can remain untrusted while deterministic code retains authority;
- the current orchestration is visibly fixed/mechanism-specific, which is an observable limitation rather than a hypothetical desire for "more AI".

The original reason for deferring **all** agentic evaluation until after B5 is therefore weaker than it was at route creation.

## 5. Findings

### AUDIT-005-F1 — Broader agentic behavior is technically feasible

**Finding:** ACCEPTED.

Nothing in the current evidence model prevents a product-level agent/controller from operating over typed, read-only UpgradePilot capabilities.

In fact, the current explicit states, provenance, `unresolved` behavior, proof boundaries, and deterministic adapters provide a stronger substrate for an agent than an unconstrained prompt-first design would have.

### AUDIT-005-F2 — Broader agentic behavior has been deferred, not disproven

**Finding:** ACCEPTED.

The current narrow model role is the result of scoped method admission and sequencing, not evidence that LLM/agentic orchestration is categorically inappropriate for UpgradePilot.

The repository has not yet run a product-level comparative experiment showing that an agent controller is worse, unnecessary, or unsafe when bounded by the existing evidence system.

### AUDIT-005-F3 — The strongest first agentic role is investigation orchestration, not replacement of deterministic evidence semantics

**Finding:** ACCEPTED.

The first serious product-level agentic experiment should target:

```text
current typed investigation/evidence state
→ identify material evidence gap / hypothesis
→ choose one admitted read-only evidence action
→ receive typed result/problem
→ update investigation state
→ choose next action or stop
```

It should **not** initially replace:

- exact repository/PR/package identity;
- dependency extraction/reconciliation;
- package-manager/environment membership semantics;
- workflow parsing;
- CI proof-strength composition;
- exact-source grounding;
- security/authorization boundaries;
- final maintainer-action policy.

This makes current deterministic modules agent tools/evidence authorities rather than discarded code.

### AUDIT-005-F4 — Additional model roles are plausible but should be staged

Useful candidate roles, ordered from nearer-term to stronger authority, are:

1. **evidence-gap diagnosis / hypothesis generation**;
2. **next admitted investigation-action selection**;
3. **adaptive stopping / escalation recommendation**;
4. **bounded semantic extraction over unstructured evidence** (already proven in one narrow role);
5. **cross-evidence synthesis/explanation** from typed evidence;
6. **maintainer-action recommendation reasoning** only after separate comparative evidence and policy-boundary work.

The first pilot should not combine all six.

### AUDIT-005-F5 — A generic multi-agent/framework architecture is not justified

**Finding:** KEEP EXCLUDED.

There is currently no evidence requiring:

- LangChain/LangGraph or another orchestration framework;
- MCP as an internal product architecture requirement;
- multi-agent personas/debate;
- vector stores/RAG infrastructure;
- autonomous shell execution;
- autonomous target-repository mutation;
- an LLM-generated universal evidence graph;
- a cloud-model fallback.

The smallest credible experiment is one controller, a closed action catalog, deterministic execution adapters, typed observations, bounded iterations, and explicit stopping.

### AUDIT-005-F6 — The experiment must compare against the current deterministic planner/orchestration baseline

**Finding:** REQUIRED.

The agentic method must not be adopted because it is more fashionable or expressive.

The baseline is the existing deterministic/mechanism-specific orchestration and investigation selection.

A product-level agentic pilot must demonstrate material value such as:

- better changed-case action selection across materially different evidence gaps;
- less fixture/mechanism-specific application branching;
- correct abstention when no admitted action can resolve the gap;
- no stronger unsupported claims;
- acceptable latency/cost/resource behavior;
- debuggable action/evidence traces.

### AUDIT-005-F7 — Current route sequencing should be reassessed before more ordinary B2 expansion

**Finding:** REASSESS / ADVANCE.

The user has explicitly selected broader product AI/agentic work as the next implementation priority after the current learning plans.

The correct repository consequence is:

```text
finish active learning route
→ execute bounded agentic orchestration plan
→ first reconcile route/admission boundary
→ run frozen comparative pilot
→ adopt / retain as pilot / reject / defer
→ only then decide whether to resume source-clarity / Cluster 6 / other B2 work
```

This does not mean the agentic method is pre-adopted. It means its **evaluation** becomes the next selected product responsibility.

## 6. Proposed first agent boundary

A useful first conceptual contract is:

```text
InvestigationSnapshot
    established evidence
    unresolved/conflicted propositions
    attempted actions + outcomes
    admitted action catalog
    proof/authorization constraints

        ↓

AgentPlanner
    chooses ONE next action
    or explicit STOP / DEFER
    with reason tied to current gap

        ↓

Deterministic Action Executor
    validates action identity/arguments
    performs only admitted read-only capability
    returns typed evidence/problem

        ↓

State Reducer / Existing Domain Logic
    validates/interprets/reconciles result
    updates trusted investigation state

        ↺ bounded loop
```

The model proposes; deterministic code admits, executes, and establishes evidence.

## 7. Security and authority boundary

The first pilot must preserve:

```text
model output != authorization
model-selected action != executable until deterministically admitted
untrusted source text != instructions
agent hypothesis != established evidence
agent stop/recommendation != final maintainer action
```

Initial allowed actions should be read-only public-evidence capabilities only.

No arbitrary shell command, repository mutation, automatic merge/comment/review, credential expansion, paid action, or open-ended URL/tool invocation is admitted by this audit.

## 8. Evaluation cases

Use frozen cases with materially different control-flow pressure, not one happy path:

- **S001** — positive selected docs environment / transitive Soup Sieve path;
- **S011** — affected `mlx` environment versus selected `dev` environment;
- **S005** — tox-mediated lock-consumption shape outside current direct selection support;
- at least one Python-support case where the existing deterministic investigation selector has a known next target;
- at least one case where the correct result is **stop/defer/unresolved** rather than another action.

The first evaluation can use replay/frozen tool results so model planning quality is tested separately from network variance and third-party execution.

## 9. Disposition

1. Keep ADR-0006 unchanged; it still correctly owns the narrow local semantic extractor.
2. Keep the coding-agent governance plan separate from product runtime architecture.
3. Do not turn existing deterministic domain modules into LLM prompts.
4. Create a dedicated bounded product-level agentic investigation/orchestration evaluation plan.
5. Record in `MEMORY.md` that, after the active learning plans finish, this evaluation is the selected next product responsibility before the previously queued ordinary B2 continuation.
6. At execution entry, reconcile the 90-day X1 sequencing boundary before product-source adoption; do not silently violate the controlling route.
7. Adopt permanent product architecture only after comparative evidence; otherwise retain as experiment, reject, or defer.

## 10. References

- `PROJECT_CHARTER.md`
- `plans/UPGRADEPILOT_90_DAY_PLAN.md`
- `plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md`
- `plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md`
- `plans/B2_LOCAL_LLM_SEMANTIC_EXTRACTION_REEVALUATION_PLAN.md`
- `plans/UPGRADEPILOT_AGENT_GOVERNANCE_REFINEMENT_AND_EVALUATION_PLAN.md`
- `proposals/2026-07-20_UPGRADEPILOT_PRODUCT_AMBITION_AND_ENHANCEMENT_PROPOSAL.md`
- `docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md`
- `src/upgradepilot/upstream/support_drop_extractor.py`
- `src/upgradepilot/investigation.py`
