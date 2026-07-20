# UpgradePilot Current Memory

**Last updated:** 2026-07-20  
**Purpose:** Compact current-state memory for a newly started AI assistant. Keep this file below 200 lines.

## Current control state

- Primary project: UpgradePilot.
- Program window: 2026-07-20 through 2026-10-17.
- Current route: R2 — Automated vertical slice.
- Current milestone: M2 — First automated vertical slice.
- M1 / UP-S01: Passed on `pydantic/pydantic#13432`.
- M1 recommendation: run targeted checks for semantic correctness of generated Algolia search records.
- M2-entry architecture-status audit: Passed.
- Initial Python source-layout decision: Accepted.
- `docs/program/career/plans/UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md` is approved, controlling, active, and aligned with the accepted source boundary.
- M2-S01 status: active; pre-code onboarding in progress.
- Mode: Green.
- Focused minutes: not recorded.
- Active record: `working-memory/2026-07-20_M2-S01_case-identity-normalization.md`.
- Accepted source-layout record: `docs/architecture/ADR-0001-initial-python-source-layout.md`.
- Concise review note: `learning/concepts/case-identity-validation-and-normalization.md`.

## Active session state

- Step 1 orientation is complete enough to proceed.
- Step 2 teaching is substantially complete; the integrated behavior gate remains open.
- Case identity, exact snapshots, evidence association, raw/normalized data, validation, deterministic transformation, `ValueError`, dictionaries, lists, functions, modules, type hints, unit tests, and bounded test claims were introduced at the depth required before implementation.
- Repository, distribution package, import package, module, `src` layout, editable installation purpose, and import-path verification were introduced conceptually.
- Ali demonstrated guided reasoning about mutable PR snapshots, revision-specific CI evidence, explicit rejection of malformed identity, and separation of repository/product naming from Python import naming.
- Ali corrected fragmented micro-question teaching and challenged temporary-layout reasoning that ignored long-term project growth.
- The initial source/package boundary is accepted.
- No `pyproject.toml`, package directory, source file, test file, installation output, import output, accepted behavior, or implementation ownership exists yet.

## Accepted initial source boundary

```text
UpgradePilot/                  # repository and product workspace
├── pyproject.toml             # not created yet
├── src/
│   └── upgradepilot/          # not created yet
│       ├── __init__.py
│       └── case_identity.py
└── tests/
    └── test_case_identity.py
```

Naming:

- repository/product: `UpgradePilot`;
- distribution: `upgradepilot`;
- import package: `upgradepilot`;
- first module: `upgradepilot.case_identity`.

Accepted scope:

- source/package boundary only;
- minimal root `pyproject.toml` when implementation begins;
- no speculative source subpackages or layered architecture;
- reassess only from observed import, packaging, distribution, interface, or module-cohesion limitations.

## Repository state

- Repository role: documentation, memory, learning, planning, proposal preservation, architecture decisions, and authorized implementation home.
- Accepted source implementation: none.
- Accepted tests, package metadata, installation evidence, executable examples, or CI: none.
- Accepted architecture: ADR-0001 source/package boundary only; complete internal architecture remains undecided.
- `docs/architecture/ARCHITECTURE.md` and `docs/architecture/DECISIONS.md` were removed from the active tree after their audit and replacement by a fresh accepted decision.
- Former AI-generated architecture and scaffold remain historical evidence in Git history only and must not be restored or used as an implementation baseline.
- Root responsibilities:
  - `README.md` — human-facing entry point and concise responsibility map;
  - `AGENTS.md` — durable repository-wide agent behavior;
  - `LEARNING-PREFERENCES.md` — durable project-specific teaching and assessment preferences;
  - `MEMORY.md` — current state;
  - `working-memory/` — detailed records for formal sessions and material work;
  - `learning/` — durable educational artifacts;
  - `plans/` — authorized future detailed project-local technical plans;
  - `proposals/` — substantial unadmitted future ideas and candidate directions;
  - `docs/architecture/` — accepted architecture decisions;
  - Career tracker — canonical general product-progress and capability state.

## Completed evidence

- Repository correction: `working-memory/2026-07-19_REPO-AUDIT_premature-scaffold-correction.md`.
- M1 investigation: `working-memory/2026-07-19_UP-S01_manual-evidence-investigation.md`.
- Architecture-status audit: `working-memory/2026-07-19_M2-ENTRY_architecture-status-audit.md`.
- Agent-instruction redesign: `working-memory/2026-07-19_REPO-GOV_agent-instructions-and-learning-preferences.md`.
- Learning/planning environment: `working-memory/2026-07-19_REPO-GOV_learning-environment-and-plan-ownership.md`.
- Responsibility map and tracker ownership: `working-memory/2026-07-20_REPO-GOV_readme-responsibility-map-and-tracker.md`.
- Future proposal area and enhancement audit: `working-memory/2026-07-20_REPO-GOV_future-enhancement-proposals.md`.
- Initial source-layout decision: `docs/architecture/ADR-0001-initial-python-source-layout.md` and this active record.

## Demonstrated depth

- M1 remains narrow D2 guided evidence work with substantial AI assistance.
- Ali demonstrated narrow guided understanding of dependency relationship, evidence states, CI limits, silent-output risk, proportional checks, and changed-evidence reasoning.
- For source layout, Ali challenged misleading framing, required a production-grade project-wide decision, understood the repository-versus-import-package distinction with guidance, accepted the recommendation, and directed synchronization.
- This is Ali-directed design participation, not practical packaging or architecture ownership.
- Independent package creation, installation, import diagnosis, implementation, testing, and end-to-end repository investigation remain unproven.

## Current decisions

1. Learning and ownership must precede accepted implementation.
2. AI-generated code or architecture does not become progress merely because it exists or passes tests.
3. The M1 report action is `run targeted checks`, not a safety certification.
4. M1 passes at narrow D2 guided depth; broad capability mastery is not claimed.
5. Former AI-generated architecture has no current authority and is not a baseline.
6. Build responsibilities through: teach → predict → execute/direct → inspect → modify/test/diagnose → record evidence.
7. Current state belongs in `MEMORY.md`, not durable instruction files.
8. Career owns program-level planning; UpgradePilot owns detailed technical plans, accepted architecture decisions, implementation, tests, learning, and working records.
9. The Career tracker remains the single general product-progress and capability tracker.
10. During learning-critical work, use meaningful technical chunks followed by integrated reasoning, tracing, transfer, or practical assessment.
11. Proposals are not plans, architecture decisions, current state, or authorization.
12. Keep repository/product name `UpgradePilot`.
13. Use `upgradepilot` for distribution and import naming.
14. Use `src/upgradepilot/` for importable product code and `tests/` for tests.
15. Add only a minimal root `pyproject.toml` when implementation begins.
16. Do not place application modules directly under `src/` or pre-create speculative internal layers.
17. Reassess ADR-0001 only after an observed technical limitation.

## M2-S01 authorized responsibility

Given manually supplied identity fields for `pydantic/pydantic#13432`, validate and normalize them into one deterministic Python record without mutating the raw input.

Required behavior and evidence:

1. manually create the real input dictionary from the M1 report;
2. validate required identity fields and normalize text values;
3. require a positive PR number and 40-character hexadecimal base/head SHAs;
4. require non-empty dependency, version, and changed-file values;
5. require old and new versions to differ;
6. return a new normalized dictionary while leaving raw input unchanged;
7. include one valid test, one malformed-head-SHA test, and raw-input non-mutation proof;
8. preserve one Ali-directed change and one diagnosed failing case;
9. verify editable installation and that `import upgradepilot` resolves from `src/upgradepilot/`.

Not authorized:

- implementation before the integrated behavior gate passes;
- live network acquisition;
- JSON/schema frameworks;
- persistence, recommendation policy, report generation, CLI, services, CI, containers, cloud, models, graphs, or agents;
- runtime/test dependencies;
- speculative source subpackages or restoration of former scaffold files.

## Pre-code gate

Before package metadata, source, or tests are created, Ali must explain as one connected model:

1. why case identity is separate from release, CI, and recommendation evidence;
2. which fields identify the exact PR snapshot;
3. what happens when the head SHA is malformed;
4. why normalization returns a new dictionary instead of mutating raw input;
5. what the valid test proves and does not prove.

The source-layout selection is closed. Review ADR-0001 for understanding; do not reopen it as a preference poll without new technical evidence.

## Exact next authorized action

Close the integrated behavior gate. Then create only `pyproject.toml` and `src/upgradepilot/__init__.py`, run editable installation and import-path verification, write `tests/test_case_identity.py` first, and only then create `src/upgradepilot/case_identity.py`.

## Canonical references

- `README.md`
- `AGENTS.md`
- `docs/architecture/README.md`
- `docs/architecture/ADR-0001-initial-python-source-layout.md`
- `docs/program/SOURCE.md`
- `docs/program/career/plans/UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md`
- `docs/program/career/tracking/UPGRADEPILOT_EVIDENCE_AND_PROGRESS_TRACKER.md`
- `working-memory/2026-07-20_M2-S01_case-identity-normalization.md`
- `learning/concepts/case-identity-validation-and-normalization.md`
- `proposals/README.md`