# Caller/signature native adoption implementation

**Artifact status:** implementation companion prepared for review and explicit Build activation. Writing or approving this artifact does not execute the product transfer, a live attempt or product cutover.

**Responsibility:** deliver the qualified caller/signature source-evidence capability through ordinary UpgradePilot acquisition, native Workspace material, reports, source inspection and durable offline recovery.

**Source horizon:** main `c53430c6`, inspected November 1, 2026. Paths below are execution mappings, subject to source reconciliation before their increment. [`MEMORY.md`](../MEMORY.md) alone selects live work and records completion.

## 1. Relationship to the existing design

The [native-adoption and qualification design](CALLER_SIGNATURE_NATIVE_ADOPTION_AND_QUALIFICATION_PLAN.md) owns the adoption scope, source-evidence meaning, qualification rules, profile and recovery contract. This companion owns exact responsibility transfer, implementation dependencies, checks and acceptance. It specializes the parent's ordered delivery responsibilities; it does not create a second adoption policy or replace its gates.

Apply the [Charter](../PROJECT_CHARTER.md), [stage plan](UPGRADEPILOT_90_DAY_PLAN.md), [Core invariants](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md) including `JUST-*` and recovery §6.4, [Product Decision Model](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md), [Minimum Useful Generality](../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md), [Naming Clarity](../docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md), [source-association ADR-0011](../docs/architecture/ADR-0011-explicit-source-association-bases-and-proposal-boundary.md), [Workspace ADR-0012](../docs/architecture/ADR-0012-canonical-investigation-workspace-and-recovery-boundary.md) and [reconstruction/storage ADR-0013](../docs/architecture/ADR-0013-versioned-native-reconstruction-and-workspace-checkpoint-storage.md). [ADR-0007](../docs/architecture/ADR-0007-responsibility-based-python-subpackages.md) governs package admission and executable dependency direction; [Security](../SECURITY.md) governs credentials, private retention and external actions.

The [whole-file analysis design](CALLER_SIGNATURE_ANALYSIS_WORK_ADMISSION_PLAN.md) supplies the qualified allocation/partiality method. Reference it rather than revive older full-input assumptions or re-specify its algorithm here. Existing specs/ADRs suffice for the selected transfer. A materially different resource, trust, persistence, recovery or semantic method must return to its proper owner before implementation.

[AUDIT-014](../audits/2026-11-01_AUDIT-014_caller-signature-native-integration-readiness.md) was independently reconciled against the current interface owners in the [dated disposition record](../working-memory/2026-11-01_caller-signature-readiness-audit-plan-reconciliation_cycle.md). Its failure/recovery handoff clarification and three measured sequencing refinements are incorporated below. They do not change analysis semantics or activate Build.

## 2. Product outcome, scope and entry evidence

The supported question is: **which retained target calls can be related to selected old/proposed Python definitions, how are their arguments received locally, and which source/version/import/dispatch premises remain unresolved?** Deliver that evidence with original text, partiality, method identity and recovery. Preserve distinct responsibilities:

| Responsibility | Authority and claim boundary |
|---|---|
| Acquisition/retention | Records exact observed source, selection, association and costs; does not establish installation or execution. |
| YAML/runtime correlation | Remains with existing CI owners; this source-only profile does not run it. |
| Dependency/runtime-state proof | Remains with existing dependency/CI owners; bound source arguments are not installed-state proof. |
| Source correspondence/comparison | Establishes qualified conditional paths and local `bound`, `rejected` or `undetermined` results. |
| Interpretation/presentation | Presents evidence and missing premises; does not manufacture semantic compatibility or applicability. |
| Maintainer decision | Existing action/adequacy authority remains separate; local rejection is not permission to change or merge anything. |

Include the qualified direct/import/forwarding/initializer/limited factory-protocol forms, ordered binding alternatives, keyword reception, unknowns, partial work and failed acquisition/analysis. A direct-call-only demo or a viewer for experimental bundles does not complete this responsibility. Complete retained text and incomplete analysis must remain distinguishable.

The explicit `--evidence-profile caller-signature` is the initial model-free product entry. The existing default invocation must retain its behavior. A default combined API/CI/runtime profile, general dynamic Python resolution, arbitrary value flow, runtime execution, independent semantic/usefulness acceptance, all-family Workspace migration and automatic continuation/replay remain separate responsibilities. These exclusions control proof and implementation coupling; they do not declare missing installation/dispatch evidence irrelevant to the user's eventual decision. Re-enter them when an actual consumer question or retained failure requires that evidence.

### Dated entry evidence

| Evidence | What it can establish for this transfer |
|---|---|
| [Qualified analysis review](../working-memory/evidence/2026-11-01-analysis-capacity-and-work-admission/REVIEW.md), [method freeze](../working-memory/evidence/2026-11-01-analysis-capacity-and-work-admission/qualified-method.json) | Experimental binding2/checker1/correspondence2, explicit whole-file profile, complete text, checked trace normalization and resource admission; implementation at `a8233eb9`. |
| [Retained results](../working-memory/evidence/2026-11-01-analysis-capacity-and-work-admission/retained-qualification-results.json) | LifeLog partial-capacity pressure, ordinary forwarded HTTPX and glyphsLib/pytest protocol pressure. Reuse is exposed retained evidence, not fresh acquisition. |
| [Untouched Digimon review](../working-memory/evidence/2026-11-01-untouched-partial-analysis-qualification/ordinary-digimon-scraper-pr-16/REVIEW.md) | One unchanged-method ordinary transfer with five informative paired roots; selected `get` binds in both versions while forwarded `request` remains undetermined. No native product acceptance. |
| [Native entry observations](../working-memory/evidence/2026-11-01-untouched-partial-analysis-qualification/native-adoption-entry-observations.md) | Concrete capture/projection/codec/CLI seams and unresolved representation choices. Observations are not an implementation. |

The one untouched contrasting case is sufficient under the parent's frozen-method gate when relevant semantics are unchanged. A demonstrated equivalent relocation does not require an arbitrary extra case campaign. Apply the parent's development-exposure rule to material changes, including acquisition, selection, association, admission or limits: preserve original results, freeze a qualified successor, and obtain a new untouched contrasting case before cutover. Never regrade old evidence with current code.

Before using retained material, verify the exact private input/result/companion availability and hashes against its public-safe index. Missing local material is proof debt, not authorization to refetch into the frozen capture or substitute a different version. A separately labelled derivation/reacquisition needs its own contract and cannot restore an observation that was never retained.

## 3. Product ownership and transfer map

Use a cohesive `src/upgradepilot/caller_signature/` owner for analysis across target and dependency repositories. Target-only declaration ownership and provider-specific packages cannot honestly own that cross-repository comparison. Flat root modules would scatter the same admitted capability. This is a concrete responsibility boundary admitted through ADR-0007, not a generic service framework. Create modules only when real implementation enters them; no empty package scaffolding in planning. The mapping below selects responsibility-bearing seams, not a requirement to retain every helper or create one module per dataclass.

| Qualified source seam | Product destination | Transfer treatment |
|---|---|---|
| `api_python_bindings`: `ImportFact`, `ReferenceFact`, `BindingTraceStep`, `BindingAssessment`, `analyze_python_bindings`, `binding_state` | `caller_signature/bindings.py` | Move the pure ordered/scoped analysis and limits with discriminating native tests. Preserve alternatives, reasons and trace order. |
| `api_call_signature`: `SourceSpan`, `CallArguments`, `ParameterFact`, `CallableSignature`, `SourceFacts`, `AnalysisLimit`, `extract_python_source`, `compare_arguments` and result types | `caller_signature/analysis.py` | Move extraction/comparison; preserve conditional receiver and argument semantics. No runtime import of analyzed code. |
| `api_source_correspondence`: `PythonSourceModule`, `SourceRelationshipStep`, `module_name`, `absolute_import`, `analysis_group_key`, `discover_source_candidates` and its private traversal/admission | `caller_signature/correspondence.py` | Move supported path discovery and complete whole-file allocation; preserve priority, group atomicity, omissions and limits. Keep graph concepts separate from dependency installation reachability in `dependency/uv_reachability.py`. |
| `api_signature_evidence`: `AnalysisLimits`, normalized trace encode/decode, structure-cost calculation, fact/span/comparison integrity | `caller_signature/evidence.py` | Extract reusable typed domain records and fixed integrity rules. Remove experiment method-closure/file-IO responsibilities from the product subset; keep one shared trace implementation. |
| `api_target_context`: inventory/client, dependency declarations, import candidates, `TargetContextAcquirer`, fact extraction bridge | `github/repository.py` for provider inventory; new `target/source_context.py` for target selection/declaration/import context | Reuse repository identity/text clients and existing dependency parsers. Move only needed context behavior; keep existing narrow `target/python.py` requires-python owner intact. Binding extraction delegates to the new reusable owner. |
| `api_change_source_acquisition`: `PublisherProvenanceInspector`, `associate_declared_source`, required association/problem records; source-retrieval subset of `DeclaredReleaseWindowAcquirer` | Existing `pypi/provenance.py`, `upstream/repository.py`, `github/tag.py`, `github/repository.py` retain provider/association foundations; `caller_signature/source_acquisition.py` owns remaining qualified composition | Reuse admitted association bases. Transfer the source subset and independently required premises; changelog/release-window selection not consumed by this profile stays experimental. No second URL-trust authority. |
| `api_adapter_exploration`: dependency metadata, `select_exploration_version`, `PythonModuleSourceRequest`, `ExaminedPythonModule`, `PythonSourceAcquisitionWork`, `PythonSourceAcquisitionRun`, `AdapterSourceExplorer` | `caller_signature/source_acquisition.py`; provider-only metadata uses existing `pypi/api.py` boundary | Move qualified native/sample selection, module requests, adapter exploration and source accounting. Keep samples distinct from native versions. Preserve positive-origin adapter admission and conditional direct-source admission. |
| `TrialAcquisitionPolicy`, `TrialPublicSession`, timeout-recovery policy/receipt | `caller_signature/acquisition.py`, delegating credential confinement to `github/auth_session.py` and transport to existing clients | Rewrite experimental names/wrapping into explicit shared invocation policy and accounting. Preserve physical-attempt charging and selected recovery eligibility; do not modify account quota or generic provider defaults. |
| `api_target_context_smoke.acquire_public_pr_context`, `examine_changed_package_modules`, ordinary `prepare_ordinary_inputs` and `acquire_ordinary_comparison_inputs` | `caller_signature/source_progress.py`, invoked from `investigation.py` with `AcquiredDependencyInputs` and the ledger in `caller_signature/acquisition.py` | Split reusable source selection and publication material from transport and trial envelopes. Accept already acquired inputs so the caller uses a single PR prefix. |
| Ordinary `prepare_ordinary_comparison`, analysis-admission/discovery checks, result records | `caller_signature/evidence.py` for records/integrity; `correspondence.py` for production; `worker.py` for bounded execution/composition | Rewrite envelope coupling into typed native inputs/results. Keep producer execution separate from decoding. Explicit native methods, not experiment source hashes, admit reconstruction. |
| Ordinary `_worker`, `run_ordinary_comparison` process control | `caller_signature/worker.py` | Move the earned worker limits/isolation mechanism; use product-owned entry and bounded exchange. Do not launch an experimental module from runtime. |
| Fixed native shapes | `caller_signature/native_codec.py` for file facts/durations; `caller_signature/result_codec.py` for cross-file analysis input/result closure; families registered through `workspace/native_codecs.py` | Explicit owner encode/decode and known version layouts, using shared bounded representation primitives. Separate cross-file integrity from per-file trace integrity; no generic dataclass reflection or opaque experiment envelope. |
| Catalog creation and source views | `workspace/source_access.py`, caller/signature source payload and `workspace/consumer_access.py` | Reuse exact text/catalog validation; domain source roles/membership belong to the caller/signature owner. No second independent source browser. |
| Native capture/projection, host/store, normal CLI/report | Existing `workspace/native_capture.py`, `native_projection.py`, `lifecycle_host.py`, `checkpoint_store.py`, `investigation.py`, `cli.py`, `report_projection.py`, `report_file.py`, `report.py` | Extend their admitted responsibility; do not build a second application, store or report truth owner. |
| Curated selectors, trial manifests, `api_release_window_manifest`, method-source hash admission, outer attempt/freeze/private-file layout and historical readers | `experiments/` | Keep experimental. Thin adapters may call product owners for new production, while fixed historical envelopes keep explicit compatible decoding. Do not refresh saved hashes or rewrite frozen bundles. |

The module names above are concrete execution targets; a later demonstrably simpler split/merge is ordinary design judgment if ownership/dependencies/proof are preserved and this mapping is reconciled. Do not grow an acquisition monolith merely to fit a filename. A new external dependency, generic execution engine or durable architectural boundary requires its own justification/owner review.

Dependency direction: bindings → no acquisition; analysis → bindings; evidence → analysis/bindings plus fixed representation primitives; correspondence → evidence/analysis plus admitted source catalog; source acquisition → provider/target owners; acquisition → those owners plus source acquisition; worker → evidence/correspondence. Native codecs depend on records, not runners. Application composes these with Workspace; CLI composes application and consumers. No product import of experiments/tests/tools, and no dependency/CI owner imports the new capability just to infer runtime state.

## 4. Freeze semantic equivalence before transfer

Bind the qualified method and immutable retained inputs in the implementation cycle before moving source. Maintain an explicit mapping for changed record/source IDs and experimental roles (`target`, native-old/new, samples) to product roles `target_repository`, `old_dependency`, `proposed_dependency`, `constraint_sample`. Record the exact observed spellings from each admitted envelope; do not infer them from this summary.

Compare experimental and native projections modulo only that reviewed mapping:

- Exact source text/digests/repository/revision/path, dependency transition, selection and association bases, native versus constraint-sample identities and uncertainty.
- Import/reference/call/signature facts, order/spans, binding alternatives/reasons/traces, receiver assumptions, path alternatives and required premises.
- Local outcomes/violations/keyword reception and root-to-pair membership; logical calls remain distinct from multiple witness records.
- Whole-file group membership/admission/order, analyzed versus unexamined units/reasons, scanned versus admitted work, candidate omissions/exhaustion, and all semantic work limits.
- Failure/partial/non-evaluated distinctions and the source text retained when later work fails.

Preserve binding2/checker1/correspondence2 behavior and `static-import-whole-file-analysis/1`, including paired module admission, external-import root priority, all-source scan charges and producer structure-allocation semantics. Literal paths/versions/repository names or reviewer witnesses cannot become selectors. Keep renamed/conditional/rebinding/ambiguous/unsupported controls alongside real cases.

Different timestamps, native material IDs, native wire sizes and measured costs are expected; compare their meanings and limits rather than assert byte-identical outputs or equal elapsed time. Preserve experimental method identity as lineage, separately from native producer and decoder identities. Any unexplained semantic difference fails equivalence until classified. Do not silently accept it because native output looks more useful.

## 5. Native material and representation decisions

### Families, basis and states

Implement two owner-specific codec1 families as selected by the parent:

| Family | Retained material and basis |
|---|---|
| `caller_signature_sources` | Exact source catalog/text, target/dependency roles, declarations/import/association bases actually used, selection/source questions and refusals, acquisition policy/events/recovery, available timings/costs/omissions and native method identity. References actual `investigation_inputs`; include PR description basis only where consumed. |
| `caller_signature_comparison` | Analyzed facts, normalized traces, discovered roots/paths/premises, argument outcomes/reception, coverage/admission/work/limits and bounded analysis problems. References the exact sources record and investigation inputs. Source texts are not duplicated here. |

Use existing envelope/lifecycle state machinery. `not_evaluated` means no producer run; a recorded payload can contain typed partial/failed/problem results and retained progress. Worker completion, useful paired evidence and complete coverage are independent. `facts=None` is admitted only for a supported explicitly unexamined unit; an analyzed unit without facts is invalid. Absence, empty text, no candidate, unsupported analysis, failed execution and missing/corrupt material must remain distinguishable.

Capture initializes both families with valid placeholders/input edges and refreshes pending references using the existing owner. Add producer-version staging and exact known support for these two new producer methods only. Initial native family producer versions are `"1"`, separately identifying component versions/profile and codec1. Final method identifiers are the installed owning producer functions from section3, frozen with native tests. Existing families keep their None/version-unavailable gaps; new unknown versions refuse affected reconstruction. Do not globally admit all non-null versions or relabel codec1 as semantic version1.

Adding families must not retroactively require them in older checkpoints. Existing supported projections remain inspectable from their historical material; requesting the absent caller/signature projection returns an explicit missing/not-available outcome. Do not rewrite old stores to insert fabricated placeholders or silently migrate their schemas.

The source payload uses `caller_signature/source_evidence.py` records and `source_codec.py`: one exact catalog/module-role/analysis-limit root plus typed acquisition receipts. Preserve target declarations/import candidates/coverage, module requests/origins/refusals/metadata, sample selection, material omissions, source work, physical-request/recovery receipts and source-method lineage. Full observations reuse existing release/project-link/publisher/tag evidence types. Historical receipt-only qualification uses explicit `retained_experiment` origin and missing full-association/tag observations; it never invents those observations or proves normal product acquisition. Unrelated release-window/changelog result bodies stay with their admitted owners.

Family producer version1 identifies the exact installed emitters `workspace.native_capture.NativeInvestigationCapture.capture_caller_signature_sources` and `capture_caller_signature_comparison`; the payload separately retains analysis producer1/binding2/checker1/correspondence2 and acquisition lineage/gaps. `comparison_codec.py` receives the exact decoded source family for fixed cross-file result validation. These concrete splits refine the section3 map without adding a new store/runner or allowing codec1 to stand for semantic support. The actual normal acquisition producer and its source-first lifecycle composition still require their own implementation/qualification.

### Trace representation and capacity

Use explicit per-file normalized trace tables and checked integer references, preserving every original step/alternative/order/reason. Do not naively embed repeated full trace dataclasses through `RecordRef`: current native encoding adds wrappers and performs no graph deduplication. The owner may use fixed `ObjectFields`/sequence layouts where adequate; no opaque serialized graph/string, arbitrary class loading, compression bypass or global resource increase.

Retain the qualified producer work-allocation/cost semantics. Measure additional native payload/envelope/checkpoint/report overhead separately; do not silently reduce admitted units or paths to absorb wrapper cost. The early probe must encode/decode the retained cohort through real native layouts and enclosing guards, measure bytes/structural cost and expanded-reference work, and compare every trace. LifeLog is required pressure, not just a small synthetic payload. If required native material does not fit, preserve the result and return to a representation/design decision before bulk promotion. A different allocation/admission method needs material-change classification and qualification.

The native JSON limits remain 64MiB/depth64/262,144 structure tokens at their actual boundaries; report-file capacity remains its own 16MiB owner. Passing an inner payload guard does not prove its enclosing checkpoint or report fits. No source omission or summary-only saved report may silently replace the admitted retention contract.

### Exact timing and costs

Select owner-specific canonical hexadecimal finite-float scalar text for existing measured durations, decoded with an explicit supported duration layout. This preserves the original binary float exactly without adding a global float primitive. The field must declare seconds and measurement scope; bound its length, require canonical `float.hex()` form, finite nonnegative values and exact round trip. It encodes one numeric scalar, never a hidden evidence structure. Expose readable seconds in presentation while retaining the exact value. Unknown/unmeasured durations remain absent with a reason, not zero.

Prove representative fractions, zero, supported extremes and malformed/negative/nonfinite/type/canonical-form refusals. Preserve integer request/byte/candidate counts and available stage/total measurements; distinguish wall elapsed, charged acquisition and worker time, and measured peak memory from unavailable measurements. Do not invent precision or add stage times as though overlap cannot occur. If this simple owner layout fails a real consumer need, revisit this decision before extending global scalar semantics.

### Fixed validation placement

Domain codecs validate fixed shapes, bounded scalar/trace/span integrity and supported semantics. Workspace projection validates exact target/material-input/source-role relationships. Host/store owns admitted publication and lineage. Consumer projection consumes those guarantees; add repeated checks only for a distinct supported boundary under Core `JUST-*`.

Require the complete ordered protocol witness and premises whenever **any** of `allocation`, `attribute_getter`, `factory_return`, `call_protocol` appears. Retain the discriminating corruption control with both former trigger operations removed while protocol residue remains. Reject wrong roles/versions/content joins, foreign fact/path identities, duplicate/unused/out-of-range/bool trace indices, paths through unexamined units, inconsistent work/admission and unknown support. Valid different source repositories/revisions must not be rejected as though all material belongs to the target.

Reconstruction validates recorded facts and their closure; it never reparses Python, reruns discovery/checking, selects current defaults, loads arbitrary classes or reacquires missing evidence.

## 6. Delivery increments and acceptance

Each increment is a coherent authorized Build/Learning-by-Doing cycle with progressive public-safe records and appropriately validated commits/pushes. Repeat source reconciliation where intervening work matters. Commit boundaries may combine tightly coupled changes; they must not manufacture product acceptance for an unfinished layer. Equivalence runs throughout, not only at the end.

Apply [Operating Guide §7.2–7.3.1](../OPERATING_GUIDE.md#72-ai-assisted-engineering-ownership) to select a scoped ownership opportunity and justified depth within an increment, such as tracing retained source progress or verifying a recovery failure boundary. Record the actual attempt/assistance separately from product proof in the existing cycle; deeper standalone study stays in its applicable learning route. Advanced internals need not all become immediate participation prerequisites. This clarification leaves the delivery sequence, supported scope and engineering acceptance obligations below intact.

### Responsibility freeze and native representation proof

Reconcile the section3 map with actual imports/callers/tests, extract the exact reference projections and ID mapping, and move the minimum pure record types needed for real native record/trace/duration encoding in the capacity probe. Use actual native encode/decode/guards, not a synthetic dictionary merely labelled native. No product import of experimental types is allowed even for this early increment. Keep the feature unselected by default.

**Acceptance:** retained text/facts/traces/partiality round-trip equivalently for the cohort, duration/version decisions have discriminating checks and native overhead fits. Failure or unavailable material is a preserved blocker at this design/proof boundary, not a passing probe. No bulk kernel move before sufficient representation proof. A probe is representation proof, not Workspace/application adoption.

Within representation/projection work, inspect one early report sketch using actual retained LifeLog or protocol material before bulk acquisition transfer (AUDIT-014-I1). Label it retained experimental evidence/presentation exploration, not a native product result. Show distinct roots, paired outcomes, alternative witnesses, necessary premises, unexamined units and retained/omitted diagnostics. Record readability/navigation concerns in the same cycle; preserve all material premises. This is an inexpensive sequencing refinement, not a human-usability acceptance gate or a new UI project. Keep the final native task review.

### Product analysis owners and native evidence

Promote bindings, extraction/checking, correspondence, evidence/admission and the bounded worker. Introduce the real `caller_signature/` package with implementation. Migrate active experiment production to delegate where compatible, retain explicit historical readers, and account for every moved substantive helper in the cycle map. Register/capture/reconstruct both families with exact producer identities and material references; test staged defaults and old-family behavior.

**Acceptance:** focused native tests preserve full admitted scope, retained-cohort projections match, codec/protocol/work corruption refuses correctly, unknown versions have explicit outcomes, and historical bundles still open under their earned contract. Product execution imports no experiment module. Do not retain two independently evolving analyzers or claim adoption from codec-only tests.

When the product package and worker entry exist, perform installed-distribution smoke proof immediately (AUDIT-014-I3), before acquisition transfer. Build the actual artifact and use a temporary isolated environment with available declared dependencies, outside the checkout, with `experiments/` unavailable and no injected source/checkout PYTHONPATH. Record interpreter, artifact identity, parent/worker import origins and subprocess command; run a small bounded analysis through the installed worker. Verify both processes resolve the selected installed artifact. Do not change the existing developer installation or add dependencies/frameworks for this check. Keep broader installed-product qualification later; a checkout-explicit test pass cannot substitute for this distribution proof.

### Shared acquisition and source-progress publication

Transfer target context, library acquisition and invocation policy composition through existing provider/association owners. The caller/signature branch accepts the normal `AcquiredDependencyInputs` from `investigation.py`. One shared ledger includes the common prefix and every physical retry; avoid a hidden independent session or counter reset. Keep auth host confinement, redirect refusal, identity guards, original uncertainty and native/sample separation.

Initialize Workspace after the shared prefix establishes the observed exact target. Publish purpose/request/admission/attempt intent before capability work. Publish acquired source progress before analysis, with actual input/material basis and required receipts. Preserve useful progress when later library acquisition, receipt encoding, analysis or publication fails. Unreturned values, pre-initialization failure and disk failure retain only what actually reached the admitted store; missing completion stays unknown. Source text without required association/receipt remains observed text with a gap, not admitted comparison evidence.

**Acceptance:** actual-client controlled composition proves a single prefix/ledger, exact repo/PR/base/head joins and absence of hidden calls; source checkpoints survive supported post-acquisition failures. Timeout/memory/fact/structure/candidate stops remain typed and do not become no-exposure results. Source-first behavior uses Workspace boundaries, not copied experimental attempt files.

### Normal application, CLI and durable report delivery

Add the explicit evidence profile at the ordinary application entry; keep provider/domain sequencing out of CLI. Reuse schema2 host/store, predecessor conflict, acknowledgement and backup behavior. Implement explicit `--workspace-store PATH`, disclosed volatile operation without it, and `--open-workspace PATH --revision REVISION_ID` for selected offline recovery. Reject recovery combinations with live repository/PR/auth/profile arguments; no automatic latest-target refresh, resume or store migration.

Keep source-profile delivery composition in `src/upgradepilot/caller_signature_delivery.py`: delegate provider sequencing to `investigation.py`, project canonical native evidence through `report_projection.py`, publish the report through the host and return structured operation/publication context to CLI. The same application owner performs fixed historical report opening without generation or capability authority. CLI retains arguments, display and shell exit precedence.

Project the caller/signature report from canonical native material through normal report/consumer access. Prefer existing schema1; extend strict known assessment/state admission where sufficient. Keep the parent report contract for distinct roots/witnesses, old/proposed local outcomes, premises, coverage, costs and full retained source views. Source-only CI/runtime branches say not evaluated; do not fabricate empty successful runs, installations or applicability evidence. Do not add a second evolving caller/signature store to `PublicPullRequestInvestigation`.

Newly requested report generation may invoke existing maintainer synthesis under its authority. Retain the exact encoded report/action in lifecycle ConsumerView/ViewDelivery with the complete actual material basis and installed projection identity before acknowledging a report-bearing checkpoint. The retained report is historical delivery, not a new native fact family. `--open-report` and Workspace recovery decode it without invoking the report-generation/synthesis path. A selected source-only checkpoint without a report remains source-only; no report is fabricated during recovery.

**Acceptance:** normal CLI → Workspace → report → original source view → saved report/store → fresh-process open works; old CLI/report tests retain behavior. Empty versus absent source remains correct. Save/render/size failure preserves Workspace and reports delivery failure without truncating or replacing evidence. Recovery under forbidden provider/credential/AST/discovery/checker/model/synthesis/target-code hooks succeeds for valid retained deliveries and refuses supported corruption. Publication conflicts and unknown acknowledgements never trigger capability retry.

#### Command outcomes and recovery handoff

Settle the failure-to-recovery contract through application/CLI/host owners (AUDIT-014-F1). Return the minimum structured operation/publication context needed by CLI; keep it separate from native source-comparison truth. In particular, current host `current` advances only after acknowledged publication: it cannot identify an unacknowledged attempted successor. Preserve attempted identity and last confirmed boundary at the publication owner; do not invent them from exception text. Reuse existing exact store inspection where that operation is selected, rather than introduce a second store or generic receipt framework.

For the explicit caller/signature profile and new Workspace-opening mode, use this exit contract. Preserve existing default invocation and report-opening codes. Exit status describes the requested command, separately from evidence usefulness or compatibility:

| Requested operation outcome | Exit | Required distinction |
|---|---|---|
| Completed requested delivery, including useful partial evidence or an explained unsupported/insufficient result | `0` | Display evidence disposition and coverage separately. Unsupported/insufficient is not positive qualification. An admitted partial result differs from a hard-aborted producer. |
| Input/auth configuration rejected | `2` | No claim of acquired evidence or durable revision before initialization. |
| Acquisition failure / invalid provider response | `3` / `4` | Preserve current categories, actual costs and any independently confirmed earlier checkpoint. |
| Requested external report-file save failed | `5` | File save failed even if report display or Workspace delivery succeeded; name their distinct statuses. |
| Invalid saved report / unavailable requested source | `6` / `7` | Preserve existing offline semantics; never acquire replacements. |
| Report projection, rendering or retained-report delivery encoding failed | `8` | Report request failed; distinguish an already confirmed source/comparison checkpoint from a report-bearing revision. Storage publication failure uses11 instead. |
| Invalid/unsupported/missing requested Workspace revision on offline open | `9` | Identify affected boundary; no silent fallback to latest/earlier revision. Valid explicit source-only opening may return0 without synthesizing a report. |
| Analysis execution/hard resource failure | `10` | Partial retained sources may survive, but analysis did not complete. Explicit supported partial admission can instead complete with0. |
| Publication conflict, failed durability or unconfirmed acknowledgement | `11` | Distinguish conflict, known failure and unknown completion; no false durability or capability retry. |

When several failures occur, preserve all causes. Publication uncertainty/failure takes exit precedence, then failed producer work, then projection/render/delivery, then external save. Evidence usefulness never overrides a failed requested operation. Unsupported/insufficient evidence may be a successfully delivered answer, while remaining a failed positive-adoption criterion.

Always give a compact operation/evidence/durability handoff on completed or failed profile invocations where context is available. For confirmed durable state, expose the store path, lineage and exact confirmed revision plus presence of sources/comparison/retained report at that boundary; print the safely quoted explicit `upgradepilot --open-workspace PATH --revision REVISION_ID` invocation. Report external saved-file success separately. State missing report/comparison without silently generating either. Volatile state must say volatile-only, with no durable-open promise. Pre-initialization failure has no Workspace revision.

For acknowledgement uncertainty, disclose attempted revision and last confirmed boundary separately; the attempted revision is not labelled durable. Exact `inspect_publication` may resolve that identity as published/not-published; an inspection error remains unknown. Do not infer absence from a failed inspection, silently follow a competing head or rerun the capability. Preserve the staged identity needed for supported inspection, and avoid exposing credentials in diagnostics.

Add discriminating controls within the planned CLI/recovery tests: a hard analysis failure after a source checkpoint prints a confirmed identifier that a fresh process opens with forbidden provider/evaluator calls; report-file save failure distinguishes Workspace/report delivery from the absent file; acknowledgement loss cannot claim durability or duplicate capability work, including failed identity inspection; conflict/volatile/pre-initialization cases expose only their earned boundary. These checks complete the handoff contract, not a new recovery framework.

### Connected retained qualification and separately frozen product attempt

Exercise all selected retained/control pressures through the normal product application with controlled provider responses. Direct kernel invocation is not sufficient. Keep retained-input analysis, controlled provider composition and real fresh acquisition as distinct proof classes. Run the matrix in section7 and resolve new supported-contract defects before a live product attempt.

For one fixed root-level call-to-definition question, measure delivery count, delivered bytes, paging/source operations and reviewer navigation effort through the existing report/source/bounded-native paths (AUDIT-014-I2). Record whether the answer and required premises were recovered, and distinguish machine-delivery counts from measured human time. A large payload alone does not prove missing access. Only a demonstrated consumer difficulty justifies a smallest sufficient structured per-root projection; decide that extension in the owning design before implementing it. Do not enlarge delivery budgets, build a generic browser or omit premises merely to improve the measurement.

Before any provider call for that attempt, freeze one **native product** contract: descriptive case/attempt identity; exact repo/PR/base/head/dependency guards; installed method/runtime/config/profile; auth mode and credential source without secret values; allowed hosts/methods; shared-prefix budget; source/analysis/correspondence limits; recovery policy; new private store/report/evidence destinations; expected coverage and useful/partial/unsupported/refusal/stop criteria. Freeze task criteria from section8 before outcome review. An exposed PR can prove connected product behavior, not untouched generalization. Never reuse the experimental `controlled_ordinary_pr_composition` or fresh experimental attempt envelope as product authority.

Use the parent's ordinary limits and qualification/retry rules as the baseline, with all-prefix accounting. Measure controlled request allocation before freezing the invocation. The product profile may not silently gain a second allowance, cap enlargement, selector or automatic retry to reach useful evidence. GitHub account quota and local policy are different limits. A supported explicit PyPI pre-response-timeout recovery remains charged within the same totals; no whole-attempt retry or target execution.

**Acceptance:** the normal product invocation retains actual acquisition/analysis/publication/render/save costs and useful conditional paired evidence with exact source closure; saved Workspace/report/source recover in a separate process without reevaluation. Preserve every failed/inconclusive attempt with its cause, costs and disposition. A transport/identity/availability failure is not a checker failure; a legitimate unsupported source form is not a mandate to patch a lower owner. A demonstrated supported defect must be diagnosed and repaired under a recorded successor, with exposure/equivalence consequences. Do not repeat until green.

### Maintainer-task review and adoption disposition

Review the actual retained native output against section8, record corrections and proof limits, and choose engineering adoption of the explicit profile, limited pilot, repair, defer or reject. Passing native engineering is not independent usefulness, full-project completion or permission to merge target PRs. Default-profile expansion requires its own decision.

**Acceptance:** all applicable delivery/proof obligations have evidence and an explicit disposition; no unresolved new product failure is hidden by experimental debt. The live handoff links the exact records and names remaining responsibilities without beginning an unrelated expansion.

## 7. Qualification matrix and validation order

| Pressure | Required comparison/control |
|---|---|
| LifeLog retained full input | Same complete text and whole-file admissions/reasons; scanned versus admitted work; native paired evidence and unresolved forwarded call; native trace/payload/checkpoint/report capacity under unchanged guards. Original strict failures remain frozen. |
| Ordinary HTTPX | Preserve one logical forwarded call with multiple export witnesses, paired local outcomes and sample/import uncertainty; do not reintroduce a historical app keyword absent from this capture. |
| Retained local rejection | Preserve the genuine earlier HTTPX rejected-versus-bound case under its own source/version premises, separately from later ordinary evidence. Both passing/binding cases alone do not qualify rejection behavior. |
| glyphsLib/pytest and renamed controls | Preserve initializer/factory/protocol paths, ordered witnesses and variadic/dispatch uncertainty. Historical CI/runtime limitation remains a separate missing proposition. |
| Digimon retained qualified input | Preserve five distinct paired roots, both local get bindings, unresolved forwarded request and actual gaps. Its experimental fresh status does not make native replay fresh or untouched. |
| Work limits and partiality | Irrelevant files, conditional imports/aliases/rebinding, indirect components, atomic old/new refusal, oversized required file, syntax problem, fact/node/candidate/structure/time/memory stops and zero-candidate outcomes. All text survives where admitted retention succeeded. |
| Integrity and method support | Source/target/role/transition swaps, path/span/fact corruption, incomplete protocol residue, trace-table corruption, wrong basis, analyzed missing facts, inconsistent unexamined sets, unknown family/codec/producer version. Distinguish unsupported, missing and corrupt. |
| Publication/recovery | Post-source analysis failure, missing required receipt, serialization/store conflict/disk/ack failure, interruption before/after intent, source-only checkpoint and retained report checkpoint; previous committed revision survives. Fixed cold open performs no work. |
| Compatibility and boundaries | Existing product source/report/CLI/store behavior and None-version gaps; fixed historical experiment envelopes; installed product package without experiments available; static product dependency rules. |

Validation order: focused owner tests → native family/capture/projection controls → actual-client controlled application/host/store/report/source tests → retained equivalence → actual CLI and fresh-process cold recovery → historical compatibility → full active product suite and architecture checks. Begin the relevant equivalence checks at the first changed owner, and repeat affected checks when source changes; do not run the whole suite after every tiny edit.

Use current product suites including `tests/test_source_topology.py`, native reconstruction/checkpoint/lifecycle/host/consumer tests and `tests/test_cli.py`, `test_report.py`, `test_report_file.py`; introduce native caller/signature tests under `tests/` for the new responsibility. Experimental tests and `tools/check_experiment_boundaries.py` provide separate compatibility/boundary evidence. Exact commands/selection and fresh results belong in cycle evidence, not a permanently green plan.

The source-horizon experimental broad suite had recorded baseline failures and the governance doctor had a root marker mismatch. Preserve them as dated debt, establish the applicable product baseline and distinguish new failures. They do not waive any introduced product failure. Never report documentation checks, test totals or byte round-trip alone as native adoption, semantic acceptance or independent usefulness.

## 8. Maintainer task and decision criteria

Before the final product attempt, freeze the task, baseline inputs, reviewer exposure/assistance, questions, measures and disposition rules. Use the same retained source and actually available version/CI/release context for both views; do not grant historical installation/dispatch answers absent from either capture.

The reviewer must recover the exact dependency transition; locate a relevant target call and any forwarded/protocol path; compare old/proposed local reception; identify unresolved applicability premises and unexamined coverage; inspect exact original source; and name the next evidence that would distinguish a remaining uncertainty. Score faithful completion, missing/misleading premises and correction burden. Record navigation operations/time when actually measured and separate acquisition/analysis/render/restore costs. Without measurements, report observations and unknown benefit rather than claimed time savings.

AI-assisted source-aware review may establish engineering corrections and a justified explicit-profile pilot, with exposure disclosed. It cannot supply independent maintainer usefulness or learner mastery. Any false installation/execution/compatibility/merge claim or unrecoverable source basis blocks engineering adoption until repaired; no useful paired evidence remains inconclusive for the selected positive product proof. If presentation hides necessary premises or adds no demonstrated benefit over source inspection, repair presentation or reconsider adoption before expanding analysis mechanisms.

## 9. Completion, failure handling and handoff

Completion requires evidence for supported-scope semantic transfer, native versions/material basis, source-progress survival, normal product profile/CLI/report/source delivery, exact retained report recovery, fresh-process no-work reconstruction, product regression/boundaries, separately frozen actual product proof and task-review disposition. Record each claim at the strength its evidence earns. Partial coverage is allowed when explicit and useful; procedural success alone is not a useful result.

Stop and reconcile the owning decision when required evidence cannot fit, exact source association cannot be preserved, native method support is undefined, schema1 cannot faithfully retain the view, accounting hides prefix work, a method difference is material or retained evidence defeats the admitted generality. Preserve source/history/costs, diagnose the earliest sufficient owner and choose repair, explicit unsupported/partial, successor qualification or defer. Fix real demonstrated defects; do not mutate lower owners to turn a legitimate boundary into a pass. No frozen overwrite, silent cap increase, fallback credential, automatic new case/retry, target-code execution or target-repository mutation.

Allowed changes after Build activation: mapped product owners, their native tests, directly affected experimental adapters/tests/inventory, required evidence records and owner/navigation reconciliation. Excluded: unrelated CI/runtime semantic changes, wholesale historical rewrites, external dependencies/frameworks, broad all-family migration, default combined-profile cutover, model campaigns or untrusted checkpoint import. Publication is coherent validated increments on the authorized repository workflow; commits/pushes record actual proof, debt and limits.

Each implementation cycle records meaningful learning/engineering evolution and failures progressively, teaches the verified result proportionately, and preserves unassessed ownership honestly. `MEMORY.md` selects continuation; cycle records own dated progression; this plan remains position-neutral. A completed planning artifact is ready for review and subsequent Build activation, not evidence that the feature has shipped.

## 10. Handoff to combined evidence and runtime applicability design

After connected product qualification and task/adoption disposition, hand off to the parent's [combined evidence and runtime applicability design checkpoint](CALLER_SIGNATURE_NATIVE_ADOPTION_AND_QUALIFICATION_PLAN.md#16-combined-evidence-and-runtime-applicability-design-checkpoint) before optional syntax families or non-required case campaigns. That section alone owns the trigger, existing-evidence comparison, package-state/import/dispatch/exercise/behavior separation, required design outputs and follow-up proof boundary. A decision-critical gap may justify bringing forward planning through explicit scope reconciliation; this implementation plan does not silently absorb a combined default profile or runtime observer/runner. Preserve current source-only delivery and its finite shared budget while the appropriate owners decide whether any additional capability is justified. `MEMORY.md` selects actual activation; the handoff is not evidence of runtime implementation or permission to execute target code.
