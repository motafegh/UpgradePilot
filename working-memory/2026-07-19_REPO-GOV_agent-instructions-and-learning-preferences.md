# Repository Governance — Agent Instructions and Learning Preferences

**Date:** 2026-07-19  
**Step ID:** REPO-GOV  
**Status:** Completed  
**Route / milestone:** R2 / M2 — entry preparation

## Authorized objective

Redesign the repository instruction system so `AGENTS.md` contains only stable agent-operating rules, add a project-specific `LEARNING-PREFERENCES.md`, remove duplicated volatile state, and keep repository entry points and memory references consistent.

## Starting state

- `AGENTS.md` said it was stable but contained the current route, milestone, audit, blocker, and temporary prohibitions.
- `MEMORY.md` correctly recorded that the architecture-status audit had passed.
- `README.md` still described that audit as active and blocking.
- No project-specific `LEARNING-PREFERENCES.md` existed.
- Prior AegisLab, Sentinel, Career, and CyberSecEngineer instruction files contained useful patterns but also project-specific or oversized material that could not be copied blindly.

## Expected output and pass condition

Expected output:

- a length-optimized, durable root `AGENTS.md`;
- a stable UpgradePilot-specific `LEARNING-PREFERENCES.md`;
- corrected routing references in `README.md`, `MEMORY.md`, and `working-memory/README.md`;
- no change to the exact authorized M2 next action;
- no code, tests, architecture adoption, package metadata, CI, or implementation.

Pass condition:

- volatile state exists only in current-state files;
- instruction files have distinct responsibilities and no material conflict;
- first-party agent-instruction guidance has been considered;
- all links and repository-state statements are internally consistent;
- `MEMORY.md` remains below 200 lines.

## Scope and stop line

In scope: repository instruction and navigation documents plus this working-memory record.

Out of scope: M2 session design, source implementation, architecture adoption, Career snapshot edits, roadmap changes, and capability claims.

## Sources and comparative review

First-party and specification sources consulted:

- OpenAI Codex guidance on `AGENTS.md` scope, nested precedence, validation commands, and manual review;
- GitHub Copilot guidance on repository-wide and path-specific instructions and the need to avoid conflicting concurrently loaded files;
- the open `AGENTS.md` format guidance treating the file as an agent-facing repository README;
- Anthropic Claude Code guidance favoring specific, structured, regularly reviewed project instructions;
- Ali's AegisLab, Sentinel, Career, and CyberSecEngineer instruction files;
- the approved UpgradePilot Learning and Execution Contract.

## Important design correction during the work

The first draft of `LEARNING-PREFERENCES.md` repeated too much of the 691-line canonical Learning and Execution Contract.

That draft was rejected and replaced with a narrower file containing only Ali-specific interaction refinements:

- accurate mental models and anti-oversimplification;
- depth classification;
- minimum complete chunks;
- informed rather than blind prediction;
- live generation-first interaction;
- realistic assessment and recall;
- debugging as model repair;
- tangent control and direct correction style.

## Final decisions

1. `AGENTS.md` is the single substantive, tool-neutral root agent contract.
2. Current route, milestone, blockers, SHAs, active procedures, and exact next action belong outside `AGENTS.md`.
3. `LEARNING-PREFERENCES.md` refines teaching style but does not duplicate or override the canonical contract.
4. `MEMORY.md` remains the compact current-state file.
5. `working-memory/` remains the detailed progressive record system.
6. Future `CLAUDE.md`, `GEMINI.md`, or Copilot files should be thin routing shims unless a demonstrable tool-specific rule is required.
7. Nested `AGENTS.md` files may be added only when a subtree develops genuinely different accepted commands or conventions.
8. Destructive Git actions, unreviewed dependencies, fabricated evidence, silent failure states, and unsupported completion claims are explicitly prohibited.
9. The exact M2 next action is unchanged.

## Files changed

- `AGENTS.md` — rewritten as durable repository-wide agent instructions.
- `LEARNING-PREFERENCES.md` — added as the project-specific teaching-preference specification.
- `README.md` — corrected stale architecture-audit state and added instruction routing.
- `MEMORY.md` — recorded the final instruction split without changing the M2 next action.
- `working-memory/README.md` — added the learning-preferences relationship and strengthened progressive-record guidance.
- this record — created and updated progressively.

## Validation

Validated against branch `agents-learning-spec-rewrite`:

- `AGENTS.md` is 147 content lines and contains no current route, milestone, active blocker, commit SHA, or active audit procedure.
- `LEARNING-PREFERENCES.md` is subordinate to and explicitly avoids duplicating the canonical contract.
- `MEMORY.md` is 105 content lines, below the 200-line hard limit.
- `README.md` and `MEMORY.md` agree that `M2-ENTRY-01` passed and the next action is to define and activate the first bounded M2 session.
- all new internal paths referenced by the changed files exist.
- the compare against `72d63246afc4204780988c0a5ff7b78e17df419c` contains documentation changes only.
- no source code, tests, package metadata, executable example, CI, architecture adoption, or Career snapshot file changed.

## Assistance and ownership

- Direction, constraints, and approval to apply: Ali-directed.
- Comparative research, drafting, and repository edits: AI-generated / AI-assisted.
- Ali has not yet reviewed the final text line by line or demonstrated practical use of the new contract.
- This governance improvement does not establish implementation capability.

## Result and continuation

**Pass condition:** Passed.

`MEMORY.md` was updated. No canonical tracker update was required because the active route, milestone, capability depth, and exact next action did not change.

**Exact next authorized action:** Define and activate the first bounded M2 learning/implementation session using the completed Pydantic case, without restoring the prior scaffold or assuming retained architecture proposals are accepted.
