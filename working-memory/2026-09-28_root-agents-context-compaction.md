# Root AGENTS Context Compaction

**Date:** 2026-09-28
**Status:** CLOSED
**Responsibility:** reduce always-loaded root governance context without changing the newly finalized canonical Learning-by-Doing model

## Why

`AGENTS.md` had grown to 390 lines / ~38k characters. Outside the newly finalized LbD model, several older sections duplicated procedure already owned by operation/support Skills, `docs/README.md`, or `SECURITY.md`.

Root governance should act primarily as a bootloader/router plus high-salience engineering invariants, not as the complete operating manual.

## Changes

- Preserved the newly finalized LbD section byte-for-byte.
- Compressed the Smart Situational Override Rule while preserving its material-override semantics and owner-reconciliation requirement.
- Reduced request/action routing to the authorization distinctions needed at root.
- Kept the responsibility-owner table as the primary navigation surface.
- Compressed operation routing to primary-operation → Skill mapping plus only material composition rules.
- Defined `upgradepilot-project-reentry-orientation` as standalone read-only orientation when a substantive LbD cycle is not yet being entered; A0/A1 own equivalent orientation inside a substantive cycle.
- Reduced artifact-management prose to root invariants and delegated detailed promotion/navigation to `docs/README.md`.
- Reduced context discipline to the smallest-sufficient-context route and conditional owner loading.
- Kept persistent engineering/proof safeguards that are broadly relevant at root.
- Removed duplicated security/trust/high-risk-action safeguards from root and centralized them in `SECURITY.md`.

## Security ownership consolidation

`SECURITY.md` now explicitly owns repository-level safeguards for:

- secrets/private information;
- untrusted evidence/content;
- external target mutation;
- destructive/history-rewriting Git;
- paid/material external actions;
- credential-sensitive actions;
- unknown/third-party code execution;
- deliberate credential/transport behavior.

`AGENTS.md` now contains routing pointers to `SECURITY.md` rather than repeating these rules.

## Verification

After compaction:

```text
AGENTS.md: 390 lines / ~38k chars
→ 293 lines / ~23k chars
```

The canonical LbD section was compared against commit `8b4c2f31cf98ee0610713c223af994354576f306` and is exactly preserved (137 lines in both versions).

A root scan confirmed security-related terms remain only as owner/routing pointers (plus ordinary wording such as non-destructive validation), not duplicated safeguard procedures.

The re-entry Skill no longer contains the obsolete `A → B → C → D → E` model and now explicitly defers to A0/A1 when a substantive cycle is entered.

## Commits

- `318fc87` — compact root agent governance.
- `26960ae` — centralize security and high-risk safeguards.
- `24642a8` — separate standalone re-entry from LbD A0/A1.

## Live-state effect

No product source/tests changed. The Runtime Dependency-State Proof Increment 2 live continuation remains unchanged: resume through refined A0 re-entry and A1, then STOP.

UP-SKILL:upgradepilot-working-memory
