# Semantic Naming and Execution-Coordinate Decoupling — Working Memory

**Date/time:** 2026-09-05 18:01 Europe/Berlin  
**Session status:** ACTIVE  
**Primary responsibility/mode:** Planning/Design + working-memory support  
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
→ stop before broad migration until the plan is reviewed/continued
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

Consulted the owners/procedures needed for this planning responsibility:

- `AGENTS.md`
- `.agents/skills/upgradepilot-planning-design/SKILL.md`
- `plans/README.md`
- `docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md`
- `MEMORY.md`
- `working-memory/README.md`
- `.agents/skills/upgradepilot-working-memory/SKILL.md`

No product/source implementation work was authorized or performed as part of this planning slice.

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

## 5. Important unresolved decisions

These are intentionally left open for the inventory/analysis rather than decided from preference alone.

1. **Which high-level coordinates remain useful?**  
   `B2` may have legitimate route/navigation value even if deeper labels such as `R4-B2B` do not. Evidence must decide the boundary.

2. **Should coordinates remain in active plan filenames at all?**  
   Candidate rule is semantic filename/title first, with route coordinate only as secondary metadata when useful.

3. **How should ordered plan steps be represented?**  
   Descriptive headings are preferred; ordinary numbering may be used for reading order but should not automatically become durable identifiers.

4. **Which current executable names are genuinely coupled to plan history?**  
   Known examples to inspect include coordinate-bearing experiment/test forms such as `b2_x1_*` and `r4a_*`, but no rename is pre-approved merely from the pattern.

5. **Is compatibility required for renamed importable modules?**  
   Do not create aliases/shims unless an actual supported consumer or migration obligation is demonstrated.

6. **Do current governance files need modification?**  
   Existing rules already cover much of the desired behavior. Any governance change must close a demonstrated gap rather than duplicate accepted wording.

---

## 6. Current session route

The next bounded work, when continued, is:

```text
build the active/reference/historical coordinate inventory
→ classify representative families by real responsibility
→ decide the durable coordinate boundary
→ record those decisions here
→ only then begin selected active-file migration
```

Expected search families include:

```text
B1 / B2
X1
R0...R8
R4-A / R4-B / R4-C / R4-D
A1 / A2 / A3 / A4
R4-B1 / R4-B2A / R4-B2B / R4-B3...
b2_x1 / r4a / r4b identifier and filename forms
```

The inventory must distinguish active owners/executables from historical provenance. It must not become a global replacement list.

---

## 7. Current proof / non-proof

Established now:

- the dedicated branch exists from the recorded main tip;
- the naming/coordinate issue is supported by current governance and representative active vocabulary;
- a bounded consequential migration plan now exists;
- the plan explicitly protects historical provenance and behavior boundaries.

Not established yet:

- the complete set of active files that should be renamed;
- which route coordinates should remain durable;
- whether governance wording requires refinement;
- any source/test/import migration correctness;
- any post-migration link/test/compile proof.

No broad migration should be claimed complete from this planning session.
