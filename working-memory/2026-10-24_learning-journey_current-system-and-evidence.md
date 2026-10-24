# Learning journey — UpgradePilot's current system and evidence flow

## Full learning route and progress

**How to read the checkboxes:** `[x]` means the named teaching unit or exercise has been covered/completed at the stated depth. It does **not** certify mastery of its whole module. `[ ]` means remaining teaching, practice or verification. Learner answers and corrections are preserved below; explanation, agreement and passing product tests alone do not establish mastery.

The original route had seven broad subjects. The later route elaboration separately named the bridge to the proposed next design; it appears as item8. The HTTPX end-to-end walkthrough consolidates the original subjects rather than replacing them. This is a teaching route, not authorization to execute a product plan.

### 1. Purpose, dependency updates and structured inputs

- [x] Explain repository, dependency, pull request, diff and exact requirement using actual HTTPX PR20.
- [x] Read the actual `requirements.txt` change: `httpx==0.27.2` → `httpx==0.28.1`.
- [x] Distinguish an observed proposed requirement change from installation, execution and compatibility.
- [x] Introduce provider/API acquisition, Python records and named fields.
- [x] Explain `PullRequestObservation` and the identity/description split.
- [x] Walk through provider observation → changed files → dependency analysis → `AcquiredDependencyInputs`.
- [ ] Independently trace relevant function calls, arguments, returns and branches in source; repair material Python-reading prerequisites locally.
- [ ] Examine dependency-analysis problem/unsupported outcomes without equating them to an unsafe update.

### 2. Identity, observation scope and evidence association

- [x] Explain base/head code-revision identifiers versus mutable PR description text.
- [x] Explain observation time, UTF-8 byte count and description fingerprint; integrity is not truth/authenticity.
- [x] Complete the same-head/edited-description prediction: Ali correctly identified unchanged head, changed description hash and later observation time.
- [x] Introduce the final PR identity reread around changed-file acquisition and its non-atomic observation boundary.
- [x] Discuss exact proposition scope: package/version/environment/time; reuse adequate evidence rather than demand duplicate proof.
- [ ] Trace exact target/run/attempt/input bindings and the relevant validation/refusal branches in source.
- [ ] Study the FCI frozen-versus-fresh distinction: missing historical fields cannot be retroactively filled from later observations.
- [ ] Practise detecting mismatched, stale, incomplete and contradictory evidence with real retained cases.

### 3. CI: configuration, execution and bounded dependency state

- [x] Explain CI, GitHub Actions, workflow, run, job and step.
- [x] Separate configured operations, correlation to runtime records and positive execution evidence.
- [x] Use real HTTPX zero returned exact-head runs and separately acquired FCI001 matched-but-skipped steps.
- [x] Complete the successful-job/skipped-steps reasoning exercise: Ali explained why job success does not establish those operations executed.
- [x] Explain that UpgradePilot analyzes existing CI evidence; it does not rerun the target's installation/tests in this path.
- [x] Introduce pip, requirements-file consumption, environment selection and command options/configuration.
- [x] Explain the bounded `RequirementSatisfiedAtCommandCompletion` proposition and limits: no fresh-install causality, later persistence/use, compatibility or action permission.
- [x] Explain successful dry-run behavior using an existing controlled product test; do not present that test as a positive real HTTPX CI observation.
- [x] Introduce `state`/`reason`/`detail`, `not_established` versus absence, and overall `no_admitted_candidate` versus per-command results.
- [x] Work through why a successful dry run must not be reported as a failed installation; preserve separately supported evidence meanings.
- [ ] Trace actual CI preparation, correlation, execution and dependency-state code with their discriminating tests.
- [ ] Deepen command/environment/source identity, installation destination and effective configuration reasoning.
- [ ] Independently interpret positive/problem/unresolved outcomes and diagnose missing evidence without relying on memorized labels.

### 4. Change meaning, impact and target applicability

- [x] Introduce the distinction between what PR prose says, whether the upstream statement is supported, and whether it affects this target.
- [x] Introduce the current HTTPX report's missing caller/framework premises and the existence of copied removal/deprecation context.
- [ ] Study source statements, supported interpretations, technical candidates and applicability as separate responsibilities.
- [ ] Trace a real HTTPX caller/callee example: call arguments, accepted parameters, source/version correspondence and unresolved dispatch or target resolution.
- [ ] Study a real bounded Python-support-drop path and target Python relevance.
- [ ] Study OpenCV's published-artifact comparison:27 removed/8 added exact tags, target alternatives, source-distribution availability and unknown source-build success.
- [ ] Explain why relevant state/behavior evidence still does not automatically grant maintainer-action permission.

### 5. Workspace and explicit retention

- [x] Introduce capture, encoded records, Workspace state and revisions through the description's real path.
- [x] Introduce record family/owner/codec-version metadata and the distinction from the encoded observation payload.
- [x] Explain explicit selected-field retention: capture does not automatically archive every response or argument.
- [x] Explain default volatile memory versus separately selected durable storage; finishing the investigation does not automatically erase its revision.
- [x] Introduce the returned `workspace_revision` and direct description projection.
- [ ] Inspect exact layouts, encoding/decoding, immutable records/revisions, payload hashes and input-reference closure in code.
- [ ] Study version compatibility, historical not-recorded material, optional unsupported decoding and integrity refusals.
- [ ] Trace durable checkpoint publication and cold-process reconstruction; distinguish them from report reopening, continuation and replay.

### 6. Reports, saving and offline source inspection

- [x] Explain structured `InvestigationReport` versus rendered terminal text.
- [x] Trace description observation → `ReportSource.content` → optional saved JSON → offline source display.
- [x] Explain report-local source IDs, source metadata, attribution and limits; retained source text does not become an accepted semantic finding.
- [x] Explain that projection creates the report record and the CLI separately saves it if requested.
- [x] Explain encoding/decoding, schema1 report envelope and digest at an introductory level.
- [x] Explain opt-in saving, no replacement of an existing destination, and literal sanitized source display.
- [x] Complete the saved-A/live-B reasoning exercise: Ali chose A; clarify that no-refresh semantics apply even when internet is available.
- [x] Explain that reopening reads the saved report independently of GitHub and the original in-memory investigation.
- [x] Deliver the full HTTPX input-to-report walkthrough; Ali reconstructed the main data path.
- [ ] **CURRENT:** complete the pending source-localization exercise after the reconstruction corrections.
- [ ] Trace concrete report projection, encoding, validation, lookup and rendering source with failure-path tests.
- [ ] Practise missing/empty/null/invalid/oversized description distinctions, historical absence, bad file/source ID and corruption outcomes.

### 7. Tests, experiments, failures and proof limits

- [x] Introduce controlled provider tests, record round trips and the difference between fixture proof and real external behavior.
- [x] Distinguish recent real negative CI cases from a controlled positive/dry-run dependency-state example.
- [x] Explain the actual retained HTTPX packet and controlled October23 composition; no new live investigation occurred during teaching.
- [x] Discuss why source access, byte identity or a report digest does not establish semantic correctness or usefulness.
- [ ] Independently read a meaningful test: setup → action → assertions → protected behavior → stronger claims not proved.
- [ ] Examine full-case composition/cold-process/installed CLI evidence and their separate obligations.
- [ ] Study the earlier semantic failures: valid citations and complete delivery still permitted false cert-removal and forwarding assertions.
- [ ] Distinguish product behavior, developer diagnostics, experimental methods, semantic acceptance, independent usefulness and learner ownership.
- [ ] Practise debugging and engineering judgments across layers; no product modification while this journey remains Learning-Only.

### 8. Bridge to the proposed next design

- [ ] Understand the proposed deterministic call/signature evidence question and the existing AST/binding/source/adapter owners.
- [ ] Compare observed structural facts, conditional caller/callee relationships and actual target applicability.
- [ ] Explain justified scope, unresolved constructs, consumer/proof needs and reuse/simplification choices before any Build decision.
- [ ] Reconstruct a coherent overall case and its limitations, interpret relevant tests and challenge one meaningful design choice.
- [ ] Ali explicitly decides whether to continue learning, repair remaining gaps or return to another project operation. Learning progress does not authorize Build automatically.

## Journey identity and operating agreement

- Created October24,2026, reconstructing the learning already underway in this conversation across October23–24. No exact earlier message times or historical learning durations are invented.
- Purpose: Ali asked to understand and master what exists before further building, using actual cases, data flow, source and tests. He initially reported not understanding the work; assume prerequisites need explanation rather than treating prior approval as understanding.
- **Learning-Only:** no product/source/test/plan/specification/ADR changes, new acquisition, inference or target execution are authorized by this teaching journey. Read-only source/evidence inspection and appropriate learning checks remain allowed.
- Ali explicitly requested this one progressively maintained working-memory record. It owns this journey's teaching route, learner observations, corrections and exact learning resume point. It is not a new study package, implementation plan or product-state authority.
- No engineering phase template is used: the entire selected cycle is learning. This follows Ali's explicit instruction and the Learning-Only route; it does not waive evidence or authorization boundaries.
- `MEMORY.md` retains only the live mode/product handoff and a link here. Do not copy these lesson checkboxes or learner history into another live owner or create a parallel learning-memory file.
- Entry repository horizon: `c9d1feb2`; relevant product implementation remains `85491b89`, with subsequent test/documentation/evidence corrections. These are dated anchors, not claims that the repository will never change.
- Preserve the unrelated untracked `2026-10-03_broad-project-and-future-plans-audit_lbd-cycle.md`.

## Exact learning resume point

The connected HTTPX walkthrough has been taught, and Ali has reconstructed the main description path. The teacher then corrected the explicit acquired-input handoff, selected-field capture, projection-versus-save boundary and Workspace lifetime. **Ali has not yet answered the following exercise or independently demonstrated those corrections in a second trace.**

> Hypothetical debugging exercise, not an observed defect: the saved JSON's intended source contains description A. Opening that same file with the intended source ID displays description B. Would you begin with GitHub acquisition, or with the later file-decoding/source-selection/rendering path? Which known fact narrows the search?

Resume by hearing Ali's reasoning, then explain or repair the relevant boundary. Do not supply an invented learner answer or mark the exercise complete. Use this to connect data-flow reconstruction to diagnosis; continue with an appropriately sized source/test chunk from the route rather than restarting orientation or repeating the entire dry-run discussion.

## Meaningful learning progression and corrections

| Subject | Ali's demonstrated answer or question | Correction, limit or remaining depth |
| --- | --- | --- |
| Requirement declaration | Initially said we know what the provider described and cannot infer safety/compatibility/exercise. | Clarified that the acquired patch itself is evidence of the declared proposed change. Different evidence is needed for installed state; provider here means our acquisition component. No independent source trace yet. |
| Mutable description | Correctly reasoned that a manual description change must be distinguished from code identity. | Keep identity and observation records separate; commit identity does not bind mutable PR prose. |
| Fingerprint/time/head prediction | Correctly predicted changed description fingerprint and observation time, unchanged head when no code commit changed. | Successful introductory reasoning under the stated scenario; detailed hashing/encoding and source validation remain to study. |
| Offline A versus live B | Correctly chose the previously acquired A. | Clarified that saved-report no-refresh behavior, rather than mere network unavailability, is the reason; even online reopening preserves A. |
| Successful job/skipped steps | Explained that overall success can mislead about individual operations and that skipped steps do not establish execution. | This was the separate real FCI001 fresh diagnostic, not an HTTPX execution or retroactive repair of its frozen bundle. |
| Dry-run success | Recognized that the dry-run flag prevents deriving installation from success. | Refined wording from successful installation to successful planning operation. A package could already be present; no positive/negative installed-state conclusion follows from this command alone. |
| Unknown versus failed | Initially focused on not knowing whether the package was installed earlier. | Separated known successful operation from unestablished package state. A lack of installed-state proof does not turn the operation into a failed installation. |
| Independent evidence and redundant investigation | Explained that separate evidence must retain its own meaning, then challenged why more installation proof would be needed if installed state were already adequately proven. | Accepted the challenge: reuse adequate same-scope evidence and stop that proof branch. Another check needs a different unresolved proposition, relevant state change/conflict or justified independent boundary. A limitation of one observation does not cancel another adequate proof. |
| Scope and current implementation | Discussed package/version/environment/time and later behavior/state as distinct questions. | Current runtime feature is a bounded per-command proof route, not a general observer/adaptive stopping engine. Do not describe a hypothetical alternative proof path as implemented. |
| HTTPX end-to-end reconstruction | Named provider observation, identity/description, capture, retained description record, Workspace revision, report projection/content, saving and offline reading without refetch/reanalysis. | Correct main path. Teacher added `AcquiredDependencyInputs.description`, explicit rather than automatic-all-arguments capture, optional separate CLI save, and non-erasing Workspace finish semantics. Confirmation through diagnosis is pending. |

The learner's spontaneous necessity question is evidence of initial engineering judgment on that boundary. It does not establish mastery of all stopping logic, all CI semantics, full source ownership or general product architecture. No percentages, scores or completed-module mastery are inferred.

## Real case and source anchors used in teaching

- **HTTPX normal evidence:** Aidan-Wallace/kubernetes-dashboard-token-api PR20, `httpx 0.27.2 → 0.28.1`, `requirements.txt`, base `b065646e4b7b894964567950f9ad770b02c136c2`, head `391508134b083b8f54461c0b576e8f7985c6ecb4`. [Original capture review](evidence/2026-10-22-matched-report-source-capture/REVIEW.md), [original report](evidence/2026-10-22-matched-report-source-capture/report.txt).
- **New source-access evidence:** [Build review](evidence/2026-10-23-pr-description-build/REVIEW.md), [retained-case receipt](evidence/2026-10-23-pr-description-build/retained-case-receipt.json), [task review](evidence/2026-10-23-source-access-task-review/REVIEW.md). HTTPX report `72081813-39ef-402a-8e51-ec40f6ac9073`; its PR source `source-1` retains9,348 UTF-8 bytes. The October23 output was controlled composition of October22 responses, not a fresh live capture. Source IDs are report-local.
- **Actual technical outcomes in that HTTPX packet:** supported declared dependency transition; zero returned exact-head pull-request workflow runs; no admitted runtime candidate; old/proposed package metadata available; stronger upstream authority unestablished; no candidate observed within the bounded wheel-tag-loss horizon. Current action evaluator allows explained abstention only. Merged PR metadata is not a compatibility proof.
- **FCI001:** [paired diagnostic review](evidence/2026-10-20-current-ci-owner-diagnostic/PAIRED_REVIEW.md). Fresh observed job identity permits correlation of two skipped user steps; success of the overall job does not establish those operations executed. Historical frozen jobs lacked head fields and remain unchanged. The package-state evaluator was not invoked by that diagnostic.
- **Controlled tests, not actual target execution:** [provider tests](../tests/test_github_client.py), [description composition tests](../tests/test_pull_request_description.py), [dependency-state tests](../tests/test_ci_dependency_state.py). Positive/dry-run examples demonstrate product reasoning on controlled inputs, not a real positive runtime witness for HTTPX or FCI001.
- **Implementation reading route:** [PR provider](../src/upgradepilot/github/pull_request.py) → [shared input preparation](../src/upgradepilot/investigation_inputs.py) → [investigation coordinator](../src/upgradepilot/investigation.py) → [native capture](../src/upgradepilot/workspace/native_capture.py) → [native projection](../src/upgradepilot/workspace/native_projection.py) → [report projection](../src/upgradepilot/report_projection.py) → [report encoding/files](../src/upgradepilot/report_file.py) → [CLI](../src/upgradepilot/cli.py) and [source rendering](../src/upgradepilot/report.py).
- **Future real contrasts:** OpenCV artifact/support-context review and retained historical caller/callee failures will be used when their route items begin. Their existence is not evidence that those lessons have already been completed.

## Teaching evidence and proof limits

During teaching, the assistant read current source and retained records. It checked the existing HTTPX report hash and exercised the actual offline source CLI with network/provider/investigation entry points blocked: return0, output matched the prior saved view, existing file unchanged. This checked the teaching example's current fidelity; it was not a new live run, new semantic evaluation or learner-owned test execution.

The earlier908-test product proof, installed-package checks and prior evaluation results remain dated engineering evidence. They do not establish Ali's mastery. No product change or new full test run occurred during this learning dialogue. No broad Audit, new implementation design, model experiment or proposed next source-relation Build was activated.

## How to maintain this same record

- Keep the full route at the top and update the relevant checkboxes when a named teaching/practice unit is actually covered. Keep deeper source/test/transfer work unchecked until done.
- At meaningful learning points, summarize the real question/example, Ali's reasoning, correction or changed understanding, remaining gap and evidence pointer. Record doubts, useful counterarguments, mistakes and teacher corrections when they affect later understanding.
- Distinguish introduced, explained, independently reconstructed, diagnosed and still pending in prose. Do not turn these into a new scoring framework or mark mastery from acknowledgment.
- Maintain one exact pending exercise/resume point. Preserve material earlier corrections below; do not replace the progression with only the latest conclusion or a raw transcript.
- Revisit earlier concepts through natural retrieval/transfer; restore prerequisites where needed. Do not make incidental syntax memorization an artificial gate.
- Keep examples honest: actual observations, controlled fixtures and hypothetical debugging cases must stay distinguishable. Preserve source/evidence horizons when revisiting older work.
- Record new material product-state changes only in root MEMORY; lesson progress belongs here. If product state changes in parallel, recheck the needed owner/source before teaching it as current.
- Save/commit/push coherent documentation updates under Ali's standing publication instruction, preserving unrelated work. Do not create a commit for every answer or repeat product regression for prose-only learning updates without a new proof need.
- On a learning pause, leave the precise question/source/resume point. On return to engineering, require Ali's explicit mode change and reconcile root MEMORY; this record grants no Build authority.

## Record creation check — October24,2026

Created retrospectively at Ali's explicit request, using the actual conversation's explanations, learner answers, corrections and unanswered exercise. The phase-free shape is deliberate. This is a working progression record, not a newly authored textbook or a second product plan. Creation validation confirms all18 local links resolve, all8 route subjects are present, the unanswered exercise remains unchecked, no engineering-phase headings were introduced, and git diff --check passes. The focused change is this record plus root MEMORY's mode/link; product source/tests and the unrelated untracked record are untouched. No product regression is required for this documentation-only addition.

UP-SKILL:upgradepilot-learning-only
UP-SKILL:upgradepilot-working-memory
