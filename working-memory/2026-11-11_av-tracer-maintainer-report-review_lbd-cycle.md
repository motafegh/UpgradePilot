# AV-Tracer saved-report maintainer review — Learning-by-Doing cycle

Date: 2026-11-11  
Session status: PAUSED — review evidence established; learner ownership check and cycle closure pending  
Primary operation: bounded read-only maintainer-report review, with Learning-by-Doing  
Selected plan: [AV-Tracer maintainer-task review and evidence checkpoint](../plans/AV_TRACER_MAINTAINER_TASK_REVIEW_AND_EVIDENCE_CHECKPOINT_PLAN.md)  
Prior qualification: [exact-version allocation build](2026-11-11_caller-signature-exact-version-allocation_build-cycle.md) · [public-safe receipt](evidence/2026-11-11-av-tracer-exact-version-allocation/qualification.json)

UP-SKILL:upgradepilot-repository-audit. UP-SKILL:upgradepilot-learning-by-doing. UP-SKILL:upgradepilot-working-memory.

## Cycle state and learning map

- A0 — DONE: Current GitHub `main` was `a84267ca` (planning-only continuation after qualification); local WSL checkout remained at `af92c23f` with an unrelated untracked file, left untouched. The plan, receipt, governing caller/signature/report/AI boundaries, and actual private saved artifact were located.
- A1 — DONE (prior agreed continuity): Ali approved the integrated evidence → explanation → applicability → AI-decision sequence in the preceding discussion and explicitly selected execution of that plan. The historical 1,099-test and offline-cold-open outcomes were not rerun here.
- A2 — DONE (prior agreed task): Fix the maintainer question, inspect the native saved report and retained original sources; evaluate fidelity, navigation and decision relevance separately, preserving conditional source versus unobserved runtime proof. Prior detailed plan discussion and explicit go-ahead compress repeated pre-review gates; they do not waive later review/learning decisions.
- B — DONE for saved-report review and deterministic diagnostic. No code, model, provider requests, target execution or test runs.
- Verification — GREEN for file/read-only evidence integrity; incomplete for independent usefulness. Actual report SHA-256 and exact source inspection were verified, as detailed below.
- D — CURRENT: one ownership question remains for Ali concerning source-level mismatch versus CI/runtime proof.
- E — PENDING: consolidate after learner response and select the separate combined-evidence/runtime checkpoint.
- C — CONTINUOUS: this record preserves report/source observations, a presentation shortcoming, source/renderer ownership, an environment-specific CLI caveat and proof limits.

Learning bridge: `TestClient(app)` is a target-source fact; the sampled FastAPI re-export leads to sampled Starlette, which passes `app=` to a candidate HTTPX base initializer; a version-specific signature check is **not** proof that the particular CI job executed that route with those installed files. A useful report must make both the mismatch and the proof boundary visible.

## Exact private saved-report admission

Read the retained `report.json` and its offline textual CLI reopening under the owner-only `$HOME/.local/share/upgradepilot/av-tracer-exact-allocation-2026-11-11.v6SbOe/` capture; the original source-bearing artifact remains outside Git. Verified:

- Saved report SHA-256 `85fd07790ebb0e44eecda9b1f6688251e1d0dec7dc2d340dc66beb9105d69bd3` equals the [qualification receipt](evidence/2026-11-11-av-tracer-exact-version-allocation/qualification.json).
- Saved report ID `99a373c2-98d0-43ee-8a4b-2e7c449e82ba`; generated `2026-11-11T13:32:42.617144+00:00`; footer confirms revision `80a58d494a8c46009aab8dc72b94b447`.
- Exact PR `ivaronkun-Ahey/AV-Tracer#11`, base `527a004918c0f825e97c3583404242605fd58ec2`, head `25e7205f39103456e7efbc4e9f503f3debc7b5d8`, HTTPX `0.25.2 → 0.28.1`.
- Read-only `PYTHONPATH=src .venv/bin/upgradepilot --open-report <retained-report> --show-source <id>` reopened `source-28`, `source-16`, `source-29`, `source-31`, and `source-36` from the saved artifact without new GitHub/PyPI collection.
- A first `.venv/bin/upgradepilot --show-source` invocation without `PYTHONPATH=src` rejected the option: the local installed import path was older than the current checkout's CLI. Setting the source import path resolved the local diagnostic. Treat this as a **local invocation/version-selection caveat**, not proof that the current product CLI omits the feature or that packaging is generally broken.

## What a maintainer can establish today

The actual report opens with `Review at a glance`, source-only conditional caller/signature evidence and a direct old-versus-proposed outcome:

- `source-28`: exact target-head `backend/tests/test_app.py:6` contains a **module-level** `client = TestClient(app)` imported via `fastapi.testclient`.
- `source-16`: sampled FastAPI 0.104.1 `fastapi/testclient.py:1` reexports `starlette.testclient.TestClient`.
- `source-29`: sampled Starlette 0.27.0 `starlette/testclient.py:399` calls `super().__init__(app=self.app, base_url=..., headers=..., transport=..., follow_redirects=True, cookies=...)`.
- `source-36`: old HTTPX 0.25.2 `httpx/_client.py:620` declares a named `app` argument in `Client.__init__`; all six relevant keywords bind in the candidate source comparison.
- `source-31`: proposed HTTPX 0.28.1 `httpx/_client.py:639` lacks a named `app` parameter and records `unexpected_keyword: app`. The other five forwarded keywords bind.

**Conditional answer:** Yes: if the relevant execution imports the sampled Starlette forwarding implementation and resolves its `super()` call to the compared proposed HTTPX constructor, `app=` will be rejected by that declared signature. At the test module's top level, reaching `TestClient(app)` could expose this during pytest collection/import. This is a supported source-level conflict, **not an observed error** from this run.

**Not established:** actually installed FastAPI/Starlette/HTTPX files and versions in the target test environment, effective import/MRO/dispatch, whether this execution reaches the candidate body, actual exception, CI failure cause, update safety, complete impact coverage, or non-abstention maintainer-action permission. The saved report explicitly states CI dependency coverage and runtime state **not evaluated**, partial acquisition (24 retained source files, 33 material omissions), six conditional witnesses, and continued abstention.

**Decision-critical possible next observation:** recover already retained exact-head backend pytest traceback and installation/import record *if available*, and check both (1) that the actual execution reached `TestClient` / the `app` forwarding call and (2) the concrete loaded package/file identity. Missing traceback or version proof remains unresolved; the historical failed job must not be retroactively attributed to this signature witness.

## Evidence versus explanation versus decision value

**Fidelity — positive for the admitted static comparison.** The report's opening connects exact PR/version roles, root call, compared call, the old/proposed fit result, and conditional/CI unknowns. Its detailed facts and offline source opens support the central source-level mismatch. No false causal CI claim was found in the inspected sections.

**Usability — material, precisely located gap.** The saved textual view is **5,602 lines / 252,212 bytes**. Its opening around lines 21–29 says `Old: arguments fit`, `Proposed: arguments rejected`, but does **not** name the failing `app` keyword or explain the forwarding mechanism. The proposed witness begins near line 2423; `Keyword reception: app: not_received` is at line 3715 and `Local violation: unexpected_keyword: app` at line 3721. The corresponding old `app: named_parameter` fact appears at line 5046. Large repeated path-source bodies dominate detailed witnesses. These are **location/navigation proxies from this one textual rendering**, not measured human time or an independent-reader result.

**Decision utility — partial.** The first view asks what installed version/import binding/runtime dispatch applies and rightly withholds action. It does not offer a concise, prioritized next observation for distinguishing a static risk from an observed test failure. The exact source citations make a bounded investigation possible; they do not yet prove that maintainers are faster or make better decisions.

**Smallest credible transparent baseline (proposed only, not implemented or independently tested):** Within the same admitted facts and sources, put this alongside the old/proposed result: “Sampled Starlette 0.27.0 forwards `app=` to `httpx.Client.__init__`; HTTPX 0.25.2 accepts it and 0.28.1 rejects it. This finding applies only if the target execution imports that implementation and reaches that callable. Check the actual installed/loaded versions and relevant pytest traceback before claiming an observed failure.” Link `source-28/16/29/36/31`; retain omissions and unresolved CI/runtime state. This requires no new evidence, inference or architecture.

**Responsible placement:** The native witness projection already retains `Keyword reception` and `Local violation` facts in `src/upgradepilot/report_projection.py`, while `src/upgradepilot/report.py::_signature_overview` renders only outcome labels/root/call/unknowns. The gap can plausibly be corrected in existing native presentation ownership, with a consistency check for ambiguous/multiple witnesses; it is **not** evidence of a missing acquisition parser or an AI-only reasoning requirement. No code change is authorized by this review.

### Source-only disposition

**Continue as a bounded pilot; defer a general maintainer-usefulness/adoption claim.** The selected static mismatch and source provenance are real and useful, but the current textual layout imposes substantial evidence-navigation cost. A narrower deterministic view is the justified first comparator; the pilot does not grant a block/merge conclusion or imply runtime proof. AV-Tracer is exposed development evidence, not a fresh transfer holdout.

The [combined-evidence/runtime-applicability checkpoint](../plans/CALLER_SIGNATURE_NATIVE_ADOPTION_AND_QUALIFICATION_PLAN.md#16-combined-evidence-and-runtime-applicability-design-checkpoint) is the **next separate review responsibility after the learner check**. Its work has not been performed in this cycle. The scheduled AI design checkpoint has likewise **not** been decided; this report-level presentation gap alone does not justify model inference.

## Ownership check and pause boundary

Reasoning question for Ali: **If the target's backend pytest job failed at this exact PR head, why does that fact alone not prove UpgradePilot's `app=` signature mismatch caused the failure? Which concrete execution evidence would strengthen or falsify the proposed causal link?**

The expected learning obligation is to separate the source hypothesis from observed test execution, resolved runtime file identities and traceback attribution, not to memorize a line number. After this discussion, complete D/E in this record and make the next plan checkpoint active in `MEMORY.md` only if the live responsibility changed. Preserve the existing local untracked file and the owner-only report.
