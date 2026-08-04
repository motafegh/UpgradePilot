# UpgradePilot Current Memory

**Last updated:** 2026-08-04  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, selected continuation, and current learning state.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Parent plan:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)
- **Step 6:** closed with disposition `adopt_bounded_extractor` for the narrow support-drop semantic role.
- **Accepted semantic architecture:** ADR-0006 — bounded local support-drop semantic extractor.
- **Accepted source-layout evolution:** ADR-0007 — responsibility-based internal Python packages.
- **Source reconciliation:** **complete and behavior-validated**.
- **Final reconciliation evidence:** [`working-memory/2026-08-04_B2-source-structure-reconciliation-final-acceptance.md`](working-memory/2026-08-04_B2-source-structure-reconciliation-final-acceptance.md)
- **Step 7 runtime plan:** [`plans/B2_TARGET_PYTHON_STEP_7_BOUNDED_EXTRACTOR_RUNTIME_INTEGRATION_PLAN.md`](plans/B2_TARGET_PYTHON_STEP_7_BOUNDED_EXTRACTOR_RUNTIME_INTEGRATION_PLAN.md)
- **Next authorized product increment:** **Step 7B — deterministic crossed-release Markdown source windows**.

The temporary source-reconciliation stop line is removed. Do not interpret that as permission to skip the Step 7 plan's own boundaries.

## Final validated source architecture

Active product source is organized by demonstrated responsibility:

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

The old flat compatibility module layer has been removed. `tests/test_source_topology.py` protects absence of those paths.

`upgradepilot.__init__` is intentionally minimal; internal contracts are imported from their owners.

## Final acceptance evidence

Ali ran the final post-cleanup gate from synchronized WSL `main`.

### Active product regression

```text
Ran 323 tests in 0.061s
OK
```

Command:

```bash
python -m unittest discover -s tests -v
```

### Completed Step 6 experiment regression

```text
Ran 27 tests in 0.004s
OK
```

Command:

```bash
python -m unittest discover -s experiments/tests -v
```

### Entry points

```text
python -m upgradepilot --help: PASS
installed upgradepilot --help: PASS
```

### Worktree

```text
branch up to date with origin/main
nothing to commit, working tree clean
```

## Live public-source regressions after cleanup

### Step 7A changelog discovery

```text
LIVE STEP 7A PROOF: PASS
repository: facelessuser/soupsieve
exact commit: 28108ab805818c832d9568142a99844fd95a0d39
path: docs/src/markdown/about/changelog.md
```

The path was recovered by the generic exact-commit discovery rule without a product path constant.

### Step 5 interval acquisition

The first final-acceptance attempt failed at Git tag lookup with HTTP 401 because `tools/live_s001_upstream_interval_proof.py` inherited an ambient stale/invalid `GITHUB_TOKEN` and sent it to a public endpoint.

This was diagnosed as validation-environment credential contamination, not a source/refactor defect. The proof tool was changed to anonymous public GitHub reads, matching the Step 7A proof policy.

The rerun passed:

```text
LIVE STEP 5 PROOF: PASS
crossed releases: 2.7, 2.8, 2.8.1, 2.8.2, 2.8.3, 2.8.4
resolved commit: 28108ab805818c832d9568142a99844fd95a0d39
changelog path: docs/src/markdown/about/changelog.md
changelog blob SHA: 6f221b7398681a580fa199044b3d3f1e11b55493
changelog bytes: reported=17370, decoded=17370
authority basis: tagged_changelog
GitHub Release bodies admitted: 0
```

No changelog semantics or target-Python relevance were evaluated by this proof.

A stale/invalid shell `GITHUB_TOKEN` may still exist locally. Public proof tools no longer depend on it, but authenticated future runtime work should inspect/fix that credential rather than inheriting it silently.

## Architecture corrections completed during reconciliation

### Dependency

The active dependency flow is:

```text
source-specific extraction
→ ExtractedDependencyVersionChange | DependencyChangeProblem
→ PR-wide comparison
→ DependencyVersionChange | DependencyChangeProblem
```

The transition-era `PinnedDependencyChange` runtime path is removed.

### Shared primitives

One owner now exists for:

```text
PEP 503 package identity        → package_identity.py
repository-relative POSIX path → repository_path.py
GitHub locator/object identity  → github/identity.py
```

### Version methods

The old combined `packaging_method.py` is gone:

```text
dependency/versioning.py   → dependency release interval / PEP 440 ordering
target/python_specifier.py → Python-line vs requires-python semantics
```

### Repository files

One active `RepositoryTextFile` model serves workflow, target, dependency, and changelog text evidence. Runtime acquisition can preserve repository/path/revision/blob/byte/retrieval identity.

### Upstream

Trusted repository identity ends at:

```text
PyPI Source metadata
+ PyPI publisher provenance
→ UpstreamRepositoryEvidence
```

The obsolete `UpstreamReleaseEvidence.claim_state='unresolved_claim'` generation is retired. GitHub release acquisition, interval authority, semantic candidate extraction, deterministic claim grounding, and target relevance remain separate boundaries.

### Application / CLI

```text
CLI input
→ investigate_public_pull_request(...)
→ typed investigation result
→ CLI rendering / exit policy
```

`investigation.py` deliberately still preserves the pre-Step-7 target acquisition order. Step 7E will make target-Python acquisition conditional on a grounded support-drop claim.

## Test topology

`tests/` now means **active product regression**.

`experiments/tests/` means **completed Step 6 experiment/harness regression**.

The seven Step 6 tests were moved, not deleted. Historical experiment source imports were migrated to current product trust modules, and the semantic-corpus path calculation was corrected for the relocation without changing the corpus.

## Reconciliation incident retained

The first broad migration validation failed because new dependency modules imported:

```text
repository_relative_path_parts
```

while the real shared primitive was:

```text
repository_relative_parts
```

Five collection failures shared that one root cause. Every test that loaded past the import chain passed, and Step 7A live behavior also passed, which localized the defect. The mismatch was corrected before continuing.

Full record:
[`working-memory/2026-08-04_B2-source-reconciliation-major-tranche-import-failure-and-corrections.md`](working-memory/2026-08-04_B2-source-reconciliation-major-tranche-import-failure-and-corrections.md)

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

## Step 7 path interpretation after restructuring

The Step 7 plan was written before ADR-0007. Use the current architecture when implementing it:

```text
7A exact-commit changelog discovery:
  src/upgradepilot/github/changelog.py

7B deterministic crossed-release Markdown windows:
  src/upgradepilot/upstream/changelog.py

7C bounded local semantic adapter:
  src/upgradepilot/upstream/support_drop_extractor.py

7E application sequencing:
  src/upgradepilot/investigation.py

CLI presentation:
  src/upgradepilot/cli.py

Existing trust/relevance owners that must not be weakened:
  src/upgradepilot/upstream/claim.py
  src/upgradepilot/upstream/interval.py
  src/upgradepilot/target/relevance.py
```

Do not scaffold future files before their increment actually begins.

## Exact continuation

Resume with **Step 7B — deterministic crossed-release Markdown source windows**.

Step 7B must remain deterministic and semantic-neutral:

```text
trusted crossed-release interval
+ exact tagged changelog
→ exact matching Markdown release sections
→ preserved original lines and offsets
→ complete bounded source window
or explicit unresolved problem
```

Do not begin model runtime integration until the Step 7B deterministic proof obligations are satisfied.

## Learning state

Current exposure includes:

- architecture responsibility vs import wiring;
- provider/domain/application/interface boundaries;
- consumer-first compatibility-shim retirement;
- exact shared-symbol contracts during refactors;
- preserving identifier grammars while centralizing validation;
- one strong exact-revision repository evidence model;
- separating repository identity, release authority, and semantic claim state;
- separating active product regression from historical experiment regression;
- using live regressions to localize structural defects;
- diagnosing broad collection failures that share one root import defect;
- distinguishing ambient authentication failures from product evidence failures.

Current depth: substantial implementation exposure and repeated evidence-driven debugging; no formal mastery assessment has been performed.
