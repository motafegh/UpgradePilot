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
| Deployments | Previously compared `google/gemma-4-12b` and `qwen3.6-35b-a3b-ud`. Resolve and hash actual model/package/template identities, placement, context and reasoning configuration before selection. An unavailable/unqualified deployment is withheld, never silently substituted. A changed model requires explicit protocol revision before case outcomes. |
| Assignments | Two cases × two treatments × two deployments: eight planned assignments, one each. Within deployment 1 use HTTPX raw→structured and glyphsLib structured→raw; reverse those orders for deployment 2. Serial execution, fresh contexts/state. One sample cannot estimate stochastic reliability or general superiority. |
| Case ceilings | 16 total model calls; 524288 input tokens; 131072 generated tokens including reported reasoning; 48 charged operations; 8 MiB delivered observations; 14400 seconds. Output ceiling/final reserve 8192 tokens; context 32768; temperature 0.2; HTTP timeout 1800 seconds. Corrections consume these ceilings: at most two visible corrections, at most one terminal correction. No failure-selective retry or output salvage. |
| Charging and packing | Freeze exact tool-to-backend accounting before calls. Count rejected requests, pages, native calls and underlying operations, not just wrappers. Retain whole-event omissions, unknown usage, timeouts and failures. Unreported reasoning/timeout usage is unknown, not zero. No hidden reasoning retention. |
| Qualification | Two fresh canary sequences per treatment/deployment, up to six model calls each; both treatments must qualify before that deployment's paired case runs. Up to 48 qualification + 128 case calls overall. A failed pair stays withheld with costs retained. |
| Review | Freeze source obligations and nine-dimension definitions before outputs. Balance/arm-mask first review where feasible; record revealed identities and assistance. Development review may be AI-assisted and cannot establish independent acceptance. |

These are maximum inherited envelopes, not a target for resource spending. Early mechanical failure stops the affected configuration. Any change affecting comparability is versioned before the affected batch and applied symmetrically; preserve prior artifacts. Do not tune against measured outputs and pool them into the same experiment.

The run manifest additionally freezes exact prompts and schemas, tool/menu/reference mapping, common packing/omission policy, source/view scope, random seed when actually supported, response/parser versions, code hashes, assignment IDs/order, deployment feasibility, resource controls and review procedure. These artifacts depend on the implemented bridge and fresh environment; completing them is an explicit output of mechanical integration, not an unowned planning gap. No canary or case run is admitted with placeholder fields.

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
