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
- **Current controlling work:** [`plans/B2_SOURCE_CODE_STRUCTURE_RECONCILIATION_PLAN.md`](plans/B2_SOURCE_CODE_STRUCTURE_RECONCILIATION_PLAN.md)
- **Accepted layout evolution:** ADR-0007 — responsibility-based internal Python packages.
- **Feature stop line:** no Step 7B/model-runtime/conditional target-Python capability until source reconciliation passes its final acceptance gate.

## Verified pre-refactor baseline

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

## First broad post-migration validation — failed, diagnosed

Ali's first broad validation after major tranche 1 reported:

```text
focused run: 47 attempted, 3 import errors
full run: Ran 320 tests in 0.059s, FAILED (errors=5)
python -m upgradepilot --help: import failure
```

All failures shared one root cause:

```text
new dependency modules imported:
repository_relative_path_parts

actual shared primitive:
repository_relative_parts
```

The five full-suite collection failures were:

```text
test_cli
test_dependency_analysis
test_exact_requirement_change
test_source_topology
test_step8_source_recognition
```

Every test that loaded past that import chain passed. The live Step 7A proof still passed, showing the GitHub/changelog migration was independent of the dependency symbol-wiring defect.

The mismatch is fixed in the real dependency owners. Full incident history:
[`working-memory/2026-08-04_B2-source-reconciliation-major-tranche-import-failure-and-corrections.md`](working-memory/2026-08-04_B2-source-reconciliation-major-tranche-import-failure-and-corrections.md)

## Current source architecture — implemented, broad revalidation pending

The following paths now own implementation rather than acting as aliases to flat modules:

```text
upgradepilot/github/
  api.py
  identity.py
  pull_request.py
  actions.py
  repository.py
  release.py
  tag.py
  changelog.py

upgradepilot/pypi/
  api.py
  release.py
  provenance.py

upgradepilot/dependency/
  change.py
  requirements.py
  analysis.py
  uv_lock.py
  versioning.py

upgradepilot/ci/
  workflow_commands.py
  dependency_exercise.py

upgradepilot/target/
  python.py
  python_specifier.py
  relevance.py

upgradepilot/upstream/
  repository.py
  interval.py
  interval_evidence.py
  claim.py
```

Source-neutral package-root primitives remain:

```text
json_contract.py
package_identity.py
repository_path.py
```

Application/interface split:

```text
investigation.py  → application sequencing
cli.py            → argparse, environment input, rendering, exit policy
```

## Important intentional contract corrections now implemented

### Legacy dependency extraction removed

The active exact-requirements path no longer routes through:

```text
PinnedDependencyChange
UnsupportedDependencyChange
DependencyChangeResult
extract_pinned_dependency_change(...)
```

The modern flow is:

```text
source-specific extraction
→ ExtractedDependencyVersionChange | DependencyChangeProblem
→ PR-wide comparison
→ DependencyVersionChange | DependencyChangeProblem
```

### Root package façade removed

`upgradepilot.__init__` is intentionally minimal:

```python
__all__ = ()
```

Internal contracts are imported from their owning module.

### `packaging_method.py` responsibilities split

Real owners:

```text
dependency/versioning.py       → dependency release interval + PEP 440 ordering
target/python_specifier.py     → Python X.Y line vs requires-python method
```

The combined flat module is currently only a migration shim.

### Repository-text evidence converged

There is one active `RepositoryTextFile` type. Runtime acquisition populates strong exact-revision evidence:

```text
repository
requested path
returned path
revision
blob SHA
reported byte count
decoded byte count
UTF-8 content
retrieval time
```

The historical `ExactRepositoryTextFile` name is temporarily an alias to this same class, not a second evidence generation. Exact-head workflow/target acquisition now uses the same strict byte-agreement path as dependency/changelog acquisition.

### Old upstream semantic generation retired

The active application no longer uses:

```text
UpstreamSourceResolver
→ UpstreamReleaseEvidence
→ claim_state='unresolved_claim'
```

Trusted repository identity ends at:

```text
PyPI Source metadata
+ PyPI publisher provenance
→ UpstreamRepositoryEvidence
```

GitHub releases, interval authority, semantic candidates, and deterministic claim grounding remain separately owned later boundaries.

### CLI/application split activated

`investigate_public_pull_request(...)` owns current evidence sequencing. `cli.py` calls it and only presents the typed result / maps shell exits.

CLI no longer prints obsolete `Claim state: unresolved_claim` or couples repository identity to one proposed GitHub Release record.

## Migration compatibility still intentionally present

Several old flat source paths currently exist only as compatibility shims pointing **to the new owner**. New implementations do not import the old flat implementation.

Examples:

```text
github_api.py
github_client.py
github_actions.py
github_repository.py
github_release.py
github_tag.py
pypi_api.py
pypi_client.py
pypi_provenance.py
dependency_change.py
dependency_analysis.py
exact_requirement_change.py
uv_lock_change.py
packaging_method.py
target_python.py
target_python_relevance.py
upstream_changelog.py
upstream_interval.py
upstream_interval_acquisition.py
upstream_claim.py
```

These shims are temporary diagnostic/migration aids. Final cleanup after the next broad green run must migrate remaining tests/tools to precise owners and remove obsolete flat paths.

`upstream_source.py` no longer exposes `UpstreamReleaseEvidence` or `claim_state`; it contains only temporary aliases to the new repository-identity generation.

## Step 7A status

The exact-commit changelog-discovery implementation physically lives at:

```text
src/upgradepilot/github/changelog.py
```

The live S001 proof tool imports that owner. The last user-run live proof still passed after the first major tranche.

Do not interpret source reconciliation as Step 7 semantic-runtime progress.

## Immediate validation gate

The current second major tranche has not yet been executed in Ali's WSL checkout. The next action is one broad pull + validation, not another micro-gate.

Required checks:

```text
1. focused architecture/provider/domain/import tests
2. full current tests/ suite
3. python -m upgradepilot --help
4. installed upgradepilot --help
5. live Step 7A proof
6. clean git status + current HEAD
```

If green, perform the final cleanup tranche:

```text
migrate remaining active tests/tools off flat compatibility paths
remove obsolete flat source shims
separate completed Step 6 experiment-harness tests from tests/
run active product suite and experiment suite independently
final stale-name/docstring/import search
final package/console/live Step 7A acceptance proof
```

## Step 6 retained facts

Final bounded extractor evidence remains:

```text
model: gemma-4-e4b-it-ud
contract version: 2
strict oracle: 24 / 25
adoption safety: 25 / 25
all material critical repeats consistent: true
all 10 adoption-gate checks: true
disposition: adopt_bounded_extractor
```

Accepted semantic boundary:

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

Until source reconciliation passes final acceptance, do not begin:

- Step 7B deterministic crossed-release source windows;
- normal-runtime LM Studio semantic client;
- Instructor/Pydantic or automatic retry integration;
- conditional target-Python activation;
- full S001 relevance execution;
- compatibility, safety, merge, defer, or recommendation logic.

## Learning state

Current exposure now includes:

- architecture responsibility vs import wiring;
- provider/domain/application/interface boundaries;
- compatibility shims that point old → new rather than new → old;
- exact shared-symbol contracts during refactors;
- preserving previously proven identifier grammars;
- one strong exact-revision repository evidence model;
- separation of repository identity, release authority, and semantic claim state;
- why a live regression can localize a structural failure;
- why broad collection failures can share one root import defect.

Current depth: substantial implementation exposure and repeated evidence-driven debugging, but no formal mastery assessment and source reconciliation is not yet user-validated complete.
