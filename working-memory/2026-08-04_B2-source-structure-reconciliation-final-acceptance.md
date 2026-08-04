# B2 Source-Structure Reconciliation — Final Acceptance

**Date:** 2026-08-04  
**Scope:** final behavior validation of the completed source/test/tool topology reconciliation  
**Controlling plan:** `plans/B2_SOURCE_CODE_STRUCTURE_RECONCILIATION_PLAN.md`  
**Architecture:** ADR-0007 — responsibility-based internal Python packages

## Final disposition

The B2 source-code structure reconciliation is **complete and behavior-validated**.

The final repository state has passed the required deterministic product regression, separate historical experiment regression, package/console entry-point checks, and the existing live public-source regressions that protect Step 5 and Step 7A behavior.

No Step 7B/7C/7D/7E semantic-runtime capability was implemented during the reconciliation.

## Final deterministic acceptance evidence

Ali ran from synchronized WSL `main` after the final flat-shim removal and test separation.

### Active product regression suite

Command:

```bash
python -m unittest discover -s tests -v
```

Result:

```text
Ran 323 tests in 0.061s

OK
```

Meaning:

- `tests/` now measures active product behavior only;
- obsolete flat module paths are asserted absent;
- current provider/domain/application imports are exercised;
- no Step 6 experiment-harness tests are included in this count.

### Completed Step 6 experiment/harness regression suite

Command:

```bash
python -m unittest discover -s experiments/tests -v
```

Result:

```text
Ran 27 tests in 0.004s

OK
```

Meaning:

- the completed Step 6 semantic corpus, smoke adapter, contract-v2 mapping, live-evaluator scoring, assessment scoring, and localhost proxy-isolation mechanics remain executable;
- historical experiment coverage is preserved without being counted as normal product-runtime coverage.

### Application entry points

Commands:

```bash
python -m upgradepilot --help
upgradepilot --help
```

Results:

```text
python -m upgradepilot --help: PASS
installed upgradepilot --help: PASS
```

This proves both the module entry point and installed console-script entry point survived the package restructure.

### Worktree state

Result:

```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

## Existing live regressions retained

### Step 7A exact-commit changelog discovery

Previously rerun after the final source cleanup:

```text
LIVE STEP 7A PROOF: PASS
```

The generic GitHub exact-commit discovery rule recovered:

```text
docs/src/markdown/about/changelog.md
```

for the historical S001 Soup Sieve commit without a product path constant.

### Step 5 upstream interval acquisition

The first final-acceptance rerun failed with HTTP 401 because the validation tool inherited a stale/invalid `GITHUB_TOKEN` and sent it to a public GitHub endpoint.

That was diagnosed as ambient credential contamination, not an acquisition/refactor defect. The proof tool was corrected to use anonymous public GitHub reads, matching the Step 7A live-proof policy.

The rerun then passed:

```text
LIVE STEP 5 PROOF: PASS
```

Observed evidence included:

```text
crossed releases: 2.7, 2.8, 2.8.1, 2.8.2, 2.8.3, 2.8.4
tag ref: refs/tags/2.8.4
resolved commit: 28108ab805818c832d9568142a99844fd95a0d39
changelog path: docs/src/markdown/about/changelog.md
changelog blob SHA: 6f221b7398681a580fa199044b3d3f1e11b55493
changelog bytes: reported=17370, decoded=17370
authority basis: tagged_changelog
GitHub Release bodies admitted: 0
```

No changelog semantics or target-Python relevance were evaluated by that proof.

## Final architecture accepted

The duplicate flat compatibility module layer is gone. Active product ownership is under:

```text
upgradepilot.github
upgradepilot.pypi
upgradepilot.dependency
upgradepilot.ci
upgradepilot.upstream
upgradepilot.target
```

with source-neutral/application boundaries at:

```text
upgradepilot.json_contract
upgradepilot.package_identity
upgradepilot.repository_path
upgradepilot.investigation
upgradepilot.cli
```

`upgradepilot.__init__` remains intentionally minimal.

The application boundary is:

```text
CLI input
→ investigate_public_pull_request(...)
→ typed investigation result
→ CLI rendering / exit policy
```

## Step 7 handoff after reconciliation

The reconciliation stop line is removed. The next authorized product increment is **Step 7B — deterministic crossed-release Markdown source windows**.

The Step 7 plan predates the final package restructure, so its modification-boundary filenames must be interpreted using the accepted owners:

```text
Step 7A existing discovery:
  src/upgradepilot/github/changelog.py

Step 7B new deterministic changelog/window interpretation:
  src/upgradepilot/upstream/changelog.py

Step 7C bounded local semantic adapter:
  src/upgradepilot/upstream/support_drop_extractor.py

Step 7E application sequencing:
  src/upgradepilot/investigation.py

CLI presentation:
  src/upgradepilot/cli.py

Existing deterministic trust/relevance boundaries to preserve:
  src/upgradepilot/upstream/claim.py
  src/upgradepilot/upstream/interval.py
  src/upgradepilot/target/relevance.py
```

No empty Step 7 modules should be created until the corresponding increment is implemented.

## Final conclusion

The source-structure reconciliation achieved its intended purpose:

```text
transition-era flat package
→ demonstrated responsibility packages
→ precise imports
→ one active product suite
→ separate experiment suite
→ preserved live acquisition behavior
→ clean application/CLI boundary
```

The repository is now structurally ready to resume Step 7 implementation from Step 7B.
