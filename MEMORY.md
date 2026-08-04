# UpgradePilot Current Memory

**Last updated:** 2026-08-04  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, selected continuation, and current learning state.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Parent plan:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)
- **Step 6:** closed with disposition `adopt_bounded_extractor` for the narrow support-drop semantic role.
- **Accepted semantic architecture:** ADR-0006 — bounded local support-drop semantic extractor.
- **Step 7 runtime plan:** [`plans/B2_TARGET_PYTHON_STEP_7_BOUNDED_EXTRACTOR_RUNTIME_INTEGRATION_PLAN.md`](plans/B2_TARGET_PYTHON_STEP_7_BOUNDED_EXTRACTOR_RUNTIME_INTEGRATION_PLAN.md)
- **Source reconciliation plan:** [`plans/B2_SOURCE_CODE_STRUCTURE_RECONCILIATION_PLAN.md`](plans/B2_SOURCE_CODE_STRUCTURE_RECONCILIATION_PLAN.md)
- **Accepted layout evolution:** ADR-0007 — responsibility-based internal Python packages.
- **Final source cleanup:** implemented remotely; final WSL acceptance gate pending.
- **Final cleanup record:** [`working-memory/2026-08-04_B2-source-structure-final-cleanup.md`](working-memory/2026-08-04_B2-source-structure-final-cleanup.md)
- **Feature stop line:** no Step 7B/model-runtime/conditional target-Python capability until the final structural acceptance gate is green.

## Verified baseline before reconciliation

Before source migration Ali reported:

```text
Ran 353 tests in 0.077s
OK
```

and:

```text
LIVE STEP 7A PROOF: PASS
path: docs/src/markdown/about/changelog.md
```

Durable baseline:
[`working-memory/2026-08-04_B2-source-structure-reconciliation-baseline.md`](working-memory/2026-08-04_B2-source-structure-reconciliation-baseline.md)

## Reconciliation incident retained

The first broad validation after major tranche 1 failed because new dependency modules imported the nonexistent symbol:

```text
repository_relative_path_parts
```

while the shared owner actually exposed:

```text
repository_relative_parts
```

Five full-suite collection failures shared that one cause. Every test that loaded past the import chain passed, and the Step 7A live changelog proof still passed, which localized the defect away from the GitHub/changelog boundary.

The mismatch was corrected before the second tranche proceeded. Full incident record:
[`working-memory/2026-08-04_B2-source-reconciliation-major-tranche-import-failure-and-corrections.md`](working-memory/2026-08-04_B2-source-reconciliation-major-tranche-import-failure-and-corrections.md)

## Final active product source topology

The flat transition layer has been removed. Active product source is now organized by demonstrated responsibility:

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
│   ├── __init__.py
│   ├── dependency_exercise.py
│   └── workflow_commands.py
├── dependency/
│   ├── __init__.py
│   ├── analysis.py
│   ├── change.py
│   ├── requirements.py
│   ├── uv_lock.py
│   └── versioning.py
├── github/
│   ├── __init__.py
│   ├── actions.py
│   ├── api.py
│   ├── changelog.py
│   ├── identity.py
│   ├── pull_request.py
│   ├── release.py
│   ├── repository.py
│   └── tag.py
├── pypi/
│   ├── __init__.py
│   ├── api.py
│   ├── provenance.py
│   └── release.py
├── target/
│   ├── __init__.py
│   ├── python.py
│   ├── python_specifier.py
│   └── relevance.py
└── upstream/
    ├── __init__.py
    ├── claim.py
    ├── interval.py
    ├── interval_evidence.py
    └── repository.py
```

No future Step 7 modules were scaffolded early.

## Removed flat module layer

The following transition modules no longer exist:

```text
ci_dependency_exercise.py
dependency_analysis.py
dependency_change.py
exact_requirement_change.py
github_actions.py
github_api.py
github_client.py
github_release.py
github_repository.py
github_tag.py
packaging_method.py
pypi_api.py
pypi_client.py
pypi_provenance.py
target_python.py
target_python_relevance.py
upstream_changelog.py
upstream_claim.py
upstream_interval.py
upstream_interval_acquisition.py
upstream_source.py
uv_lock_change.py
workflow_commands.py
```

`tests/test_source_topology.py` now requires all of these old import paths to remain absent.

## Important architecture after cleanup

### Dependency

The modern flow is:

```text
source-specific extraction
→ ExtractedDependencyVersionChange | DependencyChangeProblem
→ PR-wide comparison
→ DependencyVersionChange | DependencyChangeProblem
```

The legacy `PinnedDependencyChange` runtime architecture is not active.

### GitHub / PyPI

Provider-specific acquisition lives under `upgradepilot.github` and `upgradepilot.pypi`.
Shared identity/path mechanics do not depend on unrelated provider clients.

### Version methods

The old combined `packaging_method.py` is gone:

```text
dependency/versioning.py
→ dependency release interval + PEP 440 ordering

target/python_specifier.py
→ Python X.Y line vs requires-python semantics
```

### Repository file evidence

One active `RepositoryTextFile` evidence model serves workflows, target metadata, dependency files, and changelogs. Runtime acquisition can preserve:

```text
repository
requested path
returned path
immutable revision
blob SHA
reported byte count
decoded byte count
UTF-8 content
retrieval timestamp
```

A few older type-name aliases may remain inside the real owning module. They do not create duplicate implementation files and are not part of the source-topology problem.

### Upstream

Trusted repository identity ends at:

```text
PyPI Source metadata
+ PyPI publisher provenance
→ UpstreamRepositoryEvidence
```

GitHub releases, interval authority, semantic candidates, and deterministic claim grounding are independently owned boundaries. The obsolete `UpstreamReleaseEvidence.claim_state='unresolved_claim'` generation is retired.

### Application / CLI

```text
investigation.py
→ application sequencing

cli.py
→ arguments, environment input, rendering, exit policy
```

The CLI no longer constructs the entire evidence graph itself.

## Product tests and experiment tests are now separate

Active product regression:

```bash
python -m unittest discover -s tests -v
```

Completed Step 6 experiment/harness regression:

```bash
python -m unittest discover -s experiments/tests -v
```

The seven Step 6 harness/evaluation tests were moved rather than deleted. Experiment source was also migrated to current product trust imports, so historical evaluation machinery does not require removed flat modules.

The semantic-corpus test's repository-relative path calculation was adjusted for its new directory; the corpus itself was not changed.

## Tools

The Step 7A changelog-discovery proof already imports `upgradepilot.github.changelog`.

`tools/live_s001_upstream_interval_proof.py` now imports only current provider/domain owners. It is public/read-only network validation and does not call LM Studio.

Step 6 runner tools remain historical experiment launchers, not product runtime.

## Generated local artifacts

`__pycache__/`, `*.py[cod]`, and `*.egg-info/` are ignored generated artifacts. They can still appear in a local `tree` command and do not represent repository source architecture.

`tools/` remains the developer/live-validation executable convention. An empty local `scripts/__pycache__/` does not establish a second script boundary.

## Final acceptance gate — exact next action

The final topology is implemented remotely but must not be called behavior-validated until Ali runs this from a clean synchronized WSL checkout:

```bash
git pull --ff-only origin main

python -m unittest discover -s tests -v
python -m unittest discover -s experiments/tests -v

python -m upgradepilot --help
upgradepilot --help

python tools/live_s001_changelog_discovery_proof.py
python tools/live_s001_upstream_interval_proof.py

git status
git log -1 --oneline
```

No LM Studio call is required for this structural acceptance gate.

A useful final tree view is:

```bash
tree src/upgradepilot tests experiments \
  -I "__pycache__|*.pyc|*.egg-info|*.md|*.json|*.txt"
```

If the gate is green, mark source reconciliation behavior-validated and resume Step 7B deterministic crossed-release source-windowing.

## Step 6 retained facts

```text
model: gemma-4-e4b-it-ud
contract version: 2
strict oracle: 24 / 25
adoption safety: 25 / 25
all material critical repeats consistent: true
all 10 adoption-gate checks: true
disposition: adopt_bounded_extractor
```

Accepted semantic boundary remains:

```text
LM Studio localhost HTTP
+ gemma-4-e4b-it-ud
+ contract v2
+ temperature 0
+ seed 0
+ automatic retries disabled
+ deterministic exact-source reconstruction
+ mandatory validate_support_drop_candidates(...)
```

This is not general model trust.

## Stop line

Until the final source acceptance gate passes, do not begin:

- Step 7B deterministic crossed-release source windows;
- normal-runtime LM Studio semantic client;
- Instructor/Pydantic or automatic retry integration;
- conditional target-Python activation;
- full S001 relevance execution;
- compatibility, safety, merge, defer, or recommendation logic.

## Learning state

Current exposure includes:

- architecture responsibility vs import wiring;
- provider/domain/application/interface boundaries;
- consumer-first compatibility-shim retirement;
- exact shared-symbol contracts during refactors;
- preserving previously proven identifier grammars;
- one strong exact-revision repository evidence model;
- separating repository identity, release authority, and semantic claim state;
- separating active product regression from historical experiment-harness regression;
- why live regressions help localize structural failures;
- why broad collection failures can share one root import defect.

Current depth: substantial implementation exposure and repeated evidence-driven debugging, but no formal mastery assessment. Final source reconciliation behavior validation is still pending.
