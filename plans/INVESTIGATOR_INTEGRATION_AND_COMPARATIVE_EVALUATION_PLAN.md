# Investigator Integration and Comparative Evaluation Plan

**Status:** admitted planning baseline; implementation, acquisition and inference require their own cycle entry and explicit activation.
**Responsibility:** integrate a single local Investigator with the product Workspace and determine whether structured native evidence access improves its evidence use over raw-oriented navigation.
**Live selection:** [MEMORY.md](../MEMORY.md) alone. This plan defines execution and proof, not current progress.

## 1. Product purpose, scope and owners

The product responsibility is useful, evidence-backed dependency-update assistance for public Python maintainers. This experiment measures a bounded mechanism contributing to that responsibility: finding relevant evidence, interpreting it correctly, preserving material uncertainty and proposing justified next work or stopping. It does not establish maintainer benefit, general semantic competence or permission to act merely by producing a report.

The initial offering comprises actual dependency/source-context and CI coverage/runtime native results, including their unknown/problem states, plus bounded frozen raw source navigation. Strong release/interval authority, general API applicability and adequacy remain unavailable unless separately admitted native owners supply them. This narrowing tests the interfaces already qualified by real preparation without requiring unrelated full migration or inventing evaluators. A negative result is bounded to this offering; a missing decision-critical family must be identified before proposing expansion.

| Owner | Execution consequence |
| --- | --- |
| [Charter](../PROJECT_CHARTER.md), [project route](UPGRADEPILOT_90_DAY_PLAN.md) | Public Python dependency-update decision support; experiments earn explicit dispositions and do not waive unfinished product outcomes. |
| [Core](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md), [Product Decision Model](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md), [Synthesis](../docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md) | Identity, material validity, observation/proposal/evaluation separation and action permission remain product-owned. |
| [ADR-0012](../docs/architecture/ADR-0012-canonical-investigation-workspace-and-recovery-boundary.md), [ADR-0013](../docs/architecture/ADR-0013-versioned-native-reconstruction-and-workspace-checkpoint-storage.md), [Workspace plan](INVESTIGATION_WORKSPACE_IMPLEMENTATION_AND_MIGRATION_PLAN.md) | Use the canonical host/native projections and supported checkpoint contracts; no research-owned replacement Workspace. |
| [Older planner plan](BOUNDED_PRODUCT_AGENTIC_INVESTIGATION_PLANNER_AND_ORCHESTRATION_EVALUATION_PLAN.md), [accepted planner protocol](B2_X1_PHASE3_EVALUATION_PROTOCOL.md) | Separate action-relative evaluation, oracle and protected-set obligations; follow §6 below. |
| [Report/usefulness plan](MAINTAINER_REPORT_PRESERVATION_AND_USEFULNESS_EVALUATION_PLAN.md#5-independent-usefulness-evaluation) | Independent maintainer utility remains a different comparison and may begin without full migration when its own readiness holds. |
| [Minimum Useful Generality](../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md), [Security](../SECURITY.md), [Environment](../ENVIRONMENT.md) | No known-case answer rules, authority escalation, hidden-reasoning capture, target execution/mutation, paid/cloud fallback or assumed current deployment facts. |

This adapts the [H1 proposal at research commit 253b48de](https://github.com/motafegh/UpgradePilot/blob/253b48de20b475eada48810d193bd420c51aa7d4/proposals/2026-10-08_H1_WORKSPACE_INVESTIGATOR_INTEGRATION_EXPERIMENT_DESIGN.md). That historical proposal remains evidence; this plan owns the bounded main-facing integration sequence. The older Fixed-versus-Agent comparison and interpretation-only trials remain historical references, not controls for a new evidence freeze. Do not copy or reactivate the entire research program.

## 2. Concrete product seam and reuse boundary

| Responsibility | Product seam / adapter consequence |
| --- | --- |
| Exact common inputs | [Shared acquisition](../src/upgradepilot/investigation_inputs.py) and [preparation](../src/upgradepilot/workspace/preparation.py) invoke the real dependency/CI owners. Preserve complete changed-file and exact target checks; no fabricated CI or upstream premises. |
| Canonical state and lifecycle | [Host](../src/upgradepilot/workspace/lifecycle_host.py), [material validity](../src/upgradepilot/workspace/material_validity.py) and native capture/projections own state. Each assignment gets a fresh host/lineage and separate mutable accounting. |
| Source/native delivery | [Source catalog](../src/upgradepilot/workspace/source_access.py) and [consumer access](../src/upgradepilot/workspace/consumer_access.py) supply list/read/literal-search/resolve and structured views/pages. Existing-record delivery is not a fresh producer attempt. |
| Purposes and requests | Trusted composition admits generic discovery purposes against the exact source universe/method. Genuine proposition-relative needs require a supported native non-final assessment. A model cannot mint authority, install methods or invent that assessment. |
| Proposals and stopping | Use attributed proposals/citations and separate procedural termination. The generic semantic/adequacy evaluator's unsupported outcome remains visible. Offline review never becomes runtime product feedback. |
| Local model and experiment | Reuse justified strict structured transport, fit measurement and receipts from the pinned research implementation after dependency/licensing/source inspection. Port only the needed experiment responsibilities; product runtime imports no experiment code. |
| Output/reference bridge | Preserve the Contract-2 laboratory report as attributed output, with a lossless product-reference mapping. Undelivered/invalid references refuse; absent fields are not filled from known answers. No product-report or action-authority promotion. |

Resolve exact adapter function names, tool schemas and public exports during the integration cycle against inspected source. They are implementation work, not reasons to create another architecture. If a required route is absent, identify the exact unmet claim and smallest product change before Build; do not emulate authoritative facts in the experiment. Source-only API semantic repair remains separately selected.

The experiment-owned adapter, scripted driver, exact reference/charging contract and offline proof entry are documented in the [mechanical qualification guide](../experiments/INVESTIGATOR_WORKSPACE_MECHANICAL_QUALIFICATION.md). Its inference-withheld mechanical manifest does not replace actual deployment/model-interface qualification or the final run manifest.

## 3. Recover or establish the common input freeze

Interface qualification and availability of the actual input bundle are separate entry conditions. The [October 15 qualification record](../working-memory/evidence/2026-10-15-common-investigator-preparation/qualification.json) supplies dated target/content/projection identities and historical proof. Its [evidence README](../working-memory/evidence/2026-10-15-common-investigator-preparation/README.md) identifies the original temporary paths; those paths are not a retention guarantee.

1. Search only known/documented local retention locations first. A candidate recovery must match the recorded target, provider receipt, source-profile and checkpoint identities. Check the store through its supported read-only validation, not file existence alone. Preserve original copies.
2. If no complete matching bundle is available, record exactly what remains recoverable. A source corpus or digest cannot reconstruct missing provider bodies. Do not label new network acquisition as reproduction of the old freeze.
3. A separately activated preparation may obtain the minimum missing anonymous public inputs using the existing diagnostic/providers. Preserve actual acquisition times, exact base/head, full changed-file and native-input checks; refuse drift. If a case is no longer feasible, stop and revise the paired case selection before outcomes rather than manufacture its data.
4. Create a new common freeze when any underlying evidence changes. Requalify native parity/unknowns, reference access and accounting for both treatments. Historical model outputs never become controls for the enriched inputs.
5. Keep receipts, profiles, checkpoints, manifests and required method/configuration data in an owner-only durable directory outside Git and temporary directories. Use the supported checkpoint backup API for stores. Verify a copied/backup bundle can be read from its new location without network/model/evaluator calls. Checkpoint and source-profile retention remain separate; no new storage framework or product replay feature is needed.

Before any real-model call, the run manifest must contain resolved absolute local paths, content/target identities, capture limitations, preparation-operation counts, a successful offline availability check and the code/interface identities. Public-safe summaries belong in the cycle evidence directory; do not commit raw/private receipts, credentials or hidden reasoning. Retention location is chosen and validated at entry, not inferred from an expired `/tmp` path.

## 4. Planned comparison and run controls

Both treatments are single adaptive Investigators on the same product host. The raw-oriented control receives bounded raw navigation. The structured treatment additionally receives the admitted dependency/CI native views and exact pages. Both receive the same underlying source universe and native preparation, target/transition, generic task, authority rules and proposal policy. Withheld native views in the control are a treatment restriction, not nonexistent data. This is a representation-and-native-analysis access bundle; gains cannot be attributed to serialization alone.

No case-specific paths, solved candidates, expected answers, interpretation-only packets or review labels enter model inputs. Both arms may read the raw producer premises. Do not selectively enrich an arm or provide privileged evaluation feedback. Preparation cost is reported separately; every within-run backend/native operation and repeated delivery remains charged and visible.

The following is the **planned development baseline**, adapted from H1, not inference authorization or a claim of current runtime availability:

| Setting | Baseline and qualification rule |
| --- | --- |
| Cases | The known HTTPX PR #20 and glyphsLib PR #1145 dependency transitions identified by the qualification record, conditional on exact input qualification. These remain exposed development cases. |
| Treatments | Raw-oriented and structured-native access; no Fixed-policy rerun, interpretation-only arm, critic or multi-agent topology. |
| Deployments | Exactly two planned candidates: `google/gemma-4-12b` and **Qwen3.8-27B**, using the user-selected Unsloth repository `unsloth/Qwen3.8-27B-GGUF`, quantization `UD-Q4_K_M` (approximately 16 GB as a planning estimate, not a measured asset size). This substitutes for `Qwen3.6-35B-A3B-UD` under the pre-run revision below; it is not a third arm. Resolve and hash actual model/package/template identities, runtime/version, placement/offload, context and reasoning configuration before inference. An unavailable/unqualified deployment is withheld, never silently substituted. |
| Assignments | Two cases × two treatments × two deployments: eight planned assignments, one each. Within deployment 1 use HTTPX raw→structured and glyphsLib structured→raw; reverse those orders for deployment 2. Serial execution, fresh contexts/state. One sample cannot estimate stochastic reliability or general superiority. |
| Case ceilings | 16 total model calls; 524288 input tokens; 131072 generated tokens including reported reasoning; 48 charged operations; 8 MiB delivered observations; 14400 seconds. Output ceiling/final reserve 8192 tokens; context 32768 is the inherited provisional reference, to be justified or explicitly revised by measured deployment-envelope qualification below; temperature 0.2; HTTP timeout 1800 seconds. Corrections consume these ceilings: at most two visible corrections, at most one terminal correction. No failure-selective retry or output salvage. |
| Charging and packing | Freeze exact tool-to-backend accounting before calls. Count rejected requests, pages, native calls and underlying operations, not just wrappers. Retain whole-event omissions, unknown usage, timeouts and failures. Unreported reasoning/timeout usage is unknown, not zero. No hidden reasoning retention. |
| Qualification | Two fresh canary sequences per treatment/deployment, up to six model calls each; both treatments must qualify before that deployment's paired case runs. The dated qualification revision freezes its own cohort/order/aggregate call ceiling; the expanded six-candidate re-entry explicitly supersedes the original48 qualification ceiling. The later eight-case-assignment budget remains128 calls. A failed pair stays withheld with costs retained. |
| Review | Freeze source obligations and nine-dimension definitions before outputs. Balance/arm-mask first review where feasible; record revealed identities and assistance. Development review may be AI-assisted and cannot establish independent acceptance. |

These are maximum inherited envelopes, not a target for resource spending. Early mechanical failure stops the affected configuration. Any change affecting comparability is versioned before the affected batch and applied symmetrically; preserve prior artifacts. Do not tune against measured outputs and pool them into the same experiment.

The run manifest additionally freezes exact prompts and schemas, tool/menu/reference mapping, common packing/omission policy, source/view scope, random seed when actually supported, response/parser versions, code hashes, assignment IDs/order, deployment feasibility, resource controls and review procedure. These artifacts depend on the implemented bridge and fresh environment; completing them is an explicit output of mechanical integration, not an unowned planning gap. No canary or case run is admitted with placeholder fields.

### Pre-run Qwen deployment substitution — October 16, 2026

Ali selected Qwen3.8-27B from `unsloth/Qwen3.8-27B-GGUF`, `UD-Q4_K_M`, to replace the prior Qwen3.6-35B-A3B-UD candidate **before inference or outcome-producing runs**. This is a protocol revision to the second deployment slot. The design remains two cases × two treatments × two deployments = eight planned assignments; balanced order, serial execution, fresh assignment state, shared evidence, accounting and all existing qualification/review gates remain in force. Historical Qwen3.6 research results/configurations remain historical and are not controls for this revised comparison.

The requested repository/quantization labels identify the candidate, not an already qualified local asset. Before any qualification canary or case inference, verify download completion and record the actual exact GGUF filename(s), byte sizes and SHA256 hashes (all required parts if split), repository revision when available, runtime/backend and versions, context allocation, GPU offload/layer placement, exact prompt/chat template identity/content hash, and reasoning mode/budget/configuration. Preserve supported settings and unknowns honestly; no old Qwen deployment identity, template, placement or reasoning setting may fill a missing new-deployment field. The planned context/budgets above remain protocol targets subject to actual fit/interface qualification, not observations about the replacement model.

Freeze these identities/settings in the run manifest before inference and use the same declared deployment configuration for both treatments. Record any necessary treatment-specific transport/interface difference and qualify both treatments; do not tune configurations using case outcomes. Download incompleteness, missing identity/configuration or failed fit/qualification withholds the affected deployment's pairs. A further substitution or comparability-affecting configuration change requires an explicit versioned pre-run revision; neither an extra model arm nor fallback to the old Qwen is implicit. This amendment authorizes no download, inference or cloud fallback.

### Smaller-model candidates and measured deployment envelopes

The user-directed smaller-model shortlist comprises `gemma-4-e2b-it`, `gemma-4-e4b-it-ud`, `mimo-v2.6-distill-qwen-9b` and `qwen3.5-9b-ud`, subject to exact asset/template/runtime qualification. Qwen3-4B-Instruct-2507 and Ministral 3 3B are excluded from this shortlist at Ali's direction; do not promote them because of an earlier assistant recommendation. Shortlisting does not add measured arms. Before including any smaller deployment in a batch, explicitly revise/freeze the selected deployment count, assignments/order, budgets and question; the existing two-deployment/eight-assignment baseline remains until that selection is made. Candidate availability, training labels and file size alone establish no Investigator quality.

Deployment qualification must choose a measured operating point for the defined workload, not claim a global optimum or blindly maximize context/offload. Treat GPU weight offload, KV-cache placement, context allocation, evaluation batch size and output/reasoning limits as distinct settings. Smaller models may use high/full weight offload when the actual workload and cache fit with headroom; larger models on the supported 8 GiB GPU use partial offload rather than forcing all weights into GPU memory. Record requested and actually applied settings; API defaults or nominal percentages do not prove placement. Freeze flash-attention/cache configuration and backend versions as applicable. [LM Studio load configuration](https://lmstudio.ai/docs/developer/rest/load) and [applied-config inspection](https://lmstudio.ai/docs/python/model-info/get-load-config) inform implementation; actual installed behavior must be checked.

First measure tokens in the **fully rendered** system/task/tool/chat-template input, allowed observation/history packing and late/final request shapes with the actual tokenizer. Admit a context only if measured packed-input tokens + reserved generated tokens + an explicit justified margin fit. The 8192-token response reserve includes generated reasoning where the runtime charges it; context capacity and maximum generated tokens are separate controls. Reference 32768 is not a reason to allocate that amount when a smaller envelope suffices, nor permission to reduce capacity until relevant evidence or final output is silently lost. If a changed context/packing/output policy changes comparison conditions, revise/version the protocol before the affected batch.

Use a bounded set of independent, outcome-blind canary workloads representing both treatments, short and near-envelope inputs, late history and final response production. They must exercise complete visible structured responses, tool/reference behavior and honest omissions without case-specific expected answers or protected material. Choose candidate context/offload settings from measured fit/pressure, estimate memory where supported, then measure actual prompt-processing time, time to first token, generated throughput, total latency, peak GPU/host memory, input/generated/reported-reasoning usage, completion/stop reason and failures. Retain failures/costs; do not capture hidden reasoning content. Resource qualification requires its own explicit inference activation and fits the bounded qualification budget; declare any extra configuration-sweep budget before calls rather than creating uncharged exploratory runs.

Select the fastest stable measured configuration that satisfies the declared input/output/completeness/headroom requirements and record the trade-off. Higher offload or larger context is not an automatic winner. Distinguish context overflow, generated-token exhaustion, timeout, memory failure, empty visible response, malformed output and early/semantically incomplete stopping before changing a parameter. Every adjustment records the observed symptom/metric, hypothesized cause, exact changed setting and discriminating recheck; unsupported diagnoses do not justify arbitrary increases/decreases. A context increase cannot repair an insufficient generation cap by itself, and valid stop metadata alone cannot establish substantive completion. [LM Studio's prediction controls](https://lmstudio.ai/docs/typescript/api-reference/llm-prediction-config-input) distinguish generation limits and context-overflow policies; avoid undisclosed server truncation.

Keep one frozen qualified envelope for both treatments within each deployment. Prefer comparable admitted context/packing conditions across models when feasible; if per-model hardware limits require different envelopes, preregister/disclose those differences and interpret cross-model results as deployment-specific, not a causal parameter-count ranking. Raw-versus-structured fairness, complete accounting, immutable outputs and no outcome-driven tuning remain mandatory. Fit estimates are preflight evidence, while successful load/canaries supply separate actual qualification; neither establishes semantic usefulness. No load, canary, automatic sweep or measured comparison is activated by this planning amendment.

### Pre-comparison stateless qualification revision — October 17, 2026

The first independent canaries spent five calls: Gemma exposed automatic BOS insertion
missing from SDK text rendering; Qwen's visible output failed the tool/report wire despite
matching measured prompt counts. Those failures remain rejected and separately retained.
Neither was context overflow or output-budget exhaustion. Correct input measurement from
actual tokenizer special-token identity and use the existing closed tool/report schemas
as runtime JSON grammar, without repairing or promoting prior output. Apply this revised
wire symmetrically before affected inference; explicit stateless reference eligibility
and all identity/authority/fairness gates remain unchanged.

The revised independent sequences use **five calls each**, still within the six-call
upper bound: positive read/follow-up, scoped zero/empty/problem outcomes, real typed
reference/report proposal and procedural stop remain required for both treatments.
Separate model note/event-readback probes are deferred; their mechanical contracts remain
proved, not newly claimed as real-model qualifications. They were additional probes, not
requirements removed from the selected gate. Any later evidence that those tools are a
material model-interface prerequisite triggers their explicit re-entry before affected use.

Freeze two deployments × two treatments × two sequences = eight qualification assignments,
40 new calls maximum; together with five prior attempts this is at most **45 of the original
48 calls**, with no free retry/sweep. Failed deployments remain withheld with costs retained.
Qwen's actually enabled native MTP setting is explicitly retained/disclosed as part of that
deployment; reported draft tokens/latency are separate runtime costs, not an extra model arm
or a claimed cause of the earlier output failure. The exact revision, profiles, order and
budgets belong in the dated immutable batch freeze. The two-deployment/eight-case semantic
comparison remains separately gated and is not activated by this revision.

### Six-candidate qualification re-entry — October 17, 2026

Ali's explicit instruction to continue after the incomplete two-core work admits a
separate **six-deployment qualification cohort**, not six semantic comparison arms.
Qualify Gemma 4 E2B, Gemma 4 E4B, MiMo-V2.6-Distill-Qwen-9B, Qwen3.5-9B,
Gemma 4 12B and Qwen3.8-27B UD-Q4_K_M, serially in that order. Alternate which treatment
starts per deployment; each has short Raw/Structured and long Raw/Structured sequences.
Freeze the exact 24 ordered sequence identities before inference. The later semantic
comparison remains **two deployments / eight case assignments**, unactivated; selecting
smaller replacements there requires its own explicit pre-comparison decision/revision.

The revision permits at most six calls per sequence (five required steps plus at most
one extra response), **144 new calls**, with all **19 earlier attempts** retained:
**163 aggregate qualification calls maximum**. This explicitly supersedes the old
48-call qualification ceiling rather than treating unused calls or added arms as free.
Reserve the full earlier 8192-token allowance for the interrupted call whose actual usage
is unavailable; never substitute that conservative budget reservation for measured usage.
The later case budget is unchanged. No hidden retry, automatic sweep or salvage is admitted.

Use the same clarified ordered task for every candidate/treatment. Explicitly distinguish
zero-match search from the separately required empty-file read and ask for a concise
report of at most 350 words. Permit 2048 generated tokens per call for these synthetic
interface tasks: the earlier complete Qwen report used 1411, leaving over 600 tokens of
headroom; truncation remains a failed check, never an accepted shorter report. This
qualification-only limit does not change the 8192-token case-study reserve. Keep context
32768 for the declared original input/output envelope; do not claim an optimal context
without comparative speed/completeness measurements. Use actual GGUF/BOS metadata and live
render/token measurements. Keep CPU q8_0 KV and batch256 as the controlled baseline; use
full weight offload for the four smaller candidates only if actual load/resource evidence
supports headroom, retaining partial offload for the two larger deployments. Retain actual
native MTP and requested/applied reasoning configuration; unsupported settings withhold.

The earlier valid Gemma report omitted a required operation. Task clarification is an
interface-scaffolding revision, not evidence that its cause is known or that autonomous
investigation improved. Assess actual operations, outcomes and cited evidence; never force
the correct tool via the runtime grammar. Keep all refused originals and their charges,
while allowing a corrected request to satisfy the still-required operation. Strict JSON,
usage/configuration correspondence and current-request-only evidence admission remain.

For this diagnostic cohort, a behavioral failure withholds that sequence/deployment's
later comparison but does not suppress the other independent frozen sequences. This
replaces deployment-wide early withholding to provide the requested six-candidate views.
A load/identity failure withholds that deployment and is recorded without a fallback;
other independent candidates may proceed. An interrupted/unknown-usage call is charged
its reserved upper bound and never retried within the revision. Qualification requires
all four sequences; partial completion is reported as partial. Inspect actual outputs
and costs from every attempted assignment, including failures. Any further adjustment
must be diagnosed, recorded and frozen as a distinct revision before affected calls.

### Complete stateless observation presentation repair — October 17, 2026

After preserving the frozen six-candidate batch outcomes, permit one common request-
presentation repair before withholding deployments solely on that interface. The old
batch may be explicitly superseded at a completed prediction boundary when actual
latency and the shared history defect make completing the remaining old-format runs
worse than applying/requalifying the repair. Preserve all originals/costs; label
unfinished/unattempted sequences superseded, never completed or model failures. A
separate supersession record must identify the boundary and actual/unknown usage; do
not fabricate the original runner's normal-completion summary. Source inspection shows
that canonical JSON wraps each observation as an escaped string and sorts changing
history before the large fixed task. Completed short runs show repeated operations despite
included history; long calls repeatedly pay substantial first-token latency. These are
supported presentation/cache-efficiency hypotheses, not established model-internal causes.

Keep the canonical packed bytes for admission/accounting, but present their complete
contents as fixed protocol/task/report fields first, then current phase/menu/omissions,
then chronological event identifiers, each original UTF8 model-authored request and
its exact original returned observation JSON content. Actual missing-file observations
may omit the path, so results alone do not provide complete stateless action history.
Retain the original request separately at the experiment adapter/driver boundary;
non-UTF8 or historical unavailable intent stays explicitly unavailable, never repaired.
Omit request/result pairs together and retain omission bytes/hashes for both components.
Past requested/forged citations grant no evidence authority: eligible IDs still come
only from the included delivered observations, never from prior request text.
Do not duplicate or rewrite source content, omit facts, add hidden memory, reveal omitted
evidence or force an expected next action. Every component and every eligible reference
must survive actual template rendering; generation must use that exact measured request.
Two explicit system/user messages remain complete stateless inputs. This is a common
interface revision, not an outcome-driven case prompt change or relaxed qualification gate.

Apply the same representation to all six candidates and requalify four sequences each:
**six deployments / 24 new sequences / 144 new calls maximum**, with the preceding
19 attempts plus every actual r5 attempt retained separately. r5's eight small-Gemma
calls are already spent; its remaining four deployments can spend at most96, so its
actual total is at most104. The aggregate cycle ceiling is explicitly revised from163
to **267 calls maximum** (19 +104 +144), not an uncharged retry. Freeze actual prior
spend, current code/profiles, all24 distinct ordered IDs and exact ceilings before new
inference. Earlier outcomes keep their original dispositions and are never pooled as
same-protocol successes. No further automatic sweep is admitted by this amendment.

Explicitly pin each candidate's exposed actual prediction defaults from its own r5 native
receipt (including CPU threads, sampler and reasoning parser settings), retaining source
identity/hash. Override template/reasoning/output only with the declared current values;
never inherit another model's defaults or reuse its prior per-call runtime grammar.
Actual applied values must match those requested in every new prediction.

Represent the small Gemmas' observed runtime special-token prelude using actual tokenizer
BOS identity verification and exact prompt-count admission, retaining their contradictory
file metadata and the fact that native prompt token IDs are unexposed. Preserve2048
synthetic-only output limit,32768 context, reasoning-off and already measured weight/KV
settings unless actual fit drift requires a separately recorded change. Zero-generation
reloads showed MiMo ratio1 applying29 then30 layers, and Qwen9 ratio1 applying30 then
the all-layer sentinel. Before r6 inference substitute requested ratio0.85 for these two
slots, yielding28 backend layers in both inspected profiles: high partial offload below
the lowest observed automatic cap. Preserve the unused ratio1 preparations, verify the
fixed actual layer count at execution reload and disclose that change; it is not a new
candidate arm, global optimum or causal presentation-only performance comparison.
Recheck all
rendered shapes after the presentation revision. Retain the strict assessor for this
revision; descriptive review separately identifies redundant-but-complete operations,
missing operations and unsupported report statements. Later semantic comparison remains
two deployments/eight case assignments and unactivated.

### 4.9 Bounded native-mode follow-up after the complete r6 cohort

Finish r6 unchanged; retain every failed sequence and its actual visible output. Its
strict reasoning-off requirement is a deployment condition, not a general model-quality
verdict. In r6, small Gemmas intermittently return reasoning-labelled fragments despite
the applied off flag; MiMo reaches required operations but repeats/exhausts a report or
uses ineligible references. Do not erase these outcomes or merely increase context.

Admit **three fresh configuration deployments / 12 sequences / 72 calls maximum**:
Gemma E2B, Gemma E4B, then MiMo9B, each short Raw, short Structured, long Raw, long
Structured. All six candidate assets remain available. This is a bounded qualification
follow-up, not three additional arms in the later two-deployment/eight-assignment case
comparison. Before affected inference, freeze exact completed prior spend plus72 within
an explicitly revised **327 aggregate call ceiling** (111 prior +144 r6 maximum +72).
No automatic further parameter sweep is admitted.

Use each actual loaded template with thinking explicitly on. Keep complete stateless
request/result history, current-request reference admission, runtime grammar, context32768,
weight placement and CPU q8_0 KV unchanged. Apply/verify temperature1/top-p0.95/top-k64
for E2B/E4B, and temperature0.6/top-p0.95/top-k20 for MiMo. Explicitly disable extra
min-p/repetition filtering rather than claiming absent r6 sampler fields resolved their
effective defaults. These recipes are grounded in the [Google model card](https://ai.google.dev/gemma/docs/core/model_card_4)
and MiMo's [published generation configuration](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B/blob/2367e865d009c13ac81713a2878291d33ab28177/generation_config.json).
The [MiMo card](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B)
uses thinking mode; [Google's thinking documentation](https://ai.google.dev/gemma/docs/capabilities/thinking)
distinguishes small-Gemma and larger-Gemma off templates. Do not transplant the12B
empty-thought prefix into small models or change GGUF/tokenizer identity.

Raise only this declared native-mode output allowance to8192 target-generated tokens
per call, including any internal generation, with49152 maximum per sequence and the
same six-call/14400-second sequence limits. This uses the previously measured reserve
to permit thinking plus a concise visible report; it is not a claim that repetition or
invalid citations will be solved by more tokens. Reinspect every fully rendered shape
with actual native-mode configuration before freezing/executing. Requested/applied
identity/configuration and actual prompt-count checks remain mandatory.

Actual follow-up preparation selected backend2.60.0/b11698/2a667032d, replacing r6's2.59.0, with changed ubatch/context allocation and MiMo flash flag on. Freeze this
observed runtime and unified-KV flags before inference; native startup scalars must
confirm32768 per-slot capacity. Preserve unused preparations and runtime-change
evidence. This additional confound precludes attribution to reasoning/sampling alone.

The transport must permit reasoning-labelled fragments only when thinking was explicitly
requested and verified applied; it must continue discarding them before SDK accumulation
and artifact storage. Off-mode violations still fail. Retain visible responses and scalar
usage/flags only; absent separate reasoning-token counts remain unknown. Preserve the
strict sequence/citation/report guards. Report native-mode outcomes separately from r6;
different samplers/modes are not a causal single-variable or intrinsic model ranking.

### 4.10 Bind the remaining candidates to the newly selected runtime

The observed2.59.0→2.60.0 change prevents inheriting the r6 core-profile passes as
current-runtime qualification. After r7 completes unchanged, admit one separately
frozen2.60.0 operating point for Qwen9B, Gemma12B and Qwen27B, in that order:
**three configuration deployments /12 sequences /72 calls maximum**. Each uses short
Raw, short Structured, long Raw, long Structured. The overall asset cohort remains
the same six candidates; this is not an expansion of the later two-deployment/eight-case
comparison. Revise the aggregate ceiling explicitly to **363 calls** (219 actual
before r7 +72 r7 maximum +72 r8 maximum); freeze actual completed prior spend before
new inference, not this conservative maximum as measured usage.

Keep complete stateless history, source/reference/menu/report/strict-sequence guards,
32768 context,CPU q8_0 KV and existing measured weight placement. Use thinking off,
2048 per-call/12288 per-sequence generation,temperature0.2 and explicitly top-k40 /
top-p0.95 with extra min-p/repetition filters disabled. This is a declared controlled
interface operating point, not an optimum or a claim about unresolved r6 defaults.
The explicit samplers plus backend change preclude attributing differences to runtime
alone. No changes to case prompts, protected material, output repair or forced tools.

Prepare/inspect all36 actual rendered shapes and exact current executable, template,
tokenizer, asset, load, unified-KV and prediction settings; freeze identities/order/code/
configuration/budgets before affected calls. Verify requested/applied correspondence
and actual measured prompt usage in every prediction. Preserve r6/r7 originals,
including every withheld outcome, and report all new dispositions separately. No
further automatic sweep or semantic case inference follows this bounded completion.

## 5. Ordered execution and proof gates

Use coherent Learning-by-Doing cycles; the first integration cycle may complete with no inference. Do not split obvious implementation details into separate ceremonial cycles. Each gate produces reviewable evidence and an explicit proceed/refuse/inconclusive result.

| Gate | Required result | Failure / stop consequence |
| --- | --- | --- |
| Input and interface entry | Exact common bundle available/qualified; actual supported seam and exclusions mapped; next-cycle A-phase and modification scope established. | Recover or explicitly refreeze inputs; name an exact missing interface if one exists. No generic infrastructure restart. |
| Mechanical integration | Shared product host adapter; raw-control fidelity; structured views/pages; strict request/proposal/reference mapping; isolated assignments and complete accounting. Freeze prompts/tools/manifest from this result. | Repair adapter/contract defects before calls. No model diagnosis from broken delivery or authority. |
| Model interface qualification | Fresh local identity/fit checks, positive read, later follow-up, scoped zero/empty/failure, valid purpose/reference/proposal, and procedural stop exercised for both treatments. | Withhold the deployment's pairs, retain failures/costs, make a bounded repair or configuration disposition. |
| Paired development comparison | All admitted assignments attempted under the freeze, immutable originals, failures/withheld runs retained, review against actual common sources. | Preserve not-comparable, failed, incomplete and unsupported results separately; no selective reruns. |
| Evaluation disposition | Evidence-backed mechanism conclusion with costs, limits and concrete next responsibility; older planner disposition coordinated under §6; usefulness readiness addressed under §8. | Inconclusive is valid. No silent product adoption or another preparation phase without a discriminating need. |

Mechanical controls must cover exact target/material/scope/method rejection; missing/incomplete/drifted inputs; malformed/extra-authority requests; rejection without execution; zero/empty/problem distinctions; reference escape and truncated search previews; omitted native records with partial-page access; unsupported semantic/adequacy outcomes; stale versus unrelated-revision progress; publication failure and observable work accounting; isolated host/notes/caches; model-input exclusion of oracle/review data. Reuse existing product tests for established invariants; add tests for the actual new adapter seams instead of copying the suite.

Verify changed experiment contracts and nearest product integration first. Product source changes require affected checkout and fresh noneditable installed proof under the Build Skill; experiment-only changes require their own focused/integration suite and import-direction checks, not an invented full-product implementation claim. Reuse guarded cold inspection only for the retention claim actually made. No target code/workflow execution is included.

### Proposed cycle grouping and adaptation

The following is the planning baseline for work after common-input qualification, not a fixed cycle quota, calendar promise or automatic activation. Each selected cycle uses the canonical learning/action progression; its record owns detailed phase status, while MEMORY.md owns live selection.

| Proposed coherent cycle | Result and completion boundary | Initial expectation, not a promised outcome |
| --- | --- | --- |
| Investigator adapter and mechanical qualification | Product-host bridge, strict tool/request/proposal/reference mapping, faithful raw/native offerings, fresh assignment state/accounting and focused integration/failure proof. Model-free. At the first completed mechanical gate, perform the older planner entry review under §6 and assess usefulness readiness under §8. | Existing interfaces should support a small bridge; contract mapping, reference/omission handling and isolation are the likely pressures. No semantic/model advantage follows from mechanical success. |
| Actual deployment and model-interface qualification | Resolve both actual local deployments and complete required canaries for both treatments, or explicitly withhold an unqualified deployment with retained costs/reasons. Preserve the pre-run Qwen substitution and all actual-identity gates. | Fit, template/reasoning behavior and strict-interface behavior need measurement; no replacement-model performance assumption. |
| Paired comparison, semantic review and disposition | Attempt all admitted assignments under the frozen protocol; retain failures/withheld states and immutable outputs; review material claims, uncertainty, stopping and costs; produce a bounded retain/reject/inconclusive disposition. | Mixed development results are plausible: easier evidence navigation may coexist with interpretation/applicability errors. Eight exposed-case assignments cannot establish general superiority or stochastic reliability. |

The older action-planner execution/disposition and independent maintainer usefulness retain their separate owners and questions. Either may need a separately selected cycle when ready; usefulness need not wait for Investigator success. Thus three core cycles, with potentially one or two related cycles, is a coordination estimate rather than an obligation or a cap. The first mechanical gate reviews the older planner even if later model work is delayed.

Keep ordinary defects/failed checks inside their current responsibility until repaired or truthfully dispositioned; do not create a cycle merely to rename missing verification. Combine or split work only when progress demonstrates a better coherent responsibility or genuinely distinct proof/ownership boundary. A new cycle is justified by a material new responsibility, not a file count, routine correction or desired technology exposure. If evidence changes selected scope, design, protocol, proof or sequencing materially, explain the circumstance and trade-off, reconcile the owning plan/protocol before affected execution, and preserve the rationale in the cycle record. The gates, protected material, fairness, authority and evidence truth remain controlling. No further cycle, model run, framework or native-family expansion is activated by this grouping.

## 6. Explicit disposition of the older action-planner obligation

**Coordination decision: retain a separate action-relative checkpoint; share compatible transport/accounting only.** Do not rewrite its accepted oracle to fit H1 reports or count H1 evidence-use scores as action-selection results. The [accepted protocol](B2_X1_PHASE3_EVALUATION_PROTOCOL.md) owns its one-action question, development/protected cases, thresholds, contamination and allowed dispositions. Its frozen processing inputs are a separate evaluation profile, not the H1 common source freeze.

At the first completed mechanical-integration gate, perform the bounded checkpoint entry review under the [planner plan](BOUNDED_PRODUCT_AGENTIC_INVESTIGATION_PLANNER_AND_ORCHESTRATION_EVALUATION_PLAN.md): reconcile current contract/selector/transport identities, previously exposed versus still-protected material, available frozen inputs and earliest unfinished required proof. Reuse valid prior work rather than restart the historical phase sequence. Do not open protected answers for adapter tuning or silently substitute current semantics for a historical oracle.

If the accepted question/profile remains valid, select its separately authorized development/protected execution under that owner. If not, produce an evidence-backed reject/defer or a specific protocol-repair decision identifying the exact invalid dependency, retained product cost and re-entry evidence. Method adoption is not assumed. This entry review can proceed independently of H1 semantic outcomes and must not be postponed until H1 succeeds.

The combined evaluation handoff cannot release ordinary B2 continuation without that explicit planner disposition. The H1 development batch need not wait for protected planner scoring when its own gates pass, but cannot close or replace that obligation. A new deferral needs concrete decision-changing evidence; “finish Workspace,” “H1 passed,” or another model being available is insufficient. Framework adoption remains separately justified by a demonstrated limitation of the synchronous baseline.

## 7. Semantic review and decision rules

Carry forward the [nine-dimension definitions at the research cutoff](https://github.com/motafegh/UpgradePilot/blob/253b48de20b475eada48810d193bd420c51aa7d4/working-memory/evidence/2026-10-07-broader-agency-evidence-interface/evaluation-dimensions-v2.json), retaining their content identity in the run manifest. No weighted winner score is introduced.

| Dimension | Evidence to retain |
| --- | --- |
| Relevant evidence coverage | Preregistered source obligations; available, delivered, observable use, cited and supported states separately; undiscovered feasible obligations remain counted. |
| Interpretation correctness | Material subject/operation/polarity/release/time/capture meaning across claims, notes and report, including correct use of native unknowns. |
| Unsupported claims | Unsupported versus contradicted propositions and advice premises, with source reasons; deduplicate repeated propositions transparently without hiding their surfaces. |
| Scoped negative evidence | Actual query scope, paging and completeness; no empty/failure/global-absence substitutions. |
| Unresolved quality | Specific missing premise, unavailable evidence, unsupported evaluator, conflict or unperformed check and its consequence. |
| Stopping quality | Stop proposal versus procedural end; remaining feasible discriminators at actual capability/budget; unavailable adequacy evaluation remains unavailable. |
| Recommendation usefulness | Specific supported explanation/proposed next work in attributed laboratory output; no product action permission or independent user-benefit claim. |
| Reviewer effort | Active source-check/triage/revision intervals, assistance and interruptions; unmeasured time stays unknown. Failed runs contribute triage cost. |
| Resource cost | Preparation plus every model/backend/native/view attempt, measured tokens/bytes/time, packing, corrections and unknown usage. |

Freeze source obligations before output review and hide them from the Investigator. New obligations found during review are supplemental, preserving the original denominator. Review every material assertion, including summaries/recommendations; valid citation shape does not prove entailment. Preserve the immutable model output separately from review corrections. Record active review timers with pauses; do not infer effort from model wall time. AI-assisted known-case review is formative, not independent or unseen proof.

- **Retain as development pilot:** paired evidence identifies useful gains in correct evidence use/coverage/uncertainty or stopping, with no hidden critical unsupported claims or authority violations and explicit cost trade-offs. Mixed per-case effects remain visible.
- **Reject the affected configuration/claim:** authority or identity promotion, material false confidence, or a claimed advantage resting on unequal information/hidden costs. Distinguish product adapter defects from model errors before choosing repair.
- **Inconclusive / named defer:** qualification/input/review failure, incomparable profiles, ambiguous trade-offs or insufficient evidence. Preserve the smallest discriminating follow-up; do not invent a winner.

Known-case success does not admit a production Investigator. Generalization requires a separately frozen protected sample/replication design with independently reviewed obligations and reviewers, without case-specific tuning or outcome-driven exclusions. HTTPX/glyphsLib remain development evidence. A source/reference defect routes to integration repair; semantic failure despite adequate delivery routes to a bounded semantic-method investigation; lack of benefit routes to simplification/rejection rather than more machinery by default.

## 8. Future responsibilities, activation and closure

| Responsibility | Trigger and proper next owner |
| --- | --- |
| Independent maintainer usefulness | At integration/evaluation handoff, check whether actual normal reports, equivalent ordinary-review source packets and independent reviewers meet the [existing study](MAINTAINER_REPORT_PRESERVATION_AND_USEFULNESS_EVALUATION_PLAN.md#5-independent-usefulness-evaluation). Select it or record the exact gap/re-entry condition in MEMORY. Model development need not finish first. Reviewer contact needs explicit authorization. |
| Semantic capability | A reviewed decision-critical interpretation/applicability/adequacy failure persists with adequate evidence. Select the exact method/baseline/rejection question; no automatic generic evaluator or critic. |
| Broader native family | A real required question cannot be served at the offered native strength. Use the smallest justified expansion under the Workspace plan; no family expansion solely to improve a known-case score. |
| Consumer migration and continuation | Follow the Workspace plan's direct consumer, supported-family and present-authority gates when their responsibility is selected. A research transcript cannot satisfy those contracts. |
| Deterministic replay | Specify the retained-input processing boundary, methods and equivalence test under Charter/Core before activation. Bundle availability or cold checkpoint recovery does not satisfy replay. |
| Framework, additional model or topology | Measured capability/resource failure against the simple baseline justifies a separate comparison and any needed ADR. Exposure for learning alone does not justify product dependencies. |

Completion requires the admitted integration/qualification/comparison evidence or a truthful explicit refusal/inconclusive disposition, immutable artifacts with retention limits, semantic and cost review, older planner coordination, usefulness readiness disposition, and D/E learning/handoff under the selected cycle. No project stage is passed solely by this experiment.

Allowed later implementation scope is the experiment adapter/runner, its tests and evidence, plus a separately identified necessary product seam repair. Product changes follow the Build procedure and accepted owners. Excluded: target mutation/execution, arbitrary shell/network tools, paid/remote inference, semantic-oracle leakage, automatic retries/salvage, hidden reasoning capture, general agent platform, automatic schema migration, new action permissions, full consumer migration or replay by implication. Stop on a consequential contract/method conflict and reconcile its proper owner before continuing.
