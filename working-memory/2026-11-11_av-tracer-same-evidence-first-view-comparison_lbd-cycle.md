# AV-Tracer frozen-evidence first-view comparison — Learning-by-Doing cycle

Date: 2026-11-11
Primary responsibility: read-only **development** comparison of the actual original versus updated first-view renderer on the same frozen AV-Tracer saved report; distinguish improved access to an already known fact from independent maintainer usefulness.
Governing plan: [Maintainer report usefulness — saved first-view and independent usefulness boundaries](../plans/MAINTAINER_REPORT_PRESERVATION_AND_USEFULNESS_EVALUATION_PLAN.md#first-view-comparison-on-saved-reports)
Previous verified Build: [First-view precision Build](2026-11-11_av-tracer-signature-first-view_build-cycle.md)
Related original receipt: [Public-safe AV-Tracer report packet](evidence/2026-11-11-av-tracer-exact-version-allocation/REPORT_REVIEW_PACKET.md)

UP-SKILL:upgradepilot-repository-audit. UP-SKILL:upgradepilot-learning-by-doing. UP-SKILL:upgradepilot-working-memory.

## Cycle state
- A0 — DONE: current `main` reconciled at `634bf33c365fea6ca17a5a6cdb42899c9e6353e9`; local WSL `main` fast-forwarded non-destructively to that exact head, unrelated untracked October working-memory file left untouched. Baseline original report, original cold rendering and current CLI availability verified. Current saved report digest: `85fd07790ebb0e44eecda9b1f6688251e1d0dec7dc2d340dc66beb9105d69bd3`; original `cold.txt` digest: `32d1338d5d42ded6b2834fe764df57f71b17a1faa985ad55f947944d307ac182`.
- A1 — DONE at continuity-compressed depth: immediately prior session taught evidence/renderer separation, tested `app` versus `option` and missing/conflicting witnesses, and closed the 1,100-test Build; Ali explicitly approved the proposed same-saved-evidence next comparison. No new scope/authorization choice before this read-only task.
- A2 — DONE at continuity-compressed depth: freeze the maintainer task and permitted evidence; compare **actual** saved original `cold.txt` against current cold `--open-report` rendering. Evaluate exact truth and evidence limits, first-view placement, mechanical navigation proxy and missing next observation. Do not equate analyst familiarity with independent reviewer success.
- B — CURRENT: perform fixed-report comparison, without acquiring new sources, executing target code, modifying product source, or using an LLM.
- Verification — PENDING: confirm both text outputs identify the same saved report, report hash unchanged, original output intact, measured positions and limits accurate.
- D — PENDING: ownership learning on what a renderer-only presentation change can and cannot establish.
- E — PENDING: close with a justified usefulness/next-responsibility disposition.
- C — CONTINUOUS: record actual results, corrections and evidence limits.

## Frozen review design (recorded before comparative output inspection)
- **Task:** Given AV-Tracer PR #11 and the offered report, identify (1) exact HTTPX old/proposed transition; (2) the material caller/signature concern including the rejected keyword and source pointers; (3) static/conditional versus observed installed/runtime/CI proof; (4) material unresolved questions; (5) a decision-relevant next observation if adequately supported, without wrongly attributing CI failure or authorizing maintainer action.
- **Identity/inputs:** `ivaronkun-Ahey/AV-Tracer#11`; exact base `527a004918c0f825e97c3583404242605fd58ec2`; head `25e7205f39103456e7efbc4e9f503f3debc7b5d8`; saved report ID `99a373c2-98d0-43ee-8a4b-2e7c449e82ba`, SHA-256 above, revision `80a58d494a8c46009aab8dc72b94b447`. This is an already exposed development case (prior assistant read detailed evidence and helped build the renderer).
- **View A:** original real `cold.txt` saved at original qualification time (5,602 lines previously recorded), no re-render/reacquisition.
- **View B:** actual current `PYTHONPATH=src .venv/bin/upgradepilot --open-report <same-report.json>` output (renderer on `main` including first-view improvement), not analyst-authored rephrasing; full source and deep details identical in material basis.
- **Access parity:** Both views are provided the *same* underlying saved report, detailed witness content, source IDs and offline source-opening command. Any additional separately recorded historical CI evidence is excluded from the two conditions. The analyst's prior knowledge is disclosed, not hidden.
- **Metrics:** verify identity/hash, text line number of first-view summary and of the first precise `app` violation statement, whether one can answer each task element using the first view alone, exact source refs and limits present, how many **additional section/keyword-navigation operations** a planned analyst route would require to learn the specific rejected keyword. These are *location and planned-navigation proxies*, not independently measured reader effort, actual elapsed human time, causal usability effect or real source opens unless performed and counted.
- **Expected failure modes:** misleading causal CI wording, missing runtime limits, wrong PR/version binding, missing cited source IDs, first view still hiding the exact rejection, or no additional value after accounting for already available search/navigation.
- **Bounds:** Read-only reporting/documentation only, no new GitHub/PyPI live provider evidence, no target tests, models, report schema, code edits, CI traceback retrieval, external reviewer recruiting or independent utility experiment. Contrasting non-AV-Tracer tasks and reviewer independence are outside this single-case development diagnostic; note this as study readiness debt.

## Evidence results

### Same-evidence, same-recovery-route proof

The initial **actual** updated `--open-report` output exposed `Rejected keyword: app` at line 26 while the original saved `cold.txt` had no such first-view line. That initial comparison also showed six unrelated missing Workspace-recovery footer lines, because the two commands used different read routes. This was a **comparability issue**, not a change in product evidence. The original frozen protocol above is preserved as authored; the final comparison **amends the View B recovery route** to `--open-workspace <same retained store> --revision 80a58d49...`, to match View A. A proposed `--open-report`-against-Workspace comparison is not the final result.

The corrected **same exact Workspace revision** comparison is recorded in [machine-readable public-safe receipt](evidence/2026-11-11-av-tracer-same-evidence-first-view/comparison_receipt.json). Its strict line-sequence difference was **exactly one inserted line**: `Rejected keyword: app` at line **26**. No other lines were modified or removed. Original `cold.txt`: **5,602 lines**, SHA-256 `32d1338d5d42ded6b2834fe764df57f71b17a1faa985ad55f947944d307ac182`. Updated same-route text: **5,603 lines**, SHA-256 `713932a8df956f2c3a78dc67e3f802d2c9519c52f24a876a033a7dfdeca8a036`. Original `report.json` remained SHA-256 `85fd07790ebb0e44eecda9b1f6688251e1d0dec7dc2d340dc66beb9105d69bd3`. Both outputs identify report `99a373c2-98d0-43ee-8a4b-2e7c449e82ba`, exactly the same sources and Workspace revision.

Original report's precise rejection `Local violation: unexpected_keyword: app` first appears at line **3,721** in detailed evidence; the updated report still retains that same detailed statement at line **3,722** and adds the first-view value at **26**. Thus the new version makes the keyword visible **3,695 lines earlier** relative to the original detailed position. This is a textual-position metric only, not measured scrolling, elapsed time or independent human benefit.

### Frozen task answer by first-view content

| Required task element | Original first view | Updated first view | Interpretation |
| --- | --- | --- | --- |
| Exact `httpx 0.25.2 → 0.28.1` transition | Present | Present | No difference |
| Caller/signature outcome | Old fits, proposed rejects; `source-28` root and `source-29` compared call | Same plus exact `app` keyword | **One directly useful information-access improvement** |
| Full Starlette-to-HTTPX forwarding explanation and callee signature identity | Not in first view; must inspect detailed source/witness | Still not in first view; must inspect detailed source/witness | No independently established reduction in source opening |
| Source-only and dispatch condition | Explicitly conditional | Unchanged | No authority promotion |
| Installed CI/runtime applicability | `CI dependency coverage: not evaluated`; `Runtime dependency state: not evaluated` | Exactly the same | No new runtime fact |
| Decision-relevant next check | Generic open question about installed version/import binding/dispatch | Exactly the same | No newly prioritized exact-head traceback or loaded-file check |
| Maintainer action permission | `Maintainer action: abstain` in detailed report, not first view | Same `abstain`, still detailed | No action change |

The **full report**, not the first view alone, already contained the decisive keyword and supporting source detail in both conditions. A reader who starts at the beginning now needs **zero additional within-report seeks to discover the name `app`** versus at least **one within-report search/seek to find the explicitly named detail** in the original. This is a *protocol-based minimum-navigation inference* from fixed content, not a recorded human action count or timed usability study. The review was authored by an assistant already familiar with this exact case and renderer implementation; it is **contaminated for independent usefulness evaluation**, not blinded.

### Task-specific finding and limits

**Finding supported:** The deterministic Build made one already retained, correct, decision-relevant fact available in the default first view without changing detailed report data, citation lists, CI/runtime unknowns, action abstention or Workspace recovery. This is a **positive development presentation result on one exposed case**.

**Not established:** It does not prove a shorter actual review time, better independent maintainer decisions, general usability across dependency updates or changed runtime applicability. The fact is still conditional on source/dispatch assumptions. The new view does not explain the complete FastAPI→Starlette→HTTPX chain, specify the exact next observation/traceback, or elevate the historical CI failure to an observed cause. Neither condition can responsibly recommend a non-abstention maintainer action from the saved source-only evidence.

**Alternatives / next decision:** (1) Keep the verified renderer correction and avoid further code work solely to polish AV-Tracer; (2) consider the existing multi-case/independent maintainer-usefulness protocol if actual user benefit needs proof, with contrasting cases, equal access and independent reviewers; (3) propose another deterministic presentation adjustment only after a second concrete supported task/read-friction finding, rather than assuming this one-line improvement justifies broader architecture, LLM interpretation or generic runtime observation. Separately retained exact-job logs/traceback may serve a CI causality investigation **if selected**, but must not be imported into this same-evidence experiment.

## Verification and ownership gate

- B — DONE: complete real paired report comparison plus independent public-safe receipt.
- Verification — GREEN for static report identity, one-line strict difference, source/CI/runtime/action stability, original preserved hashes, and original-versus-updated offline Workspace recovery. This result needs no target-code test or external acquisition; the previous renderer Build already passed 1,100 product tests.
- D — CURRENT: discuss what exactly is improved and why this observation is **not** independent maintainer usefulness or proof of CI failure. Wait for Ali's own interpretation before assigning independent understanding.
- E — PENDING: consolidate the review and choose the next scope after D; no new Build authorization follows automatically.
- C — CONTINUOUS: original mode-comparability issue, repair, machine-verifiable findings and limitations retained here.

**D ownership question:** If the new first view contains `Rejected keyword: app` at line 26, while the old view contains the same correct fact in detailed evidence at line 3,721, what can we now claim with confidence about UpgradePilot, and what **additional experiment/evidence** would be required before claiming it makes maintainers faster or leads to better decisions?
