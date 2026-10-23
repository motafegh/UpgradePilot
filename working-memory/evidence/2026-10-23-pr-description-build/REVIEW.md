# PR description preservation and offline source inspection — verified result

Recorded October 23, 2026. Product implementation: `85491b89`; subsequent checkpoint-test compatibility corrections and evidence publication are in the same [Build cycle](../../2026-10-23_pr-description-and-offline-source_build-cycle.md). Contract: [report plan §10](../../../plans/MAINTAINER_REPORT_PRESERVATION_AND_USEFULNESS_EVALUATION_PLAN.md#10-pr-description-preservation-and-offline-source-inspection-design).

## Delivered consumer behavior

The normal investigation now preserves its initial PR description observation through shared preparation, an additive native family and direct Workspace-to-report projection. The source remains the report's existing PR source. Its state, actual observation time, API URL, decoded-text digest and measured byte count are explicit. Missing/null/invalid/oversized bodies do not erase valid other evidence. The 256KiB UTF-8 bound rejects full retention rather than inventing a partial body; historical absence remains not recorded.

Saving remains opt-in. A maintainer can inspect the actual retained source ID listed in a saved report:

```text
upgradepilot OWNER/REPOSITORY NUMBER --save-report PATH
upgradepilot --open-report PATH --show-source SOURCE_ID
```

The viewer displays literal source with attribution and limitations, removes nonprinting controls from display and preserves saved text/hash. HTML/Markdown/instructions remain untrusted source data. It performs no network/provider/synthesis operation, follows no URL and writes no file. Empty retained text succeeds; invalid arguments, bad file, unavailable source and canonical projection failures have distinct exits2/6/7/8. Ordinary summaries do not dump descriptions or imply a durable file without saving.

Public schema1, existing identity/input layouts, checkpoint schemas, CI/Python input closures and maintainer-action policy are unchanged. New reports record generator2; renderer2 declares its display identity. The default experimental native offering remains limited to its existing dependency/CI families.

## Real retained-case result

| Controlled composition | HTTPX PR20 | OpenCV PR1111 |
| --- | --- | --- |
| Full description retained |9,348 UTF-8 bytes |5,902 UTF-8 bytes |
| Requests consumed from frozen packet |8 |13 |
| Added requests |0 |0 |
| Existing assessments/findings/unknowns/action |Unchanged |Unchanged |
| Save/open/source-view parity |Pass |Pass |
| Original inputs/reports unchanged |Pass |Pass |

[Receipt](retained-case-receipt.json) and [finite recipe](verify_retained_cases.py) bind all original HTTP body hashes and both public/private original reports. Normal provider/domain composition produces new records from controlled response inputs. These are separately identified controlled outputs, not a fresh live acquisition or an official historical rerun. New observation timestamps describe the controlled interpretation, never the October22 acquisition. Status-only404 inputs have unreadable bodies, so new consumption would fail instead of fabricating an empty server response. Full new reports/source views/native records remain private with restricted permissions; no wholesale API dump was added to Git.

The result exposes previously lost copied release context for inspection. It does not interpret that context, repair the broader Investigator or alter an upstream authority decision.

## Verification and corrections

- Full deterministic product regression: **908 tests/130.019s, OK**. Command: `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src:tests:. .venv/bin/python3 -m unittest discover -s tests -q`.
- Focused provider/application/native/report/CLI/source checks:103 tests/68.270s, OK. Separate checkpoint checks after their correction:48 tests/40.827s, OK. These overlap the full suite and are not added to its denominator.
- Product tests protect representation states, byte/Unicode bounds, same-head description edits, identity/acquisition failures, exact stored versus sanitized display text, supported/unsupported dependency composition, optional version isolation, target/reference/hash corruption, offline source/file/argument outcomes and cold-process checkpoint source reconstruction with re-entry forbidden.
- Source-capture diagnostic:9 tests/1.080s, OK. Its two-run parity assertion now injects a shared observation clock rather than erasing a recorded timestamp.
- [Historical compatibility receipt](historical-report-receipt.json):6/6 historical reports strictly decode/round-trip/reopen; original hashes/generator identities remain unchanged; zero network attempts.
- [Installed receipt](installed-receipt.json) and [recipe](verify_installed.py): a new venv installed the package through normal package-index access. `pip check`, console/module help and actual installed console-script source viewing succeed outside the checkout. Provider/network/synthesis/save calls are forbidden during both full-case views.32 focused tests also pass against the installed package/0.444s, with `src` absent from PYTHONPATH. Distribution versions are recorded; no project dependency changed. Hosted verification was not invoked.
- Initial failures remain recorded in [validation progression](validation-progress.json):94-test focused run had5 failures, and first908-test regression had11. Older native/checkpoint tests hard-coded the old family cardinality or assumed every family fed CI/Python. Scope/count expectations were corrected and independent source-specific checks retained; no runtime owner was loosened to satisfy those tests.
- Sampled historical research migration experiment:9 tests with10 errors on both unchanged `5a1a7641` and changed product source. Its obsolete application-level `analyze_dependency_change` patch seam predates this cycle. This existing experimental compatibility debt is explicitly deferred; it does not invalidate the passing source-access/product checks.

## Acceptance and limits

The selected offline source-access responsibility is delivered and evidenced. Source bodies remain copied/unverified PR context, with upstream coverage unassessed. Integrity is consistency, not authenticity. Runtime dependency state, target impact, compatibility and stronger action permission retain their previous proof boundaries. General replay, complete Workspace migration, broader semantic correctness, independent maintainer utility and learner mastery are not established.

Useful separate learning topics: identity versus mutable observations; absence/empty/problem/history distinctions; additive versioned transfer and scoped refusal; immutable input closure; exact stored versus safe displayed text; deterministic clocks in comparison tests; why cardinality tests should track the submitted boundary rather than freeze a historical architecture.

The next responsibility is reviewing what the newly accessible context enables in a concrete maintainer task and selecting the next justified product gap. It does not automatically trigger a third capture, semantic/model changes or a new action rule.

UP-SKILL:upgradepilot-build-implement
UP-SKILL:upgradepilot-working-memory
