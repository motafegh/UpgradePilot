# UpgradePilot Agent Skills Governance Stage 4 — Learning Mode Reconciliation Plan

**Plan status:** Authorized bounded execution plan  
**Authority:** Non-controlling execution coordination; root `AGENTS.md`, `OPERATING_GUIDE.md`, package-local learning owners, and normal operation owners remain authoritative.  
**Source proposal:** `proposals/2026-08-27_UPGRADEPILOT_AGENT_SKILLS_AND_GOVERNANCE_EVOLUTION_PROPOSAL.md`

## Responsibility

Reconcile the admitted Learning-by-Doing and Learning-Only Skills so their trigger/action boundaries are distinct, package discovery remains generic, and B2 stays a real compatibility regression target without being cached as a universal Skill route.

This stage does **not** add new teaching theory, retrieval-practice/storage-strength rules, another learning Skill, a new learning package, or product changes.

## Entry evidence

The Stage 4 baseline audit established:

- Learning-by-Doing is an overlay for substantive real project work; the primary operation controls authorization and action;
- Learning-Only is the primary procedure when understanding/mastery is the selected responsibility and product mutation is paused;
- both Skills intentionally share global teaching principles through `OPERATING_GUIDE.md` and must not collapse into one mode;
- the current Learning-Only Skill has a generic package discovery route **and** an additional hard-coded `B2 compatibility pattern` containing one package path and exact filenames;
- the original Group-6 plan and validation record explicitly define B2 as the first compatibility/integration target and say its specialized route/depth mechanics must not be copied into the universal Skill;
- `LEARN-002` already protects the exact B2 package route through package-local owners, so the global Skill does not need to cache those filenames to preserve B2 behavior;
- Learning-by-Doing's automatic activation clause can currently be read broadly enough to load the overlay during a substantive standalone Learning-Only session even though Learning-Only already applies the shared global teaching principles;
- the two frontmatter descriptions are directionally distinct but can express the negative boundary more clearly for Skill selection.

## Audit disposition

```text
KEEP
- Learning-by-Doing as an overlay during real primary-operation work
- Learning-Only as the standalone no-product-mutation mastery operation
- shared global teaching principles in OPERATING_GUIDE.md
- generic package discovery in Learning-Only
- package contract/index/LEARNING_MEMORY/plan/depth-map/source-test responsibility model
- B2 as a behavioral compatibility case in learning_only_cases.json
- Learning-Only technical independence, source/test proof, prerequisite repair, memory separation, Audit composition, and return-to-building behavior

NARROW / CLARIFY
- both Skill descriptions so trigger metadata distinguishes overlay work from standalone mastery
- Learning-by-Doing activation so standalone Learning-Only is an explicit negative trigger
- Learning-Only package-discovery wording so package-local filenames/route are discovered from local owners rather than cached globally

REMOVE FROM GLOBAL SKILL
- the hard-coded B2 package path/file-name compatibility subsection

ADD REGRESSION COVERAGE
- Learning-by-Doing must not load merely because a standalone Learning-Only session is substantive
- Learning-by-Doing must still load when explicitly requested together with a mutating/read-only primary operation that is progressing real project work
- generic package discovery must work for a non-B2 package shape without assuming B2 filenames
```

## Allowed modification boundary

This stage may modify only:

- `.agents/skills/upgradepilot-learning-by-doing/SKILL.md`;
- `.agents/skills/upgradepilot-learning-only/SKILL.md`;
- `tools/agent-governance/cases.json` for Learning-by-Doing routing regression coverage;
- `tools/agent-governance/learning_only_cases.json` for generic-package/B2 compatibility coverage;
- this plan to record structural completion.

No root governance, `OPERATING_GUIDE.md`, B2 package files, other learning packages, product source/tests, specifications, ADRs, `MEMORY.md`, or governance-doctor semantics are in scope.

## Execution sequence

### 1. Sharpen Skill metadata

Learning-by-Doing description must emphasize:

- real project work under another primary operation;
- overlay behavior;
- explicit or materially useful learning/action composition;
- exclusion of standalone Learning-Only mastery sessions.

Learning-Only description must emphasize:

- learning/mastery is the selected responsibility;
- product mutation is paused;
- use for standalone study of existing project material rather than project work progressing through another primary operation.

Do not overstuff descriptions with workflow detail.

### 2. Add an explicit Learning-by-Doing negative trigger

In Learning-by-Doing activation, state that a substantive Learning-Only session does not by itself justify loading Learning-by-Doing. Learning-Only already consumes shared `OPERATING_GUIDE.md` teaching principles.

Learning-by-Doing remains available when Ali explicitly requests it with a real primary operation or when substantive project work genuinely benefits from the full action/evidence/ownership-transfer cycle.

### 3. Generalize Learning-Only package discovery

Keep the current preferred package-routing roles, but make clear that exact filenames and package-local sequencing are discovered from the package itself.

Remove the global `B2 compatibility pattern` subsection with its hard-coded path and exact filenames.

Do **not** weaken B2 compatibility: `LEARN-002` remains the regression case that proves B2 resolves to its real package-local contract/index/memory/plan/depth-map owners.

### 4. Protect trigger and locality behavior

Update/add behavioral cases so that:

- an explicit Build/Design/Audit + Learning-by-Doing request still composes the overlay;
- a standalone `stop building; study/master this` request expects Learning-Only and does not expect the Learning-by-Doing Skill merely because the session is substantive;
- B2 continuation still resolves to exact B2 package owners;
- a hypothetical non-B2 package with different local filenames is discovered through its package-local controls rather than forcing the B2 file layout.

Behavioral cases are regression contracts, not new semantic owners.

## Proof obligations

### Structural proof

Confirm:

- neither Skill becomes a copy of the other;
- Learning-by-Doing still contains its complete overlay procedure;
- Learning-Only still contains its complete standalone learning procedure;
- the B2 hard-coded subsection no longer exists in the universal Learning-Only Skill;
- generic package-routing roles remain present;
- no package-local B2 file changed.

### Trigger/routing proof

Confirm the case banks distinguish:

```text
real project work + learning overlay
→ primary operation + Learning-by-Doing

standalone mastery / product mutation paused
→ Learning-Only

existing learning package continuation
→ Learning-Only + discovered package-local owners
```

### Locality proof

Confirm B2-specific route/file names remain represented only where they are legitimate evidence/owners (for example `LEARN-002` and the B2 package itself), not as universal Learning-Only procedure.

### Diff/scope proof

Compare this plan commit with the final Stage 4 tip and confirm only the allowed files changed.

### Executable governance validation

Per the agreed workflow, full execution of:

```bash
python tools/agent-governance/governance_doctor.py
```

is deferred until the Skills/governance branch is finalized, merged, and pulled locally. No executable PASS is claimed before that run.

## Pass condition

Stage 4 is structurally ready when:

- the Learning-by-Doing/Learning-Only trigger boundary is explicit in metadata and procedure;
- standalone Learning-Only no longer risks automatic dual loading solely because it is substantive;
- Learning-Only package routing is generic and package-local;
- B2 remains protected by its real compatibility case without global hard-coding;
- one non-B2 package case protects generic discovery;
- the diff remains inside the allowed boundary;
- no new pedagogy/framework work starts.

## Stop line

After learning-mode trigger/locality reconciliation and structural behavioral-contract review are complete, stop.

Do not begin:

- retrieval-practice/storage-strength additions;
- new teaching workspaces or lesson artifact frameworks;
- routing execution-runner work;
- root governance pruning;
- another Skill admission.