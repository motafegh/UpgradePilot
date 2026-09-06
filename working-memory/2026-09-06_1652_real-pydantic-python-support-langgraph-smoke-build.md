# Real Pydantic Python-Support LangGraph Evidence-Gap Smoke Build

**Date/time:** 2026-09-06 16:52 +03:30  
**Session status:** CONTINUED  
**Primary responsibility/mode:** Build/Implement + Learning-by-Doing  
**Related plan:** `../plans/LANGGRAPH_BOUNDED_EVIDENCE_GAP_PLANNER_INDEPENDENT_DESIGN_IMPLEMENTATION_AND_COMPARISON_PLAN.md`  
**Previous evidence:** `2026-09-06_semantic-naming-main-reconciliation-and-merge.md`  
**Continued by:** `2026-09-06_1752_real-pydantic-python-support-langgraph-executable-proof.md`

## 1. Session anchor

The semantic naming migration was merged and its post-rename executable proof was closed:

```text
8 migrated focused semantic test modules
→ 58/58 PASS in the normal WSL virtual environment
```

The next responsibility was the bounded real LangGraph smoke using the public
`pydantic/pydantic` pull request `#13432`. Product-runtime integration remained unauthorized.

The selected LangGraph plan requires one real graph flow using current product-owned evidence and capabilities and recording:

- the workflow input boundary;
- the model decision;
- deterministic execution authority;
- exact external acquisition;
- final semantic/domain outcome;
- useful framework observability;
- framework friction/benefit;
- proof limits.

## 2. Pre-build model

Use the existing real pydantic dependency-upgrade product path rather than hand-constructing planner facts:

```text
normal investigate_public_pull_request(pydantic/pydantic#13432)
→ real PublicPullRequestInvestigation
→ preserve its pre-target Python-support assessment
→ LangGraph start input
→ real LocalEvidenceGapPlanner through the ordinary-Python comparison adapter
→ current post-planner authority snapshot supplier
→ OrdinaryPythonEvidenceGapAuthorityAdapter as deterministic control oracle
→ GitHubRepositoryClient exact authorized read
→ native LangGraph target interpretation + deterministic conclusion
```

Important control boundary:

```text
reuse established product/domain truth
!=
reuse ordinary-Python architecture as LangGraph state/topology
```

The comparison adapters remain justified because planner/admission semantics are intentionally held constant while orchestration architecture is compared. The native graph still owns workflow state, routing, effect boundary, and final result.

## 3. Environment/security boundary

The smoke crosses two live boundaries:

- WSL → local LM Studio loopback at `127.0.0.1:12345`;
- WSL → public GitHub REST for the pydantic pull request and exact target file.

`ENVIRONMENT.md` and `SECURITY.md` require process-local isolation when ambient GitHub credentials/proxies are not part of the public proof. Do not expose token values or globally disable proxy/VPN configuration.

Execution command:

```bash
env \
  -u GITHUB_TOKEN \
  -u HTTP_PROXY -u HTTPS_PROXY -u ALL_PROXY \
  -u http_proxy -u https_proxy -u all_proxy \
  python -m experiments.real_pydantic_python_support_langgraph_evidence_gap_smoke
```

The local planner transport already uses a requests session with `trust_env=False`, preserving the LM Studio loopback boundary.

## 4. Smoke runner implementation

Semantic source owner:

`../experiments/real_pydantic_python_support_langgraph_evidence_gap_smoke.py`

The runner intentionally lets the normal product investigation complete first. That normal path already performs its own target-Python read. The graph then starts from the preserved pre-target assessment and performs a second exact immutable-head target read through the LangGraph effect boundary.

This gives two useful real checks without duplicating domain semantics:

```text
graph investigation outcome
== normal product target-Python result at the same immutable head

and

graph final Python-support impact assessment
== normal product final impact assessment
```

The smoke also uses LangGraph `stream_mode="updates"` to record the per-node runtime path. Expected action path for the established pydantic case:

```text
plan → authorize → investigate → conclude
```

No persistence, checkpointing, human-approval interruption, subgraph, parallel, or multi-turn machinery was added merely for observability.

## 5. Current post-planner authority boundary

The current experiment has no independent durable/concurrent orchestration state store. The `authority_snapshot_supplier` is invoked only after the planner outcome and re-derives the authority snapshot from:

- the current real `PublicPullRequestInvestigation` object;
- its current product-owned pre-target assessment and investigation selection;
- the current graph turn's consumed-action history and budget.

This preserves the proposal-versus-authority separation and provides the correct seam for future current-state ownership. It does **not** claim concurrent-state freshness beyond what the bounded experiment actually owns.

## 6. Source-level proof boundary at this point

Established by source/owner inspection:

- the smoke uses the real pydantic pull-request investigation rather than a hand-built fixture;
- planner invocation is the real local LM Studio planner seam;
- deterministic authority remains separate from model output;
- the graph performs its own exact GitHub read through the authorized effect boundary;
- semantic comparison uses existing product-owned target/impact results rather than duplicate experiment truth;
- the runner records the LangGraph node-update path without adding persistence machinery;
- the execution command preserves current environment/security rules.

Runtime execution was the next required proof and is preserved in the continued executable-proof record.

`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`
