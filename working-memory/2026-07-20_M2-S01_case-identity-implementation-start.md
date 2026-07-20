# M2-S01 Working Memory — Case-Identity Implementation Start

**Date:** 2026-07-20  
**Session:** M2-S01 continuation  
**Status:** Active  
**Route / milestone:** R2 / M2 — First automated vertical slice  
**Mode:** Green  
**Focused minutes:** Not recorded

## Current objective

Continue the first UpgradePilot implementation responsibility:

> Receive a manually supplied raw case-identity dictionary, normalize the permitted representations, validate the required rules, and return a new deterministic case record without mutating the raw input.

## Starting state

- The initial source/package layout is accepted through `docs/architecture/ADR-0001-initial-python-source-layout.md`.
- The repository/product name remains `UpgradePilot`.
- The Python distribution and import package name is `upgradepilot`.
- No `pyproject.toml`, source package, implementation module, or test module exists yet.
- No implementation behavior, test result, packaging execution, or practical ownership is claimed yet.

## Current mental model

```text
raw input dictionary
→ confirm required fields and basic value types
→ normalize only declared representations
→ validate the normalized values
→ construct a new case-identity dictionary
→ return it while preserving the raw input
```

## Immediate work

Before implementation, make the bounded case-identity contract explicit:

- required fields;
- accepted basic types;
- permitted normalization;
- validation rules;
- output shape;
- failure behavior;
- non-mutation guarantee;
- intentionally deferred behavior.

Then proceed through the accepted package and test-first implementation sequence.

## Scope and stop line

In scope:

- the minimum package boundary already accepted by ADR-0001;
- one case-identity normalization function;
- standard-library tests for the bounded valid and invalid behavior;
- observed installation, import, test, and diagnosis evidence;
- one Ali-directed modification.

Out of scope:

- live GitHub or PyPI acquisition;
- schema frameworks or external dependencies;
- recommendation policy or report generation;
- persistence, CLI, services, CI, containers, cloud, ML, graphs, or agents;
- speculative source subpackages or broader internal architecture.

## Evidence and ownership state

- Current work is AI-assisted.
- Ali has directed the project structure and the need for an explicit behavioral contract before implementation.
- Practical implementation, packaging, testing, and debugging ownership remain unproven.

## Exact continuation

Define and record the bounded case-identity contract, then begin the minimum package and test-first implementation work.