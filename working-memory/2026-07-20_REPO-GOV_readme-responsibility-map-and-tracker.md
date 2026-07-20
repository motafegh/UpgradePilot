# Repository Governance — README Responsibility Map and Tracker Ownership

**Date:** 2026-07-20  
**Step ID:** REPO-GOV  
**Status:** Completed  
**Route / milestone:** R2 / M2 — first automated vertical slice

## Objective

Put the concise repository responsibility map in the root README, make the existing Career tracker explicitly canonical, and avoid creating another reference or tracker file.

## Decisions

1. The root `README.md` is the human-facing responsibility map.
2. No separate repository-responsibility-map file is created now.
3. `Career/tracking/UPGRADEPILOT_EVIDENCE_AND_PROGRESS_TRACKER.md` is the single general product-progress and capability tracker.
4. UpgradePilot does not maintain a second general tracker.
5. A separate technical inventory is allowed only when it measures a distinct engineering concern and does not duplicate the canonical tracker.
6. Detailed rules remain in their owning files; the README table only routes readers.

## Files changed

### Career

- `README.md`

Career merge commit: `d1cafdfd61c1b03b291e6cd196e06480be950087`.

### UpgradePilot

- `README.md`
- `AGENTS.md`
- `MEMORY.md`
- `docs/program/SOURCE.md`
- `docs/program/career/README.md`
- this record

## Validation

- No new responsibility-map file was created.
- No new progress tracker was created.
- The README map routes to the existing owning files and areas.
- The canonical tracker path is named exactly.
- Distinct technical inventories remain allowed only for non-overlapping engineering concerns.
- The mirrored Career README is byte-identical to canonical Career content.
- Snapshot provenance points to Career commit `d1cafdfd61c1b03b291e6cd196e06480be950087`.
- No source code, tests, architecture, plan, route, progress state, capability claim, or M2-S01 scope changed.
- The exact M2-S01 next action remains unchanged.

## Assistance and ownership

- Direction and decisions: Ali-directed.
- Drafting, integration, and repository edits: AI-generated / AI-assisted.
- This governance change establishes no implementation capability.

## Result

**Pass condition:** Passed.

The repository now has one concise human-facing responsibility map and one canonical general progress/capability tracker without adding unnecessary files.

## Exact next authorized action

Start M2-S01 using its required start message, then answer the five pre-code questions before creating any source file.
