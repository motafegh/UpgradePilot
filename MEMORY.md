# UpgradePilot Current Memory

**Last updated:** 2026-08-04  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, selected continuation, and current learning state.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Parent plan:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)
- **Step 6:** closed with disposition `adopt_bounded_extractor` for the narrow support-drop semantic role.
- **Accepted semantic architecture:** [`docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md`](docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md)
- **Step 7 runtime-integration plan:** [`plans/B2_TARGET_PYTHON_STEP_7_BOUNDED_EXTRACTOR_RUNTIME_INTEGRATION_PLAN.md`](plans/B2_TARGET_PYTHON_STEP_7_BOUNDED_EXTRACTOR_RUNTIME_INTEGRATION_PLAN.md)
- **Selected work before further Step 7 capability:** [`plans/B2_SOURCE_CODE_STRUCTURE_RECONCILIATION_PLAN.md`](plans/B2_SOURCE_CODE_STRUCTURE_RECONCILIATION_PLAN.md)
- **Accepted source-layout evolution:** ADR-0007 — responsibility-based internal Python packages.
- **Source reconciliation:** major tranche 1 implemented remotely; user validation pending.
- **Latest tranche record:** [`working-memory/2026-08-04_B2-source-structure-major-tranche-1.md`](working-memory/2026-08-04_B2-source-structure-major-tranche-1.md)
- **Latest repository commit before this memory update:** `e2afe49dee8d8db95acb41870f5bb2fe80ad038c`.

## Last verified pre-refactor baseline

Ali synchronized the checkout and reported:

```text
Ran 353 tests in 0.077s

OK
```

Then the live Step 7A proof reported:

```text
LIVE STEP 7A PROOF: PASS
path: docs/src/markdown/about/changelog.md
```

This baseline is preserved in:

[`working-memory/2026-08-04_B2-source-structure-reconciliation-baseline.md`](working-memory/2026-08-04_B2-source-structure-reconciliation-baseline.md)

It is the comparison point for the new major tranche; it does **not** prove the new tranche yet.

## Major tranche 1 implemented

### Real dependency ownership

Active implementation now exists under:

```text
upgradepilot/dependency/change.py
upgradepilot/dependency/requirements.py
upgradepilot/dependency/analysis.py
```

The direct exact-requirements path no longer routes through the legacy:

```text
PinnedDependencyChange
UnsupportedDependencyChange
DependencyChangeResult
extract_pinned_dependency_change(...)
```

Old flat dependency modules are compatibility shims only while remaining callers/tests migrate.

### Root package API

`upgradepilot.__init__` is intentionally minimal and no longer re-exports the internal evidence/client graph:

```text
upgradepilot.__all__ == ()
```

Internal code should import precise owners.

### Responsibility packages

The demonstrated architecture now has explicit packages:

```text
upgradepilot.github
upgradepilot.pypi
upgradepilot.dependency
upgradepilot.ci
upgradepilot.upstream
upgradepilot.target
```

Some large provider/domain modules are still backed by temporary compatibility imports and are not yet claimed physically migrated.

### Step 7A ownership

The actual changelog-path discovery implementation now lives in:

```text
upgradepilot.github.changelog
```

The old `upgradepilot.upstream_changelog` path is only a compatibility shim. The live proof tool imports the new GitHub-owned path.

The shared Git object-ID validator preserves the pre-refactor 40- or 64-hex grammar.

### Upstream repository identity

`upgradepilot.upstream.repository` now isolates the trusted-repository question:

```text
PyPI Source metadata
+ PyPI publisher provenance
→ UpstreamRepositoryEvidence | UpstreamRepositoryProblem
```

Its success record has no semantic `claim_state` and does not require a GitHub Release.

The old `UpstreamSourceResolver` remains active only because current CLI orchestration has not yet migrated.

### Application boundary

`upgradepilot.investigation.investigate_public_pull_request(...)` and
`PublicPullRequestInvestigation` now exist as the application orchestration owner.

The existing CLI has **not** yet been switched to it; that switch will be done together with CLI/investigation test migration in major tranche 2.

## Intentionally unfinished reconciliation work

Major tranche 2 still owns:

1. physically moving/removing the remaining large flat GitHub/PyPI/CI/upstream/target implementation modules and deleting their temporary shims;
2. migrating `uv_lock_change.py` and removing its duplicated repository-path validation;
3. physically splitting/removing `packaging_method.py` after callers/tests use dependency versioning and target specifier owners;
4. converging `RepositoryTextFile` / `ExactRepositoryTextFile` into one strong exact-revision evidence contract;
5. removing old `UpstreamSourceResolver` / `UpstreamReleaseEvidence.claim_state='unresolved_claim'` from active architecture;
6. switching `cli.py` to `investigation.py` and migrating CLI tests accordingly;
7. separating completed Step 6 experiment-harness tests from active product tests;
8. final stale docstring/comment/naming audit;
9. final import/installation/console/live-Step-7A regression proof.

## Exact continuation

First synchronize the WSL checkout to remote `main`, then validate **the whole major tranche at once**:

```bash
git pull --ff-only origin main

python -m unittest \
  tests.test_source_topology \
  tests.test_identity_primitives \
  tests.test_dependency_change \
  tests.test_exact_requirement_change \
  tests.test_dependency_analysis \
  tests.test_upstream_changelog \
  tests.test_target_python \
  tests.test_target_python_relevance \
  tests.test_package_interface \
  -v

python -m unittest discover -s tests -v

python -m upgradepilot --help
upgradepilot --help
python tools/live_s001_changelog_discovery_proof.py

git status
git log -1 --oneline
```

Return the focused result, full-suite count/time, both entry-point smoke results if any error appears, complete live Step 7A output, and final Git status/head.

If this broad gate passes, proceed directly to **major tranche 2**. Do not return to per-file micro-gates.

## Step 6 semantic boundary remains unchanged

Accepted runtime method remains:

```text
LM Studio local HTTP
+ gemma-4-e4b-it-ud
+ contract v2
+ temperature 0
+ seed 0
+ no automatic retries
+ deterministic exact-source reconstruction
+ mandatory validate_support_drop_candidates(...)
```

No source-reconciliation change grants broader model authority.

## Stop line

Until source reconciliation reaches its final acceptance gate, do not implement:

- Step 7B crossed-release Markdown source windows;
- normal-runtime LM Studio extraction;
- conditional target-Python activation;
- compatibility/safety/merge/defer/recommendation logic;
- automatic retries or Instructor/Pydantic;
- target-repository mutation.

## Learning depth

Current exposure includes responsibility-based package design, migration shims, accidental public API removal, domain-vs-provider ownership, transition-contract retirement, exact Git identity, semantic trust boundaries, and application-vs-interface orchestration.

This is implementation exposure and guided architectural participation; it is not a claim of independent mastery.
