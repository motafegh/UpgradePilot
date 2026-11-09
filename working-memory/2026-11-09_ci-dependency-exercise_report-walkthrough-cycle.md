# CI dependency exercise report walkthrough

Ali selected one offline walkthrough and progressive teaching after the [recent progress and handoff](2026-11-08_target-wheel-applicability_qualification-cycle.md). Reconciled `56adede8` with `origin/main`. Use the [combined evidence checkpoint](../plans/CALLER_SIGNATURE_NATIVE_ADOPTION_AND_QUALIFICATION_PLAN.md#16-combined-evidence-and-runtime-applicability-design-checkpoint) and existing CI/report owners. The maintainer question is what CI actually exercised for this update and how the reader can tell.

```text
A0 — DONE: verified Git, live handoff, existing CI mapping and retained case alternatives.
A1/A2 — DONE IN CONTINUOUS CONTEXT: carried the prior onboarding and selected question into the read-only walkthrough. Introduced revision identity, static declaration and execution evidence before inspecting the report.
B — CURRENT: trace one retained native CI view through current presentation.
Verification — PENDING: confirm record-to-display fidelity and claim limits.
D/E — PENDING: teach the result and choose the justified next responsibility.
C — CONTINUOUS: preserve engineering findings and proof boundaries.
```

Select glyphsLib PR #1145 (pytest 9.0.2 → 9.0.3). The [retained native CI view](evidence/2026-10-21-investigator-native-ci-presentation/REVIEW.md) includes a successful exact-head workflow, static dependency use and a recorded failure to connect those static steps to runtime. The case has a report-level artifact. FCI001 is an alternate with stronger direct skipped-step evidence but its retained diagnostic did not produce a complete report-level dependency analysis. The learning map separates run identity, static declaration, runtime correlation and command-completion package state. Compress the repeated pre-work gates for this explicitly selected, low-risk read-only follow-up and continue to teach from the actual case. No product edit, live provider request, inference or target execution is selected. UP-SKILL:upgradepilot-learning-by-doing. UP-SKILL:upgradepilot-repository-audit. UP-SKILL:upgradepilot-working-memory.

## What CI establishes

The retained [glyphsLib view](evidence/2026-10-21-investigator-native-ci-presentation/render-repair/case-2.txt) binds base `044f19e4b1437bfc4343592486f4e3c6040306d9` and head `f3cda8a94600e58d27f1bc17c99b7693718b6350`. The Regression Tests workflow succeeded at that head. Its exact source declares requirements installation and direct pytest exercise. The aggregate `supported_not_correlated` preserves these positives and the unresolved execution link. The first reported correlation refusal is `static_job_name_missing` for YAML job key `test`. That identifies the recorded first stop and cannot establish that supplying a name alone would resolve historical runtime evidence. The runtime branch separately evaluated two direct-requirements command candidates. Both remain unresolved on `manager_environment`. Evaluated candidates alone establish neither package state nor later test use.

## Confirmed rendering defect

The [retained structured CI projection](evidence/2026-10-21-investigator-native-ci-presentation/execution/case-2/ci-presentation.json) preserves embedded LF boundaries in its command-valued facts. The [current shared renderer](../src/upgradepilot/report.py) reproduces six flattened command rows. For example, the stored first and second script lines are `python -m pip install --upgrade pip` and `python3 -m venv generate`. The display joins them into `pippython3`. A later activation line also joins the end of the environment-creation line. This obscures the exact command and sequence a reviewer is trying to inspect.

The earliest loss is in the shared presentation layer. `_project_ci` already preserves the text in the fact value. `_assessment_lines` interpolates the whole value into one display entry, then `_display_lines` strips the embedded LF as a control character. The prior experimental wrapper repair preserved separators between rendered rows. This defect is within individual rows and reproduces directly through today's `render_ci_report`. The ordinary full report uses the same assessment formatter. Scope the reproduction to the real retained CI-only view and use the shared code path to select the next owner. This finding changes no CI, runtime or action assessment.

## Verification and handoff

Verified the retained structured input and prior rendered view against their November 7 freeze hashes. Rehydrated the typed CI view from the structured artifact and called the current renderer with network connection guarded. Confirmed the identity, correlation stop, command-state blocker, six multiline command facts and the joined output. The initial test command used the wrong runtime execution module name and failed on import. Located the actual module and ran report, workflow correlation, CI runtime execution and CI dependency state together. All 43 tests passed. No historical report bytes were changed and no native investigation was replayed.

Recommend a small shared-renderer repair for command-valued facts under the [existing presentation plan](../plans/INVESTIGATOR_NATIVE_CI_PRESENTATION_PLAN.md). Preserve visible LF boundaries while keeping terminal controls inert, then prove both CI-only and full report rendering and verify that saved records and proof states remain intact. The question of how to obtain missing runtime observations stays with its evidence owners. No new build is selected in this walkthrough.

```text
B — DONE: traced the real retained report and located the earliest loss.
Verification — GREEN FOR WALKTHROUGH: frozen hash checks, current reproduction and 43 focused tests.
D/E — GUIDED HANDOFF: explain identity, correlation, execution and state, then hand off the renderer repair for selection. Independent learner practice remains unassessed.
C — DONE FOR WALKTHROUGH: preserved the case rationale, result, test correction and next owner.
```

## Renderer repair

Ali selected the immediate renderer repair after the walkthrough and outlook review. Reconciled `48a42d21` with `origin/main`. Continued this same record. The recent explanation covered the exact failure, the display owner and the two consumer proofs, so the pre-B gates carry forward for this small repair. The selected change is presentation only.

Added a workflow-derived regression through CI-only rendering and full-report encode, decode and rendering. The first fixture lacked the checkout step and produced an unrelated checkout-provenance refusal. Adding the checkout established the intended static evidence while preserving the runtime uncertainty. The corrected pre-fix test reproduced joined commands. The test also puts control characters and label-shaped text in a continuation to check that it stays inert and visibly inside the fact.

The shared assessment formatter splits fact values on LF, then prefixes continuation lines before the existing terminal filter runs. This handles multiline facts uniformly without recognizing a case, command spelling or package. CRLF works through the LF boundary and existing carriage-return filtering. Other controls cannot introduce display rows. Bumped the full-report display version to 4. The report codec, saved generator version and evidence values are separate.

All 70 focused product tests and all seven experimental CI presentation consumer tests passed. The real glyphsLib retained CI projection and Soup Sieve saved full report showed all six and seven multiline command facts respectively, with saved bytes and recorded outcomes preserved. The remote rehearsal guide now pins byte-exact regeneration to `e6778593`. A clean archive at that revision reproduced all 14 tracked reviewer files byte for byte. UP-SKILL:upgradepilot-build-implement.

The full suite passed all 1,081 product tests. Governance and whitespace checks passed. The normal offline CLI also opened the retained Soup Sieve report with renderer version 4 and displayed the saved command continuations.

```text
B — DONE: repaired shared assessment-fact rendering and documented the pinned historical renderer.
Verification — GREEN: failing-then-passing regression, both real display paths, frozen packet parity and full regression.
D/E — GUIDED HANDOFF: explain how display line boundaries and terminal filtering work together. Independent practice remains unassessed.
C — DONE FOR REPAIR: preserved the reasoning, correction and proof.
```
