# Investigator Run Control, Completion and Capability Diagnostic Plan

**Artifact status:** admitted planning baseline following Ali's October 18 agreement with the AUDIT-011 review and sequencing refinement. Publication admits the plan, not implementation, model loading or inference.

**Responsibility:** establish controlled, affordable experiment execution and determine whether a selected deployment can use supplied relevant evidence to produce a useful, calibrated interpretation before investing further in autonomous discovery.

**Live selection and exact continuation:** [MEMORY.md](../MEMORY.md) only.

## 1. Purpose, scope and controlling owners

UpgradePilot's full responsibility remains useful, provenance-backed dependency-update decision support for public Python maintainers. It needs to discover relevant evidence, distinguish observations from interpretation and missing premises, and support justified decisions or next work. This plan investigates one prerequisite: useful interpretation when relevant evidence is deliberately supplied. It does not redefine the product as a curated-packet renderer or establish autonomous discovery, stopping adequacy, maintainer usefulness, compatibility, action permission or generalization.

[AUDIT-011](../audits/2026-10-18_AUDIT-011_investigator-experiment-validity-and-progress.md), inspected at experiment revision `e0a6de39` and sharpened in `e16557e6`, identifies independent control, affordability, navigation and semantic failures. Its Qwen arithmetic is concrete: 43 of 48 operation units were spent before report generation; the actual Raw report required another 10 units including termination, while even a one-reference Structured report needed 6. Gemma's completed report independently contains unsupported advice. Fixing the ledger alone cannot establish useful interpretation.

| Owner | Consequence for this plan |
| --- | --- |
| [Charter](../PROJECT_CHARTER.md), [Core](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md) | Preserve product purpose, evidence/proposal separation, provenance, truthful failed/unknown outcomes and implementation-retention discipline. |
| [Product Decision Model](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md), [Maintainer Action Synthesis](../docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md) | A laboratory recommendation cannot grant action permission; procedural completion is not adequacy. |
| [Minimum Useful Generality](../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md) | Hand-selected source packets are disclosed diagnostic inputs, never an automated discovery method; no case-specific semantic rule or caller-provided answer enters the implementation. |
| [ADR-0012](../docs/architecture/ADR-0012-canonical-investigation-workspace-and-recovery-boundary.md), [ADR-0013](../docs/architecture/ADR-0013-versioned-native-reconstruction-and-workspace-checkpoint-storage.md) | Canonical Workspace owns material identity/validity and lifecycle records. Supported offline checkpoint reading is input recovery, not model replay or resume permission. |
| [Existing comparison plan](INVESTIGATOR_INTEGRATION_AND_COMPARATIVE_EVALUATION_PLAN.md), [three-deployment amendment](INVESTIGATOR_SEMANTIC_COMPARISON_THREE_DEPLOYMENT_AMENDMENT_2026-10-17.md) | Their frozen Raw/Structured matrix remains a distinct experiment. This new supplied-evidence protocol has its own inputs, admission, accounting and claim boundary. |
| [Report/usefulness plan](MAINTAINER_REPORT_PRESERVATION_AND_USEFULNESS_EVALUATION_PLAN.md) | Independent maintainer benefit remains separately evaluated; this plan neither requires nor authorizes reviewer contact. |
| [Security](../SECURITY.md), [Environment](../ENVIRONMENT.md), [Operating Guide](../OPERATING_GUIDE.md) | Existing local SDK/loopback safeguards, privacy, Learning-by-Doing, proportionality and evidence rules apply. |

Only experiment orchestration/control, its relevant tests and diagnostic preparation/review are prospective implementation scope. No product-source change is assumed. A genuine missing product seam returns to its owning responsibility before modification. No new dependency, framework, agent topology, storage system, API transport or product specification/ADR is selected here.

## 2. Three responsibilities and their dependency relationship

| Responsibility | Bounded output | Entry and exit |
| --- | --- | --- |
| **Run-control correctness** — AUDIT-011-F2/F3 | An explicit deadline/cancellation/interruption/usage/cleanup contract and its implementation proof | Resolve the control mechanism before dependent implementation; deterministic proof precedes any charged transport check or diagnostic. |
| **Completion affordability** — F1/F5 | First, a fixed report-only allowance sufficient for the diagnostic; later, a general adaptive terminal-reserve contract if discovery is selected | The diagnostic needs its own complete allowance. It does **not** require implementing the general discovery-reserve mechanism first. |
| **Capability localization** — F7/F8/F9/F11/F12 | One small frozen supplied-evidence diagnostic and source-backed disposition | Safe execution, packet/source integrity, fit, fixed-budget feasibility and applicable report-interface smoke must pass. Further discovery depends on the semantic result. |

The execution relationship is:

```text
run-control design and deterministic proof
    → fixed-packet composition and complete-budget feasibility
    → fresh pre-inference freeze and explicit batch activation
    → applicable bounded transport/report-interface checks
    → supplied-evidence diagnostic and offline review
    → interpretation adequate: decide on general adaptive affordability/discovery
    → interpretation inadequate: select interpretation/method/deployment diagnosis
    → control/delivery/review inconclusive: resolve that cause before judging capability
```

General adaptive citation pricing, broad navigation repair, native delivery redesign and history optimization are conditional responsibilities. Keeping them distinct prevents a small control repair from becoming a broad Investigator rewrite. They can share one future implementation increment only if their actual proof/ownership relationship justifies it explicitly.

The narrowing is temporary and diagnostic: supplying evidence removes discovery as a cause, so resources can answer a capability question earlier. It excludes proof of selecting sources, finding counterevidence independently, efficient exploration and autonomous stopping. Those capabilities re-enter when interpretation is sufficiently useful to justify testing them, or when a separately selected product question provides a concrete reason.

## 3. Run-control correctness

### Contract to establish

Use one monotonic elapsed-time basis for enforcement. Keep UTC timestamps for correlation/calendar evidence; file age and UTC differences cannot substitute for prediction elapsed time. Separate preparation, prediction, assignment and batch timers.

Before implementation, record the selected control mechanism and these observable states/relations without introducing a generic state-machine framework:

- request prepared and hash-bound;
- attempt conservatively reserved before dispatch; this is not proof the server accepted work;
- dispatch/stream observations actually available;
- complete response with trustworthy usage, known-usage failure/cancellation, or interrupted/unknown usage;
- cancellation requested versus server/runtime termination confirmed;
- report published versus complete unpublished attempt versus incomplete prefix;
- terminal publication confirmed, failed or unavailable;
- owned-runtime cleanup confirmed or unresolved.

An interruption must conservatively update the model ledger even when Python raises `KeyboardInterrupt` or another admitted `BaseException` path. Re-raise interruption after preserving state/cleanup; do not swallow it as an ordinary successful return. Unknown usage blocks subsequent prediction in that batch, and a model object cannot be reused with that uncertainty. Preserve actual known usage separately from budget reservations.

A hard deadline must work during both continuous fragments and silence. SDK inactivity timeout alone is insufficient. Cancellation needs a bounded drain/cleanup path and a result describing what was actually established. If cancellation cannot confirm runtime quiescence, stop rather than load another model or continue the batch. A late valid success can have known usage while still violating the declared elapsed bound; preserve both facts.

Persist a public-safe attempt/accounting trail sufficient to distinguish an orphan request from an unattempted case. Reuse request-based orphan discovery already present in the accounting approach. This is process-interruption accounting, not an exactly-once, power-loss or durable Workspace continuation promise. Never manufacture a canonical completed observation from a partial response.

Preserve the primary prediction/interruption failure separately from secondary receipt-write, cleanup or terminal-publication failure. A failing finalizer must not erase the only record of the original cause or turn an attempted prediction into an unattempted request.

### Mechanism decision before source modification

Start with the existing scoped SDK and explicit stream cancellation. Compare only the smallest credible ways to add total-deadline enforcement:

| Candidate | Required discrimination |
| --- | --- |
| Existing synchronous stream with a bounded cancellation/watchdog owner | Prove installed-SDK thread/channel ownership, cancellation during silence and continuous activity, and bounded cleanup; do not assume cross-thread calls are safe. |
| A contained prediction worker with parent deadline/cleanup ownership | Consider if the direct SDK path cannot provide bounded cancellation. Distinguish terminating the client worker from stopping server inference; preserve attempt/usage and owned-model cleanup. |

Select the simpler mechanism that establishes the complete contract. A transport switch or additional dependency requires a separate evidenced need; it is not a default fallback. Consult installed SDK source and current official documentation for unresolved SDK semantics. Freeze an inactivity timeout separately from the total elapsed deadline with a workload-based reason; do not choose an idle limit that predictably kills normal prompt processing.

**Selected WSL implementation:** use a temporary main-thread POSIX timer around the existing synchronous SDK channel, with monotonic checks and same-channel cancellation/drain. Refuse another timer owner or an unsupported thread/platform. This avoids SDK cross-thread ownership and a worker process. The diagnostic allocates up to 50 seconds of shared finalization per attempt (six × 50 = 300), then up to 50 seconds for owned unload and 10 seconds for SDK client release: the existing 360-second aggregate finalization ceiling is preserved. Real backend cancellation is still a separately activated first probe; installed-SDK/fake-channel proof alone cannot replace it.

**October19 receive-ownership repair:** the [first activated probe disposition](../working-memory/evidence/2026-10-19-investigator-successor-build/diagnostic-disposition.md) reproduces an SDK queue consumer abandoned by signal interruption. Ali explicitly directs fixing reasonable blockers and continuing, rather than stopping after diagnosis. Keep the same pinned SDK/channel/transport and POSIX deadline; own one pending queue-get future until endpoint processing acknowledges it. Reuse that future after interruption, defer Python control handlers only during the short local delivery/acknowledgment handoff, leaving all network and queue waits interruptible. Finalization uses its own absolute allowance rather than the prediction's short idle timeout. Retain allowlisted event-kind/receive-ownership counts without payloads. Prove actual asynchronous queue behavior, already-completed receive races, delayed/missing terminal, handled exit and bounded cleanup before runtime use.

This directed repair includes one freshly source-bound preparation/profile/fit/freeze and **one new six-attempt cohort** at the unchanged point, roles, order and per-cohort ceilings in §6, activated after offline prerequisites pass. Its cancellation probe is a new qualification of repaired code, not a retry inside the old failed cohort; the old one unknown-usage attempt and4,096/8,192 conservative token reservation remain explicit additional lineage cost. At most seven actual predictions across these two cohorts, including the old failed probe; no original-matrix slot is spent. Source/SDK/inputs/reviewer/assets/current ownership are revalidated. No semantic answer feedback, model/configuration change, output repair or selective semantic retry is included. Preserve every failed artifact; routine in-scope mechanical repair/proof need not request another permission. New unknown usage still withholds its affected batch; further inference beyond this finite increment is not automatic.

Non-prediction SDK RPC inactivity is 600 seconds within the total preparation/batch deadlines, permitting slow local load/render operations. Each prediction scopes its own inactivity allowance to its admitted prediction deadline and restores the prior RPC timeout afterward. In particular, the one-second cancellation probe cannot shorten later identity/render/tokenizer RPCs. These are distinct from the monotonic total deadlines.

The repaired prediction receiver is bounded directly by those monotonic prediction/finalization deadlines. It does not inherit the one-second SDK idle setting for a potentially longer cancellation drain; other SDK RPC timeout restoration remains required.

**October19 isolated control-proof amendment:** the repaired diagnostic-r2 actually receives terminal `success` with `stopReason: userStopped`, confirms the receive stopped/channel released and later owned unload/client cleanup, but the terminal stats expose no numeric token counts. It remains a failed unknown-usage cohort; all five later roles remain unattempted there. Do not relabel it passed under its original contract. Separate its observed control facts from the stronger accounting requirement for admitted report predictions. Repeating cancellation with arbitrary longer delays offers no demonstrated way to obtain missing counters and does not answer the capability question.

Use that completed, isolated probe as a **prospectively declared control prerequisite** for one fresh report-canary/four-case cohort. Bind its original artifacts, exact SDK, unchanged control and receive-adapter source, terminal cancellation, receive-stop/release and owned unload/client cleanup; retain its unknown4,096/8,192 reservation. No model object, client or failed batch is reused. The fresh point's canary must still provide complete numeric usage, exact prompt/configuration/instance correspondence and strict report/reference admission before the four cases. Unknown usage in any new report attempt stops that new batch unchanged. Cancellation accounting therefore establishes a conservative reserved bound, not exact actual consumption; the supported control claim is handled cancellation/terminal/owned cleanup, not complete cancelled-token telemetry.

The new cohort has at most **five attempts**,73,096 input tokens,40,960 generated tokens,322 admission units and310 finalization seconds; prediction/batch maxima stay4,200/4,800 seconds. The unused cancellation slot cannot be transferred. Across old diagnostic-r1, failed repaired diagnostic-r2 and the five new roles, at most seven actual attempts are admitted. Both old unknown reservations remain separate additional lineage cost. No semantic output has yet been observed or used to choose this amendment; model, full material cases, presentation and reviewer obligations remain fixed. Retain terminal metadata/complete returns before validating their usage so an incomplete counter payload is inspectable rather than discarded. Fresh source-bound preparation/profile/fit/freeze plus explicit matching activation remain required. Ali's directed reasonable-fix continuation authorizes this bounded repair/design; no further cancellation prediction is selected.

**Resource-constrained placement selection before semantic outputs:** runtime-r6 requested the inherited GPU ratio0.45 but actually loaded5 GPU layers rather than22 and correctly failed admission, with zero predictions and confirmed unload/client cleanup. After unload, Windows GPU telemetry showed about6,767/8,192MiB used,1,252MiB free and no llama backend; unrelated application ownership is not changed. Select the same model/assets/context/sampler/output with explicit GPU ratio0.10 and expected5 offloaded layers, under a new owned resource-point identifier. Raw ratio and observed layer count must both match; all other load/backend/template/cache/placement flags remain inherited. This is a new operating point with potentially slower prefill/generation, requiring fresh profile/complete fit and strict complete-usage report canary. It does not qualify latency at the old22-layer point. Keep cases/criteria/time/token/call ceilings unchanged; a timeout remains a failed/inconclusive result. The prior closed probe supports the unchanged cancellation protocol/receiver, not qualification of this new deployment's report behavior. This finite resource adaptation is within Ali's reasonable-fix continuation; no GPU sweep, inference retry or other application's resource change is admitted.

**Unactivated CPU-only candidate after the measured resource-canary failure:** diagnostic-r3's3269-token canary reaches its actual300-second allowance with11 prompt-progress events and no output; terminal metadata/cleanup are retained, numeric usage unknown, four cases unattempted. A separate Windows process holds about5314MiB of the8GiB GPU. The host meanwhile has about28GiB free RAM. The offline candidate proposes one CPU-only qualification at ratio0/0 GPU layers, same model/assets/context/output/sampler/template/cache and a new owned identifier, avoiding both adaptive offload and dependence on changing another application. Require actual raw ratio and backend zero-layer correspondence, fresh source-bound preparation/profile/complete fit and strict canary. Add the last wire-reported prompt-progress scalar to future receipts; old progress fractions stay unknown.

The fresh cohort remains one canary then four one-shot cases, at most5 attempts/73,096 input/40,960 generated/322 units/310 finalization seconds. Canary gets up to600 prediction/assignment seconds, cases up to900 each, fitting the unchanged4,200 prediction/4,800 batch ceiling. If this candidate is later selected, across the three retained unknown attempts and its fresh cohort, at most8 actual predictions are permitted; old12,288/24,576 reservations are additional conservative lineage cost. No semantic output has informed this CPU fallback; no case/criteria/material change, selective quality retry or model substitution follows. The completed unknown batch is not resumed. This is one finite alternative that removes the observed shared-GPU dependency, not a placement/time sweep. If CPU qualification also fails, preserve its result and require a material runtime/capacity change before further inference; reasonable offline repairs remain authorized. This candidate was prepared offline before Ali explicitly instructed waiting for his GPU-free signal. It has not been loaded, qualified or activated. That instruction withholds all model/LM Studio activity, including CPU-only runtime preparation, tokenization and prediction; no availability polling or automatic continuation is admitted. After his explicit signal, reconcile the appropriate operating point before fresh source-bound runtime preparation/freeze and activation. The sole live hold/continuation owner remains `MEMORY.md`; this paragraph preserves the candidate and its proof conditions.

**GPU-release continuation, declared before new inference:** Ali explicitly says “ok gpu is free now”, lifting the runtime hold. Fresh read-only telemetry reports6,414MiB free of8,192MiB and the local service has no loaded instances. Select one restored GPU point: ratio0.45, exactly22 observed GPU layers, context36,864, output8,192 and a fresh owned identifier. Keep inherited assets/sampler/tokenizer/template/cache, complete source selections, presentation and20 review obligations. Restore the original300-second report-canary limit; four cases retain900 seconds each. The CPU candidate remains unrun. This isolates a material resource change rather than extending timeouts or sweeping placement.

Admit one fresh source-bound preparation/runtime profile/complete fit/freeze and, after all prerequisites pass, one explicitly matching activation into a fresh five-role cohort (report canary, then packets a/b/c/d). The unchanged closed-control evidence remains an isolated prerequisite; no new cancellation prediction or old-batch reuse. Maximum5 new predictions/73,096 input/40,960 generated/322 admission units/310 finalization seconds, within4,200 prediction/4,800 batch seconds and1,200 preparation seconds. Across the three prior unknown attempts, maximum8 actual lineage predictions if all new roles execute; prior12,288/24,576 reservations remain additional conservative cost. Hard failure/unknown new usage withholds all later roles, without retry; no semantic output has informed this selection. Identity/fit mismatch withholds activation and receives its own disposition. Ali's GPU-free continuation, following the already authorized sequence and onboarding, authorizes this finite fresh cohort once its exact freeze is verified; it does not resume the interrupted matrix or adopt a product capability.

The implementation-entry record must name the chosen mechanism, timer origin, cancellation owner, drain bound, cleanup owner, terminal accounting, known limitations and focused tests. Unresolved claims about cancellation safety block that mechanism. No new real inference is needed to compare fake-clock/channel behavior.

### Focused proof

Use existing driver/model test homes and the actual adapter/orchestrator seams. Protect distinct behaviors, not a test-count quota:

1. Continuous visible/hidden-labelled activity past a fake monotonic deadline; hidden reasoning remains discarded.
2. Silence past the deadline; clock/file timestamp jumps do not affect enforcement.
3. Cancellation/late-success races, missing/invalid usage and delayed metadata; partial content never becomes a complete report.
4. Real `KeyboardInterrupt` and the explicitly supported exit/signal path; unknown usage cannot become zero or permit reuse.
5. Cleanup and terminal-publication failures, orphan requests and whole-batch withholding.
6. Unchanged successful reports, strict references, actual instance/configuration/token correspondence and owned-runtime isolation.

Run relevant narrow tests, then the existing experiment/seam and nearest Workspace controls justified by the actual diff. Product modifications would trigger separate product Build proof. A real transport check is admitted only by the later freeze and explicit inference activation, within §6; deterministic proof does not qualify installed runtime cancellation by itself.

## 4. Fixed supplied-evidence composition and affordability

### Reuse and experiment boundary

Reuse `InvestigatorAssignment`, actual `WorkspaceEvidenceAccess` source/native deliveries, request-local typed pairs, `pack_input`/measurement, the qualified SDK boundary, strict `publish_report` and lifecycle termination where they satisfy this responsibility. A thin experiment-owned report-only entry is the expected implementation shape; file layout is an execution hint, not architecture authority.

`run_scripted_trial` requires a fresh assignment and rejects existing events/notes/finish state. Do not weaken that guard to disguise primed evidence as autonomous investigation. Trusted diagnostic composition may deliberately prepare real deliveries, perform procedural finish and construct a report-phase request, with its own explicit setup/attempt/publication ledger. It must reuse the lower-layer authority checks rather than duplicate them or fabricate laboratory references.

The model makes one report attempt per diagnostic case. It chooses no discovery tool and does not demonstrate autonomous stopping. A report-phase empty tool menu means the diagnostic has supplied the frozen packet; it does not mean the whole source universe is exhausted. Native adequacy/evaluation `unsupported` remains visible. Accepted publication is attributed laboratory output, not semantic acceptance.

Attribute trusted setup requests to diagnostic preparation, not to the model. The existing presentation labels earlier model requests; the new presentation must truthfully identify its different producer without changing historical inputs or giving the model credit for scripted discovery.

Retain the complete existing report field family where adequate. Change the task/presentation identity to state the supplied-evidence, report-only responsibility. Do not introduce a new semantic evaluator merely to fit the diagnostic. Citation options must be exactly the real typed references in the delivered packet, with source scope and material validity preserved.

### Fixed allowance

The baseline allows **at most 13 trusted source/native setup reads and 16 distinct eligible evidence references per case**. No model-driven discovery, notes, search retries or correction calls are included. A native view may return several references; enforce both limits independently. Every retained/cited passage must cover the material proposition; fitting the allowance cannot justify dropping counterevidence or citing a partial record as complete.

Use existing conservative admission units, prospectively versioned for this report-only entry:

| Component | Maximum per diagnostic case |
| --- | ---: |
| Trusted setup reads | `13 × 4 = 52` units |
| Procedural finish | 3 units |
| One report publication with up to 16 distinct references | `4 + 16 = 20` units |
| Termination | 1 unit |
| **Complete allowance** | **76 units** |

**October 19 preparation correction:** the draft allowed 12 reads / 12 references / 68 units. Complete retained HTTPX preparation needs 12 source reads plus one native view returning four records: 13 reads / 16 references / 76 units. This preserves requirements/caller/callee/framework, both workflows, Dockerfile and both historical CI capture-limit records. The old cap refuses before dispatch; dropping this material would weaken the diagnostic. This prospective correction increases only fixed delivery/publication capacity, before any diagnostic output. Calls, tokens, time, case order and activation gates are unchanged; aggregate admission capacity becomes 340 units. The [Build cycle](../working-memory/2026-10-19_investigator-successor-build_lbd-cycle.md) preserves the counterexample and reconciliation.

The fixed packet cannot consume the report allowance. Enforce these bounds before its model call; no publication-cost surprise may be deferred until after generation. Initial host/purpose composition publications, model load/render/tokenizer work and preparation/review costs remain separately recorded, as in their actual existing accounting classes; the 76 units are not a claim to bound every physical operation or wall-clock cost.

The guarantee is available capacity for one **contract-valid** terminal attempt within its declared citation allowance. It does not guarantee model adherence, correct citations, useful content, successful storage or completion before the deadline. Honest unavailable/empty evidence never requires inventing a citation. Invalid or incomplete output stays rejected; no automatic repair or second attempt is included.

Native preparation can use the existing supported **65,536-byte native view capacity** when needed to include complete admitted records directly, rather than forcing the diagnostic through eight character-page predictions. This is an explicit supplied-packet policy, not a fix or claimed improvement to autonomous native navigation. Relevant existing families remain `investigation_inputs`, `ci_inputs`, `ci_coverage` and `runtime_dependency_state`; no family is added. Source reads remain bounded by the existing 100-line request contract. Freeze actual views/pages and references, not an assumed maximum shape.

### Offline feasibility gate

Before any prediction, a trusted scripted consumer must publish a structurally valid attributed report using the packet's **maximum admitted reference set** and then terminate within the exact allowance. That scripted content explicitly makes no semantic adequacy claim. Test one-below/exact boundary, attempted extra read/reference, missing evidence, invalid reference and publication failure.

Separately retain the actual Qwen 43-spent/5-remaining and glyphsLib 3+3+2 shapes as evidence of the **general adaptive** problem. Demonstrate that the fixed diagnostic composes a feasible terminal path; do not claim it repairs those autonomous routes. Full adaptive reserve proof belongs to §8.

## 5. Capability-localizing diagnostic

### Question and intended deployment

**Question:** given relevant, provenance-preserving evidence and an affordable report-only contract, can the selected deployment produce materially supported interpretation, specific uncertainty and useful next work without decision-critical false confidence?

The intended baseline is **Gemma 4 12B**, model key `google/gemma-4-12b`, at a newly declared **36,864-context / 8,192-generation** operating point. The retained reference-v2 32,768 profile remains the immutable parent for sampler, tokenizer, template, model/backend assets, cache placement and offload policy; its qualification does not qualify the new point. A fresh observed profile and complete fits must establish the new point before activation. The same model already has an observed complete real report and known semantic failures to diagnose at the older point. Its observed report cost was lower than Qwen's in different workloads; that supports a bounded cost choice, not a controlled speed ranking or intrinsic quality claim. E4B has no real semantic result in that matrix, and adding Qwen/E4B would change this diagnostic into another comparison.

The retained profile is an input identity to revalidate, not an instruction to assume the runtime unchanged:

```text
/home/motafeq/.local/share/upgradepilot/investigator-runs/semantic-comparison-2026-10-18-reference-v2/gemma12-preflight/profile.json
SHA256: 793bed85004fe1567c0d567155051e5887a893749e9c6d45c277e40065ff9531
```

Preserve that profile's template/tokenizer, load/placement, sampler, thinking mode and 8,192 output limit unless a new versioned decision explicitly changes the point. Resolve current runtime/assets/load identity at preflight. Missing/unqualified identity or unavailable deployment withholds the diagnostic; there is no implicit substitute, download, parameter sweep or extra arm. The old qualification applies to its old contract; §6 admits a small new report-only interface check, not silent inheritance or a repeat of every prior canary.

Keep the historical profile/receipts immutable. Derive a new source-bound deployment manifest that references their asset/configuration basis and records the actual new control/presentation code, identity checks and report-only qualification. Do not mutate an old source hash or weaken a verifier to make the historical admission cover the successor.

### Four fixed development cases

Use retained evidence already bound by the reference-v2 input qualification. The original private common root is `/home/motafeq/.local/share/upgradepilot/investigator-inputs/common-freeze-2026-10-16-2025`; revalidate the supported checkpoints/catalog identities and file inventories through the existing qualification path. No new source acquisition or target execution is included.

| Diagnostic case | Supplied evidence responsibility | Reviewer-only material obligations |
| --- | --- | --- |
| **HTTPX PR context** | Exact target/transition; base/proposed requirements; target TestClient use; retained old/new HTTPX Client signatures and old/new Starlette call context; relevant workflow and current/historical CI scope | Preserve the six original HTTPX obligations: transition, target consumer, API change, reference framework path, CI scope and actual runtime-binding/decision limit. A candidate mechanism plus a specific missing binding is useful; assumed installed Starlette or low-risk reassurance fails. |
| **glyphsLib PR context** | Exact pytest transition; CI workflow, tox and regression environment chain; retained historical CI results; actual native coverage/runtime outcomes and missing premises | Preserve the six original glyphsLib obligations: transition, main CI route, regression route, CI correlation, runtime uncertainty and stopping/next-work implication. A successful job observation is distinct from verified installed pytest. |
| **Captured consumer comparison, first source** | Complete relevant retained `starlette-old` class/constructor call and old/new HTTPX callee signatures, with exact source identities | Correctly identify the captured call's keyword/callee relationship and its scoped source-level consequence; preserve the distinction from the target's actual installed runtime and avoid claiming observed execution. |
| **Captured consumer comparison, second source** | The equivalent retained `starlette-new` class/constructor call, with the same old/new HTTPX callee evidence and task | Correctly distinguish whether the specific removal applies to this captured call. Do not promote a local non-applicability result into global compatibility/safety; do not leave a directly observable call fact generically unknown. |

The final two cases use real retained source to provide a source-level positive/negative contrast; they are not invented target installations or execution results. Their exact-head PR target identity is retained as provenance context, while the task explicitly limits its conclusion to the supplied reference consumer/callee pair. No captured reference version is rebound as the target's installed dependency. The pair is related to the exposed HTTPX case and is not two independent generalization samples.

Supply complete relevant signatures/calls and enough surrounding source to establish binding. Freeze exact line/character ranges, hashes, source revisions, scope and read receipts during preparation. Do not choose a two-line excerpt that hides keyword acceptance, inherited dispatch or material counterevidence. Native results remain existing attributed producer outputs, not new answers written by the reviewer. Historical HTTPX `manual_simulation`/`illustrative_non_binding` material stays at that explicit strength.

Case selection and excerpt preparation are manual diagnostic assistance. They remove discovery from the question; they are not a reusable retrieval algorithm. Do not feed source obligations, expected/forbidden conclusions, reviewer grades, prior model outputs or explanatory reviewer prose to the model. Actual sources and existing native evidence may reveal facts; that is the point of the diagnostic. A generic source-only task is allowed; an answer-bearing fixture label is not. Use neutral opaque case labels in model-facing metadata.

The baseline semantic order is HTTPX PR context → second/newer captured consumer → glyphsLib PR context → first/older captured consumer. Freeze that mapping/order before outputs; there is no claim of statistical order balance from this one cohort. Use a fresh host and per-case ledger with complete explicit requests. No earlier response or reviewer feedback enters a later model request. A single owned loaded model may serve these stateless requests if the installed binding establishes that boundary; record actual identity and caching limitations rather than claiming independent fresh-runtime samples.

### Model-facing task and evidence preservation

Use one common brief for the two PR packets: identify what changed, what the supplied consumer/upstream/CI evidence establishes, which material premises remain unresolved and what justified next work follows. Use one common brief for the two reference-consumer controls, scoped to the specific captured caller/callee relationship. Neither brief supplies a desired answer or claims evidence sufficiency.

Preserve all substantive report surfaces: claims, summary, conditions, recommendation, missing observations, unexamined material and stopping reason. Ask for a concise report, ordinarily at most 600 words; this is guidance, not permission to truncate a received output or discard material uncertainty. Full required packet content must reach the exact rendered request. No whole-event omission of required packet material is allowed; if it cannot fit, the case is not prepared, rather than silently becoming an easier task.

Prefer real canonical typed source/native references. Do not replace them with reviewer-authored summaries, notes as corroboration, fuzzy aliases or repaired IDs. The common packet/presentation policy and strict reference authority apply to every case. They do not create a Raw/Structured treatment comparison.

## 6. Prospective budget, freeze and inference admission

These are finite **plan ceilings**, chosen to make the diagnostic small enough to stop. They are not measured usage, permission to consume the ceiling, a latency promise or current execution authorization.

| Resource | Interface/control probes | Semantic diagnostic | Combined maximum |
| --- | ---: | ---: | ---: |
| Deployments | The same intended Gemma12 point | Same point | 1 |
| Prediction attempts | At most 2 | Exactly 4 planned, one per case | **6** |
| Fully rendered input per attempt | 4,096 tokens | HTTPX 24,000; newer consumer 9,000; glyphsLib 27,000; older consumer 9,000 | **77,192 input tokens** across the maximum attempts |
| Generation ceiling per attempt | Existing 8,192 tokens | Existing 8,192 tokens | **49,152 generated tokens** |
| Total prediction elapsed ceiling per attempt | 300 seconds | 900 seconds | **4,200 prediction seconds** |
| Cancel/drain/finalization allowance | At most 60 seconds per attempt | At most 60 seconds per attempt | **360 additional seconds** |
| Workspace admission units | At most 18 per probe | At most 76 per case | **340 units** |

For report-only probes, at most two setup reads/two references cost `8 + finish 3 + report 6 + termination 1 = 18`. A cancelled probe retains its real attempted charges and does not acquire a fictional publication. Diagnostic aggregate units are `4 × 76 = 304`; probes add at most 36. Counts refer to conservative admission units, not unobserved producer calls.

Zero-generation load/identity/render preparation has a separate **1,200-second elapsed preparation ceiling** and no prediction budget. The charged batch's total elapsed limit from its first attempt to final cleanup is at most **4,800 seconds**: 4,200 prediction seconds, 360 finalization seconds and 240 seconds of orchestration margin. Each attempt/finalization is also bounded above as shown; the margin cannot enlarge a prediction ceiling. Host/model preparation costs and reviewer effort are reported separately. If the declared preparation or fit is infeasible, stop for a versioned disposition rather than repeatedly loading/tuning until it passes. Full model-weight hashing need not be repeated where an inherited hash plus justified current checks suffices; never represent stat checks as a new full hash.

Context is 36,864, generation reserve8,192 and margin 256, leaving 28,416 input tokens. Every declared per-case ceiling is inside that envelope. Actual rendering/tokenization, schema size, required-packet completeness, fresh-host headroom and load/memory feasibility still require measurement. An input cannot borrow another role's unused allowance or spend spare context silently. Revise the contract before outcomes without dropping obligations, or withhold. Byte limits cannot stand in for actual token fit.

**October 19 capacity amendment, selected before any diagnostic prediction:** the original uniform16,000 /72,192 aggregate /32,768-context draft could not admit the complete inputs, including the lossless `/2` presentation. The [measured disposition](../working-memory/evidence/2026-10-19-investigator-successor-build/decoded-presentation-disposition.md) preserves that negative evidence. The selected successor adds 4,096 context and 5,000 aggregate input tokens, with fixed role reservations `24,000 +9,000 +27,000 +9,000 +2×4,096 =77,192`. Calls, model/assets, source obligations, output reserve, sampler, time and operation ceilings remain unchanged. The new context is a different operating point: preserve the old profile and declare a new request/identifier, permit only those two deltas in actual model/load/backend checks, then retain an actual observed profile. A cloned/edited old observation is not evidence of the new point. The [same Build cycle](../working-memory/2026-10-19_investigator-successor-build_lbd-cycle.md) owns execution/proof progression; this amendment does not activate inference.

The two non-semantic attempt slots have named purposes:

1. **One report-only reference canary** over independent synthetic material, exercising the exact new task/presentation/schema, every required report field, at least one currently visible eligible typed citation, and complete usage/configuration correspondence. No semantic-case answer is supplied. Failure withholds the diagnostic; no corrective retry.
2. **At most one cancellation/transport check**, only if the selected run-control mechanism needs real backend evidence beyond deterministic/installed-source proof. Declare whether it is needed and its expected cancellation/usage/cleanup outcome before the freeze. If needed, execute it first; uncertain usage or cleanup stops the batch. If not needed, mark the slot unused; it cannot be transferred to another case, retry or candidate.

Before any prediction, publish and verify a fresh, complete manifest binding:

- user activation scope; exact new protocol/source/response-parser identities and all prospective budgets;
- retained-input/current source hashes and every case's exact evidence payload/selection recipe, reference derivation policy, capture limits and required-content inventory;
- separate reviewer-only obligations, materiality/acceptance rules, reviewer identity/assistance and adjudication procedure;
- exact intended deployment/profile/runtime/template/tokenizer/load/prediction settings and requested/applied checks;
- actual zero-generation measured input/schema/context fit for every case and probe, including report phase;
- deterministic run-control, fixed-budget, strict reference and scripted publication proof;
- exact probe purposes and case order; needed admission receipts; no original freeze mutation;
- attempt/deadline/cancellation/usage/cleanup/failure policy and a fresh owner-only retention root outside Git and temporary directories;
- public-safe evidence paths and the explicit activation allowing this bounded batch after its prerequisites.

Pre-inference paths/identities/hashes must be real and resolved. No placeholder freeze, mock deployment or fabricated source reference may reach prediction. The plan itself may identify preparation work that is not yet performed; it cannot serve as the run manifest.

Zero-generation preflight retains the full exact packed/rendered inputs and measured token counts for every role before fit disposition, including an oversized request. It records the per-input cap separately from the context/generation/margin envelope. A failed role cannot be omitted from the denominator or repaired by whole-event deletion. Within the one admitted preparation, finish the independent measurements under its deadline, then withhold the executable freeze if any required fit fails. Further load/fit work needs a versioned disposition; no automatic cap increase or repeat-until-fit loop follows.

Separate frozen source identity from assignment-local identity. Source/catalog/record/payload and selection identities are concrete in the freeze. Fresh hosts mint their own delivery IDs and typed citation pairs; bind those actual mappings and exact rendered bytes in the pre-dispatch request record and validate them against the frozen source payloads and declared mapping policy. The authority-bearing request must contain only real IDs from that fresh assignment. A separate scripted feasibility assignment cannot donate its IDs or terminated mutable state. Any intentionally fresh host/revision metadata must be named and checked against its actual owner; no generic normalization may hide content/source/policy drift. Measure actual fit again before prediction, because fresh reference spelling can change token counts.

A changed control implementation does not automatically justify a full all-model canary campaign. This diagnostic's new report-only contract needs its own scoped canary and fit/identity proof. It does not qualify autonomous tools or allow the older failed/imperfect qualification outcomes to be rewritten. A larger verification need requires a new bounded decision before spending more calls.

### Complete-input presentation feasibility

The [October 19 complete-fit disposition](../working-memory/evidence/2026-10-19-investigator-successor-build/runtime-complete-fit-disposition.md) supplies a concrete counterexample to treating the original 16,000 cap as the sole preparation problem: HTTPX measured23,449 input tokens, while glyphsLib measured26,603 and exceeded the old 24,320 input envelope after reserving8,192 output and 256 margin. These are zero-generation observations, not capability results. The historical presentation-baseline sequence below explains why lossless simplification preceded the selected capacity amendment; old limits in that sequence do not override §6's amended resource table.

For a selected presentation-correction increment, preserve the product prerequisite—interpret all material supplied evidence—through this bounded sequence:

1. **Begin with the smallest reversible presentation baseline.** At the experiment model boundary, decode only the allowlisted `retained-source-view/1` and `workspace-native-view/1` delivery-content JSON strings into explicit structured values for presentation. Retain original canonical bytes separately. Do not recursively interpret arbitrary source strings, flatten meaning-bearing native variants, summarize evidence, omit an event, shorten a source range or replace typed references. The offline candidate in the disposition proves exact event-byte recovery and some byte savings; its token cost is unmeasured. This selects a first mechanism to investigate, not a claim that it will meet 16,000.
2. **Prove the boundary offline before another load.** Use the same common presentation policy for all six roles and a new presentation identity. Require byte-exact inverse reconstruction for supported deliveries; original request chronology, reference pairs, schemas, every native payload and capture/retention limitation must be preserved. Refuse unsupported/noncanonical forms explicitly rather than silently salvaging them. Keep the existing autonomous presentation unchanged. Reviewer prose must remain outside construction. Validate the model-boundary/report-only/runner/seam families justified by the diff. Preserve a fresh source-bound preparation without modifying prior roots.
3. **Declare one measurement preparation before invoking it.** A later selected verification may load only the unchanged intended Gemma point, within the existing 1,200-second ceiling, to retain all six complete rendered inputs, exact tokenizer counts and cleanup. No predictions or intermediate evidence removal. Measure a finite baseline/candidate set declared before loading; do not add candidates while observing fit. If preparation fails, retain every available measurement and terminate for disposition rather than start another load.
4. **Decide allowances from exact costs before outputs.** If every role fits the unchanged per-input/context/aggregate ceilings with justified fresh-host headroom, prepare a fresh freeze under those ceilings. If lossless presentation fits context but some roles still exceed 16,000, first evaluate a prospectively declared case-specific input allocation within the unchanged 72,192 aggregate. For example 23,000/9,000/23,000/9,000 plus two 4,096 probes is arithmetically possible; it is only an illustration and is not admitted without measured fits and headroom. No slot/capacity transfer after seeing semantic output. If no supported allocation fits, present a concrete versioned allowance decision with its resource/proof effects or withhold. Do not silently consume spare context or shrink output reserve.
5. **Stop when the evidence rejects the baseline.** An over-context candidate, inadequate headroom, failed integrity proof or infeasible aggregate withholds inference. A further representation mechanism, different context/model, smaller generation reserve, split case, removed obligation or larger aggregate is a separate consequential decision. Compare its effect on the capability question before changing the owner. No open-ended compaction/tuning loop follows.

This temporary increment improves delivery feasibility, not discovery or maintainer usefulness. It excludes metadata interning/deduplication machinery, upstream product codecs, navigation, model changes and semantic experimentation. Re-enter those responsibilities only with a concrete remaining-cost or product-evidence reason. The resource table above and current runtime admission remain unchanged until an explicit versioned decision changes them; this subsection is a bounded design/proof contract and does not itself activate another load or inference batch.

For the selected capacity successor, treat the larger context as a **new operating point** even when model/assets and sampler remain the same. Preserve the old profile, prepare a real new profile/load/backend/render identity, declare per-role and aggregate ceilings before output, and retain source-bound fit plus applicable probe/activation requirements. The [October 19 decoded-presentation disposition](../working-memory/evidence/2026-10-19-investigator-successor-build/decoded-presentation-disposition.md) preserves the original proposal/alternatives; the explicit capacity amendment above owns the selected contract. Freeze the actual observed profile's hash and use that profile for execution reload/validation. A changed or inherited point cannot bypass new fit, applicable probes or matching-freeze activation.

## 7. Semantic review, acceptance and branch consequences

### Freeze review obligations before output

Retain the original six material obligations for each PR packet. Each reference-consumer control has four required obligations: exact caller/callee identity, accurate scoped call/signature relationship, the justified consequence concerning that specific change, and the remaining runtime/whole-compatibility limit. Verify every obligation is answerable or supports a specific meaningful unresolved conclusion from its supplied packet; packet insufficiency is a preparation defect, not a way to fail the model after the fact.

Review the full original output and every decision-critical assertion across all report fields. Keep **supplied → actually delivered → cited → semantically supported** separate. A valid reference does not establish entailment. Preserve original/initial labels and source reasons before adjudication. No keyword matching, weighted winner score, report repair or runtime semantic judge is introduced.

The review is source-aware and AI-assisted unless a genuinely independent reviewer is explicitly engaged. Mask deployment/case outcome labels where feasible and disclose remaining leakage/prior exposure. Reviewer-only packets/labels never enter model inputs. Resolve material label disagreement against exact passages, supplied scope and frozen obligations; if a consequential disagreement remains, classify the decision as inconclusive. An AI-authored second pass cannot be called independent human acceptance. Reviewer contact remains outside this authorization.

### Per-case outcomes

Record execution/admission, comparability and semantic review as separate axes. A complete unpublished attempt can be source-reviewed when its actual input/output/identity is trustworthy; an operational publication failure does not erase its semantic strengths or failures. Such a run still cannot establish successful end-to-end completion. Missing/incomplete responses receive no semantic pass/fail verdict, and an identity/input-integrity failure can make even a complete response incomparable. The classifications below therefore need not be mutually exclusive for reviewable attempted content.

| Classification | Required condition | Meaning |
| --- | --- | --- |
| **Semantically adequate at this diagnostic scope** | Complete comparable report; all required material obligations supported or specifically justified unresolved; zero decision-critical unsupported/contradicted advice or authority promotion; material references/scopes usable; useful next work or scoped conclusion | Permits only the planned development-level capability inference. |
| **Semantically inadequate** | Complete comparable output has a decision-critical false premise, hides a material unresolved premise, misrepresents source availability, misses a required material relation despite its delivery, or gives generic unknown/abstention instead of observable supported findings | Target interpretation/method/deployment adequacy. Preserve correct statements too. |
| **Control/interface/delivery failure** | Deadline/cancellation/usage/identity/grammar/publication/input-delivery failure prevents a comparable complete result | No semantic competence verdict from missing output; retain any complete attempted content for attributed review separately. |
| **Review/input inconclusive** | Material packet ambiguity, source-integrity failure, incomparable conditions or unresolved reviewer disagreement | Resolve that bounded cause; do not invent acceptance or silently remove the case. |

Specific uncertainty can satisfy an obligation when the packet truly cannot establish its premise; blanket uncertainty does not satisfy directly observable facts. The two source-level controls must distinguish the captured call relationships. Neither a condition elsewhere nor `inferred` status cancels unsupported reassurance. Minor style differences do not become critical errors unless they impair a required finding/scope/traceability obligation.

### Cohort decision

Review only after the frozen case execution; do not feed interim semantic judgments back into prompts/order. With trustworthy usage and no hard control/identity/interface failure, complete the four separately executed one-shot cases even if a later offline review finds one semantically inadequate. This preserves their predeclared denominator without authorizing tuning. Hard failures/unknown usage stop remaining prediction, preserving unattempted cases.

- **All four adequate:** retain the bounded interpretation method as a development candidate. Decide explicitly whether the general adaptive completion contract and a small discovery pilot are worth implementing. This is not production adoption, reliability estimation, an intrinsic model ranking or maintainer-value acceptance.
- **Any comparable case semantically inadequate:** do not fund the next increment as autonomous-discovery optimization for this result. Select a bounded interpretation-method/deployment diagnosis or simpler evidence-preparation plus interpretation comparison. This is a development routing decision, not proof the model can never do the task. No automatic model substitution or rerun follows.
- **A hard control/delivery failure or consequential review/input uncertainty:** classify the cohort incomplete/inconclusive and identify the smallest discriminating follow-up. Do not score missing reports as semantic abstention or use a successful subset to declare a pass.

Cohort completeness and known semantic findings remain separate. A hard failure withholds cohort acceptance and further prediction, but does not erase a semantic defect already established in a comparable complete output. Preserve both in the next decision; do not use either one to manufacture a single-cause account or justify an automatic rerun.

Failure/inconclusive evidence is a valid delivered outcome. Closure requires its truthful disposition, actual cost/proof limits and the cycle's D/E learning/handoff; it does not require manufacturing a positive result. An unresolved proof gate remains unresolved, not renamed complete.

A separately authorized interpretation-method comparison may use the [evidence-first comparison plan](INVESTIGATOR_EVIDENCE_FIRST_INTERPRETATION_COMPARISON_PLAN.md). That contract preserves the completed diagnostic as historical evidence; it does not resume its frozen batch or automatically activate another model call.

## 8. Conditional general adaptive affordability and discovery

If a later decision selects autonomous discovery, first define the terminal product it must keep affordable and choose a mechanism prospectively. The **new experiment contract**, not the historical code/specification, must admit this invariant:

```text
before another discovery action is admitted:
remaining resources after that action
    ≥ declared completion allowance for finish + report + citations + termination
      + any admitted call/token/deadline reserve
```

Resource feasibility includes the action's possible reference/observation growth and a usable next report request, not just operation units. Time reserve is an opportunity under a deadline, not a guarantee of model latency/success. A failed/refused action cannot erase its spend; a new reference cannot silently overrun the intended citation allowance.

| Candidate | Reason to consider | Material cost/proof question |
| --- | --- | --- |
| Existing per-reference price with protected declared allowance | Small conceptual change; explicit report capacity | Define affordable evidence selection and what happens when material support needs more citations. |
| Fixed terminal package up to a declared citation maximum | Predictable terminal price | Price/report capacity must represent actual admitted work; a cap cannot silently erase necessary counterevidence. |
| Explicit intended-reference reservation | Reserves support selected for the intended claims | Selection/update timing, omissions and later counterevidence need a coherent procedure. |
| Reserve all eligible references | Simple conservative baseline | Inventories/repeated reads can freeze useful discovery prematurely; prove the lost capability is acceptable or choose a narrower method. |

No mechanism is selected here for general adaptive execution. The design must prove both meaningful discovery and affordable supported terminal work. Use actual Qwen Raw costs and the complete 3+3+2 native shape, changing reference counts, source/history omission, refusal and exact-boundary cases. Reject a design that passes by forcing no-citation reports, suppressing material findings or treating budget finish as adequate investigation.

Generic path guidance/recovery, compact native representation and reduced descriptor/history cost are separate hypotheses to select when useful. The audit already establishes real navigation failures; successful interpretation would make investing in their repair more discriminating. A small discovery pilot must distinguish discovery from interpretation and controller failures, using the same semantic obligations and a simpler supplied-evidence baseline. It needs a fresh finite protocol/budget, not unused slots from §6.

An unseen sample and independent source review remain necessary before broad generalization. Maintainer usefulness retains its own ordinary-review baseline and owner. This plan does not open another full model/treatment matrix automatically.

## 9. Execution, evidence retention and coordination

### Entry and modification sequence

Implementation entry points are [run control](../experiments/investigator_run_control.py), [model transport/accounting](../experiments/investigator_model_interface.py), [report-only composition](../experiments/investigator_supplied_evidence.py), [explicit real packet recipes](../experiments/investigator_supplied_evidence_packets.json), [offline preparation/retention](../experiments/prepare_investigator_supplied_evidence.py) and [gated runtime preparation/execution](../experiments/run_investigator_supplied_evidence.py). Their tests establish mechanical boundaries; dated evidence owns actual observations and MEMORY alone owns readiness/continuation.

1. Enter the selected Planning/Build responsibility under its normal Learning-by-Doing cycle. Reconcile live owners and source before acting; maintain one coherent cycle record per substantive responsibility.
2. Resolve the run-control mechanism and implement only its admitted scope after Build authorization. Complete focused/broader proof and preserve failures.
3. Prepare the report-only entry and actual supplied packets; prove strict attribution, full required delivery and the 76-unit fixed allowance offline. Do not implement general adaptive reserve/navigation merely to reach this gate.
4. Perform separately authorized zero-generation identity/render/fit preparation, complete and publish the new freeze and obtain explicit bounded inference activation.
5. Run the needed probes and then the frozen four-case diagnostic within §6; retain all attempts, failures, unattempted cases and actual usage.
6. Review and disposition under §7; teach from the evidenced result and repair/defer material ownership gaps. Select the next responsibility according to the result, without automatically performing it.

Planning completion does not authorize steps 2–5. A later explicit activation can cover the whole bounded sequence once prerequisites and limits are concrete; avoid repetitive confirmations for actions already included in that authorization. Material mechanism/scope/budget changes or failed gates require a new decision, not a hidden retry.

### Evidence and isolation

Use a fresh owner-only root under the existing `~/.local/share/upgradepilot/investigator-runs/` responsibility, with 0700 directories/0600 files. Never write into the completed reference-v2, predecessor or audit retention roots. Freeze exact path names before execution; retain packet bytes, producer receipts, canonical-to-laboratory reference mappings, requested/rendered/model-visible inputs, complete/rejected outputs, partial prefixes, usage/configuration/identity and monotonic event timings. Keep reviewer files inaccessible to model packet construction by explicit allowlisted inventory, not merely a prompt instruction.

Record the optional probe's unused/attempted status and every semantic case. Unknown usage stays unknown; reserve that attempt's declared upper bound for conservative budget accounting, clearly separate from measured spend. A new unknown-usage/cleanup-uncertain attempt withholds all later prediction in that batch. An older retained unknown does not become zero or authorize continuation of its old batch; a separately activated fresh protocol needs current runtime quiescence/ownership and its own ledger.

Public summaries contain safe identities, hashes, costs, observations, support judgments and limitations. Do not publish raw private receipts/credentials or hidden reasoning. Any resource samples are labelled sampled/whole-machine unless independent attribution exists. Report measured input/generation/draft fields and preparation/prediction/review timing separately; absent reasoning/draft breakdowns are unknown, not zero.

The [existing interrupted 12-assignment disposition](../working-memory/evidence/2026-10-18-investigator-reference-interface-v2/final-results.json) remains immutable development evidence. Do not resume its eight unattempted assignments with changed source/contract, combine old successes with new trials, or spend its unused allowance. Its original cycle's incomplete B and later D/E disposition are separate from this planning cycle and cannot be silently closed or advanced by new work.

### Mandatory stop conditions

Stop the affected responsibility at unresolved authority/material-identity conflict, unavailable required source/profile/SDK, insufficient complete packet fit, unproved cancellation/cleanup, exhausted stated budget, unknown new usage, protocol/source drift, unwanted prior runtime ownership, leakage of reviewer answers, invalid admission, or a consequential design outside the admitted boundary. Preserve enough evidence to localize the cause and identify the next bounded decision.

No target code/workflow execution or mutation, source reacquisition, paid/cloud calls, model downloads, implicit candidate substitutions, hidden-reasoning retention, selective quality retries, output salvage, validator weakening, framework/agent expansion or product adoption is included.

## 10. Planning completion and later proof boundaries

This plan is ready for review when the responsibility/ordering, fixed diagnostic budget, baseline deployment/cases, semantic gates, implementation-entry decisions, freeze/activation boundary and existing-owner coordination are explicit and mutually consistent. Link/arithmetic/source/owner checks validate the planning artifact; they do not establish runtime fit or behavior.

Execution readiness additionally requires the selected mechanism's proof, actual source-bound packet/identity/render measurements, successful applicable probe admission and explicit activation. No placeholder can be promoted by calling the plan complete.

Stable product semantics and accepted Workspace architecture are referenced, not redefined. A local experiment timer/report allowance does not require a new product specification or ADR by itself. If later work selects a durable cross-cutting method or changes product semantics, update that owner before implementation. `MEMORY.md` selects live work; this plan owns only its bounded responsibilities, sequence, ceilings and proof/stop contract.
