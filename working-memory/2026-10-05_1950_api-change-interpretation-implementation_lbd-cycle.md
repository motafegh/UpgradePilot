# Source-linked API change proposals — implementation and controlled-provider proof

Date/time: 2026-10-05 19:50 Asia/Tehran.
Session status: ACTIVE — B implemented and engineering-verified; D learning current, E pending.
Owner: [API-change/target-exposure feasibility plan](../plans/UPSTREAM_API_CHANGE_AND_TARGET_EXPOSURE_FEASIBILITY_PLAN.md), especially its source-only contract and implementation/proof handoff.
Method: [ADR-0011](../docs/architecture/ADR-0011-explicit-source-association-bases-and-proposal-boundary.md), Core §§6–6.3 and Minimum Useful Generality.
Previous: [pre-cycle readiness](2026-10-05_1936_api-interpreter-readiness_pre-cycle.md) and [closed design preparation](2026-10-05_1617_api-change-interpretation-preparation_lbd-cycle.md).
Skills: `UP-SKILL:upgradepilot-build-implement`, `UP-SKILL:upgradepilot-learning-by-doing`, `UP-SKILL:upgradepilot-working-memory`.

## Authorization and selected responsibility

After discussing the recommendation, its rationale and alignment with the earlier design, Ali explicitly agreed and requested formally starting the new cycle properly. The selected scope is experiment-local source-only API interpretation implementation, an explicit opt-in ordinary PR integration path, and controlled-provider acquisition → proposal → saved-recovery engineering proof. Actual model accuracy/omission evaluation follows in a separate immediate cycle after this cycle closes; it is not silently added to this Build or indefinitely bypassed by more infrastructure work.

Authorization persists across the cycle's learning gates; those gates are opportunities to establish/challenge understanding, not repeated requests for implementation permission. Formal entry followed A0 → A1; Ali subsequently requested proceeding to A2 without a separate understanding check, as recorded below. The previous D remains explicitly deferred; agreement about this cycle does not establish mastery of the prior whole design.

## Cycle status

- A0 — DONE: fetched remote; reconciled live owners, readiness/design handoff, exact implementation/proof plan, source/test seams and unchanged executable horizon; cycle record and living orientation map initialized.
- A1 — DONE: starting-state/evidence-maturity/proof-boundary teaching delivered; Ali explicitly said he got it and requested A2 without stopping for a check. Continuity opportunity completed; independent reasoning/mastery remains unassessed.
- A2 — DONE for orientation with explicit check adaptation: source-to-proposal implementation, ownership/data flow, failure and preservation behavior, controlled-provider proof and non-goals explained. Separate recall/pre-B check waived at Ali's request; actual mechanism ownership remains unassessed.
- B — DONE: experiment interpreter, opt-in ordinary PR integration, controlled-provider proof and versioned offline recovery implemented.
- Verification gate — GREEN for engineering scope: 31/31 focused; 120/120 active trial regression; touched Ruff/format and actual saved-read CLI equality pass. No live-model semantic or product acceptance.
- D — CURRENT: verified implementation/proof-limit handoff prepared; explanation delivered with this Build handoff, independent ownership and questions remain open. Earlier design D remains deferred.
- E — PENDING: repair/defer findings and close with the immediate real-model evaluation handoff.
- C — CONTINUOUS: this record owns meaningful cycle progression and evidence/learning gaps.

## A0 current-state reconciliation

Entry HEAD and origin/main are both `7999eea3064b126be012c44f513d308bd13976bf`; fresh fetch found no remote delta. Since closed design head `a9d34fd7`, the only committed delta is readiness evidence and live/detailed state records. No product/experiment executable or test delta invalidates the pre-cycle baseline. The unrelated untracked broad-audit record remains outside scope.

The preparation produced `source-only-api-change-v1`, generic prompt/schema, producer-reference design and 19 paired development inputs/expectations. Fresh readiness checked nine frozen artifacts, 20 sections, 75 mapped lines, all 734 within-section contiguous spans, evaluator separation and six retained producer-code identities. All model case review statuses remain `not_run`; no API-role model response exists.

The five active API trial test modules passed 100/100 and `pip check` passed during pre-cycle readiness on the same executable tree. Neither is rerun solely to initialize this documentation-only cycle entry. Full product/installed and unrelated full experiment regression were not run in readiness. The historical broader experiment-suite debt remains disclosed. Governance doctor reproduced the pre-existing missing `examples/` responsibility-map marker; this unrelated root/checker mismatch is not repaired by this cycle or claimed green.

Provider metadata in readiness was HTTP 200 on direct loopback `127.0.0.1:18080`, with the maintained Gemma `gemma4`/`Q4_K_XL` available but unloaded. This is a dated preflight observation, not a refreshed active deployment/capacity claim. Exact executable rendering, effective tokenizer/template/context, output reserve and provider schema behavior remain unverified; the current engineering responsibility can use controlled providers. Live inference stays behind its before-inference gate in the later evaluation responsibility.

Active flow inspected: `DeclaredReleaseWindowAcquirer.acquire` creates separate declaration-based complete or retained partial/ambiguous source results; `release_window_manifest` preserves the available sections and their scope; `acquire_public_pr_context` independently acquires exact target/static context and adapter exploration; current trial CLI writes acquisition-only packets. `decode_adapter_seed` validates retained adapter seed/revision/binding relationships and supports affected recovery tests. None implements API meaning. The product support-drop extractor remains a separate admitted narrow role; only its public loopback session factory is eligible for fitting reuse. No weaker source basis is cast into trusted support-drop objects.

No contradiction requires a new plan/specification/ADR at entry. The prior readiness ordering correction remains valid: exact final token-fit measurement follows implementation/freeze of the normal renderer and precedes live inference; it is not fabricated before that renderer exists.

Initialization checks: all nine frozen hashes/sizes rechecked and unchanged; all 17 local links across the three touched state records resolve. Authored documentation whitespace passes. No regression suite is rerun for this source/test-unchanged initialization; the recorded pre-cycle baseline remains explicitly scoped to its original run.

## Living A-phase orientation and learning map

### A1 continuity topics

- Distinguish prepared design from implemented API interpretation: source acquisition/binding/recovery exists, the semantic request/decoder/proposal path does not.
- The earlier cycle's engineering preparation is verified, while actual whole-design understanding remains deferred. Recent discussion established agreement on the responsibility/proof split without claiming code-level mastery.
- Explain the readiness findings and unchanged baseline: controlled-provider Build is selected; actual provider/template/context fit and API meaning are later proof obligations.
- Make the agreed change in live selection explicit: the proposed implementation cycle is now formally opened; live semantic evaluation is the immediate subsequent separate responsibility.

### A2 upcoming responsibility map

- Trace typed acquired complete/partial source → producer-controlled sections/line IDs → exact rendered request → controlled or local response → strict structure/reference checks → attributed proposals or explicit failure → versioned saved result/read-back.
- Teach the two important boundaries: code establishes source correspondence and preserves evidence; model meaning and omissions need separate evaluation. A recovered proposal does not become a product finding or an applicability/action claim.
- Explain controlled-provider injection as repeatable engineering evidence; show failure propagation and independent context preservation. Saving/read-back is offline preservation, not interrupted execution resume or fresh acquisition.
- Preserve acquisition coverage, model-reported unassessed spans and evaluator omission detection as different facts. Empty observations never establish absence of changes/impact.
- Use the actual HTTPX removal/deprecation passages for decision-relevant explanation; no syntax micro-quizzes or prior deferred D replay is required. Reasoning questions remain optional discussion aids under Ali's explicit preference against a separate check.
- Expected proof: discriminating input/output/reference/provider/capacity/truncation checks plus opt-in normal composition and saved recovery; stronger claims remain withheld.

## B boundary and proof route

One cohesive experiment responsibility with appropriately named modules/tests. Routine implementation choices remain inside Build. Do not introduce a generic inference framework, new dependency, database, agent machinery, broad graph analysis or package-specific phrase engine. Read source and relevant tests before mutation; apply Source/Naming Clarity and end-to-end ownership before material added checks/fields.

Use the frozen domain contract/prompt intent without supplying evaluator labels to the producer. Preserve every available source section/candidate, exact source text/ranges, declaration basis, missing/ambiguous scope and method identities. Strictly reject duplicate JSON keys, invalid structure/references and truncated/provider-failed output. Do not salvage partial results, secretly retry, shorten input or weaken grounding to obtain a pass. Deterministic validation cannot prove meaning or detect every free-text unsupported claim.

Keep the acquisition-only entry and existing product/support-drop/report/action behavior intact. Opt-in interpretation and offline saved recovery must be explicit. Failures preserve independently acquired target/adapter knowledge. Define the affected experiment result/version handling before changing serialization; saved input has an independently admitted reader boundary with bounded parsing and relationship checks. Reuse existing recovery only where its responsibility fits rather than calling fresh exploration to reopen a result.

Validation order after B: focused new responsibility tests → normal acquisition/inference-proposal composition and saved read-back controls → full active API trial regression. Inspect/run product regression and installed checks if shared product code changes; separately admit any needed shared provider mutation. Avoid broader testing without a changed boundary or unresolved concern. Controlled tests and an unchanged product tree do not establish product adoption.

Stop at a material design/contract conflict or proof blocker and preserve it; re-route substantive unresolved design to its owner. No live API-role inference, target install/test execution, model substitution, product integration, broader target-impact claim, independent usefulness or semantic admission is selected here.

## A1 handoff

At formal entry, the project had prepared source-only interpretation and verified acquisition/static-context/recovery foundations. The A1 handoff paused to give Ali an opportunity to question/correct that model before A2. The subsequent transition below records his instruction to proceed; implementation authorization was already given.

## A1 learning focus — starting state and evidence maturity

Ali asked for proper explanation of what must be retained, understood and mastered from A0/A1. Required responsibility-level depth: reconstruct the current implemented/prepared/unverified boundary; interpret evidence only within its exercised scope; distinguish acquired source/static context, model proposals, semantic evaluation and actual target impact. These concepts are needed to challenge implementation/evaluation claims and diagnose the next work. Exact hashes, test counts, filenames and provider API details are lookup-level; prior whole-design D and new implementation mechanics are not silently marked mastered. A2 will own the latter's minimum-complete orientation.

Teaching used the actual retained HTTPX removal/deprecation source and current readiness evidence. Two reasoning checkpoints about partial-source scope and semantic-accuracy evidence were offered. Ali requested proceeding without a check; no answer or demonstrated mastery is inferred. Continue the same cycle; no Learning-Only reroute, learning artifact, source/test mutation or extra regression run is selected.

## A1 transition and A2 orientation — user-directed check adaptation

Ali said he got the A0/A1 explanation and requested proceeding to A2 with proper teaching and no stop for checking. Circumstance: continuous context, prior scope/proof explanation and explicit learner preference. Normal route: separate continuity and pre-B understanding checkpoints. Chosen adaptation: complete the continuity opportunity, deliver the minimum-complete A2 and avoid a separate recall/quiz checkpoint; preserve an opportunity for questions/corrections and independent ownership as unassessed. Effect: implementation authorization and evidence/verification obligations are unchanged; this is not a semantic acceptance or mastery waiver. Required reconciliation: current phase/check adaptation recorded here and compact continuation in `MEMORY.md`; D later assesses actual sufficiently evidenced implementation at justified depth.

A2 teaching focuses on the missing experiment-local source-only producer/request/decoder/proposal/recovery path. Existing acquisition supplies exact complete or retained partial/ambiguous release evidence. The new producer maps every available section/line; the prompt carries source/context/limits without target or evaluator answers; the model proposes change kind/subject/assertion/timing/effective version and cites source IDs; deterministic code checks bounded shape, references, uncertainty requirements and source reconstruction while preserving proposal authority. Schema/grounding success does not assess meaning. Real HTTPX `proxies` removal and string-valued `verify` deprecation illustrate the contract using the actual frozen line map; any displayed interpretation is hand-authored teaching material, not a model result.

Explain acquisition coverage, model-reported unassessed spans and evaluator omission detection separately; preserve complete/partial/ambiguous scope beside returned observations. A provider/contract/grounding/capacity/truncation failure remains specific and retains independent target/adapter evidence. Explicit opt-in trial integration prevents existing acquisition-only behavior from implicitly calling inference. Versioned saved read-back preserves source text/identity, proposed meaning, scope, method and failures without fresh inference/acquisition; source/proposal integrity must not promote meaning into accepted product authority.

Core ownership targets: follow code-owned evidence identity versus model-proposed meaning; explain why response handling and preservation need repeatable controlled-provider proof. Operational understanding: request rendering, schema/decoder, source maps, actual context plus completion reserve, versioned reader and test seams. Lookup/deferred depth: exact enum values, offsets/library APIs, actual provider/tokenizer deployment and real-model evaluation mechanics; no need to memorize source syntax before it exists. B will implement/freeze the normal renderer and integration; controlled tests come before the active API trial regression. Exact loaded deployment/schema support/token fit precede later live evaluation, not a guessed character-based pass here.

No separate recall question is required before the already-authorized B continuation. No substantive B, new test result, model inference or demonstrated learner mastery occurred during this orientation.

## B entry — source, retention and validation decisions

Ali explicitly requested proceeding to building. Preflight inspected the normal acquisition entry, typed complete/retained partial records, release projection and current recovery/integration tests, public local-session transport and Source Clarity heuristics. Baseline remains the earlier 100 active API trial tests on the unchanged executable tree; new interpretation boundaries have no tests yet.

Implementation will use a cohesive experiment interpretation module plus an opt-in trial/saved-reader module, and extend the existing ordinary-PR composition test family beside new interpretation boundary tests. The current acquisition-only entry remains untouched. Prepared prompt/schema stay at their frozen design home and are verified/identified when used; no duplicated semantic schema, generic inference framework or dependency addition is justified.

Retain exact acquired input/source-map and structured proposals in a versioned saved packet beside the existing context. The independently admitted saved-reader boundary checks packet consistency, reconstructs the input from its acquisition projection and recovers proposal quotations; a digest is consistency evidence, not authenticity. Raw prompt/response strings and failed response content are not saved. Method/input identities and source content remain available without treating saved output as inference replay.

Local transport will refuse inference without request-bound effective-capacity evidence; controlled providers exercise integration directly. This prevents default opt-in execution from treating metadata maximum context or source characters as fit. Actual capacity measurement and provider schema execution remain the next live-evaluation responsibility. Specific input/provider/context/contract/grounding/truncation failures will preserve independent target/adapter context rather than overwrite the whole trial.

## B evolution — boundaries implemented and first proof

Implemented a cohesive experiment interpreter and opt-in trial/read-back module; extended ordinary PR composition tests and added focused interpretation/provider tests. The frozen prompt/schema are verified on use, not copied into a second semantic contract. The shape decoder implements only the frozen schema's actual keywords; uncertainty reasons and source-span recovery remain explicit additional checks. The request renders every available source character once through labelled lines, retaining offsets/hashes in the saved producer map instead of inflating inference input with redundant representations.

Complete acquired sections must correspond to the required releases. Partial/duplicate candidates retain scope and separate IDs; missing/omitted text never triggers inference. No deterministic phrase matching establishes change meaning. The controlled wrong-meaning test deliberately passes structural/reference validation, making the semantic proof limit executable. Source release and model-proposed effective version remain different fields.

The opt-in entry uses the normal PR/dependency/target/upstream/adapter acquisition path. Save/open is independently bounded/versioned, preserves all context branches, checks target/head/binding relationships with the existing pure seed decoder, rebuilds source maps/request identity and reconstructs every citation. Recomputed outer digests do not admit changed quotations, ranges, maps or scope. Digests are consistency evidence, not origin authenticity. Failed interpretations retain source scope plus independent target/adapter evidence; raw failed model content is not serialized. New saves refuse overwriting prior runs.

First focused run: source/decoder checks passed; two HTTP tests errored because a plain Mock did not implement a response context manager. Changed the fixture to MagicMock. After tightening source/release relationships, two fabricated fixtures ceased representing their intended states (an invented complete duplicate and omitted candidate without required-version metadata); corrected those fixtures rather than weakening the checks. Focused new/interacting result is now 28/28. An intermediate active-trial regression before the additional authentic-source test passed 116/116; final regression remains pending until source review ends.

Added retained-real HTTPX component recovery: inspect the previously acquired full 1,367-character window and exact target/adapter packet; fresh controlled interpretation cites `S2:L18` and recovers the real `proxies` removal quote with encode/httpx commit/path identity. This is historical ordinary acquisition plus fresh controlled engineering proof, not fresh network acquisition or model semantic quality. Tests also exercise fresh ordinary composition with controlled public provider responses. No live inference or new public acquisition has run.

## Verification gate — final engineering result

Source review tightened two genuine serialized/request boundaries. First, request decoding uses the exact frozen schema loaded into that request, avoiding a second asset read after provider output; unavailable preparation assets become a contract failure while retaining input. Second, saved complete windows cannot be relabelled under a different dependency interval by changing context/input and recomputing both request and packet digests. Mapping reuses the existing public dependency version-ordering owner for this relationship, without introducing a parallel version algorithm or reinterpreting source meaning. The new adversary changes the proposed release to 3.0 and recomputes every relevant digest; recovery still rejects it. Failure-state/source/request relationships are also checked. A redundant fixture-only calibration integrity test was removed: readiness already owns that inspection; active tests instead exercise actual mapping, composition and recovery behavior.

Final proof on the reviewed executable tree: **31/31** focused new/interacting tests; **120/120** active six-module API-trial regression (baseline 100 plus 20 new test methods). Touched Ruff check and format check pass; new CLI help passes. [Evidence and reproduction](evidence/2026-10-05-api-interpretation-implementation/README.md) distinguish normal controlled public-response composition from the [historical-real HTTPX recovery](evidence/2026-10-05-api-interpretation-implementation/controlled-httpx-recovery.json). A real subprocess opened the final local saved packet offline with exit 0 and exact packet equality. Saved size: 696,454 bytes, below 8 MiB. All nine frozen preparation assets remain unchanged; no model case was evaluated.

Retained source: full available HTTPX window (1,367 characters), exact line/quote identity and independent target/adapter branches. Final method identity includes input/request/template/schema/renderer/interpreter hashes; the evidence record freezes eleven producer/shared-mechanism file identities before live output. Structured failures never salvage partial candidates or trigger hidden retries. Source coverage, model-reported unassessed material and evaluator omissions remain independent.

Scope review: only two new experiment source modules, one new focused test module, the existing ordinary-composition test module and dated/live evidence records change. No product source/test/dependency/workflow or accepted plan/specification/ADR changes. The public loopback session factory and version-ordering helpers are reused as existing public mechanisms. Full product/installed and unrelated full experiment suites were not run because their executable responsibilities did not change. No hosted verification was dispatched: the existing workflow is manual product verification, outside this experiment proof. The known governance marker failure and historical unrelated experiment-suite debt remain unresolved and are not renamed green.

Engineering verification is GREEN for the selected controlled-provider implementation responsibility. Real-model capacity/schema support, semantic accuracy/omissions, broader target-exposure composition, independent usefulness and product admission are unproved. No live inference, fresh external acquisition or environment/dependency change occurred. The default local provider remains fail-closed without caller-measured, exact-request-bound effective capacity. Such a record checks accounting/binding consistency; it does not independently measure tokens or attest its own authenticity.

## D entry — learn from the verified path

B and engineering verification are complete. D is now the active learning/ownership responsibility; it will explain the real implementation, authentic HTTPX citation recovery, controlled adversaries and remaining proof boundaries. Pre-B check adaptation does not establish independent ownership. E remains pending until material D gaps are addressed or explicitly deferred. The next cycle remains actual local-provider/development semantic evaluation after D/E; this cycle does not perform it.

## D first teaching handoff and ownership frontier

The explanation accompanying this verified increment follows the actual responsibility flow: source acquisition owns identity/window scope; `source_input_from_projection` owns IDs and exact recoverable lines; `prepare_request` owns frozen full-source request rendering; the provider proposes meaning; `decode_proposals` validates structure/uncertainty and reconstructs evidence; `run_interpretation_trial` preserves independent branches; `decode_saved_trial` rechecks the saved evidence without inference or acquisition. The HTTPX example grounds that explanation: the controlled `proxies` proposal references S2:L18 and recovers the exact removal statement. Producer-recorded release 0.28.0 is distinct from the model's proposed effective version.

Retain these reasoning boundaries: a correct quote can accompany an incorrect meaning; empty observations do not mean no changes; incomplete acquisition can still support limited proposals without becoming complete; failed interpretation does not erase target/adapter knowledge; offline reopening establishes preservation/consistency rather than fresh truth or execution resume; a request digest binds capacity evidence but does not measure tokens. Compared with A2, the responsibility/proof split held; source review added explicit interval-relabelling and failure-state consistency controls, and compact rendering reduced avoidable request overhead without omitting source.

Independent ownership is still unassessed. Optional D reasoning prompts concern (1) a correctly cited future removal labelled current: which proof passed and which failed, and (2) capacity failure after successful target acquisition: which branches remain usable and which claims remain unavailable. These are opportunities for discussion, not renewed implementation authorization. Material misconceptions, if found, belong to E repair/defer; none is invented from lack of an answer. Earlier design D remains deferred.

Final documentation checks: all 18 local links in the touched live/cycle/evidence owners resolve; all 11 retained producer hashes match the final executable tree; all nine frozen preparation asset hashes remain unchanged; `git diff --check` passes. The unrelated untracked broad-audit working memory remains excluded. Publication follows the standing validated-increment cadence on main; no target/upstream external write or hosted workflow action is included.

Publication verified: implementation/evidence commit `ba3e78051a4d17078d58a11ad87bb5dffaf8b270` was pushed to origin/main; local and remote identities matched with 0/0 divergence. Only the excluded broad-audit record remained untracked. This follow-up records publication evidence without executable changes or new verification claims.
