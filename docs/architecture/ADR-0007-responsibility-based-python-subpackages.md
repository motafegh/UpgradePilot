# ADR-0007 — Responsibility-Based Python Subpackages

**Status:** Accepted  
**Date:** 2026-08-04  
**Owner:** Ali Rajabi  
**Scope:** Active Python package internal structure, import boundaries, and test ownership

## Context

ADR-0001 intentionally began UpgradePilot with a flat `src/upgradepilot/` package and deferred subpackages until implemented responsibilities demonstrated stable boundaries.

That reassessment trigger has now been reached. The active package contains durable families for:

- GitHub acquisition and immutable source identity;
- PyPI acquisition and provenance;
- dependency-version-change extraction and comparison;
- CI command/evidence interpretation;
- upstream repository, interval-authority, and semantic-grounding contracts;
- target Python declaration and relevance evaluation;
- application orchestration and CLI presentation.

The flat package now mixes provider names, domain names, implementation-method names, and application boundaries at one level. It also encourages a large package-root re-export surface and makes ownership harder to infer from module names.

The project is still pre-1.0 (`0.0.0`) and has no external library-API compatibility commitment that justifies preserving accidental internal import paths.

## Decision

Keep the existing distribution and source-root boundary:

```text
src/upgradepilot/
```

but organize implemented responsibilities into bounded subpackages:

```text
upgradepilot/
├── cli.py
├── investigation.py
├── json_contract.py
├── package_identity.py
├── repository_path.py
├── dependency/
├── github/
├── pypi/
├── ci/
├── upstream/
└── target/
```

Only create a subpackage or module when real implementation moves into it in the same migration. Do not pre-create speculative architecture.

Use precise imports from the owning module as the normal internal convention. Keep `upgradepilot.__init__` intentionally small; package-root re-exports are not the default internal API.

The expected responsibility reading is:

```text
GitHub     → provider-specific acquisition and exact GitHub identity
PyPI       → provider-specific release/index/provenance acquisition
Dependency → dependency-change contracts, extraction, coordination, version ordering
CI         → workflow-command reading and dependency-exercise interpretation
Upstream   → trusted upstream repository, interval authority, evidence composition, claim grounding
Target     → target Python declaration, specifier semantics, relevance
Application→ one PR investigation orchestration
Interface  → CLI argument/output/exit policy
```

`json_contract.py`, `package_identity.py`, and `repository_path.py` may remain at the package root because their meanings are genuinely cross-domain and source-neutral.

## Import and compatibility policy

UpgradePilot currently has no established public Python library API. During this reconciliation:

- active source and active product tests migrate to the new owning imports;
- transition-era root re-exports and legacy compatibility types are removed when their active consumers are migrated;
- dated historical records and experiment evidence are not mass-rewritten;
- completed experiment code may retain historical imports if it remains executable without creating a production dependency on `experiments/`;
- `src/upgradepilot/` must never import from `experiments/`.

## Test ownership

`tests/` is the active product deterministic test suite.

Completed Step 6 experiment-harness tests belong with experiment support rather than being counted indefinitely as product-runtime regression coverage. Their separation must preserve the ability to rerun the historical experiment machinery deliberately.

## Rejected alternatives

### Keep the flat package indefinitely

Rejected because implemented responsibilities now form stable provider/domain boundaries and the flat layout obscures ownership.

### Generic layered architecture

Directories such as `services/`, `repositories/`, `managers/`, `adapters/`, `infrastructure/`, or `common/` are rejected unless a later concrete responsibility demonstrates that boundary.

### One giant package-root façade

Rejected because it makes internal implementation contracts look public, increases migration cost, and weakens responsibility clarity.

### Purely cosmetic renaming

Rejected. The reconciliation also removes demonstrated transition residue and converges duplicated contracts where the underlying responsibility is identical.

## Consequences

Positive:

- module location communicates responsibility;
- provider-specific code stops depending on unrelated provider/client modules for shared identity helpers;
- future Step 7 semantic runtime code gets a clear upstream-domain home without enlarging the flat package;
- application orchestration can grow without turning `cli.py` into a god-object;
- tests can mirror product responsibilities more clearly.

Costs:

- many internal imports and active tests must change;
- historical experiment code requires deliberate compatibility handling;
- structural changes must be validated cluster by cluster to distinguish move defects from behavior defects.

## Preserved decisions from ADR-0001

ADR-0007 changes only the internal flat-module choice after ADR-0001's stated reassessment trigger was reached.

Still preserved:

```text
repository product name: UpgradePilot
Python distribution/import namespace: upgradepilot
source root: src/upgradepilot/
active test root: tests/
no speculative empty architecture
installed-package testing rather than repository-root import accidents
```

## Proof

Acceptance requires the source-reconciliation plan's gates, including:

- narrow tests after each migration cluster;
- full active product deterministic suite;
- installed/import smoke;
- CLI entry-point smoke;
- Step 7A exact-commit changelog-discovery regression;
- no production import from `experiments/`;
- no new feature capability introduced by the structural migration.

Current proof state belongs to source, tests, commands, outputs, and `MEMORY.md`, not this ADR.
