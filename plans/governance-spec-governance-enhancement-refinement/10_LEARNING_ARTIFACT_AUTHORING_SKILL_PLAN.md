# Group 10 — Learning-Artifact Authoring Skill Plan

**Plan status:** PROPOSED / planning-only  
**Branch:** `governance/learning-artifact-skill-2026-09-01`  
**Branch base:** `958b4b73d5c8fc011f1150258b9e9a73b1f51151`  
**Implementation authorization:** NOT GRANTED by this plan

## 1. Responsibility

Design and, only after separate authorization, implement one compact reusable Agent Skill for **authoring UpgradePilot learning artifacts that Ali can study or relearn later**.

This is distinct from:

- Learning-by-Doing, where learning accompanies real project work;
- Learning-Only, where Ali and the assistant actively study/master material in the current session;
- Working-Memory, which preserves detailed dated operational/session history;
- Audit, which evaluates repository quality/correctness as the primary responsibility.

The target workflow is:

```text
Ali asks for durable study material about real UpgradePilot material
→ inspect current truth + directly relevant history/evidence
→ pressure-test the material rather than rationalizing it
→ choose the smallest useful learning artifact/package
→ teach through real UpgradePilot responsibilities/cases/flows
→ calibrate depth intelligently
→ produce a reusable study/relearning artifact under learning/
```

The likely Skill identity is:

```text
upgradepilot-learning-artifact
```

Final naming may be refined during implementation only if a clearer responsibility-bearing name is demonstrated.

## 2. Why a dedicated Skill is justified

This is a frequent repeatable artifact-production workflow with judgment that is not fully owned by Learning-Only or Learning-by-Doing:

- what evidence must be inspected before writing;
- when related working-memory history is required;
- how to distinguish current truth from historical rationale;
- how to detect and surface questionable implementation instead of inventing a justification;
- when bounded Audit composition is necessary;
- how to prefer real product-simulation/user/data/control flows over detached toy examples;
- how much syntax/library/concept depth belongs in the artifact;
- when to create one focused note versus a small ordered package;
- how to keep notes neither superficial nor exhaustively long;
- how to make the result useful for later relearning.

`learning/README.md` remains the semantic/artifact owner. The new Skill must apply it rather than become a second learning specification.

## 3. Canonical owners to preserve

The implementation must preserve these boundaries:

- `AGENTS.md` — authorization, root routing, artifact responsibility;
- `OPERATING_GUIDE.md` — project-wide learning/ownership/depth/evidence principles;
- `learning/README.md` — learning-artifact meaning, snapshot policy, placement, maintenance;
- `.agents/skills/upgradepilot-learning-only/SKILL.md` — interactive standalone mastery sessions;
- `.agents/skills/upgradepilot-learning-by-doing/SKILL.md` — learning composition during real project work;
- `.agents/skills/upgradepilot-repository-audit/SKILL.md` — materially evaluative audit procedure;
- `.agents/skills/upgradepilot-working-memory/SKILL.md` and `working-memory/README.md` — detailed session/history evidence and retrieval;
- specifications / ADRs / plans — their accepted semantics/method/execution responsibilities;
- active source/tests/commands/evidence — implementation truth;
- `MEMORY.md` — live project continuation only.

The Learning-Artifact Skill is procedural and non-controlling.

## 4. Core design principles

### 4.1 Artifact-first, not active-teaching-first

The primary deliverable is reusable study material. The Skill must not require an interactive lesson, quiz loop, learner response, or mastery demonstration merely to author the artifact.

Interactive study remains Learning-Only when selected later.

### 4.2 Current truth plus relevant history

Before teaching a material code/design/plan responsibility, use the smallest sufficient evidence route:

```text
current canonical owner(s)
→ current source/tests/evidence
→ directly relevant working-memory/history when it explains implementation path, errors, decisions, fixes, or deferred alternatives
→ representative real case / product-simulation evidence when available
→ learning artifact
```

Do not scan all historical working-memory. Search/load only records materially connected to the selected responsibility or clues.

Working-memory may explain **how/why a path was reached**; it does not override current source, accepted owners, or newer evidence.

### 4.3 Never invent rationale for questionable material

The Skill must distinguish:

```text
WHAT THE PROJECT DOES
WHY THE EVIDENCE SHOWS THAT
WHY IT WAS DESIGNED THAT WAY, when evidenced
WHETHER THE DESIGN/IMPLEMENTATION IS GOOD
WHAT CREDIBLE ALTERNATIVES OR IMPROVEMENTS EXIST
```

If current material appears defective, stale, contradictory, unnecessary, misleading, or otherwise questionable:

1. do not fabricate a rationale;
2. inspect the directly relevant owners/tests/history proportionately;
3. compose the Repository-Audit procedure when the question becomes materially evaluative;
4. classify the result honestly, for example:
   - intentional/currently justified;
   - known defect with current fix;
   - defect/stale behavior;
   - questionable trade-off;
   - improvement opportunity;
   - unresolved / insufficient evidence;
5. teach the issue, fix, alternatives, and proof limits when useful to learning.

Learning-artifact authoring itself does **not** authorize fixing product source/tests. Any implementation repair requires a separately authorized Build responsibility.

### 4.4 Real UpgradePilot examples are the default

Prefer:

- real product-simulation cases;
- real user/data/control/evidence flows;
- actual source objects/functions/types;
- real failure/debugging incidents;
- real focused tests and proof boundaries;
- actual plan/design decisions.

Toy examples are allowed only as a small explanatory microscope when isolating syntax/API behavior materially improves understanding, and should reconnect immediately to the real UpgradePilot mechanism.

Do not build detached generic tutorials when the repository already contains a real teaching substrate.

### 4.5 Engineering ownership, not memorization

Use the existing project-wide depth/ownership doctrine rather than inventing a competing taxonomy.

For each subject, distinguish proportionately:

```text
MUST OWN / MASTER
→ central engineering responsibility and decisions

OPERATIONAL UNDERSTANDING
→ needed to read, reason, modify, debug, review, or safely use the mechanism

RECOGNIZE / LOOK UP
→ incidental syntax/library/API construct whose role must be understood but internals are not a prerequisite

DEFER
→ deeper detail not currently useful unless a real trigger appears
```

Learning artifacts must help Ali own engineering responsibility without demanding unaided source reproduction from memory.

### 4.6 Minimum sufficient study artifact

Avoid both failure modes:

```text
superficial summary
→ too little mechanism/context to learn from

exhaustive tutorial/document dump
→ too long to study or revisit
```

Target the **smallest complete study artifact** that gives an accurate mental model, real flow, important boundaries/failures, relevant mechanisms, proof/non-proof, and practical relearning path.

## 5. Supported artifact shapes

The Skill must adapt to the learning subject instead of forcing one universal template.

### Source/code responsibility

Emphasize as relevant:

```text
responsibility / non-responsibility
→ inputs/state/types
→ important normal data/control flow
→ important failure/problem paths
→ trust/authority boundaries
→ syntax/library/API mechanisms worth knowing
→ why material mechanisms exist
→ tests/proof/non-proof
→ real representative case
```

### Plan

Emphasize:

```text
problem / outcome
→ scope/exclusions
→ sequence/responsibility decomposition
→ dependencies / gates
→ material decisions and rationale
→ proof obligations
→ stop lines / deferred scope
```

### Architecture/design/ADR

Emphasize:

```text
problem pressure
→ accepted requirement constraints
→ alternatives when genuinely relevant
→ selected ownership/structure
→ trade-offs
→ failure modes
→ implementation consequences
```

### Concept / syntax / API / tool

Emphasize:

```text
term / mechanism
→ practical meaning
→ why it exists
→ exact role in UpgradePilot
→ nearby concepts and distinctions
→ current required depth
→ lookup/deferred internals
```

### Cross-file / end-to-end flow

Prefer one representative real case and trace producer → transformations → trust/decision boundaries → consumer/proof.

## 6. Default artifact quality features

Use only what adds value; do not turn these into a mandatory form.

Strong learning artifacts should normally make recoverable:

- purpose and source/snapshot identity;
- big-picture mental model;
- responsibility boundaries;
- one or more real UpgradePilot flows/cases;
- important failure/problem paths;
- important concepts/syntax/APIs at calibrated depth;
- rationale versus current fact versus engineering judgment;
- tests/evidence and explicit non-claims;
- known issues/fixes/improvement alternatives when material;
- source/plan/design/history anchors;
- a short **fast relearning route**;
- a few ownership/transfer prompts when they materially improve later study.

The fast relearning route should let Ali return weeks later without rereading the whole artifact first, for example:

```text
recall the core mental model
→ open 1–3 exact source/plan locations
→ trace one representative real flow
→ inspect one or two proof anchors
→ answer a few ownership questions
```

## 7. One note versus a package

Prefer **one focused artifact** when one coherent learning responsibility can be taught usefully in one note.

Use a **small ordered package** only when several learning responsibilities are genuinely distinct enough that one document would become hard to study/revisit.

Do not create a package, index, contract, depth map, learning memory, or multiple files merely for symmetry or professionalism.

Existing package-local structures remain valid where already justified; the new Skill must not impose one package layout repository-wide.

## 8. Snapshot and freshness behavior

Preserve the existing `learning/README.md` snapshot model:

- current code-bearing learning material should identify the relevant source/test revision or otherwise clearly state the artifact's evidence horizon;
- material later implementation changes do not silently rewrite a historical snapshot;
- factual errors, unsafe instructions, or broken references may be corrected explicitly;
- when a fresh learning artifact is requested for materially changed behavior, use current source/evidence and create/update the correct current artifact according to the README rather than pretending an old snapshot is current.

The Skill must never use a learning artifact as live project-state authority.

## 9. Relationship to other Skills

### Learning-Artifact + Learning-Only

The artifact Skill authors/revises study material. Learning-Only runs the active mastery session. They may compose when Ali explicitly asks to both create material and study it, but neither should be loaded reflexively merely because the other exists.

### Learning-Artifact + Learning-by-Doing

Learning-by-Doing may produce a justified reusable artifact after/beside real project work. The authoring Skill governs artifact construction when the artifact itself becomes a material deliverable.

### Learning-Artifact + Working-Memory

Working-Memory is an evidence/history input when directly relevant; it is not copied wholesale into learning notes. The learning artifact extracts reusable understanding and preserves links/provenance.

### Learning-Artifact + Audit

If authoring exposes a material correctness/necessity/ownership/design problem, compose Audit for the evaluative responsibility. Record/teach the evidence-bounded result; do not silently mutate product code.

### Learning-Artifact + Build

Build is not activated by discovering a problem. Source/test repair requires separate authorization.

## 10. External structural inspiration

During design, review a small number of public learning/teaching Agent Skills for structural ideas only. Current useful inspiration includes Matt Pocock's `teach` Skill, especially:

- evidence/trusted-resource grounding;
- small coherent learning units;
- durable quick-reference/relearning material;
- purpose-driven depth;
- separation of teaching state from reusable learning artifacts.

Do not copy its long-running lesson/workspace/HTML/quiz machinery unless a concrete UpgradePilot responsibility later justifies it.

External Skills are inspiration/evidence, not UpgradePilot authority.

## 11. Planned repository changes after approval

Expected bounded implementation surface:

1. `learning/README.md`
   - small refinement recognizing AI-authored learning/relearning artifacts as a first-class use;
   - strengthen evidence/history/audit/real-case authoring principles only where genuine gaps exist;
   - preserve existing snapshot/depth/authority rules.

2. `.agents/skills/upgradepilot-learning-artifact/SKILL.md`
   - create compact support/artifact-authoring procedure;
   - stable provenance marker `UP-SKILL:upgradepilot-learning-artifact`;
   - not a new primary operation mode.

3. `AGENTS.md`
   - minimal discoverability/routing alignment if required so natural-language requests such as "write learning notes for this code/plan/design" can find the support Skill without turning it into a primary operation.

4. `OPERATING_GUIDE.md`
   - only a concise reinforcement/reference if the new procedure needs a project-wide connection not already clear.

5. Existing Learning-Only / Learning-by-Doing / Audit / Working-Memory Skills
   - modify only where a short composition pointer is genuinely needed;
   - do not duplicate the new procedure.

6. `tools/agent-governance/governance_doctor.py` and/or behavioral case banks
   - update only what is required for the new admitted support Skill to be structurally discoverable and regression-protected;
   - preserve the distinction between five primary operation Skills and support/composition Skills.

7. This plan-family `README.md`
   - index Group 10 and its dependency/stop boundary.

No product source/tests/experiments, `MEMORY.md`, working-memory records, specifications, or ADRs should change merely to introduce this Skill.

## 12. Implementation sequence after separate authorization

### Phase A — gap trace and exact ownership map

Inspect the latest versions of:

- `learning/README.md`;
- `OPERATING_GUIDE.md` relevant learning/depth/evidence sections;
- Learning-Only, Learning-by-Doing, Audit, Working-Memory Skills;
- relevant governance-doctor Skill assumptions/case banks;
- several representative learning artifacts, especially newer compact R4 notes plus at least one older large artifact.

Produce an internal gap map:

```text
already owned adequately
→ reference only

genuine semantic gap
→ learning/README.md

genuine reusable procedure
→ new Skill

cross-skill routing gap
→ minimal pointer/reinforcement
```

Do not rewrite existing rules simply to make the new Skill self-contained.

### Phase B — finalize Skill responsibility and boundaries

Confirm:

- final Skill name/description;
- activation phrases/use cases;
- support/composition classification;
- write boundary limited to authorized learning artifacts/governance alignment;
- Audit escalation behavior;
- current-truth + relevant-history evidence route;
- real-case preference;
- artifact size/depth/proportionality rules.

### Phase C — refine canonical learning-artifact owner

Make the smallest `learning/README.md` changes needed to explicitly support:

- AI-authored study/relearning artifacts requested independently of active teaching;
- directly relevant working-memory/history as rationale/context evidence;
- current truth outranking historical rationale;
- no invented justification for questionable implementation;
- real UpgradePilot cases/flows as default teaching substrate;
- adaptive artifact shape and minimum-sufficient depth.

### Phase D — implement compact Learning-Artifact Skill

Create the Skill with a short operational flow, expected roughly:

```text
identify learning deliverable
→ establish current truth
→ recover directly relevant history
→ pressure-test / audit if needed
→ select representative real case/flow
→ calibrate depth
→ choose one note vs small package
→ author
→ QA + fast relearning route + anchors
→ STOP
```

Keep the Skill substantially smaller than the major primary-operation Skills unless real usage demonstrates a need for a conditional reference file.

### Phase E — routing/composition integration

Align only necessary references across root/Operating Guide/related Skills.

Key requirement:

```text
five primary operation Skills remain five
+
learning-artifact is a support/composition Skill
```

Natural-language intent must be enough; Ali should not need to know the exact Skill name.

### Phase F — deterministic and behavioral regression protection

Update deterministic governance checks where support-Skill assumptions require it.

Add a small number of behavioral cases covering at least:

1. explicit source-code learning-note request activates the authoring procedure without Learning-Only interaction requirements;
2. directly relevant working-memory is consulted when it contains implementation rationale/error/fix history;
3. unrelated historical working-memory is not scanned reflexively;
4. questionable implementation triggers honest evaluation/Audit composition rather than invented rationale;
5. real UpgradePilot case/flow is preferred over detached toy examples when available;
6. lookup-level incidental syntax is explained proportionately rather than expanded into a prerequisite course;
7. finding a defect does not silently authorize Build/source repair;
8. the new Skill remains support/composition rather than a sixth primary operation.

Use deterministic tooling only for objective structure/identity/reference facts. Behavioral quality still requires semantic review/trials.

### Phase G — real artifact trial

Before merge readiness, use the new Skill on at least one real bounded UpgradePilot learning-artifact request representative of actual use, preferably a code-bearing responsibility with:

- directly relevant working-memory history;
- a real product-simulation/data/control flow;
- focused tests/proof;
- enough complexity to exercise depth calibration.

Evaluate the produced artifact for:

- current factual accuracy;
- correct authority/history distinction;
- no invented rationale;
- real-case grounding;
- appropriate depth;
- useful size/structure;
- fast relearning usefulness;
- honest proof/non-proof;
- no accidental product mutation.

Refine only evidence-backed weaknesses discovered by the trial.

### Phase H — final consistency review

Check:

- learning README ↔ new Skill;
- new Skill ↔ Learning-Only / Learning-by-Doing / Audit / Working-Memory;
- root routing/discoverability;
- governance doctor assumptions;
- provenance marker uniqueness;
- no duplicated doctrine;
- no unintentional changes outside governance/learning-artifact procedure surfaces.

Then stop for Ali's explicit merge decision.

## 13. Acceptance criteria

Group 10 is implementation-complete only when all of the following are true:

1. One compact support/composition Skill exists for learning-artifact authoring.
2. `learning/README.md` remains the canonical semantic owner and clearly admits AI-authored later-study/relearning artifacts.
3. Current source/accepted owners/evidence outrank historical working-memory rationale.
4. Directly relevant working-memory is intentionally used to recover implementation path/errors/decisions when valuable.
5. The procedure explicitly forbids invented rationale for questionable implementation and routes material evaluation to Audit.
6. Real UpgradePilot cases/user/data/control/evidence flows are the default teaching substrate when available.
7. Depth is calibrated using existing ownership/operational/lookup/defer principles without a competing taxonomy.
8. The procedure can create one focused note or a small package proportionately without mandatory ceremony.
9. Learning artifacts remain snapshot-aware, non-authoritative for live state, and evidence-bounded.
10. The Skill does not silently authorize product/source/test repair.
11. Natural-language discovery works without Ali naming the Skill.
12. The five primary operation Skills remain distinct from support/composition Skills.
13. Deterministic checks and focused behavioral cases protect the new routing/identity boundaries where appropriate.
14. At least one representative real artifact trial demonstrates that the Skill produces useful, accurate, non-superficial, non-bloated study material.
15. Final branch review shows no unrelated product/runtime changes.

## 14. Explicit non-goals

Do not use Group 10 to:

- redesign Learning-by-Doing or Learning-Only broadly;
- create a universal course framework;
- require HTML lessons, quizzes, flashcards, spaced-repetition machinery, or external LMS integration;
- create a mandatory learning package for every responsibility;
- scan all working-memory before every note;
- replace Audit with learning-artifact authoring;
- repair product code without Build authorization;
- create a new product specification/ADR merely for learning-note procedure;
- rewrite historical learning snapshots for consistency;
- create learning artifacts merely because a project step occurred;
- merge the branch into `main` without Ali's separate explicit decision.

## 15. Stop line

This plan authorizes **planning artifacts only**.

After this plan and its family index are written:

```text
STOP
→ review/discuss with Ali
→ do not create the Skill
→ do not modify learning/README.md or routing/governance implementation
→ do not run an implementation trial
→ wait for separate authorization
```

Governance provenance for this planning responsibility:

```text
UP-SKILL:upgradepilot-planning-design
```
