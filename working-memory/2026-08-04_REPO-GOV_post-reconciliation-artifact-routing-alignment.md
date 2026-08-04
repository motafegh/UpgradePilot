# Post-Reconciliation Artifact-Routing and Governance Alignment

**Date:** 2026-08-04  
**Scope:** repository governance/document alignment after the B2 source-structure reconciliation  
**Behavioral scope:** documentation/governance only; no product source, test, dependency, environment, or runtime behavior change

## Purpose

After the responsibility-based Python source reconciliation passed its final acceptance gate, the repository was audited for a different class of defect: whether a future assistant could reliably determine where new product code, tests, experiments, developer tools, plans, specifications, architecture decisions, evidence, learning, and other artifacts belong.

The audit also checked whether accepted ADR navigation, selected plans, route documents, and stable instructions still reflected the responsibility-based source architecture rather than the deleted flat module layout.

## Findings

### 1. Root artifact routing was incomplete

`AGENTS.md` already assigned stable ownership for product source, product tests, plans, specifications, architecture decisions, evidence, learning, proposals, archives, and live state. It did not assign equally explicit repository responsibilities to:

```text
experiments/
experiments/tests/
tools/
```

That omission could force a future assistant to infer their meaning from dated reconciliation records.

### 2. ADR-0007 existed but was missing from architecture navigation

`docs/architecture/ADR-0007-responsibility-based-python-subpackages.md` was accepted and had controlled the source reconciliation, but `docs/architecture/README.md` still ended at ADR-0006.

This was a navigation inconsistency, not a missing architecture decision.

### 3. ADR-0001 and ADR-0007 needed an explicit relationship

ADR-0001 remains valid for:

```text
UpgradePilot repository/distribution/import naming
src/ layout
src/upgradepilot/ installed-product boundary
tests/ as the top-level active product-test root
installed-package testing
non-speculative package admission
```

ADR-0007 later exercised ADR-0001's own stable-subpackage reassessment trigger and evolved only the initial flat internal-module choice.

Without an explicit relationship note, two accepted ADRs could appear to prescribe competing layouts.

### 4. File placement needed a responsibility-first rule

The source reconciliation demonstrated that extension-based routing is incorrect:

```text
.py may be product source, product test, experiment, experiment test, or developer tool
.md may be plan, specification, ADR, working evidence, learning, proposal, archive note, or public orientation
```

The correct classifier is the artifact's owning responsibility.

### 5. The selected Step 7 plan contained pre-ADR-0007 paths

The bounded Step 7 runtime-integration plan still named deleted flat modules in its modification boundary and described sequencing as a CLI responsibility.

The product architecture now has:

```text
7A GitHub changelog discovery
→ src/upgradepilot/github/changelog.py

7B deterministic crossed-release Markdown windows
→ src/upgradepilot/upstream/changelog.py

7C product bounded semantic adapter
→ src/upgradepilot/upstream/support_drop_extractor.py

7E application sequencing
→ src/upgradepilot/investigation.py

CLI arguments/rendering/exit policy
→ src/upgradepilot/cli.py
```

The selected plan therefore required structural alignment before further implementation.

### 6. Older unselected plans and dated records can legitimately contain former paths

Several earlier B2 plans, ADR context sections, learning files, and dated working-memory records mention modules such as:

```text
dependency_change.py
packaging_method.py
upstream_claim.py
```

Those names were factual at the time some evidence was produced. Mass-rewriting historical material would erase useful chronology and make old evidence appear to have been produced under an architecture that did not yet exist.

The governance solution is not a repository-wide terminology rewrite. Instead:

- ADR-0007 controls current internal source ownership;
- root `AGENTS.md` controls repository artifact routing;
- a bounded plan selected for renewed execution must be reconciled with accepted architecture and active source first;
- dated historical evidence retains the names that were true when captured.

## Stable routing model established by the audit

```text
src/upgradepilot/
→ installable active product runtime

tests/
→ active deterministic product regression

experiments/
→ bounded non-product research, evaluation, comparison, and calibration machinery

experiments/tests/
→ regression of experiment/evaluation machinery; not product-runtime coverage

tools/
→ developer-operated diagnostics, live proofs, validation runners, and maintenance utilities

plans/
→ position-neutral bounded execution definitions

docs/specifications/
→ stable framework-independent system requirements/invariants

docs/architecture/
→ accepted/superseded consequential implementation and structural decisions

MEMORY.md
→ sole live project position and exact continuation

ENVIRONMENT.md
→ reusable WSL/Python/GPU/LM Studio environment baseline

working-memory/
→ dated execution/reasoning evidence

learning/
→ reusable understanding and historical learning snapshots

proposals/
→ substantial ideas not admitted for execution

product-simulation/
→ discovery evidence under its local controls

archive/
→ non-controlling historical implementation references

chronicle/
→ informal project story
```

The normal executable dependency direction is:

```text
tests/             → src/upgradepilot/
experiments/       → src/upgradepilot/
experiments/tests/ → experiments/ + src/upgradepilot/
tools/             → src/upgradepilot/
```

The product dependency direction must not reverse:

```text
src/upgradepilot/ -X-> tests/
src/upgradepilot/ -X-> experiments/
src/upgradepilot/ -X-> tools/
```

## New-directory admission rule

A new `src/upgradepilot/` module or subpackage is admitted only when a real implementation responsibility exists and implementation enters it in the same bounded change.

A new top-level repository directory has a higher bar because it changes the artifact taxonomy. It requires a distinct durable responsibility that cannot be owned cleanly by an existing area, and its responsibility must then be registered in root `AGENTS.md`.

Generic or speculative hierarchy such as the following remains rejected without concrete evidence:

```text
services/
repositories/
managers/
adapters/
infrastructure/
common/
utils/
```

A separate `WHERE_FILES_GO.md` was intentionally not created because root `AGENTS.md` is the correct single owner of repository-wide routing.

## Documents changed by this alignment

### `docs/architecture/README.md`

- added ADR-0007 to decision navigation;
- clarified ADR-0001 as the accepted package/source/test-root baseline whose initial flat internal choice was evolved by ADR-0007.

### `docs/architecture/ADR-0001-initial-python-source-layout.md`

- added an explicit evolution section;
- preserved ADR-0001's baseline responsibilities;
- linked the internal-layout reassessment to ADR-0007.

### `docs/architecture/ADR-0007-responsibility-based-python-subpackages.md`

- clarified product/test/experiment/tool boundaries;
- defined dependency direction;
- defined new package/top-level directory admission;
- clarified that old source-path instructions are superseded for path/ownership only while their semantic decisions remain unless separately superseded.

### `AGENTS.md`

- made artifact routing responsibility-first rather than extension-first;
- assigned explicit ownership to `experiments/`, `experiments/tests/`, and `tools/`;
- defined executable dependency direction;
- defined new-directory admission;
- reconciled ADR-0001 versus ADR-0007 authority;
- separated product, experiment, and live-tool validation claims;
- extended document-update routing for product, experiment, and tool changes.

### `README.md`

- added public source/executable-boundary orientation;
- linked ADR-0001 and ADR-0007;
- expanded the ownership table to product source, product tests, experiments, experiment tests, and developer tools.

### `plans/README.md`

- clarified that plans may name expected files but do not own permanent directory hierarchy;
- required a selected older plan to be reconciled with accepted architecture/current source before renewed execution;
- explicitly separated experiment plans under `plans/` from executable experiments under repository-root `experiments/`.

### `plans/B2_TARGET_PYTHON_STEP_7_BOUNDED_EXTRACTOR_RUNTIME_INTEGRATION_PLAN.md`

- added ADR-0007 architecture alignment;
- routed 7A/7B/7C/7E to current owners;
- corrected sequencing ownership from CLI to `investigation.py`;
- kept `cli.py` as presentation/exit policy;
- updated the modification boundary to current product paths;
- explicitly routed product tests, experiment comparisons, experiment regressions, and live proofs to their proper areas;
- prohibited recreating deleted flat compatibility modules.

### `OPERATING_GUIDE.md`

- distinguished product implementation truth, experiment/evaluation truth, and developer live-proof truth;
- added the corresponding document/update ownership rules;
- made explicit that live tools do not replace deterministic product regression.

## Stable owners audited and intentionally unchanged

### `PROJECT_CHARTER.md`

No change required. Mission, supported user/decision, product boundary, evidence doctrine, technology admission, and claim limits are independent of the internal source reorganization.

### `plans/UPGRADEPILOT_90_DAY_PLAN.md`

No change required. The route is expressed in evidence/product responsibilities rather than implementation filenames. B2/B3/B4 gate meanings remain compatible with the responsibility-based source structure.

### `plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`

No structural change required. It defines the semantic/evidence responsibility split and activation order rather than a permanent module map. Its Step 7 implementation details are delegated to the now-aligned bounded Step 7 plan.

### `docs/specifications/README.md` and accepted technical specifications

No source-layout change required. The specification owner explicitly states that specifications define **what the system must represent and guarantee**, not directory hierarchy or selected implementation structure. Adding repository-routing rules there would duplicate `AGENTS.md`/ADR-0007 ownership.

### Completed reconciliation plan and dated historical records

Not rewritten merely to make their historical source names look current. Their dated evidence remains useful for understanding what was planned, implemented, broken, corrected, and validated at each point. Current path authority is supplied by ADR-0007, active source, the selected aligned plan, and root `AGENTS.md`.

## Validation of this governance pass

This pass changed documentation/governance only.

It did not modify:

- `src/upgradepilot/`;
- `tests/`;
- `experiments/` executable code;
- `experiments/tests/`;
- `tools/` executable code;
- `pyproject.toml`;
- runtime dependencies;
- environment configuration;
- product contracts or evidence semantics.

Therefore the previously established 323-product-test, 27-experiment-test, CLI, Step 7A, and Step 5 runtime evidence remains the relevant behavior validation. A full runtime-suite rerun is not justified solely by these documentation edits.

## Result

The repository now has one explicit answer to the future-file-placement question:

> Determine the artifact's responsibility first, then place it in the existing owner. Create a new package/directory only when a real distinct responsibility requires one, and register new top-level ownership in `AGENTS.md`.

That rule applies to code, Markdown, JSON, evidence, tests, experiments, tools, plans, specifications, architecture decisions, and future artifact types.