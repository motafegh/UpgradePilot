# Tier 1 Report 02 — Dependency Risk, Reachability, and Upgrade-Impact Platforms

**Recorded:** 2026-09-29  
**Branch:** `analysis/ai-agentic-capability-map-2026-09-28`  
**Status:** COMPLETE initial deep report  
**Research family:** Dependency risk, reachability, and upgrade-impact platforms  
**Systems examined:** Endor Labs, Semgrep Supply Chain, Snyk Open Source, Socket  
**Purpose:** test whether UpgradePilot's provisional product-space hypothesis is already occupied by systems that combine target-specific dependency analysis, reachability, breaking-change analysis, remediation planning, AI reasoning, and maintainer-facing evidence.

This report records external research evidence. It does not change UpgradePilot architecture, specifications, live plans, or `main`.

---

## 1. Research questions

1. How does each system represent the dependency/application relationship?
2. How does it distinguish “dependency present” from “dependency relevant/reachable”?
3. Does it analyze what changes between old and proposed dependency versions?
4. Does it connect upstream changes to exact target usage?
5. Does it reason about breaking changes, not only vulnerabilities?
6. Which parts are static/deterministic, AI-assisted, human-curated, or runtime-derived?
7. How are uncertainty, unsupported analysis, and incomplete reachability represented?
8. What remediation/fix actions are produced?
9. What product question remains for the maintainer?
10. Which ideas should later challenge UpgradePilot's current architecture?

---

## 2. Executive result

Tier-1 Report 01's broad hypothesis—

> target-specific dependency-update impact analysis is largely underserved

—is **too broad and is corrected by this report**.

At least two reviewed products now explicitly occupy important parts of that space:

- **Endor Labs**: dependency call graphs + reachability + direct-dependency Upgrade Impact Analysis that diffs dependency versions and maps changed symbols onto application call paths.
- **Semgrep Supply Chain**: first-party code analysis + third-party dependency-version analysis + LLM-generated breaking-change/upgrade guidance, including line-level breaking-change reporting and Autofix PRs.

Snyk and Socket also perform target-specific call-graph/reachability analysis, while Socket additionally analyzes behavioral changes between dependency versions and performs dependency-graph-aware fix planning.

Therefore UpgradePilot cannot justify itself with:

```text
"existing tools only know package versions and CVEs"
```

That claim is false for the modern 2026 landscape.

The narrower open question becomes:

> **Can UpgradePilot provide a materially broader, more evidence-transparent, proposition-specific and maintainer-auditable dependency-update decision system than security-oriented reachability/remediation platforms—especially for non-security updates, CI evidence, repository-purpose context, runtime environment proof, explicit unresolved states, and general maintainer action?**

That hypothesis remains open and requires the remaining Tier-1 research.

---

## 3. Endor Labs

### 3.1 Product model

Endor Labs is an SCA/security platform whose analysis goes substantially beyond manifest-vulnerability matching.

Its documented SCA responsibilities include:

- dependency resolution;
- software risk scoring;
- function-level reachability;
- unused dependency identification;
- call-graph generation;
- Upgrade Impact Analysis;
- remediation and patching.

Its recent product framing describes a broader “code context graph” spanning application code, dependencies, containers, pipeline configuration and other software context.

### 3.2 Reachability architecture

For supported ecosystems, Endor constructs call graphs for the target package and dependency packages and combines them into a project-level graph.

Conceptually:

```text
target code call graph
+
dependency call graphs
→ combined application/dependency graph
→ vulnerable-function reachability
```

This is important external evidence for a graph-centered world model.

Endor's own language documentation also exposes analysis limitations. For example, some languages/build systems lack call-graph support, builds/dependency resolution can fail, and dynamic constructs such as reflection/callbacks can be difficult or unsupported in some analyzers.

### 3.3 Upgrade Impact Analysis

Endor's public 2026 description gives a concrete algorithm:

```text
current dependency version
vs
target dependency version
→ diff changed symbols/behavioral surfaces

target + dependency call graph
→ determine which changed symbols are on reachable paths

overlay both
→ blast-radius / remediation-risk classification
```

The public description says the system identifies changes such as:

- renamed/removed APIs;
- signature changes;
- shifted defaults/behavior;
- transitive dependency conflicts;

and then classifies upgrade impact approximately into safe / code-change-needed / breaking categories.

Earlier Endor material describes remediation-risk ratings such as High/Medium based on likely breakage.

This is very close to one major part of UpgradePilot's intended mature responsibility.

### 3.4 Scope difference

The currently documented Upgrade Impact Analysis is explicitly tied to **direct dependency updates** and security remediation.

Endor's broader system may contain additional capabilities, but the public evidence reviewed here does not establish that it owns every arbitrary Dependabot-version-update decision, repository-purpose conflict, CI-proof question, package-manager runtime-state question, or non-security mechanism UpgradePilot has explored.

That distinction must be verified rather than assumed.

### 3.5 Evidence and authority model

Endor's architecture strongly emphasizes deterministic/static evidence as a substrate for remediation/AI:

```text
dependency resolution
→ AST/call graph/context graph
→ reachability / impact evidence
→ automated or agentic remediation
```

Current Endor material explicitly argues that agents perform better when provided structured deterministic evidence instead of reconstructing SCA/impact facts through repeated search.

This independently supports an “evidence substrate before agent reasoning” architecture, although the exact evidence ontology need not match UpgradePilot's.

### 3.6 Runtime/environment fidelity

Endor relies on local/CI workers and real build tools/runtimes/package managers for accurate dependency resolution. Its documentation notes that accurate scans depend on matching the real toolchain and that scans can fail when required tools or builds are unavailable.

This is highly relevant to UpgradePilot:

> graph quality depends on environment/dependency-resolution quality.

A sophisticated impact graph does not remove the problem of proving what environment/dependency state actually applies.

### 3.7 Transferable ideas

Worth challenging UpgradePilot with:

1. graph-centered cross-package call context;
2. diff old/new dependency versions directly;
3. overlay changed symbols onto target call paths;
4. use reachability to prioritize upgrade-impact work;
5. model transitive dependency conflicts as upgrade impact;
6. provide explicit remediation-risk/blast-radius output;
7. let agents reason over precomputed evidence rather than rediscover everything.

Potential non-transferable assumptions:

- security vulnerability as the primary trigger;
- function-call reachability as sufficient for every update mechanism;
- enterprise-scale graph construction as necessary for a Python-first portfolio product.

Sources:
- https://docs.endorlabs.com/scan-with-endorlabs/language-scanning/
- https://www.endorlabs.com/learn/upgrade-impact-analysis
- https://www.endorlabs.com/learn/introducing-upgrades-remediation-give-developers-the-confidence-to-fix
- https://www.endorlabs.com/learn/ai-vulnerability-remediation
- https://docs.endorlabs.com/best-practices/build-tools-use-case

---

## 4. Semgrep Supply Chain

### 4.1 Product evolution

Semgrep Supply Chain began as vulnerability reachability/prioritization built on Semgrep's static analysis.

By 2026 its public product includes:

- dependency graph/path analysis;
- direct and transitive reachability;
- malware detection;
- Autofix PRs;
- **Breaking Change Detection**;
- **Upgrade Guidance**;
- LLM-assisted remediation reasoning.

This makes Semgrep one of the closest modern external comparisons to UpgradePilot's proposed hybrid AI architecture.

### 4.2 Reachability model

Semgrep distinguishes multiple levels of reachability:

```text
dependency reachability
→ is the dependency used?

function-level reachability
→ is the vulnerable function reached?

dataflow reachability
→ is it reached in the dangerous/exploitable way?
```

Its product emphasizes first-party static/data-flow analysis to connect application code to vulnerable dependency behavior.

This is stronger than simply seeing an import or dependency graph path.

### 4.3 Upgrade Guidance architecture

Semgrep's March 2026 public description is unusually relevant:

```text
FIRST-PARTY ANALYSIS
how target code uses the dependency
including non-vulnerable usage that may break

+

THIRD-PARTY ANALYSIS
what changed between current and target dependency versions

↓
Semgrep Pro static-analysis evidence

↓
LLM

↓
breaking-change / upgrade-guidance report
```

Where Semgrep determines a safe upgrade exists, it can generate a PR. For complex updates it reports line-level breaking changes.

This is almost a direct external realization of one candidate architecture we independently derived:

> structured cross-repository semantic reasoner with deterministic/static evidence feeding an LLM.

### 4.4 Why this materially challenges UpgradePilot

UpgradePilot cannot claim novelty merely from:

- comparing old/new dependency semantics;
- inspecting target usage;
- using static evidence before LLM reasoning;
- producing a breaking-change report;
- generating a dependency fix PR.

Semgrep is already doing those things in a security-remediation context.

UpgradePilot must therefore differentiate on broader responsibility or stronger evidence semantics rather than architecture vocabulary.

### 4.5 Boundaries visible from public material

The reviewed material is security/remediation-centered:

```text
reachable vulnerability
→ find safe fixed version
→ identify breaking change
→ produce guidance/fix
```

It does not establish that Semgrep performs a general repository-purpose analysis, exact CI-evidence proof, package-manager ambient-semantics analysis, arbitrary non-security update impact discovery, or maintainer action synthesis across all those evidence families.

Also, Semgrep's ability to produce guidance depends on supported language/package-resolution/registry capability; Python private registries were a documented blocker until Network Broker support was added in June 2026.

### 4.6 Transferable ideas

1. analyze first-party and third-party code separately, then compose;
2. inspect **non-vulnerable dependency usage** when checking upgrade breakage;
3. use static analysis to compress/ground LLM context;
4. LLM output can be downstream of deep program analysis rather than operating directly on raw repos;
5. line-level impact localization is a high-value maintainer output;
6. fix generation should be conditional on impact evidence, not merely vulnerability presence.

Questions for later comparison:

- how much of Semgrep's breaking-change conclusion is independently inspectable?
- what structured intermediate evidence is exposed?
- what happens when the LLM/static-analysis pipeline is uncertain?
- does “safe upgrade” expose proof/coverage limits?
- how broadly does the method generalize beyond security fixes?

Sources:
- https://semgrep.dev/products/semgrep-supply-chain/
- https://semgrep.dev/blog/2025/what-you-should-know-about-dependency-reachability-in-sca/
- https://semgrep.dev/products/product-updates/accelerate-remediation-with-semgrep-autofix/
- https://semgrep.dev/blog/2026/semgrep-autofix-public-beta
- https://semgrep.dev/products/product-updates/python-private-registries-now-supported-for-reachability-analysis-autofix-and-upgrade-guidance-with-semgrep-supply-chain/

---

## 5. Snyk Open Source

### 5.1 Product model

Snyk Open Source constructs a hierarchical dependency tree from manifests/build output, correlates packages with its vulnerability database, supports PR checks/fix advice/Fix PRs in supported ecosystems, and adds application-level reachability and risk prioritization.

### 5.2 Reachability architecture

Snyk's current public reachability design is particularly instructive because it combines several methods:

```text
curated vulnerability + fix-commit evidence
→ identify vulnerability-related code elements

DeepCode program analysis + AI/NLP ranking
→ root-cause candidate elements

target + dependency call graph
→ path from target code to vulnerability-related element

security-researcher verification
→ improve/validate root-cause model
```

This is not purely deterministic static analysis and not purely generative AI.

### 5.3 Excellent uncertainty boundary

Snyk's public documentation explicitly says:

```text
NO PATH FOUND
!=
proven unreachable
```

Its statuses include:

- `REACHABLE`;
- `NO PATH FOUND`;
- `NOT APPLICABLE`.

The documentation explains that static analysis can establish a positive path but failure to find a path can arise from incomplete information, control-flow limitations, dynamic behavior or missed edge cases. Results can change later when first-party code, vulnerability analysis or the engine improves.

This is one of the strongest externally observed epistemic patterns in this Tier-1 research.

It independently supports:

> absence of evidence is not evidence of absence.

But importantly, it demonstrates that a mature commercial system can expose that limitation directly to users rather than hiding it.

### 5.4 Risk Score rather than binary verdict

Snyk combines reachability with broader contextual factors in its Risk Score.

Other prioritization dimensions include:

- severity;
- exploit maturity;
- fixability;
- vulnerability context.

This creates another alternative to UpgradePilot's proposition-only architecture:

> preserve typed evidence, but project some evidence into a holistic risk-prioritization score for workflow management.

Whether that is appropriate for UpgradePilot remains open.

### 5.5 Dependency/environment realism

Snyk often uses real ecosystem/build tools to resolve dependencies. For example, Python pip projects may require `pip install -r requirements.txt` to produce the full dependency tree when no sufficient lock state exists.

Snyk also documents cases where a Fix PR cannot be produced even if a vulnerability is theoretically fixable—such as parent BOM ownership or package-manager-specific constraints.

This supports another recurring lesson:

> dependency remediation capability is constrained by where version authority actually lives.

### 5.6 Data/provenance behavior

For reachability, Snyk accesses repository source to construct call graphs, then removes the code while retaining call graph/function-name information.

That is a concrete world-model choice:

```text
raw source
→ derived semantic graph
→ retain graph, discard source
```

Useful for later privacy/storage architecture discussion.

### 5.7 Transferable ideas

1. distinguish “no path found” from “unreachable” explicitly;
2. allow analysis results to be superseded by improved evidence/analyzers;
3. combine automated analysis with human-curated vulnerability semantics;
4. retain derived structural context rather than raw code where possible;
5. expose call paths to users;
6. separate fixability from vulnerability severity/reachability;
7. treat dependency authority location as part of remediation feasibility.

Do not copy blindly:

- vulnerability risk scoring as a complete dependency-update decision;
- one aggregate score replacing inspectable propositions;
- security-only applicability semantics for arbitrary updates.

Sources:
- https://docs.snyk.io/developer-tools/snyk-cli/scan-and-maintain-projects-using-the-cli/snyk-cli-for-open-source
- https://github.com/snyk/user-docs/blob/main/scan-fix-and-prevent/manage-risk/prioritize-issues-for-fixing/reachability-analysis.md
- https://docs.snyk.io/snyk-data-and-governance/how-snyk-handles-your-data
- https://docs.snyk.io/implement-snyk/team-implementation-guide/phase-4-create-a-fix-strategy
- https://docs.snyk.io/developer-tools/snyk-cli/scan-and-maintain-projects-using-the-cli/open-source-projects-that-must-be-built-before-testing-with-the-snyk-cli

---

## 6. Socket

### 6.1 Product model

Socket began from a different security thesis than traditional SCA:

> inspect what dependency packages actually do and how their behavior changes.

Its GitHub integration analyzes dependency changes for:

- malware;
- install scripts;
- obfuscation;
- telemetry;
- native code;
- shell/network/filesystem/environment access;
- typo-squatting and other supply-chain indicators.

This is directly relevant to **dependency-update deltas**, not only known CVEs.

### 6.2 Dependency behavior as update evidence

Socket's Dependency Overview comments can appear when:

- a dependency is added;
- an updated dependency adds new capabilities;
- dependencies are removed.

This means the unit of analysis can be:

```text
old dependency package behavior
→ new dependency package behavior
→ newly introduced capability/risk
```

That is a technical-impact family UpgradePilot has not emphasized enough.

Examples:

- new install script;
- new native code;
- new network/shell/filesystem capability;
- new suspicious package behavior.

These are not ordinary API compatibility changes, but they can be highly decision-relevant.

### 6.3 Reachability has multiple explicit proof strengths

Socket currently documents three reachability levels:

1. dependency reachability;
2. precomputed function-level reachability across dependency code;
3. full application reachability across application + dependency code.

It also exposes result categories such as:

- reachable;
- potentially reachable;
- unreachable;
- pending;
- not yet supported/inconclusive.

This is a useful explicit evidence-strength model.

### 6.4 Human-verified vs AI-generated vulnerability semantics

Socket's reachability analysis depends on a specification of which parts/functions of a dependency are affected by a vulnerability.

Socket documents two provenance classes:

- human-verified specification;
- AI-generated/auto-inferred specification.

Organizations may opt into AI-generated specifications for broader coverage at somewhat higher incorrect-result risk.

This is a concrete commercial example of:

```text
same proposition type
+
different producer authority/reliability class
→ different acceptable use
```

That is highly relevant to UpgradePilot's future AI-evidence authority design.

### 6.5 Static-analysis scope limitation is explicitly documented

Socket states that code-level reachability does not cover uses outside code—for example, a build/CLI tool invoked through the command line may appear unreachable because no application call edge exists.

This is directly relevant to UpgradePilot's CI/build-tool focus:

> call-graph reachability is powerful but not a universal “dependency used” model.

### 6.6 Reachability implementation maturity

Socket's public reachability changelog exposes a striking amount of analyzer-detail:

- dynamic dispatch modeling;
- Python-specific APIs such as pickle hooks;
- reflection approximations;
- monorepo/symlink resolution;
- dependency/build-tool resolution;
- partial-analysis fallback;
- per-vulnerability analysis errors;
- stale facts-file risk;
- memory/resource failures.

This is valuable evidence about the real engineering cost of building a mature static reachability engine.

### 6.7 Socket Fix

Socket Fix computes upgrade plans to remediate vulnerabilities while minimizing disruption.

It handles:

- direct/transitive fix paths;
- minimum release age;
- optional no-major-update policy;
- PR limits;
- fix calculation without applying;
- “no fix” / “no dependency-tree path” / “partial fix” states.

Recent implementation details show it often delegates edits/resolution to real ecosystem tools such as `go mod edit` and real build/package-manager behavior instead of relying only on text mutation.

This strongly reinforces the “use ecosystem tool as semantics owner when practical” lesson from Renovate.

### 6.8 Transferable ideas

1. package-behavior **delta** is a first-class update mechanism;
2. producer authority can be explicitly labeled human-verified vs AI-generated;
3. coverage can increase by accepting lower-authority model evidence under explicit policy;
4. reachability should have several strengths, not one boolean;
5. CLI/build-tool use is a separate activation model from code-call reachability;
6. analysis errors can be per-vulnerability rather than failing the entire scan;
7. remediation should preserve “no path / partial fix / policy blocked” states;
8. use real package-manager tooling for correct mutation where possible.

Sources:
- https://docs.socket.dev/docs/socket-for-github
- https://docs.socket.dev/docs/organization-alerts
- https://docs.socket.dev/docs/reachability-analysis
- https://docs.socket.dev/docs/static-reachability-analysis
- https://docs.socket.dev/docs/reachability-results
- https://docs.socket.dev/docs/full-application-reachability
- https://docs.socket.dev/docs/socket-fix
- https://docs.socket.dev/docs/reachability-analysis-changelog

---

## 7. Cross-system architecture comparison

| Dimension | Endor Labs | Semgrep Supply Chain | Snyk Open Source | Socket |
| --- | --- | --- | --- | --- |
| Dependency graph | yes | yes | yes | yes |
| Target source analysis | yes | yes | yes | yes |
| Call-graph reachability | strong/core | strong/core | supported | multi-level/core |
| Data-flow/exploitability | broader context claims | explicit dataflow reachability | program-analysis based | primarily reachability specs + static analysis |
| Old→new version impact | explicit Upgrade Impact Analysis | explicit Upgrade Guidance / breaking-change analysis | not found as equivalent core feature | behavior diff + fix planning; no equivalent general API-impact feature found |
| LLM/AI role | AI remediation/context reasoning in current platform material | explicit LLM final breaking-change analysis | AI/NLP + program analysis + human security experts | AI-generated vulnerability specs optionally admitted; other AI malware signals |
| Human curation | security/research context | Semgrep research/rules | security expert validation | explicit human-verified reachability specs |
| Fix automation | upgrades + patches | Autofix PRs | Fix PR/fix advice | Socket Fix |
| Explicit uncertainty | support/scan limitations; details vary | finding/reachability states; public upgrade-guidance uncertainty less clear | very explicit NO PATH FOUND ≠ unreachable | explicit pending/inconclusive/support states |
| Non-security update focus | mostly security/remediation framing | mostly security/remediation framing | security/vulnerability framing | behavior/security changes and vulnerability remediation |
| CI proof semantics | not observed as central responsibility | not observed as central responsibility | PR checks but not semantic CI-proof model | scans/CI integration but not semantic CI-proof model |

This table is based only on reviewed public evidence and should not be read as a complete product capability matrix.

---

## 8. Major corrections to UpgradePilot's external assumptions

### Correction 1 — target-specific impact analysis is not unique

Endor and Semgrep both explicitly analyze whether dependency-version changes intersect target usage.

UpgradePilot must not describe its value as merely:

> “we determine whether an update matters to your code.”

### Correction 2 — graph-based world models are already production patterns

Endor, Snyk, Semgrep and Socket all construct dependency/call/data-flow structure to varying degrees.

A future UpgradePilot evidence graph would be adopting an established architectural family, not inventing a novel idea.

### Correction 3 — hybrid static-analysis + AI is already commercial reality

Semgrep's Upgrade Guidance is a concrete external example:

```text
target static analysis
+
dependency-version static analysis
→ LLM synthesis
```

Socket and Snyk also mix AI/automated program analysis with human-curated security semantics.

Therefore “deterministic substrate + bounded AI” is independently supported—but is not differentiating by itself.

### Correction 4 — uncertainty semantics vary and can be a differentiator

Snyk and Socket explicitly distinguish:

- positive path found;
- no path found;
- unsupported/not applicable;
- pending;
- analyzer limitations;
- different authority classes for vulnerability specifications.

This independently validates UpgradePilot's interest in explicit unresolved states.

But UpgradePilot would need to make these semantics broader and more systematic to differentiate.

### Correction 5 — call-graph reachability is not universal dependency relevance

Socket explicitly documents CLI/build-tool usage as a case that code-call reachability can miss.

This directly supports UpgradePilot's investigation of CI/package-manager/build semantics as a distinct relevance mechanism.

### Correction 6 — package behavior changes are a missing impact family in our current horizon

Socket demonstrates that an update can matter because the package itself gains:

- install-time scripts;
- shell/network/filesystem access;
- native code;
- telemetry;
- obfuscation or other suspicious behavior.

This deserves consideration in later candidate-discovery architecture.

---

## 9. Revised product-space hypothesis

After Tier-1 Report 02, UpgradePilot's plausible differentiation is narrower and more precise.

It is **not**:

```text
target-specific dependency impact analysis
```

because modern SCA platforms already do important forms of that.

A more defensible hypothesis is:

> **general dependency-update decision intelligence that unifies multiple impact mechanisms and evidence classes beyond vulnerability remediation, with explicit proposition/evidence provenance, CI/runtime proof semantics, adaptive investigation, uncertainty preservation, repository-purpose context, and maintainer-facing action explanation.**

Conceptually:

```text
security platforms
→ excellent vulnerability reachability / exploitability / remediation
→ increasingly strong breaking-change analysis

UpgradePilot hypothesis
→ arbitrary dependency-update PR
→ security OR compatibility OR packaging OR runtime OR repository-purpose mechanisms
→ exact environment / CI / package-state evidence
→ mechanism-specific applicability
→ explicit evidence gaps
→ targeted investigation
→ cross-mechanism decision state
→ inspectable maintainer action
```

This is still a hypothesis. Later reports may narrow it further.

---

## 10. High-value architecture lessons for later Track C

### 10.1 Consider a structural graph seriously

External evidence now comes from:

- Endor call/context graphs;
- Semgrep dependency/data-flow analysis;
- Snyk call graphs;
- Socket dependency + call-path models;
- earlier RepoGraph/RIG research.

Track C should seriously test whether UpgradePilot's mature evidence representation should include a graph/IR substrate.

### 10.2 Keep non-call activation paths

Any graph must represent more than function calls:

- CLI/build-tool execution;
- CI steps;
- package-manager operations;
- config/plugin activation;
- persisted artifacts;
- platform/environment relations;
- package install-time behavior.

### 10.3 Producer authority can be first-class data

Socket's human-verified vs AI-generated reachability specifications are a concrete precedent.

Possible mature concept:

```text
claim
+ source identity
+ producer class
+ validation class
+ evidence strength
+ coverage
```

rather than simply “model output trusted/untrusted.”

### 10.4 Positive and negative reachability need asymmetric semantics

Snyk's “NO PATH FOUND != unreachable” is an especially strong external precedent.

This should be compared directly to UpgradePilot's open-world reasoning rules.

### 10.5 Old/new dependency code diff should become a major research object

Endor and Semgrep both analyze changes between current/target dependency versions.

UpgradePilot's upstream work has focused heavily on release/changelog evidence. Track C should ask whether source/API/AST diffing of old/new upstream versions should become a first-class evidence source.

### 10.6 Behavior-delta scanning deserves its own mechanism family

Socket's package behavior analysis suggests adding candidate classes such as:

- install-time behavior changed;
- new network/filesystem/shell capability;
- new native-code surface;
- changed package scripts/hooks;
- telemetry/data-exfiltration surface.

### 10.7 Use real package/build tools where they carry authoritative semantics

Endor, Snyk, Socket and Renovate all expose cases where real ecosystem tools are used for dependency resolution/build/mutation.

This is now a repeated external pattern across multiple research families.

---

## 11. What should NOT be copied blindly

1. **Security-only framing** — UpgradePilot's target is broader than CVE remediation unless later product research proves otherwise.
2. **Call graph = complete relevance** — CLI/config/build/runtime relationships violate that simplification.
3. **“Unreachable = safe” without coverage semantics** — static analysis limits matter.
4. **One risk score as final truth** — useful for prioritization, dangerous if it erases evidence detail.
5. **Enterprise graph infrastructure too early** — external systems have scale/resources far beyond a learning-by-doing flagship.
6. **LLM report as proof** — Semgrep's pattern is valuable, but UpgradePilot should still ask what intermediate evidence is inspectable.
7. **Automatically patch because security risk is reachable** — maintainer policy, non-security effects and repository purpose may matter.
8. **Universal static analysis** — analyzer complexity/coverage is substantial and language-specific.

---

## 12. New research questions triggered

1. How exactly do Endor and Semgrep represent old→new dependency code changes internally?
2. Can open-source API-diff/static-analysis tools approximate enough of Upgrade Impact Analysis for Python?
3. Should UpgradePilot add upstream source/AST/API diff evidence in addition to release-text interpretation?
4. Can a lightweight cross-repository graph cover CI/build/package-manager/config relations without becoming an enterprise graph platform?
5. What evidence is needed to claim a changed upstream symbol is actually target-activated?
6. Should AI-generated semantic evidence have graded authority instead of a binary trusted/untrusted status?
7. Could Socket-style package behavior delta analysis reveal material non-compatibility risks for ordinary version updates?
8. How should UpgradePilot distinguish `no path found`, `not analyzed`, `not supported`, and `proven non-applicable`?
9. Can the Python ecosystem provide reliable API-diff/build-artifact/tooling signals without executing arbitrary upstream code?
10. Is UpgradePilot's strongest product niche actually **cross-mechanism synthesis and evidence honesty**, rather than impact detection itself?

---

## 13. Sources checked

### Endor Labs
- https://docs.endorlabs.com/scan-with-endorlabs/language-scanning/
- https://www.endorlabs.com/learn/upgrade-impact-analysis
- https://www.endorlabs.com/learn/introducing-upgrades-remediation-give-developers-the-confidence-to-fix
- https://www.endorlabs.com/learn/ai-vulnerability-remediation
- https://docs.endorlabs.com/best-practices/build-tools-use-case

### Semgrep
- https://semgrep.dev/products/semgrep-supply-chain/
- https://semgrep.dev/blog/2025/what-you-should-know-about-dependency-reachability-in-sca/
- https://semgrep.dev/products/product-updates/accelerate-remediation-with-semgrep-autofix/
- https://semgrep.dev/blog/2026/semgrep-autofix-public-beta
- https://semgrep.dev/products/product-updates/python-private-registries-now-supported-for-reachability-analysis-autofix-and-upgrade-guidance-with-semgrep-supply-chain/

### Snyk
- https://docs.snyk.io/developer-tools/snyk-cli/scan-and-maintain-projects-using-the-cli/snyk-cli-for-open-source
- https://github.com/snyk/user-docs/blob/main/scan-fix-and-prevent/manage-risk/prioritize-issues-for-fixing/reachability-analysis.md
- https://docs.snyk.io/snyk-data-and-governance/how-snyk-handles-your-data
- https://docs.snyk.io/implement-snyk/team-implementation-guide/phase-4-create-a-fix-strategy
- https://docs.snyk.io/developer-tools/snyk-cli/scan-and-maintain-projects-using-the-cli/open-source-projects-that-must-be-built-before-testing-with-the-snyk-cli

### Socket
- https://docs.socket.dev/docs/socket-for-github
- https://docs.socket.dev/docs/organization-alerts
- https://docs.socket.dev/docs/reachability-analysis
- https://docs.socket.dev/docs/static-reachability-analysis
- https://docs.socket.dev/docs/reachability-results
- https://docs.socket.dev/docs/full-application-reachability
- https://docs.socket.dev/docs/socket-fix
- https://docs.socket.dev/docs/reachability-analysis-changelog

---

## 14. Status / next report

**Tier-1 Report 02: COMPLETE.**

The report materially narrowed the provisional UpgradePilot product-space hypothesis.

Next research family:

> **Tier-1 Report 03 — remediation and migration engines**  
> OSV-Scanner Guided Remediation, OpenRewrite/Moderne, DepRepair/DepBench, Python API-diff tooling such as Griffe, and other materially relevant migration/remediation systems discovered during the pass.

This next report should answer a different question:

> once a dependency problem/impact is known, how do mature systems choose and construct the smallest safe remediation, and how much of migration reasoning can be automated structurally rather than through general-purpose agents?
