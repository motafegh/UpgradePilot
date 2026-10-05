# Broader LLM agency in UpgradePilot — research dossier

**Follow-up:** Ali selected the [local-only comparative evaluation protocol](../plans/BROADER_LLM_AGENCY_COMPARATIVE_EVALUATION_PROTOCOL.md). It turns the first-pass options below into concrete comparisons, deployment/corpus/oracle requirements and budgets. The dossier remains the original research synthesis; the protocol's dated evidence reconciles main's subsequently committed API interpreter without claiming real-model acceptance.

**Recorded:** 2026-10-05, Asia/Tehran

**Status:** Exploratory; first source-backed research pass, not a final design or adoption decision

**Baseline:** `7f1bd0ec29d13d32cc8a805d948b4dc422394d96`

**Research progression:** [working memory](../working-memory/2026-10-05_2052_broader-llm-agency-research.md)

**Authority:** research evidence, alternatives and candidate comparisons. Existing project restrictions are examined as hypotheses/migration context, not imposed as limits on idea generation. No implementation, experiment execution or architectural adoption follows from this document.

## 1. The question and provisional answer

**Which decisions in dependency-update investigation and maintainer support could an LLM or agent own more usefully than predefined logic, and what evidence would justify the delegation?**

The evidence supports testing substantially broader roles. It does not yet identify a winning UpgradePilot architecture. Useful candidates include richer fixed workflows, adaptive investigators, execution-assisted agents, independent recommendation, selective model authority, and specialist challenge. The architecture, model, context, tool interface and available observations all contribute to performance; changing them together would obscure the cause of improvement or failure.

Research should measure the costs of restriction: undiscovered issues, unnecessary abstention, inability to investigate unfamiliar cases, human work left unfinished and implementation complexity. It should also measure unsupported conclusions, wasted investigation, operational cost and review burden. Deterministic repeatability and agent flexibility are properties to evaluate against the task, not substitutes for useful/correct outcomes.

A recommendation can be evaluated independently of actual external action. This makes it possible to test wider judgment without turning an experiment into real merge/publication authority. Final product scope may itself be reconsidered after the research; the current boundary is not an answer to the architectural question.

## 2. Research method and evidence classes

The public Python dependency-update maintainer problem is the common task anchor. Distinguish:

- **Inspected source:** executable behavior visible at the exact baseline; tests express intended behavior, not freshly observed passes.
- **Recorded execution:** dated outputs/proofs examined here; no rerun or present-runtime claim.
- **Proposal/design:** an earlier hypothesis or decision; no capability proof by itself.
- **External empirical evidence:** an author-reported result in its studied setting, with transfer limits.
- **Documentation:** a supported interface/feature claim; no independent performance proof.
- **Research inference:** a candidate explanation, recommendation or experiment derived here.

Primary sources were refreshed on 2026-10-05. Read depth is explicit in §9. Selected paper methods/limitations were inspected where they can materially alter interpretation; other sources are abstract/overview-level leads. This is a broad first pass, not a systematic literature review or independent reproduction of published results.

The earlier [independent challenge plan](../plans/AI_AGENTIC_ARCHITECTURE_INDEPENDENT_CHALLENGE_AND_COMPARISON_PLAN.md) already sought de-anchored alternatives. Its historical phase labels are not this research's schedule. The [candidate refresh](../working-memory/2026-09-29_step2bx_independent-candidate-architecture-refresh.md), [whole-pipeline map](../working-memory/2026-09-29_step3_whole-pipeline-architecture-map.md), [AI reconciliation](../working-memory/2026-09-29_step4_existing-ai-agent-work-reconciliation.md), and [experiment register](../working-memory/2026-09-29_step5_architecture-decisions-experiment-queue-and-integration-strategy.md) are valuable predecessors, including conclusions this pass challenges.

## 3. What earlier UpgradePilot work actually establishes

| Prior work | Inspected evidence | What it supports | What remains untested |
|---|---|---|---|
| Adopted support-drop semantics | [extractor](../src/upgradepilot/upstream/support_drop_extractor.py), [ADR-0006](../docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md) | A narrow real model role with source reconstruction and downstream checks | Broader API/behavior discovery, repository investigation and independent recommendation |
| Minimally constrained E3 probe | [dated result](../working-memory/2026-08-28_B2-X1-E3-minimally-constrained-s001-planner.md), [probe source](../experiments/b2_x1_e3_minimal_s001_planner_probe.py) | On one real S001 state, one model response found the right evidence gap without closed actions, schema or admission | No tool executed; narrow typed state, one-step budget, no multi-action or repeated-run evidence |
| Ordinary-Python planner/control | [model boundary](../experiments/local_evidence_gap_planner.py), [product projection](../experiments/evidence_gap_product_planner_composition.py), [recorded real transition](../working-memory/2026-09-02_B2-X1-R4A4-runtime-lbd-and-reconciliation-closure.md) | One selected exact-declaration acquisition, domain-state update and deterministic consequence replay were recorded | General adaptive investigation, unknown impact discovery, broad tools and whole-journey value |
| LangGraph comparison | [workflow](../experiments/langgraph/evidence_gap_workflow.py), [focused proof](../working-memory/2026-09-06_B2-X1-R4B-first-wsl-executable-proof.md), [comparison](../working-memory/2026-09-06_B2-X1-R4B6-controlled-semantic-comparison-build.md) | Implemented graph routing and controlled comparison for the retained bounded semantics | Framework superiority, broad agent competence, persistence/resume value or product adoption |
| LLM final synthesis proposal | [proposal](2026-09-10_LLM_ASSISTED_MAINTAINER_DECISION_AND_REPORT_SYNTHESIS_PROPOSAL.md) | Thoughtful heterogeneous-evidence synthesis hypothesis | Its permission envelope preselects available conclusions; it cannot by itself test independent recommendation authority |
| September architecture research | [proposal](2026-09-29_UPGRADEPILOT_EVIDENCE_AI_ARCHITECTURE_PROPOSAL.md) and predecessor files above | Much of the scope/alternative inventory already exists | Many competitions are documented or deferred rather than empirically resolved |
| October direction research | [activation proposal](2026-10-02_UPGRADEPILOT_POST_RUNTIME_STATE_DIRECTION_AUDIT_AND_AI_ACTIVATION_PROPOSAL.md) | Broad discovery/context/API/utility questions and a parallel research option | Earlier sequencing and long-tail-only generalist placement are choices to challenge |
| Current investigation/action/report spine | [investigation](../src/upgradepilot/investigation.py), [action](../src/upgradepilot/maintainer_action.py), [saved report](../src/upgradepilot/report_file.py) | Fixed orchestration over owned evidence; action type admits only abstain; bounded saved report decoding exists | Wider recommendation usefulness, a full agent trace or general investigation resume |
| API/target-exposure preparation | [target source context](../experiments/api_target_context.py), [source acquisition](../experiments/api_change_source_acquisition.py), [ADR-0011](../docs/architecture/ADR-0011-explicit-source-association-bases-and-proposal-boundary.md) | Exact-source acquisition and conditional/static context are available research inputs | Main's in-progress uncommitted semantic interpreter is absent from this frozen worktree |

**Correction to the earlier chat:** we have tried a minimally constrained planner response, as well as tightly bounded executable planners. Within the artifacts reviewed here, this is not evidence of a broad tool-using whole-investigation agent comparison. No earlier result has been rerun in this research pass.

The [August evidence-first exploration](../working-memory/2026-08-28_B2-X1-evidence-first-llm-risk-and-design-exploration.md) also explicitly separated semantic correctness from deterministic grounding and questioned whether controls improve planner quality. That methodological lesson survives even if its historical implementation plan changes.

The [90-day plan](../plans/UPGRADEPILOT_90_DAY_PLAN.md) places advanced methods at a non-linear checkpoint; the [direction/utility plan](../plans/PRODUCT_DIRECTION_AND_MAINTAINER_UTILITY_INVESTIGATION_PLAN.md) compares action-led, advisor-led and hybrid outcomes; the [report plan](../plans/MAINTAINER_REPORT_PRESERVATION_AND_USEFULNESS_EVALUATION_PLAN.md) distinguishes preservation from usefulness; the [API feasibility plan](../plans/UPSTREAM_API_CHANGE_AND_TARGET_EXPOSURE_FEASIBILITY_PLAN.md) supplies source/exposure context. These are relevant integration/dependency clues. Their present sequencing and stop conditions are not used to veto this open research or to declare its alternatives inferior.

## 4. Complete responsibility and research coverage map

This inventory covers the relevant product path plus enabling concerns. Every row is considered in this pass, but the evidence depth differs. “Candidate” means a research inference, not a selected implementation. New areas may be added when they change a decision.

| Area | Candidate broader responsibility | Clue/evidence | Discriminating question / remaining proof |
|---|---|---|---|
| 1. Maintainer objective and product scope | Clarify the maintainer's concern, compare actions and help complete the decision | Charter; S002; P15 | Does the result improve decisions and review effort? Would remediation become a supported product outcome? |
| 2. Intake and exact identity | Interpret unfamiliar manifests/update structures and request missing inputs | investigation/dependency path | Can flexible discovery retain exact repo/base/head/package/environment identity? |
| 3. Acquisition and source discovery | Search for omitted sources and choose what to retrieve | source acquisition; ADR-0011 | Does expanded search improve coverage without misattribution or inaccessible-evidence assumptions? |
| 4. Release/API/behavior impact discovery | Infer changes beyond Python support and predefined categories | P03; P12; current API work | Does the method find important unseen effects and reject irrelevant changes? |
| 5. Repository context/localization | Follow wrappers, imports, config and call relationships | P02; P04; P05; target context | Compare text/AST search, structured retrieval, graph tools and progressive source access |
| 6. Applicability/reachability | Relate upstream changes to target use and conditional activation | S002; S011 | Can the agent distinguish source presence, actual binding, activated use and affected behavior? |
| 7. CI/environment/dependency state | Investigate temporal environment state and mismatched test coverage | G3; investigation/runtime-state fields | When do targeted observation or simulation outperform further static reconstruction? |
| 8. Adaptive investigation/stopping | Form hypotheses, invent investigations and revise them after observations | E3; R4; P02 | Does it acquire decision-relevant evidence, stop appropriately and recover from failed tools? |
| 9. Reproduction and testing | Generate a discriminating old/new reproduction or target test | P03; P11 | Is the test relevant to real target behavior, with a causal control and no answer leakage? |
| 10. Migration/remediation | Try a patch and inspect its behavior in an isolated environment | P03; P13; P20 | Does the repair address the target problem without weakening tests or creating regressions? |
| 11. Synthesis/recommendation | Own a provisional recommendation and supporting reasoning | earlier synthesis proposal; P15 | Independent recommendation vs explanation/selection under precomputed permission |
| 12. Reporting/human interaction | Prioritize evidence, offer alternatives and answer challenges | saved report; P11; P15 | Can reviewers recover the basis/limits and make a better decision rather than merely prefer the prose? |
| 13. Tools/orchestration | Use generic or specialist tools; handle branching and failures | R4; P02; P06; P07 | What tool design and lifecycle features change task quality? Framework identity alone is not the comparison |
| 14. Single/multiple agents | Specialist localization, parallel evidence collection or independent challenge | P09 | Compare equal-budget single-agent search/challenge; inspect correlated errors and lost context |
| 15. Context/memory/persistence/replay | Retrieve exact evidence, maintain hypotheses, resume after interruption | saved report; P07; P08; P21 | Can it recover omitted evidence and distinguish recorded replay from new model inference? |
| 16. Model/provider feasibility | Route suitable models and context/tool interfaces | ENVIRONMENT; P17 | Separate reasoning limits, context truncation, prompt/template, endpoint support and orchestration failure |
| 17. Untrusted content/execution containment | Read hostile evidence and run bounded experiments safely | P10; P06 | Measure useful task completion and injection effects together; container presence is not sufficient proof |
| 18. Evaluation/calibration/authority | Broader empirically calibrated semantic claims and abstention | P11; P16 | What risk/coverage and shift behavior justify relying on particular judgments? |
| 19. Cost/latency/maintenance | Allocate investigation effort and expose marginal value | P01; P03; P09 | Compare equal-budget efficiency and best achievable quality; include human review and maintenance cost |
| 20. Ecosystem/interoperability/adoption | Use external signals, standards and existing evidence alongside agents | P14; P19; P20; P21 | What transfers to public Python and what needs scope/schema/ADR/plan reconciliation after selection? |

The investigation can explore wider ecosystems, remediation and external-action architectures as options. These are product-expansion choices to discuss later, not assumed current features.

## 5. External evidence that changes the comparison

### 5.1 Agency is plausible, and the harness matters

SWE-agent studies agent-computer interfaces for repository navigation, editing and execution. It makes tool/interface quality a credible causal factor rather than treating the model alone as the system. Its issue-repair benchmarks do not measure UpgradePilot's dependency-specific decision responsibility. [P02](https://arxiv.org/abs/2405.15793v3)

OpenHands' SDK paper describes extensible tools, execution lifecycle and sandbox integration. It is a candidate harness/reference for a general investigator; the authors' architecture/deployment results are not comparative proof for our task. [P06](https://arxiv.org/abs/2511.03690v2)

LangGraph documents persistence, mixed deterministic/agent steps and human interaction. These features could matter for long investigations, but a graph runtime does not determine how much intellectual authority an agent has. [P07](https://docs.langchain.com/oss/python/langgraph/overview)

### 5.2 Simpler LLM workflows must remain credible competitors

Agentless uses localization, repair and validation without autonomous next-action selection. Its historical results show that a strong fixed LLM workflow is a serious baseline; they are not a current leaderboard claim or a finding that autonomy never helps. [P01](https://arxiv.org/html/2407.01489v2)

DepRepair is especially relevant because dependency repair crosses upstream and consumer repositories. It reports a structured-evidence, single-call method evaluated on 95 instances. Selected methods/limitations show that it significantly beats specified direct/raw-evidence baselines but only matches the strongest cross-architecture agent statistically; PyPI accounts for nine cases, and passing the test oracle does not establish behavior beyond coverage. Raw upstream text hurt studied configurations. These results motivate evidence/context ablations, not a permanent prohibition on raw-source access or a claim of broad Python applicability. [P03](https://arxiv.org/html/2607.17957v1)

### 5.3 Broader visibility should be tested as controlled retrieval

LocAgent investigates graph-guided localization; CodeRAG-Bench finds that useful retrieval can help while fetching and using the right context remain difficult. Both are reasons to compare direct search, structured retrieval and graph access. Neither establishes that we need a persistent graph/database. [P04](https://aclanthology.org/2025.acl-long.426/), [P05](https://aclanthology.org/2025.findings-naacl.176/)

Anthropic's context engineering guidance describes just-in-time retrieval, compaction and structured notes, including information-loss concerns. For our research, exact evidence locators should remain recoverable even when the agent's active context is summarized. This is an engineering hypothesis to test under interruption and long traces. [P08](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

Griffe supports comparing Python API snapshots; LibCST offers metadata-aware codemod mechanisms; CodeQL provides database/query analysis. They are potential tools or simpler competitors for specific propositions. API surface differences and transformed code still require target relevance/behavior verification. Tool use may involve execution or installation; this pass inspected documentation only. [P12](https://mkdocstrings.github.io/griffe/guide/users/checking/), [P13](https://libcst.readthedocs.io/en/latest/codemods.html), [P14](https://docs.github.com/en/code-security/tutorials/customize-code-scanning/analyze-code)

### 5.4 More agents and confident prose do not settle quality

The v3 scaling-agents paper studies controlled architectural comparisons and reports task-dependent gains/losses, coordination cost and error propagation. It supports equal-budget topology comparisons; its fitted relationships are not universal thresholds for UpgradePilot. [P09](https://arxiv.org/html/2512.08296v3)

AgentDojo evaluates tool-using agents over untrusted outputs and includes task utility as well as attack behavior. Its application domains differ from code repositories, so we need repository-specific attacks and benign cases rather than importing its rates. [P10](https://arxiv.org/abs/2406.13352v3)

The selective-prediction paper studies QA settings where entropy alone can produce unreliable abstention. This is a lead for empirical calibration and shift tests, not a justification for trusting self-reported confidence or claiming a guarantee in code analysis. [P16](https://arxiv.org/abs/2603.21172v1)

### 5.5 Maintainer usefulness is an independent outcome

The human–AI meta-analysis compares humans, AI and their combination across studies published through mid-2023 and finds heterogeneous outcomes, including losses in decision tasks. It cannot predict today's coding-agent performance; it does challenge the assumption that adding human review automatically improves decisions. [P15](https://www.nature.com/articles/s41562-024-02024-1)

Anthropic's agent evaluation guidance distinguishes real outcomes from transcript claims, repeated trials from one attempt, and capability evaluation from regression coverage. For our task, evidence support, important omissions and human decisions need separate grading. [P11](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)

Renovate's release/adoption/test signals and OSV's vulnerability-remediation workflow broaden the baseline/tool landscape. Aggregate update confidence and vulnerability removal answer different questions from exact-target behavioral compatibility. SLSA provenance describes artifact origins, not semantic correctness. These sources can supply tools/signals without becoming an outcome oracle. [P19](https://docs.renovatebot.com/merge-confidence/), [P20](https://google.github.io/osv-scanner/experimental/guided-remediation/), [P21](https://slsa.dev/spec/v1.2/provenance)

## 6. Architectures kept open

These are genuinely competing candidates. They may combine after evidence review, but are not a staged adoption roadmap.

| Candidate | Reasoning/control owner | Visibility/tools | Likely advantage | Main uncertainty | Useful comparison |
|---|---|---|---|---|---|
| A. Deterministic-heavy analysis | Mechanical/domain logic plus narrow semantic calls | Exact existing evidence and specialist analyzers | Stable facts, inexpensive routine cases, transparent behavior | Coverage ceiling and cost of handcrafted semantics | Current behavior and best improved non-agent baseline |
| B. Rich fixed LLM workflow | Models perform broader discovery/localization/synthesis; sequence remains predefined | Structured evidence with progressive retrieval stages | Broad semantics with less control complexity | Fixed stages may miss unanticipated paths | Agentless/DepRepair-style workflow on our cases |
| C. Agent-led investigator | Model controls hypotheses, searches, next actions and stopping | Repository/source/metadata tools; optional isolated execution | Adaptation across unfamiliar impact mechanisms | Evidence quality, stopping, recovery and effort | Generic investigator on routine and difficult cases |
| D. Evidence-workspace hybrid | Agent investigates; shared exact evidence supports checks and independent recommendation | Structured and raw-source views, optional verifier/graph tools | Reuse existing facts while widening reasoning | Double ownership, overconstrained admission or overbuilt storage | C with and without the existing evidence substrate |
| E. Execution-first diagnosis/migration | Agent or fixed search generates reproductions/patches; observations guide revision | Isolated old/new environments, tests and diffs | Direct discrimination of behavioral hypotheses | Test relevance, installation feasibility, environment fidelity | Static/retrieval-only vs added executable feedback |
| F. Specialist collaboration | Separate acquisition/localization/challenge roles with explicit integration | Shared evidence identities, isolated role contexts | Parallel work or deliberate counterevidence | Correlated errors, communication and reviewer burden | Same-compute single-agent alternatives first |
| G. Advisor-led interaction | Model helps the maintainer inspect alternatives and request evidence | Conversational access to sources, proposals and uncertainty | Useful support even when automation cannot settle a verdict | Human reliance and task completion | Human alone, report alone, AI alone and human+advisor |

For every candidate, recommendation authority can be varied independently from actual execution authority. A generalist agent deserves comparison on ordinary cases as well as unusual ones; restricting it to rare escalation would assume part of the answer.

Potential model roles beyond the first comparison: source selection, search-query formation, impact discovery, target localization, evidence-gap selection, reproduction design, patch generation, counterexample search, semantic synthesis, explanation and interactive clarification. These are research opportunities rather than reasons to create a separate agent for each.

## 7. Proposed experiment families

No family has been run or selected for implementation in this pass. These are experiment briefs to refine after reviewing the research.

| Family | Hypothesis / comparison | Inputs and controls | Outcome that would discriminate |
|---|---|---|---|
| X1. Broad impact discovery | Wider semantics finds relevant effects outside current categories | Frozen old/new upstream and target sources; current extractor, rich fixed model and agent | Adjudicated important-impact recall, false concerns, localization and source support |
| X2. Context access | Progressive retrieval is more useful than narrow projections or bulk context | Same model/task; typed-only, curated structure, direct progressive search, optional graph | Coverage, false attribution, context use and token/time cost |
| X3. Investigation control | Agent-selected/revised actions improve evidence gain and stopping | Same generic tools/budget; fixed workflow, offered-action planner, broad investigator | Correctly resolved questions, premature stop, wasted actions and recovery |
| X4. Executable feedback | Old/new reproductions improve a decision beyond static reasoning | Same frozen target/environment; add execution separately | Causal behavioral evidence, relevant checks, regressions and containment failures |
| X5. Independent recommendation | Model judgment adds useful actions beyond envelope-constrained synthesis | Same earned evidence; deterministic output, permitted-action synthesis, unrestricted experimental opinion | Evidence-backed action usefulness, omitted concerns and unsupported favorable recommendations |
| X6. Challenge/specialization | Separate challenge or parallel discovery adds value | Equal total compute/tools; one agent with challenge pass, independent samples, specialist pair | Incremental correct discoveries, errors caught, duplicated mistakes, cost |
| X7. Interruption/memory | Structured recoverable evidence improves resumed investigations | Interrupted traces; summary-only, exact-source retrieval, structured state/checkpoints | Preserved obligations, correct resumption, duplicate effects and missed evidence |
| X8. Selective authority | Empirical filtering can improve useful coverage at a stated measured risk | Protected calibration/test split; claim type, model/provider identity and shift cases | Risk/coverage with uncertainty intervals; sensitivity to model/repository change |
| X9. Maintainer usefulness | A richer investigator/advisor improves real decisions | Blinded/counterbalanced source-backed cases; comparable information/time | Decision quality, verification effort, critical misunderstanding and appropriate reliance |

The first software comparison should keep model, tools, case inputs and resources comparable where possible. Also report a separate best-achievable-quality comparison: strict equal budgets measure efficiency, while useful deployment may justify extra investigation. Neither alone answers both questions.

A failed local small-model trial would diagnose that configuration, not disprove agentic architecture. A strong model's success would not establish local deployability. Reasoning, provider/tool support, context capacity, prompt construction, harness failures and evaluation errors need separate classifications.

### 7.1 Corpus and oracle design

Use existing real cases as development material, including:

- [S002](../product-simulation/scenarios/S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1/CASE.md): HTTPX behavior through a framework adapter, insufficient relevant public tests, and unavailable historical resolution/logs. Retrospective records are clues, not a complete executable historical oracle.
- [S008](../product-simulation/S008_POST_CASE_SYNTHESIS.md): binary-wheel loss with source fallback; distinguish artifact transition from source-build failure.
- [S011](../product-simulation/S011_POST_CASE_SYNTHESIS.md): platform-specific optional dependency activation and missing CI environment coverage.
- [G3](../product-simulation/2026-09-22_G3_REALITY_CHECK_AMBIENT_SEMANTICS.md): temporal environment formation and later no-sync use; avoid command-local/global shortcuts.
- S001 as a simple planner control, plus unseen updates with irrelevant changes, real behavior breaks, conditional use, conflicting sources and genuinely unresolved evidence.

These cases are already exposed to development and research. Protect a separate evaluation set by repository/release-family/time separation; use decision-time evidence and preserve acquisition failures. Future merge status, a later maintainer patch or today's live repository state cannot silently serve as the historical recommendation oracle.

A development pilot of roughly 12–20 varied cases with repeated attempts could expose mechanisms. The final sample size should follow the intended precision/risk claim and observed variability. Small pilots cannot certify low rare-error rates. Include ordinary negative controls so additional concern generation is not rewarded indiscriminately.

Human/source adjudication should identify required facts, acceptable alternative investigations, irrelevant changes and truly unknowable propositions. Executable old/new checks provide a scoped behavioral oracle; independent hidden checks and source review reduce the chance of optimizing only for generated tests. Multiple valid investigative paths must remain valid.

### 7.2 Measures and failure diagnosis

Report per-case outcomes and aggregate uncertainty, not just a single score:

- Important impacts found/missed and supported/unsupported claims, split by mechanism and case difficulty.
- Target/source identity mistakes, evidence coverage and successful discriminating observations.
- Recommendation usefulness/correctness, unnecessary abstention and unsupported favorable conclusions, separately.
- Correct stop vs premature stop, useful recovery vs repeated failed calls, and budget exhaustion vs resolved task.
- Repeated-run success/consistency, human review time, tokens, elapsed time, provider/tool failures and maintenance effort.
- Execution boundaries and injection resilience alongside benign task performance.

Diagnose each failure from the trace: missing evidence/context, inaccurate semantics, bad planning/stopping, tool/interface problem, provider capacity/schema issue, upstream implementation defect, oracle error or intentional containment. A valid schema, exact citation, passing generated test or agreement among agents is an observation with a limited claim, not complete semantic acceptance.

Prefer traces containing visible tool calls/results, exact source/version identities, concise decision explanations, generated tests/patches and outcome records. Do not depend on access to private model reasoning.

### 7.3 Conditions for supporting or rejecting a candidate

Before scoring protected cases, agree on material benefit, critical-error limits and acceptable cost/review burden. Candidate success requires meaningful additional supported discoveries or better decisions, with evaluated false concerns, robustness and cost. A pilot success supports a further trial, not automatic production adoption.

If fixed workflows match agent outcomes at lower burden, that is a useful result. If an agent adds value only in a recognizable subset, evaluate routing and fallback. If it improves discovery but weakens recommendations, split those responsibilities rather than forcing all-or-nothing adoption. If negative results trace to inadequate tools or model capacity, repair/compare that cause before rejecting the architectural hypothesis.

## 8. Questions still requiring deeper evidence or a decision

1. Which product outcome should dominate the first comparison: broader findings, a completed investigation, a useful recommendation, or an executable migration? The present recommendation is a shared whole-investigation task with separately scored discovery/recommendation, while holding execution as an additional factor.
2. What independent adjudicator and protected case set can establish recommendation quality? Existing product-simulation conclusions cannot alone supply unseen labels.
3. Which model/provider configurations are feasible under the available local hardware and which would represent a capability ceiling? ENVIRONMENT records local deployment facts; service/model capacity was not probed here. Paid/cloud experiments are not selected.
4. How broad should the first agent's generic tools be, and which observation/containment setup would make executable experiments meaningful? No target code was executed here.
5. Does raw-source retrieval, a graph view or structured upstream evidence best serve each task? Full methods/tool-version review is needed before engineering a comparator.
6. Do current saved results retain enough exact evidence for the selected agent task? An offline report is not automatically a complete run trace or resumable investigation.
7. Does independent model recommendation need calibrated claim types, human review, a verifier, or a different product framing? The current abstention-only policy cannot be the oracle for this question.
8. Are earlier prerequisites genuine experiment dependencies or only adoption/coordination choices? Requiring two admitted product actions or non-abstention implementation first may unnecessarily constrain a separate generic-tool research comparison.
9. What has main implemented and verified by the time of experimental design? Reconcile the delta then; do not copy ongoing work or treat this frozen report as current-main truth.

Final architecture/design remains open. A reasonable next research step is to turn the most informative comparison into a concrete protocol with model/tool options, source/case acquisition, independent oracle and cost estimates, then discuss it with Ali before implementation.

One practical reconciliation already visible in source: the historical planner hardcodes port 12345, while the maintained extractor and [ENVIRONMENT](../ENVIRONMENT.md) use 18080. The recorded adopted context is 4096. Future trial feasibility must be checked for its actual request/model/load identity, rather than assuming the old pilot's provider settings or present API documentation prove a usable agent deployment. No endpoint or capacity was measured in this pass. [P17](https://lmstudio.ai/docs/developer/rest)

## 9. Primary-source register

All entries were accessed on 2026-10-05. Read depth states what was inspected; published/vendored results were not reproduced. Claims elsewhere link directly to supporting sources.

| ID | Primary source and pinned version where available | Inspection depth / use | Transfer limit |
|---|---|---|---|
| P01 | [Agentless, v2 (2024)](https://arxiv.org/html/2407.01489v2) | Abstract and introductory tool/planning limitations; fixed LLM workflow baseline | Historical issue-repair benchmark, not today's rankings or maintainer decision quality |
| P02 | [SWE-agent, v3 (2024)](https://arxiv.org/abs/2405.15793v3) | Abstract; interface/tool hypothesis | Repository issue repair; no dependency-decision oracle |
| P03 | [DepRepair, v1 (2026)](https://arxiv.org/html/2607.17957v1) | Abstract, evidence ablation/discussion and validity/limitations | Small Python subset; repair test oracle and studied contexts |
| P04 | [LocAgent, ACL 2025](https://aclanthology.org/2025.acl-long.426/) | Abstract; graph-guided localization lead | Localization/repair gains are not compatibility proof |
| P05 | [CodeRAG-Bench, NAACL Findings 2025](https://aclanthology.org/2025.findings-naacl.176/) | Abstract; retrieval quality and context-use limits | Code-generation tasks; retrieval benefit is conditional |
| P06 | [OpenHands Software Agent SDK, v2 (2026)](https://arxiv.org/abs/2511.03690v2) | Abstract; sandbox/lifecycle/composable harness lead | Author architecture claims; exact current SDK APIs not audited |
| P07 | [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview) | Current core-benefit docs | Feature availability, not task superiority |
| P08 | [Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Just-in-time retrieval, tools, compaction/notes sections | Vendor engineering guidance; task-specific verification needed |
| P09 | [Scaling agent systems, v3 (2026)](https://arxiv.org/html/2512.08296v3) | Abstract and selected limitations | Studied tasks/configurations; no universal agent-count rule |
| P10 | [AgentDojo, v3 (2024)](https://arxiv.org/abs/2406.13352v3) | Abstract; adversarial tool-output evaluation lead | Different application domains and attack exposure |
| P11 | [Demystifying agent evals (2026)](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | Task/trial/outcome definitions, research grading and variation sections | Vendor methodology; UpgradePilot oracle still to establish |
| P12 | [Griffe API checking](https://mkdocstrings.github.io/griffe/guide/users/checking/) | Git/PyPI comparison and Python API docs | API surface; installation/environment constraints; not behavior proof |
| P13 | [LibCST codemods](https://libcst.readthedocs.io/en/latest/codemods.html) | Codemod/metadata/context sections | Rewrite mechanism; correctness depends on rule and verification |
| P14 | [CodeQL code analysis](https://docs.github.com/en/code-security/tutorials/customize-code-scanning/analyze-code) | Overview lead | Database/query method; exact Actions extraction/query suitability pending |
| P15 | [Human–AI systematic review/meta-analysis (2024)](https://www.nature.com/articles/s41562-024-02024-1) | Abstract and study scope | Heterogeneous earlier studies, not modern code-agent prediction |
| P16 | [Entropy/selective prediction, v1 (2026)](https://arxiv.org/abs/2603.21172v1) | Abstract | QA calibration findings need software-task validation |
| P17 | [LM Studio REST API](https://lmstudio.ai/docs/developer/rest) | Endpoint/feature comparison | Current docs do not establish installed server/model support |
| P18 | [Building effective agents (2024)](https://www.anthropic.com/engineering/building-effective-agents) | Workflow/agent distinction and architecture tradeoffs | Historical tooling; conceptual reference, not SDK selection |
| P19 | [Renovate Merge Confidence](https://docs.renovatebot.com/merge-confidence/) | Signals, confidence and algorithm/data descriptions | Aggregate/private algorithm; exact-target evidence and oracle differ |
| P20 | [OSV guided remediation](https://google.github.io/osv-scanner/experimental/guided-remediation/) | Usage and remediation strategies | Vulnerability-focused; exact Python/backend suitability unverified |
| P21 | [SLSA provenance v1.2](https://slsa.dev/spec/v1.2/provenance) | Provenance meaning and format navigation | Artifact origin, not semantic compatibility/agent correctness |

No source supports a claim that UpgradePilot's current agentic alternatives are already reliable, independently useful or adopted. The next protocol needs deeper methods/API/corpus verification for whichever comparison is selected.
