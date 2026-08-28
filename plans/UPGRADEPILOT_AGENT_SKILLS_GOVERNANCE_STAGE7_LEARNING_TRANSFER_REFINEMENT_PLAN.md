# UpgradePilot Agent Skills Governance Stage 7 — Learning Transfer Refinement Plan

**Plan status:** Authorized bounded execution plan  
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

Stage 7 may modify only:

- `OPERATING_GUIDE.md`;
- `.agents/skills/upgradepilot-learning-by-doing/SKILL.md`;
- `.agents/skills/upgradepilot-learning-only/SKILL.md`;
- `tools/agent-governance/consistency_cases.json` for cross-mode behavioral protection;
- this plan for completion recording.

Do not modify:

- `AGENTS.md`;
- other operation Skills or Skill references;
- specifications/ADRs;
- product source/tests;
- learning packages or their memories/depth maps;
- root `MEMORY.md`;
- `governance_doctor.py` semantics;
- client-specific evaluation machinery.

## Execution sequence

### 1. Add the canonical retrieval-at-natural-recurrence rule

Extend `OPERATING_GUIDE.md §9` without changing D0–D5.

Required semantics:

```text
first meaningful exposure
→ teach the needed premises accurately

later natural recurrence of an already-taught mechanism
→ when fair and useful, ask for brief retrieval/reconstruction before replaying the explanation
→ inspect what is retained
→ restore only the explanation/support actually needed
→ continue the real responsibility
```

State explicitly:

- immediate recognition is not the same as durable ownership;
- retrieval is evidence for assistance calibration, not a pass/fail quiz gate;
- do not use retrieval before the premises were taught;
- do not quiz every repeated step;
- do not create artificial repetition schedules or detached exercises merely to satisfy this rule.

### 2. Apply the rule in Learning-by-Doing

Add a short application paragraph in the existing ownership-transfer/assistance-fading section.

Keep real project work primary. Natural recurrence should arise from the actual Audit/Planning/Build/Debug/etc. responsibility, not from manufacturing an exercise.

### 3. Apply the rule in Learning-Only

Add a short application paragraph in the existing fair-checkpoints/assistance-fading section.

Use later package/session recurrence when it genuinely exists. Do not replace package-local mastery/depth rules or invent a global schedule.

### 4. Add behavioral protection

Add two cross-mode cases to `consistency_cases.json`:

1. **natural recurrence retrieval** — an already-taught mechanism reappears later; the agent should briefly ask Ali to reconstruct/retrieve before replaying everything, then restore explanation proportionately.
2. **first exposure / missing premises** — the mechanism is genuinely new or required premises are missing; the agent must teach first rather than turning retrieval into an unfair quiz.

The cases should protect both Learning-by-Doing and Learning-Only application without changing their routing boundary.

## Explicit non-goals

Do not add:

- flashcards;
- calendar/time-based spacing rules;
- repetition quotas;
- global review schedules;
- a learner-profile database/framework;
- academic terminology merely for completeness;
- interleaving requirements unrelated to the real task;
- artificial failures or project mutations for retrieval evidence.

## Proof obligations

Confirm:

- `OPERATING_GUIDE.md §9` is the only canonical global owner of the new rule;
- D0–D5 remains intact;
- both learning Skills reference/apply the rule proportionately rather than redefining it;
- the positive case protects later natural retrieval;
- the negative case protects first exposure and missing-premise teaching;
- no package-local learning file or product file changes;
- final diff stays inside this stage boundary.

Full execution of:

```bash
python tools/agent-governance/governance_doctor.py
```

remains deferred until this Skills/governance branch is finalized, merged, and pulled locally, as previously agreed. No repository-wide executable PASS is claimed in Stage 7.

## Stop line

After this learning-transfer refinement and its behavioral cases are complete, stop.

Do not begin the sixth-Skill admission review or final whole-branch audit inside this plan.
