# Challenge-Case Screening 01

**Date:** 2026-08-07  
**Status:** Active exploratory screening; non-controlling; no new scenario admitted  
**Workspace:** `product-simulation/`  
**Canonical working branch:** `agent/product-simulation-case-screening-01`

## 1. Purpose

This record preserves the first challenge-oriented case exploration after the S006 work and the product-decision-model handoff.

The goal of this screening is **not** to find another case that neatly fits the current provisional reasoning shape:

```text
change
→ exposure
→ activation
→ consequence
→ evidence
```

Instead, the near-term priority is to find evidence that **challenges, blurs, or requires refinement of that model**.

The screening should prefer cases where:

- target exposure is ambiguous;
- exposure is mediated or multi-hop;
- the changed dependency is not directly referenced by target-owned runtime source;
- control is inverted through plugins, callbacks, hooks, entry points, decorators, framework lifecycle, or dependency injection;
- a dependency affects generated or built artifacts rather than runtime source directly;
- an environment/platform constraint matters without a clear source-level usage surface;
- exposure and activation are difficult to separate;
- the same subsystem can act as exposure in one context and evidence in another;
- one term such as `target exposure surface` starts collapsing several materially different roles.

The desired output is therefore **counterexamples, unresolved questions, and required conceptual refinements**. A full S00x scenario should be created only when a concrete unresolved question is strong enough to justify one.

## 2. Relationship to current product-model reconciliation

This file is simulation evidence only.

It does **not**:

- define the accepted UpgradePilot decision model;
- modify the active reconciliation record;
- establish `target impact pathway` or any alternative term as accepted architecture;
- replace `exposure`, `activation`, `applicability`, `consequence`, or `evidence` with a new controlling vocabulary;
- claim that the current model is wrong;
- admit S007;
- authorize implementation.

The active whole-product reconciliation remains the authority for accepted domain-model decisions. This screening exists to provide it with pressure tests and counterexamples.

## 3. Challenge shapes requested for screening

### 3.1 Multi-hop or transitive exposure

Candidate structural shape:

```text
target
→ dependency A
→ dependency B changed
```

The target may never directly reference B.

Questions:

- Is the exposure surface the target's use of A?
- Is it A's use of B?
- Is the dependency path itself the relevant unit?
- Does `surface` incorrectly imply a single local boundary when the effect propagates through a graph?

### 3.2 Plugin / entry-point / hook exposure

Candidate mechanisms:

```text
plugin registration
entry points
hook implementations
callbacks
decorators
framework lifecycle
inversion of control
dependency injection
```

Questions:

- Is target source using the dependency, or is the dependency/framework using target code?
- Does `source/API usage` remain adequate when target-owned behavior is invoked dynamically?
- Is registration/configuration the exposure, the hook implementation, the framework lifecycle, or the whole control path?

### 3.3 Build and code-generation exposure

Candidate mechanisms:

```text
code generation
asset compilation
schema generation
document generation
package/build tooling
artifact generation
```

Questions:

- Is the exposure the generator invocation?
- The generator input/configuration?
- The generated artifact?
- The later runtime use of that artifact?
- Can the dependency disappear from the runtime path while its generated output remains decision-relevant?

### 3.4 Environment-only exposure

Candidate mechanisms:

```text
wheel availability
glibc requirement
CPU architecture
OS support
system library
compiler/toolchain
ABI compatibility
native extension availability
```

Questions:

- What is the target exposure when no target source or meaningful application configuration directly invokes the changed condition?
- Is `target exposure surface` too physical/local for these cases?
- Would a broader concept such as an impact pathway describe them better?

### 3.5 Role ambiguity

Desired contrast:

```text
same subsystem
→ exposure in one case
→ evidence in another
```

Known starting contrast from S004-S006:

- pytest/test execution can be an actual affected interaction when pytest itself is the dependency under change;
- tests and CI can instead be evidence about a runtime dependency path when another dependency is under change.

The challenge search should find additional real examples rather than relying only on that existing contrast.

## 4. Screening method

For each candidate, keep the following questions separate rather than assuming they collapse into a single `exposure surface`:

1. **Where is the changed dependency located?**
   - runtime dependency;
   - development dependency;
   - transitive dependency;
   - build/tooling dependency;
   - system/environment dependency.

2. **Through what mechanism can its change propagate?**
   - direct call;
   - framework mediation;
   - dependency graph;
   - plugin/hook lifecycle;
   - generated artifact;
   - build step;
   - environment/platform constraint;
   - other indirect path.

3. **Where does target-owned behavior encounter the effect?**
   - target source;
   - target configuration;
   - generated source/artifact;
   - package/install boundary;
   - runtime environment;
   - callback/hook implementation;
   - no local encounter point yet established.

4. **What intermediary object or stage exists?**
   - dependency A;
   - generated code;
   - compiler output;
   - plugin manager;
   - framework registry;
   - lock/resolver state;
   - OS/ABI/system library;
   - none.

5. **Where is evidence observed?**
   - tests;
   - CI;
   - build output;
   - runtime reproduction;
   - package resolution;
   - generated diff;
   - environment probe;
   - upstream authority only.

A candidate is valuable if these answers resist reduction to a single clean category.

## 5. Candidate register

| ID | Candidate | Challenge family | Current status | Main value |
|---|---|---|---|---|
| C01 | `dominodatalab/container-runtime-interface-api#101` — `grpcio-tools ~=1.73 → ~=1.80` | build/code-generation; staged artifact pathway | **Strong counterexample; keep** | dependency is dev-only, executes during generation, writes committed source artifacts used later at runtime |
| C02 | `devclinton/autochangelog#4` — `pluggy ~=0.13.1 → ~=1.0.0` | plugin/hook ambiguity | **Preliminary / unresolved** | direct declaration does not by itself reveal where target exposure exists |
| C03 | `pypa/pip-audit#620` — `urllib3 >=1.26,<2 → >=1.26,<3` | multi-hop/transitive dependency constraint | **Promising; needs deeper target-path proof** | patch explicitly documents CacheControl incompatibility with urllib3 2 by way of Requests |
| C04 | environment/native/toolchain family | environment-only | **No sufficiently evidenced candidate yet** | search gap remains open |
| C05 | second role-ambiguity case | exposure/evidence role switching | **No independent strong candidate yet** | S004-S006 provide the starting contrast; more real evidence is desired |

No candidate in this register is an admitted S007.

---

## 6. C01 — container-runtime-interface-api / grpcio-tools

### 6.1 Identity

Repository:

`dominodatalab/container-runtime-interface-api`

Pull request:

`#101 — Update grpcio-tools requirement from ~=1.73 to ~=1.80`

Frozen PR head observed during screening:

`034f0a82e2c06526212353a1258f59f159538914`

PR base:

`develop`

PR state at screening time:

`open`, not merged.

The Dependabot PR changes one dependency requirement from approximately 1.73 to approximately 1.80.

### 6.2 Verified target facts

At the frozen PR head, `Pipfile` places `grpcio-tools = "~=1.80"` under `[dev-packages]`, not normal runtime `[packages]`.

Therefore the changed dependency is explicitly a **development/build-time dependency** in this repository.

The frozen file `bin/update-proto.sh` invokes:

```text
pipenv run python -m grpc_tools.protoc
```

against vendored Kubernetes/container-runtime `.proto` definitions.

That command writes generated files into `src/cri_api` using outputs including:

```text
--python_out=src/cri_api
--mypy_out=src/cri_api
--grpc_python_out=src/cri_api
```

The same script then post-processes generated Python files with `sed` and formatting.

The frozen repository contains generated runtime/library artifacts such as:

```text
src/cri_api/v1/api_pb2.py
src/cri_api/v1/api_pb2.pyi
src/cri_api/v1/api_pb2_grpc.py
```

These generated modules are repository artifacts and are part of the Python package source tree.

### 6.3 Why this challenges a single exposure-surface model

A simple direct-source model might ask:

```text
Where does target code import grpcio-tools?
```

That question is not sufficient here.

The more faithful structure is:

```text
grpcio-tools version/change
        ↓
build/development environment
        ↓
`grpc_tools.protoc` generator execution
        ↓
proto inputs + generator options
        ↓
generated Python / typing / gRPC modules
        ↓
repository/package artifact
        ↓
later runtime consumer imports/uses generated modules
```

The changed dependency can therefore matter even though it need not be present in the final runtime environment.

The dependency's behavior is materialized into another artifact.

### 6.4 Competing interpretations

At least four plausible candidates for `exposure` appear:

#### Interpretation A — generator invocation is the exposure

```text
target build script
→ grpc_tools.protoc
```

This captures where target-owned process invokes the changed dependency.

Weakness:

It does not describe where the generated behavioral consequences persist after the generator is gone.

#### Interpretation B — generator configuration/input is the exposure

```text
.proto input + protoc flags
→ generator behavior
```

This captures the contract presented to the generator.

Weakness:

The generator can change output semantics while the input contract remains unchanged.

#### Interpretation C — generated artifact is the exposure

```text
generator
→ generated Python
```

This captures the materialized boundary that later enters the product/package.

Weakness:

The generated artifact is arguably a consequence/output rather than the exposure itself.

#### Interpretation D — whole staged pathway is the meaningful unit

```text
generator dependency
→ invocation
→ input/configuration
→ generated artifact
→ package/runtime use
```

This may better preserve causality.

Weakness:

It introduces a broader concept than `surface` and may be too general if used indiscriminately.

### 6.5 Evidence-role observation

The frozen CircleCI configuration installs development dependencies and runs lint, unit tests, integration tests, build, and publish steps.

However, in the inspected configuration it does **not** explicitly call `bin/update-proto.sh` as part of ordinary CI.

That means this candidate currently does **not** prove the stronger role-ambiguity claim that the same code-generation subsystem is both the exposure mechanism and the evidence mechanism.

Instead it exposes a different question:

> CI may validate the already-generated committed artifacts while failing to re-execute the generating step whose dependency changed.

That distinction could itself become decision-relevant, but it has not yet been promoted to a scenario question.

### 6.6 Counterexample / refinement pressure

C01 provides strong evidence for this refinement pressure:

> Some dependency impacts are **temporally staged and artifact-mediated**. A changed dependency can affect a target by producing an artifact that survives after the dependency itself is absent.

Possible conceptual refinement to test—not accept yet:

```text
target impact pathway
```

may sometimes be more descriptive than a singular:

```text
target exposure surface
```

because several distinct stages participate.

### 6.7 Unresolved questions

- Which stage, if any, deserves the term `exposure`?
- Should generated artifacts be modeled as target state, consequence, intermediary evidence, or another first-class concept?
- Does the fact that generated code is committed change the model compared with generation only during packaging?
- Should coverage distinguish testing generated artifacts from testing the generation process itself?
- Would a targeted regeneration-and-diff check provide materially new information for this PR?
- Are grpcio-tools 1.73→1.80 changes actually capable of altering these generated artifacts for the target's proto inputs?

The final question is important: the structural counterexample is established, but a concrete harmful or material output difference has **not** yet been proven.

### 6.8 Scenario admission status

**Do not admit as S007 yet.**

A full case becomes justified only if a concrete unresolved question can be stated, for example:

> Does the grpcio-tools update materially alter the generated CRI Python artifacts for the repository's frozen proto inputs, and would ordinary CI fail to detect a generation-specific difference?

That question requires deeper evidence before scenario creation.

---

## 7. C02 — autochangelog / pluggy

### 7.1 Identity

Repository:

`devclinton/autochangelog`

Pull request:

`#4 — Update pluggy requirement from ~=0.13.1 to ~=1.0.0`

Frozen PR head observed during screening:

`136c565ba06c2844d2b615ad021d8fb9372902ff`

PR state at screening time:

`open`, not merged.

### 7.2 Upstream behavior pressure

The Dependabot body carries pluggy 1.0.0 changelog material including significant hook-system changes:

- removal of deprecated `implprefix` support;
- removal of the old `__multicall__` recursive hook-calling system;
- internal module names becoming explicitly private;
- stricter validation for incorrectly declared `hookwrapper=True` implementations;
- removal of older deprecated hook APIs.

These changes make pluggy 0.13→1.0 a potentially useful hook/inversion-of-control family.

### 7.3 Preliminary target observation

During the initial repository screening, straightforward searches did not reveal an obvious target-owned use of canonical pluggy surfaces such as a visible `PluginManager`, hook marker, `implprefix`, or `__multicall__` use.

This observation should be treated as **preliminary**, not a proof of absence.

What is established is narrower:

> The dependency is declared directly, but direct declaration alone has not yet established a concrete target exposure path.

### 7.4 Why this matters

A naive model can easily infer:

```text
direct dependency
→ direct target exposure
```

C02 warns against that inference.

Possible realities include:

- stale or unused direct dependency;
- use hidden behind another library or helper;
- dynamic registration/convention not found by simple search;
- framework-mediated hook loading;
- target behavior that uses pluggy indirectly despite direct declaration;
- a dependency declaration retained for historical reasons.

Therefore:

```text
dependency directness != demonstrated exposure
```

### 7.5 Current value

C02 is currently more valuable as a **negative screening lesson** than as a scenario.

It pressures the model to separate:

- package declaration topology;
- actual propagation mechanism;
- target-owned encounter point.

### 7.6 What would justify deeper work

A deeper pass is warranted only if we can establish one of the following:

- a real dynamic hook/entry-point path;
- pluggy loading target-owned code through inversion of control;
- an indirect framework that uses pluggy on the target's behalf;
- a meaningful proof that the dependency is unused/stale and therefore that declaration-only evidence would create a false exposure claim.

Until then:

**do not create a full scenario.**

---

## 8. C03 — pip-audit / urllib3 through CacheControl and Requests

### 8.1 Identity

Repository:

`pypa/pip-audit`

Pull request:

`#620 — build(deps-dev): update urllib3 requirement from <2.0,>=1.26 to >=1.26,<3.0`

Frozen PR head observed during screening:

`0673f9c0515b6142e1fd4d977abe9b03fa8d5947`

PR state at screening time:

`closed`, not merged.

### 8.2 Exact patch evidence

The PR changes one `pyproject.toml` constraint:

```text
urllib3 >= 1.26,< 2.0
```

to:

```text
urllib3 >= 1.26,< 3.0
```

The crucial evidence is the target-owned comment immediately above that constraint:

```text
We constrain this subdepency because of CacheControl's incompatibility
with urllib3 ~= 2.0 by way of requests.
```

The patch removes the old `<2.0` bound while leaving that explanatory comment in place.

### 8.3 Why this is a strong multi-hop candidate

The target itself labels urllib3 as a **subdependency** and describes the compatibility path as:

```text
pip-audit
→ CacheControl
→ Requests
→ urllib3
```

This is structurally different from S006-style target-owned runtime source directly using the changed dependency's semantics.

The relevant question becomes:

> Where is the target's exposure to urllib3 2.x?

Possible answers:

```text
pip-audit's use of CacheControl
```

or:

```text
CacheControl's use of Requests
```

or:

```text
Requests' use of urllib3
```

or:

```text
the full dependency path / resolved dependency graph
```

or perhaps:

```text
no target exposure should be assigned until a concrete target-observable consequence is identified
```

### 8.4 Why this challenges the current terminology

A single `target exposure surface` risks collapsing multiple ownership boundaries:

```text
target-owned relationship
→ third-party A
→ third-party B
→ changed third-party C
```

The changed dependency may be several hops away from target-owned code.

Yet the target can still be materially affected through installation, runtime transport, or compatibility behavior.

This supports a refinement pressure similar to C01, but by a different mechanism:

- C01 is **artifact-mediated across time**;
- C03 is **graph-mediated across dependency ownership boundaries**.

If both require a broader pathway concept, that would be stronger evidence than either alone.

### 8.5 What is not yet proven

This screening has **not yet established**:

- the exact CacheControl version and affected API/path at the PR head;
- the exact Requests version/path mediating the incompatibility;
- whether pip-audit directly exercises the affected behavior;
- whether the old compatibility issue was still active at the proposed versions;
- what observable failure or risk the target would experience;
- whether the PR was closed because another update superseded it, because the incompatibility persisted, or for another reason.

Therefore C03 is promising but not scenario-ready.

### 8.6 Useful unresolved question

A candidate question for deeper screening is:

> When a target constrains a changed package solely because of a transitive compatibility relationship, what should UpgradePilot identify as the target-relevant impact pathway, and at what point should it stop tracing the dependency graph?

This is a domain-model challenge question, not yet a full case definition.

---

## 9. Environment-only family — current gap

The requested environment-only challenge family remains open.

Desired shapes include:

```text
wheel availability
glibc / musl compatibility
CPU architecture
native compiler
system library
OpenSSL or libc requirement
platform tag
ABI change
```

The important property is:

> no meaningful target source/API path should be required for the dependency change to matter.

This would test whether `exposure surface` improperly privileges source/configuration interactions.

No candidate was verified strongly enough during this first pass to preserve as more than a search target.

Do not manufacture a candidate simply to fill this category.

## 10. Role-ambiguity family — current state

S004-S006 already establish that the same broad subsystem category can change role by context:

- tests/test tooling can be the affected target interaction when the changed dependency is a test runner or testing tool;
- tests/CI can instead be evidence about a separate runtime dependency path.

C01 adds a weaker but useful nearby observation:

- CI installs `grpcio-tools` and tests the package containing generated artifacts;
- inspected CI does not explicitly regenerate those artifacts;
- therefore testing the generated result is not the same as exercising the generation pathway.

This is not yet the strong second real contrast requested.

The desired future candidate should make role ambiguity explicit within one real system, for example:

```text
same CI/build subsystem
→ actual affected execution path
and
→ evidence-production mechanism
```

or another equally strong contextual role switch.

## 11. Cross-candidate pressure on the current model

The current evidence does **not** justify replacing the provisional model.

It does justify pressure-testing several assumptions.

### 11.1 A single local `surface` may not always exist

C01:

```text
dependency
→ generator
→ generated artifact
→ later runtime use
```

C03:

```text
target
→ dependency A
→ dependency B
→ changed dependency C
```

Both involve materially different forms of distributed propagation.

### 11.2 Dependency topology is not the same as target exposure

C02 demonstrates the danger of equating direct declaration with demonstrated interaction.

C03 demonstrates the opposite problem: a transitive dependency can matter despite no direct target declaration/use.

Therefore:

```text
directness
```

and:

```text
exposure / impact propagation
```

should remain distinct concepts.

### 11.3 Propagation mechanism and encounter point may be different

Examples:

```text
C01
propagation = generation process
encounter = generated artifact / later runtime use
```

```text
C03
propagation = dependency graph
encounter = potentially an A/B/C compatibility boundary
```

The model should not assume one node owns both.

### 11.4 Evidence can observe a downstream artifact without exercising the causal pathway

C01's CI can test committed generated code without necessarily rerunning the generator.

Therefore:

```text
downstream behavior covered
!=
causal generation pathway covered
```

This is analogous to S006's earlier discovery that nearby/component coverage is not exact behavior-path coverage, but the causal structure here is different.

### 11.5 `Target impact pathway` is a hypothesis, not a decision

A possible abstraction emerging from C01 and C03 is:

```text
target impact pathway
```

meaning a sequence of dependency, framework, artifact, graph, environment, or target-owned stages through which an upstream change can become target-relevant.

Potential advantage:

- represents multi-stage propagation without forcing one stage to be `the surface`.

Potential risk:

- too broad;
- could become an unhelpful catch-all;
- may obscure useful distinctions already captured by exposure/activation/applicability;
- may introduce unnecessary ontology if only rare cases need it.

No controlling adoption is warranted from this screening alone.

## 12. Search/process lessons

### 12.1 Do not optimize for model fit

Candidate value should increase when evidence forces us to ask:

```text
"Which category is this actually?"
```

not when it cleanly maps to the existing categories.

### 12.2 Do not count package updates as challenge cases by themselves

A dependency major-version bump is insufficient.

The candidate must expose ambiguity in propagation, ownership, role, activation, evidence, or stopping.

### 12.3 Direct code search has known blind spots

Searching for imported dependency symbols can miss:

- generated artifacts;
- plugin registration;
- dynamic loading;
- entry points;
- framework lifecycle;
- transitive mediation;
- environment/platform behavior.

It can also surface vendored copies or implementation internals that are not target-owned use.

### 12.4 Negative results are useful

Examples:

- C02 has not yet yielded a concrete pluggy hook path;
- no strong environment-only candidate has yet been proven;
- no second independent role-ambiguity case is yet strong enough.

These should remain recorded rather than replaced with weaker candidates just to complete a matrix.

## 13. Candidate priority after this pass

### Priority A — deepen C03 enough to test graph-mediated terminology

Reason:

The target's own comment explicitly describes the transitive path. This gives unusually strong target-authored evidence that the compatibility concern exists through other dependencies.

Next bounded questions:

1. Which CacheControl and Requests versions are present at the frozen PR head?
2. What exact incompatibility motivated the `<2` bound?
3. Was it still active when #620 proposed widening the range?
4. What target-observable behavior or installability consequence follows?
5. Can we identify a sensible stopping point in the graph without tracing indefinitely?

This is still screening, not automatic S007 admission.

### Priority B — deepen C01 only if generator-output materiality can be proven

Next bounded questions:

1. Does regenerating frozen proto inputs under grpcio-tools 1.73 vs 1.80 produce a material diff?
2. If yes, what kind of diff—serialization/runtime API, generated metadata, typing, formatting, version guard, or other?
3. Would existing CI detect it without explicit regeneration?
4. Does the answer require distinguishing generated-artifact state from source/API exposure?

If no material generated difference exists, C01 can remain a conceptual counterexample without becoming a full scenario.

### Priority C — continue search for true inverted-control/plugin candidate

Desired evidence:

```text
dependency/framework loads target-owned code
→ target does not call dependency directly
→ changed hook/registration semantics can affect behavior
```

Prefer entry points, pytest plugins, pluggy-based systems, framework callbacks, or dependency injection with exact target-owned registrations.

### Priority D — continue environment-only search

Seek a real dependency update where platform or native availability is the main concern and source usage is largely irrelevant.

### Priority E — seek stronger role-ambiguity contrast

Prefer one system where the same CI/build/test subsystem has both causal and evidentiary roles.

## 14. Stop line

This artifact intentionally stops before:

- creating S007;
- implementing a synthetic variant;
- changing the controlling product model;
- editing the active reconciliation record;
- modifying `MEMORY.md`;
- changing UpgradePilot product source;
- mutating any external target repository;
- declaring `target impact pathway` accepted terminology.

A scenario should be admitted only when a candidate yields a **specific unresolved question** whose answer would materially distinguish between competing product-model interpretations or reveal a missing product responsibility.

## 15. Current conclusions

The first challenge-oriented pass produced one strong structural counterexample, one strong transitive candidate, one useful negative/ambiguous plugin candidate, and two deliberately open search gaps.

The strongest provisional lesson is:

```text
changed dependency location
!=
propagation mechanism
!=
target encounter point
!=
activation condition
!=
evidence observation point
```

In straightforward cases these may collapse into a compact chain.

In harder cases they may be distributed across:

```text
multiple dependencies
multiple ownership boundaries
multiple times/stages
generated artifacts
framework-controlled execution
environment constraints
```

The current `exposure` concept should therefore be **pressure-tested rather than mechanically applied** during the next case exploration.

That is the durable handoff from this screening pass.
