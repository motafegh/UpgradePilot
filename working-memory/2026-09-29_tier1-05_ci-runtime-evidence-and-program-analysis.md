# Tier 1 Report 05 — CI / Runtime Evidence + Program-Analysis Techniques

**Recorded:** 2026-09-29  
**Branch:** \`analysis/ai-agentic-capability-map-2026-09-28\`  
**Status:** COMPLETE initial deep report  
**Research family:** CI/runtime evidence + program-analysis techniques  
**Systems/methods examined:** actionlint, zizmor, GitHub Actions native logs/runtime model, StepSecurity Harden-Runner, act, CodeQL for GitHub Actions/Python, Joern/Code Property Graphs, CrossHair, angr  
**Purpose:** determine how much of UpgradePilot's difficult CI/runtime/environment reasoning can be delegated to mature static analysis, runtime telemetry, workflow emulation, code graphs, or symbolic execution before extending bespoke logic or introducing model reasoning.

This report records external research evidence only. It does not replace current Increment-3 work on \`main\`, accepted ADRs/specifications, or authorize a tool dependency.

---

## 1. Research questions

1. Which current CI questions are already modeled by mature GitHub Actions analyzers?
2. Which questions require runtime observation rather than static analysis?
3. Can runtime telemetry establish stronger facts than workflow logs alone?
4. Can local workflow emulation serve as proof, or only as experimental evidence?
5. Can CodeQL/CPG frameworks reduce bespoke graph/control/data-flow modeling?
6. Where can symbolic execution help with conditional/path questions?
7. What parts remain inherently UpgradePilot-specific?
8. Which tools are worth hands-on exposure even if they are not adopted?

---

## 2. Executive result

The main result is **not** “replace UpgradePilot with an existing analyzer.”

It is:

> UpgradePilot currently spans several analysis layers that mature tools already separate. Some bespoke logic should remain, but several higher-level responsibilities now deserve direct comparison with existing analyzers before more custom implementation.

The external landscape separates into five layers:

\`\`\`text
1. WORKFLOW STATIC VALIDATION
   actionlint
   zizmor

2. WORKFLOW PROGRAM ANALYSIS
   CodeQL GitHub Actions
   AST + CFG + inter-step dataflow / taint

3. RUNTIME OBSERVATION
   GitHub runner/worker logs
   StepSecurity runtime process/network/file telemetry

4. EXECUTABLE RECONSTRUCTION / EMULATION
   act

5. GENERAL PROGRAM / PATH ANALYSIS
   CodeQL Python
   Joern CPG
   CrossHair
   angr
\`\`\`

No one layer provides all of:

\`\`\`text
static workflow meaning
+
exact shell/package-manager semantics
+
historical runtime execution truth
+
target package/environment state
+
decision-specific evidence sufficiency
\`\`\`

The strongest near-term architecture question is therefore:

> **Should UpgradePilot keep its specialized shell/package-manager semantics, but use a mature workflow CFG/dataflow engine such as CodeQL for higher-level workflow relations and use optional runtime telemetry for exact observations?**

That question deserves an experiment before more graph/control-flow machinery is added by hand.

---

## 3. actionlint — fast bounded workflow semantics

### 3.1 Responsibility

actionlint is a static checker specifically for GitHub Actions workflow files.

Its documented checks include:

- workflow syntax/schema;
- strong typing of \`${{ ... }}\` expressions;
- invalid/nonexistent properties;
- action input/output consistency;
- reusable workflow input/output/secret validation;
- \`needs:\` dependencies;
- runner labels;
- cron/glob validation;
- script injection checks;
- ShellCheck integration for shell \`run:\` scripts;
- pyflakes integration for Python \`run:\` scripts.

### 3.2 Why it matters

actionlint demonstrates that a substantial amount of GitHub Actions semantic validation can be handled cheaply and deterministically before any bespoke analysis.

Conceptually:

\`\`\`text
workflow YAML
→ GitHub Actions schema/expression semantics
→ shell/Python linters
→ diagnostics
\`\`\`

This is different from UpgradePilot's current responsibility:

\`\`\`text
workflow YAML
→ identify exact dependency-relevant command occurrences
→ infer which runtime evidence can strengthen which occurrence
→ derive package-manager semantic facts
\`\`\`

The overlap is partial, not complete.

### 3.3 Valuable comparator responsibilities

actionlint could potentially become a baseline/oracle for:

- workflow syntax validity;
- expression typing;
- reusable-workflow wiring;
- obvious invalid \`needs\` structures;
- shell syntax/security issues;
- Python syntax issues inside run blocks.

### 3.4 Limitations for UpgradePilot

actionlint does not by itself establish:

- whether a branch actually executed in a specific historical run;
- exact package-manager runtime state;
- effective environment/config precedence;
- dependency impact/applicability;
- target-specific evidence sufficiency.

It is primarily a checker, not a historical evidence engine.

### 3.5 Architecture implication

Before implementing a bespoke workflow-semantic validation rule, ask:

> is this already an actionlint responsibility?

If yes, integration or comparison may be cheaper and better tested than duplication.

Source:
- https://github.com/rhysd/actionlint/

---

## 4. zizmor — security-oriented GitHub Actions static analysis

### 4.1 Responsibility

zizmor is a security-focused static analyzer for GitHub Actions.

It audits workflow/action files for security problems including:

- template/script injection;
- dangerous workflow triggers;
- excessive permissions;
- unpinned/mutable dependencies;
- credential persistence and other CI/CD hardening issues.

It supports different audit personas/severity filtering and has autofix modes for some findings.

### 4.2 Why it matters

zizmor models a different proposition family from actionlint:

\`\`\`text
actionlint:
is this workflow structurally/semantically valid?

zizmor:
does this valid-looking workflow introduce CI/CD security risk?
\`\`\`

That separation is useful for UpgradePilot's mature system because dependency updates can modify CI definitions or action versions and therefore change CI trust/security even when package compatibility is unaffected.

### 4.3 Template expansion insight

zizmor's template-injection analysis explicitly reasons about the fact that GitHub expression expansion occurs before shell execution and may inject attacker-controlled values into script contexts.

This is a concrete example where:

\`\`\`text
workflow expression semantics
→ change shell command semantics
\`\`\`

and therefore reinforces that shell analysis cannot always be performed independently of Actions expression/dataflow analysis.

### 4.4 Transferable value

Potential future UpgradePilot use:

- CI security-impact candidate discovery;
- third-party Action trust/pinning checks;
- workflow change risk context;
- independent security baseline.

But zizmor does not provide runtime execution proof or package-manager semantics.

Sources:
- https://docs.zizmor.sh/
- https://docs.zizmor.sh/audits/

---

## 5. CodeQL for GitHub Actions — the most important finding in this report

### 5.1 Dedicated Actions semantic model

CodeQL now ships a dedicated GitHub Actions library.

It models:

- workflow/action AST;
- GitHub Actions-specific nodes and expressions;
- workflows/jobs/steps;
- \`if\` nodes;
- environment mappings/expressions;
- matrix expressions;
- \`needs\`;
- reusable workflows;
- shell scripts;
- action usage;
- triggers/permissions.

### 5.2 Workflow control-flow graph

The Actions library exposes a CFG.

It can ask questions such as:

- can expression/statement A execute before B?
- does A dominate B?
- is a path between two workflow constructs possible?

This directly overlaps with some of UpgradePilot's current handcrafted reasoning about:

- step ordering;
- conditions;
- path relations;
- structural execution profiles.

### 5.3 Inter-step data flow

The Actions data-flow library tracks information:

- through function calls;
- **between steps in a job/workflow**;
- through GitHub Actions expression structures.

It also includes taint tracking.

This is especially relevant to unresolved questions such as:

\`\`\`text
earlier step writes environment/config state
→ later package-manager command receives it?
\`\`\`

UpgradePilot currently needs environment reachability/provenance for cases such as \`PIP_DRY_RUN\`, \`PIP_TARGET\`, executable selection, and generated environment state.

CodeQL should therefore be treated as a serious external comparator for the **workflow-level propagation layer**.

### 5.4 Existing Actions security queries prove the model is operational

Current CodeQL Actions query suites include analyses for:

- code injection;
- attacker-controlled environment/PATH values;
- artifact/cache poisoning;
- privileged/untrusted checkout;
- excessive secret exposure;
- unpinned Actions;
- known-vulnerable Actions;
- always-true \`if\` expressions.

So this is not merely a theoretical parser API; GitHub uses the model for concrete inter-step/workflow security analyses.

### 5.5 It does not eliminate specialized shell/package-manager semantics

CodeQL can model a \`Run\` node and shell-script structures, but UpgradePilot still has a domain-specific question:

\`\`\`text
this shell occurrence
→ is it exactly a pip/uv/package-manager operation?
→ which semantic options apply?
→ what environment/config precedence changes its effect?
→ what package-state proposition follows?
\`\`\`

That remains distinct from generic workflow CFG/dataflow.

### 5.6 Strong candidate architecture

A plausible layered architecture to test is:

\`\`\`text
GitHub Actions source
→ CodeQL Actions AST / CFG / dataflow
→ exact workflow-level path + env/data relationships

→ UpgradePilot shell-command analysis
→ exact package-manager operation declaration

→ UpgradePilot package-manager semantic layer
→ package/environment propositions

→ historical runtime evidence
→ strengthen only what the observation proves
\`\`\`

This could reduce bespoke high-level workflow graph code without giving up the narrow semantic models already built.

### 5.7 Cost / risk

CodeQL has real adoption costs:

- QL language;
- database generation;
- query-pack/tooling setup;
- licensing/use conditions depending on context;
- performance/startup cost compared with a small Python parser;
- potentially awkward mapping back into UpgradePilot's typed domain state.

Therefore the right next step is a **bounded comparative experiment**, not immediate replacement.

Sources:
- https://codeql.github.com/docs/codeql-language-guides/codeql-library-for-actions/
- https://codeql.github.com/codeql-standard-libraries/actions/actions.qll/module.actions.html
- https://codeql.github.com/codeql-query-help/actions/

---

## 6. GitHub native runtime evidence

### 6.1 Standard and debug logs

GitHub provides:

- step logs;
- runner diagnostic logs;
- worker process/job logs;
- optional \`ACTIONS_STEP_DEBUG\`;
- optional \`ACTIONS_RUNNER_DEBUG\`;
- downloadable workflow-run archives.

The runner debug archive includes separate runner coordination/setup logs and worker job-execution logs.

### 6.2 Workflow environment files

GitHub's runner creates special files such as those backing:

- \`GITHUB_ENV\`;
- step outputs;
- state;
- path modifications.

A step can write environment values that affect subsequent steps.

This is directly relevant to UpgradePilot's environment-flow analysis.

### 6.3 Native logs are useful but not a universal process-trace contract

GitHub documentation exposes detailed diagnostics, but the standard workflow log model is principally:

\`\`\`text
runner orchestration
+
step/action logging
+
debug diagnostics
\`\`\`

rather than a complete operating-system process/network/file provenance stream.

That gap is exactly what runtime-security systems such as StepSecurity target.

### 6.4 Architecture implication

UpgradePilot should distinguish:

\`\`\`text
GitHub-native run evidence
from
instrumented runner telemetry
\`\`\`

rather than treating “logs” as one evidence class.

Sources:
- https://docs.github.com/en/actions/how-tos/monitor-workflows/enable-debug-logging
- https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands
- https://docs.github.com/en/actions/reference/runners/github-hosted-runners

---

## 7. StepSecurity Harden-Runner — runtime evidence rather than inference

### 7.1 Responsibility

Harden-Runner acts like a CI/CD runtime-security monitor.

Current public material describes observation/control of:

- outbound network activity;
- process activity;
- file activity/integrity;
- HTTPS/API requests in supported modes;
- per-job/per-step behavioral context;
- anomaly/baseline information;
- egress policy enforcement.

Its current 2026 product supports multiple GitHub runner operating systems/providers, with capabilities varying by tier/platform.

### 7.2 Why this is highly relevant

UpgradePilot currently tries to infer some runtime facts from:

\`\`\`text
static structure
+
step success
+
shell failure semantics
\`\`\`

Runtime telemetry can answer a different question:

\`\`\`text
what processes/files/network events actually occurred?
\`\`\`

This can be strictly stronger for some propositions.

For example:

\`\`\`text
static conditional pip command
+
step success
→ branch execution unresolved

but

runtime process evidence showing pip/python invocation
correlated to that exact workflow step
→ strong direct evidence that a package-manager process actually ran
\`\`\`

It may still not uniquely identify one static occurrence when identical commands/processes exist, and it does not automatically prove the package-manager effect succeeded. But it can eliminate entire classes of static inference.

### 7.3 Runtime telemetry creates a new evidence source, not a replacement for static semantics

A process event might establish:

- executable launched;
- command line;
- parent/child process relation;
- step correlation.

It does not by itself establish:

- why it ran;
- which static source occurrence caused it when ambiguous;
- complete effective pip configuration;
- package installation success;
- final dependency state;
- relevance to the maintainer decision.

So the strong architecture is compositional:

\`\`\`text
static source identity
+
runtime event identity
+
correlation
→ stronger execution evidence
\`\`\`

### 7.4 Security and provenance value

Runtime telemetry is also directly relevant to future agent execution:

- what process did the agent spawn?
- which host/API did it contact?
- what file did it mutate?
- which workflow step caused the effect?

That makes StepSecurity valuable to both current CI evidence research and future AI-agent security.

### 7.5 Product vs integration reality

StepSecurity is a commercial platform around an open GitHub Action/runtime approach.

UpgradePilot does not need to depend on it to learn from the architecture.

A bounded public-repository experiment can still test whether its telemetry can strengthen one UpgradePilot runtime proposition.

Sources:
- https://www.stepsecurity.io/github-actions-and-stepsecurity
- https://www.stepsecurity.io/cicd-security
- https://www.stepsecurity.io/blog/monitor-outbound-https-requests-from-github-actions-runners

---

## 8. act — useful execution reconstruction, weak historical authority

### 8.1 Responsibility

\`act\` reads GitHub Actions workflow files, determines an execution path, and runs jobs/actions locally in Docker containers.

It is excellent for:

- fast local workflow testing;
- reproducing simple workflow problems;
- exercising actions without pushing every change;
- testing hypothetical workflow modifications.

### 8.2 Critical fidelity limitation

Its own documentation states that default runner images are **intentionally incomplete** relative to GitHub-hosted runners.

Additionally:

\`\`\`text
GitHub hosted runner
→ virtual machine

act
→ Docker container
\`\`\`

which changes platform behavior, available tooling, services, filesystem/system behavior, and some OS capabilities.

### 8.3 Evidence classification

Therefore:

\`\`\`text
act execution
!=
historical GitHub Actions runtime evidence
\`\`\`

and usually:

\`\`\`text
act success
!=
proof that GitHub-hosted execution succeeds
\`\`\`

It is better classified as:

- experimental reproduction;
- test harness;
- hypothesis validation;
- candidate execution evidence under a modeled environment.

### 8.4 Valuable use

For UpgradePilot, \`act\` may help:

- generate realistic test cases;
- test parsers/control-flow assumptions;
- compare inferred vs emulated execution;
- evaluate conditional/path behavior;
- experiment without consuming GitHub Actions runs.

But it should not silently strengthen target-run truth.

Sources:
- https://github.com/nektos/act
- https://github.com/nektos/act-docs/blob/main/src/usage/runners.md

---

## 9. CodeQL Python — application data/control flow

CodeQL's Python libraries provide:

- local data flow;
- global data flow;
- taint tracking;
- control-flow graphs;
- source-location correspondence.

Control-flow queries can answer questions such as:

- can A reach B?
- can B execute without A?
- is a code block unreachable?

This is relevant to future target-usage/applicability and repository-purpose investigations.

However:

\`\`\`text
Python program control flow
!=
GitHub Actions workflow control flow
!=
shell command control flow
!=
package-manager semantics
\`\`\`

CodeQL may therefore be one component in a cross-language structural model, not a universal execution engine.

Sources:
- https://codeql.github.com/docs/codeql-language-guides/analyzing-data-flow-in-python/
- https://codeql.github.com/docs/codeql-language-guides/analyzing-control-flow-in-python/

---

## 10. Joern / Code Property Graphs

### 10.1 Responsibility

Joern builds language-agnostic Code Property Graphs from:

- source code;
- bytecode;
- binary code.

Its current docs list Python support as high maturity.

Joern combines multiple program representations into a graph and exposes query-based analysis through a Scala-based DSL.

Core capabilities include:

- robust/fuzzy parsing;
- semantic CPGs;
- taint analysis;
- custom passes;
- graph export/query;
- slicing.

### 10.2 Why this is relevant

Joern offers an alternative to accumulating separate bespoke AST/dataflow/callgraph implementations.

A mature UpgradePilot graph could potentially use an existing CPG for code-level relationships while adding external nodes for:

- package versions;
- workflows;
- CI environment;
- upstream changes;
- dependency evidence.

But Joern itself does not model all of those external supply-chain concepts.

### 10.3 Strong distinction from CodeQL

Both are query-based semantic-analysis platforms, but practical trade-offs differ:

- CodeQL has a dedicated GitHub Actions semantic library and deep GitHub integration.
- Joern emphasizes extensible cross-language CPGs, robust parsing, custom passes, and research-oriented vulnerability analysis.

For current UpgradePilot CI research, CodeQL Actions is the more directly aligned comparator.

For future broad code/evidence graph research, Joern remains valuable.

Source:
- https://docs.joern.io/

---

## 11. CrossHair — bounded Python symbolic reasoning

### 11.1 Responsibility

CrossHair symbolically executes Python functions with contract/assertion-like properties.

It uses an SMT solver and symbolic inputs to explore program paths.

It supports:

- assertions;
- PEP 316 contracts;
- icontract;
- other bounded contract styles.

### 11.2 Important limitations

CrossHair's own documentation warns that:

- it executes the analyzed code;
- side effects should be avoided;
- disk/network protections are imperfect, especially for C extensions;
- complex code may not be fully explored;
- deterministic behavior is required for some analysis modes;
- typed/compatible inputs matter.

### 11.3 Relevant use for UpgradePilot

CrossHair is **not** a GitHub Actions analyzer.

Its plausible value is much narrower:

\`\`\`text
extract pure/bounded predicate logic
→ symbolically test reachable truth assignments
→ generate counterexamples / path evidence
\`\`\`

For example, if a repository-defined helper function determines an install condition and is sufficiently pure, CrossHair might explore its predicate semantics more strongly than an LLM.

This is a niche but interesting comparator for:

- bounded conditional evaluation;
- proof/counterexample generation;
- invariant checking in UpgradePilot's own semantic functions.

### 11.4 Strong learning value

Even if never adopted into product, a bounded CrossHair lab would teach:

- symbolic execution;
- contracts;
- SMT-based reasoning;
- counterexamples;
- limits of formal methods on real Python.

Sources:
- https://crosshair.readthedocs.io/en/latest/contracts.html
- https://crosshair.readthedocs.io/en/latest/kinds_of_contracts.html
- https://crosshair.readthedocs.io/en/latest/cover.html

---

## 12. angr — general binary symbolic execution

### 12.1 Responsibility

angr symbolically executes binaries.

Inputs can become symbolic variables; branches become constraints; the solver can search for values that reach a target address/path.

It is much lower-level than UpgradePilot's current Python/YAML analysis.

### 12.2 Relevance

angr is unlikely to be a near-term UpgradePilot dependency.

Its main value is methodological:

\`\`\`text
path condition
→ constraint system
→ satisfiable/unsatisfiable
→ witness/counterexample
\`\`\`

That is the conceptual formal-method alternative to:

\`\`\`text
LLM guesses whether a branch can execute
\`\`\`

### 12.3 Learning value

High conceptual/career value for security/program-analysis exposure, but relatively low immediate product value.

Therefore:

\`\`\`text
good isolated learning lab
not current product candidate
\`\`\`

Source:
- https://docs.angr.io/en/stable/core-concepts/symbolic.html

---

## 13. Responsibility comparison

| Question | actionlint | zizmor | CodeQL Actions | GitHub logs | StepSecurity | act | CrossHair/angr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| workflow schema valid? | strong | partial | yes/modelled | no | no | must execute parse | no |
| Actions expression semantics | strong typed checks | security-specific | strong semantic model | observed values partly | runtime only | emulated | no |
| workflow CFG/path | limited checker logic | security rules | **strong explicit CFG** | historical observed path only | historical events only | emulated path | extracted program only |
| inter-step env/data flow | limited checks | security-specific | **explicit data/taint flow** | partial/log-dependent | event-dependent | executable reconstruction | no |
| shell script quality | ShellCheck | security-specific | shell script classes; domain dependent | actual output | process events | executes | not general shell |
| exact historical process ran? | no | no | no | sometimes/log-dependent | **direct telemetry** | no, reconstructed run | no |
| exact network/file/process effects | no | no | no | incomplete | **direct runtime telemetry** | modeled local run | no |
| hosted-run environment fidelity | static only | static only | static only | **actual run** | **actual instrumented run** | limited/emulated | modeled program only |
| package-manager semantics | no | no | no generic answer | observed logs only | process observation only | executes tool locally | possible only if modeled/extracted |
| symbolic branch proof | no | no | CFG/dataflow not general SMT | no | no | concrete execution | **yes for bounded model** |
| target dependency decision | no | no | no | no | no | no | no |

---

## 14. Major independent findings

### Finding C1 — workflow semantics should be layered

The evidence supports at least:

\`\`\`text
Actions semantic layer
→ shell semantic layer
→ package-manager semantic layer
→ runtime observation layer
\`\`\`

Trying to make one parser own all four is likely a poor long-term abstraction.

### Finding C2 — CodeQL Actions is the strongest immediate challenge to bespoke workflow-graph work

Its dedicated AST + CFG + inter-step dataflow are directly relevant to:

- path relations;
- env propagation;
- conditions;
- reusable workflows;
- matrix/context relationships;
- security-relevant data flows.

This does **not** mean current UpgradePilot work was wrong.

It means future growth in these areas should compare against CodeQL before creating a parallel general workflow-analysis framework.

### Finding C3 — runtime instrumentation can convert inference into observation

StepSecurity demonstrates a practical path:

\`\`\`text
infer process execution from static structure
→ optional direct process observation
\`\`\`

For repositories/runs where telemetry is available, UpgradePilot could potentially strengthen facts without proving every shell/control-flow case statically.

### Finding C4 — observed runtime truth and emulated execution must remain different evidence classes

\`act\` is extremely useful, but its runner/environment fidelity limitations mean:

\`\`\`text
historical observed run
!=
locally reconstructed run
\`\`\`

The latter can be diagnostic/test evidence without being target-run authority.

### Finding C5 — static security analyzers add impact mechanisms UpgradePilot has not emphasized

Dependency updates can alter:

- GitHub Actions dependencies;
- permissions;
- template-injection exposure;
- action pinning;
- CI trust boundaries.

actionlint/zizmor/CodeQL Actions can become sources for future **CI-security impact candidates**, not only infrastructure validators.

### Finding C6 — symbolic execution is a targeted technique, not a general solution

CrossHair/angr are strongest when the proposition can be reduced to:

\`\`\`text
bounded program + symbolic inputs + explicit property/path
\`\`\`

They are weak fits for arbitrary CI systems with network/filesystem/package-manager effects.

### Finding C7 — existing analyzers can become evidence producers rather than architecture owners

UpgradePilot need not choose:

\`\`\`text
use CodeQL
OR
use its own domain model
\`\`\`

A stronger pattern may be:

\`\`\`text
CodeQL/actionlint/zizmor/runtime telemetry
→ typed external evidence producers

UpgradePilot
→ validates/binds/normalizes their outputs
→ composes them with package/upstream/runtime evidence
\`\`\`

### Finding C8 — “absence of a static path” needs analyzer-coverage semantics

This report reinforces the earlier Snyk/Socket lesson.

Whether using CodeQL, Joern, symbolic analysis, or custom logic:

\`\`\`text
no path found
\`\`\`

should not automatically become:

\`\`\`text
path impossible
\`\`\`

unless the analyzer/model coverage is sufficient for that proposition.

---

## 15. Direct implications for current Increment-3 direction

This report must not disrupt verified work on \`main\`.

The current package-manager/environment evidence work remains valuable because none of these tools directly answers the domain proposition:

\`\`\`text
what is the effective package-manager semantic state
for this exact operation/environment?
\`\`\`

However, before UpgradePilot substantially expands custom logic for:

- general GitHub Actions control flow;
- cross-step environment propagation;
- reusable workflows;
- matrix/context propagation;
- generic workflow data flow;

perform a CodeQL-Actions comparison experiment.

Likewise, before adding more static inference to prove exact historical execution, test whether runtime process telemetry can provide a stronger optional evidence source.

### Recommended future comparator

Use one real current UpgradePilot case involving:

\`\`\`text
earlier env/config producer
→ later pip command
→ conditional/path relation
\`\`\`

Implement:

1. current UpgradePilot result;
2. custom CodeQL Actions query result;
3. actionlint/zizmor diagnostics where relevant;
4. actual GitHub run evidence;
5. StepSecurity runtime telemetry if practical.

Then compare:

- proposition coverage;
- exactness;
- implementation complexity;
- runtime cost;
- provenance;
- false positive/negative behavior;
- learning value.

---

## 16. Learning / exposure opportunities

### CodeQL — **very high-priority hands-on candidate**

What it teaches:

- QL query language;
- AST/CFG/data-flow/taint analysis;
- GitHub Actions semantics;
- Python program analysis;
- query packs;
- SARIF/code scanning;
- security analysis.

Real experiment:

\`\`\`text
write custom CodeQL Actions query
→ trace env/context value across steps
→ identify package-manager run step
→ compare with UpgradePilot's current analysis
\`\`\`

Recommended exposure:
**HANDS_ON_EXPERIMENTED / project comparator candidate**.

### actionlint — **easy hands-on candidate**

What it teaches:

- workflow schema/expression semantics;
- shell integration;
- CI linting.

Experiment:
run against real UpgradePilot/product-simulation workflows and compare findings with our parser.

Recommended:
**HANDS_ON_EXPERIMENTED**.

### zizmor — **high-value CI-security lab**

What it teaches:

- CI/CD threat modeling;
- GitHub Actions security;
- template injection;
- permissions;
- action supply-chain risk;
- SARIF/autofix-style security tooling.

Recommended:
**HANDS_ON_EXPERIMENTED**, potentially useful in product CI-security candidate discovery.

### StepSecurity Harden-Runner — **high-value runtime/security experiment**

What it teaches:

- eBPF-backed runtime visibility;
- process/network/file telemetry;
- CI security policy;
- runtime provenance;
- agent/CI execution observability.

Experiment:
instrument one public GitHub Actions workflow and correlate package-manager process events to exact step/run identity.

Recommended:
**project experiment candidate** if community-tier telemetry is sufficient.

### act — **useful practical lab**

What it teaches:

- GitHub Actions execution model;
- Docker-based runner emulation;
- environment fidelity problems;
- reproducible workflow debugging.

Recommended:
**HANDS_ON_EXPERIMENTED**, but never as historical-run proof.

### Joern — **advanced program-analysis lab**

What it teaches:

- Code Property Graphs;
- Scala/CPGQL-style query thinking;
- taint/dataflow;
- custom graph passes;
- cross-language IR.

Recommended:
research now; hands-on if graph architecture remains strong after Track C.

### CrossHair — **strong formal-method learning lab**

What it teaches:

- symbolic execution;
- SMT solving;
- contracts;
- counterexample generation;
- proof limitations.

Recommended:
bounded hands-on lab on a pure UpgradePilot semantic function.

### angr — **security-learning lab**

What it teaches:

- binary symbolic execution;
- state/path exploration;
- constraint solving;
- reverse-engineering-oriented analysis.

Recommended:
learning lab only unless a future binary/native dependency case creates product need.

---

## 17. What should NOT be copied blindly

1. Do not replace verified UpgradePilot domain semantics with a general analyzer without proposition-by-proposition comparison.
2. Do not treat CodeQL CFG reachability as historical execution proof.
3. Do not treat StepSecurity process observation as proof of package-manager semantic success/state.
4. Do not treat \`act\` as equivalent to GitHub-hosted execution.
5. Do not add CodeQL solely because it is sophisticated; compare complexity/cost against current Python implementation.
6. Do not expand symbolic execution into side-effectful repository code without isolation.
7. Do not combine actionlint/zizmor security warnings directly into dependency-impact conclusions without a typed relation.
8. Do not create a universal graph abstraction merely because CodeQL/Joern use graphs.
9. Do not assume static negative results are complete unless analyzer coverage justifies them.
10. Do not let hands-on learning experiments silently become product dependencies.

---

## 18. Track-C hypotheses

1. UpgradePilot's workflow layer may benefit from delegating generic Actions AST/CFG/dataflow to CodeQL while retaining specialized shell/package-manager semantics.
2. Runtime telemetry should become a first-class optional evidence family distinct from logs and static inference.
3. Historical observation, emulated execution, static proof, and symbolic proof should have separate evidence types/authority.
4. Generic GitHub Actions security analyzers may become candidate-discovery inputs for CI-security impacts caused by dependency/action updates.
5. Runtime telemetry may reduce the need to support every shell control-flow pattern statically.
6. CodeQL/Joern results should likely be imported as evidence rather than becoming UpgradePilot's authoritative internal model.
7. Static environment propagation is an especially strong candidate for a CodeQL comparison experiment.
8. Symbolic execution should be applied only after a proposition is reduced to a bounded deterministic model.
9. Analyzer coverage/completeness should be first-class when interpreting negative findings.
10. Current package-manager semantic work remains independently justified because generic analyzers do not own that domain.

---

## 19. Sources checked

### actionlint
- https://github.com/rhysd/actionlint/

### zizmor
- https://docs.zizmor.sh/
- https://docs.zizmor.sh/quickstart/
- https://docs.zizmor.sh/audits/

### CodeQL
- https://codeql.github.com/docs/codeql-language-guides/codeql-library-for-actions/
- https://codeql.github.com/codeql-standard-libraries/actions/actions.qll/module.actions.html
- https://codeql.github.com/codeql-query-help/actions/
- https://codeql.github.com/docs/codeql-language-guides/analyzing-data-flow-in-python/
- https://codeql.github.com/docs/codeql-language-guides/analyzing-control-flow-in-python/

### GitHub Actions runtime
- https://docs.github.com/en/actions/how-tos/monitor-workflows/enable-debug-logging
- https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands
- https://docs.github.com/en/actions/reference/runners/github-hosted-runners
- https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax

### StepSecurity
- https://www.stepsecurity.io/github-actions-and-stepsecurity
- https://www.stepsecurity.io/cicd-security
- https://www.stepsecurity.io/blog/monitor-outbound-https-requests-from-github-actions-runners

### act
- https://github.com/nektos/act
- https://github.com/nektos/act-docs/blob/main/src/usage/runners.md

### Joern
- https://docs.joern.io/

### CrossHair
- https://crosshair.readthedocs.io/en/latest/contracts.html
- https://crosshair.readthedocs.io/en/latest/kinds_of_contracts.html
- https://crosshair.readthedocs.io/en/latest/cover.html

### angr
- https://docs.angr.io/en/stable/core-concepts/symbolic.html

---

## 20. Status / next report

**Tier-1 Report 05: COMPLETE.**

Next research family:

> **Tier-1 Report 06 — repository-intelligence and agent architectures**

Primary systems/research:

- RepoGraph;
- LocAgent;
- Repository Intelligence Graph;
- AutoCodeRover;
- SWE-agent;
- OpenHands;
- Agentless;
- modern repository-context/indexing and tool-use patterns.

Central question:

> what repository representation, retrieval/indexing strategy, tool interface, and agent topology best supports UpgradePilot's open-ended impact discovery and investigation without losing provenance, wasting context, or handing the model unnecessary authority?
