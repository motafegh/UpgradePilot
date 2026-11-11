# Build a controlled pytest dependency-version comparison

Ali selected Build after explaining the difference between the finished OmniMatch pin report and the proposed two-environment test comparison. Main and origin/main reconciled at `b6f5da26`. Prior discussion covered the same commit, matched inputs, one changing dependency, same-process observation, and pass/fail/inconclusive outcomes. Compress the continuity and pre-B gates for this selected proof method. Target-specific execution and native adoption carry separate authorization and proof.

UP-SKILL:upgradepilot-build-implement. UP-SKILL:upgradepilot-learning-by-doing. UP-SKILL:upgradepilot-working-memory.

The existing [runtime proof plan](../plans/RUNTIME_DEPENDENCY_STATE_PROOF_COMPLETION_PLAN.md#conditional-cycle-2--explicit-target-owned-runtime-state-evidence) keeps command-completion state, explicit target-owned package-state acquisition and affected-path behavior separate. Build a developer-operated proof tool under `tools/`, with no product import, package installation, checkout acquisition or automatic target selection. One capture runs one named pytest case in an operator-prepared environment. A separate offline comparison checks the paired records. Verify the real pytest hook in two prepared environments with a controlled, version-sensitive fixture. This does not select Runtime-State Cycle 2 or establish an OmniMatch result.

## What the tool does

[`compare_pytest_dependency_versions.py`](../tools/compare_pytest_dependency_versions.py) has two explicit commands. `capture` runs one selected pytest node with the Python executable of an already prepared environment. It verifies the clean checkout and exact revision, requires the requested installed distribution, and records setup, call and teardown outcomes. During the call-phase report it looks up the named module already loaded in that pytest process. It verifies that the module file is present and belongs to the installed distribution's recorded files. A pin or distribution metadata alone earns no loaded-module result. It records the distribution-relative file path, leaving absolute install paths and raw pytest diagnostics out of the receipt.

`compare` reads two receipts offline. It requires the same revision, test, package, module, Python/platform, pytest, explicitly selected plugins and recorded inventory of the other distributions. Requested versions must differ. A selected node without a verified loaded module, expected-failure marker, skip, missing phase or inconsistent pytest exit stays inconclusive. The package inventory is a comparison guard rather than a byte-level environment reproduction. Operator isolation, matching environment configuration and case relevance remain prerequisites. The tool can observe a module loaded at the call boundary. It does not trace individual calls into the package.

The tool stops collection if more or fewer than the selected exact node are found. It disables automatic plugin loading and ambient/default extra pytest arguments. A project that needs a plugin can select it explicitly with `--plugin` in both runs. Full failure details stay in normal pytest output, where an operator can retain them privately. Receipts are written only to new paths outside the checkout.

## Controlled verification

Created two disposable Python 3.12.3 environments with identical pytest 8.3.5, pluggy 1.5.0, packaging 24.2 and iniconfig 2.0.0. Built two minimal local fixture wheels whose `fixturedep.value()` functions return 1 and 2 respectively. The checkout at `7af964e85d8c75f84bbaa86a3145afd3b43958c1` contains a controlled test that imports the package and asserts `fixturedep.value() == 1`. The [old receipt](evidence/2026-11-10-pytest-dependency-version-comparison/old.json) shows 1.0 loaded and the test passed. The [proposed receipt](evidence/2026-11-10-pytest-dependency-version-comparison/proposed.json) shows 2.0 loaded and the call failed with `AssertionError: assert 2 == 1`. Both setup and teardown passed. Offline comparison returned `proposed_only_test_failure`.

A second test accepted either value and returned `both_passed`. Four real pytest contrasts returned `inconclusive`: no import, a module shadowed by a checkout file, a skipped test and strict unexpected success. Wrong revision, duplicate output, missing node and mismatched recorded environment controls also passed. The final checks recreated the fixture checkout and fresh receipts after the source was finalized. Governance doctor, compile and diff checks passed. These controls exercise the developer tool, not an OmniMatch or product runtime claim.

### Command shape

Use this with a separately approved, isolated checkout and already prepared environments. Run once per version, varying the Python interpreter, expected version and receipt path. The node ID is the repository-relative pytest test path plus its selected name.

```sh
"$prepared_python" tools/compare_pytest_dependency_versions.py capture \
  --checkout "$isolated_checkout" --revision "$exact_head" \
  --nodeid "$selected_test_node" --distribution "$package" --module "$import_name" \
  --expected-version "$version" --output "$new_receipt"

python3 tools/compare_pytest_dependency_versions.py compare "$old_receipt" "$proposed_receipt"
```

A capture can exit with pytest status 1 and still leave a usable receipt for a failed test. A comparison exit of 2 signals insufficient or mismatched evidence. The reviewed OmniMatch test remains an optional exact-target experiment. Before applying this method there or elsewhere, select the maintainer concern and isolate the exact target execution under its own scope. No changes to UpgradePilot product behavior or automated action permission.

```text
A0/A1/A2 — Reconciled main and carried forward the agreed controlled comparison and scope.
B — Built one named-test observer and offline comparison over paired receipts.
Verification — Real pytest controls in two isolated fixture environments passed.
D/E — Distinguish a requested package, the module loaded by pytest and the test outcome.
C — Preserved decisions, paired receipts, failure/unsupported cases and handoff.
```
