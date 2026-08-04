# 2026-08-04 Main Architecture-Reconciliation Intake

**Learning package:** `2026-07-31-b2-evidence-pipeline-mastery`  
**Main revision inspected:** `f0096c5547304e4bb2e75c3f5a5ba175b4ca7e0a`  
**Main → learning sync:** PR #20  
**Sync merge commit:** `b0451f3cf797aa50d907f9b335f0c8fc31c6658a`  
**Classification:** architecture-changing repository delta; current CI learning mechanism preserved

## Purpose

Preserve the material source-architecture changes that landed after the previous learning baseline without rewriting older dated learning notes.

This is a learning intake, not live project state. `MEMORY.md` on `main` remains the sole owner of current product continuation.

## Delta scale

Before synchronization, the learning branch was:

```text
255 commits behind main
19 learning commits ahead
```

The delta included:

```text
accepted ADR-0007 responsibility-based subpackages
completed source-structure reconciliation
Step 6 bounded-extractor adoption
Step 7A changelog discovery validation
current Step 7B runtime-integration responsibility
active-source/test cleanup
shared primitive consolidation
experiment/product test separation
application orchestration extraction from CLI
```

Because this delta changes architectural ownership and many source paths, it is not treated as an ordinary rename intake.

## Current validated product source topology

```text
src/upgradepilot/
├── __init__.py
├── __main__.py
├── cli.py
├── investigation.py
├── json_contract.py
├── package_identity.py
├── repository_path.py
├── ci/
│   ├── dependency_exercise.py
│   └── workflow_commands.py
├── dependency/
│   ├── analysis.py
│   ├── change.py
│   ├── requirements.py
│   ├── uv_lock.py
│   └── versioning.py
├── github/
│   ├── actions.py
│   ├── api.py
│   ├── changelog.py
│   ├── identity.py
│   ├── pull_request.py
│   ├── release.py
│   ├── repository.py
│   └── tag.py
├── pypi/
│   ├── api.py
│   ├── provenance.py
│   └── release.py
├── target/
│   ├── python.py
│   ├── python_specifier.py
│   └── relevance.py
└── upstream/
    ├── claim.py
    ├── interval.py
    ├── interval_evidence.py
    └── repository.py
```

## Architecture mental model

ADR-0007 adopts **responsibility-based decomposition** rather than generic technical layers.

```text
GitHub
→ provider-specific acquisition and immutable GitHub identity

PyPI
→ provider-specific release/index/provenance acquisition

Dependency
→ dependency-change contracts, extraction, coordination, version ordering

CI
→ workflow-command interpretation and dependency-exercise classification

Upstream
→ upstream repository identity, interval authority, evidence composition, claim grounding

Target
→ target Python declaration, specifier semantics, relevance

Application
→ one PR investigation orchestration

Interface
→ CLI arguments, rendering, and exit policy
```

The architectural goal is that module location answers:

> Which responsibility owns this behavior?

It is deliberately **not**:

```text
services/
managers/
helpers/
common/
infrastructure/
```

without demonstrated ownership need.

## Important ownership changes

### CI

```text
OLD
src/upgradepilot/ci_dependency_exercise.py
src/upgradepilot/workflow_commands.py

NEW
src/upgradepilot/ci/dependency_exercise.py
src/upgradepilot/ci/workflow_commands.py
```

Current CI decision mechanics were inspected after reconciliation.

The following behavior remains materially the same as the learned version:

```text
per-workflow execution/definition/revision/path gates
one-job workflow-command restriction
separate install and package-invocation witness searches
order-blind install/exercise existence test
supported/unresolved command result
existential outer workflow aggregation
no_successful_ci versus unresolved distinction
```

Therefore Units 1–4 do not restart. Only source ownership/path references change.

### Dependency

```text
OLD flat modules
→ NEW dependency/ responsibility package
```

Current owners:

```text
dependency/change.py
→ canonical dependency-change contracts

dependency/analysis.py
→ PR-wide coordination/reconciliation

dependency/requirements.py
→ requirements/constraints extraction

dependency/uv_lock.py
→ uv.lock extraction

dependency/versioning.py
→ dependency release interval / PEP 440 ordering
```

Transition-era `PinnedDependencyChange` runtime compatibility is removed.

### Shared primitives

One precise owner now exists for cross-domain meanings:

```text
PEP 503 package identity
→ package_identity.py

repository-relative POSIX path
→ repository_path.py

GitHub locator/object identity
→ github/identity.py
```

This is consolidation by **identical meaning**, not a generic utility bucket.

### Version methods

The old combined:

```text
packaging_method.py
```

was split because one dependency library did not imply one product responsibility:

```text
dependency/versioning.py
→ dependency release/version semantics

target/python_specifier.py
→ Python-line versus requires-python semantics
```

Learning implication:

> Shared implementation dependency (`packaging`) is not sufficient reason to merge domain responsibilities.

### GitHub acquisition

Provider-specific source responsibilities now live together under `github/` while domain interpretation remains elsewhere.

Examples:

```text
github/repository.py
→ exact repository text acquisition

github/actions.py
→ workflow run/job evidence

github/changelog.py
→ exact-commit changelog-path discovery

github/tag.py
→ exact tag-to-commit resolution
```

### Application versus interface

A new application boundary exists:

```text
CLI input
→ investigate_public_pull_request(...)
→ typed PublicPullRequestInvestigation
→ CLI rendering / exit policy
```

`investigation.py` coordinates provider/domain responsibilities.

`cli.py` should no longer be treated as the sole owner of acquisition, orchestration, and presentation.

This materially changes the later request-to-output learning unit.

### Package root

`upgradepilot.__init__` is intentionally minimal:

```python
__all__ = ()
```

Internal code imports precise owning modules instead of relying on a giant root façade.

Learning implication:

> Convenience re-exports can obscure ownership and accidentally turn internal contracts into an implied public API.

### Architecture as executable contract

`tests/test_source_topology.py` protects:

```text
new responsibility-owner imports work
+
upgradepilot package root stays minimal
+
obsolete flat module paths remain absent
```

This is an important architectural-testing pattern:

> Structure can have executable invariants just like product behavior.

## Product/test boundary changes

```text
tests/
→ active product deterministic regression

experiments/tests/
→ completed Step 6 experiment/harness regression
```

The experiment tests were relocated rather than treated as normal product-runtime tests forever.

This clarifies what each test suite actually proves.

## Current product progression relevant to later learning

At this intake:

```text
Steps 1–5 closed
Step 6 closed with adopt_bounded_extractor
source reconciliation complete and validated
Step 7A exact-commit changelog discovery validated
Step 7B deterministic crossed-release Markdown source windows selected next
```

The accepted Step 6 semantic boundary is narrow, local, and evidence-gated; it is not general model trust.

The Step 7 target flow now includes two deterministic bridges before semantic inference:

```text
trusted exact proposed-tag commit
→ bounded changelog-path discovery
→ exact tagged changelog
→ deterministic crossed-release Markdown source window
→ bounded semantic extractor
→ deterministic support-drop grounding
→ conditional target-Python relevance
```

## Learning-sequence consequence

Do **not** jump from the current CI-reader lesson directly to current product Step 7B.

The learning sequence remains responsibility-based:

```text
finish current CI reader mechanics
→ close CI ownership gaps
→ canonical dependency identity
→ multi-format coordination
→ application/request-to-output orchestration
→ upstream interval/claim/version/target responsibilities
→ live acquisition
→ Step 6 bounded semantic extraction
→ Step 7 deterministic/runtime bridges
```

New implementation progress changes the future learning map, not the demonstrated learning depth.

## Historical-note preservation

Older dated learning notes intentionally retain old source paths such as:

```text
src/upgradepilot/ci_dependency_exercise.py
src/upgradepilot/workflow_commands.py
```

Those paths were correct at the recorded snapshot.

They are not mass-rewritten after ADR-0007.

Current navigation should use the live learning plan and this intake.

## Current exact learning continuation

Current mechanics already covered after the previous durable checkpoint include:

```text
_command_invokes_package(...)
package/normalized candidate set
supported wrappers
leading environment-variable assignment stripping
segment-start matching
whitespace/end token boundary
install/execution ordering is not enforced by the current static reader
```

Continue in current source at:

```text
src/upgradepilot/ci/workflow_commands.py
→ _extract_job_definitions(...)
```

Specifically, continue after locating the plain `jobs:` mapping and recording its indentation, into direct child-job discovery and body slicing.

## Depth statement

The architecture reconciliation has been **introduced and mapped** in this intake.

Do not infer independent architectural ownership yet.

Current demonstrated learning remains strongest in the CI dependency-exercise path; responsibility-based source architecture is currently an introduced cross-cutting mental model that will be reinforced as later units visit their new owners.
