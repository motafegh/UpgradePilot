# Semantic Naming and Execution-Coordinate Decoupling Plan

**Status:** AUTHORIZED PLAN ARTIFACT — position-neutral; `MEMORY.md` alone selects live activation  
**Date:** 2026-09-05  
**Responsibility:** remove unnecessary project-specific execution coordinates from the primary identity of active UpgradePilot artifacts and implementation surfaces while preserving useful roadmap navigation, historical provenance, stable semantics, executable integrity, and retrievability.

---

## 1. Why this plan exists

UpgradePilot has accumulated several layers of compact planning coordinates such as:

```text
B2
X1
R4
R4-A / R4-B
A1 / A2 / A3 / A4
R4-B2A / R4-B2B / R4-B3 / ...
```

Some of these began as useful route or execution coordinates. Over time, parts of the hierarchy escaped their local planning role and became embedded in plan filenames, headings, `MEMORY.md`, working-memory references, learning artifacts, proposals, experiment/test filenames, module names, adapter names, and ordinary project vocabulary.

That creates several risks:

```text
semantic opacity
→ a reader must remember historical plan coordinates before understanding an artifact

coordinate leakage
→ temporary execution structure becomes durable implementation/document identity

renumbering pressure
→ changing a plan sequence can imply unrelated file/code naming changes

vocabulary duplication
→ one responsibility is referred to by semantic names and several coordinate aliases

history/live-state coupling
→ plan progress labels are repeated across artifacts that should own different responsibilities
```

This plan treats the problem as a responsibility/naming migration, not a repository-wide stylistic cleanup.

---

## 2. Applicable owners and constraints

Use the smallest relevant owner chain for each decision.

### Controlling / procedural

- `../AGENTS.md`
- `../OPERATING_GUIDE.md`
- `.agents/skills/upgradepilot-planning-design/SKILL.md`
- `.agents/skills/upgradepilot-build-implement/SKILL.md` only when execution of the migration is authorized
- `README.md`

### Naming / documentation responsibility

- `../docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md`
- `../docs/README.md` when durable documentation ownership or promotion is affected
- relevant local README/AGENTS files for directories being changed

### Live state / provenance

- `../MEMORY.md` alone owns current live position and continuation
- `../working-memory/README.md` owns dated operational-memory behavior
- Git history and dated working-memory/proposal records preserve historical provenance

### Existing rules that constrain this migration

The migration must preserve these accepted principles:

1. active names should communicate owned responsibility with minimal project-specific decoding;
2. renaming must preserve or deliberately migrate imports, tests, diagnostics, documentation links, and evidence references where applicable;
3. historical records should not be mass-rewritten merely to adopt newer vocabulary;
4. plans own bounded sequence/proof/stop conditions, not live progress state;
5. source/tests establish implementation truth; plans do not dictate permanent source layout merely through historical filenames.

This plan may identify a needed refinement to the naming/governance rules, but it must not duplicate an already sufficient accepted rule merely to make the migration look larger.

---

## 3. Bounded outcome

The responsibility is complete when UpgradePilot has an evidence-backed and consistently applied distinction between:

```text
semantic identity
→ what an artifact/component actually owns or does

navigation coordinate
→ where a responsibility sits in an admitted roadmap/route when that coordinate remains useful

execution-local step label
→ temporary sequencing vocabulary that should normally remain local to its plan/session
```

and the active repository has been migrated so that:

- durable active filenames/titles/module names/test names prefer semantic responsibility over temporary execution coordinates;
- useful high-level roadmap coordinates remain available only where they materially improve navigation;
- local execution coordinates no longer need to propagate through unrelated artifacts;
- active links/imports/references remain valid;
- historical records remain intelligible and are not mass-rewritten;
- current live-state ownership remains concentrated in `MEMORY.md`;
- future plans can use descriptive ordered steps without creating another project-wide coordinate vocabulary.

This outcome does **not** require deleting every occurrence of `B2`, `X1`, `R4`, `A1`, or similar text. Each occurrence must be classified by responsibility before removal or retention.

---

## 4. Scope

### In scope

Inspect and, where justified, migrate active/control surfaces including:

- plan filenames, titles, internal step labels, and cross-plan links;
- `MEMORY.md` references and vocabulary after renamed active owners exist;
- active specifications/ADRs/governance wording only when needed to establish the durable naming/coordinate rule;
- active experiment/source module filenames and identifiers where planning coordinates became implementation identity;
- active tests whose filenames, test classes/functions, fixtures, imports, or diagnostics unnecessarily encode execution coordinates;
- active learning artifacts/maps whose primary identity depends on obsolete execution coordinates;
- active READMEs/indexes and documentation links;
- directly affected tooling or verification references;
- references inside historical records only when needed to repair a broken link or preserve accurate provenance after an active file rename.

### Historical / provenance boundary

Normally preserve unchanged:

- dated working-memory filenames and their historical wording;
- completed/historical proposals;
- old audits and product-simulation evidence;
- Git history;
- historical commit messages;
- historical plan status statements whose purpose is provenance rather than current control.

A historical file may receive a **minimal link/path repair** if an active target is renamed. Do not rewrite its historical terminology merely for uniformity.

### Explicitly out of scope unless evidence creates a separate authorized responsibility

- changing product semantics;
- changing planner/agent behavior;
- redesigning LangGraph architecture;
- changing dependency versions/framework choices;
- broad source refactors unrelated to naming/coordinate coupling;
- rewriting Git history;
- renaming every artifact with any letter/number prefix;
- replacing standard technical abbreviations merely because they are abbreviated;
- changing the 90-day roadmap sequence solely to solve naming aesthetics.

---

## 5. Questions that must be resolved before broad migration

The migration must answer these questions from evidence rather than assumption.

### Roadmap-coordinate boundary

Which high-level coordinates, if any, remain useful durable navigation?

Candidate distinction to test:

```text
high-level roadmap/stage coordinate such as B2
→ may remain as secondary navigation metadata when it materially locates work

local experiment/execution coordinate such as R4-B2B
→ should normally not be the primary durable artifact/component identity
```

Do not freeze this distinction until representative active artifacts are inspected.

### Primary identity rule

Decide whether active artifacts should follow the default form:

```text
semantic responsibility first
+ optional coordinate as secondary metadata/reference only when useful
```

rather than:

```text
coordinate hierarchy first
+ semantic description second
```

### Plan sequencing rule

Decide how plans should express ordered work without recreating the same leakage. Preferred candidates include descriptive ordered headings such as:

```text
Inventory and classification
Naming-rule decision
Active artifact migration
Executable/reference migration
Validation and reconciliation
Closure
```

Numbers may be used for reading order, but should not become durable project vocabulary unless they have an independently useful identity.

### Active-vs-historical migration rule

Define a deterministic classification for:

```text
ACTIVE OWNER / EXECUTABLE
→ migrate when naming clarity materially improves

ACTIVE REFERENCE
→ update when needed to remain correct after owner migration

HISTORICAL PROVENANCE
→ preserve wording/name; repair only broken links or factual path references when necessary
```

### Compatibility rule

For any renamed importable module, public diagnostic, command, or machine-consumed path, determine whether a compatibility bridge is actually required. Do not create aliases/shims by default; use them only when a real supported consumer or migration obligation exists.

---

## 6. Execution sequence

### Inventory and classification

Build a bounded inventory of coordinate-bearing active artifacts and representative historical references.

Search at minimum for the currently recurring families:

```text
B1 / B2
X1
R0...R8
R4-A / R4-B / R4-C / R4-D
A1 / A2 / A3 / A4
R4-B1 / R4-B2A / R4-B2B / R4-B3...
b2_x1 / r4a / r4b filename and identifier forms
```

For each material occurrence classify:

- semantic owner/responsibility;
- active owner, active reference, executable surface, or historical provenance;
- whether the coordinate carries independent navigation value;
- whether the semantic name is already sufficient;
- migration pressure/risk;
- affected links/imports/tests/diagnostics.

Do not edit broadly during inventory.

### Naming-rule decision

Using the inventory and accepted Naming Clarity standard:

1. decide which coordinate levels remain admitted as durable navigation metadata;
2. decide which levels are execution-local and should stop propagating;
3. define the preferred naming form for new plans, working memories, learning artifacts, experiment modules, and tests;
4. determine whether the existing Naming Clarity specification and/or plan guidance already fully owns the rule;
5. update the smallest durable owner only if a reusable rule is genuinely missing or ambiguous.

Record the reasoning in working memory before broad migration.

### Active plan and documentation migration

Migrate active plan/document identities first so downstream references have a stable semantic target.

For each selected rename:

- choose a responsibility-first filename/title;
- preserve the plan's actual responsibility, proof obligations, and stop line;
- remove local progress/status language that improperly competes with `MEMORY.md` when found in reusable active plans;
- update active cross-references;
- avoid rewriting unrelated plan content;
- preserve explicit historical aliases only when they materially aid transition/retrieval.

Do not mass-rename completed plans solely for uniformity.

### Executable and test migration

Where plan coordinates have become executable identity, migrate the smallest coherent dependency set.

Examples to evaluate include:

- experiment module filenames such as coordinate-prefixed `b2_x1_*` forms;
- adapter/module names such as `r4a_*` when the real responsibility can be named directly;
- experiment test filenames and import paths;
- test names/diagnostics that rely on plan codes instead of observable responsibility.

For each executable rename:

```text
identify import/reference graph
→ rename semantic owner
→ update active consumers/tests
→ determine whether compatibility is justified
→ run focused validation
```

Do not change runtime semantics during this migration.

### Learning and operational-reference reconciliation

Update active learning/index/navigation surfaces that would otherwise continue teaching the obsolete coordinate hierarchy as primary vocabulary.

For dated working memory/proposals/audits:

- preserve filenames and historical descriptions;
- update only links/path references made invalid by active renames when useful/necessary;
- do not restate old historical reasoning using new terminology as though that had been the original vocabulary.

### Live-memory reconciliation

Only after the active target names are stable, reconcile `MEMORY.md`:

- replace obsolete active filenames/primary labels with semantic owners;
- retain route coordinates only where they still carry deliberately accepted navigation meaning;
- keep exact current continuation compact;
- do not copy the entire migration history into `MEMORY.md`.

### Validation and closure

Validate the migration at several layers:

1. **Repository reference integrity**
   - no active owner links point to removed names;
   - directly affected historical links remain usable where preservation requires it.

2. **Executable integrity**
   - renamed modules import correctly;
   - focused affected tests/compile checks pass;
   - no compatibility shim exists without a concrete consumer/obligation.

3. **Naming quality**
   - active names pass the recall test;
   - primary identity describes responsibility rather than execution history;
   - one concept does not retain several competing active labels without reason.

4. **Ownership integrity**
   - plans remain position-neutral;
   - `MEMORY.md` alone owns live position;
   - historical working memory remains provenance rather than current authority.

5. **Scope integrity**
   - no product semantic or architectural behavior changed accidentally;
   - no historical mass rewrite occurred.

---

## 7. Migration decision record for each material family

Before modifying a family of related names, record a compact decision in the active working memory:

```text
current coordinate/name
→ real semantic responsibility
→ classification: durable navigation | execution-local | historical provenance
→ keep / rename / demote-to-metadata
→ affected active references
→ compatibility need, if any
→ focused validation
```

This prevents a mechanical global search-and-replace and makes exceptions explicit.

---

## 8. Proof obligations

The migration is not proven by cleaner-looking filenames alone.

Minimum proof should establish:

- representative active plans can be found/understood by responsibility without decoding nested coordinates;
- active plan links resolve after renames;
- active executable imports/tests remain green where names changed;
- code/test names no longer unnecessarily depend on plan sequence labels;
- `MEMORY.md` remains a valid compact owner of current continuation after active owner names change;
- historical evidence remains retrievable and accurately historical;
- no mass historical terminology rewrite occurred;
- the durable naming rule is clear enough that future work will not recreate the same leakage.

When local runtime validation is unavailable, record that limitation explicitly and do not claim executable proof from repository inspection alone.

---

## 9. Pass condition

This plan passes when:

```text
coordinate-bearing repository surfaces are classified
+ durable navigation coordinates are explicitly distinguished from execution-local labels
+ active owners use responsibility-first semantic identity where justified
+ affected executable/reference surfaces are migrated coherently
+ historical provenance is preserved
+ naming/governance owners are sufficient to prevent recurrence
+ focused validation establishes reference/import/test integrity within available environment
+ MEMORY.md is reconciled only after active targets are stable
```

A zero-occurrence search for `B2`, `R4`, `A1`, or similar labels is **not** a pass condition.

---

## 10. Stop lines

Stop and surface the issue rather than continuing mechanically if:

- a coordinate is part of a stable external/public contract rather than internal navigation;
- renaming would require behavior/architecture changes outside this responsibility;
- two active owners disagree on whether a label is durable semantics or temporary execution vocabulary;
- a historical artifact would need substantive rewriting merely to preserve a link;
- executable compatibility requirements are unclear;
- a rename creates disproportionate migration cost without meaningful clarity gain;
- the migration begins expanding into a general repository cleanup.

---

## 11. Prohibited shortcuts

Do not:

- globally replace `R`, `A`, `B`, `X`, or number patterns without classification;
- assume every `B2` occurrence is bad because deeper coordinate leakage is bad;
- retain opaque names merely because they are already referenced widely;
- rename historical working-memory/proposal files for cosmetic consistency;
- create aliases for every renamed module "just in case";
- move product responsibilities or change behavior under cover of naming cleanup;
- make this plan itself the current-state owner;
- introduce a new coded hierarchy to manage the removal of the old coded hierarchy.

---

## 12. Expected artifact/component touch map

The exact list is inventory-driven, but expected categories include:

```text
plans/
→ selected active coordinate-heavy plans and their active references

docs/specifications/ + plans/README.md
→ only if durable prevention rule needs clarification

MEMORY.md
→ final active-reference/live-vocabulary reconciliation

experiments/ + experiments/tests/
→ semantic module/test/import names where coordinate leakage reached executable identity

learning/
→ selected active learning/navigation artifacts where coordinates are primary identity

working-memory/
→ new semantic session record; old dated records normally preserved

proposals/ audits/ product-simulation/
→ normally historical preservation; link repair only when necessary
```

This touch map is a forecast, not authorization to modify every listed area.

---

## 13. Reassessment trigger

Reassess this plan if inventory evidence shows that the issue is not primarily naming/coordinate leakage but instead reflects a deeper unresolved roadmap/document-ownership architecture problem. In that case, stop broad migration and create/adjust the correct design responsibility rather than forcing the current plan to absorb it.
