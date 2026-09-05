# Semantic Naming and Execution-Coordinate Decoupling — Working Memory

**Date/time:** 2026-09-05 18:01 Europe/Berlin  
**Session status:** ACTIVE  
**Primary responsibility/mode:** Planning/Design + Audit/Review + working-memory support  
**Branch:** `refactor/semantic-plan-naming`  
**Branch base:** `main` at `0137837ac1fbfcfb6d86678ebe706284bdf4468a`  
**Related plan:** [`../plans/SEMANTIC_NAMING_AND_EXECUTION_COORDINATE_DECOUPLING_PLAN.md`](../plans/SEMANTIC_NAMING_AND_EXECUTION_COORDINATE_DECOUPLING_PLAN.md)

---

## 1. Session anchor

Ali raised a project-wide maintainability concern: UpgradePilot planning labels such as `R`, `A`, `B`, `X` and nested forms have been repeated through plans and then propagated into code, tests, learning artifacts, working-memory references, documentation, and normal project vocabulary. The concern is not that all route coordinates are inherently invalid; it is that temporary/local execution coordinates have increasingly become durable primary identity.

The immediate responsibility for this session is therefore:

```text
understand the coordinate-leakage problem accurately
→ isolate work on a dedicated branch
→ create one controlling migration plan
→ preserve the reasoning/goals in a new working-memory record
→ inventory and classify the real repository surfaces
→ decide the naming boundary before broad migration
```

This work is intentionally separate from the underlying LangGraph implementation responsibility currently recorded in `MEMORY.md`. This working record does not supersede `MEMORY.md` as live-state authority.

---

## 2. Starting evidence and corrected understanding

Initial inspection established that UpgradePilot currently uses several nested coordinate layers, including representative forms such as:

```text
B2
X1
R4
R4-A / R4-B
A1 / A2 / A3 / A4
R4-B2A / R4-B2B / R4-B3 / ...
```

The important correction is that these labels are not all one category.

Current working classification hypothesis:

```text
roadmap/navigation coordinate
→ may have legitimate durable navigation value

local plan/execution step coordinate
→ useful inside one execution route, but weak as durable artifact identity

historical coordinate
→ provenance that should normally remain unchanged

semantic component/artifact name
→ should communicate the real responsibility directly
```

The main problem appears when the second category escapes its local plan and becomes the primary name of modules, tests, learning artifacts, working memories, or other durable references.

### Governance evidence

`docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md` already requires:

- responsibility-predictive names with little project-specific decoding;
- plan/document titles that state exact responsibility rather than only phase/category;
- deliberate migration of imports/tests/links/evidence when renaming;
- preservation of historical records rather than mass rewriting.

`plans/README.md` also establishes that reusable plans own bounded sequence/proof/stop conditions but **not live progress state**. This matters because some current coordinate vocabulary has become intertwined with active/pass/completed state language and then repeated outside the plan.

The issue therefore looks like a combination of:

```text
naming clarity drift
+ execution-coordinate leakage
+ plan/live-state vocabulary coupling
```

not merely unattractive filenames.

---

## 3. Actions completed in this session

### Dedicated branch

Created:

```text
refactor/semantic-plan-naming
```

from current `main` tip:

```text
0137837ac1fbfcfb6d86678ebe706284bdf4468a
```

The branch name itself deliberately uses semantic responsibility rather than another internal stage code.

### Governance/procedure re-anchor

Consulted the owners/procedures needed for this responsibility:

- `AGENTS.md`
- `.agents/skills/upgradepilot-planning-design/SKILL.md`
- `.agents/skills/upgradepilot-repository-audit/SKILL.md`
- `plans/README.md`
- `docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md`
- `plans/UPGRADEPILOT_90_DAY_PLAN.md`
- `MEMORY.md`
- `working-memory/README.md`
- `.agents/skills/upgradepilot-working-memory/SKILL.md`
- `learning/README.md`

### Controlling plan created

Created:

[`../plans/SEMANTIC_NAMING_AND_EXECUTION_COORDINATE_DECOUPLING_PLAN.md`](../plans/SEMANTIC_NAMING_AND_EXECUTION_COORDINATE_DECOUPLING_PLAN.md)

The plan intentionally does **not** introduce a new coded phase hierarchy. Its execution sequence uses descriptive responsibilities:

```text
Inventory and classification
→ Naming-rule decision
→ Active plan/document migration
→ Executable/test migration
→ Learning/operational-reference reconciliation
→ Live-memory reconciliation
→ Validation and closure
```

---

## 4. Goals preserved for the coming work

The migration should achieve the following without turning into a cosmetic repository rewrite.

### Primary goal

Make semantic responsibility the normal primary identity of active UpgradePilot artifacts/components so a competent maintainer can understand what they own without first decoding execution history.

### Navigation goal

Keep high-level route/roadmap coordinates only where they provide real orientation value. If retained, they should normally act as secondary metadata/navigation rather than dominate the semantic name.

### Plan-design goal

Allow plans to express ordered work without causing every local step label to become a project-wide vocabulary term.

### Executable goal

Where planning coordinates have leaked into module/test/import names, rename the smallest coherent active dependency set while preserving behavior and proving import/test integrity.

### Historical goal

Do not mass-rename or rewrite dated working memories, proposals, audits, simulations, Git history, or other provenance merely to make old records match the new vocabulary. Repair broken active-path links only when needed.

### Governance goal

Determine whether the existing Naming Clarity and plan standards already prohibit the problematic leakage strongly enough. Refine the smallest durable owner only if a real reusable rule is missing or ambiguous.

---

## 5. Inventory and classification findings

### 5.1 Route coordinates have real semantics

The controlling `plans/UPGRADEPILOT_90_DAY_PLAN.md` explicitly defines these route gates:

```text
D0 / D1
B1 / B2 / B3 / B4 / B5
X1
C1
```

In particular:

- `B2` means the **Public PR vertical slice** stage;
- `X1` means the **evidence-gated advanced-method checkpoint**.

`X1` is intentionally non-linear and may be selected from B2–B5 under its recorded activation conditions.

Therefore `B2` and `X1` are not meaningless labels. They carry legitimate project-route navigation semantics.

**Classification:** retain as admitted route coordinates in their route owner and where `MEMORY.md` needs compact live-route location. Do **not** infer from that legitimacy that `B2/X1` belongs in every plan filename, Python module, test, learning artifact, or class name.

### 5.2 Local execution coordinates are a different category

The bounded agentic/planner work introduces several additional sequencing systems:

```text
Phase 3B / Phase 4A / ...
R0 ... R8
R4-A / R4-B / R4-C / R4-D
A1 / A2 / A3 / A4
R4-B2A / R4-B2B / R4-B3 / R4-B4 / R4-B5 / ...
```

These identify **where work happened inside a bounded plan or implementation journey**. They are useful for execution chronology and historical cross-reference, but no independent product/domain responsibility was found that requires these labels to be permanent component identity.

**Classification:** execution-local/provenance coordinates. They may remain inside the plan/history where needed, but should normally stop propagating into durable active filenames, module names, classes, tests, learning-package identity, and ordinary project vocabulary.

### 5.3 Active plan/document surfaces with high migration pressure

The currently selected planner/LangGraph responsibility is controlled/referenced through coordinate-heavy active files including:

```text
plans/B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md
plans/B2_X1_R4B_LANGGRAPH_LBD_IMPLEMENTATION_AND_COMPARISON_PLAN.md
plans/B2_X1_R4_LBD_LEARNING_DEPTH_AND_REENTRY_MAP.md
```

The higher-level checkpoint owner also remains materially relevant:

```text
plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md
```

The semantic parts already communicate most of the real responsibility. `B2_X1_R4B` and similar prefixes mainly encode route/execution history.

**Classification:** active owner/reference — high-priority migration candidates after the exact semantic names are agreed.

Important additional issue: some active reusable plans contain status/progress language such as `R4 active`, `R4-A complete`, or earlier `Phase 3B` live-continuation wording. That is separate from filename quality and should be reconciled proportionately with the accepted rule that `MEMORY.md` alone owns live position.

### 5.4 Unselected/completed plan families are not first-batch rename targets

The root `plans/` directory contains many older plan identities such as:

```text
B2_STEP_1_...
B2_STEP_2_...
...
M2_S01_...
M2_S02_...
D1_...
UPGRADEPILOT_AGENT_SKILLS_GOVERNANCE_STAGE1_...
...
```

Their presence demonstrates that coordinate-first naming has been used repeatedly across the project, but most are not selected live owners for the current responsibility.

**Classification:** do not mass-rename. Treat each as historical/completed provenance unless a later active reference or maintenance need proves otherwise. The current migration should not become a cleanup campaign over every old plan filename.

### 5.5 Current ordinary-Python control implementation has direct coordinate leakage

The current EvidenceGapPlanner ordinary-Python reference/control is split across active experiment modules including:

```text
experiments/b2_x1_evidence_gap_planner.py
experiments/b2_x1_evidence_gap_admission.py
experiments/b2_x1_evidence_gap_composition.py
experiments/b2_x1_evidence_gap_model.py
experiments/b2_x1_evidence_gap_transition.py
```

These names already contain meaningful semantic responsibilities after the prefix. Their imports also directly reference one another through the `b2_x1_...` paths.

Representative source wording confirms that the modules themselves describe their responsibilities as planner boundary, deterministic action admission, product-to-planner composition, local model interaction, and bounded state transition. `B2/X1`, `R4-A1`, `R4-A2`, etc. are explanatory/provenance labels rather than the domain responsibility itself.

**Classification:** active executable family — strong migration candidate. Because the files import one another and are imported by current LangGraph control adapters/tests, they must be migrated as one coherent import/reference slice rather than renamed independently.

### 5.6 LangGraph control bridge contains a particularly clear local-code leak

Current file:

```text
experiments/langgraph/r4a_control_adapters.py
```

contains identifiers including:

```text
R4APlannerControl
R4AControlPlannerAdapter
R4AControlAuthorityAdapter
```

The source itself defines their real responsibility more directly: they adapt the already-proven **ordinary-Python control implementation** into the independently owned LangGraph workflow contracts for comparison.

That means `R4A` is functioning as shorthand for an implementation role that can be named semantically.

**Classification:** active executable — very high-confidence coordinate-leakage candidate. A semantic form such as `ordinary_python_control_*` is more recoverable than `R4A*`; exact replacement names remain to be frozen before editing.

### 5.7 Active tests mirror the same leakage

The focused experiment tests include current names such as:

```text
experiments/tests/test_b2_x1_evidence_gap_admission.py
experiments/tests/test_b2_x1_evidence_gap_composition.py
experiments/tests/test_b2_x1_evidence_gap_model.py
experiments/tests/test_b2_x1_evidence_gap_planner.py
experiments/tests/test_b2_x1_evidence_gap_transition.py
experiments/tests/test_b2_x1_evidence_gap_langgraph.py
experiments/tests/test_b2_x1_langgraph_r4a_control_adapters.py
```

The LangGraph test content confirms that `R4-B` and `R4-A` describe comparison provenance while the observable responsibilities are the native LangGraph EvidenceGapPlanner workflow and the ordinary-Python control adapter boundary.

**Classification:** active proof surface — migrate together with the corresponding executable owners/imports. Test names/diagnostics should describe observable behavior/responsibility rather than plan coordinates where practical.

### 5.8 Older E1–E5 probes are provenance, not the same as active control modules

Files such as:

```text
experiments/b2_x1_e1_support_drop_semantic_probe.py
experiments/b2_x1_e2_s001_state_origin_probe.py
experiments/b2_x1_e3_minimal_s001_planner_probe.py
experiments/b2_x1_e4_closed_action_binding_probe.py
experiments/b2_x1_e4_deterministic_admission_probe.py
experiments/b2_x1_e4_json_schema_binding_probe.py
experiments/b2_x1_e5_no_tool_disposition_probe.py
```

record successive research/probe steps whose coordinate identity is part of how the experiment history is reconstructed.

**Classification:** historical experiment provenance — leave unchanged unless a concrete broken-reference/maintenance reason appears.

The same caution applies to older files such as `b2_x1_phase3b_harness.py`, `b2_x1_phase4a_planner_smoke.py`, and `b2_x1_s001_real_flow_a3/a4...`: they require an import/continued-use check before deciding whether they are still active executable owners or primarily historical proof machinery. Do not classify them from filename alone.

### 5.9 Frozen learning snapshots must be preserved

`learning/README.md` explicitly says commit-pinned learning snapshots are frozen educational records and should not be silently rewritten when implementation changes.

The package:

```text
learning/2026-09-01-b2-x1-r4-evidence-gap-planner/
```

contains coordinate-heavy study-note names such as:

```text
01_A1_A3_OWNERSHIP_STUDY_NOTE.md
02_REAL_FLOW_COMPOSITION_AND_LIVE_A3_STUDY_NOTE.md
```

but the learning index identifies this package as a commit-pinned snapshot.

**Classification:** historical/frozen learning evidence — preserve its identity/wording unless a factual error or broken reference requires correction.

This is different from the current active learning-depth/reentry **plan**, which remains an active migration candidate.

### 5.10 Dated working memories and proposals remain historical

Dated working-memory/proposal filenames containing `B2-X1-R4A/R4B/...` record the actual terminology used during those sessions. Their coordinate vocabulary is historical evidence, not an active naming contract.

**Classification:** preserve filenames and historical wording. If an active plan/module is renamed, update a historical file only when a direct path/link becomes broken and the repair materially helps retrieval; do not rewrite its narrative terminology.

---

## 6. Evidence-backed naming boundary recommendation

The inventory now supports this stronger default rule:

```text
SEMANTIC RESPONSIBILITY
→ primary durable identity

ROUTE COORDINATE (D0/D1/B1-B5/X1/C1)
→ allowed as secondary navigation metadata where useful

LOCAL EXECUTION COORDINATE (R*, A*, Phase*, nested variants)
→ keep local to execution/provenance; do not propagate as durable identity
```

Practical consequences if accepted:

1. `MEMORY.md` may still say the live route is `B2 / X1` because that is genuine compact route location.
2. An active bounded plan should normally be named from the responsibility, not `B2_X1_R4B_...`.
3. `R4-A` should be described semantically as the ordinary-Python reference/control implementation when durable identity is needed.
4. `R4-B` should be described semantically as the LangGraph implementation/comparison when durable identity is needed.
5. `A1/A2/A3/A4` can remain useful historical/plan-local shorthand, but active source/test identities should name planner projection, model invocation, deterministic authority/admission, transition/consequence, etc. directly.
6. Ordinary numbering in a plan can express reading/execution order without creating reusable project codes.
7. Frozen historical records continue to use the vocabulary they actually used at the time.

This rule is consistent with the existing Naming Clarity standard; the inventory has not yet demonstrated that a new specification is required. A small clarification to plan/naming guidance may still be justified later if the migration exposes ambiguity about route metadata versus execution-local labels.

---

## 7. Candidate first migration boundary

If Ali accepts the recommendation above, the safest first implementation slice is **not** every coordinate-bearing file. Use this order:

```text
A. freeze semantic names for the active plan family
→ rename the selected active plan owners/references
→ repair active links

B. freeze semantic names for the ordinary-Python control implementation role
→ rename the active b2_x1 evidence-gap module family as one coherent dependency set
→ rename r4a control-adapter file/classes semantically
→ migrate focused active tests/imports
→ validate

C. reconcile active learning-depth/navigation references
→ preserve frozen learning snapshots

D. reconcile MEMORY.md after target names are stable

E. inspect remaining coordinate-bearing active references
→ leave historical/unselected surfaces alone unless evidence requires maintenance
```

Before B, trace the import/reference graph for the older Phase-3/Phase-4/S001 proof files so we know whether any of them are still active consumers. Do not create compatibility modules by default; experiments are repository-internal unless a real supported consumer is demonstrated.

---

## 8. Exact semantic names intentionally not frozen yet

The inventory supports removing coordinate-first identity, but several exact replacements should be decided deliberately rather than by mechanical prefix deletion.

Examples to decide:

```text
B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md
→ likely responsibility-first EvidenceGapPlanner implementation/evaluation name

B2_X1_R4B_LANGGRAPH_LBD_IMPLEMENTATION_AND_COMPARISON_PLAN.md
→ likely LangGraph EvidenceGapPlanner/workflow implementation + comparison name

B2_X1_R4_LBD_LEARNING_DEPTH_AND_REENTRY_MAP.md
→ likely EvidenceGapPlanner learning-depth/reentry name

r4a_control_adapters.py / R4AControlPlannerAdapter / R4AControlAuthorityAdapter
→ likely ordinary-Python control adapter terminology
```

`Learning-by-Doing` is the project execution/teaching method rather than the plan's core technical responsibility, so `LBD` probably does not need to dominate filenames even when the plan explicitly follows that method.

Likewise, route coordinates can be retained inside plan metadata/header fields when they help orientation without controlling filename identity.

---

## 9. Current session route

Inventory/classification is complete enough for the first naming-boundary decision.

Current decision point:

```text
review/accept/refine the boundary:
semantic identity first
+ route coordinates only as secondary navigation
+ local execution coordinates confined to plan/history

→ freeze exact names for the active plan family
→ migrate active plan owners/references first
→ preserve historical/frozen artifacts
→ then trace and migrate the coherent executable/test family
```

Do not begin broad file renaming until the exact active-plan naming scheme is settled.

---

## 10. Current proof / non-proof

Established now:

- the dedicated branch exists from the recorded main tip;
- the coordinate problem is present across active plans, executable experiments, tests, active references, and frozen historical/learning artifacts;
- `B2` and `X1` have real route semantics in the controlling route plan;
- deeper `R*`, `A*`, `Phase*`, and nested labels are local execution/provenance vocabulary rather than demonstrated product responsibility;
- current ordinary-Python EvidenceGapPlanner modules/tests and LangGraph control adapters contain direct coordinate leakage;
- older E1–E5 experiments and commit-pinned learning packages have a different historical/provenance role and should not be mass-renamed;
- a responsibility-first naming boundary is supported by both repository evidence and the accepted Naming Clarity standard.

Not established yet:

- the exact replacement filenames/titles for the active plan family;
- the exact replacement module/class names for the ordinary-Python control and adapter surfaces;
- the full import graph of older Phase-3/Phase-4/S001 experiment utilities;
- whether a tiny governance clarification is required after migration;
- source/test/import correctness after migration;
- post-migration link/test/compile proof.

No broad migration is claimed complete yet.
