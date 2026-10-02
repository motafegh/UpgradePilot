# Maintainer Report, Preservation and Usefulness Evaluation Plan

**Status:** prepared conditional plan; not implementation authorization or a passed usefulness gate.
**Responsibility:** deliver and assess a faithful report of one normal dependency-update investigation, preserve the named result boundary, and determine whether it helps maintainers.
**Selection gate:** [Product Direction and Maintainer Utility Investigation](PRODUCT_DIRECTION_AND_MAINTAINER_UTILITY_INVESTIGATION_PLAN.md).
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

Reuse [the report development evaluator](../experiments/EVIDENCE_REPORT_DEVELOPMENT_EVALUATION.md) and its case/rubric files. Update evaluation machinery only when separately authorized. Preserve separate comparability, claim discipline, finding coverage, stopping and usability results.

Predeclare:

- normal product-output versus curated-evidence presentation mode;
- exact cases/revisions, supported capabilities and unavailable inputs;
- baseline current CLI and, for an outcome study, ordinary PR/CI/release-note review with equivalent decision-time information;
- tasks, reviewer independence, assistance, order controls and time/error recording;
- required findings/unknowns and forbidden stronger claims, hidden from producers;
- success/rejection criteria and where outputs/judgments are preserved.

Minimum scoped acceptance: zero critical false/misattributed claims, all required bounded findings/unknowns preserved, and independent reviewers correctly recover exact update, important finding, supporting source, proof limit and justified next step or absence of one. Demonstrate concrete added utility on contrasting development cases relative to baseline. Do not assert a percentage/time improvement without a suitable measured comparison. Sample size and recruitment must match the strength of the intended claim; a small study establishes bounded usability, not population benefit.

For later discovery/model generalization claims, establish protected evaluation with repository/release-family/time separation, human-adjudicated labels and decision-time inputs. Merge status and future incident history are not direct labels for a correct recommendation. Do not repurpose contaminated development cases as unseen evaluation.

If independent reviewers are unavailable, implementation/faithfulness may be verified while usefulness remains explicit debt. Do not mark the entire plan passed or block unrelated deterministic work under a falsely completed gate. If a report is faithful but adds no useful assistance, simplify/revise it or activate the precise discovery/coverage prerequisite; more polished prose is not a remedy by itself.

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

Use one explicit projection from PublicPullRequestInvestigation into a responsibility-named report record. Human rendering and file encoding consume that record; offline decoding reconstructs only that report record, not domain objects or a new investigation. Do not serialize arbitrary dataclasses or Python class/import names as a public contract. No new dependency, inference model, score, database, generic event log or agent is needed.

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

Design baseline: a UTF-8 JSON file with a strict versioned envelope. The proposed first version has `schema` = `upgradepilot.investigation-report`, integer `schema_version` = 1, `report` = the explicit semantic record above, and `integrity` containing a named digest method and payload digest. These are proposed external names to settle before Build, not an already released API.

Digest definition: SHA-256 of the UTF-8 encoding of the canonical JSON object containing schema, schema_version and report; sorted object keys, compact separators, ensure_ascii false, no NaN/Infinity. The digest field itself is excluded. Formatting whitespace outside the canonical payload is not an authenticity signal. Ordinary file corruption may be detected; someone editing both payload and digest can still fabricate a file. Neither digest nor schema validity supplies source truth.

Decode with non-executing JSON parsing and explicit shape/type/semantic-reference validation. Reject duplicate object keys, non-finite numeric values, unsupported schema/version, missing required components, invalid enum/state combinations, dangling references and digest mismatch with an informative file-validation error. Do not deserialize arbitrary objects or silently migrate unknown versions. Choose proportionate input-size/depth limits in implementation under SECURITY.md; demonstrate the applicable malformed-input contrasts.

Reopen offline through the same human renderer. Clearly mark saved-result mode, recorded generation time and analyzed revisions, and that no live refresh occurred. A source locator may be shown but not fetched automatically. Generating a new report ID or replacing recorded identity on open is forbidden. Preserve saved-generator versus reopening-renderer version separately when relevant.

Publication behavior: create a temporary sibling, encode and validate, then publish the complete file atomically without replacing an existing destination. Choose the smallest suitable primitive in Build and test collision/race and interrupted-write behavior. Cleanup only the invocation's own temporary file. A requested save that fails must return a nonzero operational outcome even if a readable report was already printed; it is not semantic abstention. No database, resume journal, raw-capture archive or deterministic replay is included.

### CLI and responsibility seams to implement after the design gate

Proposed user flow: `upgradepilot OWNER/REPOSITORY PR_NUMBER` prints the human report; `--save-report PATH` also preserves it. `upgradepilot --open-report PATH` opens only the saved report. Reopening is mutually exclusive with repository/PR/acquisition/auth options; invalid combinations are input errors. Do not create a second acquisition path or require an online service for reopening.

Keep existing exit meanings: 0 means a valid investigation result was presented, not merge/compatibility; unsupported transitions may still produce a valid bounded report. 2 remains input/configuration rejection, 3 acquisition failure, 4 malformed provider response. Proposed 5 = requested file-publication failure and 6 = saved-record validation/read failure. Failed acquisition before result formation remains an operational diagnostic, with no fabricated saved semantic report. Declare changed human presentation; do not advertise byte-compatible old CLI output.

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
