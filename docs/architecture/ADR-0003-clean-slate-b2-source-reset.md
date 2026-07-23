# ADR-0003 — Clean-Slate B2 Source Reset

**Status:** Accepted  
**Date:** 2026-07-23  
**Owner:** Ali Rajabi  
**Stage:** B1 — Implementation responsibility freeze  
**Supersedes:** ADR-0002 as a controlling implementation-method decision

## Context

UpgradePilot already contained an M2-era implementation for manual case identity,
normalized evidence, one narrow decision rule, local-LLM semantic extraction, input-risk
experiments, tests, scripts, and evaluation outputs.

The D1 simulations then changed the required product boundary from a narrow report-first
slice to a complete replay-to-decision runtime. Although parts of the M2 code demonstrated
useful ideas, continuing from those classes and tests would make the new design inherit
obsolete assumptions and would make Ali's learning depend on understanding and modifying a
substantially AI-generated implementation.

Ali explicitly directed the project to start the active source fresh, not assume the old
source as a baseline, preserve it properly, and write any later-needed behavior anew.

## Decision

Reset the active product source to a clean package skeleton before freezing B2.

The exact pre-reset implementation is preserved by immutable Git commit:

```text
e7425dcfc20f093ac10c9a903f1c4ae50a8b2638
```

The active tree will:

- retain the accepted repository/distribution/import boundary from ADR-0001;
- retain only a minimal `src/upgradepilot/__init__.py` package marker;
- keep a minimal dependency-free `pyproject.toml` package configuration;
- remove M2 implementation modules from the active import path;
- remove M2 tests from the active test path;
- remove M2 model/evaluation scripts and generated root outputs from the active tree;
- preserve a manifest under `archive/` that identifies the exact historical commit and
  files;
- create all B2 contracts, runtime behavior, tests, and dependencies from the accepted B1
  responsibility rather than copying the old source structure.

## Non-reuse rule

The archived implementation is evidence, not a code library or implementation baseline.

A later B2 or B4 task may inspect an archived idea only when a current responsibility names
the need. The required behavior must then be re-derived from current specifications and
case evidence, taught at the blocking depth, and implemented in the active source without
automatically restoring or copying the old module.

Similarity of a new implementation to an archived idea is acceptable only when the current
responsibility independently justifies it.

## Consequences

### Benefits

- Ali learns the new runtime from its real responsibility rather than reverse-engineering
  obsolete AI-generated code.
- Old M2 names, assumptions, tests, and provider dependencies cannot silently control B2.
- The active source truth becomes small and unambiguous.
- Historical evidence remains exactly recoverable.
- B1 can choose representations and dependencies from the accepted runtime instead of
  inherited method decisions.

### Costs

- Previously working validation and test code is no longer active.
- B2 must reimplement even concepts that may resemble earlier work.
- Fresh installation and test proof must be established again.
- Historical tests cannot be counted as current product coverage.

These costs are accepted because learning clarity and a correct runtime boundary are more
important than retaining a small obsolete implementation.

## Pydantic disposition

ADR-0002 is superseded as a controlling method decision.

Pydantic is neither rejected nor preselected. B1/B2 may consider it again only after the
new contracts and validation requirements are frozen and compared with a simpler credible
standard-library baseline. No prior Pydantic code or test establishes its automatic
readmission.

## What remains accepted

ADR-0001 remains accepted for:

- the `src/upgradepilot/` import boundary;
- the `tests/` location;
- root `pyproject.toml` metadata;
- avoidance of speculative source subpackages.

The product charter, D1 evidence, route, specifications, simulation artifacts, and learning
records remain unchanged by the source reset.

## Proof required

The reset is complete only when:

- the archive manifest points to the exact pre-reset commit;
- old runtime modules are absent from `src/upgradepilot/`;
- old product tests are absent from `tests/`;
- old model/evaluation scripts and generated root outputs are absent;
- active `pyproject.toml` has no inherited runtime dependency;
- `import upgradepilot` resolves only the fresh package marker when execution is available;
- current memory records that B1 responsibility freezing continues from a clean source.

A fresh local installation/import check may be deferred only when the execution environment
cannot obtain the repository; that limitation must remain explicit.

## Reassessment triggers

Reassess this decision only when:

- a current requirement identifies a specific archived mechanism worth comparing;
- the clean reset prevents a required compatibility or migration obligation;
- preserving an active compatibility layer becomes necessary for real external users;
- B1 discovers that a supposedly archived behavior is already a supported public contract.

Convenience, familiarity, or the existence of old passing tests is not a reassessment
trigger.

## Ownership note

Ali made the controlling decision to start active implementation fresh because the prior
AI-assisted code would obstruct his understanding and learning. The archival mechanics and
this ADR are AI-authored under that direction. This records an Ali-controlled project
boundary, not implementation capability.