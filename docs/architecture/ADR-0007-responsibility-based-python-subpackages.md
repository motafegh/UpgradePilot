# ADR-0007 — Responsibility-Based Python Subpackages

**Status:** Accepted  
**Date:** 2026-08-04  
**Owner:** Ali Rajabi  
**Scope:** Active Python package internal structure, import boundaries, test ownership, and adjacent non-product Python boundaries

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

The flat package mixed provider names, domain names, implementation-method names, and application boundaries at one level. It also encouraged a large package-root re-export surface and made ownership harder to infer from module names.

The project is still pre-1.0 (`0.0.0`) and has no external library-API compatibility commitment that justifies preserving accidental internal import paths.

The repository also contains executable Python that is intentionally **not product runtime code**: bounded experiments/evaluations and developer-operated validation tools. Their separation from the installable product must be explicit so future code does not blur product behavior, evaluation machinery, and developer operations.

## Decision

Keep the existing distribution and source-root boundary:

```text
src/upgradepilot/
```

but organize implemented product responsibilities into bounded subpackages:

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

Only create a subpackage or module when real implementation moves into it in the same bounded change. Do not pre-create speculative architecture.

Use precise imports from the owning module as the normal internal convention. Keep `upgradepilot.__init__` intentionally small; package-root re-exports are not the default internal API.

The expected product responsibility reading is:

```text
GitHub      → provider-specific acquisition and exact GitHub identity
PyPI        → provider-specific release/index/provenance acquisition
Dependency  → dependency-change contracts, extraction, coordination, version ordering
CI          → workflow-command reading and dependency-exercise interpretation
Upstream    → trusted upstream repository, interval authority, evidence composition, claim grounding
Target      → target Python declaration, specifier semantics, relevance
Application → one PR investigation orchestration
Interface   → CLI argument/output/exit policy
```

`json_contract.py`, `package_identity.py`, and `repository_path.py` may remain at the package root because their meanings are genuinely cross-domain and source-neutral.

## Adjacent executable boundaries

Executable location follows responsibility, not file extension.

```text
src/upgradepilot/
→ installable product runtime only

tests/
→ active deterministic product regression only

experiments/
→ bounded non-product research, evaluation, comparison, and calibration machinery

experiments/tests/
→ regression tests for experiment/evaluation machinery; not product-runtime coverage

tools/
→ developer-operated diagnostics, live proofs, explicit validation runners, and maintenance utilities; not normal product runtime
```

The normal dependency direction is:

```text
tests/             → src/upgradepilot/
experiments/       → src/upgradepilot/
experiments/tests/ → experiments/ + src/upgradepilot/
tools/             → src/upgradepilot/
```

The installable product must not depend on the outer support areas:

```text
src/upgradepilot/ -X-> tests/
src/upgradepilot/ -X-> experiments/
src/upgradepilot/ -X-> tools/
```

Experiment results may justify a later product change, but adoption requires the relevant product responsibility, plan/ADR when consequential, implementation under `src/upgradepilot/`, and product tests. A successful experiment does not become runtime architecture merely by being executable.

A developer proof under `tools/` may exercise live public sources or local infrastructure, but it does not itself define product behavior or replace product tests.

## Import and compatibility policy

UpgradePilot currently has no established public Python library API. During source evolution:

- active source and active product tests use owning imports;
- transition-era root re-exports and legacy compatibility types are removed when their active consumers migrate;
- dated historical records and experiment evidence are not mass-rewritten merely to mirror current names;
- historical experiment code may be minimally migrated when required to remain executable after a product contract moves;
- `src/upgradepilot/` must never import from `experiments/`, `tests/`, or `tools/`.

## Test ownership

`tests/` is the active product deterministic test suite.

Completed experiment/harness tests belong with experiment support rather than being counted indefinitely as product-runtime regression coverage. Product and experiment results must be reported separately because they prove different responsibilities.

A product behavior that graduates from an experiment requires product tests under `tests/`; experiment regression alone is not sufficient.

## New package and directory admission

Do not create a new package or repository directory because a conventional architecture often contains one.

Create a new `src/upgradepilot/` subpackage only when implemented responsibilities demonstrate a stable ownership boundary and real implementation enters it in the same bounded change.

A **new top-level repository directory** has an even higher bar because it changes the project artifact taxonomy. It requires one distinct durable responsibility that is not already owned cleanly elsewhere. When admitted, its responsibility must be registered in the root `AGENTS.md` so future assistants do not have to infer its meaning.

Prefer extending an existing owner over creating parallel homes for the same responsibility.

## Rejected alternatives

### Keep the flat package indefinitely

Rejected because implemented responsibilities form stable provider/domain boundaries and the flat layout obscures ownership.

### Generic layered architecture

Directories such as `services/`, `repositories/`, `managers/`, `adapters/`, `infrastructure/`, or `common/` are rejected unless a later concrete responsibility demonstrates that boundary.

### Put all Python under `src/upgradepilot/`

Rejected because product runtime, experimental evaluation machinery, and developer-operated proof tools have different trust, packaging, test, and lifecycle responsibilities.

### One giant package-root façade

Rejected because it makes internal implementation contracts look public, increases migration cost, and weakens responsibility clarity.

### Separate artifact-routing document

Rejected as the normal owner because it would duplicate repository governance. Root `AGENTS.md` owns repository-wide artifact routing; this ADR owns the durable Python-structure rationale.

### Purely cosmetic renaming

Rejected. The reconciliation also removed demonstrated transition residue and converged duplicated contracts where the underlying responsibility was identical.

## Consequences

Positive:

- module location communicates responsibility;
- provider-specific code stops depending on unrelated provider/client modules for shared identity helpers;
- product tests have a precise meaning distinct from experiment regression;
- experiments remain reusable without becoming hidden runtime dependencies;
- live proofs and developer diagnostics have a clear non-product home;
- future Step 7 semantic runtime code gets a clear upstream-domain home without enlarging the flat package;
- application orchestration can grow without turning `cli.py` into a god-object;
- new top-level artifact categories require explicit governance rather than silent directory growth.

Costs:

- internal imports and active tests must follow owning modules;
- historical experiment code requires deliberate compatibility handling when product contracts move;
- product/experiment/tool distinctions require maintainers to classify responsibility before adding files;
- structural changes require validation sufficient to distinguish move defects from behavior defects.

## Preserved decisions from ADR-0001

ADR-0007 changes only the internal flat-module choice after ADR-0001's stated reassessment trigger was reached.

Still preserved:

```text
repository product name: UpgradePilot
Python distribution/import namespace: upgradepilot
source root: src/upgradepilot/
active product test root: tests/
no speculative empty architecture
installed-package testing rather than repository-root import accidents
```

## Proof

Acceptance of the source reconciliation required:

- narrow tests through migration;
- full active product deterministic suite;
- separate completed experiment regression;
- installed/import smoke;
- CLI entry-point smoke;
- Step 7A exact-commit changelog-discovery regression;
- no production import from experiments/tools/tests;
- no new feature capability introduced by the structural migration.

Current proof state belongs to source, tests, commands, outputs, and `MEMORY.md`, not this ADR.
