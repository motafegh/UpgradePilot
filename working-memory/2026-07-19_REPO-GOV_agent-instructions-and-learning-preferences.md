# Repository Governance — Agent Instructions and Learning Preferences

**Date:** 2026-07-19  
**Step ID:** REPO-GOV  
**Status:** Active  
**Route / milestone:** R2 / M2 — entry preparation

## Authorized objective

Redesign the repository instruction system so `AGENTS.md` contains only stable agent-operating rules, add a project-specific `LEARNING-PREFERENCES.md`, remove duplicated volatile state, and keep repository entry points and memory references consistent.

## Starting state

- `AGENTS.md` said it was stable but contained current route, milestone, next action, and first-session requirements.
- `MEMORY.md` correctly recorded that the architecture-status audit passed but did not yet contain all current first-M2-session constraints.
- `README.md` had been corrected concurrently to close the architecture audit.
- No project-specific `LEARNING-PREFERENCES.md` existed.
- Prior AegisLab, Sentinel, Career, and CyberSecEngineer instruction files contained useful patterns but also project-specific or oversized material that could not be copied blindly.

## Expected output and pass condition

Expected output:

- a length-optimized, durable root `AGENTS.md`;
- a stable UpgradePilot-specific `LEARNING-PREFERENCES.md`;
- current M2 constraints preserved in `MEMORY.md`, not lost;
- corrected routing references in `README.md`, `MEMORY.md`, and `working-memory/README.md`;
- no change to the authorized M2 direction;
- no code, tests, architecture adoption, package metadata, CI, or implementation.

Pass condition:

- volatile state exists only in current-state files;
- instruction files have distinct responsibilities and no material conflict;
- first-party agent-instruction guidance has been considered;
- all links and repository-state statements are internally consistent;
- `MEMORY.md` remains below 200 lines;
- concurrent updates on `main` are preserved semantically.

## Scope and stop line

In scope: repository instruction, navigation, and memory documents plus this working-memory record.

Out of scope: M2 session activation, source implementation, architecture adoption, Career snapshot edits, roadmap changes, and capability claims.

## Sources and comparative review

Consulted:

- OpenAI Codex guidance on `AGENTS.md` scope, nested precedence, validation commands, and manual review;
- GitHub Copilot guidance on repository-wide and path-specific instructions and avoiding conflicting concurrently loaded files;
- the open `AGENTS.md` format guidance treating the file as an agent-facing repository README;
- Anthropic Claude Code guidance favoring specific, structured, regularly reviewed project instructions;
- Ali's AegisLab, Sentinel, Career, and CyberSecEngineer instruction files;
- the approved UpgradePilot Learning and Execution Contract.

## Design decisions

1. `AGENTS.md` is the single substantive, tool-neutral root agent contract.
2. Current route, milestone, blockers, SHAs, active procedures, and exact next action belong outside `AGENTS.md`.
3. `LEARNING-PREFERENCES.md` refines Ali-specific teaching style without duplicating the canonical contract.
4. `MEMORY.md` stores current first-M2-session constraints that were previously embedded in `AGENTS.md`.
5. `working-memory/` remains the detailed progressive record system.
6. Future `CLAUDE.md`, `GEMINI.md`, or Copilot files should be thin routing shims unless a demonstrable tool-specific rule is required.
7. Nested `AGENTS.md` files may be added only when a subtree develops genuinely different accepted commands or conventions.
8. Destructive Git actions, unreviewed dependencies, fabricated evidence, silent failure states, and unsupported completion claims are explicitly prohibited.

## Integration note

While the first draft branch was being prepared, `main` advanced with two valid corrections:

- `README.md` closed the architecture audit;
- `AGENTS.md` preserved detailed constraints for the first bounded M2 session.

A direct fast-forward was correctly rejected. A new integration branch was created from the latest `main`. The architecture-audit correction was retained, and the temporary M2-session requirements were moved into `MEMORY.md` rather than discarded.

## Files changed

- `AGENTS.md` — rewritten as durable repository-wide agent instructions.
- `LEARNING-PREFERENCES.md` — added as project-specific teaching preferences.
- `README.md` — added final instruction routing while preserving completed audit state.
- `MEMORY.md` — added instruction responsibilities and current first-M2-session constraints.
- `working-memory/README.md` — clarified the relationship and progressive lifecycle.
- this record — created for the governance change.

## Assistance and ownership

- Direction, constraints, and approval to apply: Ali-directed.
- Comparative research, drafting, integration, and repository edits: AI-generated / AI-assisted.
- Ali has not yet reviewed the final text line by line or demonstrated practical use of the new contract.
- This governance improvement does not establish implementation capability.

## Pending validation

Before closure:

- compare the integration branch with latest `main`;
- verify documentation-only changes;
- verify `AGENTS.md` contains no volatile state;
- verify `MEMORY.md` is below 200 lines;
- verify README, MEMORY, and the architecture-audit records agree;
- verify all new internal paths exist;
- fast-forward `main` without force.
