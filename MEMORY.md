# UpgradePilot Current Memory

**Last updated:** 2026-07-21  
**Purpose:** Concise project-local continuation pointer. The canonical Career tracker owns program state and capability evidence; accepted specifications/ADRs own requirements and decisions; source/tests/outputs own implementation truth.

## Current responsibility

M2-S01 — initial trusted case transformation using the accepted source boundary and Pydantic v2 runtime-contract decision.

## Accepted decisions relevant now

- Source/package boundary: `docs/architecture/ADR-0001-initial-python-source-layout.md`.
- Core contracts/invariants: `docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`.
- Runtime-contract method: `docs/architecture/ADR-0002-pydantic-runtime-contract-models.md`.
- Pydantic v2 is used for strict boundary/trusted application contracts.
- Raw source data remains outside trusted Pydantic models.
- Flat-to-nested conversion remains an explicit tested adapter.
- Application contracts remain separate from persistence records and permanent public report schemas.

## Activated semantic model

```text
repository + pr_number + base_sha + head_sha
→ PullRequestSnapshotIdentity

dependency + old_version + new_version
→ DependencyChange

changed_files
→ ChangedFileEvidence

all trusted components
→ InitialCaseRecord
```

The flat eight-field mapping is a provisional M2 adapter, not the eventual public input or one permanent identity object.

## Project-local implementation evidence

The current working record reports:

- Python 3.12.3 is available as `python3`;
- `.venv` and editable installation were created;
- Pydantic 2.13.4 was installed under `>=2.13.4,<3`;
- `upgradepilot` resolved from `src/upgradepilot/__init__.py`;
- an AI-generated first `case_identity.py` draft exists;
- 19 bounded contract tests pass, covering the real M1 case, representative invalid input, raw non-mutation/alias resistance, trusted-model protection, serialization, duplicate diagnostics, and casing policy;
- `compileall` and `pip check` pass.

These observations are not final acceptance or capability ownership. Inspect the current files and rerun relevant checks before relying on them.

## Unresolved work

- publish the verified project-local implementation change;
- reconcile the new implementation, assistance, and capability evidence in canonical Career before changing the M2-S01 gate;
- select the next controlled responsibility from canonical Career after that review.

## Ownership boundary

- Ali identified the requirements-before-method gap and challenged the premature rejection of Pydantic.
- ADR-0002 and much of the specification/implementation wording were substantially AI-generated under Ali direction.
- Package metadata, the initial implementation, and most tests are AI-generated/AI-assisted.
- Ali approved and directed the duplicate-path diagnostic improvement.
- Ali diagnosed a removed-lowercase failure with reduced assistance; strictness versus format terminology required correction.
- Broad independent Pydantic, packaging, testing, and debugging ownership remains unproven.

## Canonical references

- Canonical live state: `docs/program/career/tracking/UPGRADEPILOT_EVIDENCE_AND_PROGRESS_TRACKER.md` after checking snapshot age in `docs/program/SOURCE.md`.
- Current detailed evidence: `working-memory/2026-07-20_M2-S01_case-identity-implementation-start.md`.
- Requirements: `docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`.
- Decisions: `docs/architecture/ADR-0001-initial-python-source-layout.md` and `docs/architecture/ADR-0002-pydantic-runtime-contract-models.md`.
- Authorization: current canonical Career M2 plan and amendment.

## Immediate continuation pointer

Publish the verified implementation evidence, then reconcile M2-S01 state and assistance conservatively in canonical Career before selecting the next controlled responsibility.

Do not copy this continuation into README, `AGENTS.md`, specifications, ADRs, roadmap, or stable governance files.
