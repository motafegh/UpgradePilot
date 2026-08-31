# Group 9 — Agent Usage Provenance + Dynamic Routing Refinement Plan

**Status:** AUTHORIZED PLAN ARTIFACT — implementation requires separate user approval  
**Date:** 2026-08-30  
**Branch:** `governance/skill-provenance-secondary-routing-2026-08-30`  
**Base main:** `40ce8af62f339e9d51723011a22b77a372dfd380`  
**Responsibility:** improve observability of actual Agent-Skill use and strengthen secondary/conditional owner discovery without turning UpgradePilot governance into an always-load-everything system

---

## 1. Why this refinement exists

A blind behavioral test was run by giving another AI agent a normal bounded Build request without naming `AGENTS.md`, Skills, governance, `MEMORY.md`, `OPERATING_GUIDE.md`, or expected owner paths.

The observed execution showed a strong primary route:

```text
root repository discovery
→ AGENTS.md
→ MEMORY.md
→ selected active plan
→ Build Skill
→ relevant implementation/tests/evidence
→ Learning-by-Doing Skill
→ bounded implementation + proof-limited handoff
```

Those files materially affected operation selection, implementation location, scope, field-level design, validation claims, continuity updates, and stopping point. This is evidence that UpgradePilot's primary governance discovery/routing is genuinely usable rather than decorative.

The same trace exposed weaker second-hop / conditional routing:

- `OPERATING_GUIDE.md` was repeatedly referenced but not actually opened during substantive work;
- `ENVIRONMENT.md` was not loaded after execution/network topology became materially relevant;
- Build's conditional Source-Clarity reference was not loaded even though the work narrowed semantic/proof-bearing evidence projection;
- the R2 slice contained both Build and meaningful contract-design work, exposing ambiguity around when Planning/Design should compose with Build;
- the agent encountered live-state information incidentally before deliberately opening `AGENTS.md`, but corrected course before acting; this is recorded as low-concern evidence rather than a primary defect.

The working diagnosis is therefore:

```text
primary discovery / routing
→ strong

secondary / conditional owner discovery
→ weaker

behavioral resilience despite some missed canonical owners
→ strong because critical rules are deliberately reinforced
```

This plan addresses the weaker layer without weakening context discipline or creating mandatory governance ceremony.

---

## 2. Goals

The refinement should produce five outcomes:

1. **Skill-use observability** — when a full admitted Skill is actually loaded and materially used, normal execution evidence can expose a stable machine-searchable marker.
2. **Dynamic routing re-evaluation** — when a materially new condition appears during work, the agent re-checks whether a conditional owner/reference has become necessary before continuing.
3. **Clear routing strength** — distinguish required context, conditionally required context, and context that must not be loaded reflexively.
4. **Mixed-operation clarity** — normal local design inside Build does not trigger Skill inflation, while a genuinely new substantive design responsibility does trigger Planning/Design reconsideration.
5. **Regression protection** — the existing agent-governance evaluation system deterministically validates marker structure and behaviorally tests the new routing triggers.

---

## 3. Non-goals / prohibited scope

Do **not**:

- make every task load every governance owner;
- require a working-memory artifact merely to prove Skill use;
- insert governance markers into product source, tests, ordinary comments/docstrings, or unrelated documentation;
- treat a marker as proof that the Skill was followed correctly;
- create a new product specification, ADR, top-level governance framework, telemetry service, tracing dependency, or agent runtime;
- rewrite `PROJECT_CHARTER.md`, product specifications, product source/tests, active product plans, `ENVIRONMENT.md`, or `SECURITY.md` merely because routing to them is being improved;
- force Planning/Design Skill loading for ordinary implementation choices already inside a settled Build responsibility;
- turn conditional routing into a checklist executed after every command/edit.

---

## 4. Design A — Governance execution provenance

### 4.1 Stable Skill marker

Each of the five admitted operation Skills should expose one stable identifier using this form:

```text
UP-SKILL:<canonical-skill-name>
```

Examples:

```text
UP-SKILL:upgradepilot-build-implement
UP-SKILL:upgradepilot-repository-audit
UP-SKILL:upgradepilot-planning-design
UP-SKILL:upgradepilot-learning-by-doing
UP-SKILL:upgradepilot-learning-only
```

Use the Skill's existing canonical name rather than inventing a second identity vocabulary.

### 4.2 Emission rule

When a **full Skill was actually loaded and materially applied**, expose its marker once in the normal completion/handoff evidence when doing so is practical.

Preferred shape:

```text
Governance provenance:
- UP-SKILL:upgradepilot-build-implement
- UP-SKILL:upgradepilot-learning-by-doing
```

If a dated working-memory record is already justified by the task, the same provenance may be preserved there. Do **not** create or expand an artifact only to store the marker.

The marker means:

```text
claimed Skill activation / use
```

It does **not** mean:

```text
correct routing
correct compliance
correct technical result
complete canonical-owner loading
```

Actual trajectory/behavior remains the compliance evidence.

### 4.3 Canonical-owner evidence

Do not create a parallel marker system for every governance file in this first refinement. When material canonical owners/references need to be surfaced, list their exact repository-relative paths in ordinary provenance/handoff text.

Example:

```text
Material owners consulted:
- OPERATING_GUIDE.md
- ENVIRONMENT.md
- .agents/skills/upgradepilot-build-implement/references/source-clarity-heuristics.md
```

Reassess a dedicated `UP-OWNER:*` syntax only if later behavioral evidence shows a real machine-processing need.

---

## 5. Design B — Dynamic conditional-owner routing

### 5.1 Root re-evaluation invariant

Add a compact repository-wide rule near context/operation routing:

```text
When a material new condition appears during execution—changing the relevant owner,
risk, environment/topology, proof obligation, security boundary, or independent
operation responsibility—re-evaluate the conditional context route before continuing.
Do not re-route for ordinary child actions that remain inside the already-established responsibility.
```

This is a **material-boundary checkpoint**, not continuous re-routing.

### 5.2 Routing-strength vocabulary

Use three practical categories where they improve agent actionability:

```text
REQUIRED FOR THIS SUBSTANTIVE PROCEDURE
CONDITIONAL — LOAD WHEN THE TRIGGER APPEARS
DO NOT LOAD REFLEXIVELY
```

Do not duplicate every root rule inside every Skill. Root/`OPERATING_GUIDE.md` own the generic semantics; each Skill should expose only the conditional routes that are materially specific to its procedure.

### 5.3 Core conditional triggers to protect

At minimum, the resulting system should make these transitions hard to miss:

```text
local execution / runtime / topology / local-service / environment failure becomes material
→ consult ENVIRONMENT.md before diagnosing available execution/validation topology

secrets / credentials / private data / untrusted external execution or mutation / transport boundary becomes material
→ consult SECURITY.md

material source change narrows/transforms semantic or proof-bearing evidence, or otherwise meets Build Source-Clarity pressure
→ consult the Build Source-Clarity application reference

accepted stable product semantics/invariants may be changed or relied upon materially
→ consult the applicable canonical specification before reconstructing semantics from working-memory/history

new independent substantive design responsibility appears during Build
→ reconsider Planning/Design procedure
```

### 5.4 `OPERATING_GUIDE.md` canonical loading

The blind test showed that canonical ownership references can be behaviorally bypassed when summaries exist elsewhere. Clarify that substantive operation Skills apply `OPERATING_GUIDE.md` as the canonical project-wide method owner; the agent should consult the relevant sections rather than relying only on repeated summaries when those responsibilities are material.

Preserve proportionality: a tiny lightweight action may remain on the compact root + Operating-Guide route and should not load full Skills unnecessarily.

---

## 6. Mixed Build + Planning/Design boundary

Clarify the distinction explicitly:

### Stay in Build only

Do **not** load Planning/Design merely because implementation requires ordinary local choices such as:

- choosing a small helper boundary;
- deciding a local function signature already inside an accepted contract;
- selecting among implementation details that do not change accepted responsibility/architecture/plan semantics;
- adjusting tests around an already-owned behavior.

### Reconsider / compose Planning/Design

A Planning/Design route becomes warranted when execution reveals a **new substantive unresolved design responsibility**, for example:

- a material contract must be decided rather than merely implemented;
- ownership/layer placement is genuinely unresolved;
- consequential architecture/method alternatives need comparison;
- the selected plan no longer makes implementation unambiguous;
- continuing Build would silently decide another owner's semantics or execution design.

When the user's request already authorizes both planning and implementation, resolve enough design to remove material ambiguity and then continue under Build. Do not make the agent restart the entire session or load both Skills for every implementation micro-decision.

---

## 7. Expected modification surfaces

### Primary governance/procedure files

- `AGENTS.md`
- `OPERATING_GUIDE.md`
- `.agents/skills/upgradepilot-repository-audit/SKILL.md`
- `.agents/skills/upgradepilot-planning-design/SKILL.md`
- `.agents/skills/upgradepilot-build-implement/SKILL.md`
- `.agents/skills/upgradepilot-learning-by-doing/SKILL.md`
- `.agents/skills/upgradepilot-learning-only/SKILL.md`

### Governance evaluation / deterministic protection

- `tools/agent-governance/README.md`
- `tools/agent-governance/governance_doctor.py`
- `tools/agent-governance/build_cases.json`
- `tools/agent-governance/consistency_cases.json` when mixed-operation or cross-owner cases belong there
- other existing operation case banks only when their own routing behavior materially changes

### Conditional Build reference

- `.agents/skills/upgradepilot-build-implement/references/source-clarity-heuristics.md` only if a small clarification is actually required after inspecting the existing reference; do not modify it merely to make the route more visible.

### Normally unchanged

- `PROJECT_CHARTER.md`
- `ENVIRONMENT.md`
- `SECURITY.md`
- active product specifications unless implementation reveals a genuine semantic ownership defect
- product source/tests
- current B2/X1 implementation plan
- `MEMORY.md` unless Ali separately chooses to make this governance branch the live project continuation

---

## 8. Execution sequence after approval

### R9.1 — Freeze exact provenance contract

1. choose exact marker placement inside Skill files;
2. define the completion/handoff emission rule;
3. confirm no repository artifact is created solely for provenance;
4. confirm marker semantics are activation evidence, not compliance proof.

**Pass:** one unambiguous low-noise convention works for all five Skills.

### R9.2 — Root + Operating Guide dynamic-routing refinement

1. add the material-condition re-evaluation rule;
2. make required/conditional/do-not-load distinctions actionable without duplicating every owner rule;
3. preserve smallest-sufficient-context and responsibility-level Skill inheritance.

**Pass:** an agent can tell when to reconsider context while ordinary micro-steps remain lightweight.

### R9.3 — Operation Skill refinements

For each admitted Skill:

1. add its exact provenance marker;
2. ensure `OPERATING_GUIDE.md` relationship is operationally clear;
3. add only the Skill-specific conditional routes that can materially change execution;
4. preserve negative routing / below-materiality rules.

Build receives the deepest refinement for environment, security, Source Clarity, stable-semantics owner, and independent design escalation.

**Pass:** Skills are more actionable without becoming duplicated governance manuals.

### R9.4 — Deterministic governance-doctor protection

Extend objective checks proportionately to verify:

- every admitted Skill has exactly one expected `UP-SKILL:<canonical-name>` marker;
- markers are unique;
- marker name matches the admitted Skill name/directory;
- existing Skill/reference routing targets remain valid;
- new behavioral cases retain valid owner paths.

Do **not** make the doctor judge whether an agent truly used a marker or semantically followed a Skill.

**Pass:** structural drift in the provenance convention fails deterministically.

### R9.5 — Behavioral regression cases

Add/adjust discriminating cases for at least:

1. substantive Build where `OPERATING_GUIDE.md` is expected;
2. execution/network/topology issue arising mid-Build → `ENVIRONMENT.md` becomes expected;
3. equivalent Build without an environment issue → `ENVIRONMENT.md` remains unnecessary;
4. semantic/proof-bearing projection → Source-Clarity reference expected;
5. simple source change → Source-Clarity reference not expected;
6. ordinary local Build design choice → Planning Skill not expected;
7. genuinely new substantive design responsibility during Build → Planning/Design reconsidered/composed;
8. full Skill execution → provenance marker emitted in normal handoff evidence where observable.

Use the existing case-bank model: behavior/trajectory, not exact prose matching.

**Pass:** positive and negative cases protect both discoverability and context restraint.

### R9.6 — Validation + blind re-test

Run, when execution is available:

```text
python tools/agent-governance/governance_doctor.py
```

Then repeat one or more blind behavioral trials without naming governance/Skills in the task prompt.

Compare:

```text
primary routing
secondary/conditional owner loading
unnecessary context loading
provenance marker observability
actual behavioral compliance
```

Do not count marker presence alone as behavioral PASS.

**Pass:** deterministic checks are green and blind trials show improved secondary routing without materially worse context inflation/ceremony.

---

## 9. Evidence standard

Keep three claims separate:

```text
Layer A — deterministic structure
marker/routing paths/case declarations are structurally valid

Layer B — routing observability
agent exposes selected Skills / loads expected conditional owners when inspectable

Layer C — behavior
actual authorization, scope, owner selection, proof discipline, stopping, and output are correct
```

A marker can strengthen Layer B observability. It cannot substitute for Layer C.

---

## 10. Acceptance criteria

This refinement is ready for final branch review when all are true:

1. all five Skills have unique deterministic provenance markers;
2. marker emission is low-noise and does not create artifacts solely for logging;
3. root/Operating Guide clearly require material-condition context re-evaluation;
4. `ENVIRONMENT.md` and `SECURITY.md` conditional routes are harder to miss but still not reflexive;
5. Build Source-Clarity progressive disclosure remains conditional and gains positive/negative regression protection;
6. mixed Build/Design routing is clearer without automatic dual-Skill loading;
7. existing smallest-sufficient-context and responsibility-level Skill inheritance remain intact;
8. governance doctor validates the objective marker/routing structure;
9. behavioral case banks cover both positive and negative versions of the newly clarified routes;
10. at least one blind post-change trial is compared with the recorded pre-change blind-test pattern;
11. no unrelated product/specification/architecture rewrite has been introduced;
12. merge to `main` remains a separate explicit user decision.

---

## 11. Stop line

For the current planning step, stop after this plan and its family-index registration are committed on the dedicated branch.

Do **not** implement the governance/Skill/doctor/case-bank changes until Ali reviews this plan and explicitly says to proceed.

After implementation, stop again for final branch-wide review/validation before any merge to `main`.