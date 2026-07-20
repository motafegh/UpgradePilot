# ADR-0001 — Initial Python Source Layout

**Status:** Accepted  
**Date:** 2026-07-20  
**Decision owner:** Ali Rajabi  
**Scope:** Initial repository/source/package boundary for M2 and later growth  
**Assistance:** Technical recommendation and document drafting substantially AI-generated; Ali challenged the original temporary-layout framing, required a production-grade project-wide review, explicitly accepted the decision, and directed repository synchronization  
**Implementation effect:** None by itself. No package metadata, source, test, dependency, or executable behavior is created by this decision.

## Context

UpgradePilot is a long-lived learning-by-building flagship project rather than a disposable exercise. The repository already contains several non-source responsibilities:

```text
docs/
learning/
plans/
proposals/
working-memory/
examples/
```

The first accepted Python files therefore need a stable project namespace and a clear boundary between importable product code and repository documentation, tests, planning, and evidence.

The earlier AI-generated architecture and package decisions are invalid as current design inputs. This decision is derived fresh from the present product direction, expected growth, Python import behavior, packaging discipline, and the active M2 responsibility.

## Decision

Use the following initial source-layout baseline:

```text
UpgradePilot/                  # repository and product workspace
├── pyproject.toml             # minimum project/install metadata
├── src/
│   └── upgradepilot/          # Python import package
│       ├── __init__.py
│       └── case_identity.py   # first authorized behavioral module
└── tests/
    └── test_case_identity.py
```

Use these names:

```text
Product name:             UpgradePilot
GitHub repository:        UpgradePilot
Repository directory:     UpgradePilot
Python distribution:      upgradepilot
Python import package:    upgradepilot
Initial source module:    upgradepilot.case_identity
```

The repository name remains `UpgradePilot`. The lowercase `upgradepilot` directory is not a duplicate repository or second product; it is the Python import namespace contained inside the source root.

## Rationale

### Stable project namespace

A named import package keeps application modules under one clear namespace:

```python
from upgradepilot.case_identity import normalize_case_identity
```

This is clearer and less collision-prone than independent top-level modules such as:

```python
import case_identity
import validation
import evidence
import policy
```

### Source/repository separation

The `src/` boundary keeps importable product code separate from documentation, plans, evidence, tests, and repository utilities. Tests and development should use the installed package boundary rather than accidentally depending on the repository root being on Python's import path.

### Growth without speculative architecture

The decision provides a professional foundation for multiple future modules while avoiding premature directories such as:

```text
domain/
application/
adapters/
services/
repositories/
infrastructure/
```

Those boundaries may appear later only when implemented responsibilities demonstrate distinct ownership, dependency direction, lifecycle, or change patterns.

### Consistent product and package identity

Using `upgradepilot` for both distribution and import naming minimizes conceptual translation. A different package name would be justified only by a real conflict, multiple independently named packages, or a deliberate product split.

## Alternatives considered

### Rename the repository to lowercase

**Rejected.** Repository/product capitalization does not control Python import naming. A lowercase repository would still require a real import package and would not remove the nested namespace.

### Put modules directly under `src/`

```text
src/case_identity.py
src/evidence.py
```

**Rejected.** This creates generic top-level modules without an UpgradePilot namespace and weakens long-term organization and distribution clarity.

### Use one root-level module

```text
case_identity.py
```

**Rejected as the project baseline.** It is adequate for a disposable script or isolated exercise but not the strongest foundation for a growing flagship application with multiple repository responsibilities.

### Use a flat package at the repository root

```text
upgradepilot/
```

**Rejected for the initial baseline.** It can work, but `src/upgradepilot/` provides a clearer installed-package boundary and reduces accidental working-tree imports.

### Use a differently named package

```text
src/decision_engine/
```

**Rejected.** No current product split or naming conflict justifies making the public/internal Python namespace differ from the project identity.

## Accepted scope now

This decision accepts only:

- repository/product name `UpgradePilot`;
- distribution/import name `upgradepilot`;
- source root `src/upgradepilot/`;
- test root `tests/`;
- a minimal root `pyproject.toml` when implementation begins;
- the initial module path `upgradepilot.case_identity`.

It does not accept:

- a complete internal architecture;
- a CLI or public API;
- `scripts/` as an application-code location;
- domain/application/adapter layering;
- persistence, acquisition, policy, reporting, evaluation, or service directories;
- a framework, database, build publication workflow, dependency manager, CI system, container, or cloud design;
- empty placeholder directories for future ideas.

## Implementation rule

The active M2-S01 behavior gate must pass before `pyproject.toml`, `src/upgradepilot/`, or `tests/` are created.

When implementation is authorized, create only:

```text
pyproject.toml
src/upgradepilot/__init__.py
src/upgradepilot/case_identity.py
tests/test_case_identity.py
```

The initial `pyproject.toml` must contain only the metadata and package discovery needed to install and test the current package. Do not add runtime dependencies, CLI entry points, publication automation, or unrelated tool configuration.

## Required proof during M2-S01

```bash
python -m pip install --editable .
python -c "import upgradepilot; print(upgradepilot.__file__)"
python -m unittest discover -s tests -v
python -m compileall -q src/upgradepilot tests
```

The import output must resolve through `src/upgradepilot/` in the active environment.

## Growth rule

Begin with cohesive modules directly under `src/upgradepilot/`. Create a subpackage only when several implemented modules form a real responsibility boundary.

For example, this may eventually become justified:

```text
src/upgradepilot/
├── identity/
├── evidence/
└── reporting/
```

It must not be created in advance merely because such names are plausible.

## Reassessment triggers

Revisit this decision only when observed evidence shows one of the following:

- import behavior depends incorrectly on the working directory;
- editable or normal installation cannot support the required workflow;
- distribution naming conflicts with an external registry or product constraint;
- several modules show a stable responsibility boundary requiring a subpackage;
- a real CLI, service, plugin, or multi-package requirement changes the package boundary;
- testing or deployment demonstrates a concrete limitation of the selected layout.

Preference, novelty, visual symmetry, or a new AI suggestion alone is not a reassessment trigger.

## Ownership boundary

Ali directed and accepted this decision after challenging the original explanation and requiring a professional project-wide assessment. That supports an **Ali-directed design decision**.

It does not establish Ali-owned capability in Python packaging, imports, application architecture, or project distribution. Practical ownership requires creating, installing, importing, testing, modifying, and diagnosing the package with preserved evidence.