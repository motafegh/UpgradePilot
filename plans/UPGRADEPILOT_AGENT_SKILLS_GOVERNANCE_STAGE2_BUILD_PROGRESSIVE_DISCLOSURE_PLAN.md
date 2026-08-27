# UpgradePilot Agent Skills Governance Stage 2 — Build Progressive Disclosure Plan

**Plan status:** Authorized bounded execution plan  
**Authority:** Non-controlling execution coordination; root `AGENTS.md` and normal responsibility owners remain authoritative.  
**Source proposal:** `proposals/2026-08-27_UPGRADEPILOT_AGENT_SKILLS_AND_GOVERNANCE_EVOLUTION_PROPOSAL.md`

## Responsibility

Refine the admitted Build/Implement Skill so its always-loaded `SKILL.md` keeps the complete core Build procedure while the detailed Source Clarity application heuristics load only when a source change presents the clarity pressures those heuristics address.

This plan admits only the Stage 2 Build progressive-disclosure experiment. It does not admit Audit restructuring, Learning-Only generalization, learning-transfer changes, routing-runner work, root-governance pruning, or another Skill.

## Entry evidence

The Stage 2 baseline audit established:

- `.agents/skills/upgradepilot-build-implement/SKILL.md` is 21,415 bytes and extends beyond 540 lines;
- the core Build procedure is coherent and directly protected by `BUILD-001`, `BUILD-002`, `BUILD-003`, `BUILD-005`, `BUILD-006`, `BUILD-007`, `BUILD-008`, `BUILD-009`, and `BUILD-010`;
- Section 8 contains the compact Source Clarity acceptance rule plus 17 detailed optional application heuristics occupying roughly 170 lines;
- `BUILD-004` specifically exercises a non-trivial source-clarity situation with cross-file flow and non-obvious evidence/decision boundaries;
- `OPERATING_GUIDE.md` §6 remains the canonical owner of the seven Source Clarity outcomes and explicitly delegates detailed Build-time application to operation Skills;
- the 2026-08-23 Group-5 validation record shows the 17 heuristics were preserved to retain useful detail from the former Source Clarity contract, but does not establish that all 17 must load on every Build invocation;
- current Agent Skills guidance loads the full `SKILL.md` when activated and recommends moving detailed conditional material to focused references with explicit load triggers.

## Audit disposition

The evidence supports this classification:

```text
KEEP inline
- Build activation/mutation boundary
- exact responsibility/preflight
- executable source/test inspection
- fact vs rationale vs judgment vs authority
- JUST-* retention and end-to-end ownership
- smallest adequate change
- Learning-by-Doing pre-change model
- responsibility-bearing structure/naming
- compact Source Clarity outcome/acceptance rule
- tests/proof
- narrow-to-broad validation
- debugging
- post-change inspection/Learning-by-Doing ownership
- claim discipline
- continuity routing
- completion/stop

MOVE behind one conditional reference
- the 17 detailed Source Clarity application heuristics

REMOVE
- no whole section is currently justified for deletion
```

## Allowed modification boundary

This plan may modify only:

- `.agents/skills/upgradepilot-build-implement/SKILL.md`;
- `.agents/skills/upgradepilot-build-implement/references/source-clarity-heuristics.md` as a new focused reference;
- `tools/agent-governance/build_cases.json` to protect positive and negative progressive-disclosure behavior;
- this plan if execution exposes an ambiguity in its bounded coordination responsibility.

No root governance, `OPERATING_GUIDE.md`, specification, ADR, product source/test, other Skill, learning package, `MEMORY.md`, or governance-doctor semantics are in scope.

## Execution sequence

### 1. Create one focused Source Clarity reference

Create:

```text
.agents/skills/upgradepilot-build-implement/references/source-clarity-heuristics.md
```

Move the current 17 detailed heuristic groups there without weakening their substantive intent.

The reference must state clearly that:

- `OPERATING_GUIDE.md` §6 owns the Source Clarity outcomes;
- the Naming Clarity specification owns naming/terminology quality;
- the heuristics are optional application aids, not a checklist;
- only heuristics relevant to the actual source-clarity pressure should be applied;
- the agent returns to the main Build procedure after using the reference.

### 2. Keep a compact Source Clarity gate in `SKILL.md`

The main Build Skill must retain:

- the requirement that material source changes satisfy `OPERATING_GUIDE.md` §6;
- the competent-maintainer acceptance question;
- structure/naming before comment compensation;
- bounded maintenance of stale nearby explanation;
- an explicit rule not to load deeper Source Clarity guidance for a small already-clear change merely because Build is active.

### 3. Add an explicit branch-trigger pointer

The main Skill should load the reference when one or more material clarity pressures are present, including examples such as:

- substantial/non-trivial module orientation;
- important cross-file data/evidence flow;
- semantic/proof transformation or evidence-ladder behavior;
- non-obvious domain literals, regexes, guards, algorithms, or similar reasoning boundaries;
- multiple primary/auxiliary APIs or structural navigation ambiguity;
- type-state/narrowing semantics;
- current/transitional/legacy surfaces;
- material terminology/documentation ambiguity.

The trigger should be specific enough that `BUILD-004` clearly loads the reference while a tiny already-clear local edit does not.

### 4. Protect both sides of progressive disclosure

Update `BUILD-004` so its existing non-trivial cross-file Source Clarity setup expects the focused reference to be loaded/applied.

Add one discriminating small-edit case that expects the deep Source Clarity reference **not** to load when no trigger is present.

Do not create a separate case bank or a separate Source Clarity Skill.

## Proof obligations

### Structural proof

Inspect the final files and confirm:

- the 17 heuristic groups still exist in the new reference;
- the main Skill contains one clear conditional pointer to that reference;
- the pointer uses a one-level relative path from the Skill root;
- the main Build sequence remains intact before and after Section 8;
- no core Build responsibility was moved out of the main Skill;
- no Source Clarity semantic owner was changed.

### Behavioral-contract proof

Inspect `build_cases.json` and confirm:

- the existing `BUILD-004` non-trivial case requires the reference;
- the new small-edit case prohibits reflexive loading of the reference;
- all existing Build cases retain unique IDs and their existing core obligations.

### Diff/scope proof

Compare the Stage 2 plan commit with the final Stage 2 branch tip and confirm only the allowed Stage 2 files changed.

### Executable governance validation

Per Ali's explicit workflow decision on 2026-08-27, full execution of:

```bash
python tools/agent-governance/governance_doctor.py
```

is deferred until the Skills/governance branch is finalized, merged, and pulled into Ali's local checkout. This stage must not claim an executable governance-doctor PASS before that run.

## Pass condition

Stage 2 is structurally ready when:

- the Build core procedure remains in `SKILL.md`;
- the detailed 17 Source Clarity heuristics exist in one focused reference;
- the main Skill has a specific positive trigger and explicit no-trigger behavior;
- `BUILD-004` protects reference loading for a real clarity-pressure case;
- one small-edit case protects against unnecessary reference loading;
- final diff is inside the allowed modification boundary;
- no broader Stage 3+ work was started.

Executable governance PASS remains intentionally deferred to Ali's final post-merge local run.

## Stop line

After the Stage 2 Build extraction and structural/behavioral-contract review are complete, stop.

Do not begin:

- Repository-Audit progressive disclosure;
- Learning-Only B2-route generalization;
- storage-strength/retrieval additions;
- trigger/routing execution-runner work;
- root `AGENTS.md` / `OPERATING_GUIDE.md` pruning;
- admission of another Skill.
