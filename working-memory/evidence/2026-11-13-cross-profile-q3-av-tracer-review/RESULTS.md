# Q3 — AV-Tracer/HTTPX: Combined Source and Historical CI Investigation — retained verification

**Review date:** 2026-11-13. **Role:** Reconcile one *previously qualified* live opt-in investigation with the current installed application's **offline** reader. This is **not** a new live PR acquisition, a new model call, or a contemporary end-to-end requalification of the opt-in producer.
**Original live qualification:** [2026-11-12 recorded receipt](../2026-11-12-av-tracer-native-ci/qualification.json), product commit `42020f17`.
**Review counterpart:** [Q3 product-behavior and decision-time analysis](ANALYSIS.md). **Controlling plan:** [cross-profile qualification](../../../plans/CROSS_PROFILE_REAL_PR_END_TO_END_QUALIFICATION_EXECUTION_PLAN.md).

## Exact historical evidence scope

- Target [`ivaronkun-Ahey/AV-Tracer#11`](https://github.com/ivaronkun-Ahey/AV-Tracer/pull/11), HTTPX `0.25.2 → 0.28.1`. Original frozen base `527a004918c0f825e97c3583404242605fd58ec2`; head `25e7205f39103456e7efbc4e9f503f3debc7b5d8`.
- The previous live `caller-signature-ci` **opt-in** CLI execution selected exactly GitHub Actions run `41416124208`, attempt `1`, failed backend job `125180284415`, with explicit frozen expected base/head, authorized private authentication and a Workspace. One accepted live combined invocation exited `0` on commit `42020f17`. The older source-only capture was retained independently. Do **not** describe this as a current-baseline live acquisition.
- Original CI log: **25,609 bytes**, retained full-log **digest only** `fcb416d9f1d04d5f0588caaef91cf3dd55dc64740fa92402fc749b442e45298b`. In this **same selected job**, an `httpx-0.28.1` successful-installation token was recorded at line **240**, and the unexpected-keyword `TypeError` at line **267**. Saved `source-48` retains the **69-character error excerpt** `TypeError: Client.__init__() got an unexpected keyword argument 'app'`, *not* the full job-log text.
- The source/comparison side retains **six conditional witnesses**: five bound and one rejected. In the relevant witness, the sampled Starlette `TestClient` forwarding at `source-29 L399` calls HTTPX `Client.__init__` with `app=`; HTTPX `0.25.2` has an accepted named parameter, while `0.28.1` yields `violation_0 = unexpected_keyword: app`. That is a **source/signature result under recorded caller, callee and dispatch premises**; it does not bind the exact imported module of the observed failing process.
- The source-only report remains `abstain` and has **no** `ci-job-log` assessment. Combined report adds exactly one `ci-job-log=observed_keyword_error` assessment and two source references, `source-48` (retained excerpt) and `source-49` (producer result). Both reports explicitly leave **ordinary CI dependency coverage and runtime-state** `not evaluated` because those are not the opt-in selected-log profile's proof families.

## Independent current-reader recovery (no new remote acquisition)

The reviewed public [AV-Tracer archive](../../../examples/av-tracer/README.md) was verified against SHA-256 `ffb9365e034833ce4ba3cd35be2080b099d331271b76214e241e6d3a8e115990`. All ten manifest-listed members were independently digested. The two reports and SQLite stores were extracted into a private `0700` directory with `0600` files, *outside Git*.

| Retained item | Verified SHA-256 |
| --- | --- |
| Source-only JSON report | `85fd07790ebb0e44eecda9b1f6688251e1d0dec7dc2d340dc66beb9105d69bd3` |
| Source-and-CI JSON report | `e307eb2843cd4b5a63319b869f06907e8f4d8da867511554994e436acb4f8850` |
| Source-only SQLite Workspace | `b639287d5684db65240f10eac65b3304de4e4397c7042a2719c766b4934d7600` |
| Source-and-CI SQLite Workspace | `f244c2614052f5eceb68c66807d8a254c2f8faff13fbe8e1da0fcc58a968dbf9` |

The **current installed public CLI reader**, using the source-identical wheel built from `50f94fec713077122a8791e5e6f1495307fbf22a`, completed **six private offline subprocess checks with exit 0**:
1. Open original source-only JSON.
2. Open combined source-and-CI JSON.
3. Open original source-only SQLite revision `80a58d494a8c46009aab8dc72b94b447`.
4. Open combined SQLite revision `b2a491b4b7864342b920fe51a0694f4c`.
5. Show `source-48` from the combined Workspace, with the exact unexpected `app` error.
6. Show `source-29` from the source-only Workspace, with retained original Starlette source text.

This new check establishes **current offline JSON/Workspace reader compatibility and recoverability**, not current live opt-in ingestion, source-download reliability, GitHub API availability, same-process module identity or upgrade causality. Current offline check receipts remain private with SHA-256 `93b7727b5e9d7045324ca0618b84b2a33ea58ab0742440a406bef1abb9017dd7`. No raw source/code execution, target repository writes or local LLM inference were performed.

**Verification-method correction:** The first *aggregate review script* expected a different rendered CI-heading phrase and refused to complete its assertion. I checked the actual saved rendering; the supported heading is “Selected historical CI job-log observation: observed_keyword_error.” The verifier text check was corrected; the six successful reader commands and original evidence were **not rerun or edited**.

## What is and is not supported

**Supported within this historical route:** exact selected PR/run/attempt/job identity; source-level old-versus-new `app` signature comparison; selected job's installation token and later traceback text; precise source/excerpt identities and limits; source-only preservation; native SQLite and JSON offline recovery; conservative `abstain`.

**Not established:** the particular HTTPX `__file__` and `__version__` loaded by the failing Python process; a proof that the updated dependency *alone* caused the observed failure (counterfactual); whole-workflow CI coverage or normal dependency-consumption/run-state correlation; active decision-time maintainer usefulness; a current live opt-in producer pass. The full original job log is **not** included in the archived report; a digest is provenance for the historical log, not reconstructible original bytes.

**Next learning/ownership:** Review [Q3 analysis](ANALYSIS.md) alongside the earlier [native-bridge Build cycle](../../2026-11-12_ci_job_diagnostic_native_bridge_build-cycle.md). Ali's conceptual and independent evidence-reasoning discussion is a separate D gate; do not mark it passed merely because this historical archive opens. **Q4 — Active Open-PR CI/Runtime Correlation Case** remains a *conditional, not-started* proposal.
