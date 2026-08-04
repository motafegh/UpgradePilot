# B2 Source-Structure Reconciliation — Final Cleanup

**Date:** 2026-08-04  
**Scope:** source/test/tool topology only; no new B2 capability  
**Architectural control:** ADR-0007 and `plans/B2_SOURCE_CODE_STRUCTURE_RECONCILIATION_PLAN.md`

## 1. Why this final cleanup was necessary

After the two major source-reconciliation tranches, the real implementations had already moved under responsibility-based packages, but the repository intentionally retained temporary flat compatibility modules such as:

```text
upgradepilot.github_client
upgradepilot.github_repository
upgradepilot.pypi_client
upgradepilot.dependency_change
upgradepilot.packaging_method
upgradepilot.target_python
upgradepilot.upstream_claim
```

That migration midpoint was useful while consumers were being moved because a stale import remained diagnosable instead of becoming an immediate module-not-found failure. It was not the intended end-state architecture.

The final cleanup therefore used a consumer-first rule:

```text
migrate real consumer
→ preserve regression behavior
→ confirm the real package owns implementation
→ remove obsolete flat module
```

The repository was not made visually clean by deleting modules first and repairing failures afterward.

## 2. Final active product source topology

The intended implemented product tree is now:

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

No future Step 7 module was scaffolded early.

## 3. Flat compatibility modules removed

The following temporary source files were removed after active consumers were migrated:

```text
src/upgradepilot/ci_dependency_exercise.py
src/upgradepilot/dependency_analysis.py
src/upgradepilot/dependency_change.py
src/upgradepilot/exact_requirement_change.py
src/upgradepilot/github_actions.py
src/upgradepilot/github_api.py
src/upgradepilot/github_client.py
src/upgradepilot/github_release.py
src/upgradepilot/github_repository.py
src/upgradepilot/github_tag.py
src/upgradepilot/packaging_method.py
src/upgradepilot/pypi_api.py
src/upgradepilot/pypi_client.py
src/upgradepilot/pypi_provenance.py
src/upgradepilot/target_python.py
src/upgradepilot/target_python_relevance.py
src/upgradepilot/upstream_changelog.py
src/upgradepilot/upstream_claim.py
src/upgradepilot/upstream_interval.py
src/upgradepilot/upstream_interval_acquisition.py
src/upgradepilot/upstream_source.py
src/upgradepilot/uv_lock_change.py
src/upgradepilot/workflow_commands.py
```

`tests/test_source_topology.py` now asserts that every one of these module paths is absent with `importlib.util.find_spec(...)`.

## 4. Consumer migration

Active product tests were migrated to precise owners such as:

```text
upgradepilot.github.pull_request
upgradepilot.github.repository
upgradepilot.pypi.release
upgradepilot.dependency.change
upgradepilot.dependency.uv_lock
upgradepilot.ci.dependency_exercise
upgradepilot.target.python_specifier
upgradepilot.upstream.interval_evidence
upgradepilot.upstream.claim
```

Tests were not deleted merely because they imported old paths. Their behavioral assertions were preserved while their imports and stale architecture comments were corrected.

The public product root remains intentionally small; internal code should not treat `upgradepilot.__init__` as a giant convenience façade.

## 5. Product tests versus completed experiment tests

The completed Step 6 model-evaluation machinery remains valuable executable evidence, but it is not normal product-runtime regression coverage.

Seven Step 6 regression files were therefore moved from the active product `tests/` root to:

```text
experiments/tests/
```

The preserved experiment suite contains:

```text
test_step6_support_drop_contract_v2.py
test_step6_support_drop_contract_v2_assessment.py
test_step6_support_drop_contract_v2_live_evaluation.py
test_step6_support_drop_evaluation_harness.py
test_step6_support_drop_semantic_corpus.py
test_step6_support_drop_smoke_harness.py
test_step6c_local_http_runner.py
```

This makes the two validation statements precise:

```text
python -m unittest discover -s tests -v
→ active product deterministic regression suite

python -m unittest discover -s experiments/tests -v
→ completed Step 6 experiment/harness regression suite
```

No Step 6 model evaluation code or historical evidence was removed.

The semantic-corpus test required one path correction after relocation because its previous `Path(__file__).parents[...]` assumption was relative to the old `tests/` location. The corpus identity itself was unchanged.

## 6. Historical experiment source imports

The Step 6 experiment modules were migrated away from deleted flat product paths. They now consume current trust contracts from:

```text
upgradepilot.upstream.claim
upgradepilot.upstream.interval
```

This preserves historical experiment executability without allowing product code to depend on `experiments/`.

## 7. Developer/live tooling

`tools/live_s001_upstream_interval_proof.py` was migrated to the current provider/domain owners:

```text
upgradepilot.github.api
upgradepilot.github.repository
upgradepilot.github.tag
upgradepilot.pypi.release
upgradepilot.upstream.interval
upgradepilot.upstream.interval_evidence
```

The Step 7A changelog-discovery proof was already using `upgradepilot.github.changelog`.

Step 6 launcher tools continue to launch the historical experiment modules and do not become product runtime code.

## 8. Internal aliases versus duplicate modules

This cleanup's hard architectural requirement is that the duplicate **module layer** is gone.

A small number of migration aliases may still exist inside their one real owner, for example an older type name referring to the same canonical evidence class. Such an alias does not create a second implementation or a second file owner. It can be removed later when doing so improves the active contract rather than merely changing spelling.

This distinction prevented the final tree cleanup from becoming an unnecessary mass rewrite of otherwise-correct behavioral assertions.

## 9. Generated local artifacts

Local directories such as:

```text
__pycache__/
src/upgradepilot.egg-info/
```

are generated artifacts, not source topology. `.gitignore` already excludes `__pycache__/`, `*.py[cod]`, and `*.egg-info/`.

An empty-looking local `scripts/__pycache__/` similarly does not establish a repository script convention. `tools/` remains the developer/live-validation executable location.

## 10. What did not change

This final cleanup did **not** implement:

- Step 7B changelog source-windowing;
- the normal-runtime LM Studio model client;
- support-drop runtime inference;
- conditional target-Python activation;
- Instructor/Pydantic or automatic retries;
- new source formats;
- compatibility/safety/merge/recommendation behavior.

Step 6 remains closed with its bounded extractor disposition, and Step 7 remains paused until this structural end-state passes its final acceptance gate.

## 11. Final validation gate — pending user execution

The final structure is implemented remotely but is not yet behavior-validated as a whole after shim deletion and test separation.

Required acceptance sequence from a clean synchronized WSL checkout:

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

The live proofs use public read-only source acquisition and do not call LM Studio.

Only after this gate is green should the reconciliation be marked behavior-validated and Step 7B resume.
