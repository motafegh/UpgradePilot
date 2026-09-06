# Semantic Executable Naming Migration — Working Memory

**Date/time:** 2026-09-06 16:09 +03:30  
**Session status:** EXECUTABLE NAMING SLICE COMPLETE AT REPOSITORY/STATIC LEVEL  
**Branch:** `refactor/semantic-plan-naming`  
**Controlling migration plan:** `../plans/SEMANTIC_NAMING_AND_EXECUTION_COORDINATE_DECOUPLING_PLAN.md`  
**Primary mode:** Build/Implement naming migration; no runtime/product behavior change authorized

---

## 1. Responsibility

Migrate the current bounded EvidenceGapPlanner experiment/control implementation and its focused proof surface away from route/execution-coordinate primary identity (`b2_x1_*`, `r4a_*`) toward semantic responsibility-first names, while preserving historical executable provenance and the complete existing test surface.

This slice does **not** change planner semantics, LangGraph architecture, dependency versions, product runtime integration, or historical E1–E5 / Phase-3 / Phase-4 artifact identity.

---

## 2. Evidence-backed classification

The current ordinary-Python control family was active implementation, not merely historical provenance:

```text
b2_x1_evidence_gap_planner.py
b2_x1_evidence_gap_admission.py
b2_x1_evidence_gap_composition.py
b2_x1_evidence_gap_model.py
b2_x1_evidence_gap_transition.py
```

The LangGraph comparison bridge likewise used execution-coordinate identity:

```text
langgraph/r4a_control_adapters.py
R4APlannerControl
R4AControlPlannerAdapter
R4AControlAuthorityAdapter
```

Historical/earlier experiment families such as E1–E5 probes, Phase-3/Phase-4 harnesses, and dated S001 proof utilities were **not** mass-renamed.

Three real S001 proof utilities still import the old ordinary-Python module paths. That is a concrete compatibility obligation, so the old current-control paths remain only as narrow re-export bridges rather than duplicate implementations.

---

## 3. Semantic implementation owners

Primary implementation ownership now lives at:

```text
experiments/evidence_gap_planner_model_boundary.py
experiments/evidence_gap_action_admission.py
experiments/evidence_gap_product_planner_composition.py
experiments/local_evidence_gap_planner.py
experiments/evidence_gap_investigation_transition.py
experiments/langgraph/evidence_gap_ordinary_python_control_adapters.py
```

The LangGraph comparison bridge now uses semantic identifiers:

```text
OrdinaryPythonEvidenceGapPlannerControl
OrdinaryPythonEvidenceGapPlannerAdapter
OrdinaryPythonEvidenceGapAuthorityAdapter
```

The old `experiments/b2_x1_evidence_gap_*.py` paths and `experiments/langgraph/r4a_control_adapters.py` are compatibility/provenance bridges only. They must not be treated as the active implementation owners for future work.

---

## 4. Focused test owners

The active focused tests are now named semantically:

```text
experiments/tests/test_evidence_gap_planner_model_boundary.py
experiments/tests/test_evidence_gap_action_admission.py
experiments/tests/test_evidence_gap_product_planner_composition.py
experiments/tests/test_local_evidence_gap_planner.py
experiments/tests/test_evidence_gap_investigation_transition.py
experiments/tests/test_langgraph_evidence_gap_workflow.py
experiments/tests/test_langgraph_evidence_gap_ordinary_python_control_adapters.py
```

The five ordinary-Python focused tests preserve the **exact pre-migration blobs**. This was deliberate after an initial draft shortened two test surfaces: naming cleanup must not silently reduce proof coverage. Those preserved tests currently reach the semantic owners through the compatibility re-export modules.

The two LangGraph-facing tests were migrated directly to the semantic adapter module/classes without reducing their existing scenario coverage.

---

## 5. Commits and correction

Executable migration commit:

```text
a330fab47e7344f27b8bd5b340cd42c00c843188
Migrate evidence-gap experiment modules to semantic names
```

Proof-surface correction commit:

```text
2076118fe0d36f1686f8281f971c91d7b3abb45b
Preserve full test surface across semantic renames
```

The correction is important evidence: semantic naming is subordinate to behavior/proof preservation.

---

## 6. Validation evidence

Repository/static evidence establishes:

- the semantic implementation modules exist;
- old current-control module paths are small compatibility bridges rather than duplicate implementations;
- the seven focused coordinate-named tests were removed and reappear under semantic filenames;
- GitHub recognizes the focused test moves as renames;
- the five ordinary-Python renamed tests have zero-content-diff from their previous blobs;
- the two LangGraph tests have only the intended semantic adapter/import/name changes;
- historical E1–E5 / Phase-3 / Phase-4 tests remain unchanged;
- the branch is ahead of the pre-executable-migration checkpoint by two commits with no unrelated product-source changes.

GitHub combined status for `2076118fe0d36f1686f8281f971c91d7b3abb45b` returned no CI statuses.

Therefore **not established yet**:

- Python import/compile success in the normal WSL environment;
- focused unit-test PASS after the rename;
- LangGraph import/invoke PASS;
- real S001 execution after the rename.

Do not convert repository inspection into runtime proof.

---

## 7. Next migration slice

Next, reconcile active references to these newly stable semantic owners:

```text
MEMORY.md
→ semantic implementation/test paths and adapter terminology

selected active plans / learning companion
→ only concrete active path/name references that now became stale

migration plan / active navigation
→ record compatibility bridges as transitional historical support, not active identity
```

Historical working memories/proposals/frozen learning snapshots remain unchanged unless a broken active path makes a minimal repair necessary.

After active-reference reconciliation, perform another repository-wide bounded audit of the changed naming family before deciding whether another executable family is worth migrating.

`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-working-memory`
