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
- [x] Guided Block2 source reading of exact head/run/attempt/job bindings and their acquisition/correlation refusals; independent application remains pending.
- [x] Explain the FCI frozen/conditional/separately fresh evidence tracks and why later observations cannot repair missing historical fields.
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
- [x] Guided Block2 trace of actual CI preparation, correlation, step/command execution and dependency-state composition, with six discriminating existing tests.
- [x] Explain the command/source/environment scope and four package-manager dimensions in the connected Block2 path; detailed parser/configuration implementation remains lookup/deferred depth.
- [ ] Independently interpret positive/problem/unresolved outcomes and diagnose missing evidence without relying on memorized labels.

### 4. Change meaning, impact and target applicability

- [x] Introduce the distinction between what PR prose says, whether the upstream statement is supported, and whether it affects this target.
- [x] Introduce the current HTTPX report's missing caller/framework premises and the existence of copied removal/deprecation context.
- [x] Guided Block3 explanation of source statements, admitted interpretations, technical candidates and applicability as separate responsibilities; grounding/quotation is not a general semantic oracle.
- [x] Guided real HTTPX caller/callee trace: target TestClient use, older/newer captured Starlette forwarding and HTTPX signatures; distinguish richer historical source packets from current normal inputs and unresolved actual framework/version/dispatch binding.
- [x] Guided bounded Python-support-drop path: authority/extraction/grounding → candidate → targeted declaration read → relevance/reevaluation; retained Soup Sieve normal report supplies the real non-overlap example.
- [x] Guided OpenCV published-artifact comparison:27 removed/8 added exact tags, full-inventory target alternatives, source-distribution availability and unknown source-build success. Controlled positive/alternative-tag tests are distinct from actual unresolved OpenCV target evidence.
- [x] Explain candidate/path/proposition states, conjunctive requirements versus alternative paths, three distinct coverage questions, and the abstain-only action evaluator's separate permission boundary.
- [ ] Independently reconstruct these mechanisms, read their tests and apply the coverage/authority boundaries; questions remain deferred by Ali.

### 5. Workspace and explicit retention

- [x] Introduce capture, encoded records, Workspace state and revisions through the description's real path.
- [x] Introduce record family/owner/codec-version metadata and the distinction from the encoded observation payload.
- [x] Explain explicit selected-field retention: capture does not automatically archive every response or argument.
- [x] Explain default volatile memory versus separately selected durable storage; finishing the investigation does not automatically erase its revision.
- [x] Introduce the returned `workspace_revision` and direct description projection.
- [x] Guided Block1 reading of the description layout, explicit capture encoding, native payload hash/input references, target binding and reconstruction boundaries. Generic codec recursion remains operational/lookup depth.
- [x] Explain historical not-recorded material, optional unsupported native decoding versus integrity refusal, and independent report-schema compatibility in Block1; learner application remains in the integrated exercise.
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
- [x] Complete the introductory source-localization exercise: Ali identified the first mismatch after correct decoding, at source selection.
- [x] Introduce the actual exact-ID lookup and distinct unknown-source versus unavailable-original-text refusals using HTTPX sources1–3.
- [x] Trace the source-3 refusal condition: Ali correctly identified the true retention comparison and the effect of Boolean `or`, despite present content.
- [x] Introduce empty text versus absent content and inspect the existing empty-source test.
- [x] Complete the introductory truthiness-change review: Ali identified that the replacement merges empty text and None; teacher identifies valid retained empty text as the incorrectly rejected input.
- [x] Guided Block1 walkthrough of report projection, encoding, non-replacing publication, file validation, lookup and rendering with an existing focused test.
- [ ] **DEFERRED BY ALI:** apply the Block1 failure-boundary exercise and interpret what the focused test proves; teaching is covered, answers are unassessed.
- [ ] Practise missing/empty/null/invalid/oversized description distinctions, historical absence, bad file/source ID and corruption outcomes.

### 7. Tests, experiments, failures and proof limits

- [x] Introduce controlled provider tests, record round trips and the difference between fixture proof and real external behavior.
- [x] Distinguish recent real negative CI cases from a controlled positive/dry-run dependency-state example.
- [x] Explain the actual retained HTTPX packet and controlled October23 composition; no new live investigation occurred during teaching.
- [x] Discuss why source access, byte identity or a report digest does not establish semantic correctness or usefulness.
- [ ] Independently read a meaningful test: setup → action → assertions → protected behavior → stronger claims not proved.
- [x] Guided Block4 reading of controlled-provider semantic-boundary and binding tests: setup/action/assertions, protected behavior, and claims excluded. Independent test reconstruction above remains pending.
- [x] Examine full-case composition/cold-process/installed CLI evidence and their separate obligations; inspect the actual child-process reconstruction test and historical installed receipt without claiming a fresh installed/full-regression run.
- [x] Study the completed October19 negative comparison: valid citations and complete delivery still permitted false cert-removal/forwarding assertions and material omissions. Keep it distinct from the earlier discontinued incomplete three-deployment comparison; no frozen result was rerun or regraded.
- [x] Distinguish product behavior, developer diagnostics, experimental methods, semantic acceptance, independent usefulness and learner ownership; code/reference validation does not adjudicate entailment.
- [ ] Practise debugging and engineering judgments across layers; no product modification while this journey remains Learning-Only.

### 8. Bridge to the proposed next design

- [x] Guided Block4 explanation of the proposed deterministic call/signature evidence question and the existing AST/binding/source/adapter owners; this is orientation to a proposed design, not a completed design or implementation.
- [x] Compare observed structural facts, conditional caller/callee relationships and actual target applicability; trace where lexical binding, sampled source/version and dispatch limits prevent stronger conclusions.
- [x] Explain justified scope, unresolved constructs, consumer/proof needs and reuse/simplification choices before any Build decision. Existing adequate records may justify reuse; an inventory-only result is not product acceptance.
- [ ] Reconstruct a coherent overall case and its limitations, interpret relevant tests and challenge one meaningful design choice.
- [ ] Ali explicitly decides whether to continue learning, repair remaining gaps or return to another project operation. Learning progress does not authorize Build automatically.

## Delivery grouping and pace — revised October24 at Ali's request

Ali asked to cover more material per step and progress faster while retaining learning quality and returning to project delivery. Earlier introductory teaching used many small variants of the same boundary; compress that cadence now. The eight subjects/checklists above remain the curriculum/progress record. The four groups below organize delivery rather than create a second checklist or four guaranteed messages/sessions.

| Connected block | Included responsibilities and real examples | Intended learning result |
| --- | --- | --- |
| Data contracts, preservation and failure behavior — taught; exercise deferred by Ali | Finish HTTPX acquisition/input/capture/Workspace/report/save/open handoffs; use missing/empty/version/integrity examples and one representative test. Treat deep SQLite/storage internals operationally unless needed. | Trace a value, explain the relevant representation/failure boundaries and interpret a test without repeating every source-view condition exercise. |
| CI evidence as one complete case — taught; practice deferred by Ali | FCI frozen/fresh identity, configuration/runtime correlation, skipped execution, scoped command/environment evidence and a contrasting controlled test. | Explain which proposition is supported or blocked and which owner/source would resolve a material gap. |
| Impact and target relevance — taught; practice deferred by Ali | HTTPX copied changes/caller/signature relations, OpenCV artifact/environment limits, and a bounded Python-support example. Connect these to findings, applicability and action permission. | Guided source/evidence trace covered; independent explanation/application remains unassessed. |
| Experimental failures, proof and the next design — taught; practice deferred by Ali | Interpret the existing negative semantic results, useful test/fixture limits, product versus experiment status, existing AST/source owners and the proposed bounded source-relation responsibility. | Guided proof/design orientation covered; independent reconstruction/challenge and the return-to-engineering decision remain pending. |

Ali explicitly reconfirmed that important code/source explanations are desired and must not be skipped to accelerate. Preserve responsibility-bearing excerpts, explain unfamiliar material syntax and decisions, and show their actual caller/data/consumer relationship. Faster delivery comes from grouping related mechanisms and reducing repetitive checks, not removing important source understanding.

**October24 sequencing update:** Ali explicitly said to keep questions for later and proceed to the next block fully. Continue connected teaching without end-of-block quizzes for now. Preserve unanswered exercises below and leave independent-understanding items unchecked; do not infer mastery or block requested teaching on those answers. This instruction supersedes the earlier answer-before-advancing cadence.

Use a coherent real case/data flow plus representative code and tests per block, then one integrated reconstruction/diagnosis/design question. Do not ask a new question for every operator/field or repeat a correctly explained point. Repair actual blocking gaps locally and move on; use later natural retrieval to assess retained understanding. Incidental syntax/library details may remain recognize-and-lookup knowledge. A block can span more than one exchange if required; there is no invented completion percentage or fixed duration.

Return-to-engineering readiness concerns the selected upcoming responsibility: explain its purpose and scope, trace its main input/output and failures, distinguish evidence/authority limits, interpret a relevant test, and reason about one meaningful design/debugging choice. Completion of every deep checklist item is not a universal prerequisite. Unfinished material remains visible with a reason/re-entry trigger; do not silently count deferred depth as mastered. The complete eight-subject journey remains available after engineering resumes.

**Mode boundary:** this pace change does not resume Build. Ali still owns the explicit return-to-engineering decision. When selected, continue focused learning with real slices and verified results; do not require complete repository mastery before useful project progress. Define engineering completion by an accepted bounded product milestone and its proof, not by all learning checkboxes or repeated infrastructure expansion.

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

The connected HTTPX walkthrough and its introductory diagnostic exercise are complete at the taught depth. Ali initially chose the later path but was unsure why. After the last-known-correct-checkpoint explanation, he identified the first inconsistency after reading/decoding and chose the code selecting the source inside the viewer. This is demonstrated initial localization reasoning, not full debugging/source mastery.

Teaching now reads actual `render_report_source`: exact-ID lookup, no-match `None`, retained-text/content checks and scoped refusal. Real retained HTTPX sources are source-1/pull_request/retained_text/has content; source-2/dependency_source/reference_only/no content; source-3/producer_assessment/producer_result/has content. Read-only probes show source1 renders, unknown ID is refused, and sources2/3 are refused as lacking retained original text for this command. Existing records are unchanged; these are pure saved-record inspections, not fresh acquisition or semantic evaluation.

Ali correctly read the source-3 guard: `or` requires only one true condition, and `source.retention != "retained_text"` supplies it. This demonstrates the Boolean/branch reasoning; source-versus-producer-result meaning has been explained but not independently reconstructed in detail. Revisit that meaning naturally rather than repeat an already answered condition question.

Teaching now distinguishes valid empty retained text (`""`) from absent content (`None`), uses the current projection/viewer and existing controlled empty-source test, and explains why Python truthiness would merge the two. The real HTTPX description is nonempty; the empty case is explicitly a controlled fixture.

**Latest completed exercise:** Ali correctly identified that `not source.content` cannot distinguish empty text from None. The concrete affected valid input is `retention="retained_text", content=""`, which the proposed change would wrongly reject. Introductory review complete; no product edit occurred.

**Completed guided teaching:** all four connected blocks are covered at the explained depth: data contracts/preservation/failures/test; CI evidence/code; impact/target relevance; experimental failures/proof/proposed design. Ali explicitly postponed questions; no integrated answers or new mastery are inferred. Do not repeat a pending quiz or invent a fifth required teaching block.

**Exact learning resume point:** the four-block guided sequence is complete; the deferred practice bank remains unanswered. At Ali's next selection, use targeted gap repair/practice or transition to the engineering handoff rather than automatically extending this course. If Ali explicitly resumes engineering, re-anchor root MEMORY and the current accepted owner; the recommended engineering entry remains bounded Planning/Design of deterministic call/signature evidence, not an already authorized Build or model trial. Completing guided coverage does not close independent mastery or require repository-wide mastery before an authorized engineering return.

## Deferred reasoning/practice bank — questions for later at Ali's request

- **Block1, unanswered:** classify (A) a description above256KiB with valid PR identity, (B) an intact optional native description with unsupported codec999, (C) native description payload changed without its digest, and (D) saved-report content changed without its report-integrity digest. Identify the earliest relevant owner and unavailable-source versus refusal behavior, plus the focused test's proof/non-proof.
- **Block2, not yet asked/answered:** trace a case with a valid exact-attempt job but missing static display name; a correlated completed/skipped step; and a successful step containing an ineligible conditional install command. Distinguish acquisition, correlation, step execution, exact-command execution and package-state conclusions. Explain why a fresh observed job head does not retroactively admit an old missing-head capture.
- **Block3, not yet asked/answered:** explain why a captured older Starlette call plus a new HTTPX signature establishes a conditional mismatch but does not identify the actual installed target framework; distinguish that from the newer captured non-forwarding call. Explain why one disappeared wheel tag does not establish loss of the target's wheel path, and why a refuted bounded Python-support path does not prove the whole upgrade harmless or admit merge permission.
- **Block4, not yet asked/answered:** reconstruct one actual controlled test's setup/action/assertions and explain why a wrong proposal with a real citation can pass mechanical validation without semantic acceptance. Trace alias rebinding or a sampled adapter version into the honest uncertainty boundary; challenge whether a proposed source-relation increment reaches a concrete consumer rather than only producing another inventory.
- Check the learner's independent source/test understanding when Ali chooses to return to practice. Keep taught checkboxes distinct from answered/verified practice. Do not fabricate learner responses, mark postponed work complete, or treat continuing teaching as a return to engineering.

## Meaningful learning progression and corrections

This table preserves progression in order. Later responses resolve earlier pending notes; the exact resume point above owns the current learning continuation.

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
| Debugging localization | Ali selected the later file-decoding/source-selection/rendering path, while explicitly reporting uncertainty about the reason. | Correct direction only. Teacher explains that the saved intended source already contains A and that the offline path reads it without acquisition. Last-known-correct checkpoint and earliest-divergence reasoning are being taught; transfer answer remains pending. |
| Localization follow-up | Ali explained that the first inconsistency occurs after reading/decoding and chose the source-selection code inside the viewer. | Introductory exercise complete: decoded A is the known-correct checkpoint; selected B is the first divergent value. No real bug was observed or repaired. Actual lookup/refusal code is the next unit; its learner reasoning is pending. |
| Source-view refusal condition | Ali correctly evaluated the `or` condition and identified the producer-result retention comparison as the refusal cause, even though content is present. | Condition-reading exercise complete. Semantic source/assessment distinction remains a later retrieval target. Next unit is empty string versus None and the regression a truthiness substitution would cause; review answer pending. |
| Truthiness review and pacing | Ali identified the empty/None collapse in the alternative guard and requested broader/faster coverage, an overview of remaining work and a balance between learning and project completion. | Named the valid retained-empty input that would be wrongly rejected. Introductory exercise complete. Delivery now groups the same curriculum into four connected blocks with fewer integrated checks; no Build or broad mastery is inferred. |
| Block1 code preference and teaching | Ali accepted the four-block pace and explicitly asked to keep important code/source explanations. | Teacher provides the connected real-source lifecycle lesson and one integrated failure/test exercise. Guided coverage is recorded; learner response and independent application remain pending. |
| Deferring questions and Block2 | Ali explicitly requested questions later and full continuation to the next teaching block. | Earlier answer-before-advancing cadence is superseded. Block1 exercise remains unanswered. Block2 explains provider admission, correlation, execution eligibility, package-state composition, real FCI tracks and six focused tests; independent practice is deferred. |

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

## Learning checkpoint — October24: localization into actual source lookup

Recorded the learner's causal localization answer and completed only that introductory exercise. The actual saved-source function was inspected, with a read-only probe of HTTPX sources1–3 and an unknown ID. Teaching distinguishes search success from permission to present a record as original retained text. A producer-result record is preserved analysis, not missing data or original PR text; ordinary report assessments remain its presentation path. Existing source-view tests cover success/unknown/reference-only behavior; no new test or source change was made. Next learner response remains pending.

## Learning checkpoint — October24: faster connected teaching

Completed the pending truthiness review at introductory depth and recorded Ali's explicit pace correction. The teacher accepts that the earlier question cadence was too granular for the intended return to delivery. The curriculum is retained; delivery is consolidated into four blocks, one integrated check per coherent unit, with just-in-time depth and explicit deferrals. These are coordination groups, not engineering phases or a time estimate. Next block remains untaught. Product mode and source/tests/accepted plans remain unchanged.

## Learning checkpoint — October24: Block1 source-backed teaching

Recorded the explicit code-reading preference. Inspected provider record/parser, input preparation, native capture/layout/contracts/boundary/projection, report projection/file/CLI/viewer and existing test source. The full block explains record versus payload versus report, fixed representations and invariants, explicit absence/problem states and scoped refusals, three distinct digest scopes, file publication and offline reconstruction. No product implementation changed.

Fresh local teaching proof: the existing `test_source_cli_is_offline_read_only_with_distinct_error_outcomes` passed1 test/0.038s. Its intentional misuse check prints parser usage; the test still succeeds. Fixture work uses temporary files and controlled providers, not actual target/model execution. Existing real HTTPX native-boundary reconstruction also succeeds behind denied network/acquisition; codec1/owner github.pull_request/one input reference,9,348 UTF-8 bytes, native payload digest matches, and decoded native text equals saved report source text. This is bounded reconstruction fidelity, not a new live acquisition, complete checkpoint/replay, semantic acceptance or learner-owned proof. Existing originals remain unchanged.

Next is the integrated Block1 exercise in the resume point. Full historical908-test proof was not rerun. No AI inference, new package installation, target execution or source/test mutation.

## Learning checkpoint — October24: Block2 CI evidence and deferred exercises

User-directed adaptation: questions are postponed; teaching proceeds without claiming unanswered checkpoints are passed. Inspected Actions acquisition/run-attempt endpoint/required job identity, shared CI preparation, bounded correlator, step and exact-command execution, package-state composition and controlled tests. Read retained FCI001–3 results: selected attempts1;1/13/5 job heads/run IDs match their selected run and PR; FCI001 correlated, FCI002/3 unresolved/static_job_name_missing. These are October20 selected-CI diagnostic observations, not fresh calls today or whole-product results.

Actual FCI001: Release readiness job success; Set up job success; checkout completed/skipped; release validation completed/skipped; Complete job success. Completed step status does not substitute for successful conclusion. Current correlation permits runtime setup/post steps between uniquely matched ordered user steps. FCI002's later matrix is not its observed first refusal. FCI003's empty explicit PR-association array is not invented into a positive link. Frozen19 missing heads remain unchanged; conditional assumptions and later observed heads retain distinct proof classes.

Fresh teaching verification:6 existing tests passed/0.005s—captured second-attempt job endpoint, named-job/user-step correlation, missing literal-name refusal, continue-on-error masking, conditional-command ineligibility despite step success, and controlled positive package-state composition. No live acquisition, model call, target execution, source/test change or full908-test rerun. Reading retained public results does not rerun either official diagnostic batch. Positive test witness is not attributed to an FCI case; that diagnostic did not invoke the package-state or action evaluators.

Block2 preserves reuse and ownership: normal acquisition → exact static/runtime input bundle → static consumption/correlation → step/exact-command interpretation → same-command package-manager/state composition → report. A layer adds a distinct proposition, not a new investigation merely to repeat known evidence. Next lesson is Block3; deferred practice remains in the bank.

## Learning checkpoint — October25: Block3 impact and target relevance

Ali selected the third full connected block; important code remains included and questions stay deferred. Current Git remains on main after be417a0a; no product delta was found. Continued this same phase-free record under Learning-Only/working-memory Skills rather than creating a new cycle or teaching package. Root MEMORY's learning mode/engineering handoff remains unchanged.

Read the accepted Product Decision Model's candidate/applicability/coverage boundaries and current investigation, upstream support-drop extraction/grounding, Python-support candidate/selection/relevance, applicability composition, artifact comparison/target-tag and maintainer-action owners. Teaching distinguishes source quotation, semantic interpretation/admission, technical mechanism, exact target premises, candidate applicability, consequence and action permission. Deterministic composition consumes owner-assessed propositions; it does not itself validate source truth or establish completeness. One conjunctive path needs every necessary proposition; any refuted necessity eliminates that path; positive applicability needs one complete established alternative, while negative applicability needs all represented paths eliminated plus sufficient bounded path-model coverage. Evidence, path-model and candidate-discovery coverage are separate questions. A grounding check validates source/interval/quote constraints, not general semantic accuracy.

Real retained contrasts: (1) current normal HTTPX description access supplies copied app/proxies-removal versus cert/string-verify-deprecation context, but does not supply actual framework/caller binding. Read S002's bounded historical target/Starlette excerpts and the actual October19 packed delivered input's source pages: old/new HTTPX constructors and old/new Starlette super calls. Older captured call explicitly forwards app; newer captured call omits app while still accepting an app parameter itself. Proposed HTTPX constructor lacks app and **kwargs; cert remains explicit. This supports a conditional captured-source relation, not proof that the unpinned target installed either sampled framework or exercised it. The experimental ReferenceFact/keyword extraction already records explicit call keyword names and a ** marker; it is not a newly built generic relation solver or normal-product adoption. (2) retained October3 Soup Sieve normal model report grounds the Python3.8 drop and target >=3.10 declaration: outside_declared_python_range → established_not_applicable for this bounded candidate; action remains abstain. Do not import the broader manual S001 narrative's merge judgment into normal action authority. (3) October22 normal OpenCV retains27 removed/8 added exact tags and a proposed sdist; target associations remain not established/applicability unresolved. Full old/proposed tag intersection can refute wheel-path loss despite disappearance of a particular old tag. Published fallback is not successful source build; our own runtime is not the target environment.

Fresh learning checks:8 existing focused tests passed/0.001s—insufficient path-model coverage, established alternative with preserved conflict, exact declaration-investigation selection, no repeat after an attempted problem, Python non-overlap, old-compatible/proposed-incompatible wheel path, alternative proposed tag preventing loss, and CI support withholding action permission. Tests use controlled inputs/providers, not new real-target acquisition/execution, inference, installation or semantic evaluation. No full regression was rerun. Guided teaching and passing tests are not learner mastery or independent usefulness; deferred practice is explicit above. Next teaching is Block4, not implementation.

## Learning checkpoint — October25: Block4 failures, proof and engineering handoff

Ali requested the fourth block after Block3. Rechecked main at7c287e10 and the live owner's Learning-Only handoff; no intervening product delta was found. Continued the same learning-only responsibility and phase-free record. Questions remain deferred. No product/test/plan/spec/ADR changes, new model request/acquisition/target execution or new source-relation design were performed.

Read the completed October19 evidence-first comparison/source-aware adjudication:5 operational calls including canary complete; all4 semantic cases remain inadequate. Preserved partial corrections, HTTPX material relation omission, newer-consumer missed non-forwarding relation, glyphsLib unsupported workflow/coverage claims and older-consumer false cert removal/invented forwarding. This is a completed negative development result with exposed assistant review, not a reliability estimate or independent utility result. Root MEMORY separately preserves the older12-assignment comparison as discontinued/incomplete (3 completed,1 interrupted,8 unattempted); neither resume nor successful-subset ranking follows. Its file-age/elapsed-time correction illustrates why operational interruption, semantic failure and missing output are distinct outcomes.

Source teaching: experimental recover_spans verifies IDs/same-section/order and reconstructs producer-owned source text; decode_proposals validates shape/reasons then attaches recovered evidence, without an entailment oracle. The existing wrong-meaning/real-quote test deliberately returns a proposal, preserves proposed effective9.0 versus source-reported2.0, and refuses to convert empty observations into no impact. Read source parsing→ordered/scoped binding→established-only positive import admission, source-linked ReferenceFact and bounded adapter exploration. Alias restoration, conditional missing arm and trace exhaustion remain explicit. Latest satisfying stable adapter sample is not installed/resolved version; omitted candidates/limits are not global absence. Existing target context is independent of successful CI, so the proposed direction does not justify modifying CI owners.

Read actual checkpoint cold-child test: publishes a controlled revision, reopens read-only in another process, blocks acquisition/model/action/socket reentry and compares reconstructed text/hash/state. Read historical installed receipt and build review: separate installed package/CLI proof, controlled full-case composition and October23 full908-test result are historical and distinct from fresh teaching tests. Neither reconstruction nor saved-report reopening implies investigation continuation/replay; packaging and offline guards do not establish interpretation adequacy.

Fresh focused learning checks:7 existing experiment tests passed/0.015s—wrong-meaning/real-citation boundary and empty output, invalid/reversed/cross-section spans, alias rebinding/restoration, conditional import with unbound possibility, trace-budget refusal, sampling versus resolved version, and target context without CI prerequisite. Controlled providers/clients only; no actual model/target execution, new acquisition, broad regression or frozen semantic rerun/regrade.

Engineering handoff explained rather than executed: proposed bounded Planning/Design should qualify retained bytes/completeness/identity, reuse existing keyword/binding/source/adapter owners, settle admissible signatures and source correspondence/dispatch limits, expose observed facts versus conditional relation versus actual-target unknown, and require a concrete consumer plus real positive/negative/unresolved controls and finite costs. Dynamic ** expansion, positional rules, super dispatch, wrappers, truncated snippets and sampled versions need explicit admission/refusal. Reject package-specific expected-answer rules, generic parser expansion or inventory-only acceptance; reuse/defer/stop remain valid design outcomes. A future experiment-local success still needs separate normal-product admission and usefulness proof. All4 guided blocks are covered; independent understanding/questions and the user-selected return remain open. Root MEMORY need not change because product/mode/handoff responsibility did not change.
