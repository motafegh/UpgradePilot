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
