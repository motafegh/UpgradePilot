# UpgradePilot Audits

## Purpose

`audits/` is the durable, non-controlling home for dated critical examination of implemented or designed UpgradePilot responsibilities.

Use an audit record when a concrete concern about correctness, necessity, proportionality, maintainability, security, evidence quality, or future reassessment would otherwise be lost from chat/history.

Do **not** create an audit merely because a review occurred. Small observations can remain in the owning implementation discussion or working-memory record when no durable audit question exists.

## Authority boundary

Audit records are evidence/review records, not project-control authority.

They may identify findings, affected responsibilities, rationale, alternatives, reassessment triggers, and later resolutions. They do not:

- replace `MEMORY.md` as live-state owner;
- silently change a specification, ADR, plan, security rule, or implemented contract;
- authorize implementation merely by recommending it;
- turn speculative possibilities into requirements;
- duplicate a full plan before work is authorized.

If a finding changes stable required behavior, update the owning specification. If it changes durable architecture, update/supersede the owning ADR. If implementation work is authorized, use the normal source/test/plan process. If live continuation changes, update `MEMORY.md` only.

## Lifecycle organization

Canonical audit records keep stable paths directly under `audits/`.

Current lifecycle is managed through:

```text
audits/active/README.md     validated findings selected as current engineering inputs
audits/scheduled/README.md  validated findings explicitly selected for a concrete future trigger and plan
audits/deferred/README.md   valid findings/opportunities not selected or scheduled for current work
audits/absorbed/README.md   findings materially incorporated into stronger owners
```

See [`LIFECYCLE.md`](LIFECYCLE.md) for the movement rule.

The index titles carry the lifecycle label, for example:

```text
ACTIVE — AUDIT-007 — uv Membership Proposition and Lock-Model Boundaries
SCHEDULED — AUDIT-005 — Product AI / Agentic Orchestration and Sequencing Reassessment
```

The canonical audit ID/filename does not change merely because lifecycle changes. Existing audits contain relative references written from `audits/` root; preserving their stable canonical location avoids silently breaking those references.

Current classification (2026-08-23):

- **active:** AUDIT-001, AUDIT-006, AUDIT-007 — inputs to the source/evidence/uv reconciliation;
- **scheduled:** AUDIT-005 — mandatory post-reconciliation B2/X1 AI/agentic evaluation checkpoint, triggered after R7 acceptance/validation;
- **deferred:** AUDIT-004 — valid future uv resolver/currentness question, not current or scheduled implementation work;
- **absorbed:** AUDIT-002, AUDIT-003 — material conclusions already incorporated into stronger CI/decision-model owners; reopen only on a new trigger.

Lifecycle state records review/execution status, not authority. Reclassification never changes product behavior by itself.

## Proportional record modes

Use the **smallest audit format that preserves the decision value**.

### Compact audit — default for one bounded concern

A compact audit may contain only:

1. **Identity** — date and inspected revision/context when material.
2. **Question/scope** — exact concern and exclusions.
3. **Observation** — actual mechanism/evidence inspected.
4. **Finding and reasoning** — defect, risk, simplification opportunity, accepted complexity, or reassessment item.
5. **Disposition** — keep, simplify, defer, schedule, or reassess.
6. **References** — only the owners/evidence needed to reproduce the conclusion.

Add a reassessment trigger or required proof only when the conclusion depends on future conditions or a later change.

### Formal audit — only when justified

Use the fuller structure when the review has several findings, will drive multiple follow-ups, crosses important owners, evaluates consequential security/architecture/evidence risk, or needs durable cross-reference.

A formal audit may add:

- trigger and detailed inspected revision;
- affected source symbols/tests;
- separate finding classifications;
- alternatives/tradeoffs;
- future relevance;
- explicit reassessment triggers;
- proof required if changed;
- later resolution references.

Do not add these sections merely to satisfy a template.

## Naming

For durable formal/cross-referenced audits, use:

```text
YYYY-MM-DD_AUDIT-NNN_short-descriptive-slug.md
```

For a small one-off audit that does not need repository-wide IDs, a clear dated descriptive name is sufficient.

The date records when the audit was performed, not when a later fix occurred.

Lifecycle labels belong in the lifecycle index title, not in the canonical audit ID or stable filename.

## Finding identifiers

Stable finding IDs such as:

```text
AUDIT-001-F1
AUDIT-001-F2
```

are useful when a later plan, ADR, commit, or validation record must reference individual findings.

They are **not mandatory** for a compact audit with one or two self-contained conclusions that will not be independently cross-referenced.

## Review discipline

Prefer the smallest defensible conclusion.

- Do not call complexity overengineering merely because it is unfamiliar.
- Ask what concrete capability, responsibility, or risk the mechanism controls.
- Distinguish validation-time information from long-lived domain state.
- Distinguish unique information from values derivable from already-preserved evidence.
- Evaluate future value only against planned or observed UpgradePilot responsibilities, not generic possibilities.
- Preserve a mechanism when removal would erase useful evidence or force a more complex replacement.
- Prefer a reassessment trigger over speculative redesign when the future requirement does not exist.
- When a future responsibility **is** explicitly selected but blocked by a prerequisite, schedule it with a concrete trigger rather than leaving it indefinitely deferred.
- Apply the `OPERATING_GUIDE.md` Ceremony Tax Rule to the audit process itself.

## Relationship to other project areas

- `working-memory/` → dated execution/validation evidence and reasoning.
- `learning/` → reusable understanding.
- `proposals/` → substantial unadmitted ideas.
- `docs/specifications/` → accepted stable behavior/invariants.
- `docs/architecture/` → accepted durable implementation/structural decisions.
- `audits/` → non-controlling critical examination and follow-up questions.

An audit may identify a concern without pretending that it is already a proposal, plan, architecture decision, implementation task, or live continuation.
