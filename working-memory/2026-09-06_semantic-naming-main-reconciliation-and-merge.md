# Semantic Naming — Main Reconciliation and Merge Working Memory

**Date:** 2026-09-06  
**Branch:** `refactor/semantic-plan-naming`  
**Responsibility:** reconcile the completed semantic naming migration with the stopped current `main` head, preserve both histories, align newly added active executables, and prepare a safe merge to `main`.

## Main reconciliation

The stopped `main` head was inspected against the naming branch from their common base.

Current main-side divergence contained 14 changed paths. The new work separated cleanly into:

- workstream-supervision governance/Skill/plan/tooling;
- an end-to-end product/engineering proposal plus feasibility evidence;
- dated WSL executable-proof and controlled semantic-comparison working memories;
- one new active semantic-comparison source/test family.

The governance, proposal, tooling, and dated evidence files are already responsibility-based or historical provenance and are preserved byte-for-byte.

The only newly added active executable family requiring naming alignment was:

```text
experiments/b2_x1_r4_semantic_comparison.py
experiments/tests/test_b2_x1_r4_semantic_comparison.py
```

Those coordinate-heavy identities were migrated during reconciliation to:

```text
experiments/evidence_gap_implementation_semantic_comparison.py
experiments/tests/test_evidence_gap_implementation_semantic_comparison.py
```

The comparison vocabulary now uses semantic implementation identities:

```text
ordinary-Python implementation
LangGraph implementation
```

instead of making `R4-A` / `R4-B` the executable API identity. The four controlled scenarios and their assertions remain unchanged in responsibility:

1. no-action semantics;
2. fresh T2 consumed-action rejection;
3. authorized semantic success;
4. expected repository failure.

The comparison source now imports the semantic ordinary-Python owners directly, and the comparison test uses `OrdinaryPythonEvidenceGapAuthorityAdapter` from the semantic LangGraph comparison-adapter module.

## Existing naming migration closure

The final active ordinary-Python transition test was also reconciled to import semantic owners directly. Active focused tests therefore no longer depend on the historical compatibility module paths.

The old `b2_x1_evidence_gap_*` modules and `experiments/langgraph/r4a_control_adapters.py` remain narrow compatibility re-export paths only where preserved historical executable/provenance consumers still need them. They are not active implementation owners.

## Main proof retained without overclaiming

The main-side dated working memories record actual WSL proof before the semantic executable rename:

- native LangGraph graph/adapter focused family: **7/7 PASS**;
- controlled ordinary-Python vs LangGraph semantic comparison: **4/4 PASS**;
- repeated native graph/adapter family after comparison: **7/7 PASS**.

Those results remain valid historical evidence for the pre-rename implementation behavior. They do not, by themselves, establish that the newly renamed/import-reconciled semantic paths execute successfully.

Therefore the merge must not claim post-rename runtime PASS until the migrated focused families execute in the normal WSL control plane.

## Merge disposition

Use a real two-parent merge commit so both lines of development remain in ancestry:

```text
parent 1 = completed semantic naming branch
parent 2 = stopped current main head
```

The merged tree should contain:

- all semantic naming/governance/plan/source/test work from the naming branch;
- all current main-side supervision/proposal/tooling/historical evidence unchanged;
- semantic replacements for the newly added coordinate-heavy comparison source/test;
- reconciled live `MEMORY.md`;
- no unrelated product-runtime change.

After static merge inspection, fast-forward `main` to the merge commit.

## Post-merge proof gate

Before resuming R4-B7 or adding new implementation work, run the migrated focused semantic families in normal WSL. At minimum this must cover:

```text
experiments.tests.test_evidence_gap_planner_model_boundary
experiments.tests.test_evidence_gap_action_admission
experiments.tests.test_evidence_gap_product_planner_composition
experiments.tests.test_local_evidence_gap_planner
experiments.tests.test_evidence_gap_investigation_transition
experiments.tests.test_langgraph_evidence_gap_ordinary_python_control_adapters
experiments.tests.test_langgraph_evidence_gap_workflow
experiments.tests.test_evidence_gap_implementation_semantic_comparison
```

If green, continue the existing product journey from the already-earned next responsibility: bounded real S001 LangGraph smoke. If any failure appears, treat it first as migration evidence and repair only the naming/reference defect unless evidence establishes a real behavior issue.

## Post-merge executable proof — CLOSED

Ali ran the full migrated focused semantic family in the normal active UpgradePilot WSL `.venv` after fast-forwarding local `main` to merge commit `e3416c4d0e390a0d4a56359ac00d36a64eec2334`.

Result:

```text
Ran 58 tests in 0.038s
OK
```

The run covered all eight semantic test modules named by the proof gate and established that the final renamed implementation/test paths import and execute successfully together. In particular, the run re-established the ordinary-Python planner/model boundary, deterministic action admission, product-state composition, local model boundary behavior, investigation transition behavior, LangGraph ordinary-Python control adapters, native LangGraph workflow behavior, and framework-neutral ordinary-Python/LangGraph semantic comparison under the final semantic executable names.

Interpretation:

```text
pre-rename behavioral proof
+ final semantic naming/import migration
+ post-rename 58/58 WSL PASS
→ naming migration executable proof closed
```

This does not add new product semantics or establish LangGraph adoption. It establishes that the semantic naming migration preserved the already-proven bounded behavior and that the active semantic owner paths are executable in the project control plane.

The next experiment responsibility is therefore unblocked: bounded real S001 LangGraph smoke (historical coordinate R4-B7).

## Historical boundary

Do not rename dated working-memory filenames, historical proposals, E1-E5 probes, or recorded old commands merely to make them match current vocabulary. Their old coordinates and paths are part of the evidence they preserve.

`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-working-memory`  
`UP-SKILL:upgradepilot-repository-audit`
