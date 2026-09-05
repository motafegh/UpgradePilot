# Semantic Naming and Execution-Coordinate Decoupling Plan

**Status:** AUTHORIZED PLAN ARTIFACT — position-neutral; `MEMORY.md` alone selects live activation  
**Date:** 2026-09-05  
**Responsibility:** remove unnecessary project-specific execution coordinates from the primary identity of active UpgradePilot artifacts and implementation surfaces while preserving useful roadmap navigation, historical provenance, stable semantics, executable integrity, and retrievability.

---

## 1. Why this plan exists

UpgradePilot accumulated several layers of compact planning coordinates:

```text
B2
X1
R4
R4-A / R4-B
A1 / A2 / A3 / A4
R4-B2A / R4-B2B / R4-B3 / ...
```

Some are useful navigation. Others began as local execution labels and gradually became embedded in plan filenames, `MEMORY.md`, learning artifacts, experiment/test filenames, module/class names, working-memory references, proposals, and ordinary project vocabulary.

The resulting problem is not that codes exist. It is that **navigation and execution coordinates became semantic identity**:

```text
semantic opacity
→ understanding an artifact requires historical coordinate knowledge

coordinate leakage
→ temporary execution structure becomes durable implementation/document identity

renumbering pressure
→ planning changes imply unrelated naming changes

vocabulary duplication
→ one responsibility acquires several coordinate aliases

history/live-state coupling
→ local progress vocabulary escapes into artifacts with different owners
```

This plan therefore owns a responsibility/naming migration, not a cosmetic repository rewrite.

---

## 2. Applicable owners and constraints

### Controlling / procedural

- `../AGENTS.md`
- `../OPERATING_GUIDE.md`
- `.agents/skills/upgradepilot-planning-design/SKILL.md`
- `.agents/skills/upgradepilot-build-implement/SKILL.md` when migration execution is authorized
- `README.md`

### Naming / plan ownership

- `../docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md`
- `README.md`
- relevant local README/AGENTS files when a touched directory has one

### Live state / provenance

- `../MEMORY.md` alone owns current live position and continuation
- `../working-memory/README.md` owns dated operational-memory behavior
- Git history and dated working-memory/proposal/learning records preserve historical provenance

The migration must preserve these accepted rules:

1. active names communicate owned responsibility with minimal project-specific decoding;
2. renaming deliberately migrates affected imports, tests, diagnostics, documentation links, and evidence references where applicable;
3. historical records are not mass-rewritten merely to adopt newer vocabulary;
4. plans own bounded sequence/proof/stop conditions, not live progress state;
5. source/tests establish implementation truth;
6. a plan filename does not permanently dictate source architecture.

---

## 3. Established naming and coordinate contract

Repository inventory plus the accepted Naming Clarity standard establish the following distinction.

### Semantic responsibility — primary durable identity

The primary filename/title/name should tell a competent maintainer what the artifact or component owns without requiring historical execution knowledge.

For active plans, use the **complete semantic responsibility**. Prefer explicit wording over project-local shorthand. Longer filenames are acceptable when the additional words materially prevent misunderstanding, misleading scope, or responsibility ambiguity.

### High-level route coordinates — secondary navigation only

The controlling 90-day route gives real semantics to route coordinates such as:

```text
D0 / D1
B1 / B2 / B3 / B4 / B5
X1
C1
```

`B2` and `X1` therefore remain legitimate navigation coordinates. They may appear in the route owner, `MEMORY.md`, or plan metadata when they materially improve orientation.

They should not dominate a plan/module/test/component identity merely because the work happens at that route location.

### Local execution coordinates — plan-local or historical vocabulary

Examples include:

```text
R0 ... R8
R4-A / R4-B / R4-C / R4-D
A1 / A2 / A3 / A4
R4-B2A / R4-B2B / R4-B3 ...
Phase 3B / Phase 4A / ...
```

These may remain useful inside a bounded execution sequence and in historical provenance. They should normally not propagate into durable active filenames, module names, classes, tests, learning-package identity, or ordinary component vocabulary.

### Abbreviation rule for plans

Project-local process abbreviations such as `LBD` must not substitute for the actual responsibility in a plan filename/title. Learning-by-Doing can remain method metadata/content when relevant.

Standard technical product/framework names and widely established technical abbreviations may remain when they are clearer than artificial expansion.

### Plan sequencing rule

Plans may use ordinary numbering for reading order and may preserve locally useful historical step labels, but new sequencing should prefer descriptive responsibility headings such as:

```text
Inventory and classification
Naming-rule decision
Active plan migration
Executable/test migration
Reference reconciliation
Validation and closure
```

Reading-order numbers must not automatically become reusable project vocabulary.

### Active versus historical rule

```text
ACTIVE OWNER / EXECUTABLE
→ migrate when responsibility-first naming materially improves clarity

ACTIVE REFERENCE
→ update when needed to stay correct after owner migration

HISTORICAL / FROZEN PROVENANCE
→ preserve original identity and wording; repair only broken factual paths/links when useful
```

### Compatibility rule

Do not create aliases/shims automatically when executable names change. Add compatibility only when a real supported consumer or migration obligation is demonstrated.

These rules are now owned durably by `UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md` and `plans/README.md`; this plan applies them rather than becoming a competing naming standard.

---

## 4. Scope

### In scope

Inspect and, where justified, migrate active/control surfaces including:

- selected plan filenames, titles, cross-plan links, and route metadata;
- `MEMORY.md` active references after semantic owners exist;
- active experiment/source module filenames and identifiers where execution coordinates became implementation identity;
- active tests whose filenames, identifiers, imports, or diagnostics unnecessarily encode execution coordinates;
- active learning/navigation artifacts where coordinates are primary identity;
- affected READMEs/indexes/documentation/tooling references;
- directly affected historical links only when an active rename would otherwise break retrieval.

### Historical / provenance boundary

Normally preserve unchanged:

- dated working-memory filenames and historical terminology;
- completed/historical proposals;
- frozen learning snapshots;
- old audits and product-simulation evidence;
- Git history and commit messages;
- historical experiment/probe identities whose coordinate is part of provenance.

### Explicitly out of scope unless separately authorized by evidence

- changing product semantics;
- changing planner/agent behavior;
- redesigning LangGraph architecture;
- changing dependency/framework choices;
- broad source refactors unrelated to naming;
- rewriting Git history;
- renaming every artifact containing a letter/number prefix;
- replacing standard technical abbreviations merely because they are abbreviated;
- changing the 90-day route to solve naming aesthetics.

---

## 5. Evidence-backed migration families

### Active plan family

The selected coordinate-heavy plan identities are migrated to responsibility-first names:

```text
B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md
→ BOUNDED_EVIDENCE_GAP_PLANNER_IMPLEMENTATION_COMPARISON_AND_EVALUATION_PLAN.md

B2_X1_R4B_LANGGRAPH_LBD_IMPLEMENTATION_AND_COMPARISON_PLAN.md
→ LANGGRAPH_BOUNDED_EVIDENCE_GAP_PLANNER_INDEPENDENT_DESIGN_IMPLEMENTATION_AND_COMPARISON_PLAN.md

B2_X1_R4_LBD_LEARNING_DEPTH_AND_REENTRY_MAP.md
→ BOUNDED_EVIDENCE_GAP_PLANNER_IMPLEMENTATION_COMPARISON_LEARNING_DEPTH_AND_REENTRY_MAP.md

B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md
→ BOUNDED_PRODUCT_AGENTIC_INVESTIGATION_PLANNER_AND_ORCHESTRATION_EVALUATION_PLAN.md
```

The new names intentionally retain words such as `bounded`, `independent design`, `implementation`, `comparison`, `evaluation`, `learning depth`, and `re-entry` where they materially distinguish the file's responsibility.

`B2 / X1` remains plan metadata/navigation rather than primary filename identity.

### Ordinary-Python evidence-gap implementation family

Current active experiment modules include:

```text
experiments/b2_x1_evidence_gap_planner.py
experiments/b2_x1_evidence_gap_admission.py
experiments/b2_x1_evidence_gap_composition.py
experiments/b2_x1_evidence_gap_model.py
experiments/b2_x1_evidence_gap_transition.py
```

Their semantic responsibilities already exist after the `b2_x1_` prefix. They form one coherent import/reference family and should be migrated together, not independently.

### LangGraph ordinary-Python comparison adapters

Current:

```text
experiments/langgraph/r4a_control_adapters.py
R4APlannerControl
R4AControlPlannerAdapter
R4AControlAuthorityAdapter
```

The real responsibility is adapting the **ordinary-Python control implementation** into LangGraph-owned workflow contracts for comparison. `R4A` is historical execution shorthand rather than durable semantic responsibility.

Exact executable replacement names must be frozen from the import/reference graph before mutation.

### Active tests

The focused tests mirror the executable leakage and should migrate with their owners/imports, including the current evidence-gap and LangGraph/control-adapter test families.

### Historical experiment probes and frozen learning artifacts

E1–E5 probes, dated phase-specific proof files where provenance is their purpose, dated working memories/proposals, and commit-pinned learning packages remain historical unless a concrete active-consumer/link reason requires maintenance.

---

## 6. Execution sequence

### Inventory and classification

Classify material coordinate-bearing surfaces as durable navigation, execution-local, active owner/reference/executable, or historical provenance. Do not use global textual replacement as the classification method.

### Naming-rule decision

Apply the established contract in Section 3. Refine a durable naming owner only when a reusable ambiguity is actually found.

### Active plan and documentation migration

For selected active plans:

- use complete responsibility-first filenames and matching titles;
- keep route coordinates only as secondary metadata where useful;
- preserve responsibility, proof obligations, and stop lines;
- update active cross-references;
- avoid unrelated content rewrites;
- do not mass-rename completed plans.

### Executable and test migration

For each coherent executable family:

```text
identify active import/reference graph
→ freeze semantic owner/module/type names
→ rename owner and active consumers/tests together
→ determine whether compatibility is actually required
→ inspect changed diff
→ run focused validation when runtime is available
```

Do not alter runtime semantics during naming migration.

### Learning and operational-reference reconciliation

Update active learning/index/navigation surfaces that would otherwise teach obsolete execution coordinates as primary identity. Preserve frozen/detailed historical artifacts except for necessary factual path repair.

### Live-memory reconciliation

After active target names are stable:

- replace obsolete active filenames/primary labels in `MEMORY.md`;
- retain deliberate route coordinates only where they still provide real navigation;
- keep live continuation compact;
- do not turn `MEMORY.md` into migration history.

### Validation and closure

Validate:

1. active reference integrity;
2. executable import/test integrity for renamed code;
3. naming recall quality;
4. live-state ownership in `MEMORY.md`;
5. historical preservation;
6. absence of accidental semantic/architecture changes.

---

## 7. Decision record required for each executable family

Before executable mutation, preserve in working memory:

```text
current coordinate-heavy name
→ semantic responsibility
→ classification
→ exact replacement name
→ affected active imports/tests/references
→ compatibility need, if any
→ selected focused validation
```

This prevents mechanical prefix deletion and makes exceptions explicit.

---

## 8. Proof obligations

Cleaner filenames alone are not proof.

Minimum proof should establish:

- selected active plans are understandable by responsibility without nested-coordinate decoding;
- active plan links/references resolve after migration;
- `MEMORY.md` points to the semantic active owners;
- executable imports/tests remain correct where executable names change;
- code/test names no longer unnecessarily depend on plan-sequence labels;
- historical/frozen evidence remains retrievable and accurately historical;
- no mass historical terminology rewrite occurred;
- durable naming owners are sufficient to prevent recurrence.

When local runtime validation is unavailable, state that limitation explicitly; repository inspection does not substitute for executable proof.

---

## 9. Pass condition

This plan passes when:

```text
material coordinate-bearing surfaces are classified
+ durable navigation is distinguished from execution-local vocabulary
+ selected active owners use responsibility-first semantic identity
+ affected executable/reference surfaces are migrated coherently
+ historical provenance is preserved
+ durable naming rules prevent recurrence
+ focused reference/import/test validation is complete within the available environment
+ MEMORY.md points to stable semantic active owners
```

A zero-occurrence search for `B2`, `R4`, `A1`, or similar labels is **not** a pass condition.

---

## 10. Stop lines

Stop and surface the issue rather than continuing mechanically if:

- a coordinate is part of a stable external/public contract;
- renaming would require unrelated behavior/architecture changes;
- active owners disagree on whether a label is durable semantics or execution vocabulary;
- historical material would need substantive rewriting merely to look consistent;
- executable compatibility requirements are unclear;
- migration cost becomes disproportionate to clarity gain;
- the work expands into a general repository cleanup.

Do not:

- globally replace `R`, `A`, `B`, `X`, or numeric patterns;
- assume every `B2` occurrence is invalid;
- retain opaque names merely because they are widely referenced;
- rename historical working-memory/proposal/learning artifacts for cosmetic consistency;
- create compatibility modules "just in case";
- move product responsibilities or change behavior under cover of naming cleanup;
- introduce a new coded hierarchy to remove the old one.

---

## 11. Reassessment trigger

Reassess this plan if evidence shows that the remaining problem is primarily roadmap/document-ownership architecture rather than naming/coordinate leakage. In that case, stop this migration and move the new responsibility to its correct owner rather than forcing this plan to absorb it.
