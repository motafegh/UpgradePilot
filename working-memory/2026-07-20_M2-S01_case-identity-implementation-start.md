# M2-S01 Working Memory — Initial Case Contract and Representation Decision

**Date:** 2026-07-20 to 2026-07-21  
**Session:** M2-S01 continuation  
**Status:** Active  
**Route / milestone:** R2 / M2 — First automated vertical slice  
**Mode:** Green  
**Focused minutes:** Not recorded

## Current objective

Define the smallest coherent contract for UpgradePilot's first automated transformation, select an appropriate Python representation and validation method from the actual project requirements, and only then begin test-first implementation.

The corrected implementation responsibility is:

> Receive a manually assembled input derived from the M1 case, preserve the raw input, validate and normalize the activated fields, and construct one trusted initial case record that separates PR snapshot identity, dependency change, and changed-file evidence.

## Starting state

At activation of this continuation:

- the initial source/package layout was accepted through `docs/architecture/ADR-0001-initial-python-source-layout.md`;
- the repository/product name was `UpgradePilot`;
- the Python distribution and import package name was `upgradepilot`;
- no `pyproject.toml`, source package, implementation module, or test module existed;
- the original plan described eight fields as one case-identity dictionary;
- no representation method, runtime dependency, implementation behavior, test result, packaging execution, or practical ownership was accepted.

## Initial mental model

The session initially used:

```text
raw input dictionary
→ confirm required fields and basic value types
→ normalize declared representations
→ validate normalized values
→ construct a new case-identity dictionary
→ return it while preserving raw input
```

This was adequate for discussing a local transformation but incomplete as a project model.

## Calibration and discussion evidence

Ali stated that validation, cleaning, and rule-definition methods felt familiar conceptually and that the session should not manufacture difficulty merely because Python syntax or implementation details remained unproven.

Ali proposed:

- regular expressions as a possible normalization/validation mechanism;
- Pydantic as a possible way to provide required-field checks, typing, normalization order, cross-field validation, new-output construction, non-mutation, and failure behavior.

The first AI response rejected Pydantic because the narrow session plan prohibited schema frameworks and external dependencies. Ali correctly challenged that reasoning:

- the project should not preserve a weaker method merely because an earlier pre-implementation plan assumed one;
- method selection should consider the full UpgradePilot trajectory, not only the immediate function;
- the rules and product contracts must be decided before framework mechanics can be meaningfully debated;
- assessment should allow Ali to complete his proposed approach before the AI supplies the alternative answer.

This was a material learning-method and technical-planning correction.

## Problem identified

The governing charter, capability specification, roadmap, and milestone plan correctly define:

- mission and user;
- supported decision classes;
- evidence doctrine;
- raw and normalized evidence;
- provenance and evidence states;
- persistence, replay, evaluation, and later experiments;
- milestone order and capability gates.

They intentionally do not define the project-level conceptual objects and their relationships.

The original M2 plan then moved directly from broad product requirements to one eight-field dictionary. Discussion exposed that the dictionary conflated:

```text
PR snapshot identity
+
dependency transition
+
changed-file evidence
```

Without an intermediate contract layer, local choices about dictionaries, Pydantic, strictness, coercion, errors, serialization, and persistence could establish misleading permanent assumptions.

## Accepted correction

A project-level technical specification layer was added:

- `docs/specifications/README.md`;
- `docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`.

The Career control layer was amended through:

- `plans/UPGRADEPILOT_M2_S01_TECHNICAL_CONTRACT_AMENDMENT.md`.

The corrected semantic mapping is:

```text
repository + pr_number + base_sha + head_sha
→ PullRequestSnapshotIdentity

dependency + old_version + new_version
→ DependencyChange

changed_files
→ ChangedFileEvidence

all components + preserved raw/manual source reference
→ InitialCaseRecord
```

The eight-field dictionary remains a provisional manual M2 adapter. It is not the eventual public input and not one permanent identity object.

## Accepted whole-project boundaries

The specification now records:

- acquisition request;
- pull-request snapshot identity;
- dependency change;
- changed-file evidence;
- aggregate initial case record;
- raw source record;
- provenance;
- normalized evidence record;
- explicit evidence states;
- repository/dependency context;
- decision input and result;
- report;
- run/replay record;
- evaluation and experiment records.

Defining these concepts does not authorize implementing all of them during M2.

## Activated M2 rules

The provisional manual adapter requires:

```text
repository
pr_number
base_sha
head_sha
dependency
old_version
new_version
changed_files
```

Current accepted/provisional behavior:

- all eight fields required;
- exact accepted types and no silent coercion;
- surrounding-whitespace trimming only for declared strings and paths;
- basic `owner/name` form;
- positive integer PR number, excluding booleans;
- full 40-character hexadecimal base and head SHAs;
- non-empty dependency and version strings;
- old/new versions differ;
- non-empty changed-file list with non-empty paths;
- raw input and nested mutable values unchanged;
- no partial trusted record after adapter failure;
- invalid manual input remains distinct from missing, inaccessible, stale, conflicting, rejected, unsupported, or not-applicable external evidence.

## Representation decision state

No implementation method is accepted yet.

Candidates:

- plain dictionaries and explicit validation functions;
- `TypedDict` plus runtime validation;
- standard-library dataclasses;
- Pydantic models;
- a purpose-specific combination.

The comparison must consider:

- runtime field/type enforcement;
- strictness versus coercion;
- normalization order;
- field and cross-field validation;
- nested conceptual composition;
- raw preservation and mutation resistance;
- structured errors;
- serialization and contract evolution;
- persistence separation;
- dependency, security, maintenance, and upgrade cost;
- test clarity and failure diagnosis;
- Ali ownership and reversal path.

A durable framework or cross-project representation policy requires an ADR. The source-layout ADR remains valid and does not settle this decision.

## Assistance and ownership

- Ali materially identified the missing technical-contract layer through challenge and reasoning.
- Ali proposed Pydantic as a candidate and rejected premature framework dismissal.
- The AI supplied the whole-project pipeline analysis and drafted the specification and governance amendment.
- The correction is Ali-directed and substantially AI-generated.
- No representation selection, package setup, implementation, test execution, or debugging capability is yet established.

## Scope and stop line

In scope now:

- technical-contract review;
- comparison of representation and validation methods;
- one accepted method decision;
- ADR creation when required;
- then the minimum package and test-first implementation.

Still out of scope:

- implementing every conceptual contract;
- live multi-source acquisition;
- persistence/database/ORM work;
- full evidence hierarchy;
- recommendation or report responsibilities not separately authorized;
- CLI/API framework, CI, containers, cloud, services, queues, ML, graphs, LLMs, or agents;
- speculative source subpackages;
- restoration of prior scaffold files.

## Exact continuation

Compare the candidate representation and validation methods against the accepted specification and M2 amendment. Select the smallest credible method for the activated M2 contract and M3 trajectory, record an ADR if required, then create the minimum package boundary and resume test-first implementation.
