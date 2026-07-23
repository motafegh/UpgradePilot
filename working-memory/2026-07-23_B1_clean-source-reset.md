# B1 Clean Source Reset

**Status:** Complete  
**Date:** 2026-07-23  
**Stage:** B1 — Implementation responsibility freeze  
**Owner:** Ali Rajabi  
**Decision:** [`../docs/architecture/ADR-0003-clean-slate-b2-source-reset.md`](../docs/architecture/ADR-0003-clean-slate-b2-source-reset.md)

## Trigger

After B1 inspected the previous M2 implementation, Ali explicitly directed the project to
start active source fresh, preserve the old implementation properly, and create required
behavior anew because inherited AI-generated code could confuse his understanding and
learning.

## Preserved historical boundary

Exact pre-reset commit:

```text
e7425dcfc20f093ac10c9a903f1c4ae50a8b2638
```

Manifest:

- [`../archive/2026-07-23_PRE_B2_M2_IMPLEMENTATION.md`](../archive/2026-07-23_PRE_B2_M2_IMPLEMENTATION.md)

Git history is the immutable archive. The old files were not copied into another importable
source tree.

## Active changes

- reset `pyproject.toml` to zero runtime dependencies;
- reset `src/upgradepilot/__init__.py` to a package marker;
- removed all other M2 modules under `src/upgradepilot/`;
- removed all M2 tests and added `tests/README.md`;
- removed local-model and input-risk scripts;
- removed generated M2 model/evaluation JSON files from the repository root;
- superseded ADR-0002's inherited Pydantic decision;
- updated route, B1 requirements, reconciliation, memory, README, agent instructions, and
  learning navigation.

## Structural validation

Connector-backed comparison from the pre-reset commit confirmed removal of:

- eight M2 source modules beyond `__init__.py`;
- nine M2 test files;
- three M2 scripts;
- eleven root-level evaluation outputs.

Explicit absence checks returned `404 Not Found` for representative old paths:

- `src/upgradepilot/case_identity.py`;
- `tests/test_case_identity.py`;
- `scripts/evaluate_python_support_models.py`.

The active `pyproject.toml` was parsed with Python `tomllib`, the package marker compiled,
and an isolated source-path import of `upgradepilot` succeeded with empty `__all__`.

Observed validation result:

```text
toml_parse=passed
compile=passed
isolated_import=passed
```

## Validation limitation

A real clean checkout, editable installation, and repository test command were not run
because the available execution environment could not resolve `github.com`.

No active tests exist yet, by design. B2 must establish fresh installation, import, unit,
and acceptance-test proof.

## Ownership and assistance

Ali made the controlling clean-source and learning decision. The archival design,
repository edits, and validation were substantially AI-executed. This records project
control, not implementation ownership.

## Exact continuation

Keep B2 code paused. Freeze and review:

1. the minimum complete replay-to-decision responsibility;
2. replay fixture contents;
3. deterministic runtime behavior;
4. the smallest dependency and representation baseline;
5. the bounded application interface;
6. universal and conditional responsibilities;
7. acceptance tests and Ali-owned work;
8. one bounded B2 implementation plan.