# AUDIT-014 — Caller/signature native integration readiness

**Date:** 2026-11-01

**Inspected revision:** `e7082e96` on `main`, equal to `origin/main` after fetch.

**Responsibility:** independent review of the qualified experimental capability, native-adoption design, implementation companion and actual product integration boundaries.

**Authority:** non-controlling audit. Recommendations do not activate Build, change qualification rules, or establish product adoption. Lifecycle selection belongs in the [audit indexes](README.md); live execution selection belongs only in [MEMORY.md](../MEMORY.md).

## Assessment

**The planned direction is technically coherent and sufficiently grounded to enter its first, bounded native-representation proof when Build is authorized. I found no confirmed architectural blocker requiring a broad rewrite and no evidence requiring another arbitrary experimental case campaign.**

This is a qualified planning assessment, not an approval of an implementation that does not yet exist. The native capacity, source-progress publication, application/report integration and cold recovery obligations remain real gates. Their absence today is expected unfinished work, not evidence that the plans are defective.

There is **one concrete delivery-contract gap** worth settling before the application/CLI increment: how a partially failed invocation communicates its recoverable revision and command outcome. Three further recommendations below are proportionate improvements, not demonstrated defects or mandatory new workstreams.

The experiments have earned a conditional source-evidence capability. They have not established runtime compatibility, independent maintainer usefulness, or native product delivery. The current plans preserve that distinction correctly.

## Scope and evidence standard

The main reviewed owners are the [adoption/qualification design](../plans/CALLER_SIGNATURE_NATIVE_ADOPTION_AND_QUALIFICATION_PLAN.md), [implementation companion](../plans/CALLER_SIGNATURE_NATIVE_ADOPTION_IMPLEMENTATION_PLAN.md) and [whole-file analysis admission design](../plans/CALLER_SIGNATURE_ANALYSIS_WORK_ADMISSION_PLAN.md). I checked their relationship to the [upstream API/exposure parent](../plans/UPSTREAM_API_CHANGE_AND_TARGET_EXPOSURE_FEASIBILITY_PLAN.md), [Charter](../PROJECT_CHARTER.md), [Core specification](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md), [minimum-generality rules](../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md), and accepted [package](../docs/architecture/ADR-0007-responsibility-based-python-subpackages.md), [source-association](../docs/architecture/ADR-0011-explicit-source-association-bases-and-proposal-boundary.md), [Workspace](../docs/architecture/ADR-0012-canonical-investigation-workspace-and-recovery-boundary.md) and [reconstruction/storage](../docs/architecture/ADR-0013-versioned-native-reconstruction-and-workspace-checkpoint-storage.md) boundaries.

The executable trace covered qualified binding/extraction/comparison, correspondence and admission, source acquisition/accounting, fixed experimental readers, shared product dependency inputs, native capture/codecs/projection, lifecycle delivery, consumer access, CLI/report serialization and checkpoint storage. Relevant source/tests were inspected directly; planning prose was not treated as executable proof.

This is not a fresh semantic annotation of every historical experiment, an audit of every unrelated experiment family, a security penetration test, a new live acquisition, or an independent usefulness study. Older model-comparison outcomes are context, not evidence that the caller/signature capability works. No frozen experiment was rerun, repaired or regraded. No product, test, plan, specification or ADR was changed by this review.

### Current verification

The [audit evidence packet](../working-memory/evidence/2026-11-01-native-adoption-independent-audit/README.md) retains commands, results and the reproducible read-only artifact check.

| Check performed in this audit | Result | What it establishes |
|---|---|---|
| Frozen method/source reconciliation | All 106 indexed source hashes match | Inspected donor implementation remains the qualified source horizon; this is not native semantic-version admission. |
| Retained LifeLog, ordinary HTTPX and glyphsLib/protocol artifacts | 18 indexed files match; fixed opening and recorded work/source-text reconciliation pass | The selected development/regression cohort remains available and internally coherent. |
| Untouched Digimon attempt | 26 indexed files match; actual outer/inner fixed opening passes | The retained completed attempt and source closure remain inspectable. This does not rerun acquisition or independently prove every historical selection assertion. |
| Earlier curated HTTPX rejection control | Five indexed files match; fixed opening reproduces the five recorded outcomes, including the rejection | Negative local comparison evidence remains available, separately from the later ordinary capture. No new producer run or semantic regrading. |
| Guarded fixed opening | AST parsing, HTTP requests, socket connection, discovery, argument comparison and credential-reader hooks forbidden | The exercised reopening paths require none of those operations. Retained bytes remain unchanged. |
| Experimental API tests | 280 pass | Current focused donor behavior and experiment integration controls. |
| Selected product tests | 192 pass | Current native reconstruction, checkpoint, lifecycle, host, consumer, CLI/report and source-topology baseline. New caller/signature product behavior is absent and therefore untested. |
| Static experiment boundary check | Pass: 131 artifacts, 122 Python modules, 262 internal edges | Current inventory and static dependency direction; not a claim about every possible dynamic execution path. |

The first API test command resolved an older installed package and failed five module imports. The corrected checkout-explicit command passed; the original failure is retained. The artifact-check script likewise first lacked the repository root on its import path; that launch failure and correction are preserved. Neither was repaired by changing project source or reinstalling packages.

I did not rerun the entire product suite, the full experiment suite, or the governance doctor. The [qualified analysis verification](../working-memory/evidence/2026-11-01-analysis-capacity-and-work-admission/verification.json) records historical full-experiment debt of one failure, 25 errors and 11 skips; the [planning verification](../working-memory/evidence/2026-11-01-native-adoption-implementation-planning/verification.json) records the root governance marker debt. Those remain historical evidence, not newly verified green or newly introduced failures.

## What the experiments actually established

The evidence progression is credible because it preserves several distinct kinds of result rather than treating later success as erasing earlier failure:

1. [Curated HTTPX/Starlette comparison](../working-memory/evidence/2026-10-28-caller-signature-build/REVIEW.md) includes a real local rejection: the older forwarded `app` keyword has no receiving slot in the proposed initializer. The newer caller differs. This is separate from the later ordinary HTTPX capture, which does not contain that historical forwarding.
2. [Protocol/factory qualification](../working-memory/evidence/2026-10-30-protocol-factory-source-correspondence/REVIEW.md) extends the source-correspondence pressure beyond direct calls. Neither a factory witness nor local parameter reception establishes actual dispatch.
3. LifeLog exposed capture and analysis capacity failures. The [whole-file admission review](../working-memory/evidence/2026-11-01-analysis-capacity-and-work-admission/REVIEW.md) retains the failed larger-fact and intermediate representation attempts. The successor retains text, uses explicit whole-file admission and lossless trace tables, and keeps unchanged outer resource guards.
4. [Digimon qualification](../working-memory/evidence/2026-11-01-untouched-partial-analysis-qualification/ordinary-digimon-scraper-pr-16/REVIEW.md) exercised the unchanged frozen method on the selected new ordinary case. Its retained result has 14 source files, 1,463 facts and 21 comparisons; 20 native-version witness records represent five paired target roots. Both selected `get` definitions bind locally; forwarded `request` remains undetermined. Neither 20 records nor 21 comparisons means that many independent calls or successful runtime tests.

The current artifact check confirms LifeLog retains 28 files and leaves 17 Python units unexamined; HTTPX retains 24 files and leaves three unexamined; the protocol capture retains 12 files with no unexamined Python units. Full file analysis does not imply complete source-path or runtime coverage. LifeLog also records 3,044 omitted diagnostic entries. These are relevant presentation pressures, not concealed failures or a reason to invalidate useful partial evidence.

The one-case untouched gate is deliberately bounded. Existing varied controls plus one unchanged-method contrasting case support the selected transfer criterion; they do not estimate statistical reliability. The plans correctly reset the untouched claim after material method changes and preserve it after demonstrated equivalent relocation. No additional fixed case quota is justified by this audit.

## Design decisions that should be retained

| Decision | Independent assessment and reason |
|---|---|
| Explicit model-free caller/signature profile; existing default unchanged | Appropriate first integration boundary. Automatically combining CI/runtime/model work would introduce a different aggregate-budget and proof problem. The deferred combined profile remains a real product limitation, not something this audit silently removes. |
| One cohesive cross-repository analysis owner with existing provider foundations | Reasonable responsibility split. Target-only or provider-only placement would misdescribe analysis spanning target, old/proposed dependency and samples. No extra framework or service is needed. Exact module splits remain ordinary implementation judgment. |
| Shared `AcquiredDependencyInputs` and one invocation ledger | Correct. `investigation.py` already obtains the PR/dependency prefix; calling the experimental full runner would duplicate orchestration and could hide costs or identity drift. Account for every physical retry within the same limits. |
| Separate source and comparison native families | Correct separation of retained observations from derived analysis. Source progress can survive later analysis failure; comparison basis must remain bound to its actual source record. Native source text need not be duplicated in the comparison payload. |
| Minimum record transfer plus actual native capacity proof before bulk promotion | Essential and already in the plan. LifeLog's normalized fact cost is 194,179 of 196,608 allocated structure tokens and comparison cost 32,632 of 32,768. Additional native wrappers cannot be assumed free. This is an acknowledged gate, not a newly discovered omission. |
| Explicit trace normalization and owner-specific duration layout | Defensible. The current native codec does not deduplicate repeated records or admit floats. Canonical finite hexadecimal seconds preserve existing values without a broad primitive change. Its precision is preservation of the measured value, not a claim of equivalent clock accuracy. Implementation proof remains required. |
| New-family producer-version support only | Correct. `_decode` currently rejects non-null versions, while capture emits absent versions. Both ends must change together for the new methods; old families must retain their historical gaps. Codec version is not semantic version. |
| Fixed reconstruction rather than producer replay | Required by the admitted recovery contract and already implemented for earlier families. New reconstruction must not parse source, rediscover candidates or synthesize a new historical action. |
| Retain the generated report/action as a lifecycle delivery | Fits the existing `ConsumerView`/`ViewDelivery` path and avoids a second domain truth family. It still requires actual material/method binding, enclosing-capacity proof and disclosure of duplicated retained source bytes. |
| Schema1 report as a first implementation baseline | Reasonable, not yet proved sufficient. Current records can carry facts, assessments, unknowns, sources and limitations; the strict state reader needs explicit new admissions. A schema bump should follow a demonstrated representation need, not anticipation alone. |
| Existing abstention authority unchanged | Correct. Source-local `bound` or `rejected` is not permission to merge, block or execute checks. Native presentation may expose useful evidence while the action remains abstention. |
| Historical experiments remain separate; active analyzers delegate to product owners | Correct end state. Preserve fixed old envelopes and evidence while avoiding two independently evolving implementations. Tests must continue to distinguish product proof from experiment compatibility. |

No unsupported mechanism should be retained merely because it exists in the experiment. In particular, curated selectors, historical hash admission, freeze orchestration, attempt-directory lifecycle and unused release-window machinery have no automatic product claim. The companion explicitly recognizes this and does not propose a wholesale copy.

## AUDIT-014-F1 — Complete the CLI failure-to-recovery handoff contract

**Classification:** bounded implementation-plan gap. **Priority:** medium before the application/CLI increment; not a blocker to the first representation probe. **Confidence:** high about the omission; no claim of an observed defect in the unbuilt profile.

**Evidence.** The implementation companion's application/CLI section (lines 152–160 at the inspected revision) requires `--workspace-store PATH`, `--open-workspace PATH --revision REVISION_ID`, source-only recovery, preservation after save/render/size failures, and no retry after conflict or unknown acknowledgement. It does not specify how the invocation exposes the revision needed by that recovery command or maps the new operation outcomes to command success/failure. The parent design has the same durable-recovery intent without completing this interface contract.

The current [CLI](../src/upgradepilot/cli.py), `main` lines 69–145, owns explicit exit handling for input, acquisition, report save/open, source availability and projection errors. It has no Workspace output receipt or checkpoint-error branch. This is expected current behavior, but it supplies no existing end-to-end contract for the new feature to inherit unchanged. The [store](../src/upgradepilot/workspace/checkpoint_store.py), `inspect_publication`, already distinguishes exact publication inspection from retry; the [host](../src/upgradepilot/workspace/lifecycle_host.py) owns publication state.

**Consequence.** A source checkpoint could be correctly retained after analysis or report failure, yet the command might expose only a generic failure. The user would then need internal store knowledge to identify the revision for the promised explicit recovery command. Conversely, a useful partial result, failed execution, unknown publication acknowledgement and successful report save are different outcomes; one undifferentiated success indicator would obscure them. This is a foreseeable interface ambiguity, not evidence that storage currently loses data.

**Smallest recommended change.** In the existing implementation companion, settle a compact outcome/handoff table before implementing the CLI increment:

- Distinguish useful partial completion, explained unsupported/insufficient evidence, execution/resource failure, publication conflict or unconfirmed acknowledgement, report delivery/save failure, and invalid historical opening.
- Define command exit meaning separately from evidence usefulness and compatibility. Reuse existing codes where their meanings fit; this audit does not prescribe new numeric codes.
- When durability is confirmed, expose the store and exact recoverable revision, plus whether it contains sources, comparison and/or retained report. Give the explicit offline-open invocation.
- When acknowledgement is unknown, identify the attempted revision and last confirmed boundary without calling the attempted publication durable. Use the existing identity-inspection path if selected; never retry capability work automatically.
- State volatile-only and pre-initialization failure honestly; they cannot promise a durable revision.

**Required proof if adopted.** One actual CLI failure after a source checkpoint must expose an identifier that a fresh process can use to open that exact checkpoint without provider or evaluator calls. A report-save failure must distinguish retained Workspace/report delivery from the absent external report file. An acknowledgement-loss control must not produce a false durability claim or duplicate capability execution. Compose these into the already-planned failure controls; no separate recovery framework or broad new plan is needed.

**Owner/disposition:** clarify the companion's application/CLI acceptance section, then implement through existing application/CLI/host owners when authorized. Do not change the source-analysis method or restart untouched qualification solely for this interface clarification.

## Improvements worth considering, without treating them as defects

### AUDIT-014-I1 — Inspect a realistic report view earlier

**Recommendation:** during representation/projection work, inspect one explicitly labelled retained-evidence report sketch before the bulk acquisition transfer. Use the actual LifeLog or protocol result and show distinct roots, paired outcomes, witness alternatives, necessary premises and omitted coverage. Keep the final native maintainer-task review required by sections 6 and 8.

**Reason:** the existing generic report renderer emits every assessment's facts, details and limitations. LifeLog has 145 comparisons, 256 retained gap entries and 3,044 omitted entries; protocol evidence has many witnesses for few roots. Correct data can still require excessive reading. An early sketch can expose that cheaply, before presentation assumptions become entrenched in the native mapping.

**Limit:** I did not conduct a human usability trial, so this is a sequencing improvement, not a finding that the new report is unusable. A sketch neither establishes product delivery nor justifies dropping premises or changing admission. Keep it in the same cycle/evidence record, not a new UI project.

### AUDIT-014-I2 — Measure native-consumer navigation before adding another API

**Recommendation:** include delivery count, bytes and navigation effort for one root-level question in the connected consumer check. Reuse the report/source path and current bounded paging first. Add a structured per-root view only if a concrete consumer cannot reasonably answer the question through those paths.

**Reason:** [WorkspaceEvidenceAccess](../src/upgradepilot/workspace/consumer_access.py) currently bounds whole native views and falls back to exact JSON pages of at most 4,096 characters. The retained LifeLog result is approximately four megabytes. Byte paging preserves access but does not by itself make a call-to-definition question convenient. Native representation and report projections may reduce that burden; measure the actual result before designing a new interface.

**Limit:** paging already exists. Large payload size is not a missing-access defect, and this audit recommends neither a generic object browser nor larger default delivery budgets. The new profile must extend family/projection validation as already planned.

### AUDIT-014-I3 — Bring installed-package smoke proof forward when the worker moves

**Recommendation:** once the product-owned package and worker entry exist, run a small installed-distribution smoke check from outside the checkout with `experiments/` unavailable. Keep the broader installed-product and historical compatibility checks at final qualification.

**Reason:** the plan already requires installable product independence, and the static boundary checker passes. This audit nevertheless demonstrated that the local interpreter can resolve an older installed product unless the checkout is explicit. An explicit-source test suite can therefore pass while concealing packaging or worker subprocess resolution problems. The worker's module invocation is a useful early point to test the actual distribution boundary.

**Limit:** this is a test-order refinement, not evidence of a packaging defect in the unbuilt feature. Do not change environments, add dependencies, or create a packaging framework just to satisfy the suggestion. Record exact interpreter/import origin for the check.

## Questions resolved without adding findings

- **“Should all Workspace families migrate first?”** No necessity was demonstrated. The selected profile can use the admitted source/comparison/lifecycle path while unrelated migrations remain explicit debt.
- **“Must another untouched case run because code moves?”** No. A changed hash is not by itself changed semantics. The planned equivalence mapping is the correct discriminator; material acquisition/admission/meaning changes still require successor qualification.
- **“Do both versions binding make the experiment uninformative?”** No. A conditional positive source relation is useful evidence. The earlier genuine rejection remains a separate regression pressure; a new negative outcome must not be manufactured.
- **“Are partiality and omitted diagnostics failures to hide?”** No. They are reported limits. The audit confirms retained partial records exist; the product must preserve their meaning.
- **“Does lack of a global float primitive require redesign?”** No. The selected owner-specific scalar representation is adequate in principle and has an explicit first-increment proof obligation.
- **“Does a large result make current native access impossible?”** No. Paging exists. Convenience and cost need measurement, as I2 states.
- **“Can green current tests establish native adoption?”** No. They establish the donor and existing product baseline, not the unimplemented join.
- **“Should old failing experiments be repaired during this migration?”** Not without a relevant supported responsibility. Preserve baseline debt and require every newly introduced product failure to be resolved or explicitly blocked.
- **“Should this review add models, agents, an execution engine, new persistence or broader Python semantics?”** No evidence here justifies those additions.

## Recommended disposition

Keep the current adoption scope, ownership and staged proof sequence. Clarify F1 before the application/CLI increment. Consider I1 and I3 as inexpensive ordering refinements within existing work; keep I2 conditional on a measured consumer problem. Do not make these suggestions an excuse to rewrite the plans or delay the already-selected representation probe with unrelated cleanup.

The first native probe should still stop if the retained cohort cannot fit real native layouts and enclosing guards without semantic loss. Later acceptance still requires connected product acquisition, source-progress retention, native comparison, report/source delivery, fixed recovery, compatibility proof and an honest task-review disposition. No part of this audit activates those operations.

Reviewer assistance: AI-authored independent inspection of the repository and retained evidence; no independent human usefulness or learner-mastery claim. The [cycle record](../working-memory/2026-11-01_caller-signature-integration-independent-audit_cycle.md) preserves the review route, proportional process adaptation and verification limits.
