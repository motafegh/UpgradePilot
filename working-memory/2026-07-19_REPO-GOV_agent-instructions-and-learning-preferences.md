# Repository Governance — Agent Instructions and Learning Preferences

**Date:** 2026-07-19  
**Step ID:** REPO-GOV  
**Status:** Active  
**Route / milestone:** R2 / M2 — entry preparation

## Authorized objective

Redesign the repository instruction system so `AGENTS.md` contains only stable agent-operating rules, add a project-specific `LEARNING-PREFERENCES.md`, remove duplicated volatile state, and keep repository entry points and memory references consistent.

## Starting state

- `AGENTS.md` says it is stable but contains the current route, milestone, audit, blocker, and temporary prohibitions.
- `MEMORY.md` correctly records that the architecture-status audit has passed.
- `README.md` still describes that audit as active and blocking.
- No project-specific `LEARNING-PREFERENCES.md` exists.
- Prior AegisLab, Sentinel, Career, and CyberSecEngineer instruction files contain useful patterns but also project-specific or overly large material that must not be copied blindly.

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

## Research and early findings

First-party and specification sources consulted:

- OpenAI Codex guidance on `AGENTS.md` scope, nested precedence, test commands, and manual validation;
- GitHub Copilot guidance on repository-wide and path-specific instructions and avoiding conflicts between concurrently loaded instruction files;
- the open `AGENTS.md` format guidance treating the file as an agent-facing repository README;
- Anthropic Claude Code memory guidance on structured, specific, regularly reviewed project instructions.

Early design decision:

- keep one tool-neutral root `AGENTS.md` as the substantive agent contract;
- do not add duplicate `CLAUDE.md` or Copilot instruction content;
- allow future tool-specific files only as thin routing shims when a tool demonstrably requires them;
- route teaching behavior to `LEARNING-PREFERENCES.md` and current state to `MEMORY.md`.

## Assistance and ownership

- Direction and constraints: Ali-directed.
- Comparative research, drafting, and repository edits: AI-generated / AI-assisted.
- Final ownership requires Ali review and later practical use; this document change alone does not establish implementation capability.
