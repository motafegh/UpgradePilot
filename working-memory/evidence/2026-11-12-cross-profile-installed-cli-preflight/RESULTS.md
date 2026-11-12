# Cross-profile qualification — installed CLI readiness evidence

**Date:** 2026-11-12
**Responsibility:** Local installation, offline product smoke, subprocess deadline and receipt. **No new public PR acquisition, local-model inference, target code execution or target mutation occurred.**
**Source baseline:** `50f94fec713077122a8791e5e6f1495307fbf22a` (wheel build).
**Disposition:** Installed-product preflight passed. Live case identities, model readiness and case-specific admission remain open.

## Isolated installed application

- Created a new owner-private Python **3.12.3** virtual environment outside the checkout. The existing development `.venv` was **not changed**. The local checkout was first fast-forwarded to the then-current remote `main`, preserving the unrelated untracked working-memory file.
- Built a standard Python wheel from that checkout and installed it with project-declared runtime dependencies. `pip check` returned no broken requirements.
- Wheel: `upgradepilot-0.0.0-py3-none-any.whl`, **410,203 bytes**, SHA-256 `190257ec38328a340cf2132513e09432c8f594af4c51da218bfad81cfca420ca`. The package metadata version `0.0.0` is not a source-commit identity; use the frozen commit, wheel hash and installed-file parity together.
- The actual installed `upgradepilot` entry point resolves to `upgradepilot.cli:main`. Six material installed imports matched source SHA-256 bytes: CLI, investigation, report projection, GitHub API, PyPI API and local semantic extractor. Installed dependencies include requests **2.34.2**, packaging **26.3**, PyYAML **6.0.3** and the specified tree-sitter grammar versions.
- Installed CLI `--help` passed. A nonexistent offline report was refused without external acquisition.

## Minimal process supervisor and independent checks

The new [supervisor](../../../tools/run_qualification_cli.py) invokes the **installed public CLI unchanged** in a fresh subprocess. It creates private, non-overwriting output; records stdout/stderr, exit status, elapsed time and an optional report digest; and applies a parent deadline with process-group termination. It **does not** intercept HTTP, replace any evidence producer, block a naturally admitted model call or claim exact HTTP/model cost.

**Seven focused offline tests passed** in [the regression tests](../../../tests/test_run_qualification_cli.py): exit/stdout/stderr/report-digest preservation, stalled-process deadline, spawned descendant cleanup, existing-output refusal, invalid executable, nonprivate output-parent refusal and invalid deadline.

The installed CLI reopened both historical AV-Tracer JSON reports from the reviewed archive **offline**, showing `Rejected keyword: app` and `Maintainer action: abstain`; the combined report additionally showed the selected historical CI observation. It also reopened retained `source-48` text containing the observed unexpected-keyword traceback. All three supervised offline operations exited **0**. These are reader-compatibility checks, not new live acquisition or causal regression proof.

A full `unittest discover -s tests -v` run in the isolated installed interpreter finished **1,121 tests passed** in the test runner's reported **232.137 seconds**. These tests include the seven new supervisor tests. This establishes controlled regression integrity, not general production reliability or a representative performance estimate.

## Private retention and proof limits

The owner-only `installation-preflight-receipt.json` contains wheel and source provenance, module SHA-256 parity, dependency versions, full test log checksum, offline-reader receipts and timestamps. Private receipt SHA-256: `e6d419f1ad18706467105e52f2917ed4bafb469038abce3f2b194b1e0cb4f32e`. Private installation logs and the extracted old reports remain outside Git. This public note intentionally omits machine-specific paths, credentials and raw third-party bodies.

**Not yet qualified:** the live **Q1 — CARLA/OpenCV: Normal Dependency and Artifact Investigation**; live **Q2 — Pydantic/Soup Sieve: Normal Investigation with Conditional Local Language Model**; model dispatch or grounding on the current installed product; global HTTP request/decoded-byte limits; external expected-SHA refusal before the normal CLI's first changed-file fetch; or general product correctness.

**Next required gate:** separately validate and freeze the actual public Q1 — CARLA/OpenCV PR identity/dependency transition, credentials/proxy/quota and one private invocation/report destination; receive per-case live-acquisition admission. Review that result before freezing Q2 — Pydantic/Soup Sieve, with same-invocation model-call observability. Q3 — AV-Tracer/HTTPX: Combined Source and Historical CI Investigation remains an archived reference. Preserve actual partial/blocked results and mark unmeasured fields `not_measured`, not zero.
