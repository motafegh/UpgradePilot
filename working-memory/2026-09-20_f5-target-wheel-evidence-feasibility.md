# Target wheel-compatibility evidence-source feasibility — 2026-09-20

**Session status:** ACTIVE — bounded analysis/Planning-Design and Learning-by-Doing; no F5 product implementation selected or authorized.
**Main starting horizon:** `91837914e78b91c4d01cf5e83ec02b0b86ced7f4` (F4 closed).
**Prior:** [F4 CI-consuming job → Target composition](2026-09-20_f4-ci-consuming-job-target-composition.md); [action-relative comparison](2026-09-20_action-relative-producer-reachability-comparison.md).
**Controlling route:** [end-to-end evidence-to-action plan](../plans/END_TO_END_PRODUCT_FLOW_LEARNING_AND_EVIDENCE_TO_ACTION_EXECUTION_PLAN.md); [accepted action semantics](../docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md). `MEMORY.md` alone owns live selection.

## A — orientation: DONE for feasibility-selection slice

Following F4's controlled proof and learning closure, distinguish a correctly identified CI-consuming job and its *declared* runner/Python/install-source context from an exact target-supported wheel-tag observation. Product question: can lawful, exact target-owned evidence establish the supported wheel tags for a relevant target environment, and can that evidence flow through the normal application to the existing artifact-serviceability applicability contract? This is a feasibility/producer-source question, not approval to generate tags from runner/Python labels or from UpgradePilot's own runtime.

## B — bounded action-relative comparison and source inspection: DONE at current read-only horizon

- Accepted action semantics: wheel-path loss is not itself installation failure or permission to block. With a source distribution available, source-build success is a separate question. A specific bounded follow-up check might eventually be justifiable when its exact prerequisite/defeater and product-versus-maintainer execution boundary are established; neither F5 nor any action is admitted by this comparison.
- `src/upgradepilot/impact/artifact_serviceability.py` already defines `TargetWheelCompatibilityEvidence` with exact repository/revision/source/supported tags and implements complete old/proposed wheel-tag intersection. Its controlled fixtures are not proof of a normal producer.
- Current `src/upgradepilot/target/artifact_environment.py` emits partial static job runner, Python declaration and installation declaration, while leaving exact wheel compatibility unresolved. F4 now supplies the correct job. `src/upgradepilot/investigation.py` still calls `evaluate_artifact_serviceability_impact(candidate)` without a target tag witness. No exact target tag observation or normal composition is demonstrated by these source reads.
- AUDIT-008 F6 would require a separate exact installed version/artifact witness if a selected proposition calls for one; current `supported_runtime_correlated` does not establish it. F7 favorable merge requires positive bounded discovery/context coverage and is a wider independent prerequisite. Do not implement them as a queue.
- Existing S008 real-case analysis established CPython-3.6 Linux wheel-path loss with sdist fallback from the case's bounded source/context and package evidence, but its inspected public CI did not establish execution of that exact Python-3.6 artifact transition or an exact target tag-set witness. S008 therefore discriminates the technical proposition but does not prove the missing general normal-source acquisition method.
- Selected **next bounded responsibility: F5 evidence-source feasibility**, not F5 code. Determine whether a concrete supported public-PR/CI path provides a trustworthy environment-specific supported-tag observation tied to exact repository/revision/job/environment and adequate to discriminate full old/proposed wheel compatibility. If no such observation is available within the admitted public/read-only boundary, record the unavailable/deferred proof honestly and reconsider a different action-relative producer instead of inventing a generic log parser, deriving tags from broad configuration, or expanding into generic CI/agent infrastructure.

## C — preservation and current evidence limit: DONE for analysis so far

No source, tests, specifications, or existing plans were changed; no new executable test or live public-PR proof was performed. This file records the proposed/selected bounded feasibility investigation and why it follows F4. Exact witness provenance and execution feasibility are **unverified** and are the subject of the next action; do not claim F5 implementation, artifact applicability, or non-abstention permission.

## D — post-analysis ownership check: NEXT

Check Ali's understanding of the distinction between a static job's `runs-on`/`python-version` declaration and evidence of its exact supported wheel tags, and why S008's published inventory alone does not identify the normal CI target's tag set.

## E — repair and continuation: PENDING

After the reasoning check, assess one concrete public target-owned candidate witness and its exact identity/proof boundary. Select a bounded producer/design/build only if a truthful feasible source and action-relative value survive; otherwise document the blocker and return to the existing action-relative comparison. Preserve F4 closure and the scheduled AUDIT-005 checkpoint. No automatic F5/F6/F7 build or new maintainer action.

**Procedures:** `UP-SKILL:upgradepilot-planning-design`; `UP-SKILL:upgradepilot-working-memory`; canonical A→B→C→D→E.