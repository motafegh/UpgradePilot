# Apply the pytest version comparison to OmniMatch

Ali approved continuing with the tool after the [controlled proof](2026-11-10_pytest-dependency-version-comparison_build-cycle.md) and asked about organizing developer tools as their number grows. Main and origin/main reconciled at `afd4a2d1`. Interpret the immediate continuation as the already-described one-test OmniMatch comparison. The previous conversation supplied the understanding gate for this fixed pair. Scope is a developer qualification, with a single known target and no remote writes.

UP-SKILL:upgradepilot-build-implement. UP-SKILL:upgradepilot-learning-by-doing. UP-SKILL:upgradepilot-working-memory.

## Frozen attempt scope

- Target `Kotlasuhasreddy123/Project-OmniMatch#20`, reviewed base `db5576e5b38053a7b46d89ff51e1175eb61ab9c2`, exact frozen checkout `22fc7709642599feca7b9527fe4f44874d04e520`. Select only `backend/tests/test_security_guardrails.py::test_rate_store_has_a_hard_size_bound`.
- Follow the exact-head backend verification workflow's direct install pins and Python 3.11 selector. Use local Python 3.11.15 and one old-pin wheel resolution. Freeze the common wheel files and hashes, replace only the HTTPX wheel for the proposed arm, and run offline dependency checks in both arms. Two installations and test executions share the same isolation profile and use separate disposable writable scratch directories. Wheel acquisition uses public PyPI and wheels only, with a 120-second resolution deadline and no automatic retries or source builds.
- Docker Desktop's Linux engine was unavailable. The temporary Ubuntu bubblewrap package was extracted without installation. Verified a new user/mount/PID/network isolation route with only loopback visible and no home directory mounted. Use a cleared environment, read-only exact target checkout, Python, tool and wheel inputs, with disposable scratch, no host credentials or network, and a 45-second deadline per named pytest execution. The comparison tool records its normal selected-node and loaded-module proofs. This is a local derivative of the target CI setup, with its own runner provenance.
- Keep raw output in private scratch. Publish only safe receipt fields, hashes and a scoped result. Stop if the pinned environment or isolation check fails. No dependency substitutions or broadened target execution without separately recording a successor scope. Same-process test evidence is independent of normal product reporting or maintainer action.

Static preflight recovered the exact workflow and test from the frozen commit. It exposed a nested pytest root issue. Without an explicit root directory, pytest collected a test under `backend/pytest.ini` as `tests/...`, while the tool requires a repository-relative node ID. The change supplies the checkout as pytest's root directory. A controlled nested-project capture passed and still reported `backend/pytest.ini` as its configuration file. Wheel-only public preparation resolved all eleven direct pins under Python 3.11.15. An initial freeze check guessed the wrong transitive wheel count and stopped before execution. The corrected check verifies the actual direct pins, unique wheel names and size bound, then freezes the common wheel bytes plus the two HTTPX alternatives. A stricter bubblewrap preflight passed with explicit user namespace creation, nested user namespaces disabled and all capabilities dropped.

## Paired result

The offline installs used 44 identical common wheels plus their respective HTTPX wheel. The 46 downloaded wheels totaled 40,253,471 bytes. Both arms passed `pip check`, loaded `backend/pytest.ini` and collected exactly the specified repository-relative test. The same-process observer tied `httpx/__init__.py` to each requested distribution. Both checkouts remained clean.

| Arm | HTTPX loaded | Pytest result |
| --- | --- | --- |
| [Old receipt](evidence/2026-11-10-omnimatch-isolated-pytest-comparison/old.json) | 0.27.0 | One passed in 0.44 s, including passed setup, call and teardown |
| [Proposed receipt](evidence/2026-11-10-omnimatch-isolated-pytest-comparison/proposed.json) | 0.28.1 | One passed in 0.48 s, including passed setup, call and teardown |

Both runs emitted five warnings. The [offline comparison](evidence/2026-11-10-omnimatch-isolated-pytest-comparison/comparison.json) returned `both_passed`. The matched recorded inventory and [wheel manifest](evidence/2026-11-10-omnimatch-isolated-pytest-comparison/wheel-manifest.json) identify the byte-identical common wheels and tool used. A separate offline replay from the saved receipts reproduced the comparison byte for byte. The test durations are pytest's local output, not a timing comparison or end-to-end setup duration. Compile, diff and governance checks passed.

The app behavior asserted by this one test held in both local environments. The result is separate from the original GitHub workflow observation. The green target jobs still declared the old pin, and this pair did not rerun those jobs or establish a whole-upgrade verdict. No product runtime or action behavior changed. The local developer tool was useful here because it produced an exact, version-bound test receipt and exposed a genuine repository-relative naming gap in its own first real application.

Ali reported that Docker Desktop had been closed and reopened it after the isolated runs succeeded. Retain the original Docker availability observation and the completed bubblewrap result. No Docker rerun is needed to qualify the selected pair.

## Tool organization and handoff

Keep the reusable comparator in the existing `tools/` developer area. Keep the real-case manifests and receipts in dated evidence. If several developer tools later share proven receipt, runner, or environment responsibilities, a named subpackage inside `tools/` can own that shared code. A second script alone does not justify a general framework or a product import. The current result closes this targeted developer comparison. Further work should be selected by a distinct maintainer question or a real recurring tool responsibility.

```text
A0/A1/A2 — Reconciled the selected target, previously taught comparison, and isolation scope.
B — Fixed nested node naming, prepared matched isolated environments, and ran one named test per arm.
Verification — Two passing receipts, matched inventory and wheel basis, offline replay and nested control.
D/E — Separate the result of this one local test from prior target CI and overall compatibility.
C — Preserved preflight failures, corrections, manifests, receipts and handoff.
```
