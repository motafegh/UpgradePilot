# B2/X1 Learning-Only Tiny Mastery Plan

**Artifact lifecycle:** APPROVED compact learning route  
**Broader execution owner:** `B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md`  
**Accepted evaluation protocol:** `B2_X1_PHASE3_EVALUATION_PROTOCOL.md` (`b2-x1-phase3a-v2`)  
**Live-state owner:** `../MEMORY.md`  
**Learning procedure:** `../.agents/skills/upgradepilot-learning-only/SKILL.md`

## 1. Responsibility

Provide the smallest mastery route needed to leave the temporary Learning-Only pause with an accurate mental model of the already-implemented B2/X1 planner boundary, then return learning to the normal Learning-by-Doing/Building loop.

This plan intentionally does **not** replace the broader B2/X1 engineering/evaluation plan or the accepted Phase-3 protocol. Those remain available for later build, replay, protected scoring, baseline comparison, and disposition work.

## 2. Proportionality rule

Learn only what is required to safely understand and continue the implementation already built.

```text
must-master mechanism now
→ understand through real source + focused tests
→ reconstruct the important flow
→ move on

later mechanism that becomes concrete during build
→ learn through Learning-by-Doing when reached
```

Do not turn this pause into a generic LLM/agent course, a memorization gate, or a requirement to master future scoring infrastructure before using the first development smoke.

## 3. Six mastery chunks

### Chunk 1 — proposition and evidence-state foundation

Use real `PropositionAssessment` code and examples to understand:

- proposition identity and ownership;
- `established | refuted | unresolved | conflicted`;
- evidence coverage as a separate dimension;
- why typed epistemic state is planner input instead of raw source prose.

**Exit:** reconstruct one proposition as `key → state → evidence coverage → owner → meaning` and explain why state and coverage are not the same fact.

### Chunk 2 — trusted planner state, action space, and untrusted proposal

Master together:

- `InvestigationSnapshot`;
- `AllowedInvestigationAction`;
- `AgentPlanResult`.

Understand the authority split:

```text
snapshot
→ what deterministic UpgradePilot currently knows

allowed action
→ what deterministic UpgradePilot permits the planner to select

agent plan result
→ what the untrusted model proposes
```

Repository, revision, path, mutation class, action semantics, and result families remain pre-bound trusted state rather than model-created authority.

**Exit:** explain what the model owns and name the important authority it does not own.

### Chunk 3 — structured output, strict parsing, and deterministic semantic admission

Trace:

```text
JSON Schema
→ provider-shaped JSON
→ agent_plan_result_from_mapping(...)
→ AgentPlanResult
→ admit_agent_plan(...)
→ admitted action / admitted no-tool disposition / admission problem
```

Master the distinction:

```text
schema-valid
!= correctly parsed
!= semantically admitted
!= trusted authority
```

Use focused Phase-2 tests for unknown actions, identity/path escape, mutation, repeat, budget, proposition, result-family, and injection-shaped-data boundaries.

**Exit:** diagnose at least one example that is schema-valid but must still be rejected by deterministic admission.

### Chunk 4 — bounded planner states and autonomy

Understand the exact experiment meanings of:

- `choose_action`;
- `stop`;
- `defer`;
- `unresolved`.

Pay particular attention to `stop` versus `defer` versus epistemic `unresolved`, and to the fact that an `AdmittedNoToolDisposition` is safe from capability execution but is not deterministic proof that the planner's reasoning was correct.

**Exit:** classify representative action/no-tool situations and explain where semantic correctness is evaluated.

### Chunk 5 — evaluation case, planning question, oracle, request projection, and leakage

Trace:

```text
PlannerEvaluationCase
├── trusted planning_question
├── trusted snapshot
└── evaluator-only oracle
        ↓
render_planner_request(...)
        ↓
model-facing request only
```

Understand:

- planning question versus answer/oracle;
- evaluator metadata versus planner context;
- `case_key` exclusion;
- context engineering / request projection;
- oracle or label leakage;
- development versus protected evaluation separation.

Use the renderer tests that alter evaluator-only metadata while requiring identical model-facing request bytes.

**Exit:** explain why leaking expected state/action or protected labels would invalidate the evaluation even if the model then performs well.

### Chunk 6 — Phase-4A development smoke and its proof boundary

Trace the already-prepared path:

```text
d-a1-smoke + d-s004-stop
→ render_planner_request(...)
→ build_lmstudio_payload(...)
→ LM Studio local request
→ parse_structured_plan(...)
→ admit_agent_plan(...)
→ DevelopmentSmokeDecision
```

Understand:

- why the first smoke is only two cases × two repeats;
- strict structured output and local transport roles;
- raw model output versus parsed/admitted evidence;
- why semantic model errors remain observable rather than hidden by retries;
- why development smoke evidence is not protected scoring or adoption evidence.

**Exit:** state exactly what a successful four-call smoke can establish and at least three claims it cannot establish.

## 4. Learning-Only exit reconstruction

The pause is complete when the important flow can be reconstructed and reasoned about without needing perfect memorization:

```text
deterministic UpgradePilot evidence
→ PropositionAssessment
→ InvestigationSnapshot
→ trusted closed AllowedInvestigationAction catalog
→ planner-facing request projection
→ untrusted model output
→ structured-output shape
→ strict parsing
→ AgentPlanResult
→ deterministic semantic admission
→ admitted read-only action / no-tool disposition / rejection
```

Ali should be able to answer, in substance:

1. What does the model own?
2. What important authority stays deterministic?
3. Why does JSON Schema not make a planner decision trustworthy?
4. What distinguishes `stop`, `defer`, and `unresolved`?
5. Why must oracle/protected metadata remain outside planner input?
6. What can the development smoke prove and not prove?

This is an understanding/reconstruction gate, not a wording or memorization test.

## 5. Deliberately deferred to Learning-by-Doing

Do not keep Learning-Only open merely to pre-master:

- all protected cases;
- S001 replay implementation details;
- scoring aggregation/manifests/digests;
- full baseline-comparison machinery;
- production-reliability claims from repeated sampling;
- deep LM Studio/runtime internals;
- transformer or quantization internals;
- generic provider abstractions;
- semantic retries;
- prompt/version-management systems;
- caching;
- LLM-as-a-judge;
- MCP or RAG;
- agent frameworks, multi-agent designs, or observability platforms.

Replay, protected scoring, repeated-run interpretation, failure diagnosis, and baseline comparison remain important. Learn them when their real implementation/execution becomes the active Learning-by-Doing responsibility.

## 6. Stop line

When the six chunks and exit reconstruction are sufficiently understood:

```text
Learning-Only mastery pause
→ STOP
→ return to normal Learning-by-Doing/Building on an explicit continue/build request
```

Do not extend this tiny plan simply because another adjacent AI/LLM topic is interesting. Add a topic only if a real understanding gap blocks safe continuation of the current B2/X1 implementation or Ali explicitly chooses to extend the mastery scope.