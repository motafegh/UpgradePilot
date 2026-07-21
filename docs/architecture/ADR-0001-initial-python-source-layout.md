# ADR-0001 — Initial Python Source Layout

**Status:** Accepted  
**Date:** 2026-07-20  
**Owner:** Ali Rajabi  
**Scope:** Initial repository, distribution, import-package, source, and test boundary

## Context

UpgradePilot is a long-lived Python project whose repository also contains documentation, plans, evidence, and learning material. The first source files need a stable import namespace and must not rely accidentally on the repository root being importable.

The decision must establish a professional starting boundary without pre-creating speculative internal architecture.

## Decision

Use:

```text
UpgradePilot/
├── pyproject.toml
├── src/
│   └── upgradepilot/
│       ├── __init__.py
│       └── case_identity.py
└── tests/
    └── test_case_identity.py
```

Naming:

```text
Product/repository:       UpgradePilot
Python distribution:      upgradepilot
Python import package:    upgradepilot
Source root:               src/upgradepilot/
Test root:                 tests/
Initial module:            upgradepilot.case_identity
```

The lowercase package is the Python namespace inside the repository, not a second product or repository.

## Rationale

- A named import package prevents generic top-level modules from colliding with unrelated code.
- The `src/` layout separates installed application code from repository documents and tests.
- Tests exercise the installed package boundary rather than relying on working-directory behavior.
- The layout supports later modules while allowing subpackages only when real responsibilities demonstrate a boundary.
- Matching distribution and import names minimizes unnecessary naming translation.

## Alternatives

### Root-level module

Rejected as the project baseline because it is suited to a script or disposable exercise, not a growing application.

### Modules directly under `src/`

Rejected because they would create generic top-level imports without an UpgradePilot namespace.

### Flat root package `upgradepilot/`

Valid in general, but not selected because the `src/` boundary more clearly tests installed-package behavior.

### Pre-created layered architecture

Rejected. Directories such as `domain/`, `application/`, `adapters/`, `services/`, or `infrastructure/` require demonstrated responsibility and dependency boundaries before admission.

## Consequences

Accepted now:

- root `pyproject.toml`;
- `src/upgradepilot/` import package;
- `tests/`;
- cohesive initial modules directly under `src/upgradepilot/`.

Not decided:

- complete internal architecture;
- CLI or public API;
- persistence, acquisition, policy, reporting, or evaluation packages;
- dependency manager, publication workflow, CI, container, service, or cloud design.

## Proof

Implementation must verify:

- editable installation succeeds;
- `import upgradepilot` resolves from `src/upgradepilot/`;
- tests import the installed package;
- current source remains within the accepted boundary.

Proof state belongs to source, tests, commands, outputs, and current working evidence—not this ADR.

## Reassessment triggers

Revisit only when evidence shows:

- import behavior incorrectly depends on working directory;
- installation cannot support the required workflow;
- naming conflicts with a real distribution constraint;
- implemented modules demonstrate a stable subpackage boundary;
- a real CLI, service, plugin, or multi-package requirement changes the package boundary;
- testing or deployment exposes a concrete limitation.

Preference, novelty, or a new AI suggestion alone is not a trigger.

## Ownership note

Ali directed and accepted the decision after challenging the earlier temporary-layout framing. That supports an Ali-directed design decision, not broad Python packaging or architecture ownership.
