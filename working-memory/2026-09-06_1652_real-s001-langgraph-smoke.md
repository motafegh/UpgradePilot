# Real S001 LangGraph Evidence-Gap Smoke

**Date/time:** 2026-09-06 16:52 +03:30  
**Session status:** ACTIVE  
**Primary responsibility/mode:** Build/Implement + Learning-by-Doing  
**Related plan:** `../plans/LANGGRAPH_BOUNDED_EVIDENCE_GAP_PLANNER_INDEPENDENT_DESIGN_IMPLEMENTATION_AND_COMPARISON_PLAN.md`  
**Previous evidence:** `2026-09-06_semantic-naming-main-reconciliation-and-merge.md`

## 1. Session anchor

The semantic naming migration is merged and its post-rename executable proof is closed:

```text
8 migrated focused semantic test modules
→ 58/58 PASS in the normal WSL .venv
```

The already-earned next responsibility is the bounded real S001 LangGraph smoke (historical route coordinate R4-B7). Product-runtime integration remains unauthorized.

The plan requires one real S001 graph flow using current product-owned evidence/capabilities and recording the workflow input, model decision, deterministic authority result, exact external acquisition, final semantic/domain outcome, relevant framework observability, framework friction/benefit, and proof limit.

## 2. Pre-build model

Use the existing real S001 path rather than hand-constructing planner facts:

```text
normal investigate_public_pull_request(pydantic/pydantic#13432)
→ real PublicPullRequestInvestigation
→ preserve its pre-target Python-support assessment
→ LangGraph EvidenceGapLangGraphStartInput
→ real LocalEvidenceGapPlanner through the ordinary-Python control adapter
→ T2 authority snapshot supplier
→ OrdinaryPythonEvidenceGapAuthorityAdapter as the deterministic control oracle
→ GitHubRepositoryClient exact authorized read
→ native LangGraph target interpretation + deterministic conclusion
```

Important control boundary:

```text
reuse established product/domain truth
!=
reuse ordinary-Python architecture as LangGraph state/topology
```

The existing adapter remains justified here because holding planner/admission semantics constant is part of the framework comparison. The native graph still owns workflow state, routing, effect boundary, and final result.

## 3. Environment/security boundary

The smoke crosses two live external/runtime boundaries:

- WSL → local LM Studio loopback at `127.0.0.1:12345`;
- WSL → public GitHub REST for S001 and the exact target file.

`ENVIRONMENT.md` and `SECURITY.md` require process-local isolation for this public proof when ambient GitHub credentials/proxies are not part of the responsibility. Do not expose token values or globally disable the user's proxy/VPN.

Execution command must therefore use:

```bash
env \
  -u GITHUB_TOKEN \
  -u HTTP_PROXY -u HTTPS_PROXY -u ALL_PROXY \
  -u http_proxy -u https_proxy -u all_proxy \
  python -m experiments.s001_langgraph_evidence_gap_real_flow_smoke
```

The local planner transport already uses a requests session with `trust_env=False`, preserving the LM Studio loopback boundary.

## 4. Smoke runner implementation

Added:

`../experiments/s001_langgraph_evidence_gap_real_flow_smoke.py`

The runner intentionally lets the normal product investigation complete first. That normal path already performs its own target-Python read. The graph then starts from the preserved pre-target assessment and performs a second exact immutable-head target read through the LangGraph effect boundary.

This gives two useful real checks without building duplicate domain semantics:

```text
graph investigation outcome
== normal product target-Python result at the same immutable head

and

graph final Python-support impact assessment
== normal product final impact assessment
```

The smoke also uses LangGraph `stream_mode="updates"` to record the per-node runtime path. Expected action path for the established S001 decision is:

```text
plan → authorize → investigate → conclude
```

No persistence/checkpointer/HITL/subgraph/multi-turn machinery is added merely for observability.

Commits:

- `40df3e1a3548f8c15f345a54319032d86dc76d1e` — initial real S001 LangGraph smoke runner
- `25d9183b5effcde171b70ac0039f50d3b960e7ca` — refine semantic and runtime diagnostics

## 5. T2 currentness boundary

The current experiment has no independent durable/concurrent orchestration state store. The `authority_snapshot_supplier` is invoked only after the planner outcome and re-derives the authority snapshot from:

- the current real `PublicPullRequestInvestigation` object;
- its current product-owned pre-target assessment and investigation selection;
- the current graph turn's consumed-action history and budget.

This preserves the proposal-versus-authority separation and provides the correct seam for future current-state ownership. It does **not** claim concurrent-state freshness beyond what the current bounded experiment actually owns.

## 6. Current proof boundary

Established by source/owner inspection:

- the smoke uses the real S001 product investigation rather than a hand-built fixture;
- planner invocation is the real local LM Studio planner seam;
- deterministic authority remains separate from model output;
- the graph performs its own exact GitHub read through the authorized effect boundary;
- semantic comparison uses existing product-owned target/impact results rather than duplicate experiment truth;
- the runner records the LangGraph node-update path without adding persistence machinery;
- the execution command preserves current environment/security rules.

Not yet established:

- the new runner imports successfully in WSL;
- the current LM Studio model is reachable/usable for the planner call;
- the real public S001 product investigation succeeds in this run;
- LangGraph emits the expected `updates` event shape/path under the installed `langgraph==1.2.11`;
- the model selects `acquire_exact_target_python_declaration` in this real run;
- deterministic authority admits it;
- the exact graph repository read succeeds;
- graph target evidence/final assessment match the normal product path;
- the real S001 LangGraph smoke is green.

## 7. Immediate handoff

Pull current `main` in the normal UpgradePilot WSL `.venv`, then execute the one process-isolated smoke command. Preserve the compact terminal output and the generated `/tmp/upgradepilot-s001-langgraph-evidence-gap-real-flow-smoke.json` only if deeper diagnosis is needed.

Do not treat a single green S001 smoke as product reliability, general planner quality, or LangGraph adoption evidence. If green, record exact evidence and move to LangGraph findings/value-cost evaluation for the later implementation comparison.

`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`
