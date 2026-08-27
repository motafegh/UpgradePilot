# Working Memory — B2/X1 Phase 0 AI-Engineering and Route Re-Baseline

**Date:** 2026-08-27  
**Status:** PHASE 0 COMPLETE — PROCEED TO PHASE 1  
**Current plan:** `../plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md`  
**Audit basis:** `../audits/2026-08-21_AUDIT-005_product-ai-agentic-orchestration-sequencing.md`  
**Accepted deterministic executable baseline:** `b50e4b1a656625c3215dd3fbf08c28012c6d18aa`  
**R7 final handoff:** `2026-08-27_B2-R7-R7.9-R7.10-final-acceptance-and-agentic-handoff.md`

## 1. Phase-0 question

Phase 0 does not ask whether an agent sounds useful in general. It asks whether, **after the accepted R7 deterministic reconciliation**, UpgradePilot still has a concrete orchestration limitation for which a bounded model-driven planner experiment is technically fair, product-admitted, secure enough to evaluate, and meaningfully comparable to the real deterministic baseline.

The allowed Phase-0 dispositions are:

```text
PROCEED TO PHASE 1
or
REJECT CHECKPOINT
or
DEFER / RESCHEDULE CHECKPOINT
```

No planner implementation or product-source mutation is authorized by this record.

## 2. Re-anchored project/route authority

### Project Charter

The Charter still requires every advanced method to have:

```text
observed limitation
+ simpler credible baseline
+ bounded hypothesis
+ measurable success/rejection conditions
+ explicit security/cost/failure modes
+ adopt / retain-as-pilot / reject / defer disposition
```

It also keeps target mutation, automatic merge/comment/review, generic agent platforms, and unsupported safety claims outside the core boundary.

### 90-day route

The controlling route explicitly defines X1 as a non-linear evidence-gated checkpoint that may be entered early from B2 when:

```text
observed admitted limitation exists
+ simpler baseline exists
+ bounded measurable experiment exists
+ security/cost/cleanup are explicit
+ MEMORY.md selects it
+ unfinished B2 core is not silently waived
```

The route also contains the anti-skip rule for a previously scheduled X1 checkpoint whose prerequisite becomes satisfied. R7 acceptance satisfied that trigger; entering this checkpoint is therefore route-compliant, not a silent violation of B2→B3→B4→B5 sequencing.

### Security

`SECURITY.md` remains directly compatible with the proposed first planner boundary:

```text
external repository/upstream/CI/model content = evidence/data
!= project authority
!= authorization
!= permission to mutate or execute unknown code
```

The first planner therefore remains read-only and must not execute target code, create arbitrary URLs, expand credentials, or turn model output into stronger trusted state.

## 3. Accepted deterministic baseline entering the experiment

Accepted executable revision:

```text
b50e4b1a656625c3215dd3fbf08c28012c6d18aa
```

Final R7 acceptance evidence:

```text
focused R3→R6/cleanup/provenance bundle    88 tests / OK
complete deterministic suite               515 tests / OK
compileall                                 PASS
live S001 normal path                      PASS
```

The real current baseline is not a toy rule. It is the accepted deterministic product flow:

```text
public PR / exact identity
→ provider-admitted exact evidence
→ dependency/source interpretation
→ project/environment selection
→ bounded reachability or project-source membership
→ static CI consumption / coverage
→ upstream evidence / bounded semantic extraction where activated
→ mechanism-specific impact/applicability investigation
→ typed application result
```

Any agentic comparison must preserve this baseline honestly.

## 4. Post-R7 orchestration limitation still exists

Current `src/upgradepilot/investigation.py` was inspected after R7.

The normal application function still performs a largely predetermined Python sequence:

```text
investigate_public_pull_request(...)
→ acquire PR / changed files
→ analyze dependency
→ if dependency transition:
   → acquire exact-head workflow runs/jobs/files
   → derive R3→R4/project-source→R5 consumptions
   → evaluate CI coverage
   → acquire package/upstream/release/changelog evidence
   → run bounded support-drop semantic extractor when authority is available
   → build Python-support impact candidate
   → deterministic select_python_support_drop_investigation(...)
   → if selected, acquire the exact target declaration
   → reevaluate relevance/impact
```

This is good deterministic orchestration, but it confirms the same limitation identified by AUDIT-005:

```text
current application sequencing is mostly fixed/mechanism-specific
!= general typed investigation state from which one bounded planner chooses the next useful admitted evidence action
```

The limitation therefore survived R7 rather than being accidentally solved by the source-evidence reconciliation.

## 5. ADR-0006 / local-model reassessment

ADR-0006 remains valid for its **separate bounded semantic-extraction responsibility**.

Current durable local deployment remains:

```text
WSL UpgradePilot
→ loopback HTTP
→ LM Studio on Windows

adopted semantic model key: gemma-4-e4b-it-ud
```

No evidence in Phase 0 requires changing that accepted extractor, model, transport, grounding contract, or provider boundary.

Important separation:

```text
ADR-0006 extraction success
!= evidence that gemma-4-e4b-it-ud is a capable investigation planner
```

The existing local model may be used later as a planning candidate/control only after a planning-specific structured-action smoke/evaluation. It must not be silently promoted from extractor to planner.

## 6. Fresh 2026 AI/LLM engineering reassessment

Phase 0 reviewed current official/recent material only to the depth needed for this bounded responsibility.

### 6.1 Structured tool/action contracts are now mature enough for the experiment

OpenAI's current function-calling documentation supports strict JSON-schema function arguments and recommends strict mode. It also supports disabling parallel tool calls so the model can be constrained to **zero or one function call per turn**. This maps closely to UpgradePilot's planned `AgentPlanResult` / one-next-action contract.

Relevant official source:

- OpenAI, Function calling: https://developers.openai.com/api/docs/guides/function-calling

Key engineering consequence:

```text
model can propose one typed action
!= application must execute it

schema-valid call
!= semantically/authoritatively admitted call
```

UpgradePilot still needs its own deterministic action admission even when a provider guarantees syntactic schema compliance.

### 6.2 Local LM Studio remains a credible experiment transport

Current LM Studio documentation supports:

- JSON-schema structured output;
- model-requested custom tool calls through OpenAI-compatible chat/responses endpoints;
- application-owned tool execution;
- OpenAI-compatible endpoints at the already-admitted local server boundary.

Official sources:

- https://lmstudio.ai/docs/developer/openai-compat/structured-output
- https://lmstudio.ai/docs/developer/openai-compat/tools
- https://lmstudio.ai/docs/developer/openai-compat/responses

LM Studio explicitly notes that structured/tool behavior is model-dependent. Therefore the local transport is plausible, but a planning-capable local model must be measured rather than assumed.

### 6.3 Remote providers are plausible controls, not selected architecture

Current OpenAI and Google Gemini APIs both support application-owned custom function/tool calling and structured results. Gemini's current documentation explicitly separates built-in tools from custom tools and states that, for custom tools, the application executes the requested function.

Official sources:

- OpenAI function calling: https://developers.openai.com/api/docs/guides/function-calling
- Gemini tools: https://ai.google.dev/gemini-api/docs/tools
- Gemini function calling: https://ai.google.dev/gemini-api/docs/function-calling
- Gemini structured output: https://ai.google.dev/gemini-api/docs/structured-output

Anthropic remains a plausible remote comparison provider, but no exact provider/model is selected in Phase 0. Provider/model identity must be frozen later under the evaluation plan with privacy, cost, and repeatability recorded.

### 6.4 No agent framework is currently justified

The first experiment requires only:

```text
snapshot
→ one model planning call
→ parse structured result
→ deterministic admission
→ replay/read-only capability result
→ deterministic state update
→ bounded loop
```

OpenAI's current Agents SDK is a capable framework for cases where an SDK should run the recurring agent loop, state, tools, tracing, handoffs, guardrails, etc. That maturity does **not** establish that UpgradePilot needs the framework. The current first-pilot responsibility does not require specialist handoffs, multi-agent ownership, hosted tool ecosystems, or framework-managed state.

Official source:

- https://developers.openai.com/api/docs/guides/agents

Phase-0 disposition:

```text
first implementation preference = ordinary Python/app-owned loop
agent framework = NOT JUSTIFIED YET
MCP = NOT REQUIRED
multi-agent = NOT REQUIRED
browser/computer/shell tools = EXCLUDED
```

A framework can be reconsidered only if Phase 1–4 exposes a concrete missing capability whose implementation would be materially worse than the dependency cost/complexity.

### 6.5 Evaluation should score traces/actions, not prose plausibility

Current OpenAI agent-evaluation guidance emphasizes end-to-end traces, tool-choice/safety-policy evaluation, then repeatable datasets/eval runs once desired behavior is defined.

Official source:

- https://developers.openai.com/api/docs/guides/agent-evals

That supports the existing UpgradePilot plan:

```text
freeze cases/oracle before tuning
→ capture planner action/state traces
→ score action choice / stop-defer / overclaim / identity / security behavior
→ compare against deterministic baseline
```

The evaluation target is the planner's orchestration responsibility, not whether its written explanation sounds convincing.

## 7. Current prompt-injection / tool-authority reassessment

Prompt injection remains a material unsolved risk, especially when agents consume repository, CI, issue, upstream, or tool-result text and can choose actions.

OpenAI's current agent-safety guidance recommends keeping untrusted variables out of higher-authority messages, constraining data flow with structured outputs, and running trace/eval checks. It explicitly notes structured isolation reduces but does not eliminate prompt-injection risk.

Official source:

- https://developers.openai.com/api/docs/guides/agent-builder-safety

Anthropic's recent 2026 agent-security work likewise emphasizes that prompt injection remains a live problem and that blast radius should be reduced by constraining what an agent can access/do rather than assuming model robustness is perfect.

Recent sources:

- Anthropic, *Trustworthy agents in practice*, 2026-04-09: https://www.anthropic.com/research/trustworthy-agents
- Anthropic, *How we contain Claude across products*, 2026-05-25: https://www.anthropic.com/engineering/how-we-contain-claude

UpgradePilot consequence:

```text
untrusted repository/upstream/tool text
→ data field in typed/replay evidence
!= developer/system instruction
!= action catalog
!= authorization
```

The frozen prompt-injection-shaped case should be retained and treated as a required discriminating security case, not an optional curiosity.

The first experiment's deliberately small blast radius remains:

```text
closed read-only action catalog
+ no arbitrary URL/shell/browser/MCP
+ deterministic exact identity/argument admission
+ typed result/problem families
+ bounded iterations
+ no target mutation
+ no model authority over evidence promotion
```

This is sufficient to make an **experiment** reasonable; it is not proof that a later product agent would be safe to adopt.

## 8. AI/LLM role inventory after re-baseline

### Already adopted

```text
bounded upstream support-drop semantic candidate extraction
→ ADR-0006
→ model output untrusted
→ deterministic exact-source recovery + validation
```

### In scope for first planner evaluation

```text
1. evidence-gap diagnosis
2. choose ONE admitted next investigation action
3. bounded hypothesis / expected-outcome framing
4. explicit adaptive stop / defer
```

### Plausible later roles but out of first-pilot scope

```text
cross-evidence synthesis/explanation
stronger planning across more capability families
maintainer-action recommendation reasoning
```

Each would need a separate evidence/authority gate before adoption.

### Still unjustified / excluded

```text
generic multi-agent debate/personas
agent framework merely for loop syntax
MCP/plugin ecosystem as product architecture
arbitrary web/browser/shell/code execution
arbitrary repository-file selection
vector DB/RAG merely for agent context
target repository mutation
automatic merge/comment/review
model-owned compatibility/safety truth
model-owned source authority or evidence promotion
```

## 9. Frozen evaluation cases remain discriminating

The post-R7 evidence does not make the planned cases stale.

```text
S001
→ positive docs selection + transitive uv reachability + CI support
→ pressure correct stopping / avoid redundant evidence requests

S011
→ affected mlx != selected dev
→ pressure non-selection and proof-strength discipline

S005
→ tox-mediated lock use outside direct uv selector support
→ pressure correct defer/support-boundary recognition

Python-support deterministic investigation case
→ pressure whether planner can select the same useful exact target-declaration acquisition as current deterministic selector

Correct STOP/DEFER case
→ pressure against endless tool use

Prompt-injection-shaped evidence case
→ pressure untrusted data vs authority/action-catalog separation
```

No case is removed in Phase 0.

## 10. Phase-0 decision

### Observed limitation

```text
YES
→ current application orchestration remains largely fixed and mechanism-specific
```

### Real simpler baseline

```text
YES
→ accepted b50e4b1 deterministic product baseline
→ 88 focused + 515 full + live S001 accepted evidence
```

### Bounded hypothesis / measurable rejection

```text
YES
→ existing plan has action/stop/security/generalization/cost metrics
→ explicit ADOPT / RETAIN AS PILOT / REJECT / DEFER gate
```

### Security / authority boundary adequate for an experiment

```text
YES
→ closed read-only catalog + deterministic admission + typed state + bounded loop
→ prompt injection remains a scored failure mode, not assumed solved
```

### Current model/tooling capability sufficient to run a fair pilot

```text
YES
→ structured outputs and application-owned tool calling are mature across local/remote options
→ provider/model quality still must be measured
```

### Framework dependency required now

```text
NO
```

### ADR-0006 change required now

```text
NO
```

## 11. Disposition

```text
PHASE 0 = COMPLETE
DISPOSITION = PROCEED TO PHASE 1
```

This means:

```text
proceed to read-only capability/orchestration inventory
!= adopt an agent
!= select a provider/model
!= add a framework
!= modify product source
```

Phase 1 should now map only capabilities relevant to the first planner:

```text
action candidate
→ owning function/module
→ exact typed inputs
→ typed result/problem
→ proposition/proof boundary
→ read-only/security class
→ rough cost/latency class
```

and identify the **smallest orchestration seam** at which a planner could choose actions without becoming a semantic/evidence authority.
