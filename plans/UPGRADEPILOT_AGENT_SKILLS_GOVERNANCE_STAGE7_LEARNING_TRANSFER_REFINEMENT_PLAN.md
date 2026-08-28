# UpgradePilot Agent Skills Governance Stage 7 — Learning Transfer Refinement Plan

**Plan status:** Structurally complete; executable repository-wide doctor run deferred to final post-merge local validation  
**Authority:** Non-controlling execution coordination; root `AGENTS.md`, `OPERATING_GUIDE.md`, admitted Skills, package-local learning owners, and current user authorization remain authoritative.  
**Source proposal:** `proposals/2026-08-27_UPGRADEPILOT_AGENT_SKILLS_AND_GOVERNANCE_EVOLUTION_PROPOSAL.md`

## Responsibility

Strengthen durable learner transfer with one small project-wide rule: after a mechanism has already been taught and later reappears naturally, use a brief fair retrieval/reconstruction opportunity before replaying the full explanation when that helps measure retained understanding.

This stage does not create a spaced-repetition system, flashcard schedule, learner-profile framework, interleaving framework, teaching sub-Skill, or new operation Skill.

## Entry audit

The read-only audit established:

- prediction, reconstruction, diagnosis, proof classification, and explanation already exist in both learning Skills;
- `OPERATING_GUIDE.md` already requires fair checkpoints and D0–D5 assistance fading by the specific responsibility;
- current rules already restore explanation when a changed context reveals a real prerequisite/model gap;
- the mature B2 learning package independently records later reconstruction as a meaningful mastery gate rather than treating immediate recognition as sufficient;
- the remaining gap is that later natural recurrence does not explicitly say to retrieve/reconstruct before replaying the prior explanation;
- interleaving needs no new framework because real project responsibility already determines when several concepts must be reasoned about together.

## Ownership decision

`OPERATING_GUIDE.md §9` remains the canonical owner because retrieval at natural recurrence is part of assistance fading and evidence of demonstrated understanding.

The two learning Skills apply that rule only inside their existing procedures:

```text
OPERATING_GUIDE.md §9
→ canonical retrieval-at-natural-recurrence rule

Learning-by-Doing Skill
→ apply during progressing real project work

Learning-Only Skill
→ apply during standalone mastery
```

No package-local mastery rule is copied globally beyond this reusable principle.

## Allowed modification boundary

Stage 7 modified only:

- `OPERATING_GUIDE.md`;
- `.agents/skills/upgradepilot-learning-by-doing/SKILL.md`;
- `.agents/skills/upgradepilot-learning-only/SKILL.md`;
- `tools/agent-governance/consistency_cases.json`;
- this plan for completion recording.

It did not modify:

- `AGENTS.md`;
- other operation Skills or Skill references;
- specifications/ADRs;
- product source/tests;
- learning packages or their memories/depth maps;
- root `MEMORY.md`;
- `governance_doctor.py` semantics;
- client-specific evaluation machinery.

## Implemented changes

### 1. Canonical retrieval-at-natural-recurrence rule

`OPERATING_GUIDE.md §9` now preserves D0–D5 and adds the reusable rule:

```text
first meaningful exposure
→ teach the needed premises accurately

later natural recurrence of an already-taught mechanism
→ when fair and useful, use brief retrieval/reconstruction before replaying the explanation
→ inspect what is retained
→ reduce or restore support proportionately
→ continue the real responsibility
```

The rule explicitly states:

- immediate recognition after explanation is not durable ownership;
- retrieval is evidence for assistance calibration, not a pass/fail quiz gate;
- partial/inaccurate retrieval restores the missing explanation or prerequisite;
- genuinely new mechanisms or missing premises are taught first;
- deliberately deferred detail is not tested;
- every repeated step does not become a quiz;
- no flashcards, detached exercises, manufactured failures, or project work are created merely for retrieval opportunities.

### 2. Learning-by-Doing application

The existing ownership-transfer section now applies the Guide rule when an already-taught mechanism naturally reappears in later real project work.

The primary project responsibility remains primary. Retrieval must not manufacture a task or interrupt every recurrence.

### 3. Learning-Only application

The existing fair-checkpoint section now applies the same rule when an already-taught mechanism naturally reappears in the active package/session.

Package-local mastery/depth rules remain authoritative. No global review schedule or repetition quota was introduced.

### 4. Behavioral protection

`consistency_cases.json` now contains:

- `CONSISTENCY-014 — learning_transfer_natural_recurrence_retrieval`
  - positive case for brief fair retrieval before replaying a known explanation when recurrence conditions are satisfied;
  - requires adaptive support afterward;
  - rejects pass/fail treatment and manufactured recurrence.

- `CONSISTENCY-015 — learning_transfer_teach_before_retrieval`
  - negative boundary case for genuinely new mechanisms or missing premises;
  - requires minimum accurate teaching first;
  - rejects unfair first-exposure recall tests, withholding required context, and artificial repetition schedules.

The cases are cross-mode behavioral contracts and do not alter Learning-by-Doing versus Learning-Only routing.

## Explicit non-goals preserved

Stage 7 added none of the following:

- flashcards;
- calendar/time-based spacing rules;
- repetition quotas;
- global review schedules;
- a learner-profile database/framework;
- academic terminology merely for completeness;
- interleaving requirements unrelated to the real task;
- artificial failures or project mutations for retrieval evidence.

## Proof performed

### Responsibility proof

Final ownership remains:

```text
OPERATING_GUIDE.md §9
→ canonical assistance fading + retrieval-at-natural-recurrence semantics

Learning-by-Doing Skill
→ real-project-work application

Learning-Only Skill
→ standalone-mastery application

package-local learning owners
→ exact package depth/mastery/continuation specialization
```

No second global pedagogy owner was introduced.

### D0–D5 proof

The existing D0–D5 assistance-fading levels remain unchanged. The new rule follows them and uses retrieval only as another evidence source for selecting the next support level.

### Behavioral-boundary proof

The paired cases protect both directions:

```text
already taught + natural recurrence + premises available
→ retrieve briefly when useful
→ adapt support

new mechanism OR premises missing
→ teach first
→ retrieve only later when fair
```

### Diff/scope proof

Compared with Stage 7 plan commit `a15116f1c72b15e431a684beb3459b3a582f8486`, the implementation-before-plan-closure changed exactly four files:

```text
.agents/skills/upgradepilot-learning-by-doing/SKILL.md  +2 / -0
.agents/skills/upgradepilot-learning-only/SKILL.md      +2 / -0
OPERATING_GUIDE.md                                      +15 / -0
tools/agent-governance/consistency_cases.json           +27 / -1
```

The single JSON deletion is formatting/end-of-file normalization associated with the appended cases; inspection confirms the previous `CONSISTENCY-001..013` case content remains and `CONSISTENCY-014..015` are appended.

No package-local learning file or product file changed.

## Executable governance validation

Full execution of:

```bash
python tools/agent-governance/governance_doctor.py
```

remains deferred until this Skills/governance branch is finalized, merged, and pulled locally, as previously agreed.

No repository-wide executable PASS is claimed in Stage 7.

## Pass condition

Stage 7 is structurally complete because:

- one canonical retrieval-at-natural-recurrence rule now exists in the established assistance-fading owner;
- both learning Skills apply it without duplicating a teaching framework;
- fair first-exposure teaching remains protected;
- natural recurrence, not artificial scheduling, supplies retrieval opportunities;
- positive and negative behavioral cases protect the distinction;
- the change stayed inside the authorized boundary.

## Stop line

Stage 7 stops here.

Do not begin the sixth-Skill admission review or final whole-branch audit inside this plan.
