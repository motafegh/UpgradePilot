# UpgradePilot Agent Skills Governance Stage 3 — Audit Progressive Disclosure Plan

**Plan status:** Authorized bounded execution plan  
**Authority:** Non-controlling execution coordination; root `AGENTS.md` and normal responsibility owners remain authoritative.  
**Source proposal:** `proposals/2026-08-27_UPGRADEPILOT_AGENT_SKILLS_AND_GOVERNANCE_EVOLUTION_PROPOSAL.md`

## Responsibility

Refine the admitted Repository-Audit Skill so its always-loaded `SKILL.md` retains the complete evaluative procedure while two genuinely conditional probe families—deep Source-Clarity review and governance-system quality review—load only when the selected audit question requires them.

This plan admits only the Stage 3 Audit progressive-disclosure refinement. It does not admit Learning-Only generalization, learning-transfer changes, routing-runner work, root-governance pruning, or another Skill.

## Entry evidence

The Stage 3 baseline audit established:

- `.agents/skills/upgradepilot-repository-audit/SKILL.md` is 19,628 bytes and extends beyond 500 lines;
- the core Audit procedure is coherent and directly protected by `AUDIT-001` through `AUDIT-007`;
- correctness, necessity, retention, end-to-end ownership, overlapping evidence, proof strength, complexity, cross-owner consistency, finding classification, and read-only stopping are part of the normal evaluative procedure and must remain inline;
- Section 5.9 contains detailed Source-Clarity review probes that are explicitly described as optional;
- Section 5.10 applies only when governance itself is the audit subject;
- the 2026-08-23 Group-3 validation record says former Source-Clarity detail was preserved as optional audit probes rather than a universal checklist;
- the original Group-3 plan defines governance-system audit as a distinct proportional depth rather than a universal lens for local audits;
- Stage 2 established the project-local progressive-disclosure pattern: keep core procedure inline, move conditional detail behind a precise trigger, and protect both positive and negative loading behavior.

## Audit disposition

```text
KEEP inline
- activation and read-only action boundary
- bounded / cross-responsibility / governance-system depth selection
- exact audit question and scope
- smallest-sufficient owner loading
- independent implementation/observed truth
- cross-owner consistency chain
- correctness
- implementation fact vs rationale vs judgment vs authority
- necessity analysis
- JUST-* retention
- end-to-end ownership
- overlapping evidence
- proof strength and claim boundaries
- complexity/proportionality
- compact Source-Clarity outcome + trigger
- compact governance-system probe trigger
- finding classification
- smallest disposition
- durable audit-record discipline
- evidence/limitations reporting
- stop boundary
- Learning-by-Doing composition
- output and completion discipline

MOVE behind one conditional reference
- detailed Source-Clarity review probes
- detailed governance-system quality probes

REMOVE
- no whole section is currently justified for deletion
```

## Allowed modification boundary

This plan may modify only:

- `.agents/skills/upgradepilot-repository-audit/SKILL.md`;
- `.agents/skills/upgradepilot-repository-audit/references/conditional-audit-probes.md` as a new focused reference;
- `tools/agent-governance/audit_cases.json` to protect positive and negative disclosure behavior;
- this plan if execution exposes an ambiguity in its bounded coordination responsibility.

No root governance, `OPERATING_GUIDE.md`, specification, ADR, product source/test, other Skill, learning package, `MEMORY.md`, or governance-doctor semantics are in scope.

## Execution sequence

### 1. Create one focused conditional-probes reference

Create:

```text
.agents/skills/upgradepilot-repository-audit/references/conditional-audit-probes.md
```

The reference must preserve two clearly separated probe families:

1. Source-Clarity / maintainability probes;
2. governance-system quality probes.

It must state that these are optional application aids, not new semantic owners or universal audit checklists, and that the agent returns to the main Audit procedure after applying the relevant probes.

### 2. Keep compact triggers in the main Audit Skill

For Source Clarity, keep inline:

- `OPERATING_GUIDE.md` §6 and Naming Clarity as the owners;
- the outcome-based maintainability question;
- a trigger to load the conditional probe reference when source readability/maintainability, cross-file flow, proof transformations, non-obvious reasoning, API/state/legacy ambiguity, or comparable clarity pressure is materially part of the audit.

For governance-system audits, keep inline:

- the fact that additional governance-quality probes apply only when governance/agent controls themselves are the subject;
- a trigger to load the same conditional reference for canonical ownership, reinforcement, activation/context cost, state leakage, deterministic enforcement, behavioral coverage, or agent-machinery questions.

For ordinary audits without either pressure, do not load the conditional reference reflexively.

### 3. Protect disclosure behavior in the Audit case bank

Add one positive Source-Clarity case that requires the reference.

Add one positive governance-system case that requires the reference.

Use an existing bounded case to protect the negative path where neither probe family is relevant; do not create a redundant third case if `AUDIT-005` can carry that expectation cleanly.

Do not create another case bank or another Audit Skill.

## Proof obligations

### Structural proof

Confirm:

- both detailed probe families exist in the new reference;
- the main Audit Skill contains explicit positive triggers;
- the reference uses a one-level path under the Skill root;
- the main Audit flow remains complete before and after the narrowed lens sections;
- no normal Audit responsibility was moved out of `SKILL.md`;
- no canonical semantic owner changed.

### Behavioral-contract proof

Confirm:

- the Source-Clarity case requires the reference only for material maintainability/clarity pressure;
- the governance-system case requires the reference only when governance itself is being audited;
- the bounded negative case prohibits reflexive loading when neither trigger applies;
- existing `AUDIT-001..007` obligations remain intact and IDs stay unique.

### Diff/scope proof

Compare this plan commit with the final Stage 3 tip and confirm only the allowed files changed.

### Executable governance validation

Per the agreed workflow, full execution of:

```bash
python tools/agent-governance/governance_doctor.py
```

is deferred until the Skills/governance branch is finalized, merged, and pulled into the local checkout. Do not claim an executable governance-doctor PASS before that run.

## Pass condition

Stage 3 is structurally ready when:

- the complete normal Audit procedure remains inline;
- the two conditional deep-probe families exist in one focused reference;
- positive and negative load behavior is explicit and protected by the audit case bank;
- final diff is inside the allowed boundary;
- no later proposal stage has started.

Executable governance PASS remains intentionally deferred to the final post-merge local run.

## Stop line

After this Audit extraction and structural/behavioral-contract review are complete, stop.

Do not begin:

- Learning-Only B2-route generalization;
- storage-strength/retrieval additions;
- trigger/routing execution-runner work;
- root `AGENTS.md` / `OPERATING_GUIDE.md` pruning;
- admission of another Skill.
