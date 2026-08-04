# UpgradePilot Current Memory

**Last updated:** 2026-08-04  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, selected continuation, and current learning state.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Parent plan:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)
- **Step 6:** closed with disposition `adopt_bounded_extractor` for the narrow support-drop semantic role.
- **Accepted semantic architecture:** ADR-0006 — bounded local support-drop semantic extractor.
- **Accepted source-layout evolution:** ADR-0007 — responsibility-based internal Python packages and adjacent product/experiment/tool boundaries.
- **Source reconciliation:** **complete and behavior-validated**.
- **Final reconciliation evidence:** [`working-memory/2026-08-04_B2-source-structure-reconciliation-final-acceptance.md`](working-memory/2026-08-04_B2-source-structure-reconciliation-final-acceptance.md)
- **Post-reconciliation governance alignment:** complete; record at [`working-memory/2026-08-04_REPO-GOV_post-reconciliation-artifact-routing-alignment.md`](working-memory/2026-08-04_REPO-GOV_post-reconciliation-artifact-routing-alignment.md).
- **Step 7 runtime plan:** [`plans/B2_TARGET_PYTHON_STEP_7_BOUNDED_EXTRACTOR_RUNTIME_INTEGRATION_PLAN.md`](plans/B2_TARGET_PYTHON_STEP_7_BOUNDED_EXTRACTOR_RUNTIME_INTEGRATION_PLAN.md), aligned to ADR-0007/current source ownership.
- **Next authorized product increment:** **Step 7B — deterministic crossed-release Markdown source windows**.

The temporary source-reconciliation stop line is removed. Do not interpret that as permission to skip the Step 7 plan's own boundaries.

## Repository artifact-routing handoff

Root `AGENTS.md` is the canonical repository-wide artifact-routing owner. File placement is selected by responsibility rather than extension.

```text
PROJECT_CHARTER.md
→ stable mission, user, product boundary, claims

MEMORY.md
→ sole live project position and exact continuation

ENVIRONMENT.md
→ reusable WSL/Python/GPU/LM Studio environment baseline

SECURITY.md
→ stable security/privacy/credential/untrusted-evidence/external-action rules

src/upgradepilot/
→ installable active product runtime

tests/
→ active deterministic product regression

experiments/
→ bounded non-product research/evaluation/comparison/calibration

experiments/tests/
→ regression of experiment/evaluation machinery; not product-runtime coverage

tools/
→ developer-operated diagnostics, live proofs, validation runners, maintenance

plans/
→ position-neutral bounded execution definitions

docs/specifications/
→ stable framework-independent requirements/invariants

docs/architecture/
→ accepted/superseded consequential implementation and structural decisions

working-memory/
→ dated execution/reasoning/public-safe incident evidence

learning/
→ reusable understanding and historical learning snapshots

proposals/
→ substantial ideas not admitted for execution
```

Normal dependency direction:

```text
tests/             → src/upgradepilot/
experiments/       → src/upgradepilot/
experiments/tests/ → experiments/ + src/upgradepilot/
tools/             → src/upgradepilot/
```

Product runtime must not import `tests/`, `experiments/`, or `tools/`.

New `src/upgradepilot/` modules/subpackages require a real product responsibility. New top-level repository directories require a distinct durable artifact responsibility and must be registered in root `AGENTS.md`.

ADR-0001 remains the stable distribution/import/source-root/test-root baseline. ADR-0007 controls responsibility-based internal product packages, precise import ownership, the minimal package-root surface, and product/experiment/tool separation. Earlier flat-path instructions are superseded for path/ownership only; their semantic decisions remain unless separately superseded.

## Security/credential handoff

`SECURITY.md` is the stable owner of credential-use rules.

Public read-only developer validation should use anonymous access unless authentication is part of the selected proof. Ambient tokens must not be consumed silently merely because they exist; authentication failure must remain distinguishable from source absence, malformed evidence, transport failure, and product logic failure.

A stale/invalid shell `GITHUB_TOKEN` may still exist in Ali's local environment. Public proof tools no longer depend on it. If later authenticated runtime work actually requires a token, inspect or replace that credential without exposing its value.

## Governance alignment audit result

The post-reconciliation audit changed only stable owners whose responsibility required alignment:

```text
AGENTS.md
README.md
SECURITY.md
OPERATING_GUIDE.md
plans/README.md
plans/B2_TARGET_PYTHON_STEP_7_BOUNDED_EXTRACTOR_RUNTIME_INTEGRATION_PLAN.md
docs/architecture/README.md
docs/architecture/ADR-0001-initial-python-source-layout.md
docs/architecture/ADR-0007-responsibility-based-python-subpackages.md
```

Audited and intentionally unchanged because their responsibilities remain source-layout-neutral:

```text
PROJECT_CHARTER.md
ENVIRONMENT.md
plans/UPGRADEPILOT_90_DAY_PLAN.md
plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md
docs/specifications/README.md
accepted technical specifications
```

`ENVIRONMENT.md` was intentionally left unchanged because the stale ambient token is freshness-sensitive local state, not a reusable machine baseline. Its general rule belongs to `SECURITY.md` and its observed incident remains dated evidence.

Unselected older plans and dated historical evidence were not mass-rewritten merely to replace former filenames. Root `AGENTS.md`, ADR-0007, active source, and a selected/reconciled bounded plan control future placement.

The governance pass changed documentation only. It did not modify product source, tests, experiments, tools, dependencies, environment configuration, or product evidence semantics; therefore the established runtime acceptance evidence remains applicable without a documentation-only suite rerun.

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

`tests/` means **active product regression**.

`experiments/tests/` means **experiment/evaluation regression** and is reported separately.

The completed Step 6 tests were moved, not deleted. Historical experiment source imports were migrated to current product trust modules, and the semantic-corpus path calculation was corrected for the relocation without changing the corpus.

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

## Step 7 source ownership

The selected Step 7 plan is aligned to ADR-0007 and uses these owners:

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
- responsibility-first artifact routing across product/tests/experiments/tools/docs/security;
- exact shared-symbol contracts during refactors;
- preserving identifier grammars while centralizing validation;
- one strong exact-revision repository evidence model;
- separating repository identity, release authority, and semantic claim state;
- separating active product regression from experiment regression;
- using live regressions to localize structural defects;
- diagnosing broad collection failures that share one root import defect;
- distinguishing ambient authentication failures from product evidence failures.

Current depth: substantial implementation exposure and repeated evidence-driven debugging; no formal mastery assessment has been performed.
