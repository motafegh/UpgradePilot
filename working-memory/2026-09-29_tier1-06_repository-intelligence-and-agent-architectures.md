# Tier 1 Report 06 — Repository Intelligence and Agent Architectures

**Recorded:** 2026-09-29  
**Branch:** `analysis/ai-agentic-capability-map-2026-09-28`  
**Status:** COMPLETE initial deep report  
**Research family:** Repository intelligence, context retrieval, and software-engineering agent architecture  
**Systems/research examined:** RepoGraph, LocAgent, Repository Intelligence Graph (RIG), CodexGraph, AutoCodeRover, CodeRAG-Bench/CodeRAG, Sourcegraph Code Graph/Cody, SWE-agent, OpenHands, Agentless, GitHub Copilot repository instructions/skills/MCP patterns  
**Purpose:** determine what repository representation, context-selection strategy, agent-computer interface, and reasoning topology best fit UpgradePilot's future open-ended impact discovery and investigation responsibilities without wasting context, losing provenance, or granting unnecessary model authority.

This report records external research evidence only. It does not authorize a repository graph, general software agent, external framework, or product architecture change.

---

## 1. Research questions

1. What should a model/agent actually see about a repository?
2. Is a flat file tree/raw source sufficient?
3. When do code graphs outperform lexical/semantic retrieval?
4. Should build/test architecture be represented separately from code structure?
5. How should an agent navigate source without flooding context?
6. How much repository search should be fixed/deterministic versus model-selected?
7. How important is the agent tool interface itself?
8. When does an adaptive agent outperform a fixed staged pipeline?
9. How should repository instructions, skills, tools, graphs, and raw files compose?
10. Which patterns could support UpgradePilot impact discovery without becoming an autonomous coding-agent product?
11. Which technologies deserve hands-on exposure for learning/career value?

---

## 2. Executive result

The strongest independent conclusion is:

> **Repository intelligence is not one thing.**

The reviewed systems separate at least five distinct responsibilities:

```text
A. STRUCTURAL WORLD MODEL
   files / symbols / imports / calls / inheritance
   RepoGraph, LocAgent, CodexGraph, Sourcegraph Code Graph

B. BUILD / TEST ARCHITECTURE
   buildable components / runners / tests / package managers / coverage
   Repository Intelligence Graph

C. CONTEXT LOCALIZATION / RETRIEVAL
   lexical, semantic, graph traversal, AST search, fault localization
   CodeRAG, AutoCodeRover, Sourcegraph, LocAgent

D. REPOSITORY KNOWLEDGE / INSTRUCTIONS
   AGENTS.md, path instructions, skills, project conventions
   GitHub Copilot and other production coding-agent patterns

E. AGENT-COMPUTER INTERFACE / EXECUTION LOOP
   file view/edit/search, shell, tests, sandbox, history compression
   SWE-agent, OpenHands

F. REASONING TOPOLOGY
   fixed localization → reasoning → validation
   vs adaptive agent loop
   Agentless vs SWE-agent/OpenHands
```

This means an architecture described only as:

```text
"give the LLM repository context"
```

is underspecified.

A mature system must decide:

- which repository representation exists;
- how it was derived;
- which parts are authoritative versus heuristic;
- how context is selected;
- which raw source can be retrieved on demand;
- what stable repository instructions are injected;
- which tools/actions the model can invoke;
- how much the model controls sequencing;
- how observations return to trusted state.

The strongest current UpgradePilot research hypothesis is **not** one giant repository graph and not one generalist agent.

It is a layered, queryable repository-intelligence substrate:

```text
exact repository revision

├─ source/symbol structure
├─ build/test/CI architecture
├─ package/dependency/environment evidence
├─ product-specific evidence/propositions
├─ repository instructions/purpose/policy
└─ exact raw source retrievable on demand

          ↓ query / retrieve

bounded semantic reasoner or investigation planner

          ↓

deterministic validation / trusted-state update
```

The model should not have to reconstruct stable repository structure repeatedly from raw files, but neither should it be permanently confined to a lossy preselected summary.

---

## 3. RepoGraph — repository code graph as reusable context

### 3.1 Core concept

RepoGraph research argues that LLM software-engineering systems underperform when repositories are treated as independent flat files.

RepoGraph builds a repository-level code graph and provides it as a plug-in to existing software-engineering methods.

The ICLR 2025 paper reports improvements when RepoGraph is added to four systems across two types of approaches on SWE-bench, and also evaluates it on CrossCodeEval.

The key pattern is:

```text
repository source
→ structural graph
→ reusable navigation/context layer
→ existing reasoner/agent
```

The graph is not necessarily the reasoner.

### 3.2 Why this matters for UpgradePilot

This directly challenges two inefficient extremes:

```text
EXTREME 1
model receives raw files
and reconstructs all structure each time

EXTREME 2
UpgradePilot hand-builds one bespoke extractor
for every new semantic question
```

A shared repository graph can preserve stable structural knowledge once and support many later queries.

### 3.3 Scope limitation

A traditional code graph usually represents things such as:

- files;
- functions/classes;
- imports;
- references;
- calls;
- inheritance.

That is useful but insufficient for UpgradePilot's full world:

- GitHub Actions jobs/steps;
- package-manager operations;
- external package versions;
- build/test artifacts;
- runtime observations;
- upstream release evidence;
- maintainer policy.

Therefore a RepoGraph-style code structure should be treated as one **view** of the repository, not automatically the universal evidence graph.

### 3.4 Transferable idea

> Build deterministic/queryable repository structure once; let different reasoning components consume it instead of repeatedly re-discovering it.

Sources:
- RepoGraph, ICLR 2025: https://proceedings.iclr.cc/paper_files/paper/2025/hash/4a4a3c197deac042461c677219efd36c-Abstract-Conference.html

---

## 4. LocAgent — graph-guided multi-hop localization

### 4.1 Core architecture

LocAgent represents a codebase as a directed heterogeneous graph.

Documented graph concepts include:

- files;
- classes;
- functions;

with relationships such as:

- containment;
- imports;
- invocation/calls;
- inheritance.

The agent is given graph-navigation capabilities and performs multi-hop exploration to locate the code relevant to a natural-language issue.

### 4.2 Empirical result

The ACL 2025 paper reports up to:

- 92.7% file-level localization accuracy;
- downstream issue-resolution improvement under multiple attempts;
- substantially lower model cost compared with proprietary-model baselines in the reported setting.

The significant point for UpgradePilot is not the exact benchmark number.

It is:

> **multi-hop structural navigation can outperform asking the model to infer repository topology from text retrieval alone.**

### 4.3 Implication for dependency-update analysis

A dependency-update mechanism may touch code indirectly:

```text
dependency API
→ adapter module
→ framework integration
→ configuration layer
→ tests
```

Lexical search for the package name can miss relevant wrappers or abstractions.

A graph traversal can discover structural neighbors even when the exact dependency name disappears behind an internal abstraction.

### 4.4 Risk

Graph search inherits graph-construction limits.

If:

- dynamic imports;
- dependency injection;
- plugin loading;
- reflection;
- framework magic;

are missing from the graph, then graph-localization recall can be misleading.

Therefore:

```text
graph says connected
→ strong structural evidence

graph has no edge
→ not automatically proof of non-relation
```

This mirrors the negative-reachability lesson from Tier-1 Report 02.

Source:
- https://aclanthology.org/2025.acl-long.426/

---

## 5. Repository Intelligence Graph (RIG) — build/test architecture as an authoritative view

### 5.1 Different graph, different responsibility

RIG is particularly useful because it does **not** attempt to represent all source-code semantics.

It intentionally focuses on repository build/test architecture.

Its graph includes:

- buildable components;
- aggregators/orchestration targets;
- runners;
- test definitions;
- external packages;
- package managers;

connected by evidence-backed dependency and coverage relations derived from build/test artifacts.

### 5.2 Deterministic extraction

The accompanying SPADE extractor derives RIG from concrete build/test metadata.

The reported implementation currently emphasizes CMake/CTest-oriented extraction.

The graph is then exposed as an LLM-friendly structured view.

### 5.3 Empirical result

Across three commercial coding agents and eight repositories, the paper reports:

- mean accuracy improvement of 12.2%;
- completion-time reduction of 53.9%;
- larger gains on multilingual repositories.

The key qualitative result is especially important:

> supplying correct structural architecture shifts failures away from misunderstanding repository structure toward reasoning mistakes over an accurate structure.

### 5.4 Major UpgradePilot implication

This supports a concept that differs from a source-code graph:

```text
CODE GRAPH
who calls/imports whom?

BUILD/TEST GRAPH
what builds what?
what test covers what?
what runner executes what?
what package manager contributes to what?
```

UpgradePilot likely needs both kinds of questions.

Therefore Track C should challenge the idea of one universal graph.

A better mature model may be:

```text
shared identities
+
multiple evidence-backed graph views
```

where each graph makes only the claims justified by its extractor.

Source:
- https://arxiv.org/abs/2601.10112

---

## 6. CodexGraph — agent-generated graph queries over a graph database

### 6.1 Core concept

CodexGraph stores code-repository structure in a graph database and lets an LLM agent generate graph queries.

The architecture is:

```text
repository
→ graph extraction
→ graph database

natural-language task
→ LLM generates structured graph query
→ precise graph retrieval/navigation
→ returned code context
→ downstream reasoning
```

The reported implementation uses a unified graph schema and graph-query language.

### 6.2 Why this differs from fixed graph tools

LocAgent can expose specialized graph-navigation tools.

CodexGraph instead gives the model a more general query interface.

This creates an important architecture axis:

```text
fixed domain graph tools
vs
general graph query language
```

### 6.3 Trade-off

A general graph query interface gives flexibility but increases model responsibility:

- it must formulate a useful query;
- understand graph schema;
- interpret results;
- recover from bad queries.

For UpgradePilot, a graph database does not automatically imply letting the model freely write arbitrary queries.

A safer alternative could expose selected query capabilities while retaining a graph backend.

### 6.4 Learning relevance

This method strongly supports a later graph-database/GraphQL/Cypher comparison, particularly alongside GUAC.

Source:
- https://arxiv.org/abs/2408.03910

---

## 7. Sourcegraph Code Graph / Cody — production repository intelligence

### 7.1 Production-scale code intelligence

Sourcegraph's Code Graph indexes semantic information such as:

- symbol definitions;
- references;
- symbols;
- documentation relationships.

The graph/index is built using language-aware indexing and can be produced automatically or via CI indexing.

Cody then uses Sourcegraph search and code intelligence to retrieve context for LLM interactions.

### 7.2 Architecture pattern

The public model is roughly:

```text
repository indexing / Code Graph
+
code search
+
permission filtering

→ selected context snippets
→ LLM
```

This is a mature production precedent for separating:

```text
context retrieval
from
model inference
```

### 7.3 Context selection remains explicit

Cody also allows users to:

- attach specific files;
- attach symbols/directories/repositories;
- constrain context;
- rerun with different context.

This reinforces the broader research finding:

> even with strong automatic indexing, explicit context control remains useful.

### 7.4 UpgradePilot implication

UpgradePilot's future semantic component might benefit from:

```text
structural search/query service
+
explicit evidence projection
+
on-demand raw source
```

instead of dumping all repository files into a model request.

Sources:
- https://sourcegraph.com/docs/cody/core-concepts/code-graph
- https://sourcegraph.com/docs/cody

---

## 8. Retrieval is valuable but noisy — CodeRAG-Bench

### 8.1 Core finding

CodeRAG-Bench evaluates multiple retrievers and language models across repository-level and other code tasks.

It reports two simultaneous truths:

```text
high-quality retrieved context
→ improves generation

but

retrievers often fail to retrieve useful context
and
models sometimes fail to exploit retrieved context
```

This means “add RAG” is not an architecture answer.

### 8.2 UpgradePilot implication

Repository retrieval needs its own evaluation:

- recall of decision-relevant evidence;
- irrelevant-context rate;
- provenance;
- source-revision correctness;
- amount of context;
- whether downstream reasoning actually uses the evidence.

### 8.3 Context type matters

Earlier dependency-specific research (DepRepair) independently found that distilled migration evidence outperformed raw upstream context.

Together the evidence suggests:

```text
raw repository context
→ potentially high recall but noisy

generic embedding retrieval
→ potentially relevant but lossy

structural graph retrieval
→ relationship aware but extractor limited

typed evidence projection
→ precise but risks preselection loss
```

A mature system may need all four as selectable context sources.

Source:
- https://aclanthology.org/2025.findings-naacl.176/

---

## 9. AutoCodeRover — AST-aware search + test-driven localization

### 9.1 Software-engineering-oriented search

AutoCodeRover explicitly rejects treating a repository as only files.

It searches over program structure such as:

- classes;
- methods;
- AST entities;

and iteratively retrieves context based on the issue.

### 9.2 Test evidence sharpens search

When tests exist, AutoCodeRover adds spectrum-based fault localization.

That creates:

```text
structural repository model
+
actual test execution behavior
→ better localization
```

This is highly relevant to UpgradePilot's future candidate-discovery problem.

For example:

```text
upstream symbol changed
→ structural target search gives candidate usages

plus

affected tests/runtime coverage
→ prioritize candidates
```

### 9.3 Strong lesson

The best context source can depend on the available evidence:

```text
no tests
→ structural search

tests available
→ structural + dynamic localization
```

That argues against one fixed retrieval mechanism.

Source:
- https://arxiv.org/abs/2404.05427

---

## 10. SWE-agent — the tool interface is itself part of intelligence

### 10.1 Agent-Computer Interface (ACI)

SWE-agent's key thesis is that an LLM is a computer user with interface requirements different from a human's.

Its custom ACI substantially changes performance.

Important design observations include:

- limited-window file viewing rather than dumping files;
- succinct repository search results;
- edit operations with linting/validation;
- explicit working-directory/open-file state;
- clear feedback when commands return no output;
- tool documentation optimized for model use;
- trajectory/history processing.

### 10.2 Important context lesson

SWE-agent found that showing more context for each search match could confuse the model.

Its default design instead showed a concise list of matching files and let the model inspect selectively.

This is an important independent challenge to:

```text
more context = better
```

### 10.3 State after every action

SWE-agent's tool system exposes an explicit state command after actions.

This is conceptually valuable:

```text
agent action
→ deterministic environment effect
→ explicit observed state
→ next reasoning turn
```

That is close to the architecture we have considered for bounded investigation, although SWE-agent gives much broader operational freedom.

### 10.4 Current project status

Current SWE-agent documentation states that SWE-agent has been superseded by **mini-swe-agent**, with SWE-agent itself in maintenance-only mode.

Therefore learning should focus on its **ACI principles**, not necessarily on adopting the legacy framework.

### 10.5 UpgradePilot implication

Tool design deserves independent evaluation.

An agent offered:

```text
read_repository()
```

and an agent offered:

```text
find_symbol()
find_callers()
get_dependency_evidence()
get_workflow_path()
get_exact_source_range()
run_admitted_check()
```

are not equivalent systems even if both use the same model.

Sources:
- https://swe-agent.com/latest/background/aci/
- https://swe-agent.com/latest/background/architecture/

---

## 11. OpenHands — generalist agent + sandbox/runtime platform

### 11.1 Product architecture

OpenHands represents the broad generalist-agent architecture.

Its platform supports agents that can:

- write/read code;
- use shell commands;
- browse the web;
- run tools;
- operate in sandboxed environments;
- integrate with repository workflows;
- support multiple models;
- integrate MCP/tool servers;
- manage conversations/iterations;
- perform issue/PR resolution.

The newer OpenHands SDK emphasizes:

- composable agent implementations;
- local-to-remote execution portability;
- sandboxed execution;
- lifecycle control;
- multi-model routing;
- security analysis;
- user interfaces/APIs.

### 11.2 GitHub workflow integration

OpenHands can be triggered from issues/PRs, work iteratively, and receive follow-up feedback through review/comments.

This is a real production-style example of:

```text
repository issue
→ general agent
→ sandboxed work
→ pull request
→ human review
→ follow-up agent iteration
```

### 11.3 Context/tool architecture

OpenHands exposes broad tools rather than only a narrow problem-specific evidence projection.

That is an important competitor to UpgradePilot's bounded planner architecture.

### 11.4 Strength

A generalist agent can handle unexpected repository structures and custom scripts without requiring every capability to be predesigned.

### 11.5 Risk

The flexibility creates corresponding problems:

- longer trajectories;
- more actions;
- more execution risk;
- context management;
- higher cost;
- difficult replay/evaluation;
- greater chance of investigating irrelevant paths;
- larger prompt-injection/untrusted-repository surface.

### 11.6 UpgradePilot implication

OpenHands is the strongest “broad-agent” baseline we should compare against later.

The question should not be:

> can OpenHands inspect a repo?

It clearly can.

The relevant question is:

> for UpgradePilot's evidence/decision problem, does a generalist agent produce better coverage/usefulness than a structured evidence pipeline at acceptable authority/cost/replay risk?

Sources:
- https://arxiv.org/abs/2407.16741
- https://arxiv.org/abs/2511.03690
- https://docs.openhands.dev/openhands/usage/run-openhands/github-action

---

## 12. Agentless — fixed pipelines remain a mandatory baseline

### 12.1 Core architecture

Agentless deliberately removes adaptive tool-selection.

Its pipeline is roughly:

```text
hierarchical localization
→ repair generation
→ patch validation/selection
```

Localization progressively narrows:

- repository/file level;
- class/function level;
- fine-grained locations.

Repair generates multiple candidates around localized regions.

Validation uses tests/reproduction evidence and candidate selection.

### 12.2 Why it matters for UpgradePilot

Agentless demonstrates that a well-designed fixed pipeline can beat more autonomous systems when the task stages are sufficiently understood.

This should become a permanent evaluation principle:

> **Every proposed UpgradePilot agent should be compared against the strongest fixed deterministic/model pipeline that solves the same responsibility.**

### 12.3 Particularly relevant analogy

For UpgradePilot impact investigation:

```text
FIXED PIPELINE
transition
→ candidate discovery
→ localization
→ applicability
→ predetermined targeted checks
→ report

vs

AGENT
state
→ choose any next evidence action
→ update state
→ repeat
```

The agent should only win when the value of the next action genuinely depends on intermediate results in a way a fixed pipeline handles poorly.

Source:
- https://arxiv.org/abs/2407.01489

---

## 13. Repository instructions, skills, and MCP — production context has another layer

### 13.1 GitHub Copilot current pattern

Modern GitHub Copilot supports multiple persistent repository-context mechanisms:

- repository-wide instructions;
- path-specific instructions;
- `AGENTS.md` / agent instructions;
- agent skills (`SKILL.md` + resources/scripts);
- MCP servers for external tools/data.

This matters because repository understanding is not derived only from source code.

Repositories contain **human-authored operational knowledge** such as:

- how to build/test;
- conventions;
- which areas are authoritative;
- project-specific policies;
- domain vocabulary.

### 13.2 Skills are selective context

GitHub describes skills as detailed task-specific instructions/resources that the agent loads when relevant, rather than injecting all guidance into every request.

This is another independent example of:

```text
large knowledge base
→ selective context activation
```

### 13.3 UpgradePilot implication

UpgradePilot already uses governance, AGENTS.md, skills, plans, and working memory.

The external product trend suggests these should be recognized as an explicit repository knowledge layer rather than treated as incidental prompt text.

Potential mature distinction:

```text
SOURCE FACTS
what code/config says

STRUCTURAL FACTS
what analyzers/graphs derive

PROJECT KNOWLEDGE
what maintainers explicitly declare

OPERATIONAL MEMORY
what prior runs/evaluations established
```

Each has different authority/freshness.

Sources:
- GitHub Copilot repository instructions documentation
- GitHub Copilot agent skills documentation
- GitHub Copilot MCP/customization documentation

---

## 14. Cross-system comparison

| System/method | Main repository representation | Context selection | Agent autonomy | Execution feedback | Key strength | Core limitation |
| --- | --- | --- | --- | --- | --- | --- |
| RepoGraph | repository code graph | graph neighbors/structure | external reasoner dependent | no | reusable structure | extractor coverage |
| LocAgent | heterogeneous file/class/function graph | agent multi-hop graph navigation | medium | mostly localization-oriented | strong localization | graph completeness |
| RIG | deterministic build/test graph | supplied structured architecture | low/consumer-defined | no direct execution | authoritative build/test context | narrow extractor scope |
| CodexGraph | graph DB | model-generated graph queries | medium/high | no inherent runtime | flexible graph navigation | query/schema burden |
| Sourcegraph | indexed symbols/references + search | automatic + user-selected | low/assistant dependent | no inherent runtime | production code intelligence | not decision-specific |
| AutoCodeRover | AST + search + test fault signals | iterative structural localization | bounded | yes, tests | evidence-guided localization | repair-task specific |
| SWE-agent | raw repo through optimized ACI | model chooses search/view | high | yes | interface design | broad trajectory/cost |
| OpenHands | broad repo + tools + sandbox | model/tool loop | high | yes | generality | authority/security/cost |
| Agentless | hierarchical summaries/context | fixed staged localization | low | validation/tests | simplicity/cost | less adaptive |
| CodeRAG/RAG | retrieved chunks/documents | retriever | low/varies | no inherent | cheap broad retrieval | relevance/noise |

---

## 15. Major independent findings

### Finding RI1 — world model, retrieval, and reasoning should remain separate responsibilities

A repository graph is not a retrieval algorithm.

A retrieval system is not a reasoner.

An agent loop is not a world model.

Conflating them hides architectural choices.

### Finding RI2 — structural context consistently improves repository reasoning

RepoGraph, LocAgent, RIG, AutoCodeRover, CodexGraph, and Sourcegraph all independently support some form of:

```text
explicit structure
> flat bag of files
```

for important repository tasks.

This is now a strong external pattern.

### Finding RI3 — there may be multiple legitimate repository graphs

At minimum:

```text
CODE STRUCTURE GRAPH
symbols / calls / imports

BUILD-TEST GRAPH
components / tests / runners / package managers

SUPPLY-CHAIN / EVIDENCE GRAPH
packages / artifacts / attestations / vulnerabilities

UPGRADEPILOT PROPOSITION GRAPH
claims / evidence / unresolved relationships
```

Trying to force these into one universal ontology too early may reduce clarity.

A federated/multi-view model with stable identities may be stronger.

### Finding RI4 — context should be progressively disclosed

SWE-agent, RAG research, and DepRepair all provide evidence that excessive raw context can reduce effectiveness.

A strong context flow may be:

```text
compact structural/evidence summary
→ targeted query
→ exact source range
→ broader raw context only when needed
```

### Finding RI5 — raw source access should not be banned categorically

The independent research does **not** support a permanent rule that models should only ever see narrow typed projections.

For open-ended discovery, controlled raw-source access can be necessary.

A better distinction is:

```text
trusted state used for authority
vs
model-visible source/context used for discovery
```

Raw source can be visible without automatically becoming trusted evidence.

### Finding RI6 — the agent-computer interface materially affects model capability

SWE-agent shows that tool/interface design changes performance.

Therefore model evaluation without fixing the tool interface can be misleading.

UpgradePilot's future planner evaluation must specify:

- available tools;
- observation format;
- context limits;
- action granularity;
- error feedback;
- state projection.

### Finding RI7 — fixed pipelines remain the correct baseline

Agentless and DepRepair together strongly support:

```text
structured fixed pipeline
before
adaptive agent
```

unless adaptivity has measurable value.

### Finding RI8 — deterministic repository maps can reduce agent work and cost

RIG demonstrates that supplying authoritative structural context can improve both accuracy and speed.

This suggests future UpgradePilot agents should not spend tokens/actions rediscovering mechanical facts that deterministic extraction can provide.

### Finding RI9 — project instructions/skills form a separate knowledge layer

AGENTS.md, path-specific instructions, skills, and similar mechanisms carry explicit maintainer knowledge not inferable reliably from code structure.

This should not be mixed blindly with derived evidence.

### Finding RI10 — graphs themselves need provenance/coverage

A graph edge should eventually answer:

```text
why does this edge exist?
which extractor produced it?
from which revision?
with what confidence/coverage?
```

This links Tier-1 Report 06 back to Tier-1 Report 04's provenance findings.

---

## 16. Direct implications for UpgradePilot

### 16.1 Keep current typed evidence work

The current project direction still has value.

Repository graphs do not replace:

- exact package-manager semantics;
- source identity;
- evidence provenance;
- runtime observation;
- target decision logic.

### 16.2 Do not make typed projections the only possible model context

For bounded trusted propositions, typed projections remain ideal.

For broad discovery, an agent/model may need:

- graph navigation;
- lexical/semantic search;
- exact source ranges;
- upstream source/docs;
- repository instructions.

The architecture should separate **model visibility** from **trusted authority**.

### 16.3 Consider a repository-intelligence service boundary

A future service/component might expose capabilities such as:

```text
find_symbol
find_references
find_callers
find_callees
find_importers
find_tests_for_component
find_build_owner
find_package_usage
find_ci_consumers
retrieve_exact_source
search_repository
get_repository_instruction
```

Backends could evolve independently:

- simple parser;
- CodeQL;
- Sourcegraph;
- custom graph;
- build/test graph;
- search index.

This is more flexible than hardwiring one graph implementation into product semantics.

### 16.4 Prefer evidence-backed multi-view graphs over universal graph ambition

Potential mature shape:

```text
RepositoryIdentity
     │
     ├── CodeStructureView
     ├── BuildTestView
     ├── WorkflowView
     ├── DependencyView
     ├── SupplyChainView
     └── DecisionEvidenceView
```

Relations across views are admitted only when evidence supports them.

### 16.5 Broad impact discovery is still a strong LLM candidate

A model can search/navigate these views to ask:

- which target components could be affected?
- what mechanism explains the link?
- what evidence is missing?
- which source range should be inspected next?

But applicability/authority can still be evaluated separately.

### 16.6 Agent adaptivity should be justified at the evidence-action level

A full OpenHands-style generalist agent is probably excessive for routine cases.

A stronger staged escalation might be:

```text
deterministic extraction
→ fixed semantic/discovery pipeline

if material uncertainty remains
AND several useful evidence actions exist
→ bounded investigation agent

if repository is genuinely atypical
→ optional broader generalist investigation
```

This is a hypothesis for Track C.

---

## 17. Candidate context architecture for later comparison

Not adopted; recorded as an independently derived option:

```text
EXACT REVISION
     │
     ├── deterministic repository maps
     │     ├─ code/symbol graph
     │     ├─ build/test graph
     │     ├─ workflow graph
     │     └─ dependency graph
     │
     ├── UpgradePilot trusted evidence/propositions
     │
     ├── maintainer/project knowledge
     │     ├─ AGENTS.md
     │     ├─ project instructions
     │     └─ selected skills/policies
     │
     └── raw-source retrieval interface
           ├─ exact file/range
           ├─ search
           ├─ references
           └─ upstream evidence

                  ↓

          CONTEXT SELECTOR
      fixed retrieval or bounded agent

                  ↓

            MODEL / REASONER

                  ↓

      structured candidate hypothesis
      or evidence-action proposal

                  ↓

     deterministic validation/admission

                  ↓

          trusted next state
```

Key property:

> **The context selector may be intelligent without the context becoming authoritative merely because the model saw it.**

---

## 18. Recommended comparison experiments

### Experiment 1 — graph vs raw/lexical localization

Choose one real dependency-impact case.

Compare:

1. grep/lexical search;
2. semantic/vector retrieval;
3. code graph traversal;
4. CodeQL/structural query;
5. model-guided graph navigation.

Measure:

- relevant-location recall;
- irrelevant context;
- tokens;
- latency;
- provenance;
- missed indirect usage.

### Experiment 2 — RIG-style build/test map for UpgradePilot

Build a very small deterministic map for one Python repo:

```text
package/module
→ test
→ CI job
→ runner
→ package-manager operation
```

Compare a model's answers with and without the map.

Do not build a universal graph; prove the value first.

### Experiment 3 — fixed pipeline vs adaptive planner

Use the same evidence gap.

Compare:

```text
fixed action sequence
vs
current EvidenceGapPlanner
vs
broader repo-navigation agent
```

Measure:

- evidence acquired;
- actions used;
- unnecessary exploration;
- cost;
- stopping behavior;
- wrong authority claims.

### Experiment 4 — Sourcegraph/CodeQL/simple graph backend

Expose the same abstract query:

```text
find references / callers / affected tests
```

through different backends.

Determine whether UpgradePilot benefits more from:

- external mature engine;
- minimal custom index;
- or no persistent repository graph.

### Experiment 5 — repository instructions as explicit evidence/context

Give the model:

1. source only;
2. source + AGENTS/project instructions;
3. source + structured repository-purpose summary;
4. source + both.

Measure whether purpose/policy reasoning improves and whether instructions can incorrectly override source facts.

---

## 19. Learning / exposure opportunities

### Code graph implementation — **high-value project lab**

Candidate stacks:

- Tree-sitter;
- NetworkX/SQLite/graph store;
- SCIP/ctags where appropriate;
- CodeQL-derived structure;
- Neo4j/Cypher as an alternative.

What it teaches:

- AST extraction;
- graph schema design;
- symbol resolution;
- graph traversal;
- impact analysis;
- source provenance.

Recommended exposure:
**HANDS_ON_EXPERIMENTED**, preferably with a deliberately small Python repository graph before any product integration.

### LocAgent / RepoGraph concepts — **high conceptual + experimental value**

Experiment:
construct a small file/class/function graph and expose graph-navigation tools to a local model.

Skills:

- heterogeneous graph modeling;
- multi-hop agent search;
- context budgeting;
- localization evaluation.

### Repository Intelligence Graph — **strong project-learning candidate**

Implement a small Python-specific RIG-like map from:

- pyproject/test config;
- pytest collection;
- GitHub Actions;
- package-manager evidence.

Skills:

- build/test architecture;
- coverage relationships;
- evidence-backed graphs;
- Pydantic schemas;
- agent context design.

This may align unusually well with UpgradePilot if bounded carefully.

### Neo4j / Cypher — **useful graph-database lab**

CodexGraph makes this relevant.

A bounded lab could:

- load a small code graph into Neo4j;
- write Cypher queries;
- let a model generate constrained read-only queries;
- compare against typed graph tools.

Recommended:
learning lab unless graph-db need becomes real.

### Sourcegraph Code Graph / search — **valuable production-system exposure**

Even without adopting Sourcegraph, studying or using its search/code-intelligence interface teaches:

- semantic indexing;
- symbols/references;
- enterprise repository search;
- context retrieval.

Recommended:
research + hands-on if accessible without disproportionate setup.

### SWE-agent / mini-swe-agent ACI concepts — **very high agent-engineering value**

The legacy SWE-agent framework itself is now maintenance-only, but its ACI principles remain highly valuable.

Hands-on candidate:
build a tiny UpgradePilot-specific agent tool bundle with:

- constrained file view;
- symbol/graph search;
- evidence query;
- read-only check execution;
- explicit post-action state.

Skills:

- tool design;
- observation shaping;
- context control;
- trajectory logging;
- agent evaluation.

### OpenHands — **high-value generalist-agent comparator**

Hands-on value:

- sandboxed software agent;
- model/tool loop;
- MCP;
- GitHub issue/PR workflow;
- budget/iteration management;
- security controls.

Recommended:
bounded comparator experiment, not product dependency.

### Retrieval/RAG evaluation — **important AI-engineering skill**

Use a small corpus of repository files/evidence and compare:

- BM25/lexical;
- embedding retrieval;
- graph retrieval;
- hybrid retrieval.

Measure actual recall/precision rather than relying on intuition.

### GitHub Copilot instructions / skills / MCP — **already highly relevant**

UpgradePilot already has:

- AGENTS-style governance;
- skills;
- tool/connector concepts.

A future learning note should explicitly compare our governance/skills approach against current GitHub Copilot agent-instruction/skill conventions.

This provides useful practical experience in modern repository-agent customization.

---

## 20. What should NOT be copied blindly

1. Do not build Neo4j/graph infrastructure before a query/value experiment proves the need.
2. Do not treat a graph edge as truth without extractor/revision/coverage provenance.
3. Do not feed the full repository graph to every model call.
4. Do not permanently prohibit raw-source access for discovery.
5. Do not let repository instructions override observed source/evidence facts.
6. Do not assume semantic/vector retrieval has adequate recall without measurement.
7. Do not equate localization benchmark success with dependency-impact correctness.
8. Do not adopt OpenHands/generalist agents when a fixed pipeline is adequate.
9. Do not copy SWE-agent framework architecture merely because the ACI research is useful; the project itself is now maintenance-only/superseded.
10. Do not make the code graph, build graph, supply-chain graph, and decision-evidence graph one ontology before proving cross-view value.
11. Do not let model-generated graph queries mutate graph state or bypass read-only evidence boundaries without independent admission.
12. Do not treat model-selected context as complete evidence coverage.

---

## 21. Track-C hypotheses

1. UpgradePilot should distinguish repository **world models**, **retrieval**, **reasoning**, and **authority** rather than calling all of them “context.”
2. Multiple evidence-backed repository views may be stronger than one universal graph.
3. Structural repository context should be precomputed where mechanical and reused by models/agents.
4. Controlled raw-source access should remain available for open-ended discovery.
5. Fixed pipelines remain the default baseline; agents earn adoption only when adaptive evidence selection measurably helps.
6. A repository-intelligence capability interface may be more stable than committing to one graph backend.
7. Build/test architecture deserves its own first-class representation, not only symbol/call structure.
8. AGENTS.md/skills/project instructions should be modeled as maintainer-declared knowledge, distinct from source-derived facts.
9. Context retrieval quality/coverage must be evaluated separately from model reasoning quality.
10. Agent tool interface and observation format are part of the algorithm and must be frozen during comparative evaluation.
11. OpenHands-style broad agents are useful as comparators/escalation mechanisms, not obviously as the default product architecture.
12. A small RIG/LocAgent-style experiment may have unusually high combined product + learning value for UpgradePilot.

---

## 22. Sources checked

### Repository graphs / intelligence
- https://proceedings.iclr.cc/paper_files/paper/2025/hash/4a4a3c197deac042461c677219efd36c-Abstract-Conference.html
- https://aclanthology.org/2025.acl-long.426/
- https://arxiv.org/abs/2601.10112
- https://arxiv.org/abs/2408.03910
- https://sourcegraph.com/docs/cody/core-concepts/code-graph
- https://sourcegraph.com/docs/cody

### Retrieval / localization
- https://aclanthology.org/2025.findings-naacl.176/
- https://arxiv.org/abs/2404.05427

### Agent architectures
- https://arxiv.org/abs/2405.15793
- https://swe-agent.com/latest/background/aci/
- https://swe-agent.com/latest/background/architecture/
- https://arxiv.org/abs/2407.16741
- https://arxiv.org/abs/2511.03690
- https://docs.openhands.dev/openhands/usage/run-openhands/github-action
- https://arxiv.org/abs/2407.01489

### Production repository-agent context
- GitHub Copilot repository custom instructions documentation
- GitHub Copilot agent skills documentation
- GitHub Copilot customization/MCP documentation

---

## 23. Status / next report

**Tier-1 Report 06: COMPLETE.**

Next research family:

> **Tier-1 Report 07 — evaluation, maintainer UX, and decision-quality measurement**

Primary areas:

- BUMP;
- DepBench / DepRepair;
- SWE-bench / SWE-bench Verified / software-agent evaluation methodology;
- replay and protected evaluation;
- calibration/selective prediction;
- maintainer review/decision-support research;
- dashboards, explanation, prioritization, and human-in-the-loop evaluation.

Central question:

> how should UpgradePilot prove that its evidence, AI components, investigation, and final maintainer output are actually useful and trustworthy—without optimizing only for benchmark accuracy, test pass rate, or a persuasive report?
