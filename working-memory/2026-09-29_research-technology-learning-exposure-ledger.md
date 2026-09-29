# Research Technology Learning / Exposure Ledger

**Recorded:** 2026-09-29  
**Branch:** `analysis/ai-agentic-capability-map-2026-09-28`  
**Status:** ACTIVE supporting ledger  
**Purpose:** track technologies, tools, libraries, standards, and methods surfaced during external research that may be valuable either to UpgradePilot, to transferable engineering learning, or both.

This ledger does **not** authorize product adoption.

## Experience evidence states

- **RESEARCHED** — evaluated/documented only.
- **HANDS_ON_EXPERIMENTED** — installed/configured/executed on a bounded real case.
- **PROJECT_INTEGRATED** — implemented in UpgradePilot with code/tests/design evidence.
- **VALIDATED_OPERATED** — repeatedly exercised against representative cases with evaluation/diagnostics.

Only the latter three justify saying there was hands-on experience, and the exact wording should match the achieved state.

## Current candidates from Tier-1 Reports 01–03

| Technology / method | Why technically interesting | Learning / career value | Current evidence state | Suggested exposure target |
| --- | --- | --- | --- | --- |
| Renovate architecture (Manager / Datasource / Versioning / Platform) | mature extensibility decomposition for dependency automation | plugin architecture, ecosystem abstraction, product orchestration | RESEARCHED | research + possible architecture comparison |
| dependabot-core ecosystem contracts | stable per-ecosystem fetch/parse/check/update interfaces | adapter architecture, package ecosystem integration | RESEARCHED | research only unless direct comparison experiment becomes useful |
| Updatecli source→condition→target→SCM→action model | declarative typed workflow/capability composition | declarative automation, policy/config pipelines | RESEARCHED | bounded lab if orchestration design needs a comparator |
| Endor-style call/context graphs | target + dependency structural reachability and upgrade impact | program analysis, graph modeling, impact analysis | RESEARCHED | high-value future lab/architecture experiment |
| Semgrep / Semgrep Supply Chain | static/dataflow analysis + dependency reachability + LLM upgrade guidance | static analysis, rule/query design, code security, AI+analysis hybrid systems | RESEARCHED | **high-priority hands-on candidate** |
| CodeQL | semantic/data-flow queries across code | query-based program analysis, security engineering, graph/dataflow reasoning | RESEARCHED | **high-priority hands-on candidate** |
| Joern / Code Property Graph | unified graph model for program analysis | graph queries, CPGs, cross-language analysis | RESEARCHED | hands-on lab if graph research remains promising |
| Socket behavior-delta analysis | captures install scripts, shell/network/filesystem/native-code changes | supply-chain threat analysis, package behavior reasoning | RESEARCHED | research first; experiment if package-behavior mechanism enters product horizon |
| OSV-Scanner Guided Remediation | graph-aware remediation strategy selection | dependency graph optimization, remediation planning, security tooling | RESEARCHED | **good bounded hands-on candidate** |
| deps.dev / Open Source Insights | reusable package/version/dependency graph | public supply-chain APIs, dependency graph data | RESEARCHED | likely hands-on during Tier-1 #04 |
| GUAC | graph-oriented software supply-chain evidence aggregation/query | knowledge/evidence graphs, GraphQL, provenance/SBOM integration | RESEARCHED | **strong hands-on candidate if graph substrate remains relevant** |
| OpenRewrite | type-attributed lossless semantic trees + deterministic migration recipes | AST/IR transformation, refactoring automation, migration systems | RESEARCHED | strong conceptual exposure; hands-on if Python/JVM comparison is useful |
| Moderne | large-scale recipe execution / migration governance | code transformation at scale, migration UX | RESEARCHED | research/demo exposure; likely not product dependency |
| Griffe | Python API model + breaking-change detection | Python API compatibility analysis, static inspection | RESEARCHED | **very high-priority hands-on/project experiment candidate** |
| LibCST | Python concrete syntax tree + metadata-aware codemods | safe source transformation, codemods, compiler/tooling concepts | RESEARCHED | **very high-priority hands-on/project experiment candidate** |
| DepRepair / DepBench methodology | distilled cross-repository evidence + LLM repair + executable oracle | evaluation design, LLM repair pipelines, benchmark methodology | RESEARCHED | reproduce/borrow methodology rather than library integration |
| symbolic execution (angr / CrossHair) | proves/rejects bounded path properties under modeled semantics | formal methods, program analysis, path constraints | RESEARCHED | hands-on lab when conditional/runtime analysis question warrants it |
| actionlint | GitHub Actions semantic/static checking | CI static analysis, workflow semantics | RESEARCHED | easy hands-on comparator for CI research |
| zizmor | GitHub Actions security analysis | CI/CD security, static workflow auditing | RESEARCHED | likely hands-on in CI/security research |
| StepSecurity Harden-Runner/runtime monitoring | per-step process/network/file evidence | runtime security/observability, CI evidence, policy | RESEARCHED | strong hands-on candidate if runtime evidence research supports it |
| OpenShell / sandbox-policy runtime concepts | external policy enforcement for agent execution | sandboxing, policy, agent security, capability control | RESEARCHED | research now; hands-on if agent execution reaches product experiment |
| SLSA | software supply-chain provenance framework | provenance, build integrity, supply-chain security | RESEARCHED | likely practical exposure in Tier-1 #04 |
| in-toto | attestations/layout-based supply-chain verification | provenance, attestations, policy verification | RESEARCHED | likely hands-on/example in Tier-1 #04 |
| SPDX / CycloneDX / VEX | standardized SBOM and vulnerability/exploitability exchange | industry supply-chain standards, interoperability | RESEARCHED | **high-value standards exposure** |
| LangGraph | stateful agent workflow orchestration | agent state machines, checkpointing/orchestration | HANDS_ON_EXPERIMENTED (existing UpgradePilot experiments) | retain evidence; deepen only on real product pressure |
| LangChain agent concepts | higher-level agent/tool/middleware abstraction | common agent ecosystem concepts | RESEARCHED | defer hands-on until real orchestration pressure |
| local LM Studio / structured-output model integration | bounded local inference and schema-driven model calls | local inference, model serving, structured output, evaluation | PROJECT_INTEGRATED / VALIDATED in bounded experiments | retain and extend only when product responsibility requires |
| evidence-gap planner architecture | model planning + deterministic admission | AI agent authority boundaries, state/action design, evaluation | PROJECT_INTEGRATED experimentally | strong portfolio evidence; deepen only with richer real action space |

## Highest-value near-term learning candidates

These currently appear especially strong because they combine transferable skill value with plausible UpgradePilot relevance:

1. **Griffe** — directly useful for Python dependency API-diff research.
2. **LibCST** — directly useful for Python structural transformation/codemod work.
3. **Semgrep** — relevant to reachability, static analysis, security, and AI-assisted dependency impact.
4. **CodeQL** — teaches deeper data-flow/query reasoning and program-analysis fundamentals.
5. **GUAC + SLSA/in-toto/SPDX/CycloneDX** — useful for graph/provenance research and supply-chain-security skills.
6. **OSV-Scanner Guided Remediation** — practical graph-aware vulnerability/remediation tooling.
7. **StepSecurity / zizmor / actionlint** — useful for CI evidence/security and aligned with current runtime-proof work.
8. **Joern or CrossHair/angr** — deeper program-analysis exposure when a concrete responsibility justifies the cost.

## Learning-selection rule

A technology is not chosen merely because it is trending.

Prefer hands-on exposure when:

```text
real UpgradePilot question
+
credible tool/method fit
+
meaningful transferable skill
+
bounded experiment with observable output
```

If product need is weak but learning value is high, use a separate bounded lab/experiment rather than increasing product complexity.

## Evidence we should preserve when experimenting

To make later experience claims defensible, record:

- exact tool/version/configuration;
- problem/question being solved;
- commands/config/code written;
- input dataset/repository/case;
- output/results;
- failures/debugging;
- tests/evaluation;
- comparison to baseline;
- what was learned;
- final retain/reject/defer decision.

This allows future claims such as:

> “Built and evaluated a Python API migration prototype using Griffe and LibCST”

only after that experiment actually exists.


## Tier-1 Report 04 additions

### deps.dev / Open Source Insights
- **Current state:** RESEARCHED.
- **Learning value:** high.
- **Hands-on target:** query two PyPI versions, compare declared requirements vs resolved generic dependency graphs, and compare with target-derived evidence.
- **Recommended exposure:** HANDS_ON_EXPERIMENTED.

### GUAC
- **Current state:** RESEARCHED.
- **Learning value:** very high.
- **Hands-on target:** run GUAC locally, ingest CycloneDX/SPDX, enable deps.dev/OSV enrichment, query relationships with GraphQL.
- **Recommended exposure:** HANDS_ON_EXPERIMENTED; possible later architecture comparator.

### CycloneDX 1.7
- **Current state:** RESEARCHED.
- **Learning value:** very high.
- **Hands-on target:** encode one UpgradePilot evidence case with components, dependency edges, evidence techniques, occurrences, callstack, claims, evidence, assessor, citation, formulation.
- **Recommended exposure:** HANDS_ON_EXPERIMENTED; possible future interchange/export candidate.

### SPDX 3.0.1
- **Current state:** RESEARCHED.
- **Learning value:** high.
- **Hands-on target:** model repo/build/dependency relationships and compare `NoneElement` vs `NoAssertionElement` with UpgradePilot unresolved/non-applicable semantics.
- **Recommended exposure:** HANDS_ON_EXPERIMENTED.

### SLSA 1.2 + in-toto + Sigstore/Cosign
- **Current state:** RESEARCHED.
- **Learning value:** very high for supply-chain security.
- **Hands-on target:** generate and verify an attestation for a GitHub Actions artifact/report bound to exact revision/workflow/artifact digest.
- **Recommended exposure:** project experiment candidate if audit/replay value is confirmed.

### GitHub artifact attestations / dependency submission
- **Current state:** RESEARCHED.
- **Learning value:** high and directly aligned with existing GitHub Actions work.
- **Hands-on target:** compare static dependency detection with build-time submitted snapshots; generate/verify a small artifact attestation.
- **Recommended exposure:** project experiment candidate.

### OSS Review Toolkit
- **Current state:** RESEARCHED.
- **Learning value:** high but heavier.
- **Hands-on target:** analyze a small Python project, inspect OrtResult, export SPDX/CycloneDX, optionally add one policy rule.
- **Recommended exposure:** bounded lab if Track C needs a mature SCA pipeline baseline.


## Tier-1 Report 05 additions

### CodeQL for GitHub Actions / Python
- **Current state:** RESEARCHED.
- **Learning value:** extremely high.
- **Hands-on target:** write a custom Actions query tracing an environment/context value across steps into a package-manager run step; compare against UpgradePilot's current result.
- **Skills:** QL, AST, CFG, dataflow, taint tracking, GitHub Actions semantics, SARIF/security analysis.
- **Recommended exposure:** HANDS_ON_EXPERIMENTED / project comparator candidate.

### actionlint
- **Current state:** RESEARCHED.
- **Learning value:** high for CI semantics with very low experiment cost.
- **Hands-on target:** run against UpgradePilot/product-simulation workflows and compare diagnostics with current parser assumptions.
- **Recommended exposure:** HANDS_ON_EXPERIMENTED.

### zizmor
- **Current state:** RESEARCHED.
- **Learning value:** high for CI/CD security.
- **Hands-on target:** audit representative workflows, inspect template-injection/permissions/action-pinning findings, compare with product candidate-discovery needs.
- **Recommended exposure:** HANDS_ON_EXPERIMENTED.

### StepSecurity Harden-Runner
- **Current state:** RESEARCHED.
- **Learning value:** very high for CI/runtime/agent security.
- **Hands-on target:** instrument a public workflow and correlate package-manager process/network events with exact job/step/run identity.
- **Recommended exposure:** project experiment candidate if accessible telemetry is sufficient.

### act
- **Current state:** RESEARCHED.
- **Learning value:** useful/practical.
- **Hands-on target:** emulate representative GitHub Actions cases and record divergence from hosted-run evidence.
- **Recommended exposure:** HANDS_ON_EXPERIMENTED; never treated as historical-run authority.

### Joern
- **Current state:** RESEARCHED.
- **Learning value:** high/advanced.
- **Hands-on target:** generate a Python CPG, write a small dataflow/call query, compare representation with CodeQL.
- **Recommended exposure:** lab candidate after Track C if graph architecture remains relevant.

### CrossHair
- **Current state:** RESEARCHED.
- **Learning value:** very high for formal-method fundamentals.
- **Hands-on target:** apply symbolic execution to one pure UpgradePilot semantic/predicate function and inspect counterexamples/path coverage.
- **Recommended exposure:** bounded learning/project lab.

### angr
- **Current state:** RESEARCHED.
- **Learning value:** strong security/reverse-engineering exposure, low current product fit.
- **Hands-on target:** isolated symbolic-execution exercise on a tiny binary/path condition.
- **Recommended exposure:** learning lab / defer from product.


## Tier-1 Report 06 additions

### Small Python repository graph / Tree-sitter-style indexing
- **Current state:** RESEARCHED.
- **Learning value:** very high.
- **Hands-on target:** build a compact file/class/function/import/call graph for one Python repository and expose impact/reference queries.
- **Skills:** AST extraction, graph schema, symbol resolution, graph traversal, provenance.
- **Recommended exposure:** HANDS_ON_EXPERIMENTED / possible project comparator.

### Repository Intelligence Graph (RIG) concept
- **Current state:** RESEARCHED.
- **Learning value:** very high and unusually aligned with UpgradePilot.
- **Hands-on target:** build a bounded Python map connecting modules/packages, tests, CI jobs, runners and package-manager evidence.
- **Skills:** build/test architecture, evidence-backed graph modeling, Pydantic, agent context design.
- **Recommended exposure:** project experiment candidate.

### Neo4j / Cypher
- **Current state:** RESEARCHED via CodexGraph architecture.
- **Learning value:** high.
- **Hands-on target:** load a small code/evidence graph, write read-only Cypher queries, compare model-generated queries with typed graph tools.
- **Recommended exposure:** bounded graph-database lab; product only if graph backend need becomes real.

### Sourcegraph Code Graph / search
- **Current state:** RESEARCHED.
- **Learning value:** high for production code intelligence.
- **Hands-on target:** use indexed symbol/reference/search workflows on a representative repository if accessible.
- **Recommended exposure:** research + practical lab, not current dependency.

### Retrieval comparison / CodeRAG methods
- **Current state:** RESEARCHED.
- **Learning value:** high AI-engineering value.
- **Hands-on target:** compare lexical/BM25, embeddings, graph retrieval and hybrid retrieval on a small frozen repository question set.
- **Recommended exposure:** project evaluation lab.

### SWE-agent / mini-swe-agent ACI principles
- **Current state:** RESEARCHED; legacy SWE-agent itself is maintenance-only/superseded.
- **Learning value:** very high for agent engineering.
- **Hands-on target:** create a small UpgradePilot-specific tool interface with constrained file viewing, structural search, evidence query, read-only check execution and explicit post-action state.
- **Recommended exposure:** project experiment candidate focused on ACI concepts rather than legacy framework adoption.

### OpenHands
- **Current state:** RESEARCHED.
- **Learning value:** very high.
- **Hands-on target:** run one bounded repository issue/investigation in a sandbox, inspect trajectory/tool use/context/cost, and compare with a fixed UpgradePilot pipeline.
- **Skills:** generalist agents, sandbox execution, MCP, model routing, lifecycle/budget controls.
- **Recommended exposure:** bounded comparator experiment; not default product dependency.

### Agentless architecture
- **Current state:** RESEARCHED.
- **Learning value:** high methodology value.
- **Hands-on target:** implement/freeze a simple staged localization→reasoning→validation baseline for the same case used in an agent experiment.
- **Recommended exposure:** evaluation baseline rather than separate technology adoption.

### GitHub Copilot repository instructions / skills / MCP
- **Current state:** RESEARCHED, with analogous UpgradePilot AGENTS/skills usage already present.
- **Learning value:** high and current.
- **Hands-on target:** create a comparison note/experiment mapping UpgradePilot governance and skills to current repository-agent customization conventions.
- **Recommended exposure:** project-integrated documentation/agent-workflow learning.


## Tier-1 Report 07 additions

### SWE-bench evaluation harness / containerized SWE evaluation
- **Current state:** RESEARCHED.
- **Learning value:** very high.
- **Hands-on target:** run a small containerized software-engineering evaluation and inspect task/oracle quality rather than only leaderboard scoring.
- **Skills:** benchmark harnesses, Docker reproducibility, hidden tests, eval methodology, contamination awareness.
- **Recommended exposure:** bounded evaluation lab.

### Python BUMP / DepBench-style dependency-update corpus
- **Current state:** RESEARCHED as methodology; not yet built.
- **Learning value:** extremely high and directly product-relevant.
- **Hands-on target:** create a small reproducible Python corpus with exact pre/post dependency transitions, environment images, mechanism labels, and executable or evidence-based oracles.
- **Skills:** dataset construction, Docker, evaluation design, dependency breakage taxonomy, reproducibility.
- **Recommended exposure:** strong future UpgradePilot project experiment/artifact candidate.

### Calibration / selective prediction
- **Current state:** RESEARCHED.
- **Learning value:** very high for applied AI engineering.
- **Hands-on target:** compute confidence/uncertainty and risk-coverage curves for one bounded semantic model responsibility; compare abstention policies.
- **Skills:** calibration, uncertainty, selective risk, thresholding, statistical evaluation.
- **Recommended exposure:** project experiment when next semantic-model evaluation is active.

### Agent trajectory analytics
- **Current state:** RESEARCHED conceptually; UpgradePilot already records bounded planner transitions experimentally.
- **Learning value:** very high.
- **Hands-on target:** build an evaluator that measures action sequences, evidence gain, cost, invalid actions, stopping, and repeated-run variance for EvidenceGapPlanner.
- **Recommended exposure:** project experiment candidate when planner action space expands.

### Maintainer decision-support study
- **Current state:** RESEARCHED methodology.
- **Learning value:** high for product/HCI evaluation.
- **Hands-on target:** once report UX stabilizes, compare normal dependency PR vs deterministic UpgradePilot report vs hybrid report on decision time, correctness, trust calibration, and evidence usage.
- **Recommended exposure:** defer until product surface is stable enough for meaningful human study.
