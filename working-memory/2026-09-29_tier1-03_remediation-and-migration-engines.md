# Tier 1 Report 03 — Remediation and Migration Engines

**Recorded:** 2026-09-29  
**Branch:** `analysis/ai-agentic-capability-map-2026-09-28`  
**Status:** COMPLETE initial deep report  
**Research family:** Remediation and migration engines  
**Systems examined:** OSV-Scanner Guided Remediation, OpenRewrite/Moderne, DepRepair/DepBench, Griffe, LibCST  
**Purpose:** understand how mature systems choose remediation strategies, transform manifests/source, localize affected usage, validate fixes, represent partial/no-safe-fix states, and separate remediation planning from execution.

This report records external research evidence. It does not authorize UpgradePilot remediation/mutation work or change live project architecture.

---

## 1. Research questions

1. Once an impact/problem is known, how does the system decide what change to make?
2. Does it optimize for minimum dependency change, minimum source change, maximum vulnerabilities fixed, or another objective?
3. Is remediation strategy deterministic, rule-based, model-generated, or interactive?
4. How are target usage sites found?
5. How are upstream breaking changes represented?
6. How are manifests, lockfiles, and source code transformed?
7. Are real ecosystem/package-manager tools invoked?
8. How is a proposed fix validated?
9. How are partial fix, no fix, unsupported, or risky-fix states represented?
10. Which parts are reusable for a future Python-first UpgradePilot repair path?

---

## 2. Executive result

The strongest result is that **remediation is not one responsibility**.

The reviewed systems decompose it differently, but together expose at least this chain:

```text
impact/problem established
→ remediation candidates
→ strategy/risk trade-off
→ affected-site localization
→ concrete manifest/source transformation
→ dependency graph / lock regeneration
→ executable/static validation
→ remaining unresolved/partial-fix state
```

Four distinct remediation philosophies emerged:

1. **graph strategy optimizer** — OSV-Scanner;
2. **deterministic semantic transformation recipes** — OpenRewrite/Moderne;
3. **evidence-grounded generative repair** — DepRepair;
4. **Python structural/API-diff + codemod substrates** — Griffe + LibCST.

The external evidence therefore argues against a future architecture where one generic LLM simply receives “fix this dependency update.”

---

## 3. OSV-Scanner Guided Remediation

### 3.1 Product responsibility

OSV-Scanner Guided Remediation starts from known vulnerable dependency state and asks:

> what bounded dependency changes can remove the most vulnerability exposure with acceptable graph disruption?

It analyzes the full transitive dependency graph using deps.dev data and offers alternative remediation strategies rather than one mandatory patch.

### 3.2 Strategy families

Current documented strategies include:

- **in-place** lockfile remediation;
- **relock / relax** direct dependency constraints;
- **override** for Maven dependency-management cases.

The key architecture is:

```text
same vulnerability set
+
same dependency graph

→ multiple possible remediation strategies
→ different change/risk profiles
```

This is a concrete example of remediation as a **choice among non-equivalent strategies**, not merely version selection.

### 3.3 Optimization objective

For relaxation, patches are ranked approximately by:

```text
more vulnerabilities removed
+
less dependency change
```

Users can constrain:

- maximum dependency depth;
- severity;
- dev-only scope;
- number of top patches;
- whether a patch may introduce a new vulnerability.

This is explicitly multi-objective:

```text
benefit
vs
blast radius / breakage risk
```

### 3.4 Graph recomputation

When a direct dependency constraint is relaxed, the graph is recomputed and additional choices can become available.

This means remediation is stateful:

```text
choose patch
→ recompute graph
→ new candidate set
→ choose again
```

This is naturally planner-like even though the current implementation is not framed as an LLM agent.

### 3.5 Real ecosystem-tool execution

For npm relocking, OSV-Scanner deletes the old lock state and runs the package manager to regenerate the lockfile.

This again reinforces an external pattern seen in Renovate/Socket:

> when ecosystem semantics are complex, use the real ecosystem tool when safe/practical instead of fully reimplementing it.

### 3.6 Security boundary

The documentation explicitly warns that guided remediation can be unsafe on untrusted projects because package-manager execution can:

- execute scripts;
- contact configured registries;
- consume project-defined behavior.

This is directly relevant to any future UpgradePilot mutation/execution layer.

### 3.7 Explicit limitations

Documented limitations include incomplete npm peer-dependency/override handling, workspace limitations, Maven profile/property limitations, and unsupported non-registry dependency forms.

The important pattern is not the individual bugs. It is:

> remediation output quality is only as good as the dependency-resolution model.

### 3.8 Transferable ideas

- represent multiple remediation strategies explicitly;
- expose risk/change trade-offs rather than one “best fix”;
- recompute candidates after each structural change;
- maintain “cannot resolve with this strategy” states;
- distinguish graph-fix feasibility from runtime/application compatibility;
- treat package-manager execution as a privileged/unsafe capability.

Source:
- https://google.github.io/osv-scanner/experimental/guided-remediation/

---

## 4. OpenRewrite / Moderne

### 4.1 Product model

OpenRewrite is fundamentally a **semantic transformation engine**.

Its core representation is the Lossless Semantic Tree (LST):

```text
syntax
+ formatting
+ semantic/type attribution
→ format-preserving semantic program tree
```

Recipes search, analyze and transform this representation.

Moderne adds large-scale indexing/execution/coordination across repositories.

### 4.2 Why the LST matters

The LST preserves whitespace/comments/style while carrying type information.

That enables transformations such as:

- distinguish two same-named methods from different libraries;
- identify exact type/method usage;
- update imports;
- alter build files;
- rewrite APIs without losing formatting.

This is a concrete example of a **typed transformation world model**.

### 4.3 Recipes are composable remediation knowledge

A migration can be one recipe or a composition of many recipes.

Example Java upgrade recipes combine:

- dependency changes;
- deprecated API replacements;
- build target changes;
- plugin updates;
- framework migrations.

The remediation knowledge is encoded as reusable, inspectable transformation programs.

This stands in sharp contrast to a generative repair model.

### 4.4 Preconditions

OpenRewrite recipes can use explicit preconditions:

```text
if semantic/search condition holds
→ transformation eligible

else
→ transformation skipped
```

Preconditions can be composed with AND/OR/NOT-like logic.

This is important because it separates:

```text
applicability
!=
transformation
```

even inside a remediation engine.

### 4.5 Idempotence and reproducibility

OpenRewrite recommends recipes be idempotent/immutable: the same semantic tree and configuration should produce the same result.

This is a strong engineering property for migration automation.

### 4.6 Dry run and explicit commit boundary

Moderne's platform workflow allows a recipe to be dry-run across repositories, inspect results, and only then choose whether/how to commit or open PRs.

So:

```text
transformation proposal
!=
repository mutation
```

This separation is directly relevant to UpgradePilot's authority model.

### 4.7 Search/data-table mode

Recipes can produce data tables rather than changing source.

Examples include:

- dependency vulnerability data;
- dependency resolution diagnostics;
- call graphs;
- low-confidence files;
- lock regeneration failures.

This means the same semantic infrastructure supports:

```text
analysis/reporting
and
mutation
```

without requiring them to be the same operation.

### 4.8 Confidence/coverage detail inside analysis

OpenRewrite's call-graph data can record low-confidence files when type information is unavailable.

That is a notable external example of a deterministic analysis tool exposing **coverage/confidence weakness** instead of silently pretending its graph is complete.

### 4.9 Dependency mutation and package-manager behavior

Current recipes vary by ecosystem.

Examples:

- Java dependency upgrades manipulate build declarations;
- JavaScript dependency recipes can run the package manager to regenerate locks;
- current Python upgrade recipes support `pyproject.toml`, `requirements.txt`, and `Pipfile`, with lock regeneration behavior that differs by format/tool.

This reinforces that the transformation engine can combine:

```text
semantic source rewrite
+
structured config mutation
+
ecosystem execution
```

depending on responsibility.

### 4.10 Moderne scale layer

Moderne adds:

- thousands of recipes;
- large repository sets;
- dry-run result inspection;
- commit/PR strategies;
- migration tracking;
- curated recipe marketplaces.

This is valuable as a mature UX/governance reference.

### 4.11 Limitations / cost

The deterministic recipe model has a major cost:

> someone must encode the migration semantics.

For known, recurring migrations that is a feature. For novel breaking changes or paradigm shifts, recipe creation can be expensive.

### 4.12 Transferable ideas

- format-preserving semantic IR for mutation;
- separate analysis/search from mutation;
- explicit preconditions;
- composable remediation primitives;
- idempotence;
- dry-run before effect;
- structured data tables;
- expose low-confidence/parse/resolution failures;
- curate approved remediation capabilities;
- reuse real package-manager execution where required.

Sources:
- https://docs.openrewrite.org/
- https://docs.openrewrite.org/concepts-and-explanations/lossless-semantic-trees
- https://docs.openrewrite.org/concepts-and-explanations/type-attribution
- https://docs.openrewrite.org/concepts-and-explanations/recipes
- https://docs.openrewrite.org/reference/yaml-format-reference
- https://docs.openrewrite.org/authoring-recipes/recipe-conventions-and-best-practices
- https://docs.openrewrite.org/authoring-recipes/data-tables
- https://docs.openrewrite.org/reference/recipes-with-data-tables
- https://docs.moderne.io/user-documentation/moderne-platform/getting-started/running-your-first-recipe/
- https://docs.moderne.io/user-documentation/recipes/recipe-catalog/python/upgradedependencyversion/

---

## 5. DepRepair / DepBench

### 5.1 Different problem framing

DepRepair argues that dependency breaking-change repair is inherently cross-repository.

The crucial evidence may live in:

- upstream release notes;
- API diffs;
- migration instructions;

while the consumer repository only contains outdated usages.

This is especially important when no local failing test directly identifies the affected source.

### 5.2 Benchmark discipline

DepBench contains 95 real dependency-update repair cases across:

- Maven;
- npm;
- Cargo;
- PyPI.

Each case has a Docker-based executable oracle that runs the consumer's own tests.

This is currently one of the most relevant external evaluation designs for future UpgradePilot repair experiments.

### 5.3 Repair architecture

DepRepair uses three evidence-processing components:

```text
upstream evidence filter
→ distill relevant migration rules

consumer usage locator
→ identify affected source/import sites

subcategory-aware guide
→ tailor repair instructions to breakage class

→ single LLM repair call
→ patch
→ executable oracle
```

The breaking-change classes include:

- direct rename;
- compound API migration;
- import migration;
- paradigm shift.

### 5.4 Strong empirical result

The paper reports:

- 89.5% executable pass rate with GPT-5.5;
- 82.1% with Claude Opus 4.6;
- highest pass rate per tested backbone.

More importantly for architecture, raw upstream evidence **reduced** LLM/agent success by 7–23 percentage points, while structured evidence improved it.

That is a very strong argument for:

> preprocess and structure evidence before model repair.

### 5.5 Localization matters

The benchmark analysis reports:

- 60% of developer patches introduce an upstream API symbol absent from pre-update consumer source;
- 89% of patches touch multiple files;
- median patch size is broad enough that naive one-line API replacement is insufficient.

This explains why local code search alone is inadequate.

### 5.6 Residual hard class

Paradigm shifts remain the hardest category, with the best methods solving only around two-thirds of those cases.

That distinction is important:

```text
rename/import migration
→ rule/structured guidance friendly

paradigm shift
→ structural redesign/refactoring problem
```

A future remediation system should not treat both as the same repair class.

### 5.7 Failure taxonomy

The paper reports the **empty patch / no usable patch** as the dominant model failure, rather than incorrect patches being the only main problem.

That suggests remediation evaluation must include:

- abstention/no patch;
- partial patch;
- incorrect patch;
- valid but non-minimal patch;
- executable success.

### 5.8 Transferable ideas

- build cross-repository evidence before repair;
- convert noisy upstream text into migration rules;
- explicitly localize target usage;
- classify breaking-change type before generating a patch;
- evaluate with executable oracles;
- maintain a real protected repair benchmark;
- use general LLM repair for novel changes where recipes do not exist;
- do not assume multi-turn agents beat a well-grounded fixed model pipeline.

Source:
- https://arxiv.org/abs/2607.17957

---

## 6. Griffe — Python API-diff evidence

### 6.1 Product role

Griffe is not primarily a migration engine. It provides a Python API model that can be loaded:

- from source;
- from Git refs;
- from installed/importable code;
- from package versions/indexes.

It can compare two API snapshots and emit structured breaking-change objects.

### 6.2 Breakage classes

Documented breakages include:

- object removed;
- object kind changed;
- base class removed;
- parameter removed;
- parameter moved;
- required parameter added;
- optional parameter made required;
- parameter default changed;
- parameter kind changed;
- attribute value changed;
- some type-related categories.

This makes Griffe a compelling Python-native source of:

```text
old upstream API
vs
new upstream API
→ deterministic breaking-change candidates
```

### 6.3 Explicit unsupported semantic comparisons

Griffe's documentation explicitly states that some compatibility checks—such as return-type and attribute-type compatibility—are not yet supported because static compatibility is non-trivial.

This is architecturally important:

> API-diff tooling has an explicit supported semantic surface; it should not be treated as complete breaking-change detection.

### 6.4 Structured output

Breakages are objects, not merely text messages, and Griffe can serialize API models.

That could support downstream target-usage correlation without relying only on changelog language.

### 6.5 Source vs dynamic inspection

Griffe can analyze statically or inspect dynamically when needed, with controls over whether inspection is allowed/forced.

That creates another useful evidence-strength distinction.

### 6.6 Transferable ideas

For Python-first UpgradePilot research:

- evaluate Griffe as an upstream old/new API evidence source;
- preserve exact breakage kind and affected symbol;
- correlate breakages with target usage;
- record which comparison classes are unsupported;
- avoid interpreting “no Griffe breakage found” as general compatibility proof.

Sources:
- https://mkdocstrings.github.io/griffe/
- https://mkdocstrings.github.io/griffe/guide/users/checking/
- https://mkdocstrings.github.io/griffe/reference/api/checks/

---

## 7. LibCST — Python transformation substrate

### 7.1 Product role

LibCST parses Python into a concrete syntax tree that preserves formatting/comments and supports metadata-backed codemods.

It is not itself a dependency migration policy engine.

It is a **safe-ish structural transformation substrate**.

### 7.2 Codemod model

LibCST codemods provide:

- repository/file execution;
- metadata resolution;
- visitor/transformer abstractions;
- multi-pass transforms;
- warnings;
- structured success/failure/skip results;
- parallel application;
- unified diff output instead of immediate writes.

This is a useful Python-native analogue to part of OpenRewrite's transformation layer.

### 7.3 Metadata model

Codemods can declare metadata dependencies and retrieve scope/type/position/repository-level information.

A `FullRepoManager` can provide repo-level metadata caches.

This can support transformations that are more semantic than raw text replacement.

### 7.4 Transferable idea

A possible future Python repair stack could be:

```text
Griffe
→ upstream API change facts

target structural search / type metadata
→ affected usage sites

recipe/model-generated migration plan
→ LibCST codemod

tests / build / other verification
→ validated or rejected patch
```

This is only a research hypothesis. It has not been compared experimentally.

Sources:
- https://libcst.readthedocs.io/en/latest/
- https://libcst.readthedocs.io/en/latest/codemods.html
- https://github.com/Instagram/LibCST/blob/main/docs/source/metadata.rst
- https://github.com/Instagram/LibCST/blob/main/docs/source/codemods.rst

---

## 8. Cross-system responsibility map

| Responsibility | OSV Guided Remediation | OpenRewrite/Moderne | DepRepair | Griffe | LibCST |
| --- | --- | --- | --- | --- | --- |
| identify known problem | vulnerabilities | recipe/search precondition | dependency breaking change | upstream API breakage | external owner |
| generate remediation candidates | graph strategies | recipes | model repair | no | codemod author/model |
| rank strategies | graph risk/reward | configured recipe | implicit model reasoning | no | no |
| localize target usage | graph dependency relation | semantic tree / recipe search | explicit usage locator | upstream-only API tree | metadata/search |
| source transformation | no/general manifest focus | primary responsibility | LLM patch | no | primary substrate |
| manifest transformation | yes | yes | possible model patch | no | possible custom code |
| lock regeneration | yes | ecosystem-specific recipes/tools | patch/oracle dependent | no | external |
| executable validation | dependency recompute; install separate in some paths | external build/tests normally required | Docker consumer-test oracle | no | external |
| partial/no-fix state | explicit strategy limitations | skip/parse/resolution failures | empty/failed patch | unsupported comparison kinds | TransformSkip/Failure |
| deterministic repeatability | high | high/idempotent recipes | model-nondeterministic | high | high for given codemod |

---

## 9. Major independent findings

### Finding R1 — remediation selection and patch generation must remain separate concepts

OSV-Scanner shows remediation can first be:

```text
which strategy should we choose?
```

while OpenRewrite/LibCST show a separate responsibility:

```text
how do we execute a known transformation?
```

DepRepair adds a third:

```text
how do we synthesize a transformation when no known recipe exists?
```

This separation should be preserved in later architecture comparison.

### Finding R2 — deterministic recipes and generative repair are complementary, not substitutes

A likely mature hierarchy is:

```text
known high-confidence migration rule
→ deterministic recipe/codemod

novel but evidence-rich breaking change
→ evidence-grounded model repair

paradigm shift / low-confidence case
→ interactive investigation / maintainer
```

This is a hypothesis for Track C, not an adopted design.

### Finding R3 — the transformation world model matters

OpenRewrite's LST and LibCST's CST/metadata demonstrate that safe refactoring benefits from a format-preserving semantic structure.

This is distinct from the analysis/evidence graph question studied in Tier-1 #02.

A mature system may need:

```text
analysis/evidence graph
!=
source transformation IR
```

rather than forcing one representation to serve both.

### Finding R4 — “minimal remediation” is multi-dimensional

OSV optimizes vulnerability removal against dependency graph change.

A dependency migration can also optimize for:

- files changed;
- API edits;
- major-version jumps;
- transitive churn;
- runtime behavior risk;
- security risk;
- test impact;
- human review burden.

There may be no single global minimum.

### Finding R5 — executable validation is the strongest practical repair oracle found

DepBench's Docker-based consumer test oracle provides concrete patch validation.

But executable success remains bounded by test adequacy and environment fidelity.

So:

```text
tests pass after repair
!=
proof of global semantic correctness
```

### Finding R6 — upstream source/API diff deserves higher priority in UpgradePilot research

Griffe and DepRepair both show that upstream API differences can be structured mechanically rather than inferred only from release prose.

For Python, this is especially actionable.

### Finding R7 — paradigm shifts need a different remediation class

DepRepair's hardest cases are not simple symbol edits but conceptual/API paradigm changes.

Those may justify:

- broader semantic model reasoning;
- multi-step agent investigation;
- maintainer interaction;
- or explicit non-automatic remediation.

### Finding R8 — mutation security becomes a first-class architecture concern

Any future remediation path that runs package managers or arbitrary project build/test commands inherits:

- install-script execution;
- registry/network access;
- credentials;
- filesystem mutation;
- potentially malicious repository code.

This means remediation architecture cannot be designed independently from the later agent-execution-security research family.

---

## 10. What this changes about UpgradePilot research

### 10.1 Do not rush UpgradePilot into patch generation

The current product decision-analysis responsibility remains valuable independently of remediation.

The research suggests a future separation:

```text
DECISION / IMPACT SYSTEM
What is wrong / relevant / unresolved?

then optionally

REMEDIATION PLANNER
What repair strategies are justified?

then optionally

PATCH ENGINE
How is the selected repair materialized?

then

VALIDATOR
What does the changed repository prove?
```

### 10.2 Python-first remediation has a plausible structural stack

A credible future experiment is:

```text
Griffe old/new API diff
+
target usage localization
+
migration evidence
→ deterministic recipe if known
OR bounded model repair if novel
→ LibCST transform
→ exact diff
→ targeted/full tests
```

This is attractive because each layer can be evaluated independently.

### 10.3 Recipe libraries can become a memory of validated migrations

OpenRewrite demonstrates a mature pattern:

```text
one migration solved well
→ encode as reusable recipe
→ future cases become deterministic
```

A future UpgradePilot could potentially convert repeated model-assisted migration knowledge into deterministic reusable Python migration recipes rather than repeatedly paying model uncertainty.

This is a research hypothesis and may or may not fit product scope.

---

## 11. What should NOT be copied blindly

1. **Do not turn UpgradePilot into a codemod platform** before the decision-support product is justified.
2. **Do not treat recipe availability as proof that the recipe applies** to this exact target.
3. **Do not treat successful tests as universal correctness**.
4. **Do not run package-manager/build commands on untrusted repositories without a strong sandbox/policy boundary**.
5. **Do not assume an LLM agent is better than a grounded single-call repair pipeline**.
6. **Do not equate API signature compatibility with behavioral compatibility**.
7. **Do not use “minimum change” without defining the dimension being minimized**.
8. **Do not generate patches before establishing whether remediation is actually the current maintainer need**.

---

## 12. Track-C hypotheses and future experiments

1. Compare changelog-only upstream evidence against Griffe/API-diff evidence for Python dependency updates.
2. Compare a deterministic API migration rule against DepRepair-style LLM repair on the same migration class.
3. Test whether a model can generate a LibCST/OpenRewrite-style deterministic codemod from one validated repair and whether that rule generalizes safely.
4. Compare graph-level “minimal dependency change” against source-edit minimality and maintainer review burden.
5. Evaluate whether repair strategy selection should be deterministic optimization, model planning, or interactive human choice.
6. Create explicit repair outcome states:
   - fully remediated;
   - partially remediated;
   - patch proposed but validation failed;
   - no admissible strategy;
   - unsupported transformation;
   - unsafe to execute;
   - maintainer action required.
7. Treat package-manager execution as a privileged capability with explicit evidence and security policy.
8. Investigate whether repeated model repairs can be distilled into approved reusable recipes.

---

## 13. Sources checked

### OSV-Scanner
- https://google.github.io/osv-scanner/experimental/guided-remediation/

### OpenRewrite / Moderne
- https://docs.openrewrite.org/
- https://docs.openrewrite.org/concepts-and-explanations/lossless-semantic-trees
- https://docs.openrewrite.org/concepts-and-explanations/type-attribution
- https://docs.openrewrite.org/concepts-and-explanations/recipes
- https://docs.openrewrite.org/reference/yaml-format-reference
- https://docs.openrewrite.org/authoring-recipes/recipe-conventions-and-best-practices
- https://docs.openrewrite.org/authoring-recipes/data-tables
- https://docs.openrewrite.org/reference/recipes-with-data-tables
- https://docs.moderne.io/user-documentation/moderne-platform/getting-started/running-your-first-recipe/
- https://docs.moderne.io/user-documentation/recipes/recipe-catalog/python/upgradedependencyversion/

### DepRepair / DepBench
- https://arxiv.org/abs/2607.17957

### Griffe
- https://mkdocstrings.github.io/griffe/
- https://mkdocstrings.github.io/griffe/guide/users/checking/
- https://mkdocstrings.github.io/griffe/reference/api/checks/

### LibCST
- https://libcst.readthedocs.io/en/latest/
- https://libcst.readthedocs.io/en/latest/codemods.html
- https://github.com/Instagram/LibCST/blob/main/docs/source/metadata.rst
- https://github.com/Instagram/LibCST/blob/main/docs/source/codemods.rst

---

## 14. Status / next report

**Tier-1 Report 03: COMPLETE.**

Next research family:

> **Tier-1 Report 04 — dependency/evidence graph foundations + provenance standards**

Primary systems/standards:

- deps.dev / Open Source Insights;
- GUAC;
- OSS Review Toolkit;
- SBOM ecosystems such as SPDX/CycloneDX;
- in-toto / SLSA / Sigstore/GitHub attestations where relevant.

Central question:

> should UpgradePilot invent and own its own evidence/provenance representation, or can mature dependency graphs and supply-chain provenance standards provide part of that substrate?
