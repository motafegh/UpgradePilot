# Q3 — AV-Tracer/HTTPX: Product-behavior and maintainer-decision analysis

**Date:** 2026-11-13. **Role:** Historical combined source/signature and *exact selected CI job log* investigation; current installation checked only for offline recovery. Not an active-PR utility experiment or fresh opt-in provider exercise.
**Evidence owner:** [RESULTS.md](RESULTS.md), [original live receipt](../2026-11-12-av-tracer-native-ci/qualification.json), [native CI Bridge Build cycle](../../2026-11-12_ci_job_diagnostic_native_bridge_build-cycle.md).
**Decision state:** prior implementation and real historical scope qualified; current-reader recovery passed; D learner ownership **not automatically closed**, E final closure pending.

## What we asked this case to test

The optional `caller-signature-ci` execution profile was deliberately designed to combine **two narrower facts**, without claiming they establish a full upgrade-caused CI failure:

1. A **conditional source comparison** of the same captured Starlette caller interacting with an old versus proposed HTTPX constructor signature.
2. An **observed error-text excerpt from one explicitly selected historical GitHub Actions job**, with exact PR revision, run, attempt, job, full-log digest and line numbers.

The result is useful when a maintainer asks: “Does the new HTTPX API appear incompatible with this captured caller, and does the selected CI job show the same error signature?” It cannot fully answer: “Did that upgrade cause this failing test, which actual dependency file executed, and should we merge or block?”

## Execution/first-stop matrix — distinguished from ordinary dependency investigation

| Capability or proof | What was actually exercised | Earliest limitation / interpretation |
| --- | --- | --- |
| PR and head/base freeze | **Established** in prior live opt-in run: exact `AV-Tracer#11` base/head; explicit run `41416124208`, attempt `1`, job `125180284415` | User-selected exact historical run/job, not automatic CI discovery. A different attempt/job, even with matching error text, cannot be substituted |
| Source acquisition and caller/callee roles | **Six comparisons**, five `bound`, one `rejected`; tagged/sampled Starlette and HTTPX source references retained | Conditional on captured source roles, root call, paths and dispatch/binding assumptions. Does **not** show target project test actually reached that Starlette version/call path |
| Old HTTPX `0.25.2` | Static `httpx.Client.__init__` accepted `app=` under the captured caller/binding rules | A source-level old-version compatibility fact, not evidence that historical target tests ran successfully with old release |
| Proposed HTTPX `0.28.1` | Same witness rejected `app=`, with `violation_0 = unexpected_keyword: app` | Source mismatch, not yet an observed failing import/test |
| Historical exact job read | Previously executed; one selected failed backend-job log yielded `httpx-0.28.1` installation summary line **240** and `TypeError: Client.__init__() got an unexpected keyword argument 'app'` line **267** | **Observed textual correlation in a single selected job**, but installation summary does not establish which version/file pytest actually imported |
| Exact process/module identity | **Not established** | Missing direct `httpx.__version__`, `httpx.__file__`, and concrete failing call/dispatch identity **inside the relevant execution environment** |
| Upgrade counterfactual | **Not established** | Would require a suitably controlled old/new dependency comparison holding relevant source, environment and path constant and showing differential execution, not merely source text and one job's error |
| Full CI workflow/job/step consumption | **Outside selected proof family**; ordinary `ci` and `runtime` remain `not evaluated` | The selected-log profile is not a substitute for normal full workflow YAML ↔ executed step ↔ dependency-consumption correlation |
| Upstream project/LLM | **Outside selected profile** | Q3 does not invoke the ordinary conditional upstream Python support-drop model; `not_evaluated` here is expected profile selection, not a missing model-provider failure |
| JSON/source retention | Original source files retained; the selected job's **69-character error excerpt** and original **full-log SHA-256** retained | Full job log bytes **not retained**, so offline replay can verify saved excerpt/declared digest but cannot reconstruct the full original provider response |
| Native SQLite Workspace | Prior exact revision recovered; current installed reader independently reopened both frozen Workspace revisions and source excerpts | **Durable offline compatibility established**; current live opt-in acquisition/correlation still not exercised |
| Maintainer action | `abstain` in both source-only and combined reports | Correctly refuses an upgrade-safety or merge decision. Whether the diagnostic improves a real maintainer's next action is **not independently tested** |

## Why source agreement + CI error still isn't causality

**`TestClient(app)` → Starlette forwards `app=` → `httpx.Client.__init__` → HTTPX 0.28.1 rejects `app`.** is the **static, conditional mechanism** supported by the captured source files. The separately selected failed job includes both a successful-installation text token for `httpx-0.28.1` and the same unexpected-keyword error.

These facts increase the **plausibility of a concrete upgrade-related incompatibility hypothesis** but do not supply the missing runtime links:

- The installation log token is not evidence of the *same Python interpreter's actual imported module/version/file*. Multiple environments, import paths, preinstalled packages and step scopes can differ.
- The error text identifies the keyword and callable, but on its own does not bind the selected Starlette source, dependency version or exact runtime call stack to the saved comparison.
- One observed failing job does not establish that an otherwise identical old-version run passed. Without a controlled contrast, assigning *all* failure causality to the dependency update would overstate the evidence.
- Selected job identity and SHA are essential. A matching exception in a **different** attempt, job or PR head is separate evidence, not interchangeable with the selected receipt.

A future stronger diagnosis would require **per-execution environment identity** (Python interpreter, installed distribution/version, module `__file__` and `__version__`, exact test command/path and traceback), and only then a separately bounded **counterfactual comparison** if upgrade-caused failure must be established. That is a recommendation for an evidence design, **not** authorization to execute untrusted target tests or mutate the public PR.

## Product usefulness and engineering implications

This case is more actionable as a *debugging orientation* than an ungrounded “it might break” warning: it names the precise forwarded keyword, old/new interface difference and the selected error. However, the product does not yet provide supported non-`abstain` action permission. A maintainer can investigate with better specificity, but UpgradePilot cannot certify the full upgrade disposition on current evidence.

The optional exact-job route has an important positive safety property: **a chosen failed job cannot silently become a claim about a different job or attempt**. Its principal product limitation is narrower scope, not missing code in the normal CI analysis. The full original job-log material is intentionally not retained, which helps privacy/resource bounds but limits later independent inspection; an archive digest by itself cannot restore discarded bytes.

## Contrasting Q1/Q2/Q3 — what is covered and what remains

- **Q1 — CARLA/OpenCV: Normal Dependency and Artifact Investigation:** fresh ordinary CLI case proved package artifact differences, but no exact-head runtime records and no authoritative upstream publisher provenance; model not reached.
- **Q2 — Pydantic/Soup Sieve: Normal Investigation with Conditional Local Language Model:** fresh ordinary CLI case reached a real local model, grounded a Python-3.8 support-drop claim against tagged changelog and evaluated Pydantic's declared Python range. Exact-head CI run/job records existed, but no retrieved step details and no admitted consumption correlation.
- **Q3 — AV-Tracer/HTTPX: Combined Source and Historical CI Investigation:** prior **opt-in** profile connected conditional source signature mismatch with an *exact selected job* TypeError; current JSON/SQLite replay passed, but no fresh current opt-in acquisition and no proof of imported version or causal regression.

The three cases therefore cover **different evidence mechanisms**, not three independent repetitions of the same complete normal pipeline. All are historical; none establishes current maintainer utility on an actionable PR. The next optional **Q4 — Active Open-PR CI/Runtime Correlation Case** should only be admitted to answer a precise missing ordinary-profile run/job/step consumption question—not because Q3 was skipped.

## Hypotheses to retain, without automatic feature changes

| Candidate question | Needed discriminating evidence | Status |
| --- | --- | --- |
| **R1 — Exact imported runtime dependency identity**: should selected-log diagnostics report a measured version/file identity when safely captured? | Bounded source and execution metadata in *the same observed process/step*; failures where installed and imported versions disagree | **Research/producer-boundary question**, not a Q3 implementation defect proved by this historical excerpt |
| **R2 — Consumer-facing actionability**: could an accurate conditional mismatch + observed same-job error guide a maintainer's next check more effectively than a generic abstain? | A task-based reviewer comparison on complete, permissioned evidence; evaluate decisions, calibrated uncertainty, source inspectability | **High practical utility question**, separate from binary source/CI correctness |
| **R3 — Source-versus-log preservation balance**: is the original-source/digest/excerpt combination sufficient for later independent review? | Reviewer exercise with private full log at original decision time and archived excerpt; explicit retention/privacy cost analysis | **Conditional**, not blanket full-log persistence |
| **R4 — Current-profile applicability**: does the present installed opt-in live source/CI flow still work when a suitable actionable case is available? | Separately admitted live case with exact source and selected job availability and current code identity | **Not currently verified**; do not conflate with planned ordinary-profile Q4 or rerun stale evidence just for a green check |

## Learner ownership gate (not automatically marked complete)

A useful engineering question is:

**Suppose a second GitHub Actions attempt produces the identical `TypeError`, while the original archived receipt names attempt 1. Can we use the second attempt's log as evidence for the original exact-job claim? What would we additionally need to prove that HTTPX `0.28.1` was actually the module imported when the failing test executed?**

The right reasoning should separate **identical error text** from **same observation identity**, and then distinguish **package installation text** from **same-process module identity**. Ali's prior demonstrated claim-discipline is recorded separately; this newer specific check still requires an explicit user answer before D learner ownership can be closed. E closure and any Q4 selection also remain open.
