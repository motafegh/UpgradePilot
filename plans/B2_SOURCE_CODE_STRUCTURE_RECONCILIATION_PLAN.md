# B2 Source-Code Structure Reconciliation Plan

**Status:** Bounded source-architecture reconciliation plan  
**Route:** B2 — Public PR vertical slice  
**Architectural baseline:** [`../docs/architecture/ADR-0001-initial-python-source-layout.md`](../docs/architecture/ADR-0001-initial-python-source-layout.md)  
**Naming control:** [`../docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md)  
**Related continuation:** [`B2_TARGET_PYTHON_STEP_7_BOUNDED_EXTRACTOR_RUNTIME_INTEGRATION_PLAN.md`](B2_TARGET_PYTHON_STEP_7_BOUNDED_EXTRACTOR_RUNTIME_INTEGRATION_PLAN.md)

## 1. Purpose

Reconcile the active Python source, test, experiment, and developer-tool structure after the B2 implementation has accumulated enough real responsibilities to justify stable internal package boundaries.

The plan is not a feature-development increment. Its purpose is to make the already implemented system easier to understand, test, extend, and own before the Step 7 bounded semantic extractor is moved into normal runtime.

The work must address structural inconsistencies that arose naturally during incremental implementation:

1. the flat `src/upgradepilot/` package now mixes provider, domain, method, and application naming dimensions;
2. `upgradepilot.__init__` exposes a very large accidental package-level API;
3. active dependency extraction still routes through transition-era `PinnedDependencyChange` compatibility code;
4. repository-relative path validation is duplicated across active modules;
5. PEP 503 package-name normalization is owned by `dependency_change.py` even though several domains depend on it;
6. GitHub repository and immutable-commit identity validation are scattered across unrelated clients;
7. `upstream_changelog.py` performs GitHub Git-object acquisition/discovery despite being named as an upstream-domain module;
8. `upstream_interval_acquisition.py` is pure evidence composition despite its acquisition name;
9. `packaging_method.py` groups unrelated dependency-version and target-Python responsibilities merely because both use the `packaging` library;
10. `github_repository.py` contains two generations of repository-text evidence contracts;
11. the older `UpstreamSourceResolver` / `UpstreamReleaseEvidence.claim_state='unresolved_claim'` path overlaps conceptually with the newer interval-authority and grounded-claim architecture;
12. `cli.py` owns client construction, orchestration, sequencing, and presentation in one file;
13. active source comments/docstrings contain stale module names and obsolete data-flow descriptions;
14. comment density and educational style vary materially between older and newer modules;
15. active product tests and historical Step 6 experiment-harness tests share one `tests/` root despite proving different things;
16. generated local artifacts such as `__pycache__`, `*.egg-info`, and an empty `scripts/` tree can obscure the intended executable/source boundaries even though they are ignored by Git.

The plan must fix these issues without using the cleanup as a pretext to broaden B2 capability.

---

## 2. Why reconciliation is justified now

ADR-0001 deliberately rejected speculative subpackages and said cohesive initial modules should remain directly under `src/upgradepilot/` until implemented responsibilities demonstrated stable boundaries.

Its reassessment triggers explicitly include:

- implemented modules demonstrating a stable subpackage boundary;
- a real CLI changing the package boundary;
- testing or deployment exposing a concrete limitation.

Those triggers are now satisfied by actual source:

```text
GitHub acquisition family
PyPI acquisition family
dependency-evidence family
CI interpretation family
upstream authority/claim family
target-Python family
CLI/application orchestration
completed Step 6 experiment family
```

The migration therefore evolves ADR-0001 according to its own admission rule. It does not introduce an abstract layered architecture such as `services/`, `repositories/`, `managers/`, `adapters/`, or `infrastructure/` without demonstrated need.

Before the first source move, record the accepted durable subpackage decision in a new ADR that supersedes only ADR-0001's *flat internal-module* choice while retaining:

```text
src/ layout
upgradepilot distribution/import namespace
tests as active product-test root
no speculative package scaffolding
```

The ADR should be created only after the synchronized baseline has been revalidated.

---

## 3. Non-negotiable invariants

### 3.1 No hidden feature work

This reconciliation must not implement:

- Step 7B Markdown source windows;
- the normal-runtime LM Studio model client;
- support-drop runtime inference;
- conditional target-Python activation;
- new compatibility, safety, merge, defer, or recommendation behavior;
- target-repository mutation;
- automatic retries;
- Instructor/Pydantic adoption;
- new package/source formats;
- arbitrary source discovery or ranking.

Step 7A behavior may be moved and renamed but must not be broadened.

### 3.2 Preserve semantic trust boundaries

Structural moves must not weaken:

```text
complete changed-file acquisition
exact immutable Git revision identity
exact dependency-version evidence
upstream interval authority
Step 2 support-drop grounding
CI dependency-exercise proof boundary
target-Python relevance boundary
explicit unresolved/abstention behavior
```

### 3.3 No compatibility baggage without a real consumer

UpgradePilot is still version `0.0.0` and has no established external library API commitment. Internal transition wrappers should not be retained solely because tests once imported them.

Before deleting a compatibility symbol, search active product source, active product tests, tools, and experiment code. Preserve compatibility only if a concrete active consumer requires it and the migration cannot be completed in the same bounded cluster.

### 3.4 No generic junk-drawer modules

Do not create:

```text
utils.py
helpers.py
common.py
misc.py
manager.py
service.py
```

merely to reduce duplicate lines.

A shared primitive is admitted only when the meaning is genuinely identical across its callers and its owner can be named precisely.

### 3.5 No empty scaffolds

Create a package/module only when the same migration cluster moves or implements its real responsibility. Do not pre-create future Step 7 files such as `upstream/changelog.py` or `upstream/support_drop_extractor.py` before their capability exists.

### 3.6 Historical evidence stays historical

Do not mass-rewrite dated working-memory, learning snapshots, archived records, or committed JSON evidence merely because active module names change. Those records should continue to describe the source paths/names that existed when the evidence was captured.

Update historical material only for a broken functional link or factual corruption, not terminology synchronization.

### 3.7 Validation after every cluster

Each migration cluster must run:

```text
narrow tests for the changed responsibility
+ import/package smoke where relevant
+ complete active product deterministic suite
```

Do not stack several unvalidated structural clusters and debug them together.

---

## 4. Target product source topology

The end-of-reconciliation product source should communicate the architecture directly:

```text
src/
└── upgradepilot/
    ├── __init__.py
    ├── __main__.py
    ├── cli.py
    ├── investigation.py
    ├── json_contract.py
    ├── package_identity.py
    ├── repository_path.py
    │
    ├── dependency/
    │   ├── __init__.py
    │   ├── change.py
    │   ├── analysis.py
    │   ├── requirements.py
    │   ├── uv_lock.py
    │   └── versioning.py
    │
    ├── github/
    │   ├── __init__.py
    │   ├── api.py
    │   ├── identity.py
    │   ├── pull_request.py
    │   ├── actions.py
    │   ├── repository.py
    │   ├── release.py
    │   ├── tag.py
    │   └── changelog.py
    │
    ├── pypi/
    │   ├── __init__.py
    │   ├── api.py
    │   ├── release.py
    │   └── provenance.py
    │
    ├── ci/
    │   ├── __init__.py
    │   ├── workflow_commands.py
    │   └── dependency_exercise.py
    │
    ├── upstream/
    │   ├── __init__.py
    │   ├── repository.py
    │   ├── interval.py
    │   ├── interval_evidence.py
    │   └── claim.py
    │
    └── target/
        ├── __init__.py
        ├── python.py
        ├── python_specifier.py
        └── relevance.py
```

This tree is the intended *end state for responsibilities that already exist*. It is not permission to add empty files.

Future Step 7 responsibilities may later justify:

```text
upstream/changelog.py
upstream/support_drop_extractor.py
```

but those files must appear only when Step 7B/7C actually implements them.

### Architectural reading of the target tree

```text
GitHub
├── HTTP/JSON mechanics
├── GitHub identity rules
├── PR identity + changed files
├── Actions evidence
├── exact repository files
├── releases
├── tags
└── exact-commit changelog discovery

PyPI
├── bounded JSON mechanics
├── release + release-index evidence
└── publisher provenance

Dependency
├── canonical dependency-change contracts
├── PR-wide source coordination
├── exact requirements extraction
├── uv.lock extraction
└── dependency-version semantics

Upstream
├── trusted upstream repository identity
├── interval authority contracts
├── acquired-evidence composition
└── deterministic claim grounding

CI
├── bounded workflow-command reading
└── dependency-exercise evaluation

Target
├── target Python declaration
├── requires-python/Python-line method
└── target relevance

Application
└── one public-PR investigation orchestration

Interface
└── CLI argument/output/exit policy
```

---

## 5. Source migration map

The expected active-file mapping is:

| Existing | Target | Main reason |
|---|---|---|
| `github_api.py` | `github/api.py` | GitHub provider mechanics |
| `github_client.py` | `github/pull_request.py` plus identity extraction | It owns PR/changed-file acquisition, not generic GitHub reading |
| `github_actions.py` | `github/actions.py` | GitHub Actions source boundary |
| `github_repository.py` | `github/repository.py` | immutable repository-file evidence |
| `github_release.py` | `github/release.py` | exact GitHub Release evidence |
| `github_tag.py` | `github/tag.py` | exact Git tag/commit identity |
| `upstream_changelog.py` | `github/changelog.py` | implementation is GitHub Git-object path discovery |
| `pypi_api.py` | `pypi/api.py` | PyPI transport mechanics |
| `pypi_client.py` | `pypi/release.py` | exact release + release-index acquisition |
| `pypi_provenance.py` | `pypi/provenance.py` | PyPI Integrity provenance |
| `dependency_change.py` | `dependency/change.py` | canonical dependency contracts/comparison |
| `dependency_analysis.py` | `dependency/analysis.py` | PR-wide dependency-source coordination |
| `exact_requirement_change.py` | `dependency/requirements.py` | requirements/constraints extraction |
| `uv_lock_change.py` | `dependency/uv_lock.py` | uv.lock extraction |
| dependency-version part of `packaging_method.py` | `dependency/versioning.py` | PEP 440 dependency-release ordering |
| `workflow_commands.py` | `ci/workflow_commands.py` | bounded workflow command interpretation |
| `ci_dependency_exercise.py` | `ci/dependency_exercise.py` | CI dependency-exercise evidence |
| `upstream_source.py` | reconcile into `upstream/repository.py` | preserve only trusted upstream-repository responsibility |
| `upstream_interval.py` | `upstream/interval.py` | interval authority contracts |
| `upstream_interval_acquisition.py` | `upstream/interval_evidence.py` | pure selection/composition, not acquisition |
| `upstream_claim.py` | `upstream/claim.py` | deterministic semantic trust admission |
| `target_python.py` | `target/python.py` | exact target Python declaration |
| target-Python part of `packaging_method.py` | `target/python_specifier.py` | Python-line/specifier method |
| `target_python_relevance.py` | `target/relevance.py` | bounded target comparison |
| orchestration portion of `cli.py` | `investigation.py` | application sequencing |
| argument/output portion of `cli.py` | remains `cli.py` | CLI interface policy |

`json_contract.py` remains at package root because it is genuinely source-neutral structured-value validation shared by provider families.

---

## 6. Migration sequence

### Cluster 0 — synchronize and freeze the baseline

Before source edits:

1. make local `main` exactly follow `origin/main` while preserving any blocking untracked file outside the worktree first;
2. verify `git status` is clean;
3. record the exact baseline commit;
4. run the active deterministic product suite;
5. run the Step 7A focused tests that already exist remotely;
6. run the Step 7A live S001 changelog-discovery proof if the deterministic tests pass;
7. do not alter architecture while baseline validation is failing.

The baseline run distinguishes pre-existing failures from refactor regressions.

### Cluster 1 — record the subpackage architecture decision

Create one ADR that:

- states that ADR-0001's reassessment trigger has been reached;
- preserves the `src/upgradepilot/` package boundary;
- accepts responsibility-based subpackages only for demonstrated clusters;
- rejects speculative layered architecture;
- defines precise-import preference over a large root façade;
- defines `tests/` as active product tests only;
- keeps completed experiment machinery outside `src/`;
- records no feature or dependency change.

No source move happens before this decision is recorded.

### Cluster 2 — establish true shared identity/path primitives

Create only the shared primitives already proven to have identical meaning:

#### `package_identity.py`

Move PEP 503 distribution-name normalization out of `dependency_change.py`.

Required rule:

```text
package spelling
→ lowercase
→ collapse runs of -, _, . into '-'
→ normalized distribution identity
```

All dependency, PyPI, and upstream callers import the same owner.

#### `repository_path.py`

Centralize source-neutral repository-relative POSIX path validation currently duplicated in requirements, uv.lock, dependency analysis, and GitHub/file-discovery code where the semantics are actually identical.

Do not force a source-specific path rule into this primitive. Provider-specific constraints such as `.github/workflows/` remain with their source owner.

#### `github/identity.py`

Centralize GitHub-specific locator/object identity:

```text
validate_repository(...)
validate_commit_sha(...)
```

Only exact identity syntax belongs here. Network acquisition and authority do not.

Validation gate:

- focused shared-primitive tests;
- duplicate active implementations removed or explicitly justified;
- full product suite green.

### Cluster 3 — migrate the GitHub provider boundary

Move GitHub modules under `upgradepilot.github` and repair imports without changing acquisition semantics.

Target modules:

```text
github/api.py
github/identity.py
github/pull_request.py
github/actions.py
github/repository.py
github/release.py
github/tag.py
github/changelog.py
```

Key corrections:

- rename `GitHubReadClient` to a name that exposes its actual PR responsibility, preferably `GitHubPullRequestClient`;
- move `PullRequestIdentity` and `ChangedFile` with that PR boundary;
- make release/tag/repository/changelog modules depend on `github.identity`, not the PR client merely for locator validation;
- move Step 7A `GitHubChangelogPathClient` to `github/changelog.py`;
- reuse one immutable commit-ID validator;
- retain `GitHubApiClient` as the provider-neutral-within-GitHub HTTP/JSON base;
- keep endpoint-specific failure meaning in focused clients.

Do not yet change repository-file evidence shapes in this cluster. Move first, converge later.

Validation gate:

- all GitHub focused tests;
- Step 7A changelog tests;
- package/import smoke;
- complete product suite.

### Cluster 4 — migrate the PyPI provider boundary

Move:

```text
pypi_api.py        → pypi/api.py
pypi_client.py     → pypi/release.py
pypi_provenance.py → pypi/provenance.py
```

Preserve:

- bounded streamed-body acquisition;
- endpoint-specific HTTP state meaning;
- exact release identity;
- release-index raw-version preservation;
- Integrity API provenance semantics.

Update imports to `package_identity.normalize_package_name`.

No PyPI behavior or source-authority decision changes in this cluster.

Validation gate:

- all PyPI focused tests;
- external-contract adapter tests if they cover these boundaries;
- complete product suite.

### Cluster 5 — reconcile the dependency package and remove legacy extraction

Create:

```text
dependency/change.py
dependency/analysis.py
dependency/requirements.py
dependency/uv_lock.py
```

#### Canonical contract cleanup

Keep the modern flow:

```text
source-specific extraction
→ ExtractedDependencyVersionChange | DependencyChangeProblem
→ compare extracted results
→ DependencyVersionChange | DependencyChangeProblem
```

Apply the accepted naming specification while the contracts are already moving. Prefer:

```text
DependencyChangeSourceEvidence
DependencyChangeProblem
```

over transition-era or less direct names when migration remains local and mechanically testable.

#### Remove transition-era active path

Delete from active product architecture after all active consumers are migrated:

```text
PinnedDependencyChange
UnsupportedDependencyChange
DependencyChangeResult
extract_pinned_dependency_change(...)
_LEGACY_PROBLEM_CODES
_extract_legacy_pinned_dependency_change(...)
```

Rewrite `extract_exact_requirement_changes(...)` to directly parse one admitted changed file and return the modern file-level result. Preserve the already validated exact-pin rules:

- complete patch evidence;
- exactly one removed and one added exact pin;
- same file;
- supported file status;
- normalized package identity equality;
- version actually changed;
- explicit problem result on ambiguity/incompleteness.

Do not keep a legacy parser merely to reduce code-edit size.

#### Source recognition ownership

Keep requirements/constraints path admission with `dependency/requirements.py`.

Keep uv.lock path/status admission with `dependency/uv_lock.py`.

`dependency/analysis.py` coordinates source formats; it should not own duplicate path grammars.

Validation gate:

- exact-requirement tests rewritten against the modern contract;
- uv.lock tests;
- dependency comparison/analysis tests;
- explicit search confirms no active product/test import of removed legacy types;
- complete product suite.

### Cluster 6 — separate CI responsibilities

Move:

```text
workflow_commands.py      → ci/workflow_commands.py
ci_dependency_exercise.py → ci/dependency_exercise.py
```

Preserve the important split:

```text
exact workflow text
→ bounded visible-command reading
→ command evidence

command evidence + successful exact-head run/job evidence
→ dependency-exercise evaluation
```

Correct stale source comments that still refer to `PinnedDependencyChange` or `ci_authority.py`.

Do not broaden the shallow YAML/shell grammar during this move.

Validation gate:

- workflow-command tests;
- CI dependency-exercise tests;
- complete product suite.

### Cluster 7 — split `packaging_method.py` by domain responsibility

Do not organize domain code around a third-party library name.

Move dependency release/version behavior to:

```text
dependency/versioning.py
```

including:

```text
ParsedDependencyReleaseInterval
OrderedCrossedReleaseVersions
PackagingVersionProblem
parse_dependency_release_interval(...)
order_crossed_release_versions(...)
```

Move Python-line/`requires-python` behavior to:

```text
target/python_specifier.py
```

including:

```text
PythonLineSpecifierEvaluation
PythonLineSpecifierProblem
evaluate_python_line_specifier(...)
```

The `packaging` dependency remains an implementation detail used by both modules.

Delete `packaging_method.py` after imports/tests migrate.

Validation gate:

- packaging/version tests split according to ownership;
- target specifier tests;
- interval-selection and target-relevance callers compile/import from new owners;
- complete product suite.

### Cluster 8 — migrate target-Python domain modules

Move:

```text
target_python.py           → target/python.py
target_python_relevance.py → target/relevance.py
```

Normalize the successful-state construction pattern so `TargetPythonDeclaration.state == 'available'` is derived/defaulted rather than requiring callers to pass a constant value manually, matching other successful evidence records.

Preserve the semantic split:

```text
exact pyproject.toml
→ target Python declaration

trusted support-drop claim + target declaration
→ Python-line relevance
```

Do not change Step 7 activation order here. The orchestration change still belongs to the later Step 7 runtime-integration plan.

Validation gate:

- target Python interpretation tests;
- target Python relevance tests;
- complete product suite.

### Cluster 9 — migrate upstream authority and claim modules

Move:

```text
upstream_interval.py             → upstream/interval.py
upstream_interval_acquisition.py → upstream/interval_evidence.py
upstream_claim.py                → upstream/claim.py
```

The rename from `interval_acquisition` to `interval_evidence` must reflect actual behavior: this code is pure selection/composition from already acquired evidence.

Preserve:

- old-exclusive/proposed-inclusive interval identity;
- crossed-release evidence;
- tagged-changelog evidence composition;
- source-authority rules;
- exact claim grounding;
- all explicit claim problem states.

Do not put model calls into `upstream/claim.py`. Deterministic trust admission remains pure.

Validation gate:

- interval authority tests;
- interval evidence/acquisition-composition tests;
- claim and claim-edge tests;
- complete product suite.

### Cluster 10 — converge repository-text evidence contracts

After GitHub and downstream modules have stable package locations, reconcile:

```text
RepositoryTextFile
ExactRepositoryTextFile
RepositoryFileEvidence
ExactRepositoryFileEvidence
```

into one strong exact-revision text-evidence model used consistently by:

```text
workflow definitions
pyproject.toml
uv.lock
upstream changelog
other admitted exact repository text
```

The strong contract must retain at least:

```text
repository
requested path
returned path
immutable revision
blob SHA
reported byte count
decoded byte count
UTF-8 content
retrieval time
```

Unavailability must remain distinguishable from an empty file.

Migration rule:

- strengthen older workflow/target callers to consume the strong contract;
- do not create a weaker compatibility view unless a concrete active consumer proves it necessary;
- keep source-authority semantics downstream; exact file evidence proves identity/acquisition, not meaning.

Because this cluster intentionally strengthens evidence validation, classify any changed outcome explicitly rather than calling it a pure rename.

Validation gate:

- exact repository-file tests;
- workflow file tests;
- target Python tests;
- uv.lock tests;
- tagged-changelog tests;
- complete product suite.

### Cluster 11 — reconcile the old upstream-source architecture

The old `UpstreamSourceResolver` currently combines several facts:

```text
PyPI Source candidate
+ PyPI publisher provenance
+ proposed GitHub Release
→ UpstreamReleaseEvidence
→ claim_state='unresolved_claim'
```

The newer architecture has explicit owners for:

```text
trusted upstream repository identity
crossed-release interval
source authority
grounded semantic claim
```

Reconcile the old path rather than maintaining two semantic generations.

#### New narrow upstream-repository responsibility

Create `upstream/repository.py` around one question:

> Do PyPI project metadata and PyPI-reported publisher provenance establish one trusted GitHub repository identity for this package release?

Expected result family:

```text
UpstreamRepositoryEvidence
UpstreamRepositoryProblem
```

The repository result should preserve the evidence needed to explain why the identity was admitted, but it must not contain a semantic claim state.

#### Remove fake semantic state

Retire:

```text
UpstreamReleaseEvidence.claim_state = 'unresolved_claim'
```

because semantic claim resolution now belongs exclusively to the Step 2/Step 6 claim path.

#### Separate GitHub Release evidence

`github/release.py` continues to own exact GitHub Release acquisition. Release bodies may later contribute to interval authority, but upstream-repository identity must not require one proposed-version release object merely to exist as a combined record.

This cluster may intentionally change CLI wording that exposes the obsolete `Claim state: unresolved_claim` line. That is a conceptual correction, not a new product capability.

Validation gate:

- upstream repository identity/provenance tests;
- GitHub release tests independently remain green;
- no active source exposes the obsolete semantic `unresolved_claim` state;
- complete product suite.

### Cluster 12 — separate application orchestration from CLI presentation

Create `investigation.py` for the application responsibility:

> perform one read-only public-PR evidence investigation using the already defined source/domain boundaries.

Move out of `cli.py`:

- client construction/coordination;
- PR acquisition sequencing;
- dependency-analysis invocation;
- target/CI/package/upstream sequencing that already exists before Step 7;
- construction of one explicit investigation result.

Keep in `cli.py`:

- `argparse` configuration;
- environment-to-application input such as optional GitHub token lookup;
- user-facing console rendering;
- exit-status policy.

The structure should become:

```text
CLI input
→ investigation orchestration
→ typed investigation result
→ CLI presentation
```

Do not implement the Step 7 conditional target-Python activation in this cluster. Preserve the pre-Step-7 execution order so structural reconciliation can be distinguished from feature integration.

Prefer a concrete `investigate_public_pull_request(...)`-style entry point or equally clear responsibility name. Do not introduce a generic service/container/factory framework merely for dependency injection.

Validation gate:

- investigation orchestration tests;
- CLI tests focused on argument/output/exit policy;
- `python -m upgradepilot` smoke;
- installed `upgradepilot` console-script smoke;
- complete product suite.

### Cluster 13 — shrink the root package API

After active internal imports have moved to precise module owners, simplify `upgradepilot/__init__.py`.

The package root should no longer re-export dozens of internal:

```text
clients
problem-state aliases
provider records
constants
legacy compatibility types
internal helper functions
```

Preferred baseline:

- package documentation;
- only genuinely intentional package metadata or a very small explicitly justified public surface.

Internal product code, tests, tools, and experiments should import from the owning module/subpackage.

Replace the existing package-interface test that protects the large façade with tests that protect:

```text
import upgradepilot succeeds
import causes no network activity
intentional package metadata/surface only
console/package entry points remain valid
```

Validation gate:

- repository search for accidental root imports;
- package import smoke;
- console entry point smoke;
- complete product suite.

### Cluster 14 — separate active product tests from completed experiments

`AGENTS.md` defines:

```text
tests/ — active product tests only
```

Move Step 6 experiment-harness tests out of the active product test root.

Recommended experiment organization:

```text
experiments/
└── step6_support_drop/
    ├── __init__.py                 # only if required for reliable module imports
    ├── step6_support_drop_smoke.py
    ├── step6_support_drop_evaluation.py
    ├── step6_support_drop_contract_v2.py
    ├── step6_support_drop_contract_v2_replay.py
    ├── step6_support_drop_contract_v2_live_evaluation.py
    ├── step6_support_drop_contract_v2_assessment.py
    ├── step6_support_drop_semantic_corpus.json
    └── tests/
        └── experiment-harness tests
```

The exact historical filenames may be retained inside the directory to preserve traceability. Update executable wrappers/imports but do not rewrite historical evidence documents to pretend the new path existed when old runs occurred.

After this cluster:

```bash
python -m unittest discover -s tests -v
```

must mean **active product regression suite**.

A separate explicit command may validate completed experiment machinery when needed, for example:

```bash
python -m unittest discover -s experiments/step6_support_drop/tests -v
```

Do not count the experiment suite as product-runtime coverage.

Validation gate:

- active product suite green;
- experiment suite green independently;
- Step 6 tools still resolve their experiment modules;
- no `src/upgradepilot` import depends on `experiments`.

### Cluster 15 — normalize developer executable structure and generated artifacts

Keep `tools/` as the one project convention for developer/live-validation executables.

Do not maintain a separate `scripts/` convention unless a real executable responsibility appears that differs from `tools/`.

Local generated artifacts remain ignored and may be removed from the worktree for clarity:

```text
__pycache__/
*.pyc
src/upgradepilot.egg-info/
```

No commit should be required for generated-artifact cleanup because `.gitignore` already owns it.

Do not over-organize `tools/` into subdirectories merely because a few files exist. Reassess only when stable executable families make the flat directory difficult to navigate.

### Cluster 16 — active source comments/docstrings and naming audit

Perform this incrementally during every move, then one final focused audit.

Correct active source references to removed/renamed modules such as:

```text
PinnedDependencyChange
ci_authority.py
old flat module paths
old package-level façade imports
unresolved_claim as a semantic architecture
```

Use the educational-comment standard:

Keep comments/docstrings that explain:

- module responsibility;
- data flow;
- trust boundary;
- exact evidence meaning;
- why a non-obvious design choice exists;
- important edge/failure semantics;
- terminology that materially improves learning.

Remove or shorten comments that merely narrate obvious Python mechanics when they obscure the actual architecture.

Do not strip useful educational explanation merely to minimize line count.

Apply the naming specification's recall test to active module/type/function names during their migration. Do not launch unrelated cosmetic renames.

Validation gate:

- no active docstring points to nonexistent modules/contracts;
- names map cleanly to the target architecture;
- complete product suite green.

---

## 7. Test topology after reconciliation

The product test tree should mirror stable product responsibilities without requiring one test file per source file.

Recommended direction:

```text
tests/
├── test_cli.py
├── test_investigation.py
├── test_package_import.py
├── dependency/
│   ├── test_change.py
│   ├── test_analysis.py
│   ├── test_requirements.py
│   ├── test_uv_lock.py
│   └── test_versioning.py
├── github/
│   ├── test_api.py
│   ├── test_pull_request.py
│   ├── test_actions.py
│   ├── test_repository.py
│   ├── test_release.py
│   ├── test_tag.py
│   └── test_changelog.py
├── pypi/
│   ├── test_api.py
│   ├── test_release.py
│   └── test_provenance.py
├── ci/
│   ├── test_workflow_commands.py
│   └── test_dependency_exercise.py
├── upstream/
│   ├── test_repository.py
│   ├── test_interval.py
│   ├── test_interval_evidence.py
│   └── test_claim.py
└── target/
    ├── test_python.py
    ├── test_python_specifier.py
    └── test_relevance.py
```

Do not split a coherent test file merely to make the tree symmetrical. Edge/integration tests may remain separate where they prove a distinct contract.

Tests that cross several modules but still exercise product behavior may use clear names such as:

```text
test_dependency_change_integration.py
test_upstream_interval_integration.py
```

rather than being forced into artificial unit-only categories.

---

## 8. Validation strategy

### 8.1 Baseline proof

Before migration, record:

```text
origin/main commit
focused Step 7A deterministic result
full active test count/time
Step 7A live proof result if available
```

### 8.2 Per-cluster proof

For each cluster:

1. run the smallest changed test set;
2. run import/installation smoke when package paths changed;
3. run complete active product tests;
4. inspect `git diff --stat` and `git diff` for unintended semantic edits;
5. search for stale imports/names owned by that cluster;
6. commit only after the cluster is green.

### 8.3 Structural proof

At the end, verify:

```text
no active flat modules remain that belong to an admitted subpackage
no active imports use removed legacy dependency contracts
no product source imports experiments
no experiment-harness tests remain under tests/
upgradepilot.__init__ is intentionally small
python -m upgradepilot works
installed upgradepilot console script works
full product deterministic suite passes
separate experiment suite passes
```

### 8.4 Live proof

After deterministic reconciliation succeeds, rerun the already authorized Step 7A live changelog-discovery proof from its updated path/imports.

This is a regression proof for existing behavior, not new capability.

Do not rerun the 25-call Step 6 model evaluation merely because files moved. Re-evaluate the model only if the productized model contract/deployment changes later under Step 7.

---

## 9. Commit discipline

Prefer one coherent commit per validated migration cluster or small tightly related subcluster.

Examples:

```text
architecture: record responsibility-based source packages
refactor: centralize package and repository identity
refactor: group GitHub acquisition modules
refactor: group PyPI acquisition modules
refactor: remove legacy pinned dependency path
refactor: separate dependency and target version methods
refactor: unify exact repository text evidence
refactor: narrow upstream repository identity
refactor: separate investigation orchestration from CLI
refactor: reduce package root exports
refactor: separate product and experiment tests
```

Do not mix unrelated feature work into these commits.

After each commit, the repository should remain understandable and testable; temporary broken import states should not be pushed as ordinary checkpoints.

---

## 10. Explicit semantic-change ledger

Most clusters should be behavior-preserving. The following planned corrections may intentionally change active contracts or output and therefore require dedicated tests and explicit review:

### Legacy dependency removal

Changes internal/public Python symbol availability but should preserve accepted dependency-extraction behavior.

### Exact repository evidence convergence

May reject malformed/inconsistent evidence that the older weaker file model accepted. This is a deliberate evidence-strengthening change.

### Upstream source reconciliation

Removes the obsolete `claim_state='unresolved_claim'` representation and may change the corresponding CLI diagnostic. Semantic claim authority moves exclusively to the newer grounded-claim boundary.

### Root package API shrink

Removes accidental package-level imports. This is intentional because no external stable library API has been admitted.

Every other cluster should be treated as behavior-preserving unless the diff proves otherwise.

---

## 11. Final acceptance gate

The reconciliation is complete only when all of the following hold:

1. the synchronized pre-refactor baseline was recorded;
2. the subpackage architecture ADR is accepted;
3. product source matches the demonstrated responsibility boundaries;
4. shared identity/path primitives have one owner each;
5. no active dependency extraction routes through legacy `PinnedDependencyChange` contracts;
6. GitHub clients depend on GitHub identity primitives rather than unrelated PR modules;
7. Step 7A changelog discovery lives under the GitHub acquisition boundary;
8. PyPI acquisition lives under one PyPI provider package;
9. dependency versioning and target Python specifier semantics are separated by domain;
10. exact repository text uses one strong active evidence contract;
11. old upstream `unresolved_claim` semantics are removed from active architecture;
12. CLI presentation and application orchestration are separated;
13. `upgradepilot.__init__` exposes only an intentional minimal surface;
14. active product tests live under `tests/` and completed Step 6 experiment tests do not;
15. no product runtime imports experiment code;
16. active source comments/docstrings describe the real architecture;
17. narrow tests pass after every cluster;
18. final active product deterministic suite passes;
19. separate completed experiment suite passes;
20. package/import/console entry points pass;
21. Step 7A deterministic and live behavior still passes after path migration;
22. no Step 7B/7C/7D/7E feature behavior was implemented as part of the reconciliation.

---

## 12. Stop line and handoff back to Step 7

Stop the reconciliation when the final acceptance gate passes.

Only then return to the bounded extractor runtime-integration plan.

The next product sequence remains conceptually:

```text
validated Step 7A exact-commit changelog discovery
→ Step 7B deterministic crossed-release Markdown source windows
→ Step 7C product local semantic adapter
→ Step 7D support-drop evaluation boundary
→ Step 7E conditional CLI/application orchestration
→ Step 7F controlled + live S001 proof
```

The restructured package names may require the Step 7 plan's expected module paths to be updated before implementation, but its evidence and safety requirements remain controlling.

Do not interpret completion of this source reconciliation as progress on Step 7 semantic runtime capability itself.
