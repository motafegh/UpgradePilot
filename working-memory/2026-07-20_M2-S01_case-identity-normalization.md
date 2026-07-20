# M2-S01 Working Memory — Case-Identity Normalization

**Date:** 2026-07-20  
**Session:** M2-S01  
**Status:** Superseded  
**Superseded on:** 2026-07-21  
**Superseded by:** `working-memory/2026-07-20_M2-S01_case-identity-implementation-start.md`  
**Route / milestone:** R2 / M2 — First automated vertical slice  
**Mode:** Green  
**Focused minutes:** Not recorded

## Supersession reason

This record preserves the first M2-S01 orientation, teaching, and source-layout decision. It is no longer the active execution record because later pre-code discussion identified a material semantic problem:

- the original eight-field “case identity” mixed PR snapshot identity, dependency transition, and changed-file evidence;
- the project lacked a technical-contract layer between governance and implementation;
- framework/method selection was being constrained before the whole activated contract was understood.

The controlling continuation is now:

- `docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`;
- `docs/program/career/plans/UPGRADEPILOT_M2_S01_TECHNICAL_CONTRACT_AMENDMENT.md`;
- `working-memory/2026-07-20_M2-S01_case-identity-implementation-start.md`.

Git history preserves the full pre-supersession version of this record.

## Original authorized objective

The session originally stated:

> Given manually supplied identity fields for `pydantic/pydantic#13432`, validate and normalize them into one deterministic Python record without mutating the raw input.

That bounded transformation remains useful, but its terminology and trusted output were corrected before implementation.

## Starting repository state

At session activation:

- accepted source implementation: none;
- accepted tests: none;
- accepted package layout: none;
- accepted architecture: none;
- the removed AI-generated scaffold was not an implementation baseline;
- the real case fields came from the completed M1 report.

## Scope that was originally established

The session admitted:

- one manually created Python dictionary for the real case;
- field validation and text normalization;
- a new output while preserving raw input;
- the minimum source/package boundary;
- one valid test;
- one malformed/missing `head_sha` test;
- one non-mutation assertion;
- one Ali-directed behavior change;
- one observed and diagnosed failure.

It excluded live acquisition, persistence, recommendation policy, report generation, CLI, services, CI, containers, cloud, agents, ML, graphs, and speculative source subpackages.

The later amendment supersedes only the blanket framework/dependency prohibition and the conflated conceptual model. The broad stop line remains.

## Original teaching progress

Concepts introduced at the depth required for the original bounded task included:

- exact PR snapshots;
- repository/PR identity versus base/head revisions;
- evidence association with the correct revision;
- raw versus normalized input;
- normalization versus validation;
- deterministic transformation;
- explicit invalid-input failure;
- dictionaries, lists, functions, modules, type hints, and `unittest`;
- mutation, shallow copying, and independent output construction;
- repository, distribution package, import package, and module;
- `src` layout and editable installation purpose;
- import-path verification.

Observed guided reasoning included:

- Ali explained that one PR number may contain different head revisions;
- Ali recognized that earlier CI evidence does not automatically support a later revision;
- Ali preferred clear rejection over silent continuation for malformed identity;
- Ali distinguished repository/product naming from Python import naming;
- Ali challenged fragmented micro-question teaching and temporary-layout framing.

## Source-layout decision preserved from this record

The accepted initial boundary remains:

```text
UpgradePilot/
├── pyproject.toml
├── src/
│   └── upgradepilot/
└── tests/
```

Naming:

- repository/product: `UpgradePilot`;
- distribution/import package: `upgradepilot`;
- source root: `src/upgradepilot/`;
- tests: `tests/`.

The decision is recorded in:

- `docs/architecture/ADR-0001-initial-python-source-layout.md`.

This accepts a source/package boundary, not complete internal architecture.

## Instructional corrections preserved

The first teaching attempt fragmented the material into repeated micro-questions before a complete mental model had been established. Ali correctly identified the momentum and guessing problem.

The corrected rhythm was:

```text
meaningful technical chunk
→ connected explanation and example
→ integrated reasoning or practical task
→ inspect evidence
→ correct the model
→ continue
```

A second correction was:

> A first source-boundary choice must be evaluated against likely project growth without inventing speculative internal layers.

The later contract correction added a third rule:

> Allow Ali to complete a proposed design approach before supplying the alternative answer, and define whole-project contracts before selecting implementation methods.

## Assistance and ownership at supersession

- The work was AI-assisted.
- Ali materially directed teaching-method and source-layout corrections.
- The source-layout recommendation and documentation were substantially AI-generated.
- No package creation, installation, import verification, representation selection, implementation, test execution, or debugging was Ali-owned.

## Corrected continuation

The original flat model is replaced conceptually by:

```text
PullRequestSnapshotIdentity
+
DependencyChange
+
ChangedFileEvidence
+
raw/manual source reference
→ InitialCaseRecord
```

The next action is not the original five-question behavior gate. It is to compare representation and validation methods against the accepted core specification, select and record the method, and then resume minimum test-first implementation.
