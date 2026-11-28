# Screen MapProxy for use of Soup Sieve's changed selector behavior

November 28, 2026. Used the repository-audit and working-memory skills at the doing-only cadence. The [grounded explanation checkpoint](2026-11-28_evidence-grounded-explanation-checkpoint.md) established the two attributed Soup Sieve 4.0 selector changes. This check looked for an exact-head MapProxy call or fixture that would make either change relevant to a maintainer decision.

## Exact target and scope

MapProxy PR #1559 changes Soup Sieve 3.0.4 to 4.0 in `requirements-tests.txt`. The screen froze the retained base `a6507dd0dba671e48d303a74f7a5575dadf7fd76` and head `ac01b8901935bfc16a0195277b4aec1c43275897`. The exact Git commit, complete recursive tree and bounded archive arrived through three anonymous reads. The archive had all **662 tracked regular files**. Each file matched its exact Git blob. No special members or missing tracked files were found. [Exact PR](https://github.com/mapproxy/mapproxy/pull/1559)

The read-only scan parsed **293 Python files** and checked 605 UTF-8 non-binary files for package names, selector entry points and literal `template` or `iframe` markup. It also checked the one non-UTF-8 text readme for the ASCII terms. It inspected named API attributes and literal dynamic import or attribute references. The direct Beautiful Soup and Soup Sieve text matches were in the test pin file and changelog. The Python package scan found two WebTest import sites. It identified 134 `lxml` and five `xml` attribute references and no matching Soup Sieve or Beautiful Soup import, named CSS selector entry point, or WebTest HTML/form/click access in Python. These are static results over the verified snapshot.

## Follow the indirect test dependency

The exact test file pins WebTest 3.0.0, Beautiful Soup 4.14.3 and Soup Sieve 4.0. The two wrapper wheels matched exact PyPI release metadata and file digests. Their declared dependency chain is WebTest → Beautiful Soup → Soup Sieve. The imported WebTest response class imports Beautiful Soup, and Beautiful Soup's CSS module can import Soup Sieve. This supports a plausible import path in an environment that installs the declared packages. It leaves the actual CI-loaded packages open. [Exact test requirements](https://github.com/mapproxy/mapproxy/blob/ac01b8901935bfc16a0195277b4aec1c43275897/requirements-tests.txt)

The tracked system-test fixture constructs `WSGITestApp` from WebTest's `TestApp`. One WMS test calls `app.get` and passes `resp.lxml` to its capabilities check. In WebTest 3.0.0, that response property dispatches to lxml's HTML or XML parser. Its separate `html` property creates a Beautiful Soup object. Beautiful Soup's `Tag.select` delegates to its CSS interface and then to Soup Sieve. The inspected MapProxy code did not use that selector path or supply a fixture tied to the two release clauses. The distinction explains why a pinned test dependency and even a possible import are insufficient to establish a selector behavior change for the target. [Representative WMS test](https://github.com/mapproxy/mapproxy/blob/ac01b8901935bfc16a0195277b4aec1c43275897/mapproxy/test/system/test_wms.py#L63-L71)

This screen supports no positive target compatibility claim for these two changes. Code loaded dynamically, plugin behavior and actual test execution require their own evidence. A green workflow and a dependency pin do not establish an affected selector call or coverage.

## Deterministic baseline and decision

The installed offline CLI reopened the ordinary report and its exact tagged changelog as `source-38`. The retained changelog text matches the evidence from the earlier check. Looking up the `4.0` heading recovers the two scoped selector statements directly. The complete 4.0 section alone runs from line 6 through 102 and is 9,524 characters. It explains the ordinary report's complete-window stop at 4,096 characters. The original text remains inspectable and the report action remains `abstain`.

Defer the model comparison on this case. Direct lookup recovers the upstream statements and the inspected wrapper behavior, while target use of either affected condition remains unestablished. A model would still need a source-bound selector call or fixture to make an applicability claim. Reopen that task when such evidence is available and a specific explanation problem survives the deterministic baseline.

The next product decision is whether the existing complete changelog-window boundary is adequate for its Python-support task on large individual releases. Use the existing tagged-text access and complete-window refusal as the baseline. The observed 4.0 section already exceeds the cap, so separating releases alone would still stop on this case. Any review of that boundary should preserve coverage, citation alignment and explicit stops before justifying a design or implementation change.

[Exact-head and wrapper verification](evidence/2026-11-28-mapproxy-selector-use-screen/verification.json)

`UP-SKILL:upgradepilot-repository-audit` · `UP-SKILL:upgradepilot-working-memory`
