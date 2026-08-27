# UpgradePilot Agent Skills Governance Stage 6 — Root and Operating Guide Refinement Plan

**Plan status:** Authorized bounded execution plan  
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
- proportional-process / ceremony-cost semantics
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
- operation-Skill relationship wording that currently can imply Learning-by-Doing overlays Learning-Only
- keep the exact five Skill paths but avoid duplicated activation prose where a compact routing statement is enough

ADD
- one canonical communication-clarity rule applying across all UpgradePilot interaction modes
- one explicit Source Clarity sentence that good comments/docstrings are required where they carry material meaning not adequately recoverable from naming/structure/signatures, while rejecting decorative comment/docstring volume

REMOVE / MOVE
- no whole major guide section is justified for removal by current evidence
```

## User requirements traced to owners

### 1. Comments and docstrings during implementation

The existing responsibility chain is already correct:

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

Therefore Stage 6 must **not** create a new comments/docstrings specification or copy those heuristics into root context. It should only make the high-salience requirement explicit enough that implementation cannot treat comments/docstrings as optional polish when they are needed for Source Clarity.

### 2. Clear, simple English across project interaction

No current durable owner expresses the requested rule strongly enough.

The accepted Naming Clarity standard concerns artifact names/technical terminology and explicitly does not own learner-teaching procedure. It includes some user-facing label clarity, but it is not a project-wide conversation/output style owner.

`OPERATING_GUIDE.md` is the correct canonical owner because it defines how Ali and AI work and communicate across Audit, Planning, Build, debugging, Learning-by-Doing, Learning-Only, testing, and evidence work.

Required canonical semantics:

- use clear, direct, literal English in project conversation, explanation, updates, questions, summaries, and handoffs;
- preserve exact standard technical/specialized terminology when it is the precise term;
- do not replace technical terms with vague simplifications;
- for ordinary non-technical language, prefer common everyday words with one clear meaning in context;
- avoid unnecessary idioms, metaphors, figurative expressions, obscure wording, and multi-layered phrasing when a direct literal alternative exists;
- when a necessary technical or project term may be unfamiliar, keep the exact term and explain it in plain language.

Root `AGENTS.md` should carry only a short high-salience reinforcement pointing to the Operating Guide.

## Allowed modification boundary

Stage 6 may modify only:

- `AGENTS.md`;
- `OPERATING_GUIDE.md`;
- `tools/agent-governance/consistency_cases.json` for the cross-operation communication-clarity regression;
- `tools/agent-governance/README.md` only if the consistency-bank coverage description needs alignment;
- this plan to record structural completion.

Do not modify:

- any operation Skill;
- any Skill reference;
- the Naming Clarity specification;
- any other specification/ADR;
- product source/tests;
- learning packages;
- root `MEMORY.md`;
- `governance_doctor.py` semantics.

## Execution sequence

### 1. Add communication clarity to the canonical operating method

Add a compact project-wide communication subsection near the Operating Guide boundary/relationship section, without renumbering existing major sections.

The rule must apply to all operation modes, not only Learning-Only or teaching.

Do not ban precise technical terminology. The target is simpler ordinary English around the technical content.

### 2. Add concise root reinforcement

Add one short standing instruction in `AGENTS.md` that:

- requires clear/direct/literal ordinary English;
- preserves precise technical terms;
- points to `OPERATING_GUIDE.md` for the complete communication rule.

Do not duplicate the full rule in root.

Update the responsibility map entry for `OPERATING_GUIDE.md` if needed so communication clarity is part of its stated responsibility.

### 3. Reconcile Learning-by-Doing and Learning-Only globally

Correct root/guide wording so the global surfaces match Stage 4:

```text
real project work progressing under Audit/Planning/Build/Debug/etc.
→ primary operation + Learning-by-Doing overlay when material

standalone mastery with project work paused
→ Learning-Only primary procedure
→ shared teaching principles come from OPERATING_GUIDE.md
→ do not load Learning-by-Doing merely because the learning session is substantive
```

Keep all five exact Skill paths discoverable so current deterministic routing validation remains valid.

### 4. Strengthen the high-salience comments/docstrings statement

In the root Source Clarity safeguard and/or canonical Source Clarity section, state explicitly that good, truthful, maintained comments/docstrings are required where important responsibility, flow, invariant, decision rationale, domain rule, semantic/proof transformation, or proof limitation would remain ambiguous from naming/structure/signatures alone.

Also preserve the proportional boundary:

- comments/docstrings do not compensate for vague names or poor structure;
- do not require decorative comments/docstrings on every import, line, trivial helper, or obvious callable;
- detailed heuristics remain in the conditional Build reference.

### 5. Add behavioral protection for communication clarity

Add one `consistency_cases.json` case because the rule applies across operation families.

The case should pressure both sides of the requirement:

```text
preserve exact technical terminology
+
use plain literal ordinary English around it
```

Expected behavior should reject:

- replacing correct technical terms with inaccurate baby-language;
- unexplained obscure/internal jargon;
- unnecessary metaphors/idioms/figurative phrasing;
- ambiguous conversational wording when a direct expression is available.

This is a behavioral contract, not a deterministic prose-style linter.

### 6. Do not force pruning where no responsibility evidence supports it

The audit found no major root/guide section whose whole responsibility should be removed. Do not delete material solely to reduce bytes or lines.

Narrow duplicated wording only when the same behavior remains recoverable from the correct owner and high-salience reinforcement.

## Proof obligations

### Responsibility proof

Confirm:

- `OPERATING_GUIDE.md` is the canonical project-wide communication-clarity owner;
- root reinforcement is shorter and points to the guide;
- Naming Clarity remains the artifact naming/terminology owner rather than becoming a conversation-style contract;
- Source Clarity/comments/docstrings remain owned by the Guide + Build application procedure/reference.

### Routing proof

Confirm root and guide no longer imply Learning-by-Doing should overlay standalone Learning-Only.

### Source Clarity proof

Confirm the edited global wording still preserves:

```text
structure/naming first
→ comments/docstrings where material ambiguity remains
→ truthful maintained explanation
→ detailed conditional heuristics only when clarity pressure requires them
```

### Behavioral-contract proof

Confirm the new consistency case protects clear ordinary English without weakening technical terminology.

### Diff/scope proof

Compare this plan commit with the final Stage 6 tip and confirm only allowed files changed.

### Executable governance validation

Per the agreed workflow, full execution of:

```bash
python tools/agent-governance/governance_doctor.py
```

remains deferred until the Skills/governance branch is finalized, merged, and pulled locally. No repository-wide executable PASS is claimed before that run.

## Pass condition

Stage 6 is structurally ready when:

- project-wide communication clarity has one canonical owner and one concise root reinforcement;
- technical terminology remains precise while ordinary English is required to be clear/direct/literal;
- Learning-by-Doing/Learning-Only global wording matches the admitted Skill boundary;
- comments/docstrings remain explicitly part of Source Clarity without creating comment inflation or a new specification;
- no unjustified major-section deletion occurs;
- the communication rule has behavioral regression coverage;
- changes remain inside the allowed boundary.

## Stop line

After root/guide refinement and its behavioral case are complete, stop.

Do not begin inside Stage 6:

- retrieval-practice/storage-strength pedagogy additions;
- client-specific invocation metadata;
- live model-evaluation CI;
- another Skill admission;
- broad terminology migration such as renaming every historical use of a project label;
- product/source/test changes.