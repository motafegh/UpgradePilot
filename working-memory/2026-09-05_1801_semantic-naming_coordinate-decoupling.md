# Semantic Naming and Execution-Coordinate Decoupling — Working Memory

**Date/time:** 2026-09-05 18:01 Europe/Berlin  
**Session status:** ACTIVE  
**Primary responsibility/mode:** Planning/Design + Audit/Review + Build/Implement + working-memory support  
**Branch:** `refactor/semantic-plan-naming`  
**Branch base:** `main` at `0137837ac1fbfcfb6d86678ebe706284bdf4468a`  
**Related plan:** [`../plans/SEMANTIC_NAMING_AND_EXECUTION_COORDINATE_DECOUPLING_PLAN.md`](../plans/SEMANTIC_NAMING_AND_EXECUTION_COORDINATE_DECOUPLING_PLAN.md)

---

## 1. Session anchor

Ali identified a project-wide maintainability problem: planning coordinates such as `R`, `A`, `B`, `X`, nested stage forms, and related abbreviations were repeatedly propagated from plans into code, tests, learning artifacts, working memories, documentation, and normal project vocabulary.

The concern was corrected from "codes are bad" to:

```text
useful navigation coordinates
!=
semantic responsibility identity
```

The migration is intentionally separate from the underlying LangGraph implementation responsibility. `MEMORY.md` remains sole live-state authority.

---

## 2. Evidence-backed classification

Repository inventory established four relevant categories.

### High-level route coordinates

The 90-day route explicitly defines `D0/D1`, `B1-B5`, `X1`, and `C1`. In particular, `B2` and `X1` have genuine route meaning.

**Decision:** keep high-level route coordinates only where they materially aid navigation, normally in the route owner, `MEMORY.md`, or secondary plan metadata.

### Local execution coordinates

Examples:

```text
R0...R8
R4-A / R4-B / R4-C / R4-D
A1 / A2 / A3 / A4
R4-B2A / R4-B2B / R4-B3...
Phase 3B / Phase 4A / ...
```

These describe bounded execution/provenance. No independent product responsibility was found that requires them to become durable component identity.

**Decision:** keep them plan-local/historical when useful; stop propagating them into primary active filenames, module/class/test identity, or unrelated artifact vocabulary.

### Active executable/reference surfaces

Current ordinary-Python evidence-gap modules and LangGraph control adapters/tests contain direct coordinate leakage, including `b2_x1_*` and `r4a_*` forms.

**Decision:** strong next migration candidates, but only as coherent import/reference families after exact semantic replacements are frozen.

### Historical/frozen evidence

E1-E5 probes, dated working memories/proposals, commit-pinned learning packages, and similar records preserve the vocabulary actually used during their historical work.

**Decision:** do not mass-rename. Repair only a factual broken path/link when materially useful.

---

## 3. Naming contract frozen with Ali

Ali accepted the classification and added an explicit preference:

- plan filenames must accurately reflect their actual internal responsibility/context;
- detailed plans may have longer filenames;
- complete descriptive wording is preferred over project-local shorthand/abbreviations when shorthand can cause misunderstanding, misalignment, or misleading scope.

The resulting durable rule is:

```text
semantic responsibility
→ primary durable identity

high-level route coordinate
→ optional secondary navigation metadata

local execution coordinate / process abbreviation
→ plan-local or historical; not a substitute for semantic identity
```

`LBD` is not used as a primary plan filename identity because Learning-by-Doing is an execution/teaching method rather than the technical responsibility owned by those plans.

Standard technical product/framework names remain allowed when they are the clearest normal terminology.

---

## 4. Durable governance refinement completed

The accepted Naming Clarity standard now includes `NAME-013`, requiring active plan filenames/titles to use complete semantic responsibility as their primary identity and explicitly allowing longer filenames when precision prevents ambiguity.

`plans/README.md` now also owns the plan-local application rule:

- semantic responsibility first;
- route coordinates secondary when useful;
- local execution codes/abbreviations do not control filename/title identity;
- full descriptive wording preferred when expansion prevents misunderstanding;
- historical plans are not mass-renamed merely for consistency.

The controlling naming migration plan was reconciled from open naming questions to these established decisions.

---

## 5. Active plan-family migration completed

The selected active plan identities were migrated as follows.

### Bounded evidence-gap planner implementation/comparison/evaluation owner

```text
OLD
plans/B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md

NEW
plans/BOUNDED_EVIDENCE_GAP_PLANNER_IMPLEMENTATION_COMPARISON_AND_EVALUATION_PLAN.md
```

The new title is:

```text
Bounded Evidence-Gap Planner Implementation, Comparison, and Evaluation Plan
```

`B2 / X1` remains secondary route metadata.

### LangGraph bounded implementation/comparison owner

```text
OLD
plans/B2_X1_R4B_LANGGRAPH_LBD_IMPLEMENTATION_AND_COMPARISON_PLAN.md

NEW
plans/LANGGRAPH_BOUNDED_EVIDENCE_GAP_PLANNER_INDEPENDENT_DESIGN_IMPLEMENTATION_AND_COMPARISON_PLAN.md
```

The new title is:

```text
LangGraph Bounded Evidence-Gap Planner Independent Design, Implementation, and Comparison Plan
```

The longer name deliberately preserves `bounded`, `independent design`, `implementation`, and `comparison` because all materially distinguish the responsibility. `B2 / X1` remains route metadata; `R4-B` is retained only as historical execution metadata/content where needed.

### Implementation-comparison learning-depth owner

```text
OLD
plans/B2_X1_R4_LBD_LEARNING_DEPTH_AND_REENTRY_MAP.md

NEW
plans/BOUNDED_EVIDENCE_GAP_PLANNER_IMPLEMENTATION_COMPARISON_LEARNING_DEPTH_AND_REENTRY_MAP.md
```

The new title is:

```text
Bounded Evidence-Gap Planner Implementation Comparison Learning Depth and Re-entry Map
```

### Higher-level agentic planner/orchestration evaluation owner

```text
OLD
plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md

NEW
plans/BOUNDED_PRODUCT_AGENTIC_INVESTIGATION_PLANNER_AND_ORCHESTRATION_EVALUATION_PLAN.md
```

The new title is:

```text
Bounded Product Agentic Investigation Planner and Orchestration Evaluation Plan
```

All four old active filenames were removed after the semantic owners existed and the active references were repointed. They are not retained as duplicate active aliases.

---

## 6. Active-reference reconciliation completed for this plan family

`MEMORY.md` now points to:

```text
plans/BOUNDED_EVIDENCE_GAP_PLANNER_IMPLEMENTATION_COMPARISON_AND_EVALUATION_PLAN.md
plans/LANGGRAPH_BOUNDED_EVIDENCE_GAP_PLANNER_INDEPENDENT_DESIGN_IMPLEMENTATION_AND_COMPARISON_PLAN.md
plans/BOUNDED_EVIDENCE_GAP_PLANNER_IMPLEMENTATION_COMPARISON_LEARNING_DEPTH_AND_REENTRY_MAP.md
```

Its route wording now uses the semantic responsibility alongside the retained `B2/X1` navigation coordinate.

The new parent/LangGraph/learning-depth plan files point to one another through the semantic filenames. Historical proposal and working-memory filenames remain unchanged.

No compatibility alias was created for the deleted plan paths because no supported machine consumer requiring one was established; Git history preserves the old identities.

---

## 7. Scope deliberately not consumed yet

This slice did **not** rename executable code/tests.

Known next-family candidates include:

```text
experiments/b2_x1_evidence_gap_planner.py
experiments/b2_x1_evidence_gap_admission.py
experiments/b2_x1_evidence_gap_composition.py
experiments/b2_x1_evidence_gap_model.py
experiments/b2_x1_evidence_gap_transition.py

experiments/langgraph/r4a_control_adapters.py
R4APlannerControl
R4AControlPlannerAdapter
R4AControlAuthorityAdapter

corresponding focused tests/imports
```

These must be treated as coherent dependency/import families. Exact semantic replacements should be frozen only after tracing active consumers, including older Phase-3/Phase-4/S001 proof utilities that may still import them.

Historical E1-E5 probes, dated working memories/proposals, and frozen learning snapshots remain outside cosmetic migration.

---

## 8. Proof and limits at this stopping point

Established:

- the route-coordinate versus execution-coordinate distinction is evidence-backed;
- the full descriptive plan naming rule is now durable in accepted naming/plan guidance;
- four selected active plan owners have semantic responsibility-first filenames and matching titles;
- active cross-plan references and `MEMORY.md` have been repointed to the semantic owners;
- old active filenames were removed rather than retained as competing aliases;
- high-level `B2 / X1` navigation remains available as secondary metadata;
- historical/frozen artifacts were not mass-rewritten;
- no product/runtime semantics, framework architecture, or dependencies were changed by this plan-name migration.

Not established yet:

- a repository-global guarantee that no historical/unselected text mentions the removed filenames;
- executable module/test naming migration correctness;
- import/test/compile proof for future executable renames;
- whether any older active proof utility requires a compatibility decision during executable migration.

Repository code-search responses for exact old names were incomplete/unreliable, so they are not treated as global proof. Validation for this slice relies on the active owner set, explicit cross-references, `MEMORY.md`, directory/diff inspection, and Git history.

---

## 9. Time-scoped handoff

The plan-name migration slice is complete enough to validate/close before source/test naming begins.

Next bounded responsibility under the naming plan:

```text
trace the active import/reference graph for the ordinary-Python evidence-gap implementation
→ classify older proof/harness consumers
→ freeze complete semantic module/class/test names
→ migrate the coherent executable/test family
→ run focused validation where the normal runtime is available
```

Do not mechanically strip `b2_x1` or `r4a`. Name each executable surface from its real responsibility.

`UP-SKILL:upgradepilot-repository-audit`  
`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-working-memory`
