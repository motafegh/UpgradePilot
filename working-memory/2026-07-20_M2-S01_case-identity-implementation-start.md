# M2-S01 Working Evidence — Initial Trusted Case

**Date:** 2026-07-20 to 2026-07-21  
**Status:** Active material-work record  
**Milestone:** M2 — First automated vertical slice  
**Plan:** `plans/M2_S01_INITIAL_TRUSTED_CASE_PLAN.md`

## 1. Responsibility

Implement and verify the first trusted UpgradePilot case transformation:

```text
manual eight-field input
→ preserve raw mapping/list
→ strict boundary validation and permitted normalization
→ explicit flat-to-nested adapter
→ PullRequestSnapshotIdentity
→ DependencyChange
→ ChangedFileEvidence
→ InitialCaseRecord
```

The flat mapping is a provisional M2 adapter, not the eventual public input or permanent semantic identity.

## 2. Why the contract changed

The initial M2 planning treated the eight fields too much like one flat identity and prohibited external validation frameworks before the real contract had been defined.

Ali challenged that sequence and identified the requirements-before-method gap:

- project responsibilities and invariants must be clear before rejecting a method;
- the project should not preserve a weaker approach merely because an earlier plan assumed it;
- Pydantic was a credible candidate for required fields, strict runtime types, normalization, nested construction, mutation protection, and structured failures;
- Ali needed enough explanation to evaluate alternatives before approving one.

This led to:

- the project-local core specification;
- ADR-0002 selecting bounded Pydantic v2 use;
- a corrected nested semantic contract;
- the consolidated project-local M2-S01 plan.

## 3. Accepted boundaries

### Source/package

- repository/product: `UpgradePilot`;
- distribution/import package: `upgradepilot`;
- source root: `src/upgradepilot/`;
- tests: `tests/`;
- no speculative package layers.

### Runtime contracts

- raw mappings/lists remain outside trusted Pydantic models;
- activated boundary and trusted models use strict Pydantic v2 validation;
- undeclared fields are rejected;
- trusted models are frozen;
- trusted changed-file paths use `tuple[str, ...]`;
- flat-to-nested conversion remains explicit and directly tested;
- Pydantic validation errors may remain internal during M2;
- application models are not persistence rows or permanent public report schemas.

### Activated behavior

- all eight fields required;
- exact accepted runtime types; no silent coercion;
- whitespace trimming only where declared;
- valid SHAs stored lowercase;
- repository uses the current basic `owner/name` boundary;
- PR number is a positive non-boolean integer;
- base/head SHAs are 40 hexadecimal characters;
- dependency and versions are non-empty;
- old/new versions differ;
- changed-file paths are non-empty and unique after trimming;
- path order is preserved;
- raw mapping/list remain unchanged;
- trusted paths do not alias the raw list;
- validation failure returns no partial trusted record.

## 4. Files created

- `pyproject.toml`;
- `src/upgradepilot/__init__.py`;
- `src/upgradepilot/case_identity.py`;
- `tests/test_case_identity.py`.

The first complete implementation and most tests were AI-generated after Ali explicitly requested a full first draft for learning through real code.

## 5. Observed environment and proof

Observed:

- Python 3.12.3 is available as `python3`;
- `.venv` creation succeeded;
- editable installation succeeded;
- Pydantic 2.13.4 installed under `>=2.13.4,<3`;
- `upgradepilot` resolved from `src/upgradepilot/__init__.py`;
- `pip check` reported no broken requirements;
- `compileall` passed.

Initial test-first evidence:

- the valid test initially failed with `ModuleNotFoundError` because `upgradepilot.case_identity` did not yet exist;
- after the AI-generated implementation draft, the real M1 valid-case/non-mutation test passed;
- direct invalid-input probing produced structured `int_type` and `extra_forbidden` findings;
- malformed-head-SHA testing produced structured location `('head_sha',)` and expected message meaning.

## 6. Test evidence

The suite expanded to 19 passing tests covering, at minimum:

- real valid M1 transformation;
- required and extra fields;
- representative strict runtime types;
- repository, PR-number, SHA, text, version, and path invariants;
- permitted normalization and source-order preservation;
- raw non-mutation and alias resistance;
- nested trusted-record creation;
- serialization;
- direct trusted-contract validation;
- frozen-model behavior;
- duplicate-path diagnostics;
- non-SHA casing preservation.

These results must be rerun before current acceptance because this record is historical evidence, not executable truth.

## 7. Ali-directed duplicate-path change

Ali approved improving duplicate-path rejection so the error identifies the first normalized duplicate.

Evidence:

- the test was changed first and failed because the prior set-length comparison detected duplication but discarded duplicate identity;
- the AI explained the source-order scan and `seen`-set repair;
- the smallest implementation change passed the targeted test, full suite, and `compileall`.

Ownership conclusion:

- behavior change: Ali-directed;
- diagnosis and code: AI-assisted rather than Ali-owned.

## 8. Lowercase-SHA failure diagnosis

A controlled defect removed lowercase SHA canonicalization.

Ali correctly identified:

- the missing `.lower()` behavior;
- the resulting uppercase stored value;
- the smallest repair.

Correction required:

- strictness and hexadecimal format validation still passed;
- the failure was normalization/canonicalization, not strict typing or format validation.

A later reconciliation found that a temporary repair had matched the generic text normalizer instead of the SHA normalizer. That would have lowercased repository, dependency, version, and path values while failing to canonicalize SHAs.

The functions were corrected and a non-SHA-casing regression was added. All 19 tests, `compileall`, editable import verification, and `pip check` passed afterward.

Ownership conclusion:

- Ali diagnosed the missing lowercase behavior with reduced assistance;
- boundary terminology required correction;
- final repair and regression strengthening remained AI-assisted.

## 9. Assistance and capability boundary

- Ali identified and challenged the requirements-before-method defect.
- Ali proposed Pydantic as a serious candidate and approved the bounded method.
- The detailed comparison, specification, ADR, initial package metadata, implementation, and most tests were substantially AI-generated.
- Ali directed the duplicate diagnostic improvement.
- Ali completed one reduced-assistance failure diagnosis with a conceptual correction.
- Broad independent Pydantic, packaging, testing, debugging, or Python application ownership remains unproven.

## 10. Current unresolved work

Before M2-S01 can close:

1. inspect current source, tests, and environment;
2. rerun the proof commands;
3. compare code/tests with activated specification requirements;
4. identify any actual remaining proof or ownership gap;
5. ensure the Ali-directed change and failure-diagnosis evidence satisfy the current plan at the claimed narrow scope;
6. record concise continuation in `MEMORY.md`.

## 11. Career boundary

Do not update Career for this ordinary project continuation.

Ali will explicitly request a Career review when he wants Career to inspect UpgradePilot and update coarse project state, capability assessment, workload/capacity, role strategy, or portfolio claims.

## 12. Immediate continuation

Follow `MEMORY.md` and `plans/M2_S01_INITIAL_TRUSTED_CASE_PLAN.md`:

- inspect current implementation truth;
- rerun the narrow and broader required checks;
- identify a demonstrated gap before editing;
- complete only the remaining M2-S01 proof and ownership work.
