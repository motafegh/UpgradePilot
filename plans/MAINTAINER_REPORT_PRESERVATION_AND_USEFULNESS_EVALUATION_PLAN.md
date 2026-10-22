# Maintainer Report, Preservation and Usefulness Evaluation Plan

**Status:** execution/evaluation plan with separate feature-faithfulness and independent-usefulness gates; activation and proof status belong only in MEMORY.md.
**Responsibility:** deliver and assess a faithful report of one normal dependency-update investigation, preserve the named result boundary, and determine whether it helps maintainers.
**Selection gate:** [Product Direction and Maintainer Utility Investigation](PRODUCT_DIRECTION_AND_MAINTAINER_UTILITY_INVESTIGATION_PLAN.md).
**Workspace relationship:** [Workspace implementation and migration](INVESTIGATION_WORKSPACE_IMPLEMENTATION_AND_MIGRATION_PLAN.md) owns canonical producer/consumer cutover and recovery; this plan owns report behavior and its usefulness study. Each has a separate activation/proof boundary.
**Project route:** [Evidence-Derived Learning and Building Plan](UPGRADEPILOT_90_DAY_PLAN.md).
**Live selection:** [MEMORY.md](../MEMORY.md) alone.

## 1. Full responsibility and first increment

The supported user must be able to identify the exact update, understand material findings and their sources, distinguish what remains unknown, and identify a justified next step where one exists. The user must be able to inspect the same named result later. Final actions remain subject to the accepted [Maintainer Action Synthesis](../docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md) contract.

The first delivery trial is a normal-path human report plus a versioned saved-result representation, with meaningful incomplete/degraded/unsupported behavior and a declared evaluation protocol. It is not a new evidence acquisition engine.

Important deferred responsibilities:

- full raw-response capture, recomputation of deterministic reasoning, execution resume and cross-run query infrastructure;
- broad impact discovery and comprehensive workflow/environment coverage;
- new action permissions, AI-written final synthesis, patch generation and target writes;
- web/API interfaces, multi-repository operations and private/multi-ecosystem input.

These are distinct proof obligations rather than conveniences removed to pass a small test. Saved-result reopening makes a report inspectable, but cannot reproduce unrecorded acquisition or reasoning. Known coverage limits must remain visible rather than disappearing from the evaluation denominator. If independent users need recomputation or richer impact evidence before the output is useful, revise the trial or activate the exact missing responsibility rather than declare success.

## 2. Entry conditions and contract decisions

Before implementation selection:

1. the direction comparison selects independent report utility as a justified trial;
2. exact normal producer/source boundaries have been traced;
3. report required states, source references, supported claims and availability distinctions are accepted through the correct semantic owner;
4. saved-result version/identity/reopen/error semantics have a clear owner;
5. an evaluation protocol freezes case selection, input mode, criteria and baseline before result inspection;
6. unresolved design decisions and authorized Build scope are explicit.
7. the named-consumer retention review in §9 records what is retained, retrievable or unavailable before public-schema freeze or evidence discard; compatibility with future AI roles is not inferred from versioned JSON alone.

Use the [Core Pipeline](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md), [Product Decision Model](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md), [Minimum Useful Generality](../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md) and Naming Clarity specifications. Extend an existing semantic owner when it fits; create a report specification only if the public report/serialization responsibility genuinely cannot be owned cleanly there. Do not invent an ADR for ordinary rendering; a consequential persistence or package-boundary choice may require one.

The [existing replay proposal](../proposals/2026-09-08_RUN_RECORDS_EVIDENCE_PRESERVATION_REPLAY_AND_RECOVERY_PROPOSAL.md) informs alternatives, not an accepted schema or storage decision.

## 3. Proposed report contract to resolve before Build

The following are design requirements to evaluate and promote, not already implemented public fields:

| Report concern | Required design decision / proof |
| --- | --- |
| Exact identity | Repository, PR, base/head, dependency transition and relevant observed revisions remain distinguishable |
| Findings | Material meaning and supporting evidence; candidate, grounded interpretation, observation and applicability are not flattened |
| Coverage/availability | Supported, unsupported, not evaluated, not activated, no admitted candidate and unresolved outcomes remain distinguishable where material |
| Runtime strength | Static consumption, runtime correlation and command-completion package state retain their separate propositions; no implicit later-use/behavior claim |
| Unknowns | Explain material uncertainty and its consequence; empty projected uncertainty is not global closure |
| Next checks | Only producer-grounded, discriminating proposed checks with interpretation and stop/re-entry logic; allow no justified check |
| Actions | Existing admitted action or explicit unavailable/not evaluated synthesis; do not manufacture non-abstention or represent operational failure as semantic abstention |
| Sources | Recoverable references of correct evidence class, with explicit missing source content rather than fabricated citations |
| Saved result | Named schema/method version, run identity, exact input/configuration identity actually available, output integrity and explicit unsupported/corrupt versions |
| Failure/exit behavior | Result printed, partial result, acquisition failure and action disposition must not be confused |

Do not require every output to have a finding or check. Honest limitations can pass faithfulness while failing usefulness. No report field may claim producer facts that the investigation did not retain; either record that absence or admit a precise producer-retention change.

## 4. Design and implementation sequence

### Design normal PR-description preservation and source inspection when justified

Entry: source-aware task review demonstrates material context in normally acquired PR responses that current product consumers lose, and identifies a concrete offline/source-inspection or downstream-consumer obligation. Use [the October23 retained-case review](../working-memory/evidence/2026-10-23-maintainer-task-development-review/REVIEW.md) as exposed development evidence, not an independent utility result. Compare this bounded enabling increment with opening the ordinary PR and with the existing [API/source-examination trial](UPSTREAM_API_CHANGE_AND_TARGET_EXPOSURE_FEASIBILITY_PLAN.md); do not add a second acquisition graph or weaken publisher authority.

The included capability is preservation and usable inspection of attributed PR description text. It excludes automated change meaning, exhaustive release coverage, target exposure/applicability, a new check/action, full raw-response archives and general replay. This is a temporary enabling boundary inside the broader report/interpretation responsibility. Re-enter semantics or additional acquisition only when the accessible text leaves a concrete missing premise and a bounded method/question is selected.

The concrete producer, representation, failure, native/report compatibility, offline access and acceptance design is [§10](#10-pr-description-preservation-and-offline-source-inspection-design). Reconcile a stronger owner only where its responsibility changes; this design uses the existing Core/Workspace method. Source/test implementation and new inference/acquisition require separate authorization. Live entry and the chosen responsibility belong only in MEMORY.md.

### Establish the baseline and proof boundary

Capture the current CLI output under exact declared input conditions. Freeze a product/case identity manifest separately from expected findings and forbidden claims. Use existing development cases as such; do not call them blind or protected once their conclusions informed design.

Inspect `PublicPullRequestInvestigation`, `cli.py`, `maintainer_action.py`, their focused tests and the normal evidence producers. Record which facts exist but are not presented, versus facts unavailable to the producer. Include runtime-state and static-only CI boundaries.

### Settle projection and preservation ownership

Prefer a faithful projection over the existing typed investigation. Presentation cannot rerun parsers, establish applicability, invent checks or recreate provider authority. Share the semantic result between human and saved output rather than maintaining two inference paths.

Choose an explicit serialization boundary; do not blindly serialize every dataclass or freeze internal type shapes as a public API. Compare inspectable file export with storage only where real query/lifecycle needs exist. Define schema-version compatibility, incomplete writes, result identity and redaction at that boundary.

Reopening a saved report must make its observation time/revisions and stale-now status understandable. It must not make live requests or imply fresh validation. Full deterministic replay requires recorded recomputation inputs and a separately admitted gate.

Promote settled framework-independent semantics and consequential methods before Build follows. Stop here if an owning decision is unresolved.

### Implement only after authorization

Expected edit anchors: `src/upgradepilot/cli.py`, the typed investigation consumer boundary, and `src/upgradepilot/maintainer_action.py` only if uncertainty/action projection changes are selected. Keep `investigation.py` orchestration-only unless precise input retention is independently necessary. Introduce a responsibility-named report module only when real implementation needs it; no speculative package tree.

Relevant existing tests: `tests/test_cli.py`, `tests/test_maintainer_action.py`, `tests/test_investigation.py`, and runtime-state composition tests where that seam matters. Add serialization/reopening tests at the actual implementation owner once admitted.

### Verify normal producer and consumer composition

Required contrasts:

- normally produced supported evidence with material findings;
- static-only CI and an admitted command-completion state, preserving different proof strength;
- unresolved runtime semantics and no admitted runtime candidate;
- semantic-provider unavailable/no claim/invalid claim, kept distinct;
- unsupported dependency transition and acquisition failure before result formation;
- artifact applicability unavailable at the exact target-evidence boundary;
- saved result reopened offline, malformed/version-incompatible input and interrupted publication.

Use fixtures to isolate a state; they do not prove normal acquisition, public prevalence or independent user benefit. A fixture-built positive runtime witness is labeled controlled proof. Obtain representative normal-path evidence for externally claimed product coverage, or record that debt.

Run focused checks first, then the justified product regression and installed CLI checks. A renderer need not require fresh model inference unless semantic-provider behavior changed. No tool/experiment result becomes a product pass.

## 5. Independent usefulness evaluation

### Separate evaluation questions and readiness

Reuse [the report development evaluator](../experiments/EVIDENCE_REPORT_DEVELOPMENT_EVALUATION.md) and its [case manifest](../experiments/evidence_report_development_cases.json) as development material. Assistant-authored labels, richer simulation interpretation and synthetic calibration need review; they are neither independent user results nor unseen cases. Revise executable evaluation machinery only under separate authorization.

| Question | Comparator / evidence | Readiness and limit |
| --- | --- | --- |
| Faithful implementation/migration | Original versus revised/direct/recovered report under equivalent native inputs, fixed time and declared generated-ID normalization | Product/consumer proof under the Workspace plan; equal reports alone establish no user benefit. |
| Faithful presentation of supplied context | Declared curated packet versus report; preserve all supplied interpretation and scope disclosures | Development presentation review only. It cannot establish normal acquisition, extraction or discovery. |
| Source-aware development task review | Analyst-reconstructed answers from the same frozen normal sources versus actual report support, omissions and source access | May be performed by the assistant when selected; expose implementer/label overlap and prior case knowledge. Supports diagnosis/prioritization, not independent utility or untreated task performance. |
| Maintainer usefulness | Ordinary PR/CI/release-note/source review versus report-assisted review with equivalent decision-time source information | Exact normal producer outputs, comparable source packets, reviewed tasks/labels and independent reviewers. Can begin before Workspace completion or positive action admission. |
| Post-cutover usefulness change | Reuse the frozen utility protocol where inputs/capabilities remain comparable | Separate from native parity; new lifecycle display/context cannot be assumed helpful. Mark changed evidence/modes and refreeze if comparison changes materially. |

Prepare/freeze the protocol as soon as case feasibility is known. Do not delay the utility question until every future Workspace feature is complete. If representative existing reports meet readiness, explicitly select their study or record a reasoned deferral. Neither plan automatically launches acquisition/inference or recruits/messages reviewers.

Assistant review is a permitted development mode when selected; it does not replace the independent pilot below. Do not invent a blind baseline, time-saving result or independent adjudication by having the same informed assistant answer both conditions. Preserve source-only answers as analyst reconstructions, check actual omissions as well as faithful claims, and retain no-benefit/inconclusive judgments. Further engineering may follow a separately authorized concrete gap without pretending independent usefulness has passed.

Before freezing a utility task, distinguish a fixed-retained-input report comparison from ordinary open-ended PR/CI/release/source review. The former can isolate assistance over a declared information set; it does not establish benefit over unrestricted maintainer discovery. Disclose navigation/access differences and keep source affordances comparable. Normally acquired PR descriptions may already contain copied release context even when stronger upstream publisher provenance is unavailable; inspect the actual packet rather than treating the stronger refusal as absence of all source text. Copied context retains its own attribution/coverage limits.

The [Investigator integration/evaluation handoff](INVESTIGATOR_INTEGRATION_AND_COMPARATIVE_EVALUATION_PLAN.md#8-future-responsibilities-activation-and-closure) is an explicit readiness review point, not a prerequisite that this study must wait for. Distinguish its laboratory proposal-quality/reviewer-effort evidence from this plan's actual normal-product maintainer task comparison. When selecting the next responsibility, record feasible normal reports, equivalent source packets and independent reviewer availability, or the exact missing condition and re-entry trigger in MEMORY. Do not infer an absent reviewer from a lack of outreach, and do not contact anyone without authorization.

### Freeze a feasible normal-product pilot

Matched source/report preparation may precede study readiness as a separately bounded developer diagnostic. Observe the existing normal producer's requests and consumed response bytes; retain the normal report separately from the ordinary-review source packet. Record partial/unread/failed inputs explicitly, preserve streamed error semantics, and do not build a baseline from report conclusions. Diagnostic budgets or unadmitted model access must stop capture rather than manufacture a normal provider failure. Keep decoded bodies private with public-safe hashes/receipts and bind the exact code/case/identity/limits before live execution. This preparation does not require a new public report schema or imply replay, semantic acceptance, independent labels or a started utility study. Existing producer/client seams are implementation options, not a requirement to change domain owners.

Before generating comparative outputs or observing reviewer answers, record one public-safe study manifest in the selected cycle's evidence directory. Include the following, with immutable output/input hashes added when actually produced:

| Manifest group | Required contents |
| --- | --- |
| Claim and mode | Bounded development usability/utility question, normal versus curated mode, supported capability subset, proposed adoption/rejection consequence and explicit unearned claims. |
| Cases and inputs | Repository/PR/base/head/dependency transition, observation/capture times actually available, exact decision-time sources and lawful retained-content/reference availability, case independence and known contamination. |
| Product and baseline | Product/code/report/schema versions, actual configuration/model identity if used, complete allowed source packets and equal task/reference/time affordances. Missing identity stays explicit. |
| Oracle | Independently reviewed required findings/unknowns, material source pointers, forbidden claims and interpretation of an absent justified next check. Hide oracle/expected answers from producers and reviewers during tasks. |
| Participants and assignment | Relevant Python-maintainer/review experience, independence/assistance, case/condition/order allocation, label exposure and exclusions established before outcomes. |
| Evidence and disposition | Output/task-answer paths/hashes, observations/errors/elapsed-time method, comparability/faithfulness/utility rules, failure/refusal handling and explicit inconclusive outcome. |

Use at least three materially contrasting responsibility pressures for the initial pilot, not three near-duplicate updates: a normally reachable bounded finding with target/source scope; static versus command-completion/conditional-runtime limits; and degraded/unsupported evidence where the user must identify the missing obligation without inventing a remedy. Prefer existing retained/development cases when their actual normal producer inputs are available. CARLA/Dictare/Freqtrade simulation material may inform labels or curated review, but must not be injected into normal product inputs. The retained Pydantic/Soup Sieve support-drop subset is development grounding, not by itself a complete normal report case.

Resolve feasibility before freezing the actual cases. When the normal producer cannot supply a case's material evidence, record the gap and select a feasible contrasting case or keep the normal study unready. Do not create a new engine capability merely to fill a study quota, hide unsupported cases after seeing output, or count related artifacts as independent cases. Exact mismatched inputs are `not_comparable`; matching inputs with false output identity are a critical product error, not an exclusion.

The ordinary-review condition receives the same admissible decision-time source information, such as PR/diff, CI evidence and package/upstream texts, without UpgradePilot's derived findings or expected answers. The assisted condition receives that packet plus the actual report. Preserve access/navigation conditions and disclose if acquisition/presentation differences are part of the question. A richer report-only packet would confound information availability with report usefulness and requires a separately named comparison.

### Reviewer tasks, independence and ordering

For a bounded independent pilot, arrange at least two reviewers with relevant Python dependency-review familiarity who did not author the report, implementation or labels. Ali/assistant review remains useful development analysis but cannot be the independent result. If suitable reviewers are unavailable, preserve that debt and continue only independently authorized mechanical work.

Each reviewer sees a case once in one condition. Assign both conditions for each case across different reviewers; rotate conditions across cases and balance task/order exposure as far as the small pilot permits. Do not have one reviewer examine the same case with and without the report and interpret their learned second answer as improvement. Record experience differences and residual allocation imbalance; the small pilot supports descriptive case-level observations, not a causal population/time-saving estimate.

Ask each reviewer to recover:

1. The exact dependency transition and analyzed/source revisions.
2. The material supported finding, or the specific reason no finding is established.
3. Its source and proof strength, including static/observed/applicable distinctions.
4. The unresolved obligation that materially limits a conclusion.
5. A justified next check and how its possible observations would matter, or why no such check is supported.

Record task answers and source-navigation steps before debriefing. Elapsed task time excludes setup and is recorded by the same method for both conditions. Log requested clarification and substantive coaching; coached outcomes do not satisfy independent task recovery. Preference/confidence feedback supplements task evidence and cannot replace it. Do not add a semantic judge, model vote or new dashboard for this first manual study.

### Acceptance, rejection and inconclusive results

Report per case/condition: operational outcome/comparability; claim discipline; required finding/unknown coverage; stopping/next-check validity; reviewer task recovery; observed burden and assistance. Preserve the development evaluator's distinct failure/incomplete/not-scored meanings. Provider/model failure is operational evidence, not semantic abstention. Never pool unlike cases into one accuracy score or remove unsupported outputs from the denominator silently.

Scoped acceptance requires zero critical false/misattributed/authority-promoting report claims, preservation of all applicable required findings and material unknowns, and independent assisted task recovery without substantive author coaching. A usefulness claim additionally requires identifiable practical assistance relative to ordinary review on more than one contrasting responsibility: for example locating a material source, avoiding a specific false inference or recognizing a discriminating check. Cite the actual answer/navigation evidence and retain cases with no benefit or added confusion. Honest blanket unknowns may pass some truthfulness checks while failing useful assistance.

Reject affected output/method for critical false confidence or fabricated support. If faithful output adds no practical assistance, revise/simplify the report or investigate the precise missing producer/reasoning capability. If cases/reviewers are unavailable, inputs are incomparable or the benefit remains ambiguous, record `not_established`/inconclusive with the smallest discriminating follow-up; a polished report or positive preference is not a substitute. This pilot cannot establish population benefit, unseen semantic generalization or a percentage/time improvement without a separately suitable measured comparison.

Any rubric/case correction after freeze preserves the original record, gives its evidence/reason and applies symmetrically; no silent relabeling to pass a favored output. Later discovery/model claims require protected repository/release-family/time-separated evidence and human-adjudicated labels. Merge status and future incidents are not direct truth labels for a recommendation.

## 6. Completion, stop and subsequent responsibilities

Report the gates independently: contract/design accepted; authorized implementation verified; saved-result reopening verified; independent usefulness established or unproven. Complete this plan only for the selected declared outcome with its required gates met. MEMORY.md records the exact live stopping point.

Further entry conditions:

- deterministic replay: users/evaluation need recomputation and exact captured inputs can support it;
- discovery: material omitted changes prevent useful findings;
- coverage/runtime observation: a scoped missing fact blocks a useful conclusion/check;
- action admission: positive permission becomes normally reachable, through the synthesis owner;
- migration: a concrete breaking-change remedy has independent verification evidence.

Stop before another capability build. No database, graph, model, agent, broad resilience framework or target mutation follows automatically from a successful report trial.

## 7. First-trial contract and implementation design

This is the concrete design to review before Build; its preparation does not prove implementation or usefulness. Stable representation semantics are in [Core §6.1](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md#61-evidence-reports-and-saved-result-boundaries). Action permission remains in its existing specification. No new report specification is needed: the Core already owns representation/provenance/version/failure invariants. No ADR is needed for ordinary rendering and an inspectable file baseline using existing standard-library facilities; reassess if a consequential storage/service/package method is proposed.

### Shared semantic projection

Use one explicit projection from the admitted native investigation inputs into a responsibility-named report record. Initial delivery uses `PublicPullRequestInvestigation`; [Workspace migration](INVESTIGATION_WORKSPACE_IMPLEMENTATION_AND_MIGRATION_PLAN.md) cuts over that input to a one-way Workspace-native projection while preserving report semantics. Any temporary legacy projection has a named parity/compatibility reason, explicit loss boundary and removal trigger under ADR-0012. This report plan does not retain a second producer or define the canonical recovery schema. Human rendering and file encoding consume the same report record; offline decoding reconstructs only that report record, not domain objects or a new investigation. Do not serialize arbitrary dataclasses or Python class/import names as a public contract. Ordinary reporting adds no dependency, inference model, score, database, generic event log or agent; Workspace persistence is owned separately.

For a historical recovered Workspace, render the retained synthesis/conclusions and their basis. The normal projection's existing synthesis invocation must be separated from that historical path: Core §6.4 prohibits evaluators during recovery. Fresh synthesis under current conditions is a separately admitted evaluation, not an implicit effect of reopening or rendering history.

The report boundary may describe owned states and their consequences through deterministic, source-grounded wording. It may not recompute applicability or discover new facts. Preserve static CI consumption, runtime correlation, command-completion state, actual later use and behavior as different propositions. In particular, command completion cannot become fresh-install causality or compatibility. A no-candidate result retains its evaluated horizon; it is not global absence of impacts.

| Public report component | Required contents / initial source |
| --- | --- |
| Identity | Repository, PR, exact base/head, supported dependency transition or its explicit problem; workflow/execution revisions remain attributed separately |
| Production context | Report identifier and UTC generation time; generator method/version; declared auth mode without credential values; available product version; unrecorded code/model/config identity stated explicitly rather than guessed |
| Assessments | Named topic, owner state/reason/detail, scoped proposition, source references and limitations; support dependency, CI, runtime-state, package/artifact, upstream interpretation and target-applicability topics |
| Findings | Material established facts or attributed interpretations with assessment/source links and trust strength; candidate/grounded claim/corroborated fact remain different |
| Unknowns | Exact unresolved question, reason, relevant evidence links and its bounded consequence; absent consequence is stated as not established |
| Action | Existing synthesis result and its reasons/limits when evaluated, or explicit not-evaluated/unavailable state; no new action or check category in this trial |
| Sources | Report-local identifiers, evidence class, actual locator/identity and transformation metadata when retained, retrieval time when available, retained excerpts/content versus reference-only/not-retained state and reasons |
| Preservation limits | What can be inspected offline, what source/input content is absent, and what the record cannot recompute or establish |

Mandatory source references resolve within the report. A statement backed only by a producer's recorded problem/detail is identified as such, not falsely cited to unretained raw content. Unknown observations use explicit states/reasons; null must never imply an evidence-backed negative conclusion. Existing upstream package retrieval timestamps may be copied; report generation time must not be substituted for unavailable PR/workflow acquisition times. Report-local IDs are references, not cross-run evidence identities.

Material retention/projection review before coding:

- PublicPullRequestInvestigation contains runtime_dependency_state_result, but cli.py does not present it. Project it without rerunning CI parsers/correlation or expanding the admitted direct-requirements/pip family.
- Existing CLI prints supported_not_correlated detail, while synthesis's generic CI residual-uncertainty projection excludes that state. Reconcile shared report uncertainty against the actual typed result. If synthesis is exposed, improve its material CI/runtime uncertainty within its own responsibility; do not rely on an empty residual list as closure or silently replace permission evaluation.
- PackageReleaseEvidence/PackageReleaseIndexEvidence retain source URL and retrieved_at. Dependency source evidence retains file/extraction identity. Workflow run/job and runtime-state assessments retain scoped command/revision relationships. Preserve their different evidence meanings.
- The application result does not retain every fetched workflow/source document, provider configuration, model identity or raw response. Do not broaden orchestration to capture all of them merely to fill a report. Preserve available locators/context with explicit absence; assess retention against both current claim review and the named forthcoming consumers in §9. Select a justified retention change where an exact source/context requirement would otherwise be lost, or record its explicit capability/re-entry cost before freezing the boundary.
- Archived simulation diagnoses remain separate development evidence. No case-ID-specific reporting logic or manual expected-answer input enters product runtime.

### Saved-result representation and offline reopening

First-trial file contract: a UTF-8 JSON file with a strict versioned envelope. Version 1 has `schema` = `upgradepilot.investigation-report`, integer `schema_version` = 1, `report` = the explicit semantic record above, and `integrity` containing a named digest method and payload digest. These are the selected first-trial external names; future incompatible changes require explicit version handling.

Digest definition: SHA-256 of the UTF-8 encoding of the canonical JSON object containing schema, schema_version and report; sorted object keys, compact separators, ensure_ascii false, no NaN/Infinity. The digest field itself is excluded. Formatting whitespace outside the canonical payload is not an authenticity signal. Ordinary file corruption may be detected; someone editing both payload and digest can still fabricate a file. Neither digest nor schema validity supplies source truth.

Decode with non-executing JSON parsing and explicit shape/type/semantic-reference validation. Reject duplicate object keys, non-finite numeric values, unsupported schema/version, missing required components, invalid enum/state combinations, dangling references and digest mismatch with an informative file-validation error. Do not deserialize arbitrary objects or silently migrate unknown versions. Choose proportionate input-size/depth limits in implementation under SECURITY.md; demonstrate the applicable malformed-input contrasts.

Reopen offline through the same human renderer. Clearly mark saved-result mode, recorded generation time and analyzed revisions, and that no live refresh occurred. A source locator may be shown but not fetched automatically. Generating a new report ID or replacing recorded identity on open is forbidden. Preserve saved-generator versus reopening-renderer version separately when relevant.

Publication behavior: create a temporary sibling, encode and validate, then publish the complete file atomically without replacing an existing destination. Choose the smallest suitable primitive in Build and test collision/race and interrupted-write behavior. Cleanup only the invocation's own temporary file. A requested save that fails must return a nonzero operational outcome even if a readable report was already printed; it is not semantic abstention. No database, resume journal, raw-capture archive or deterministic replay is included.

### CLI and responsibility seams to implement after the design gate

Selected first-trial user flow: `upgradepilot OWNER/REPOSITORY PR_NUMBER` prints the human report; `--save-report PATH` also preserves it. `upgradepilot --open-report PATH` opens only the saved report. Reopening is mutually exclusive with repository/PR/acquisition/auth options; invalid combinations are input errors. Do not create a second acquisition path or require an online service for reopening.

Keep existing exit meanings: 0 means a valid investigation result was presented, not merge/compatibility; unsupported transitions may still produce a valid bounded report. 2 remains input/configuration rejection, 3 acquisition failure, 4 malformed provider response. 5 = requested file-publication failure and 6 = saved-record validation/read failure. Failed acquisition before result formation remains an operational diagnostic, with no fabricated saved semantic report. Declare changed human presentation; do not advertise byte-compatible old CLI output.

Expected bounded seams: a report projection/record owner, human renderer, explicit versioned encoder/decoder/file handling, and CLI integration. Select minimal responsibility-named files under the existing source layout during Build, avoiding a speculative package hierarchy. Existing dataclass/standard-library style is the baseline. investigation.py stays orchestration-only unless an independently justified retention gap is selected. Tests cover projection meanings, same-record human/saved correspondence, source/reference validity, offline opening, errors and atomic publication—not merely matching implementation text.

The first coherent Build outcome must include projection plus save/open composition, not an isolated polished example. Run focused projection/CLI/action/file tests, relevant integration, full deterministic product regression and installed CLI checks. Obtain declared representative normal-path evidence or record its absence; deterministic fixtures do not prove live-model quality or all case coverage.

## 8. First-trial evaluation protocol

Freeze a per-attempt manifest before comparative outputs are constructed: protocol/version, mode, cases/inputs/revisions and hashes, declared producer capability, source/output/code identities, baseline, evaluator expectations kept outside product input, reviewer/assistance/order assignment, task and rejection criteria. An unfilled reviewer or protected-input selection is explicit entry debt; do not label the study started or frozen while these are absent.

| Track | Inputs and baseline | Permitted claim |
| --- | --- | --- |
| Normal-product usability | Current CLI baseline and new report from the same retained typed result/input evidence and declared producer/configuration state; control differing live acquisitions | Whether rendering normally available evidence improves the scoped understanding task |
| Curated-evidence presentation | Declared archived packet versus alternative presentation of the same packet; manual interpretations disclosed | Organization/faithful communication of supplied evidence, not discovery or product acquisition |
| Later outcome comparison | Ordinary PR/CI/release-note review versus report-assisted review with equivalent decision-time evidence | Maintainer task benefit within the measured sample, after independent review and suitable order/case controls |

Development pressures are S001 degraded model/static CI, S002 partial normal API/context coverage and S008 artifact/fallback distinctions; S013–S016 remain supplementary controls. Existing CARLA/Dictare/Freqtrade evaluator labels can inform development review but are not independent or unseen data. Pin exact archived bytes and declared capability before use. Neither a current mutable PR nor a richer curated packet automatically matches a historical baseline. If no retained typed result supports same-evidence rendering, obtain a new matched baseline/report pair rather than reconstructing one by parsing the old log into evidence.

Reviewer task, in plain language: identify the exact update and analyzed revisions; explain the important finding and supporting source; state what is still unknown and why; distinguish proposed work from observed execution; identify a justified next step or correctly recognize that none is established. Record answers, source locations used, errors and assistance. Time may be recorded, but no speed claim follows without a comparable task and suitable controls.

The report author does not supply independent review. Ali's assisted learning answers may identify wording gaps but are labeled assisted orientation rather than independent maintainer utility. An independent evidence adjudicator reviews evidence-backed expected/forbidden meanings outside report production; disagreements remain recorded. Task reviewers must not see those expected answers before their tasks. A person who already adjudicated a case is not a blind task reviewer for that case. Counterbalance presentation order or use equivalent different case assignments, and disclose prior exposure. If the same reviewer sees both presentations of one case, record carryover and restrict the claim; do not treat the second answer as an independent sample.

Scoped acceptance: comparable inputs; zero critical false/misattributed claims; all required admitted findings, identity/source and uncertainty distinctions adequate; proposed/executed work and action availability correctly identified. Demonstrate at least one concrete task improvement over baseline without losing a material correct answer, and report case-specific failures/omissions. No averaging can hide an unsupported full HTTPX diagnosis or turn all-unknown output into a useful case pass. Existing development cases can establish scoped developmental usability, not unseen generalization. Independent utility remains unproven if reviewer access or adjudication is missing.

Rejection/re-entry: critical overclaim → repair projection/retention first; faithful but unhelpful report → identify presentation versus missing-evidence cause and simplify or select its owner; no comparative gain → do not add sophistication merely for polish; missing normally reachable action premises → retain unavailable action rather than rename it as advice. Protected cases and broader recruitment are required before broader product/model utility claims. Preserve unsuccessful attempts and frozen scope rather than retroactively excluding their failures.

## 9. Foreseeable AI use and evidence-retention review

The report trial must be compatible with credible future AI responsibilities. It does not implement those roles or claim that a saved report is sufficient to run them. Apply [Core §6.2](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md#62-foreseeable-evidence-consumers-and-ai-contributions). The [evidence/AI research proposal](../proposals/2026-09-29_UPGRADEPILOT_EVIDENCE_AI_ARCHITECTURE_PROPOSAL.md), especially its source-context and role distinctions, informs this review without adopting its complete architecture.

The named roles below are concrete design pressures, not an exhaustive product ceiling or a mandatory capability backlog. Revisit them when another credible consumer demonstrates a different information/proof need.

| Named consumer | Place in the product flow | Required information / first-trial consequence | Separate future gate |
| --- | --- | --- | --- |
| Bounded release interpretation | During investigation; existing adopted LLM role | Exact release/source text and identity, proposed interpretation, grounding/authority and unresolved states; report preserves attribution and available supporting content | Existing extractor admission and semantic-quality proof remain separate from report faithfulness |
| Broader impact discovery | During investigation | Upstream changes and relevant target code/configuration/dependency relationships; compact report fields cannot be the only permissible context | Selected discovery outcome, richer evidence acquisition and omission-sensitive evaluation |
| Evidence-gap investigation agent | During investigation or explicitly requested follow-up | Structured findings, exact unresolved question, relevant evidence/environment/time scope, available capabilities and a grounded way to judge new observations | Explicit tool/action contracts, admission, bounded execution and state-dependent benefit; report export is not a continuation engine |
| Interactive explanation | After an existing result | Findings, reasons, source references/content and preservation limits; answers must distinguish recorded knowledge from unavailable context | Grounded explanation evaluation and explicit distinction between answering and starting new acquisition |
| Optional AI-assisted report wording | At presentation | The same material facts/unknowns/action availability as the shared report, plus enough source context to check generated explanations | Faithfulness comparison with deterministic baseline; no independent action or fact authority from fluent prose |

### Required retention ledger before public-schema freeze / Build

Record the actual producer-to-consumer path for each material information family: producing field/type and exact identity; retained content versus reference-only/unavailable state; named human/AI consumer need; access/retrieval responsibility; what the first exported representation will retain; the cost and re-entry condition of each omission. This ledger belongs in the active design cycle record, with stable semantic conclusions promoted to Core. Do not create a competing generic metadata owner.

Source-grounded starting pressures:

- PublicPullRequestInvestigation retains immutable PR revisions and typed results. Retain identities and structured state/reasons; do not make readable prose the only interface for later reasoning.
- AuthoritativeUpstreamIntervalEvidence and TaggedChangelogEvidence retain bounded authoritative source material; GroundedUpstreamClaimSource includes an exact quote and offsets. Review preserving the existing relevant text or scoped excerpts and their identities rather than replacing them with an interpretation alone. An excerpt declares its range and omitted context; it cannot stand for the whole document. The report's human summary can remain short while the owned supporting record remains richer.
- Current CI/runtime assessments retain scoped execution/consumption evidence but not every original workflow document/log. Name those absences. A later gap-planning or temporal investigation may need a distinct source-acquisition/retention responsibility; no static result alone supplies it.
- Current target/artifact and package records contain useful scope, metadata and source facts, not arbitrary repository code or an observed source-build result. A future code/context investigator must obtain that missing context under its own source/authority boundary.
- Provider/model configuration, full prompts/raw responses and operation history are not a complete retained orchestration trace. Capture specifically necessary input/method identity when that responsibility is selected, without secrets or unrelated data. Do not retroactively invent provenance or advertise restart/replay from a report ID.

Before discarding relevant content or publishing a schema, decide each named requirement visibly: retain already-owned content; add a precisely justified producer-retention change; provide an exact retrieval reference with its availability limitation; or defer with the affected capability and re-entry trigger. A blanket all-raw archive and a blanket summary-only policy are both inadequate substitutes for this review. Versioning supports later evolution but cannot restore evidence already lost.

### Boundaries and proof consequences

Investigation, evidence acquisition, model interpretation, proposal admission and presentation remain separate responsibilities using their existing owners. Models may receive progressively richer relevant context; their outputs still need source/identity checks and honest interpretation-strength labels. Tool execution is admitted by its action/security boundary. No framework-specific tool shape, agent framework, database, global planner interface or new final-action authority is selected by this compatibility requirement.

Later inquiry creates a separately identified result with an actual predecessor relationship where available, preserving the earlier output. Such linkage is not implemented resume/recovery or a mandatory new run-history service. Saved-result reopening stays offline. If raw/source retrieval is required, use a separately explicit investigation path with revalidation and record missing/changed evidence rather than silently replacing the recorded facts.

Add meaningful first-trial implementation proof at the chosen seam: a non-rendering consumer can obtain structured finding/unknown/source identity without prose parsing; retained excerpt/source ranges remain attributable; reference-only records disclose unavailable content; offline reopening cannot overwrite or refresh an earlier saved record; no model-derived proposal gains authority just by serialization. If later inquiry/lineage is selected, separately prove that its new result preserves the earlier record and that the predecessor relation is actually established. These are evidence-consumer boundary tests, not claims of implemented agent behavior. First-trial acceptance remains report/save/open faithfulness plus separately measured usefulness; each later AI capability needs its own input and outcome proof.

## 10. PR-description preservation and offline source inspection design

### Consumer, benefit and scope

The first consumer is a maintainer reopening the named saved report after live sources have changed or become unavailable. The concrete benefit is inspecting the exact PR description supplied to that investigation, alongside its attribution, without refreshing a PR URL. The existing PR page is the simpler adequate online alternative; it cannot provide this saved observation offline. Later structured investigators may consume the retained source under their own admission, but this increment neither enrolls a new model source nor changes semantic methods.

Deliver one path: normal PR observation → bounded description record → native capture/Workspace → existing report source → version1 save/open → explicit text inspection. Source access is the accepted bounded responsibility; utility and automated change understanding remain unproved. Broad API/support interpretation, target discovery, checks/actions, general raw-response archives, checkpoint UI/full migration, refresh and replay are excluded. Re-enter them only for a material missing premise and separately selected proof.

### Producer and description representation

Keep `PullRequestIdentity` and its codec-v1 fields unchanged. In the existing [PR provider](../src/upgradepilot/github/pull_request.py), use `get_pull_request_observation` for normal input preparation, returning a provider-owned `PullRequestObservation(identity, description)`. `description` is a `PullRequestDescriptionObservation` with the fields below. Keep the existing identity-only `get_pull_request` for real current callers/final coherence checks, sharing the endpoint acquisition/identity parser; neither route stores hidden last-response state. Normal preparation replaces its first identity call with one observation call, not both. Update injected normal-path client fixtures explicitly; do not add a silent fallback or another request when a caller has not supplied the new observation contract.

| Description field | Meaning |
| --- | --- |
| `state` | One of `retained`, `empty`, `missing`, `null`, `invalid_type`, `invalid_text`, `over_limit`; describes the returned `body` field, not release semantics |
| `text` | Exact decoded JSON body string only for retained/empty states; never normalized, interpreted or shortened |
| `source_url` | Validated requested PR API endpoint constructed by the provider; not an arbitrary URL supplied in the description |
| `observed_at` | Timezone-aware UTC completion of that PR response interpretation, with an injectable/fixed clock in tests; not report generation time or upstream publication time |
| `content_sha256` | SHA-256 of the decoded body's UTF-8 bytes for retained/empty states; not a digest of raw API JSON or a source-authenticity claim |
| `utf8_bytes` | Exact UTF-8 length when calculated; unknown is null, never a fabricated zero |

The wrapper binds description to the same initial response's identity. The existing final PR read still checks base/head/count around changed-file acquisition. It does not replace the first description, compare descriptions, add a request, establish atomicity or freeze text merely because the head is unchanged. A same-head description edit is a different observation, not a stale commit file or automatic continuation event. No update/retry capability is added.

Initial retention cap: **262,144 UTF-8 bytes (256KiB)** for one description. This covers the two observed inputs with ample room but is a product bound, not an asserted GitHub maximum or prevalence result. Reject retention when character count already exceeds the byte cap; otherwise strict UTF-8 encoding uses at most four times that cap before checking actual bytes. Do not allocate a second unbounded encoding of a clearly oversized body. The limit bounds additional description retention, not the existing HTTP/JSON transport's total memory. Reassess on representative refusal evidence rather than truncate or silently raise limits.

| Provider outcome | Retention and downstream behavior |
| --- | --- |
| Valid nonempty body within cap | `retained`; exact text/count/hash |
| Empty string | `empty`; retain `""`, byte count0 and the empty-text digest; whitespace-only text stays nonempty and unchanged |
| Absent `body` key / explicit null | `missing` / `null`; no text/hash/count, with distinct explanation |
| Non-string / non-UTF-8-encodable string | `invalid_type` / `invalid_text`; no coercion, replacement characters or retained text/hash |
| Body above cap | `over_limit`; no prefix/hash; retain byte count only when actually calculated |
| Failed request, invalid outer JSON or invalid required PR identity | Existing acquisition/response failure propagates; do not invent a description-only success or semantic abstention |

For source-field problems, valid identity/dependency/CI/package evidence can still proceed. No partial-description state is emitted: either retain the full decoded field or explain its absence. A complete PR body may itself quote truncated upstream notes, as OpenCV does; retain those original markers and state that upstream coverage is unassessed. Do not infer source completeness or semantic meaning with keyword rules. Record validation checks only these representation/identity invariants, never whether the described change is true.

### Native transfer and compatibility

`AcquiredDependencyInputs` carries the description observation once to initial native capture. Add **`pull_request_description` codec1**, owned by `github.pull_request`, with `investigation_inputs` as its sole input binding. Its explicit layout encodes the new description record or null for a not-recorded/not-evaluated capture. Do not modify existing `investigation_inputs`/`pull_request_identity` v1 layouts, envelope/store schemas or existing native-family input edges. Extend existing explicit layouts/capture/projection modules; no new package, generic raw archive, global version manager or framework.

Capture this source observation for supported and unsupported dependency results. An optional description argument on direct native-capture callers means explicitly not recorded, not an empty PR body. Normal provider observations always supply a concrete record, including source-field problem states. Use current producer-method/unknown-semantic-version rules; codec1 is not a newly invented producer version. Existing CI/Python source closure and default experimental native offering do not gain a dependency on the description.

Add a focused offline description projection under [native projection](../src/upgradepilot/workspace/native_projection.py). It validates existing target/reference/material closure and reconstructs only required input/description families. A historical boundary without the new family returns **not recorded** without supplying a current default body. A present unsupported description codec/method version refuses that affected projection explicitly. Existing unrelated projections remain usable. Wrong target, corrupted bytes or broken material closure remain integrity refusals; do not downgrade them to an absent description or fetch replacements.

The full report reads this source directly from `PublicPullRequestInvestigation.workspace_revision`. **Do not add another description field to that legacy result.** No Workspace revision or no recorded family means not recorded. An explicitly unsupported optional description projection becomes scoped source unavailability in the report, preserving unaffected legacy findings; catch only the admitted unsupported-version refusal reasons, not corruption/target/basis errors. Integrity refusal stops report construction and produces a clear projection error (CLI exit8), never a fabricated abstention. These failures differ from a recorded malformed/over-limit source-field problem, which does not invalidate the canonical boundary.

### Report and human access contract

Enrich the existing PR `ReportSource` rather than allocate a competing source or new semantic assessment. Keep kind `pull_request`; for retained/empty observations use existing `retained_text` and `content`. Keep the human PR locator and original PR identity facts; add description state, observed API URL, available byte count/hash, and actual observation time through existing source metadata. Method/limitation text identifies the initial PR `body` observation and its unverified/copied/coverage limits. Problem/not-recorded outcomes remain reference-only with their precise reason. They do not become a Python/API finding or change an upstream authority result.

Keep public report schema1 and its digest definition: all chosen fields/kind/retention values already exist. Use generator version2 for the changed source projection and renderer version2 for its new availability cue; these are method/display identities, not schema or model versions. Preserve old generator identity on decoded files. A newer renderer may identify itself while preserving recorded historical meanings. Existing report-file limits continue to apply; no content may be dropped to fit a failed save. Whole-report integrity does not authenticate user-edited source facts, and the viewer adds no second semantic validator.

The normal report lists the source's retained/reference-only state and a short attribution/access cue. It does not print a long description by default. The usable flow is:

```text
upgradepilot OWNER/REPOSITORY NUMBER --save-report PATH
upgradepilot --open-report PATH --show-source source-1
```

`source-1` is illustrative: use the actual report-local ID listed by that report, never a permanent PR-source ID contract. Saving remains opt-in. A normal run without `--save-report` retains no durable source file; its cue must not suggest otherwise. The source view accepts an exact ID from that saved record, not an index/path/URL to open or execute.

Implement `--show-source SOURCE_ID` only with `--open-report`. Existing open/report/auth/save exclusivity still holds; misuse exits2 before network/provider work. Read and validate the file first: malformed/incompatible/integrity-invalid file exits6 under the current contract. Unknown ID or a reference-only/producer-result source has no retained original text to inspect: explain and exit7 without network. Empty retained text succeeds and is explicitly identified as empty; successful retained-text display exits0. Inspection makes no writes. The existing source list is sufficient; no additional listing/export/browser interface is selected.

Put source lookup/rendering with [report rendering](../src/upgradepilot/report.py), with CLI owning argument/exit integration. Reuse display sanitization for headers and body. Show report/source identity, recorded time/locator, retention and limitations, then an explicitly delimited **literal source-text view**. Preserve line feeds/tabs and remove nonprinting terminal controls in the display; keep saved text/hash unchanged and disclose sanitized display. Render HTML/Markdown as inert literal source, without a browser, HTML engine, semantic passage selection or URL following. This explicit inspection can contain original HTML markup; the prohibition on raw HTML dumping applies to the ordinary summary. A polished HTML-to-text reader is deferred unless actual source-inspection feedback justifies it. Future consumers may use `ReportSource.content` without prose parsing or extra authority.

### Build scope, verification and stopping outcome

One coherent Build covers provider observation, shared preparation/native capture/codec/projection, report source mapping, offline viewer/CLI/help and directly relevant tests/README. Update the Workspace family ledger by reference; do not migrate all report/synthesis families or import experiment/tool code. The saved source and native record have different concrete inspection/recovery consumers; each representation earns its own boundary. No dependency, live capture, model invocation, target execution, new action, semantic keyword interpreter or automatic retry is required. Retained-case proofs use controlled provider inputs with clear fixture labels; they do not reopen an official acquisition batch.

| Required proof | Discriminating checks |
| --- | --- |
| Existing normal response → consumer | Replay the two retained **PR response shapes as controlled client inputs**, not an investigation replay claim; exact description/observation identity survives normal preparation/native capture/full report/save/open/source view, with zero added requests and unchanged non-source domain findings/action |
| Native publication/reconstruction | New description survives existing checkpoint storage and a fresh process with provider/model/evaluator entry points forbidden; reconstruction does not depend on live objects. An old captured boundary still supports its existing projections and returns description not recorded |
| State/capacity | Nonempty/empty/whitespace/missing/null/wrong type/invalid Unicode; byte-exact cap and one byte above; Unicode encoding; no prefix/hash-as-full-body; a recorded problem leaves valid other branches intact |
| Mutability/basis/version | Same base/head with different first/final body retains the first timestamp/hash; changed base/head/count still refuses. Wrong target/refs/digest refuses; unsupported optional codec stays explicit; old v1 layouts/records are unchanged and unrelated CI/Python projections remain supported |
| Report/CLI/offline | Schema1 round trip; six historical reports still reopen with original bytes untouched; new retained PR text is inspectable with the unchanged schema decoder. Source ID/retention errors7, file errors6, misuse2 and integrity projection error8 are distinct. No acquisition/synthesis/evaluator calls or file writes occur during source inspection |
| Display and authority | Exact stored HTML/Markdown/line endings/control characters round trip; displayed controls are inert. Default summary stays bounded and excludes body; explicit view exposes source text/limits, including copied instructions and truncation markers, without semantic promotion |

Run focused provider/native/report/file/CLI proof first; then the full deterministic product regression because shared normal acquisition/native composition changed. Recheck relevant experiment/diagnostic consumers only where signatures/source integration changed. Verify the installed CLI/help/source-view path in a temporary supported environment, recording actual setup and network/install boundaries; no hosted run is automatic. Preserve original capture/source/report bytes and distinguish new controlled results from prior official acquisitions.

Accept this increment only when a maintainer/non-rendering consumer can recover the retained description and its limits from the saved record, including offline, while all unrelated meaning/action boundaries remain intact. Reject or repair lost text, inaccessible JSON-only content, ambiguous empty/missing states, false completeness, unsafe display, implicit refresh or unsupported authority. Passing this gate establishes bounded source access, not independent usefulness, API/Python interpretation accuracy, target impact, compatibility, full recovery/replay or learner mastery. Stop after this declared capability; the next consumer/semantic/case responsibility needs its own selection.
