# Upstream API change and target exposure — feasibility plan

**Status:** Prepared bounded execution plan. Planning selects the design/proof route; executable trial Build requires its own authorization. Product adoption is conditional on the gates below.
**Responsibility:** Evaluate an ordinary public-PR → upstream change → exact target exposure → conditional proposal path, preserving source bases, coverage and missing premises.
**Method:** [ADR-0011](../docs/architecture/ADR-0011-explicit-source-association-bases-and-proposal-boundary.md).
**Other owners:** [Core](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md), [Product Decision Model](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md), [Minimum Useful Generality](../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md), [Security](../SECURITY.md), [report usefulness plan](MAINTAINER_REPORT_PRESERVATION_AND_USEFULNESS_EVALUATION_PLAN.md).
Live selection/results belong only in [MEMORY.md](../MEMORY.md).

## 1. Outcome, scope and proof classes

Deliver a reproducible isolated trial which starts from repository/PR identity and normally acquires a useful source-linked API change/exposure proposal or an explained unresolved result. Normal means ordinary acquisition within the trial, not adoption into the public product CLI. Preserve the unchanged product baseline report for comparison.

The full product responsibility includes broader behavior, artifact/environment and runtime impacts. Initial explicit API argument removal is an end-to-end proof category with a general change-interpretation method. Other observed release changes must remain visible as observations or explicitly unassessed coverage; do not filter the window to the expected argument. Full resolution, dynamic Python, arbitrary behavioral effects, target install/test/build, migration actions and adaptive agent execution are deferred until a material case and proportional proof justify them. They are not removed from the product horizon.

Keep these distinct: acquisition/identity proof; deterministic boundary tests; assisted development semantic review; normal trial reachability; protected/independent semantic admission; maintainer usefulness; product integration. A passed test or all-unknown result cannot pass all those gates. Independent report usefulness still requires the report plan's reviewer/adjudication protocol.

## 2. Allowed homes and representation contract

Use one cohesive responsibility in `experiments/` with meaningful tests under `experiments/tests/`. Reuse `src/upgradepilot/` providers and semantics only where the contracts match. Do not modify current resolver authority, support-drop prompt/role, normal investigation behavior, report v1 schema or product action permission to make this trial work. A justified reusable product-provider change must be separately admitted and proven before this plan relies on it.

Trial records must expose:

| Record | Required information |
| --- | --- |
| Input/run manifest | Exact PR/base/head/dependency; mode; code/provider/model/prompt/schema identity; time/auth mode; limits, costs, failures and case role |
| Association/examined source | Basis and eligibility; exact release/metadata/distribution scope; candidate declarations/conflicts; pinned repository/commit/path/text/hash; covered releases and omitted/unavailable scope |
| Change proposal | Source IDs/quotes/ranges; affected interface and attributed change kind/time/direction; uncertainty; no model-selected authority |
| Target context/proposal | Exact source identity; static import/call/declaration facts; requirement constraints/extras/markers; separately attributed proposed relationships; adapter version/sample scope; unresolved resolution/activation |
| Conditional impact proposal | Change/exposure/activation/consequence premises and supporting/refuting/missing evidence; explicit alternative-path/coverage limits; proposal strength rather than invented applicability |
| Trial summary | Findings and useful unknowns with reasons/source references; unassessed observations; no new action permission or claim of accepted product report compatibility |

Source references are producer-assigned. Validate exact recovered quotes/ranges, identities and all cross-references before accepting structured output. Grounding does not prove meaning. Preserve contradiction or missing support as a result, never by editing source/expected labels to fit the model.

Retain bounded public-safe acquisition/manifest/outcome evidence under dated `working-memory/evidence/`; keep raw prompts/responses and rejected archives local. Preserve or exactly recover the semantic input and template/method identity needed for review with disclosed retrieval limits. Retain attribution/license notices when distributing excerpts. No universal raw archive or prose-only evidence store is required.

## 3. Cases, baseline and frozen evaluation entry

Before inspecting trial model output, freeze exact source/input IDs, roles, expected/forbidden propositions and omission checklist outside producer inputs. Labels may select evaluation cases; they may not supply target paths, adapter names/versions or semantic answers to the normal runner.

- HTTPX `0.27.2 → 0.28.1` in the existing Kubernetes dashboard API case is known development material. Resolve the archived exact base/head through ordinary providers and declare any drift. Required window observations include `app`/`proxies` removal, the distinct SSL deprecations and visible behavior-change coverage. Distinguish attributed release prose from independently proved API/code facts.
- Soup Sieve/Pydantic is an existing stronger-route/support-drop and report continuity control. Reuse valid dated baseline evidence or run an explicitly fresh equivalent baseline; do not compare different source/model inputs as method effects.
- Freeze a second real Python release/target API case before broader semantic claims. Select for a different interface/target form, source availability and inspectable ground truth, not because a model already succeeded on it. If unavailable, label that variation debt and withhold general admission.
- Add bounded same-meaning and changed-meaning controls: paraphrase; deprecation versus removal; future/negated/added change; different subject/version; multiple observations; empty/ambiguous source; instruction-like text; malformed/truncated output. Prefer authentic real excerpts; constructed controls remain labeled constructed.
- Include direct/alias target calls, framework-mediated calls and absent CI. Old/fixed/unknown adapter-version controls may use exact supplied packets as calibration; they cannot substitute for normal adapter discovery or prove the actual target's resolved version.

Compare acquisition routes separately from interpretation methods. For an interpretation comparison, supply equivalent source/context. Baselines are the existing product route and mechanically observable facts (e.g. a scoped signature difference) where available; fixture phrase rules or caller-supplied diagnoses are not credible product baselines.

## 4. Execution sequence

### Establish identity and operational entry

Record source/test/code state; define public anonymous or explicitly authorized token mode; inspect reusable environment facts. Freeze the responding local model/deployment/template/structured-output configuration and effective context capacity. Start with the maintained local model as an evaluated pilot, not inherited ADR-0006 API adoption. No cloud fallback/model replacement/automatic retry is admitted. Credentials are never retained in manifests.

Initial explicit limits are operational controls, not semantic acceptance scores: 50 GitHub requests per case, 200 target Python files, 2 MiB aggregate target text, 1 MiB per repository text response, 10 crossed releases, two dependency/adapter hops and four version-specific adapter samples. Inventory acquisition must disclose provider truncation, examined files and omitted paths; count-based exhaustion cannot prove absence. Distribution sampling, when needed, is capped at 10 MiB download and 1 MiB metadata member. Local inference is serial, temperature 0, seed 0 and at most 1,536 output tokens per call. Respect the effective context capacity (initial maintained baseline 4,096); byte/character counts do not prove token fit. Do not silently discard input or releases to fit. A limit hit records a scoped incomplete result and re-entry condition. Revise consequential limits/input selection before consuming affected evaluation outputs; retain the earlier result.

### Implement source association and crossed-window acquisition

Implement the ADR's separate declared-source eligibility/result. Test absence/conflict/malformed/unsupported/transport distinctions and optional distribution consistency. Public provider-host scope is PyPI, its distribution host and validated public GitHub/API/raw text; reject arbitrary/credential-bearing/private/local URL targets and validate redirects against provider scope. Parse metadata/archive members without execution or installation.

Resolve exact version/tag/commit/file relationships and every admitted crossed-release section. Generic version/tag normalization is allowed; package/repository-specific expected-answer mappings are not. Preserve structural ambiguity, unparseable/missing releases, quotation bounds and source coverage. Existing stronger evidence objects are not fallback containers for weaker bases.

### Acquire exact target context independently of CI availability

From exact head identity, acquire a bounded tree inventory and eligible Python/project/dependency declaration files. Use generic paths/extensions and explicit generated/environment-directory exclusions; record exclusions and read/parse failures. Source inventory/acquisition precedes relevant import/call selection, so the known `tests/test_routes.py` path cannot be supplied as an answer.

Use AST parsing for static imports, aliases and call references; preserve limitations for wrappers/dynamic behavior. Parse supported declaration forms without pretending to run a resolver; retain raw requirements and conditions for unsupported forms. Independent model relationship proposals stay attributed proposals unless separately supported. Actual resolution, installer state and later exercise remain separate facts.

Investigate framework/adapter metadata/source only from an already acquired relationship and discriminating question. Version-specific evidence must come from exact justified versions or openly labeled exploration samples; unpinned/ranged constraints do not become a resolved version. Sampled old/fixed branches do not exhaust a range. If normal acquisition cannot supply a necessary adapter relation, preserve that premise and treat the normal-path exposure goal as incomplete; do not inject the known Starlette story.

### Implement bounded change interpretation and proposal composition

Freeze a trial-specific structured contract/prompt before its output. Use a source-only local LLM call for general attributed change observations; evaluate explicit argument-removal meaning first while preserving other observations and unknowns. If additional target relationship interpretation is needed, give it a separately identified input/output role and evaluate it independently. Neither role has tools, external instructions, self-assigned authority, hidden correction or retry loops.

Deterministic code validates source/release identity, shape, real quotes/ranges, reference integrity and permitted effects; it does not encode the semantic expected answer. Failures remain provider/contract/grounding/semantic/coverage problems at their respective proof owners. Combine only justified same-scope evidence into mechanism-specific conditional proposals. A missing premise stays visible; the model cannot declare resolution, complete coverage, compatibility or a maintainer action.

### Verify, run real-model evaluation and compare outcomes

Run focused experiment tests for each new boundary before the full active trial test set. Run product regression/installed checks when a shared product boundary changes or trial-to-product promotion is proposed. The pre-existing unrelated experiment suite is not a substitute for this trial's proof; its known failures must remain disclosed if used.

Run ordinary PR-to-trial acquisition/output with the frozen manifest and equivalent-evidence semantic controls. Record latency, tokens/request counts, omitted content and each critical false/misattributed/unsupported claim. Review source meaning separately from JSON/schema/grounding success. Keep corrected runs separately versioned; do not relabel a failed first pass as accepted.

## 5. Pass, fail and promotion

Engineering feasibility requires an ordinarily acquired, nontrivial change/exposure proposal with actual supporting source/context and honest missing premises, plus all scoped identity/authority/unknown propagation checks. Upstream-only retrieval, a hand-built diagnosis or merely completing with unknowns is not an end-to-end pass. HTTPX may expose an unresolved actual adapter version while still demonstrating a useful supported relationship; lack of the relationship itself is an incomplete result.

Development semantic acceptance requires zero critical wrong/misattributed change or unearned applicability/action claims on the frozen bounded set, preservation of required change/unknown/omission observations and correct changed-meaning controls. Assisted source review is labeled assisted; it does not pass protected/independent semantic or utility gates. Model/proposal quality remains unaccepted when ground truth/adjudication is unavailable.

Reject/re-enter for authority casting, conflicts hidden by fallback, source/target hardcoding, missed material crossed sections or observations, wrong grounded meaning, treating declarations/samples as resolved execution, unexplained all-unknown output, validator weakening, source reshaping or development contamination presented as unseen accuracy. A source-window/context-budget failure revisits acquisition/input design before semantic conclusions.

Before product adoption: separately admit the measured API semantic role; resolve candidate/proposal authority and representation effects; migrate adopted behavior to product owners with active tests; verify ordinary product PR→candidate/report and backward-compatible saved reports; review the qualitative utility/reachability/evidence-burden/coverage/maintenance/reversibility comparison from the design draft. Independent usefulness remains governed by the existing report plan. A successful isolated trial alone does not satisfy those obligations.

## 6. Stop and handoff

Stop after the scoped trial comparison and explicit adopt/revise/reject disposition, or at a material acquisition/identity/ground-truth/proof blocker. Preserve results and the smallest discriminating next responsibility in dated evidence and `MEMORY.md`. Broader environment/marker evaluation, behavior/artifact mechanisms, runtime execution and adaptive agents require their own demand-driven scope and proof rather than automatic expansion of this plan.
