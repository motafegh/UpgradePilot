# B2/X1 R4-B — First WSL Executable Proof

**Date:** 2026-09-06  
**Session status:** ACTIVE HANDOFF  
**Primary responsibility/mode:** R4-B LangGraph executable proof / Learning-by-Doing + Build/Implement  
**Related architecture/build owner:** `2026-09-04_1904_B2-X1-R4B-architecture-freeze-and-build-entry.md`  
**Related coupling correction:** `2026-09-04_2017_B2-X1-R4B-r4a-representation-coupling-correction.md`  
**Product runtime integration:** not authorized

## 1. What was executed

The corrected native R4-B LangGraph source and its R4-A control adapters were executed in the normal UpgradePilot WSL checkout and project virtual environment.

The first attempted dependency command used `uv`, but the current WSL shell did not have `uv` on PATH. That was an assistant execution-assumption error, not a LangGraph/source failure. The repository environment owner establishes WSL + the project `.venv` + Python as the normal control plane and `pyproject.toml` as dependency authority; it does not establish `uv` as a required installed tool.

The dependency group was then installed successfully through the active project virtual environment using pip support for the `experiments` dependency group declared in `pyproject.toml`.

Focused proof command:

```bash
python -m unittest \
  experiments.tests.test_b2_x1_evidence_gap_langgraph \
  experiments.tests.test_b2_x1_langgraph_r4a_control_adapters \
  -v
```

Observed result:

```text
Ran 7 tests in 0.015s

OK
```

## 2. Tests established green

Native graph behavior:

1. authorized semantic result executes exactly once, consumes the action, spends the bounded budget, and updates the Python-support domain conclusion;
2. expected repository failure spends budget without consuming the action or falsely strengthening domain state;
3. fresh T2 consumed-action state rejects a stale model proposal and preserves the T2 baseline;
4. explicit no-action routes directly to conclusion without authority or repository effect.

R4-A control-adapter mapping:

5. R4-A action decision maps to the R4-B action-proposal representation;
6. R4-A no-action decision maps to the R4-B no-action representation;
7. R4-A provider problem maps to the R4-B provider-problem representation.

## 3. What this proves

This is the first real executable proof, in the normal WSL control plane, that the corrected source can:

```text
import LangGraph
→ build/compile the StateGraph during test setup
→ invoke the graph through the tested routes
→ carry R4-B-owned State/outcomes
→ use Command routing for PLAN/AUTHORIZE paths
→ prevent forbidden repository effects on no-action/rejection paths
→ preserve the fresh T2 authority/consequence baseline
→ distinguish semantic success from expected operational failure
→ translate the reused R4-A planner control outputs behind the adapter boundary
```

The source-level coupling correction therefore survived actual execution for the covered cases.

## 4. What this does NOT prove

The green offline family does not yet establish:

- controlled normalized semantic equivalence between the full R4-A and R4-B implementations across the common comparison projection;
- a real LM Studio planner call through the R4-B graph;
- a real GitHub acquisition through the R4-B graph;
- the real S001 end-to-end LangGraph smoke;
- framework-value superiority or product adoption;
- persistence/HITL/subgraph/parallel/multi-turn value.

## 5. Learning-by-Doing correction retained

The dependency-install failure is classified correctly:

```text
uv command unavailable
→ LangGraph dependency was not installed
→ tests failed at import
!= LangGraph implementation defect
```

The subsequent green run after installing the declared experiment dependency demonstrates why environment/tooling failures must be separated from source/framework failures before changing code.

## 6. Current route

R4-B5 executable proof is complete enough for the current first slice.

```text
CURRENT
→ inspect/record the common R4-A vs R4-B comparison projection and implement/run the smallest controlled semantic comparison evidence (R4-B6)

THEN
→ bounded real S001 LangGraph smoke (R4-B7)
→ framework value/cost findings and R4-D handoff evidence (R4-B8)
→ later R4-C LangChain bounded comparison slice
```

Do not integrate LangGraph into product runtime or expand into speculative framework features before the comparison evidence earns that direction.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`  
`UP-SKILL:upgradepilot-build-implement`
