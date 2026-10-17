# Investigator deployment and model-interface qualification — LbD cycle

**Date/horizon:** October 16, 2026, Asia/Tehran; A0 from `main@4545d5f0` after a successful fast-forward pull.
**Responsibility:** qualify actual local deployment identities, bounded resource envelopes and the real model/request/tool/reference interface for the admitted Investigator comparison, or explicitly withhold an unqualified deployment.
**State at this handoff (October17):** A0/A1/A2 complete; B/Verification current. Complete six-candidate r6 results are retained; native-mode r7 is complete and current-runtime r8 is prepared/inspected/frozen. Scoped engineering checks are green; deployment dispositions remain configuration-specific. D/E pending; C continuous. This record is the single detailed owner for this successor cycle; [MEMORY](../MEMORY.md) alone owns live selection.
**Owners:** [integration plan](../plans/INVESTIGATOR_INTEGRATION_AND_COMPARATIVE_EVALUATION_PLAN.md), especially §4 measured deployment envelopes and §5 model-interface qualification; [environment](../ENVIRONMENT.md); [security](../SECURITY.md).
**Related cycle:** [adapter/mechanical cycle](2026-10-16_2045_investigator-adapter-and-mechanical-qualification_lbd-cycle.md), now CLOSED through E after the [closure handoff](2026-10-16_2301_adapter-d-e-closure-handoff.md) and [reconciliation decision](2026-10-16_adapter-closure-and-deployment-cohort-reconciliation.md). Its model-free proof remains bounded; actual model/reference visibility belongs here.
**Procedural provenance:** `UP-SKILL:upgradepilot-build-implement`; `UP-SKILL:upgradepilot-learning-by-doing`; `UP-SKILL:upgradepilot-working-memory`.
**Entry evidence:** [read-only inventory, availability and code correspondence](evidence/2026-10-16-investigator-deployment-entry/entry.json). No model output is contained or implied.

## Phase status

| Phase | Status | Evidence / responsibility |
| --- | --- | --- |
| A0 | DONE | Pulled the explicit parallel handoff, reconciled canonical owners, checked unchanged bridge/input identities and the smallest local runtime facts; initialized this record/map. |
| A1 | DONE — continuous-context compression | Only pulled delta is Ali's already-explained scheduling decision; prior B/proof is unchanged. New runtime/session facts are included in the A2 packet; no mastery inferred. |
| A2 | DONE — Ali explicitly directed scoped B | Explain actual deployment versus asset availability, request/history visibility, measured context/offload, bounded canaries, model selection and withheld-versus-qualified outcomes. |
| B | CURRENT — bounded cohorts progressing | Complete stateless request/result bridge, streaming/privacy/default/mode/KV guards delivered. R6 completed all six; r7 native-mode cohort complete, r8 current2.60.0 binding for remaining three prepared/frozen under explicit budget revision. |
| Verification gate | CURRENT — engineering green, configuration-specific results | Final35 focused/65 nearest product controls, prior four model-free regressions, current source/import/record checks pass. R6:108 calls, Gemma12/Qwen27 each4/4 at2.59.0; other four withheld overall. R7 complete59 calls: E4B4/4,E2B2/4,MiMo2/4; r8 prepared/frozen current2.60.0 points; no silent transfer of old passes or semantic case admission. |
| D | PENDING | Learn from actual runtime/interface evidence and compare expectations; do not duplicate the adapter's parallel learning. |
| E | PENDING | Repair/defer material gaps and close this responsibility truthfully before selecting semantic comparison. |
| C | CONTINUOUS | Preserve configuration/protocol decisions, trials/costs/failures, corrections, proof limits and parallel feedback in this same record. |

## A0 reconciliation and learning/cadence adaptations

The pulled commit adds only the 41-line non-owning parallel handoff. The adapter cycle and MEMORY still selected D/E before a successor; reconcile that stale scheduling state now. Fresh checks match all 17 retained snapshot artifact sizes/hashes and all four adapter/driver/qualifier/test hashes in the previous verification packet. Prior 13 new controls, 65 nearest product tests and four mechanical scripts are inherited proof at their recorded horizon, not rerun here. The October 3 untracked audit remains untouched.

At the historical entry, Ali selected the successor while adapter D/E proceeded elsewhere. **Historical scheduling adaptation:** normal route closed the prior cycle through E before another cycle; waiting would have impeded his explicit parallel allocation despite green mechanical proof. The distinct runtime/interface responsibility began with parent D/E separately owned; that scheduling horizon is now superseded by the canonical parent closure reconciled at B entry. Any parallel finding invalidating mechanical fidelity, fairness, references/packing or this entry basis blocks affected qualification/inference until reconciled. No prior learning is declared complete and no messages are sent to the parallel session.

**A1 cadence adaptation:** this is continuous shared context after B, and the only Git delta is Ali's own scheduling instruction. He previously explicitly requested progression past a redundant A1 stop. Compress the repeated continuity explanation and separate A1 stop into the A0/A2 packet instead of repeating the same onboarding; preserve A1 content, record new facts, and retain the pre-B opportunity for the genuinely new deployment responsibility. This changes cadence, not proof or authorization, and claims no learner mastery.

Read-only native inventory at `127.0.0.1:18080/api/v1/models` still reports 22 entries. Both core keys and the four smaller candidates are registered, with no loaded instances for these entries. Qwen's actual file is present at 16,464,440,224 bytes; its full hash correspondence is inherited from the earlier asset verification, not rehashed at A0. A second Gemma 12B QAT registry entry exists; it must not be conflated with the planned `google/gemma-4-12b`. Registry size/architecture labels are not exact GGUF/runtime qualification. The initial SDK check inspected only the main interpreter's default path; the broader availability conclusion was incomplete and is corrected below. No dependency, load/configuration or inference was initiated.

Source confirms the two key unfinished interface requirements. The main scripted driver deliberately sets model usage unavailable and has no model transport. Its `visible.update(packed.reference_ids)` accumulates laboratory visibility across script calls, while whole-event packing can omit an earlier source event. The pinned research provider uses an injected SDK model/chat factory and explicitly discloses an estimated template allowance. Its existing isolated SDK is available, but that alone does not supply exact new-deployment/token/template proof. Neither fact proves a broken mechanical script or a qualified real-model session.

## Living A-phase map and A2 responsibility model

- **Continuity bridge:** retained source/native material and verified product-host adapter → actual local wire/template/tokenizer/history behavior → independent interface canaries. Earlier test health is not model readiness; asset identity is not loaded-deployment fit.
- **Proposed request/session route:** prefer explicit complete stateless requests if the installed interface supports the required rendering/measurement. Then references must be backed by evidence actually included in the relevant request; old script visibility cannot stand in for an omitted source passage. A genuinely retained session is an alternative only if its actual history/context/truncation behavior is measured and accounted. Choose and version the reference/session/packing rule before calls; do not attach a transport to the scripted cumulative set blindly. This is a proposed direction, not an implemented protocol revision or a product semantic change.
- **Concrete flow:** selected local GGUF bytes/hash → actual installed runtime/backend/template/reasoning configuration → fully rendered system/task/tool/history/final-schema token measurement → context/output/headroom admission and measured weight/cache placement → one bounded request → exact response/usage/stop/error record → strict tool/proposal/reference mapping through the existing host → qualify both treatments or withhold the deployment's pairs.
- **Actual fit:** model context includes input plus generated tokens; reasoning consumes the applicable output reserve. Weight offload and KV-cache placement are separate. Choose context from measured input plus the declared output reserve and justified margin; the inherited 32768 is provisional. Smaller models may use high/full offload only with measured headroom; large models use partial offload on the supported GPU. A larger allocation is not automatically faster or more complete.
- **Expected result:** exact resolved deployment manifests and a supported measured operating point, plus canary evidence distinguishing follow-up/tool/reference behavior from model-format/failure/fit problems. No global optimum, semantic superiority or maintainer benefit follows. A failed/unsupported deployment is withheld with its costs/reasons, never silently replaced or salvaged.
- **Scope/non-goals:** experiment-owned qualification only; no paired development-case outcomes, product-source mutation, older planner fixture repair, protected oracle access, new framework/cloud provider, target execution or acquisition. Adapter D/E closure is reconciled; its narrow unassessed learning gap remains explicitly deferred. A material needed product/authority change returns to its owner before action.

## Minimal todo and predictions

- [x] Reconcile the parallel handoff, prior green mechanical entry and actual read-only availability; initialize this cycle.
- [x] Finish A2/pre-B understanding: Ali explicitly directed B and its stateless/SDK/configuration/visibility boundaries.
- [x] Freeze the qualification cohort before inference in [r3](evidence/2026-10-17-investigator-model-interface/canary-freeze-r3.json): two core deployments, eight independent canary sequences, 48 maximum calls; all six candidates remain available. The recorded core remains Gemma 4 12B + Qwen3.8-27B; four smaller candidates are not silently extra arms. This is the historical r3 horizon, superseded by later explicit qualification revisions. Extra qualification configurations require their own freeze/budget; only additional selected semantic-comparison deployments would add four actual case assignments each. The later comparison remains two deployments/eight assignments.
- [x] Resolve exact local GGUF parts/full hashes, actual runtime/backend/templates/tokenizer policy, reasoning/placement and existing isolated SDK transport for the observed profiles. R6 qualified/withheld all six; new2.60.0 operating points are separately prepared/frozen before their calls. Unknown upstream correspondence, unexposed native token IDs/parser defaults and flash-auto kernel limits stay explicit.
- [x] Implement/test and exercise the bounded real request/usage/session-visibility bridge, including post-interruption visible-fragment retention, complete intent/result history and declared native mode/sampler support. Freeze exact wire/parser/prompt/tools/reference/packing/manifest definitions and capacity rules before inference; no placeholder-bearing manifest is runnable.
- [x] Measure representative fully rendered short/near-envelope/late/final requests for all r6/r7 profiles (repeat for r8 before its calls); choose justified context/offload/cache settings and record observed speed, memory, complete visible output and failures. Distinguish input overflow, generation exhaustion, timeout, memory failure, malformed/empty output and substantive incompleteness before changing settings. Retain failed configurations/costs.
- [ ] Finish configuration-specific qualification/dispositions on current runtime: r6 all24 sequences complete, r7 native12 complete, r8 remaining-three12 prepared/inspected/frozen. Exact prior spend/configuration/order is frozen before each affected cohort; global ceiling363, with older immutable cohort bounds retained. No automatic sweep or later eight-case activation.
- [ ] Record qualified/withheld dispositions, compare A2 predictions with evidence, complete this cycle's D/E and select a successor only from actual results.

**Prediction:** actual template/token/history correspondence and complete structured responses are more uncertain than source delivery. Memory pressure may require different per-model operating points, so comparisons remain deployment-specific with one frozen envelope per treatment pair. Existing host/access APIs should remain sufficient; no generic infrastructure restart is justified. Actual model output may require a bounded configuration/interface repair or withholding; good canaries still do not establish correct dependency reasoning.

**Historical entry handoff (superseded by B activation):** A2/pre-B gate was open. The cohort and request/session rule must be made explicit, and actual identities/configuration must be resolved before qualification inference. No model has been loaded or called by this cycle entry.

**Entry validation:** four Markdown documents, 46 local links/eight anchors, fences/newlines, whitespace and parallel-owner/successor phase consistency pass; the entry JSON parses. All nine governance checks ran: eight pass, with only inherited `examples/` owner-marker debt. No executable source/tests or accepted technical owners changed; no runtime tests, full weight rehash, load or inference was repeated for this entry. The unrelated October 3 audit is preserved.

## A2 correction — existing isolated SDK recovered

Ali challenged the claim that the SDK was unavailable because nothing had changed. The original check correctly found no SDK on the default `.venv` path, but failed to trace the actual historical invocation. October 5's main cycle explicitly installed SDK 1.5.0 and dependencies only under ignored `.tmp/api-eval-sdk`, leaving `.venv`/project declarations unchanged. Its reproduction uses `--sdk-site`; the separate research record explicitly reused that main-owned optional SDK, and `broader_agency_pilot.py` appends the supplied site before importing it. This is environment-selection/invocation context, not evidence of a changed or broken installation.

Read-only verification now confirms the site directory and distribution still exist and project Python imports `lmstudio` 1.5.0 from that exact path after `sys.path.append`. `Client` and `Chat.from_history` entry points resolve; no client was constructed and no network/load/inference/install/configuration action occurred. ENVIRONMENT now records the previously omitted reusable route; entry evidence distinguishes default-path absence from isolated availability. Retract the inference that a new SDK installation/provider replacement is required. The next reuse baseline is the existing SDK with explicit site selection; new-deployment identity/template/token/session/resource qualification remains pending. No environment change since the historical runs was established; A2 was current at this correction, before the explicit B instruction below.

Correction validation: SDK import/version/path checks pass; three touched Markdown owners have 35 resolving local links/five anchors and valid fences/newlines; evidence JSON, unchanged A2-current/B-pending state and `git diff --check` pass. No executable/dependency changes or runtime model tests; the unrelated October 3 audit remains excluded.

## B activation — canonical closure and candidate reconciliation

Ali explicitly directed B after the SDK correction and requested canonical closure first. Fast-forwarded main to `65ac1783`; the two incoming records affect no executable source. Parent adapter cycle is now CLOSED through E with named deferrals, not open parallel learning. A2 is complete for this bounded responsibility; no inferred mastery. All six candidates remain available: Gemma 4 12B, Qwen3.8-27B UD-Q4_K_M, Gemma 4 E2B, Gemma 4 E4B, MiMo-V2.6-Distill-Qwen-9B and Qwen3.5-9B. Candidate availability does not expand the two-deployment/eight-case-assignment comparison baseline. Before affected inference, explicitly freeze measured count, assignment IDs/order, budgets and any protocol revision; no silent additional arms/substitution.

Use complete explicit stateless requests through the existing isolated SDK site. Resolve exact assets, runtime/backend/template/tokenizer/reasoning/context/weight/KV placement and requested-versus-applied settings. Test real transport/usage and request-local report-reference eligibility; inspect fully rendered request/reference visibility before any bounded canary batch. Persistent history needs measured justification. Later paired semantic comparison remains unactivated.

## B — October 16–17 implementation and preflight progression

The real transport remains experiment-owned, with explicit complete stateless requests and current-request-only reference admission. The existing SDK is reused; its high-level configuration reader drops newer raw server fields and its public prediction config lacks the reasoning toggle. A small pinned SDK RPC/channel binding retains actual full configuration/template and raw scalar success metadata; it filters reasoning fragments before retention and refuses unsupported shapes. No project dependency or product source changed. The [qualification guide](../experiments/INVESTIGATOR_MODEL_INTERFACE_QUALIFICATION.md) owns executable flow and reproduction.

Actual preparation found a load-versus-prediction schema difference: the loaded template omitted required prediction `stopStrings`. The first Gemma preparation failed without inference and is retained. The corrected prediction explicitly freezes no extra stop strings; original load metadata is unchanged. Gemma's 12 rendered shapes measure 1,817–22,466 tokens; Qwen's 12 measure 1,706–22,293. With 8,192 generated tokens and 256 margin the worst totals 30,914, justifying 32,768 for this declared envelope rather than claiming a global optimum. Large models use partial weights: Gemma 45% requested, actual backend flag 22 layers; Qwen 20%, 13 layers. Both expose CPU KV, q8_0 K/V, logical batch 256, physical 1120 and four slots. Flash attention is requested/reported true but backend flag is `auto`; no independently measured kernel-selection claim. App 0.4.26+4 and running CUDA llama.cpp 2.59.0/b11669 are resolved.

Full hashing resolves Gemma weight (7,381,384,864 bytes) and projector (175,115,296 bytes), explaining its 7,556,574,286-byte package registry value. Qwen's full hash matches prior Unsloth correspondence. Tokenizer metadata and actual rendered token-ID identities are retained. Two final preparation profiles refresh source correspondence before any batch freeze. Four smaller candidates remain available without measured-arm expansion.

Ali explicitly required durable retention. All consequential preparation scripts/metadata, failure records, assets index and an exact copy of the original isolated SDK are preserved under `/home/motafeq/.local/share/upgradepilot/investigator-runs/deployment-interface-2026-10-16-r1` with owner-only access; new commands use that preserved SDK through `--sdk-site`. Original scratch artifacts were moved into that root. The prior `/tmp` Ruff tool was absent on continuation; its identical pinned 0.17.1 wheel and isolated verification install are now durable outside project dependencies, with provenance/hash retained.

A process command-line inspection unexpectedly exposed an internal ephemeral backend API token in tool output. It was never used or copied into artifacts; the owned initial instance was unloaded to retire it. Subsequent inspection emits only an allowlist and copies only the generated template. This correction changes no public LM Studio exposure/authentication.

Focused proof: 24 experiment controls pass (13 prior + 11 new), 65 nearest product tests pass, touched Ruff/format and 96-file product import direction pass. Current mechanical regression and final preflight are preserved separately. No inference/semantic comparison has run at this pre-batch horizon. B/Verification remain current/pending; actual canary usage/configuration correspondence and resource behavior are still required.

**Pre-inference freeze:** final profiles bind the exact final code and twelve inspected fully rendered shapes per deployment. Final maxima are Gemma 22,460 and Qwen 22,280; observed small differences from earlier profiles arise from fresh lifecycle identifiers and stay inside the explicit margin. [r3](evidence/2026-10-17-investigator-model-interface/canary-freeze-r3.json) freezes two core deployments and ordered eight canary sequences, six calls each/48 maximum, no additional arm or free sweep. r1 is preserved unexecuted; r2 only completes available repository/runtime/SDK provenance before any call. The [evidence README](evidence/2026-10-17-investigator-model-interface/README.md) records durable paths, exact proof and limits. Current mechanical regression passes four retained-input assignments with zero model calls and unchanged input/product identities. No source changes after final preflight; actual bounded canary evidence is next within B.

**Final pre-call identity check:** source review found that a registry alias and matching raw load configuration alone would not detect a changed underlying GGUF or adjusted backend placement. Added/tested the explicit fresh-load backend/model/template/cache/weight-path check before every deployment's first call. r3 supersedes unexecuted r1/r2 before any inference. Profile snapshots prove that all preparation/render/tokenization/canary-fixture functions remain unchanged; only the execution guard changed, so no repeated preparation load or inherited model outcome is used. Final proof is 24 experiment controls (13 prior + 11 new); the frozen execution code is durably snapshotted.

## First actual canary disposition and bounded correction

The published r3 batch attempted five predictions: Gemma raw/short one, Qwen structured/short four. Both configurations are withheld and all six remaining sequences were withheld before a call. Gemma reported 1818 input versus 1817 rendered tokens; the driver stopped before adapter dispatch. Its visible original was fenced JSON with a source-prefix path and remains rejected. Qwen input accounting matched exactly for all four calls; visible output included prose `Validating JSON syntax`, one valid source read and repeated `Valid`, exhausting the correction allowance. Actual target usage totals 10,676 input/72 generated tokens; Qwen additionally reports 36 draft tokens. No later case/semantic comparison ran and no hidden reasoning text was retained.

Diagnosis verified actual newline delimiters (not literal escaped newlines), explicit reasoning-off and real EOS endings; no overflow/generation exhaustion/memory-failure diagnosis is supported. Gemma GGUF explicitly sets automatic BOS insertion; its actual token spelling/id are recovered from the already-hashed file and checked with the live tokenizer. Represent that tokenizer prelude in full measurement, not a one-token fudge. Runtime grammar derives from the actual offered tool schemas or final report schema, applied identically to both treatments and original outputs never repaired. Qwen raw load already froze `draftMtp=true`; initial inspection underemphasized it, but it was not absent from the record. Draft generation is measured additional runtime work, not an extra selected deployment or demonstrated cause.

**Proportional adaptation:** five initial calls spent → blindly repeating eight six-call sequences would exceed the original 48-call ceiling → retain the plan's actual gate responsibilities in five-call sequences, omitting separate model note/read-back steps already mechanically covered → 40 new calls plus five prior = at most45, with two deployments/eight qualification assignments and unchanged later eight case assignments → defer only explicit real-model note/read-back coverage, retain complete positive/zero/empty/problem/reference/report/stop gate → reconcile plan, exact schema/BOS policy/code/profiles/order/budgets before further inference. This is independent interface/configuration qualification, not case-output tuning or semantic acceptance. Failed originals stay immutable; no automatic additional sweep is admitted.

The revised source passes 26 experiment controls, including actual-BOS identity/no-duplication, stage-appropriate grammar/arm restriction and spent-budget carryover. Actual live-tokenizer BOS confirmation and revised fully rendered preflight are pending; B/Verification remain current/pending.

**Revised preflight/freeze ready:** actual GGUF token spelling resolves Gemma BOS `<bos>`/id2 and verifies its one-token live-tokenizer identity; Qwen input requires no automatic BOS. Exact runtime grammar is generated from the menu/report already shown to the model. Clarified synthetic paths as explicit source_id/path arguments instead of shorthand; this is an input-interface correction, not a model-internals diagnosis. Final r4 profiles measure twelve shapes each: Gemma1823–22476, Qwen1709–22295; largest +8192+256=30924 within32768. [r4](evidence/2026-10-17-investigator-model-interface/canary-freeze-r4.json) binds exact code/config/schema/BOS/profile identities before any further call:40 new maximum+5 spent=45 below48, same two deployments/eight qualification assignments, no semantic runs. Earlier two r4 preparation profiles remain retained before the clarified final profiles.

**r4 live checkpoint:** Gemma raw/short returned four complete constrained responses with exact1823/2514/2872/2391 prompt counts and788 generated tokens. It read positive source, searched scoped zero, then finished before the required empty-file read and produced an admissible cited report. Trial `completed` is therefore correctly **withheld**, not interface-qualified; all remaining Gemma canaries are withheld before calls. The fixed BOS/grammar mechanisms worked; procedural completion/citation validity did not establish the required behavior. Qwen structured/short has completed positive/zero/empty/finish with exact measured counts and is generating its report under the frozen bound; no final qualification or later semantic comparison is inferred.

## Interrupted-run reconciliation, retention repair and final handoff

After the conversation/tool interruption, no qualifier/sampler process remained and native inventory reported both core models unloaded. The original runner had saved per-assignment results but had not published its final batch summary. Preserve those originals and create a separately named [reconciled interrupted-run summary](evidence/2026-10-17-investigator-model-interface/reconciled-interrupted-r4.json), never a fabricated normal-completion file. No inference was restarted.

Actual r4 results: Gemma raw/short withheld despite a valid cited report because empty-file read was skipped; its other three sequences withheld before a call. Qwen structured/short qualified all positive/zero/empty/finish/report/reference requirements in five calls. Its raw/short performed the tool sequence but call5 report terminated after166.38 client seconds with no final usage receipt. Cause is not established; do not call it model semantic failure, generation exhaustion or timeout. The two long Qwen sequences were withheld. Qwen's completed structured report used1411 target-generated tokens; native timing reports657.84s and client timing603.08s. These clocks are not reconciled; no precise latency ranking follows.

Total r3+r4 cost is19 attempts of the original48 ceiling. Reported known totals are44,124 input/2,443 target-generated plus1,551 additional draft tokens. One terminated call's generated/actual-input usage is unknown. Reasoning counts are unreported, not zero. Sampled machine peaks across preparation/idles/canaries are5466MiB GPU and minimum22,237,892KiB host free out of66,826,744KiB; no observed memory-exhaustion diagnosis, and actual near-envelope inference remains unestablished. Public [actual results](evidence/2026-10-17-investigator-model-interface/actual-results.json) retain raw scalar timing/cost fields and scope.

The interruption exposed a real retention gap: prior SDK binding accumulated fragments until success, so the interrupted report prefix is unavailable. Do not invent/recover it from unrelated output or promote a partial response. Corrected source persists each visible fragment unbuffered before SDK accumulation, filters reasoning first, fsyncs handled exits, records fragment hash/bytes and complete-versus-partial state, and still withholds unknown-usage failures without retry. A new discriminating test emits visible prefix+hidden fragment then interrupts: visible prefix survives, hidden text is absent, no complete response is fabricated and further calls refuse. This is controlled failure-path proof, not a new real-model qualification. Old r4 freeze rejects the changed source before client/load/prediction.

Final [verification](evidence/2026-10-17-investigator-model-interface/verification.json):27 focused controls PASS;65 nearest product tests PASS(20.496s); four final offline actual-retained-case scripts PASS with zero model calls, unchanged17 input and96 product-source hashes; import direction, touched Ruff/format and owner link/JSON/whitespace checks pass. Full product, installed and hosted suites were not rerun. The unrelated October3 audit remains excluded.

**Cycle frontier:** B's transport/mechanical and retention repair are delivered; runtime qualification remains WITHHELD and the cycle is not closed or advanced to D/E as successful model qualification. All six candidates remain available, only two core deployments were measured, and the later two-case/two-treatment/two-deployment eight assignments remain unstarted. Re-entry requires an explicit current-code/profile/protocol/count/order/budget freeze that preserves all19 attempts and interruption/behavior dispositions; no failure-selective replay or free sweep. Decide that bounded re-entry before later semantic comparison. The prior adapter cycle remains CLOSED through E; planner fixture and independent usefulness responsibilities remain separately deferred/unestablished.

## Explicit continuation and six-candidate qualification re-entry

Ali challenged the ambiguous handoff, established that only two candidates had run, and
explicitly authorized continued work through recoverable failures. Fetch finds main equal
to origin/main at507c77dc; no new parallel changes. Continue this same cycle at B/Verification,
not a new cycle or repeated A gate. The preceding explanations plus explicit continuation
provide the scope/understanding opportunity; learner ownership is not inferred.

UP-SKILL:upgradepilot-planning-design composes with the already active Build/LbD/memory
procedures for the material cohort/budget revision. The plan now admits six qualification
deployments/24 sequences/144 maximum new calls,19 earlier attempts retained/163 aggregate
ceiling. Later semantic design stays two deployments/eight case assignments, unactivated.
All six receive the same clarified task and2048 synthetic-only output ceiling (earlier
complete Qwen1411 tokens); original case reserve stays8192. Context32768 is retained for
the original declared envelope, not called optimal. Small candidates request full weight
offload with CPU q8_0 KV; actual fit/headroom must be inspected.

Material adaptation: behavioral early-withhold prevented observing independent remaining
sequences -> normal route stopped a deployment after its first failure -> Ali requests
actual candidate views and sustained diagnosis -> execute every independent frozen
sequence, preserving each failure and requiring all four to qualify -> more explicitly
budgeted diagnostic evidence, unchanged comparison gates -> reconcile plan,freeze,results
and MEMORY before claims. A load/identity error still withholds its deployment. No hidden
retry, forced tool choice, output repair or case scoring.

Source inspection found that the old five-call sequence had no room for its advertised
correction, and the assessor counted a refused request against the required exact action
sequence. Neither explains Gemma's no-correction skipped empty read. Clarify the distinction
between zero search and empty read symmetrically; permit one extra response and assess
required actual operations while retaining/charging refusals. Controlled proof must verify
that correction cannot substitute for a missing operation. Durable new artifacts live at
/home/motafeq/.local/share/upgradepilot/investigator-runs/deployment-interface-2026-10-17-r5;
no consequential output is assigned to temporary storage.

Re-entry source verification:29 focused controls pass, including six-arm budget/order
rejection, retained correction/completion and independent candidate continuation after
load refusal.65 nearest product tests pass(21.834s); Ruff/format and whitespace pass.
A test initially referred to a nonexistent result.responses field; corrected to the
actual invocation charge before passing. Full hashes for all four small GGUFs are
retained in r5/small-assets.json. Both small Gemma files explicitly disable automatic
BOS; MiMo/Qwen3.5 omit the flag/BOS id, so their no-added-BOS policy remains subject to
actual first-call prompt-count correspondence rather than inherited Qwen identity.
No new inference at this verification horizon.

All six r5 preflights complete with zero generation.72 actual rendered shapes inspected:
complete packed bytes/reference ids survive actual templates, raw/structured/report menus
match, measured maxima22581/22582/22389/22409/22573/22395 tokens plus2048+256 fit32768.
Full small-Gemma backend flag999999 contrasts with actual MiMo29/32 and Qwen9B30/32
blocks despite requested ratio1; raw applied ratio1 is not full-placement proof.
Core actual layers22/13 remain partial. Both small Gemmas add_bos=false; their actual
templates differ from Gemma12's BOS and thought-channel prefix. MiMo/Qwen templates
expose empty think delimiters under explicit reasoning-off; only observed fragment/usage
metadata can qualify that behavior. All exact originals remain private.

The public [r5 freeze](evidence/2026-10-17-investigator-model-interface-r5/canary-freeze-r5.json)
and private identical copy have SHA256
b0670107c07021e102f055162996d1d5963beed29ac340c8ed85d321d5e212aa.
Six deployments/24 ordered sequences/144 new max+19 prior/163 aggregate; output2048,
case comparison still2/8 unstarted. Freeze binds actual profiles,code,asset/runtime
identities and complete stateless/history/reasoning settings before generation. A first
inspection command lacked PYTHONPATH and failed before any freeze write/inference;
corrected to the established src:tests:. invocation. No model failure inferred.

Live r5 checkpoint: both small Gemmas spent four calls each, one per independent
sequence; every actual prompt count equals rendered+1, despite own metadata explicitly
add_bos=false. Guard refuses before dispatch; original E2B outputs finish immediately,
E4B proposes the requested first source/native tool. No original is repaired or accepted.
The supported repair hypothesis is an actual runtime BOS prelude inconsistent with the
file flag; verify <bos>/id2 through the actual tokenizer, represent the prelude explicitly,
and require exact actual-count confirmation under a separate freeze. Native actual token
IDs are not exposed, so retain that interpretation limit rather than call it a proven
backend root cause.

MiMo short Raw and Structured both match usage/config/JSON but repeat the first source
read six times and exhaust turn allocation. Long Structured repeats its native first
operation. Not a generation-budget/memory diagnosis; retain actual outputs/receipts.
Long first-token times around20–21s for16-token replies contrast with short ~2–5s; native
and client clocks remain distinct. Actual machine sampled GPU peak6364MiB with no observed
exhaustion. Continue all frozen candidates/sequences and analyze retained originals.

Further inspection: MiMo all four sequences match transport/config/counts but exhaust
six responses repeating the first requested operation; no final report. Qwen3.5-9B
Structured short performs positive-read twice, zero search, empty read and finish,
then generates a report. Its valid redundant read consumes the sixth allowance. The
frozen assessor requires exact operation order, so distinguish actual gate coverage/
redundancy from strict disposition. Do not silently weaken/relabel the frozen gate.

Source-level performance observation for future measurement: pack_input constructs
static task/tool fields before history, but canonical json_bytes sorts keys, moving
changing events before the large fixed task/calibration text. Complete stateless
requests therefore need not preserve a long identical prefix. This is a cache-efficiency
hypothesis, not a proven explanation for timing or repetition; no packing/source change
or persistent session is introduced in the frozen batch.

Shared interface repair selected after frozen r5 completion: actual observation bytes
are currently escaped within the full request JSON, and sorted keys put changing history
before static calibration/task. Repetition with complete history plus repeated long
first-token costs justify a single common presentation recheck, not a proven cause or
model-internal claim. The plan now admits direct exact observation contents after fixed
task/menu state in the same explicit stateless two-message request; no step counter,
forced action, response salvage, exposed omitted evidence or relaxed assessor. This
remains the current deployment/interface responsibility. Ali's explicit sustained Build
authorization and preceding orientation cover the repair; preserve actual findings
and gate limits rather than stopping at first behavior failure.

r5 process/code remains untouched while running. Once it finishes, change/test the
experiment presentation, prepare/inspect all six exact revised profiles and separately
freeze24 new sequence IDs/144 maximum calls. Aggregate explicit ceiling267 includes19
earlier attempts+r5 at most104 (eight small-Gemma attempts already spent)+144 revised
maximum. Existing r5 outcomes remain frozen historical results, no pooling/relabeling.
Small-Gemma BOS representation is reverified in the same preparation, with contradictory
file flags retained. Later semantic comparison remains2 deployments/eight assignments.

First Qwen9 Structured report (814 generated tokens, native51.36s/client47.12s) completed
with citations/uncertainty, but its positive-read duplication causes strict withholding.
Content inspection also finds unsupported global absence/unexamined claims: requirements.txt
remains unread, while the report says no manifest/further evidence exists. This is an
AI-assisted synthetic-report fidelity observation, not a protected-case semantic score
or independent usefulness judgment. Other Qwen9 sequences repeat source/native reads.

Gemma12 short Raw and Structured now both qualify in five calls after the shared task
clarification; the prior skipped empty read is actually exercised, not a weakened check.
Raw short report635 tokens/native137.06s/client125.68s/~4.77tokens/s distinguishes
positive/zero/empty with cited source observations and no compatibility claim. Long
Structured starts with the requested native read then missing-file problem; actual
first-token costs57–63s on20k inputs support the fixed-prefix performance hypothesis,
without proving cache internals.

The staged (not running r5) presentation passes31 focused controls, including a new
old-format-failing exact-observation/readability regression, canonical packed-input
retention beside the actual request, and per-candidate native default pinning without
inheriting prior per-call grammar. Original r5 source remains unchanged. A first ad hoc
control searched for an unescaped goal inside JSON and failed; corrected to compare its
exact canonical task serialization. These are model-free staging controls, not new live
qualification. Native receipts expose CPU7/topP0.95/topK64 and parser controls for Gemma12;
r6 will freeze every candidate's own observed applied fields, never copy them across
models. Keep unreported reasoning counts unknown.

Concrete stateless-history defect found during the long Gemma12 sequence: the missing
source observation reports invalid_source_query without the requested path, and packed
history contains only results, not the preceding model request arguments. Complete
serialized input was previously overstated as complete interaction history. This does
not invalidate request-local reference eligibility, but weakens attribution of repeated
operations to model capability. The selected repair now retains original UTF8 intent
in experiment AdapterEvent (explicit None for unavailable/non-UTF8 historical input),
packs intent/result together, and presents both byte-exact texts chronologically.
Prior requests remain model-authored intent with zero reference authority; product
source/lifecycle authority stays unchanged. Whole-event omission accounts for both.

This is the earliest sufficient experiment owner: actual request -> adapter invocation/
report refusal -> observation with retained intent -> trial packing -> actual model
rendering -> strict returned-output admission. No product field or durable Workspace
recovery/replay guarantee is introduced.32 staged controls pass, including a real
missing-path observation plus a refused request containing a forged typed reference:
intent remains visible but forged IDs remain ineligible. Staging first hit a relative
mechanical-manifest source-path error; corrected private snapshot filenames, without
changing runtime source or hiding that failed check. R5 remains frozen/running.

Gemma12 long Structured report content is complete but cites internal native record
id3ae236... instead of actually delivered native_record typed id021415... . Trial
charges show terminal_corrections1 and overall turn exhaustion; the old driver does
not retain its final report-refusal detail once no next input exists. Supported failure
is wrong reference identity plus repeated missing read; do not call it an output-token
exhaustion or invent the original missing refusal text. Exact originals remain.
A staged driver fix retains each actual report-refusal detail with its attempt number;
its new final-turn control passes without accepting/repairing the report. Shared wire
clarifies delivered typed IDs versus internal record/delivery/catalog IDs.33 staged
controls and Ruff/format pass; staged source hashes retained in r5/staged-verification.json.
Canonical r5 execution code remains unchanged until normal batch completion.

Material execution override: actual Qwen27 long calls use165–184s before first token
and~0.8–1.1generated tokens/s, while all six already have actual calls and the missing
prior-intent/shared serialized-history defect is diagnosed -> normal route completes
every remaining r5 sequence before source repair -> that spends substantial additional
time on the already superseded interface and delays the actual goal -> supersede r5
after its current prediction completes, preserve exact unfinished/unattempted status
and native receipts, then apply/verify/requalify the full six-candidate repaired cohort
-> no r5 full-qualification claim, no failure-selective promotion or semantic comparison;
all costs retained -> reconcile plan,MEMORY,separate superseded summary and new frozen
prior-spend/config/code/order before any revised inference. This changes the earlier
expectation of normal r5 completion for an explicitly evidenced better route.

Qwen27 both short sequences qualify in five calls. Its Structured short report1002
target tokens/native396.46s/client363.48s/~2.69tokens/s uses actual typed references and
explicit capture/compatibility limits; MTP870draft/712accepted/158rejected are separately
retained. Native and client clocks remain distinct.88 completed native metadata records
were audited: every requested setting matches actual, including the small Gemmas whose
token mismatch preempted that normal check; zero input-event omissions at that horizon.

Supersession completed at2026-10-17T12:48:42Z after call4 of Qwen27 Raw long:92
requests/92 saved native receipts, zero newly unknown usage, runner exit130 and native
inventory unloaded.22 normal sequence summaries remain original; Qwen Raw long is
partial and Structured long unattempted. The separate [superseded summary](evidence/2026-10-17-investigator-model-interface-r5/superseded-summary.json)
never claims the original runner finished normally. Publication after the last saved
prediction is unconfirmed; all proposed outputs and known costs remain retained.
Known r5 usage1,072,548 input/7,162 generated/1,959 draft; cumulative111 attempts with
the earlier one unknown r4 call still unknown. R6 maximum111+144=255<=267 ceiling.

Only after runner exit/inventory-unloaded and verification that all four canonical
r5 source hashes still matched its freeze, applied the separately staged repair to
the four existing experiment modules.33 canonical focused controls pass(.308s),65
nearest product tests pass(20.280s), four actual retained-case model-free regressions
pass(2.140s) with17 input/96 product hashes unchanged, zero forbidden/model/native
producer attempts. AST import direction96 files and touched Ruff/format pass. No
product source/dependency/specification/ADR changes. Root r5 named staged files are
explicitly labeled nonexecuted; actual r5 source is its preflight/freeze snapshots.

Observed contextPrefill is absent/unexposed in five candidates and [] in Gemma12's
native prediction metadata; do not copy the latter into other models or infer unknown
setting semantics. Own-model exposed actual defaults are pinned as recorded, with full
render/input correspondence required. Source repair is complete, fresh all-six r6
zero-generation preparation is next before any revised inference. Later semantic
comparison stays unactivated and parent adapter cycle remains CLOSED through E.

All six revised zero-generation preflights succeed with complete prior-intent/result
presentation, own native sampler/parser defaults and verified small-Gemma <bos>/id2
representation. Actual automatic GPU placement drifted despite ratio1: MiMo29(r5)
->30(r6), Qwen9 30(r5)->all-layer sentinel(r6). Requested percentage is insufficient
to freeze actual placement. Before any r6 inference, prepare two separately retained
fixed-offload profiles at requested0.85, actual backend28 layers each. That high point
is below the smallest observed automatic cap and preserves headroom; both treatments
share it. Preserve unused ratio1 profiles, disclose this configuration change and do
not attribute subsequent timing differences solely to presentation. Small Gemmas retain
all-layer flags; larger models22/13 stay partial. CPU q8_0 KV/context32768 unchanged.
All additional preparation has zero model outputs/calls, not extra experimental arms.

R6 selected-profile inspection complete:72 actual rendered shapes include full
canonical facts, exact prior request/returned observation texts, currently eligible
refs and correct Raw/Structured/report menus. Actual backend model paths match own
GGUF policies and full asset hashes; runtime path unchanged. Selected maxima22492,22489,
22236,22254,22486,22237 plus2048+256 and original8192+256 both fit32768; this is capacity
math, not8192-generation-speed/completeness proof. Source hashes match all selected
profiles; MiMo/Qwen9 fixed profiles28 layers supersede their unused ratio1 preparations.
The [r6 freeze](evidence/2026-10-17-investigator-model-interface-r6/canary-freeze-r6.json)
SHA256f6a7b34560f5a44759d901fa65cdf69fe22a096ca081c8ab2d9d1965496556e5
fixes all6/24 ordered IDs, own native settings,111 prior+144 new max255<=267 and
unchanged later2-deployment/eight-case nonactivation before any revised inference.

### R6 live diagnosis and native-mode follow-up decision

R6 remains running with unchanged source/freeze. Both small Gemmas now match actual
prompt counts after the BOS representation fix. E2B spends8 calls, E4B16; all eight
sequences withheld. Some fail because reasoning-labelled fragments appear despite
native enableThinking=false; the retained scalar flag alone does not establish their
nonempty length, and no hidden content was retained or inspected. Other failures are
skipped operations or foreign citations. MiMo spends23 calls across four withheld
sequences: the repaired history permits the required four operations, but Raw short's
report hits2048 with repeated claims; other reports use ineligible references. All
known native usage remains saved. Qwen9 Raw short qualifies; Structured short completes
without eligible citations and remains withheld. This is partial evidence, not a final
all-six disposition. Continue the remaining frozen independent sequences unchanged.

Planning/Design support revisits the actual operating mode, rather than forcing all
models to pass. Public primary-source research is retained under durable owner-only
r7: MiMo model API revision2367e865d009c13ac81713a2878291d33ab28177, generation_config
T0.6/K20/P0.95, metadata receipt URLs/hashes. Its card uses thinking on. Google docs
distinguish small off templates from12B empty-thought blocks; no guessed template
transplant is warranted. Google recommends T1/K64/P0.95. Earlier own-model native
predictionConfig exposes CPU/tools but omits top-p/top-k; pinning exposed settings
does not establish those absent effective sampler defaults. Preserve that limitation.

Material adaptation: applied off-mode violations plus MiMo's actual repetition/citation
failures and documented intended mode -> normal shared off-only qualification -> that
would withhold these deployments without examining a credible native operating point
-> plan section4.9 admits one separately frozen native-mode configuration per E2B/E4B/
MiMo, three deployments/12 sequences/72 calls, revised327 aggregate ceiling -> same
assets, history/reference/privacy/strict guards; native-mode8192 allowance and declared
provider-grounded samplers change comparability, so outcomes remain separate and no
intrinsic ranking or later case-arm expansion follows -> exact actual prior spend,
profiles/rendering/order/code/config/budget frozen before any follow-up inference.
No automatic parameter sweep or implicit later semantic comparison. This is continuous
B diagnosis inside Ali's repeated authorization, not a new architectural responsibility
or a reopened parent cycle; A-phase intent remains established, D/E remain pending.
Stage code privately while r6 runs; apply only after its normal completion and source
identity check. The three native settings will be tested before any actual model call.

Native-mode source remains private staged-only while r6 core models run.35 staged
controls pass, including explicit/applied on-mode versus strict off-mode and declared
sampling/default compatibility; the existing pre-accumulation hidden-fragment filter
is unchanged. First staged harness invocation failed to bind its loaded test module
into the parent Python package (14 tests,1 loader error); corrected harness binds the
parent attribute,35 pass. Both logs/verification records retained in r7. Staged Ruff
and format pass. No running r6 executable was changed. Qwen9 completes all four r6
sequences: Raw short/long qualify, both Structured reports cite no eligible evidence
and remain withheld. This is an actual negative reference-use result, not missing work.
MiMo's generation config was independently fetched at exact API revision and matched
the earlier main URL bytes. Primary metadata/templates never become case evidence.

Primary-source cross-check: MiMo actual loaded Jinja template equals the pinned
upstream3916-byte template exactly; comparison/hash receipt retained, without claiming
unknown local GGUF weight-revision correspondence. No speculative parser/template
replacement is justified. All four Qwen9 visible reports inspected: both Raw interface
passes cite actual eligible IDs but contain overbroad absence/negative statements; both
Structured reports cite nothing despite delivered references, so strict gate withholds.
This reinforces interface qualification ≠ semantic validity. Original outputs remain
unchanged. Partial r6 inspection after16 sequences:67 calls,865563 input/18119 target
generated,zero newly unknown usage; separate reasoning usage remains unreported. This
partial snapshot excludes active core calls and is not the final cohort total.

### R6 completed normally; actual outputs reviewed; r7 frozen before inference

All24 r6 sequences finished normally,108 native calls,1358562 input/27399 target
generated/4182 draft tokens,zero newly unknown usage. Gemma12 and Qwen27 qualify4/4
sequences each; Qwen9 Raw2/2 but Structured0/2, all E2B/E4B/MiMo sequences withheld.
Cumulative219 calls,known2475234 input/37004 target/7692 draft; the one earlier r4
unknown remains. Four original executable hashes match r6 freeze through completion;
owned inventory unloaded before applying the native-mode source. Sampler stopped with
its durable flag. No later semantic comparison. All completed visible reports reviewed,
including refusals/corrections: Gemma12 Raw short makes unsupported update-proceed
recommendation despite only synthetic interface evidence; its Structured long corrects
one mistyped native citation on sixth call. Qwen27 generally scopes capture/runtime
uncertainty well but Structured long incorrectly says no further operations available
while tools/other sources remain offered. Qwen9 overstates missing/negative evidence;
E2B long copies calibration number16000 into report fields; E4B confuses internal/event
IDs with delivered references; MiMo repeatedly cites unavailable native/update_packet
IDs and overstates no further evidence despite unread catalog entries. Strict guards
withhold invalid IDs. Interface pass does not establish semantic correctness.

Native-mode source applied only after normal r6 completion/source validation/unloaded
inventory.35 canonical controls pass;65 nearest product tests pass22.570s. Native
preparation newly selects CUDA backend2.60.0, b11698/2a667032d from installed metadata,
not r6's2.59.0. No installation/update by this session; cause/timing unknown. New flags
ubatch512/ctx32768/parallel4 replace1120/131072/4; MiMo flash=on, Gemmas=auto. Resolve
context ambiguity before inference: startup scalar fields confirm last three owned
preparations n_ctx_slot32768,kv_unified=true. Capture only allowlisted runtime scalar
fields, no log payloads/generations/credentials. Add explicit kv-unified/no-kv-unified
flag observation/reload guards and reprepare all three; original preparations retained.
Direct binary --help exits53 with empty output, retained as failed non-inference probe;
installed metadata plus native logs suffice without installing DLLs/changing environment.
A helper path replacement accidentally changed its r6 input profile path; it fails before
load and is corrected, with both logs retained. Native profile controls now cover KV flag
drift as well as identity/offload. Previous35-control result precedes that additional
assertion; final controls run again below. No adapter/product/accepted owner changed.

Selected final r7 profiles: E2B/E4B all-layer flag, MiMo28; CPU q8_0 KV,context32768.
36 actual whole rendered shapes inspected, maxima22491/22477/22245 +8192+256 fit.
Full present_request_body, original intent/result bytes, currently eligible IDs and
Raw/Structured menus survive template rendering. MiMo template thinking-on intentionally
ends with bare assistant header, off adds <think></think>; the first offline inspector
incorrectly expected a Qwen-style open <think> suffix, fails before freeze/inference,
then corrects from exact pinned template. No model template is altered to satisfy it.
All profile code hashes match current code. Explicit samplers/mode/output and unified
flags freeze requested/applied checks; actual backend file/release metadata hashed.
R7 freezes3 deployments/12 ordered sequences/72 new max,219 actual prior,291 revision
maximum within327 aggregate ceiling. Exact freeze and inspection are publicly retained
in the r7 evidence folder before inference. No old outcome pooling or automatic sweep.

Final pre-call focused35 controls pass(.336s), including explicit KV-drift assertions;
Ruff and whitespace pass. R7 freeze SHA256
68a4e819520d6f2c8fe7e45dcbfa0a0d3df0fcfca5ba533526962ef0f764b71a
was recorded/committed before launching the bounded SDK cohort. Native launch uses
the exact existing durable r1 --sdk-site; no dependency install/replacement transport.
Read-only app file-version recheck resolves D:\LM Studio\LM Studio.exe0.4.26+4 and
GPU RTX3070 Laptop8192MiB/driver617.42 unchanged; backend selection alone changed.

Push rejected because a parallel author added9e19c254's deferred stateful/SSE note.
Fetched/reviewed its sole100-line documentation change, explicitly no current-cycle
effect; merged without executable changes and revalidated r7 frozen source hashes.
No migration, changed budget, hidden history or altered reference authority follows.

R6 public actual-results plus ANALYSIS record all candidate operations/failures and
visible report inspection. Resource summary uses5801 samples within actual call window
13:13:09–15:03:33 UTC: whole-machine sampled GPU peak5798MiB, minimum host free
30156564KiB. These are sampled machine observations, not exclusive process or continuous
maxima. Qwen27 client call time totals3050.08s, longest845.34s; clocks/conditions vary,
so no causal model speed ranking. Complete r5/r6 directories now have owner-only files/
directories and per-file size/SHA256 retention indexes; r7 holds a separate index summary.
Local retention does not assert off-machine backup or repair old r4 lost prefix.

Execution-entry record checks:8 documents/99 local links/9 JSON files/fences pass,
96 product modules have no forbidden experiment/test/tool import, touched three-file
Ruff/format pass. R7 frozen source unchanged through remote merge; no full/installed/
hosted suite rerun for this experiment-only change. Native-mode live receipts already
confirm requested/applied on-mode, explicit samplers and prompt usage with hidden
fragments discarded before accumulation/storage. This fixes the mode support boundary,
not the model's planning/citation behavior; E2B's first two sequences remain withheld
for foreign references/early completion. Continue all remaining independent frozen
sequences, not an unbudgeted retry of those failures.

Current-runtime completion decision (plan §4.10): all four native E2B sequences
finish; both long pass and both short withheld. Do not infer a beneficial context
effect: short/long canary operation sequences differ, settings/runtime also differ
from r6, and there is one stochastic sequence per condition. E4B is running.

Material evidence/runtime adaptation: r6 core passes bind2.59.0, new native loads
select2.60.0 -> normal r7-only completion would hand off old core qualification
without current-runtime proof -> leaving that as a later surprise would undercut
this cycle's deployment/interface goal -> finish r7, then one bounded current2.60.0
point each for remaining Qwen9/Gemma12/Qwen27 (three configurations/12 sequences/72
new maximum), explicitly revised363 aggregate ceiling with actual prior spend frozen
after r7 -> unchanged six assets/later two-deployment/eight-case nonactivation, no
semantic acceptance, extra cost/transparency preserved -> update plan/live owner,
prepare/inspect/freeze before any r8 inference. This is current-runtime binding, not
a parameter sweep or escalation until all models pass. Existing off/T0.2/2048 point
is retained with explicit K40/P0.95/min-p-off/repetition-off instead of pretending
r6's unexposed sampler defaults were known. Multiple changes preclude causal runtime
comparison. Native r7 cohort/code stays frozen; remaining profiles can be prepared
only after it normally unloads. All six available assets will have a measured current
runtime operating point, with legitimate withheld results preserved.

Cycle-summary reconciliation: replaced the obsolete27-test/two-core-interrupted
status at the top with actual35-control/r6-complete/r7-running/r8-admitted state.
The old r3 todo is now explicitly historical; qualification-only extra configurations
do not themselves add semantic case arms. Current semantic design stays2×2×2=8.
MEMORY's older A2/parallel-parent-open continuation is similarly labeled superseded;
parent remains CLOSED through E. No historical failed/superseded outcome is erased.

Native r7 intermediate evidence: E2B spends17 calls, short Raw foreign event label
refusal, short Structured skips empty-file read; both long sequences qualify5 calls
each. Its reports remain shallow: Raw short claims procedural steps were followed
while actual events show an early finish, and long reports cite scoped observations
without establishing update evidence. E4B spends20 calls, all four sequences qualify
with exactly five each. All four visible reports inspected: positive/zero/empty/problem/
not_evaluated outcomes and actual typed IDs are preserved, compatibility generally
left uncertain. Raw long loosely calls the interface marker a dependency-update marker,
so4/4 is still not semantic acceptance. Neither a causal thinking-mode benefit nor
a context-length benefit follows from this changed-runtime/mode/sampler/n=1 evidence.
MiMo remains active; all costs/dispositions will be finalized after normal completion.

### Native cohort complete; current-runtime completion frozen before calls

R7 finishes normally:59 calls/12 sequences,741996 input/34148 target-generated,zero
newly unknown usage; all59 lack separate reasoning counts. E2B17 calls2/4, E4B20
calls4/4, MiMo22 calls2/4. MiMo's both long reports fail reference admission even
after the sixth-call correction: Raw repeats an internal32-character native ID;
Structured mixes internal/catalog/omitted-page IDs and invented source-hash:L1:1
with delivered refs. Its omission-versus-not_evaluated wording also exceeds evidence.
Every completed visible report/correction reviewed; no repair/regrading/pooling.
R7 source hashes unchanged through completion, owned inventory unloaded, sampler
stopped. Cumulative278 calls,known3217230 input/71152 target/7692 draft,one old r4
unknown remains.350-word guidance is not a frozen hard word-count gate; original
strict assessor dispositions stay unchanged, prose quality/verbosity reviewed separately.

R8 zero-generation preflights all pass: Qwen9/Gemma12/Qwen27 maxima22252/22486/22250,
backend layers28/22/13,declared off/T0.2/K40/P.95/min-p-off/repetition-off,2048 cap,
32k serial unified CPU q8_0 KV. All36 full rendered shapes/current refs/menus/original
intent/result pairs inspected; maxima also fit8192+256. New startup-log byte window
contains exactly the three owned load records, each n_ctx_slot32768/kv_unified=true;
only allowlisted scalars saved, no generation/log payload copied. Frozen source/profile/
asset/runtime/order/budgets before calls: SHA256
bb5bcd1ae12acfea18e4da98d35bd4bacdb3fc57e38bb196422ccfc1be7ee7e5,
278 actual prior+72 new max350<=363. The two-deployment/eight-case design stays
unactivated. No source change or new dependency/framework/transport was needed.

R8 execution starts only after `ab0183a9` publishes the complete r7 analysis and
exact r8 pre-run freeze to origin/main. This preserves the before-inference horizon.
Ali explicitly reiterates progressive recording/publication: publish coherent verified
increments during the work rather than accumulating everything until final closure.
Raw private evidence remains durable locally; public-safe summaries/configuration
freezes are committed and pushed. This does not assert off-machine raw-artifact backup.

R7 retention closes at720 indexed files/27,702,486 bytes, every size/hash/0600 mode
rechecked; index SHA256 b9a3064dd0637435cd4c4a12208ff32ff4e1166e56fb584a8dabd28fdd0183f7.
Resource inspection records2051 samples, whole-machine sampled peak6614MiB and
minimum host-free30,378,692KiB,zero sample errors; no process-exclusive/continuous-peak
or causal ranking claim. R7 is now immutable at that retention horizon; subsequent
cross-cohort checkers/results are retained in r8. Public record checks pass10 documents,
113 local targets/13 JSON files and96 product import-direction scans, with frozen
execution source unchanged. R8 first independent Raw-short Qwen9 sequence qualifies
with five calls; remaining sequences are still pending, not inferred from that result.
