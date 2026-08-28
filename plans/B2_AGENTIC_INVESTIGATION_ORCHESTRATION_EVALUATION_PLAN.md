# B2 Product Agentic Investigation / Orchestration Evaluation Plan

**Status:** APPROVED + ACTIVATED — R7 activation prerequisite satisfied; checkpoint remains open until an explicit `ADOPT` / `RETAIN AS PILOT` / `REJECT` / `DEFER` disposition  
**Owner:** Ali Rajabi  
**Live-state owner:** `../MEMORY.md`  
**Stable product authority:** `../PROJECT_CHARTER.md`  
**Route authority:** `UPGRADEPILOT_90_DAY_PLAN.md`  
**Audit basis:** `../audits/2026-08-21_AUDIT-005_product-ai-agentic-orchestration-sequencing.md`  
**Accepted evaluation protocol/oracle:** `B2_X1_PHASE3_EVALUATION_PROTOCOL.md` (`b2-x1-phase3a-v2`)  
**Existing bounded semantic-model method:** `../docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md`

## 0. Checkpoint and proportionality rule

The checkpoint itself is mandatory because AI/agentic orchestration had repeatedly been postponed while deterministic capabilities expanded. Adoption is **not** mandatory.

```text
R7 accepted deterministic baseline
→ B2/X1 bounded planner evaluation
→ explicit evidence-backed disposition
→ only then ordinary B2 continuation
```

The purpose is to obtain a useful engineering decision about bounded model-driven investigation planning. It is **not** to build a production-grade agent platform, perfect evaluation framework, or exhaustive research program before the first useful model interaction.

### 0.1 Anti-rabbit-hole / anti-ceremony guard

Apply `OPERATING_GUIDE.md` proportionality and Ceremony Tax directly to this checkpoint:

1. **Investigate only decision-changing unknowns.** Stop an investigation when another fact is unlikely to change the next gate, responsibility, or claim.
2. **Prototype before infrastructure completion.** Once the minimum authority/schema/request boundary is proven, prefer a small development-only local-model smoke over building the entire protected-scoring system first.
3. **Keep hard constraints hard; keep pilot process proportional.** Exact identity, closed read-only authority, deterministic admission, proof-strength boundaries, no target mutation, and protected-set contamination controls remain strict. Formatting, report depth, generalized harness abstractions, exhaustive telemetry, and optional checks do not receive the same burden.
4. **No perfection gate.** The pilot needs evidence sufficient for its bounded decision, not proof of production reliability or completeness across every future agent pattern.
5. **No speculative machinery.** Do not add frameworks, services, generic action systems, extra agent roles, abstractions, manifests, graders, or case families until a current gate requires them.
6. **No under-engineering either.** Early model smoke is allowed only after the planner-facing request is isolated from oracle metadata, strict structured output/admission remains enforced, and the local-only/no-mutation boundary is intact.
7. **Preparation reassessment trigger.** If roughly two bounded engineering slices in a row add only pre-model preparation without producing new discriminating evidence, reassess whether the next preparation item is actually required before a development smoke. Simplify or postpone it unless a concrete risk/proof dependency justifies it.
8. **Learning breadth matters.** This flagship checkpoint should expose Ali to real LLM planning, structured outputs, local inference, prompt/eval iteration, replay, baseline comparison, and failure diagnosis. Do not spend most of the checkpoint on pre-LLM ceremony when those later concepts can be reached safely with a smaller gate.

These guards narrow process overhead; they do not weaken product evidence authority or the accepted protected-scoring oracle.

## 1. Responsibility

Evaluate whether UpgradePilot should add a **bounded product-level planner/controller** that chooses the next admitted read-only investigation action from current typed evidence state while deterministic code retains authority, execution, evidence interpretation, proof composition, and final trusted state.

Owning question:

> Given a partially established dependency-update investigation, can a bounded model-driven controller identify the material evidence gap, choose a useful admitted next investigation action (or stop/defer/unresolved), and add useful flexibility over current fixed/mechanism-specific orchestration without unsupported claims or unsafe authority?

This plan evaluates that method. It does not pre-adopt an agent architecture.

## 2. Smallest method under evaluation

```text
trusted planning question + typed InvestigationSnapshot
        ↓
local model proposes ONE admitted action
or STOP / DEFER / UNRESOLVED
        ↓
deterministic admission
        ↓
read-only capability execution or frozen replay
        ↓
existing deterministic interpretation/state update
        ↓
bounded next turn or stop
```

### Model may own only

- evidence-gap diagnosis;
- choosing one action from the closed catalog;
- bounded reason / expected-result framing;
- stop / defer / unresolved planning disposition.

### Deterministic code continues to own

- authorization and exact source identity;
- action catalog and locator binding;
- mutation/read-only boundary;
- capability execution;
- parsing and evidence promotion;
- proof-strength composition;
- security boundary;
- compatibility/safety truth;
- final trusted state.

### Explicitly outside the first pilot

- final maintainer action;
- automatic merge/review/comment;
- arbitrary shell/code execution;
- arbitrary URL/file/source selection;
- target-repository mutation;
- multi-agent systems;
- agent frameworks merely for loop syntax;
- generic browser/plugin/MCP autonomy;
- memory/vector infrastructure;
- migration of domain truth into prompts.

## 3. Accepted experiment contract and evaluation protocol

Phase 2 already established the experiment-owned contract/admission boundary under `experiments/`:

```text
InvestigationSnapshot
AllowedInvestigationAction
AgentPlanResult
admit_agent_plan(...)
```

The first real action is:

```text
acquire_exact_target_python_declaration
```

Repository/revision/path are pre-bound by trusted catalog state; the model does not invent them.

Phase 3A accepted `B2_X1_PHASE3_EVALUATION_PROTOCOL.md` (`b2-x1-phase3a-v2`). That protocol owns the exact development/protected cases, planning questions, oracle, replay expectations, thresholds, contamination rules, and protected disposition mapping. This plan references those details rather than re-specifying them.

The current one-action catalog can evaluate evidence-gap diagnosis plus action-vs-`stop | defer | unresolved`. It cannot justify a claim of general alternative-action planning, and general-planner `ADOPT` remains unavailable unless a second independently justified action appears through real product work.

## 4. Baseline and comparison rule

Use the real deterministic baseline:

```text
current application-fixed sequencing
+ current mechanism-specific investigation selection
+ current deterministic stop/non-activation behavior
```

Never manufacture a weak baseline so the model appears useful.

Classify protected decisions as already frozen by the accepted protocol:

- **comparable** — direct baseline comparison is legitimate;
- **coverage extension** — planner behavior may add coverage, but baseline absence is not a win;
- **non-comparative** — semantic/security pressure only.

## 5. Evaluation discipline: strict where it matters

The following remain zero-tolerance for accepted protected outputs:

- action/catalog/identity escape;
- target mutation or unauthorized execution;
- untrusted evidence becoming policy/tool authority;
- missing/unresolved evidence becoming a negative fact;
- static evidence becoming invented runtime proof;
- compatibility/safety/merge authority from insufficient evidence.

Development and protected material remain separated. Protected outcomes may not be used to tune a configuration and then be reused as final evidence.

Everything else should be proportionate to the pilot claim. A development smoke does not need production-grade observability, exhaustive resource accounting, or every protected-case implementation before it can teach us whether the model follows the basic planner contract.

## 6. Provider / implementation preference

Use LM Studio local inference only through the accepted WSL↔Windows loopback boundary. No remote/cloud fallback or paid-provider use is admitted by this checkpoint.

Prefer the smallest implementation:

```text
ordinary Python
+ one direct model request per planning turn
+ strict structured output
+ deterministic admission
+ bounded replay/loop only when needed
```

Do not add an agent framework unless ordinary Python demonstrably blocks a required capability.

The previously evidenced local Gemma deployment is only a candidate/control. A fresh local inventory/readiness check is enough for a **development smoke**; full scored configuration identity is required only before protected scoring.

## 7. Calibrated execution sequence

Phases 0–3A are complete and remain historical accepted work. The current live continuation is Phase 3B.

### Phase 3B-1 — minimum model-ready deterministic slice

Build only enough deterministic machinery to make an early local development smoke meaningful and safe.

Required before the first development model call:

1. planner request projection excludes oracle/partition/grader metadata;
2. strict output schema and Phase-2 deterministic admission remain green;
3. at least one development `choose_action` case and one contrasting no-tool development case can be rendered reproducibly;
4. exact pre-bound action identity cannot be changed by model output;
5. local loopback/no-proxy transport readiness can be established without remote fallback.

The current real-S001 request/oracle-isolation slice is valid implementation evidence for items 1, 2, and the shared renderer boundary, but the **protected S001 case itself must not be used for prompt/model tuning**.

**Minimum gate:** focused deterministic tests for the request renderer + Phase-2 admission pass, and the development cases needed for smoke are constructible. Do not require all protected cases, replay, baseline aggregation, grader infrastructure, run manifests, or shuffle machinery before this gate.

### Phase 4A — early development-only local-model smoke

After the Phase 3B-1 minimum gate, move to the actual LLM early.

Use only the accepted **development/calibration** cases. Start with a very small bounded smoke, normally about **3–6 semantic calls** to one locally available candidate configuration.

Purpose:

- verify local transport and strict structured-output compatibility;
- see whether the model can choose A1 on a simple action case;
- see whether it can produce at least one no-tool disposition;
- expose obvious prompt/schema/model misunderstandings;
- inspect one or two real failure modes before investing in the full scoring harness.

This is development evidence, **not protected scoring and not a quality/adoption conclusion**.

Allow only small generic corrections justified by development results, such as transport/schema compatibility or one generic task-instruction clarification. Do not start case-specific prompt patching.

If the candidate cannot follow the basic contract after a small bounded development attempt, prefer `DEFER`, `REJECT` for that configuration, or a clearly justified model change over building more evaluation infrastructure around a non-viable planner.

### Phase 3B-2 — complete only the scoring machinery that survived the smoke

If Phase 4A shows basic planner viability, complete the deterministic machinery actually required for protected scoring:

1. reconstruct the remaining frozen protected cases;
2. implement the frozen S001 replay/state transition;
3. implement baseline records only where the protocol marks comparison legitimate;
4. implement deterministic grading/claim checks and human-review record shape at the minimum useful level;
5. implement the scored run manifest/digests, reproducible order, and contamination controls required by the accepted protocol;
6. validate the complete protected request set without calling a model.

Do not generalize these pieces into a framework. Build directly from the accepted protocol and refactor only when repetition creates a demonstrated maintenance problem.

**Protected-scoring gate:** every frozen protected decision/replay can be reconstructed reproducibly; oracle fields cannot enter planner input; baseline/grading/manifest rules are fixed; deterministic tests pass without a model call.

### Phase 4B — protected local-model pilot

Freeze one exact local model/deployment/prompt/schema/sampling configuration and execute the accepted protected protocol.

The accepted protocol currently requires:

```text
3 repeats × 8 protected decisions = 24 scored decisions
6 / 6 comparable decisions exact
>= 22 / 24 overall task decisions
>= 2 / 3 per decision point
>= 22 / 24 human claim/limitation passes
0 critical authority/identity/proof violations
```

Preserve raw model output as untrusted evidence. Do not tune from protected outcomes and then reuse the same protected set as final evidence.

### Phase 5 — diagnose and compare

Classify only material failure classes:

```text
state representation
prompt/contract understanding
action or stop/defer selection
proof-strength/authority error
model/transport limitation
baseline ambiguity
```

Avoid building a taxonomy for every wording variation. Diagnose enough to answer whether the method is useful and why.

### Phase 6 — disposition

End with one explicit evidence-backed disposition:

- **RETAIN AS PILOT** — promising bounded value, but not enough for product adoption;
- **REJECT** — insufficient value or unacceptable proof/authority behavior;
- **DEFER** — comparison cannot be completed fairly because of a concrete model/infrastructure/capability blocker;
- **ADOPT** — available only if a later expanded evaluation satisfies the stronger multi-action adoption requirements; unavailable from the current one-action protected protocol alone.

### Phase 7 — only after a separately justified adoption

Integrate the smallest product-owned planner seam while keeping deterministic evidence/action authority. Do not migrate multiple independent responsibilities into one agent loop at once.

## 8. Stop / reassessment rules

Stop or simplify preparation when:

- the next preparatory artifact/check cannot change the next model-development gate;
- the same proof is already established by a stronger owner/test;
- a proposed abstraction exists only for possible future models/cases;
- a second/third round of planning is refining wording rather than removing a real ambiguity;
- development smoke can answer the uncertainty more cheaply than further analysis;
- the owning comparison question has enough evidence for a disposition.

Continue deeper only when a concrete failure, risk, protected-scoring requirement, or real product responsibility creates the need.

Do not continue adding models, tools, cases, retries, frameworks, reports, or infrastructure after the owning comparison question is answered.

## 9. Learning-by-Doing target

This checkpoint should teach through the real build rather than through prolonged pre-LLM theory. Ali should progressively understand and experience:

- deterministic evidence authority versus model planning;
- planner request/state/action contracts;
- structured model output and deterministic admission;
- local LM Studio inference and model configuration;
- prompt/schema iteration on development cases;
- action vs stop/defer/unresolved behavior;
- replay/state update;
- protected evaluation and contamination control;
- baseline comparison;
- one real model failure diagnosis;
- final retain/reject/defer reasoning.

### 9.1 AI/LLM engineering concept exposure

This flagship checkpoint should also deliberately teach the broader **AI/LLM engineering concepts** that appear through the real UpgradePilot implementation. Do not let Ali learn only project-specific class/function names when the same mechanism has a useful industry/common engineering name.

For each material AI/LLM mechanism encountered, teach proportionately:

```text
common concept / terminology
→ practical problem it solves
→ where it appears in the real UpgradePilot flow
→ implementation/data/control boundary
→ important failure mode / trade-off
→ depth needed now vs deliberately deferred
```

Concepts **directly used by this checkpoint** should be learned properly as they arise, including where applicable:

- **evaluation harnesses** — controlled machinery around cases, requests, execution, outputs, replay, grading, and comparison;
- **structured outputs / JSON Schema contracts** — constraining provider output shape without confusing schema validity with semantic/action authority;
- **agent state and action spaces** — trusted state, closed action catalog, bounded planner choices, and explicit termination/abstention states;
- **tool/action allowlisting and deterministic guardrails/admission** — model proposal versus trusted authorization/execution;
- **context engineering / request projection** — selecting exactly what trusted state the model receives and excluding irrelevant or evaluator-only information;
- **prompt architecture** — system task, trusted planning question, structured snapshot, and untrusted evidence roles;
- **oracle/label leakage and evaluation contamination** — why evaluator answers, partition labels, protected outcomes, or tuning feedback must not leak into scored model input/evidence;
- **development/calibration vs protected evaluation sets** — using early cases for iteration without converting them into final evidence;
- **smoke evaluation / capability probing** — reaching a small real model interaction early to expose transport/schema/reasoning failures before building full infrastructure;
- **replay and reproducibility** — deterministic reconstruction of state/results around nondeterministic model behavior;
- **sampling configuration and repeated runs** — temperature/seed/model variability and why repeated observations are still not a production-reliability claim;
- **tracing / observability / failure taxonomy** — preserving enough request/output/admission/result evidence to distinguish transport, parsing, policy, reasoning, and baseline failures;
- **local inference runtime/deployment** — LM Studio, model identity, quantization/context/runtime configuration, and localhost transport as an engineering boundary rather than merely a GUI choice;
- **prompt-injection / untrusted-data boundaries** — untrusted source/model/tool text remains data and cannot become policy, catalog authority, or maintainer action.

Also provide **adjacent high-value exposure** when a concept is materially connected to the current mechanism, for example hooks/lifecycle callbacks, middleware, function/tool calling, agent loops/state machines, checkpoints, model routing/fallbacks, semantic retries, prompt/version management, caching, LLM-as-a-judge, MCP, RAG, or agent frameworks. Explain what the concept is and how it relates, but **do not add it to UpgradePilot merely for exposure**. Implement/use it only when a real current responsibility or demonstrated failure justifies it.

Use three learning-depth classes:

```text
DIRECTLY USED
→ learn the concept and our real implementation well enough to explain, trace, test, and diagnose it

ADJACENT / HIGH-VALUE
→ learn the common idea and relationship now; deepen only when the project actually needs it

DEFERRED
→ acknowledge the concept when useful but avoid a detached course or speculative implementation
```

This learning objective must remain compatible with the anti-rabbit-hole rule: **technology exposure is valuable, but UpgradePilot must not become a technology-demo collection.** Prefer real project use, real code, and real failure/evaluation evidence over adding trendy machinery for its own sake.

AI-assisted implementation is allowed. Depth and ceremony remain adaptive to the real responsibility. The project should reach the next concept as soon as the previous boundary is sufficiently understood and evidenced; do not require perfect mastery or infrastructure completeness before moving forward.
