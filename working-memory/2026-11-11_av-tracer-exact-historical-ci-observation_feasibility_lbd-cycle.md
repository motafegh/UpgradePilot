# AV-Tracer exact historical GitHub Actions observation — bounded feasibility cycle

**Date:** 2026-11-11
**Primary operation:** read-only Audit/Diagnose with Learning-by-Doing.
**Owner and next-step boundary:** [current MEMORY](../MEMORY.md); [November 11 evidence/causality checkpoint](2026-11-11_av-tracer-combined-evidence-runtime-applicability-and-ai-checkpoint_cycle.md); [November 9 cross-case screening](2026-11-09_targeted-check_cross-case-qualification_cycle.md); [source-only report evidence](evidence/2026-11-11-av-tracer-exact-version-allocation/REPORT_REVIEW_PACKET.md). No product Build, external repository mutation, rerun, installation, target code execution, LLM inference or ambient credential escalation.

UP-SKILL:upgradepilot-repository-audit. UP-SKILL:upgradepilot-learning-by-doing. UP-SKILL:upgradepilot-working-memory.

## A0/A1/A2, current state and bounded task
- **A0 DONE:** GitHub main at `d816ff48f8e1fd327870e35b4545a34fb6564e2d`; prior AI-only reviewer tracks explicitly deferred due to low decision value. The AV-Tracer native saved-report evidence is source-only; it records a conditional Starlette 0.27.0 `app=` forwarding incompatibility under proposed HTTPX 0.28.1, *not* a running test traceback or a qualified CI/runtime evidence join. Earlier public PR-associated screening saw `Run pytest` exit 2 without traceback.
- **A1 DONE, continuity-compressed:** preceding discussions taught source call-chain, requested/installed/loaded distinctions, first-view rendering versus evidence strength and the one-line presentation improvement. Ali accepted the recommended **bounded real-case evidence-gap investigation**, and earlier said not to create a separate branch.
- **A2 DONE, continuity-compressed:** inspect existing GitHub Actions run/job/step and, if obtainable, exact-job log only. Test whether run/attempt/job/head/step evidence connects to the proposed dependency versions, a matching traceback and same-process version/callable. Keep exact-head workflow YAML as a separate static observation until runtime provenance supports its use.
- **Case frozen from saved records:** target `ivaronkun-Ahey/AV-Tracer` PR #11, base `527a004918c0f825e97c3583404242605fd58ec2`, head `25e7205f39103456e7efbc4e9f503f3debc7b5d8`; public historical workflow run `41416124208`, previously seen job `125180284415`. Target's exact-head `.github/workflows/ci.yml` declares a backend Python 3.11 job installing `requirements-dev.txt` then running pytest. **The workflow declaration is not itself a record of historical execution.**
- **Claim and stop line:** establish only what the exact historical job data can support, including unavailable/expired/unauthorized states. Require exact run/attempt/job/head identity before any causal claim. One failed pytest step plus a source mismatch cannot prove same-process installed/imported versions or failure cause.
- **Acquisition/effort envelope:** one run-jobs lookup, one known-job step lookup, and at most one known-job log lookup using existing GitHub connector, followed only by a small public web corroboration if connector fails or metadata conflict requires it. No enumeration, retries or downloaded artifact archive by default. Summarize excerpts/sanitized fields only; avoid emitting private/raw job logs, tokens or third-party material. If API refuses/expired, stop and preserve the precise access failure. One alternative public-view lookup is sufficient to differentiate connector/auth failure from universally missing logs.
- **Learning goal:** distinguish four propositions—step failed; traceback identifies immediate error; exact process installed/loaded dependency and callable; upgrade-caused regression—and name the evidence needed for each.

## Cycle status
A0 — DONE; A1 — DONE, continuity-compressed; A2 — DONE, continuity-compressed; B — CURRENT, bounded read-only exact-job inspection; Verification — PENDING; D — PENDING, evidence interpretation with Ali; E — PENDING, close or defer the exact remaining gap; C — CONTINUOUS, retain findings and errors.

## Findings (append after actual inspection)
PENDING. No CI job/log claim made by this record's initialization.
