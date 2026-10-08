# Investigation Workspace implementation architecture research

**Date:** 2026-10-08. **Operation:** Planning/Design with source audit.
**Branch:** `research/workspace-implementation-architecture-2026-10-08`.
**Baseline:** freshly fetched `main = origin/main = 08243e5b3e455ad26ae1cd142763f4d147269bc6`.
**Predecessor:** [main design cycle](2026-10-07_investigation-workspace-and-investigator-interface-design_lbd-cycle.md), a separate responsibility whose D/E review remains open.

## Cycle progression

```text
A0 — DONE: baseline, governance, native/consumer source and research evidence reconciled.
A1 — COMPRESSED: verified main delta presented; user review remains pending at this stop.
A2 — PREPARED: decision map/program ready; no prototype understanding gate inferred.
B — DONE for preparation: analysis and proposed program only; no prototype begun.
Verification gate — GREEN: source/owner cross-check, 58 native/report anchors and document integrity.
D — CURRENT: research-program result review; no learner-ownership inference.
E — PENDING: repair/defer review gaps and close preparation increment.
C — CONTINUOUS: retain meaningful reconciliation, decisions, evidence and handoff here.
```

## Scope and cadence adjustment

Ali explicitly requested a complete first increment: reconcile latest main, identify open decisions/reuse/risks, propose bounded research, then stop before substantial implementation/prototyping. This authorizes branch creation and preparation artifacts, not production adoption.

Circumstance/evidence → explicit preparation-only deliverable and review stop; no technology or executable seam is being selected.
Normal route → separate A1 and A2 stops before substantive analysis/design B.
Why worse here → stopping after onboarding alone would leave the expressly requested review package incomplete and require approval before there is a concrete program to assess.
Override → combine A1/A2 orientation with bounded read-only investigation and program drafting; retain the user-requested stop before any substantial prototype.
Effect → planning artifacts only, no source/test/runtime changes, no inferred understanding or technology acceptance; result review and D/E remain open.
Reconciliation → record this adjustment here and branch-local selection in `MEMORY.md`; future experiment activation requires review of the concrete program.

## Living orientation map

- Continuity: accepted B2 canonical Workspace direction; B3/B4 conceptual lifecycle and recovery proposal; `08243e5b` separates recovery from retained-input replay. ADR-0012 remains Proposed and Core has no §6.4 insertion.
- Upcoming responsibility: turn open representation/storage/seam/migration choices into comparisons with shared inputs and explicit failure or loss outcomes. Native facts and synthesis permission keep their current owners.
- Important bridge: frozen `PublicPullRequestInvestigation` result → evolving canonical Workspace → consumer projections; recovered checkpoint → historical inspection → separately validated continuation.
- Proof boundary: source inspection and documentation checks establish a grounded program, not working persistence, semantic evaluation, replay, or model quality.
- Ownership targets for review: explain which material dependencies must survive a checkpoint and why revision mismatch alone cannot determine staleness.

## Reconciliation observations

- `git fetch origin main` succeeded; `main...origin/main` was `0/0`; new branch starts exactly at main. The unrelated untracked `2026-10-03_broad-project-and-future-plans-audit_lbd-cycle.md` is preserved and excluded.
- User calls main's boundaries reviewed; repository labels ADR-0012 and Core recovery delta Proposed. Research treats them as constraints as instructed, without editing acceptance status or closing main's design cycle.
- The older B4 checklist bullet in the design record still says CURRENT, while its top block, later completed B4 evidence and `MEMORY.md` say DONE. Use the later reconciliation; do not rerun or edit main's historical checklist here.
- Native acquisition/evaluation precedes the frozen result; report save/open persists a selective report, not canonical state. Current synthesis supports explained abstention only.

## Preparation result and evidence

The [research program](../plans/INVESTIGATION_WORKSPACE_IMPLEMENTATION_ARCHITECTURE_RESEARCH_PLAN.md) separates eight open implementation questions from main-owned boundaries. Its reuse ledger traces native producers → fixed orchestration → synthesis/report → offline save/open. Material workflow/environment/source inputs are locally composed rather than retained as a complete bundle; upstream extraction history is also incomplete. These are capture/retention research risks, not authorization for universal raw capture or duplicate validation.

Prioritized program: (1) material dependency closure plus revision representation; (2) file/SQLite checkpoint comparison and conditional hybrid trial, including interruption/fault/concurrency/backup evidence; (3) scripted Investigator seam with material-basis invalidation; (4) replacement migration proof. Recommend activating only the first experiment after review. No technology winner, schema adoption or product capability is established.

The 2026-09-08 persistence proposal is historical: its no-save CLI and export-first entry context do not control the new recovery responsibility. The pinned H1 proposal at `253b48de20b475eada48810d193bd420c51aa7d4` was inspected via Git; its corpus backend is not canonical Workspace and its pure-view/native-input questions inform seam pressure only. No other worktree changed and no messages were sent to that workstream. H1's design-only status is a pinned observation, not a live status refresh.

Fresh verification: `PYTHONPATH=tests:src .venv/bin/python3 -m unittest test_ci_dependency_state test_conditional_pyproject_consumption test_python_support_impact test_impact_applicability test_report test_report_file` — **58 PASS**. This reruns native/report anchors from latest main; it does not exercise Workspace state, durability, crash recovery, concurrency, migration or model quality. No full product/experiment suite, live model, installed-package or hosted verification is warranted by this preparation-only diff.

Document verification: three touched documents, 38 local link occurrences and fenced blocks pass; selective repository internal-link, normative-ID uniqueness and audit-lifecycle checks pass; `git diff --check` passes. No protected executable or accepted-contract owner changed. Full governance doctor is not rerun; main's inherited `examples/` marker finding remains historical debt, not a fresh result or a repair target here.

## Review frontier

Review the ordered program and experiment 1's retention/representation boundary before substantial prototyping. Main's formal ADR/Core acceptance stays with main. D/E remain open; agreeing the program does not establish learner ownership or a technology choice. A meaningful ownership discussion can explain why retaining a final assessment without its material evaluation basis is inadequate, and why an unrelated revision update need not invalidate a delayed same-target observation.

## Provenance

`UP-SKILL:upgradepilot-repository-audit`
`UP-SKILL:upgradepilot-planning-design`
`UP-SKILL:upgradepilot-working-memory`
