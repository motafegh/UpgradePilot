# UpgradePilot Agent Skills Governance Stage 6 — Root and Operating Guide Refinement Plan

**Plan status:** Structurally complete; executable repository-wide doctor run deferred to final post-merge local validation  
**Authority:** Non-controlling execution coordination; root `AGENTS.md`, `OPERATING_GUIDE.md`, accepted specifications, admitted Skills, and current user authorization remain authoritative.  
**Source proposal:** `proposals/2026-08-27_UPGRADEPILOT_AGENT_SKILLS_AND_GOVERNANCE_EVOLUTION_PROPOSAL.md`

## Responsibility

Refine the always-loaded/root operating surfaces after the five-Skill progressive-disclosure and routing work. Preserve high-salience behavior, correct remaining Learning-by-Doing/Learning-Only routing ambiguity, add a project-wide clear-English communication rule, and keep the existing Source Clarity/comments/docstrings architecture explicit without creating another semantic owner.

This stage is a responsibility/context-quality refinement, not a line-count reduction exercise.

## Entry audit

The read-only Stage 6 audit established the following.

### Root `AGENTS.md`

```text
KEEP
- mandatory Learning-by-Building execution loop near the start
- authority and request-to-action boundary
- responsibility ownership map
- five-operation routing table
- live-state/artifact/executable boundaries
- context discipline
- critical persistent safeguards
- proof-class / implementation-claim discipline
- instruction admission and reinforcement rules
- owner-update/live-state discipline

NARROW / CLARIFY
- Learning-by-Doing context-loading wording so standalone Learning-Only cannot be interpreted as requiring the overlay
- Source Clarity reinforcement so comments/docstrings are named explicitly while the canonical outcomes remain in OPERATING_GUIDE.md
- add only a short high-salience communication-clarity reinforcement, not a second full communication contract

REMOVE / MOVE
- no whole major root section is justified for removal by current evidence
```

### `OPERATING_GUIDE.md`

```text
KEEP
- boundary/Skill relationship
- canonical Learning-by-Doing loop
- context engineering
- proportional-process semantics
- implementation-retention burden
- end-to-end ownership trace
- rationale/necessity/engineering-judgment method
- session/operation proportionality
- Source Clarity outcomes
- teaching/ownership method
- prerequisite repair
- assistance fading
- evidence interpretation
- debugging/failure learning
- commands/tools/environment explanation
- completion/stopping/handoff

NARROW / CLARIFY
- operation-Skill relationship wording that could imply Learning-by-Doing overlays Learning-Only
- keep the exact five Skill paths but avoid duplicated activation meaning where a compact routing statement is enough

ADD
- one canonical communication-clarity rule applying across all UpgradePilot interaction modes
- one explicit Source Clarity sentence that good comments/docstrings are required where they carry material meaning not adequately recoverable from naming/structure/signatures, while rejecting decorative comment/docstring volume

REMOVE / MOVE
- no whole major guide section is justified for removal by current evidence
```

## User requirements traced to owners

### 1. Comments and docstrings during implementation

The existing responsibility chain is correct:

```text
AGENTS.md
→ high-salience implementation safeguard

OPERATING_GUIDE.md §6
→ canonical seven Source Clarity acceptance outcomes

UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md
→ naming/terminology engineering owner only

upgradepilot-build-implement/SKILL.md
→ Build-time Source Clarity gate

upgradepilot-build-implement/references/source-clarity-heuristics.md
→ detailed conditional comments/docstrings/application heuristics
```

The detailed reference already covers reader orientation, cross-file flow, domain literals/regexes, why-comments, narrowest explanation owner, callable/type docstrings, semantic/proof transformations, guard reasoning, algorithms, terminology collisions, lifecycle surfaces, and comment/docstring maintenance.

Stage 6 therefore did **not** create another comments/docstrings specification or copy those heuristics into root context. It made the high-salience requirement explicit enough that implementation cannot treat needed comments/docstrings as optional polish.

### 2. Clear, simple English across project interaction

The accepted Naming Clarity standard concerns artifact names/technical terminology and explicitly does not own learner-teaching procedure. It includes some user-facing label clarity, but it is not a project-wide conversation/output style owner.

`OPERATING_GUIDE.md` is now the canonical communication-clarity owner because it defines how Ali and AI work and communicate across Audit, Planning, Build, debugging, Learning-by-Doing, Learning-Only, testing, and evidence work.

Canonical semantics now require:

- clear, direct, literal English in conversation, explanation, updates, questions, summaries, reviews, plans, handoffs, and learning sessions;
- exact standard technical/specialized terminology when it is the precise term;
- plain-language explanation of unfamiliar necessary technical/project terms rather than vague replacement terms;
- common everyday wording for ordinary non-technical language;
- avoidance of unnecessary idioms, metaphors, figurative expressions, obscure wording, rhetorical flourish, and layered phrasing when a direct literal alternative exists;
- simple surrounding language without shallow technical content.

Root `AGENTS.md` carries a shorter high-salience reinforcement and points back to the Operating Guide.

## Implemented changes

### Root `AGENTS.md`

Stage 6:

- added the concise all-mode communication-clarity reinforcement;
- registered communication clarity in the `OPERATING_GUIDE.md` responsibility-map row;
- made Learning-by-Doing explicitly inapplicable as an automatic overlay to standalone Learning-Only;
- aligned the context-loading bullet with that same boundary;
- strengthened the Source Clarity safeguard to name good, truthful, maintained comments/docstrings explicitly when naming/structure/types/signatures are insufficient;
- preserved the rejection of decorative explanation on obvious code.

No major root section was removed.

### `OPERATING_GUIDE.md`

Stage 6:

- added `communication clarity` to the guide's stated responsibility;
- added §1.1 as the canonical project-wide communication rule;
- corrected Learning-by-Doing/Learning-Only wording in the boundary, core loop, and operation-specific procedure sections;
- replaced the canonical figurative `Universal Ceremony Tax Rule` wording with the literal `Universal Proportional Process Rule` while preserving `Ceremony Tax` only as a compatibility alias for older active material;
- replaced nearby figurative process wording with direct `process` / `process overhead` language;
- made the comments/docstrings obligation explicit in Source Clarity §6;
- reinforced in the teaching section that technical terminology remains exact while surrounding language stays direct and ordinary.

The accepted Naming Clarity standard and all operation Skills/references remained unchanged.

### Behavioral regression

`CONSISTENCY-013 — cross_operation_communication_clarity` now pressures both sides of the communication requirement:

```text
keep exact technical terminology
+
explain it with clear literal ordinary English
```

It rejects:

- inaccurate over-simplification of technical terms;
- unexplained obscure internal shorthand;
- unnecessary metaphors/idioms/figurative expressions/rhetorical flourish;
- multi-layered wording when direct wording is available;
- shallow technical content disguised as simple language.

`tools/agent-governance/README.md` was aligned with this new cross-system case and the literal Proportional Process Rule name.

## Scope proof

Compared with the Stage 6 plan commit `768363de30f7248eb6aa57630a0ad94137abe035`, implementation changed exactly:

```text
AGENTS.md
OPERATING_GUIDE.md
tools/agent-governance/consistency_cases.json
tools/agent-governance/README.md
```

Before this plan-status update, the compare showed:

```text
AGENTS.md                                      +8 / -6
OPERATING_GUIDE.md                             +33 / -11
tools/agent-governance/README.md               +3 / -2
tools/agent-governance/consistency_cases.json  +13 / -0
```

No operation Skill, Skill reference, specification, ADR, product source/test, learning package, root `MEMORY.md`, or `governance_doctor.py` semantic logic changed.

## Responsibility proof

The final ownership split is:

```text
OPERATING_GUIDE.md §1.1
→ canonical project-wide communication clarity

AGENTS.md
→ short high-salience communication reinforcement

Naming Clarity engineering standard
→ artifact names and technical terminology quality

OPERATING_GUIDE.md §6
→ canonical Source Clarity outcomes

Build Skill + conditional Source Clarity reference
→ Build-time application of comments/docstrings and other clarity heuristics
```

No parallel semantic owner was introduced.

## Routing proof

Root and Guide now both state the same boundary:

```text
real project work progressing under a primary operation
→ Learning-by-Doing overlay when material

standalone mastery with project work paused
→ Learning-Only primary route
→ shared global teaching principles from OPERATING_GUIDE.md
→ no automatic Learning-by-Doing dual loading
```

All five exact admitted Skill paths remain present on the root/guide routing surfaces required by deterministic validation.

## Source Clarity proof

The edited global wording preserves:

```text
responsibility-bearing placement / structure / types / names first
→ comments/docstrings where material ambiguity remains
→ semantic purpose rather than syntax narration
→ truthful maintained explanations
→ detailed conditional heuristics only when real clarity pressure exists
```

The detailed 17 Build Source Clarity heuristics were not copied back into always-loaded context.

## Executable governance validation

Per the agreed workflow, full execution of:

```bash
python tools/agent-governance/governance_doctor.py
```

remains deferred until the Skills/governance branch is finalized, merged, and pulled locally.

No repository-wide executable PASS is claimed before that run.

## Pass condition

Stage 6 is structurally complete because:

- project-wide communication clarity has one canonical owner and one concise root reinforcement;
- technical terminology remains precise while ordinary English is required to be clear/direct/literal;
- Learning-by-Doing/Learning-Only global wording matches the admitted Skill boundary;
- comments/docstrings remain explicitly part of Source Clarity without creating comment inflation or a new specification;
- no unjustified major-section deletion occurred;
- the communication rule has behavioral regression coverage;
- changes remained inside the allowed boundary.

Final repository-wide executable acceptance remains contingent on the post-merge local doctor run.

## Stop line

Stage 6 stops here.

Do not begin inside Stage 6:

- retrieval-practice/storage-strength pedagogy additions;
- client-specific invocation metadata;
- live model-evaluation CI;
- another Skill admission;
- broad terminology migration such as renaming every historical use of a project label;
- product/source/test changes.