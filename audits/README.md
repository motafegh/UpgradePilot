# UpgradePilot Audits

## Purpose

`audits/` is the durable, non-controlling home for dated technical audits discovered during implementation, learning, review, or a dedicated audit session.

Use this area when inspection exposes a concrete question about whether an implemented or designed mechanism is necessary, correct, proportionate, maintainable, secure, sufficiently evidenced, or likely to need later revision.

An audit record exists so a useful concern does not disappear into chat history. It must make the concern reproducible enough that a later session can inspect the same responsibility, understand the reasoning, and decide whether a change is justified.

## Authority boundary

Audit records are **evidence and review records, not project-control authority**.

They may:

- identify implementation or design findings;
- distinguish defects from simplification opportunities, risks, and future reassessment questions;
- name affected source files, symbols, tests, plans, specifications, and ADRs;
- record why a mechanism exists and whether its value appears proportional to its complexity;
- describe candidate alternatives and their tradeoffs;
- define concrete reassessment triggers and proof required for a later change;
- link to a later plan, ADR, implementation commit, validation record, or resolution.

They must not:

- replace `MEMORY.md` as the live-state owner;
- silently change a controlling specification, ADR, plan, or implemented contract;
- declare an implementation fixed merely because an audit recommends a change;
- turn speculative future possibilities into requirements;
- duplicate a full implementation plan when no change has been authorized.

If an audit leads to a durable architecture change, update or supersede the owning ADR. If it leads to implementation work, change source/tests through the normal project process. If it changes the live continuation, update `MEMORY.md` only.

## Naming

Use:

```text
YYYY-MM-DD_AUDIT-NNN_short-descriptive-slug.md
```

Example:

```text
2026-08-01_AUDIT-001_exact-pr-file-acquisition-evidence-contract.md
```

Audit numbers are repository-local identifiers for easy cross-reference. The date records when the audit was performed, not when a later fix occurred.

## Minimum record structure

A useful audit should normally contain:

1. **Audit identity** — ID, date, trigger, inspected repository revision, and disposition at the time of review.
2. **Question** — the exact technical/design concern being evaluated.
3. **Scope and exclusions** — what was inspected and what was deliberately not judged.
4. **Observed implementation** — the actual source path and responsibility flow.
5. **Affected code and tests** — concrete files, classes, functions, records, and tests.
6. **Findings** — each finding separated and classified as defect, risk, simplification opportunity, accepted complexity, or future-reassessment item.
7. **Reasoning** — what value the mechanism provides, what is redundant or derivable, and what alternatives exist.
8. **Future relevance** — whether a planned later responsibility could make the mechanism valuable.
9. **Disposition** — keep, simplify, defer, or reassess; an audit recommendation is not authorization to implement.
10. **Reassessment triggers** — observable events that justify reopening the question.
11. **Proof required if changed** — tests/evidence that must remain true after a later refactor.
12. **References** — relevant source, tests, specifications, ADRs, plans, and later resolution records.

## Finding identifiers

Within an audit, use stable finding IDs such as:

```text
AUDIT-001-F1
AUDIT-001-F2
```

Later plans, commits, ADRs, or validation records should reference the finding ID rather than relying only on prose descriptions.

## Review discipline

Prefer the smallest defensible conclusion.

- Do not call complexity overengineering merely because it is unfamiliar.
- Ask what concrete responsibility or risk the mechanism controls.
- Distinguish information needed during validation from information that belongs in a long-lived domain record.
- Distinguish a value that is unique from one that can be derived later from already-preserved evidence.
- Evaluate plausible future value only against planned or observed UpgradePilot responsibilities, not generic possibilities.
- Preserve a mechanism when removal would erase useful evidence or force a more complex replacement.
- Prefer a reassessment trigger over speculative redesign when the future requirement does not exist yet.

## Relationship to other project areas

- `working-memory/` records dated execution and validation evidence.
- `learning/` preserves reusable understanding.
- `proposals/` holds substantial unadmitted ideas.
- `docs/architecture/` records accepted durable architectural decisions.
- `audits/` records dated critical examination of implemented or designed responsibilities and the follow-up questions they expose.

An audit can therefore identify a concern without pretending that the concern is already a proposal, plan, architecture decision, or live task.
