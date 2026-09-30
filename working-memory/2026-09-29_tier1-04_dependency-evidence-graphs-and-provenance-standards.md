# Tier 1 Report 04 — Dependency / Evidence Graph Foundations + Provenance Standards

**Recorded:** 2026-09-29  
**Branch:** `analysis/ai-agentic-capability-map-2026-09-28`  
**Status:** COMPLETE initial deep report  
**Research family:** Dependency/evidence graphs + provenance/attestation standards  
**Systems/standards examined:** deps.dev / Open Source Insights, GUAC, OSS Review Toolkit (ORT), SPDX 3.0.1, CycloneDX 1.7, SLSA 1.2, in-toto Attestation Framework v1.2, Sigstore/Cosign, GitHub artifact attestations / dependency submission  
**Purpose:** determine which parts of UpgradePilot's future evidence/provenance substrate should remain domain-specific and which can reuse or interoperate with mature graph, SBOM, attestation, and supply-chain standards.

This report records external research evidence only. It does not change accepted UpgradePilot architecture or authorize adoption.

---

## 1. Research questions

1. What dependency/evidence graph capabilities already exist publicly?
2. How do mature systems represent package identity, versions, dependency edges, build inputs/outputs, and provenance?
3. Do existing standards represent uncertainty, completeness, “no assertion”, confidence, evidence producer, or claim provenance?
4. Can existing schemas represent UpgradePilot-style evidence without losing important semantics?
5. Where do standards stop and domain-specific decision reasoning begin?
6. Could UpgradePilot consume/export these formats without making them its internal reasoning model?
7. Which tools/standards are valuable hands-on learning targets?

---

## 2. Executive result

The broad answer is:

> UpgradePilot should **not assume it needs to invent every evidence/provenance primitive**, but existing supply-chain standards are also **not a ready-made replacement for its decision model**.

The research reveals three different layers:

```text
PACKAGE / DEPENDENCY KNOWLEDGE
deps.dev
ORT Analyzer
GitHub dependency graph/submission

↓ can feed

SUPPLY-CHAIN EVIDENCE / GRAPH AGGREGATION
GUAC
SPDX
CycloneDX

↓ can be bound / authenticated by

PROVENANCE / ATTESTATION INFRASTRUCTURE
SLSA
in-toto
Sigstore
GitHub artifact attestations

↓ still does NOT inherently provide

TARGET-SPECIFIC DECISION SEMANTICS
"what does this dependency update mean for this exact repository,
environment, CI path, runtime state, and maintainer action?"
```

The strongest finding is that **CycloneDX 1.7 and SPDX 3.0.1 are much richer than a simple component inventory**.

CycloneDX 1.7 can represent:

- dependency relationships and their completeness;
- component identity evidence;
- evidence techniques and per-technique confidence;
- exact occurrences with file/line/symbol;
- call stacks;
- tools that produced evidence;
- workflow/formulation information;
- claims and counterclaims;
- assessors;
- attestations;
- evidence attached to claims;
- confidence/conformance;
- citations;
- vulnerability and VEX-like data.

SPDX 3.0.1 introduces profile-based modeling and supports:

- relationship objects;
- relationship completeness;
- explicit `NoneElement`;
- explicit `NoAssertionElement`;
- software/build/security profiles;
- build inputs/outputs;
- build tools;
- invoking agents;
- lifecycle-scoped relationships.

These are close enough to several UpgradePilot concepts that later Track C must test **interoperability and reuse**, not assume a custom vocabulary is automatically superior.

At the same time, these standards do not define UpgradePilot's proposition semantics such as:

- static command occurrence vs exact runtime execution;
- package-manager semantic precedence;
- target-specific applicability;
- “no evidence” vs “evidence of absence” for arbitrary impact mechanisms;
- investigation planning;
- maintainer-action permission;
- cross-mechanism sufficiency.

Therefore the strongest architecture hypothesis from this report is:

```text
domain-specific internal reasoning model

+ standards-aware adapters / imports / exports / attestations

rather than

either:
  fully custom isolated universe
or
  forcing all internal reasoning into SBOM/provenance schemas
```

---

## 3. deps.dev / Open Source Insights

### 3.1 Product responsibility

deps.dev is a public package/dependency intelligence service.

For package ecosystems including PyPI, npm, Maven, Cargo, NuGet, RubyGems, and Go, the API exposes:

- available package versions;
- publication/deprecation metadata;
- licenses;
- security advisories;
- project/package associations;
- declared requirements;
- resolved dependency graphs;
- OpenSSF Scorecard data;
- OSS-Fuzz information.

For PyPI specifically, requirement information includes:

- project name;
- extras;
- version specifier;
- environment marker;
- provided extras;
- external dependencies;
- required Python version.

This is immediately relevant to UpgradePilot's Python-first scope.

### 3.2 Resolved dependency graph

The API exposes a resolved dependency graph for supported package versions.

Important limitation:

> deps.dev describes the graph as similar to installing the package on a **generic 64-bit Linux system with no other dependencies present**, with exact meaning varying by ecosystem.

Therefore:

```text
deps.dev resolved graph
!=
exact target repository resolved environment
```

This makes it useful as:

- external package-version knowledge;
- candidate transitive relationships;
- version-to-version dependency change analysis;
- comparison/enrichment;

but not sufficient as exact target-environment evidence.

### 3.3 Requirements vs resolution

The API separately exposes:

```text
declared requirements
vs
resolved dependency graph
```

That distinction is valuable and independently aligns with UpgradePilot's concern that declarations should not be confused with realized state.

### 3.4 Package/project identity

deps.dev aggregates registry and source-host data and maps projects to package versions.

Its API notes that package/project mappings derived from attestations may be prioritized.

That is relevant for UpgradePilot's recurring problem:

```text
package identity
↔ upstream repository identity
```

### 3.5 Transferable value

Potential reuse:

- package/version metadata;
- PyPI requirements and environment markers;
- resolved generic dependency graphs;
- source-project mappings;
- advisory/risk enrichment;
- version-to-version dependency topology comparison.

Do not treat as:

- exact target resolution;
- target platform/environment truth;
- source of package-manager runtime semantics;
- target usage/reachability proof.

### 3.6 Learning value

**High-value hands-on candidate.**

A bounded lab could:

```text
query two PyPI versions
→ retrieve requirements
→ retrieve resolved graphs
→ diff transitive topology
→ compare against UpgradePilot target-derived evidence
→ record mismatch classes
```

This teaches:

- public dependency intelligence APIs;
- package identity canonicalization;
- PURL/ecosystem data;
- graph comparison;
- external-data reliability boundaries.

Sources:
- https://deps.dev/
- https://docs.deps.dev/api/v3/

---

## 4. GUAC — Graph for Understanding Artifact Composition

### 4.1 Product responsibility

GUAC is an OpenSSF project that aggregates heterogeneous software supply-chain metadata into a queryable graph.

Its inputs include formats/data such as:

- SPDX;
- CycloneDX;
- OpenVEX;
- CSAF;
- DSSE;
- in-toto;
- OpenSSF Scorecard;

and it can enrich the graph using:

- deps.dev for dependency/package data;
- OSV for vulnerability data;
- ClearlyDefined for license information.

This is directly relevant to our “evidence graph” hypothesis.

### 4.2 Architecture

The public architecture separates:

```text
Collectors
→ acquire documents/data

Ingestor
→ parse external formats into GUAC ontology objects

Assembler
→ create graph entities/relationships in database

GraphQL service
→ query/mutate graph

CollectSub
→ request additional enrichment when newly observed identifiers need more data
```

This is a strong real-world example of:

```text
heterogeneous evidence
→ normalization
→ canonical graph
→ demand-driven enrichment
→ query
```

### 4.3 Identity normalization and relationship synthesis

GUAC's stated purpose includes normalizing entity identities and mapping standard relationships.

That is important because a graph only becomes useful if:

```text
same package/repository/artifact
from different evidence producers
→ reconciles to stable identities
```

Otherwise a graph becomes a collection of disconnected claims.

### 4.4 Demand-driven enrichment

GUAC's CollectSub architecture is especially interesting.

Example:

```text
SBOM contains PURL
→ ingestor adds graph entity
→ CollectSub announces information need
→ deps.dev collector recognizes PURL
→ dependency/source metadata acquired
→ graph enriched
```

This is conceptually similar to an evidence-gap investigation system, but it is deterministic/event-driven rather than LLM-planned.

That gives Track C another important comparator:

> some “agentic” evidence acquisition may actually be expressible as demand-driven graph enrichment.

### 4.5 GUAC is not a decision engine

GUAC aggregates/query/enriches evidence.

It does not inherently answer:

- whether a dependency update is safe;
- which impact mechanism applies;
- whether CI proves compatibility;
- which maintainer action is justified.

Those remain consumer responsibilities.

### 4.6 GraphQL stability note

GUAC documentation states that its GraphQL definitions are not yet stable.

This matters for integration cost and supports keeping GUAC as a comparator/optional substrate rather than making a premature product dependency.

### 4.7 Transferable ideas

High-value architecture patterns:

1. heterogeneous evidence ingestion;
2. canonical ontology;
3. stable entity identity before reasoning;
4. graph enrichment triggered by missing information;
5. external evidence producers remain distinguishable;
6. query layer separated from ingestion;
7. source formats remain interoperable.

### 4.8 Learning value

**Very high-value hands-on candidate.**

A bounded real lab could:

```text
run GUAC locally with Docker Compose
→ ingest a CycloneDX/SPDX document
→ enable deps.dev enrichment
→ inspect graph via GraphQL
→ query package → dependency → vulnerability/source relationships
→ compare GUAC graph shape with UpgradePilot evidence needs
```

Skills gained:

- graph/knowledge representation;
- GraphQL;
- Docker Compose/service orchestration;
- SBOM ingestion;
- PURL identity;
- supply-chain security metadata;
- demand-driven enrichment;
- evidence normalization.

Sources:
- https://docs.guac.sh/
- https://docs.guac.sh/guac/
- https://docs.guac.sh/guac/guac-ontology/
- https://docs.guac.sh/guac/guac-components/
- https://docs.guac.sh/guac/graphql/
- https://docs.guac.sh/guac/certifier-deps-dev/

---

## 5. OSS Review Toolkit (ORT)

### 5.1 Product responsibility

ORT is a modular open-source software composition/policy pipeline.

Its major stages are:

```text
Analyzer
→ determine dependency/project metadata

Downloader
→ retrieve source

Scanner
→ license/copyright/source scanning

Advisor
→ vulnerability providers

Evaluator
→ policy rules

Reporter
→ SPDX/CycloneDX/HTML/notices/etc.

Notifier
→ external communication
```

This is highly relevant because it demonstrates a mature **evidence pipeline with stable stage ownership**.

### 5.2 Analyzer design

ORT's Analyzer queries detected package managers/build systems and emits a structured `OrtResult`.

The result becomes the input to downstream tools.

This is an important architecture precedent:

```text
one canonical intermediate result
→ several independent consumers
```

rather than each consumer re-running package discovery independently.

### 5.3 Real package-manager dependency analysis

ORT does not rely only on manifest parsing. Its analyzer can query real package managers, subject to tool/environment requirements.

The docs explicitly state analysis assumptions including that projects may need to build with common/default configuration.

So ORT also demonstrates the same boundary seen elsewhere:

```text
real ecosystem tool
→ stronger package-resolution fidelity

but
environment/tool availability
→ operational precondition
```

### 5.4 Advisor source provenance

The Advisor stores vulnerability results with additional information such as the data source and severity.

This is a simple but useful precedent for retaining:

```text
finding
+ provider identity
+ provider-specific attributes
```

### 5.5 Evaluator / policy layer

ORT's Evaluator executes policy rules after evidence acquisition.

This produces a clean separation:

```text
facts/findings
!=
policy judgment
```

That is relevant to UpgradePilot's later action-permission research.

### 5.6 Reporter interoperability

ORT can emit both:

- SPDX;
- CycloneDX;

alongside custom/human-readable reports.

This is a strong example of:

> rich internal model + standard external projections.

That pattern is likely more appropriate for UpgradePilot than forcing the internal state to equal one standard.

### 5.7 Transferable ideas

1. canonical internal intermediate representation;
2. staged analyzer/advisor/evaluator/reporter responsibilities;
3. evidence-provider provenance;
4. policy after evidence;
5. standard export formats without standard-driven internal architecture;
6. external tool requirements recorded explicitly;
7. storage/reuse of expensive scan outputs.

### 5.8 Learning value

**High-value hands-on candidate, but heavier than deps.dev/GUAC standards experiments.**

A bounded lab could:

```text
run ORT Analyzer on a small Python repository
→ inspect OrtResult
→ emit SPDX/CycloneDX
→ compare dependency resolution with UpgradePilot/deps.dev
→ optionally add one Evaluator rule
```

Skills:

- software composition analysis;
- package-manager abstraction;
- policy-as-code;
- structured evidence pipelines;
- SBOM export;
- JVM/Kotlin tooling exposure.

Sources:
- https://oss-review-toolkit.org/ort/
- https://oss-review-toolkit.org/ort/docs/intro
- https://oss-review-toolkit.org/ort/docs/tools/analyzer
- https://oss-review-toolkit.org/ort/docs/tools/advisor
- https://oss-review-toolkit.org/ort/docs/tools/evaluator
- https://oss-review-toolkit.org/ort/docs/tools/reporter

---

## 6. SPDX 3.0.1

### 6.1 Much broader than an SBOM file format

SPDX 3 uses a profile-based model.

Current profiles include:

- Core;
- Software;
- Build;
- Security;
- AI;
- Dataset;
- licensing profiles;
- extension mechanisms.

This indicates SPDX is evolving toward a generalized software/supply-chain information model rather than only inventory/license interchange.

### 6.2 Relationship as a first-class assertion

SPDX models relationships explicitly.

A relationship can include completeness information.

Two particularly important explicit values exist:

```text
NoneElement
→ assertion that no such relationship exists

NoAssertionElement
→ no assertion is being made about whether the relationship exists
```

This is highly relevant to UpgradePilot's evidence philosophy.

It externally demonstrates the value of distinguishing:

```text
known absence
!=
unknown / no assertion
```

### 6.3 Build profile

The SPDX Build profile can represent:

- build instance;
- inputs;
- outputs;
- invoking agent;
- host;
- configuration;
- tools;
- parent/child build relationships.

That means parts of CI/build provenance may be representable using a standard vocabulary.

### 6.4 What SPDX does not supply

SPDX relationships express assertions but do not automatically establish how UpgradePilot should derive or trust them.

It does not define UpgradePilot-specific reasoning such as:

- exact package-manager CLI precedence;
- conditional workflow command execution;
- target impact discovery;
- maintainer decision sufficiency.

So SPDX is best considered:

```text
portable relationship/evidence vocabulary
not
domain reasoning algorithm
```

### 6.5 Learning value

**Very high standards exposure.**

Hands-on opportunity:

```text
construct SPDX 3.0.1 model for:
repo revision
→ build
→ input dependency
→ produced artifact

represent:
known relation
vs
NoAssertion
vs
None

then compare with UpgradePilot state semantics
```

Skills:

- graph/relationship schemas;
- software supply-chain standards;
- provenance modeling;
- semantic interoperability;
- explicit uncertainty representation.

Sources:
- https://spdx.github.io/spdx-spec/v3.0.1/
- https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Classes/Relationship/
- https://spdx.github.io/spdx-spec/v3.0.1/model/Build/Build/
- https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Vocabularies/ProfileIdentifierType/

---

## 7. CycloneDX 1.7

### 7.1 Most surprising standard in this report

CycloneDX 1.7 goes substantially beyond package inventory.

It can represent:

- components/services;
- dependency relationships;
- composition/completeness;
- vulnerabilities;
- evidence;
- annotations;
- formulation/process;
- declarations;
- claims/counterclaims;
- attestations;
- citations.

This makes it especially relevant to UpgradePilot.

### 7.2 Dependency graph completeness semantics

CycloneDX explicitly warns that:

```text
component absent from dependency graph
!=
component proven dependency-free
```

Unrepresented dependencies may be unknown/opaque.

This is another independent external validation of open-world reasoning.

### 7.3 Evidence model

CycloneDX evidence can include:

- identity field being supported;
- concluded value;
- overall confidence;
- independent evidence methods;
- confidence per method;
- tools used;
- occurrences;
- call stack.

Evidence techniques include:

- source code analysis;
- binary analysis;
- manifest analysis;
- AST fingerprint;
- hash comparison;
- instrumentation;
- dynamic analysis;
- attestation;
- other.

This is strikingly close to an **evidence producer / method / confidence / result** architecture.

### 7.4 Occurrence-level evidence

Occurrences can include:

- path/location;
- line;
- offset;
- symbol;
- contextual snippet.

That is useful for source-grounded impact/reachability evidence.

### 7.5 Call-stack evidence

CycloneDX can attach call-stack information describing package/module/function relationships.

This may be useful as an interchange format for reachability evidence.

### 7.6 Formulation

CycloneDX `formulation` can describe how a referencable object was:

- created;
- assembled;
- deployed;
- tested;
- certified;

using workflows/tasks/steps, including declared and observed formulas.

This is especially interesting to UpgradePilot's CI/runtime evidence research.

### 7.7 Claims, counterclaims, assessors, attestations

CycloneDX declarations can encode:

- assessors;
- claims;
- counterclaims;
- evidence;
- target;
- attestation mapping;
- conformance;
- confidence;
- rationale.

This means the standard already supports a generic:

```text
claim
↔ evidence
↔ assessor
↔ confidence/conformance
↔ counterclaim
```

structure.

However, it remains generic. UpgradePilot would still need to define domain-specific claim semantics.

### 7.8 Citations

CycloneDX 1.7 also has citations/attribution mechanisms indicating who supplied information for specific fields.

That is relevant to multi-producer evidence lineage.

### 7.9 Architecture implication

CycloneDX is strong enough that Track C must ask:

> should UpgradePilot's external evidence/report format be CycloneDX-compatible or CycloneDX-derived?

But a second question is equally important:

> would forcing UpgradePilot's internal reasoning state into CycloneDX make the domain logic harder to understand/test?

The likely answer may differ for internal vs external representations.

### 7.10 Learning value

**Extremely high hands-on standards candidate.**

A bounded lab could construct a CycloneDX 1.7 document containing:

```text
dependency component
+ dependency edge
+ target occurrence
+ analysis technique
+ confidence
+ callstack
+ workflow/formulation
+ claim
+ evidence
+ assessor
+ citation
```

and evaluate how much of one real UpgradePilot evidence case maps cleanly.

Skills:

- SBOM standards;
- evidence/claim modeling;
- provenance;
- reachability representation;
- interoperability;
- schema validation.

Sources:
- https://cyclonedx.org/docs/1.7/json/
- https://cyclonedx.org/docs/1.7/proto/

---

## 8. SLSA 1.2

### 8.1 Scope

SLSA 1.2 is the current approved specification.

It separates tracks, currently including:

- Build Track;
- Source Track.

The Build Track focuses on artifact provenance and increasing protections against build/provenance tampering.

The Source Track focuses on how source revisions were created and the controls surrounding those revisions.

### 8.2 Provenance is verifiable production history, not semantic compatibility

SLSA provenance answers questions such as:

- which builder produced the artifact?
- using which source/inputs?
- with which parameters?
- under which build system/process?
- what output artifact resulted?

It does not answer:

- will dependency version X break target repository Y?
- did tests exercise the affected behavior?
- is an upstream API change applicable?

This distinction is crucial.

### 8.3 Resolved dependency completeness is explicitly bounded

SLSA build provenance includes `resolvedDependencies`.

The specification states completeness is best effort at least through Build L3.

That is important:

> even cryptographically protected provenance can contain evidence whose **completeness guarantee is bounded**.

Authentication/integrity does not magically create completeness.

### 8.4 Source provenance relevance

SLSA 1.2 reintroduces a Source Track.

This may become useful for:

- establishing source revision provenance;
- verifying source-system controls;
- distinguishing source revision identity from artifact build provenance.

### 8.5 Learning value

**High-value standards exposure**, especially for AI Security Automation / supply-chain work.

Hands-on candidate:

```text
generate/inspect SLSA provenance for a GitHub Actions artifact
→ identify subject
→ builder
→ source
→ build inputs
→ resolved dependencies
→ compare guarantees to UpgradePilot evidence claims
```

Sources:
- https://slsa.dev/spec/v1.2/
- https://slsa.dev/spec/v1.2/tracks
- https://slsa.dev/spec/v1.2/provenance
- https://slsa.dev/spec/v1.2/build-track-basics
- https://slsa.dev/spec/v1.2/source-requirements

---

## 9. in-toto Attestation Framework v1.2

### 9.1 Generic authenticated statement model

The in-toto Attestation Framework defines layers:

- Predicate;
- Statement;
- Envelope;
- Bundle.

A statement binds:

```text
subject artifact(s)
identified by digest

+
predicateType

+
predicate payload
```

The predicate can carry arbitrary type-specific metadata.

### 9.2 Why this is relevant

UpgradePilot could theoretically define an attestation predicate for a decision/evidence report.

For example:

```text
subject:
  exact repository revision / artifact digest

predicateType:
  UpgradePilot decision-evidence schema

predicate:
  evidence summary
  unresolved states
  analysis version
  policy version
  claim set
```

Then the statement could be signed/bundled through standard attestation mechanisms.

This would give cryptographic binding and producer identity without requiring the internal reasoning model itself to be in-toto-shaped.

### 9.3 Existing predicates

The framework already has predicate patterns for:

- build/link information;
- references to SBOMs;
- release/package identity.

The reference predicate can bind an artifact to an SPDX SBOM by digest.

This demonstrates composition:

```text
artifact attestation
→ points to SBOM
→ SBOM contains dependency evidence
```

rather than one huge document containing everything.

### 9.4 Important boundary

A signed attestation proves:

- who/what signed;
- what exact subject/predicate bytes were attested;
- integrity/binding.

It does **not** prove the predicate's semantic claim is correct.

This should remain explicit in UpgradePilot.

### 9.5 Learning value

**Very high practical supply-chain/security exposure.**

Bounded lab:

```text
create small predicate
→ bind to artifact/revision digest
→ wrap as in-toto Statement
→ sign with cosign/Sigstore
→ verify
→ intentionally change subject/predicate
→ demonstrate verification failure
```

Skills:

- attestations;
- DSSE;
- artifact identity;
- cryptographic signing/verification;
- predicate schema design;
- policy consumption.

Sources:
- https://github.com/in-toto/attestation/blob/main/spec/README.md
- https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md
- https://github.com/in-toto/attestation/blob/main/spec/v1/predicate.md
- https://github.com/in-toto/attestation/blob/main/spec/predicates/reference.md
- https://github.com/in-toto/attestation/blob/main/spec/predicates/link.md

---

## 10. Sigstore / Cosign / GitHub artifact attestations

### 10.1 Sigstore / Cosign

Cosign can sign and verify artifacts and in-toto attestations.

It supports policy validation over attestation content, including policy languages such as CUE/Rego in documented flows.

This demonstrates another important separation:

```text
attested evidence
!=
policy decision

attestation
→ cryptographic verification
→ policy evaluation
```

### 10.2 GitHub artifact attestations

GitHub artifact attestations use Sigstore-based infrastructure.

Public repository attestations are associated with Sigstore's public infrastructure/transparency log.

GitHub attestations bind information such as:

- workflow;
- repository;
- organization;
- environment;
- commit SHA;
- triggering event;

to built artifacts.

GitHub also supports SBOM-associated attestations.

### 10.3 Supply-chain integrity vs UpgradePilot decision truth

These tools can strengthen statements such as:

```text
this artifact/report was produced
by this trusted workflow
for this exact revision
using this build context
```

They cannot independently prove:

```text
UpgradePilot's semantic conclusion is correct
```

But they can make:

- provenance;
- report identity;
- evidence bundle integrity;
- reproducibility/audit trail;

substantially stronger.

### 10.4 Learning value

**Excellent hands-on candidate**, especially because UpgradePilot already lives on GitHub Actions.

Potential project experiment:

```text
generate a small UpgradePilot analysis artifact
→ generate GitHub artifact attestation
→ verify with gh attestation / cosign
→ record exact repo + workflow + commit binding
```

This would be real, portfolio-visible supply-chain security work if product relevance justifies it.

Sources:
- https://docs.sigstore.dev/quickstart/quickstart-cosign/
- https://docs.sigstore.dev/cosign/verifying/attestation/
- https://docs.github.com/en/actions/concepts/security/artifact-attestations
- https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations

---

## 11. GitHub Dependency Submission API as a live evidence-store precedent

GitHub's dependency submission API accepts commit-bound dependency snapshots.

A snapshot records:

- commit SHA;
- ref;
- detector identity/version;
- job ID/correlator;
- scanned time;
- manifests;
- resolved dependencies;
- scope.

GitHub can receive multiple submissions from different detectors and applies precedence/deduplication rules.

Notably, user/build-time submissions are prioritized because they often provide more complete information than purely static detection.

This is very relevant to UpgradePilot because it demonstrates:

```text
same proposition family
+
multiple evidence producers
+
producer precedence
+
revision binding
+
freshness / latest snapshot semantics
```

in a production platform.

It also supports matrix/job correlators to keep distinct runtime contexts separate.

This is directly adjacent to UpgradePilot's CI/evidence identity work.

Sources:
- https://docs.github.com/en/rest/dependency-graph/dependency-submission
- https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/use-dependency-submission-api

---

## 12. Cross-standard comparison

| Layer | deps.dev | GUAC | ORT | SPDX 3.0.1 | CycloneDX 1.7 | SLSA / in-toto / Sigstore |
| --- | --- | --- | --- | --- | --- | --- |
| package/version knowledge | strong | via enrichment | strong analyzer | representable | representable | limited |
| resolved dependency graph | generic ecosystem graph | aggregated | target/project analysis | relationships | dependency graph | resolved deps may appear in provenance |
| target source occurrence | no | if ingested | not primary | representable generically | explicit occurrences | no |
| call stack/reachability | no | ontology-dependent | not primary | generic relations | explicit callstack evidence | no |
| evidence producer | source implicit/API | explicit graph provenance | provider/stage | element relationships/creation info | tools/methods/assessors/citations | signer/builder/attester |
| uncertainty/completeness | API/model limitations | graph-dependent | tool-specific | completeness + NoAssertion | composition/evidence confidence | provenance guarantees + bounded completeness |
| claims/counterclaims | no | graph facts | policy violations | generic assertions | explicit declarations | arbitrary predicates possible |
| build/process provenance | no | ingestible | execution context partly | Build profile | formulation | core responsibility |
| cryptographic authentication | no | not core | no | format itself no | format itself no | core |
| policy evaluation | no | external consumers | Evaluator | external | declarations possible | external verifier/policy |
| target-specific dependency update decision | no | no | no | no | no | no |

---

## 13. Major independent findings

### Finding G1 — standard vocabularies already model uncertainty better than expected

SPDX:

```text
None
!=
NoAssertion
```

CycloneDX:

- unknown dependency completeness;
- evidence confidence;
- method-specific confidence;
- assessor identity;
- claims/counterclaims.

SLSA:

- provenance guarantees are tied to levels/producer;
- resolved-dependency completeness can still be best effort.

This independently validates UpgradePilot's concern with evidence strength and unresolved state while showing that interoperability may be possible.

### Finding G2 — cryptographic provenance and semantic correctness are different dimensions

A signed SLSA/in-toto/Sigstore attestation can strongly prove:

```text
who produced this statement
for which exact artifact/revision
without tampering
```

but not:

```text
the statement's semantic conclusion is true
```

UpgradePilot must not confuse evidence authenticity with evidence correctness.

### Finding G3 — evidence graphs need normalization and identity before reasoning

GUAC makes identity normalization a central responsibility.

This independently supports the idea that an evidence graph cannot just ingest arbitrary nodes; it needs canonical identities and typed relationship semantics.

### Finding G4 — demand-driven enrichment may solve some “agentic” acquisition problems deterministically

GUAC CollectSub shows:

```text
new graph entity
→ missing data recognized
→ matching collector invoked
→ graph enriched
```

That should compete directly with LLM-planned evidence acquisition for mechanically identifiable information needs.

### Finding G5 — rich internal model + standard projections is a mature pattern

ORT maintains its own `OrtResult` and exports SPDX/CycloneDX.

That is strong precedent for:

```text
domain-specific internal state
+
standard interchange/export
```

instead of forcing internal architecture to mirror a standard.

### Finding G6 — CycloneDX is a much stronger candidate for UpgradePilot interoperability than initially expected

Its evidence/occurrence/callstack/declaration/formulation models overlap heavily with future UpgradePilot evidence-report concepts.

A real mapping experiment is justified.

### Finding G7 — GitHub already uses producer precedence for dependency evidence

Dependency submission precedence demonstrates that evidence producer class and collection method can legitimately affect which evidence is surfaced.

This is directly relevant to our graded evidence-authority research.

### Finding G8 — target resolution remains distinct from public package graphs

deps.dev's generic Linux resolution is valuable but cannot substitute for exact target environment proof.

That distinction should remain explicit if UpgradePilot consumes it.

---

## 14. Architecture implications for Track C

Track C should compare at least three evidence-substrate strategies.

### Strategy A — fully custom domain model

```text
UpgradePilot owns all evidence/proposition types internally
standards only optional at edges
```

Strength:
maximum domain precision.

Risk:
reinventing identity/provenance/graph/attestation vocabulary.

### Strategy B — standards-native internal model

```text
CycloneDX/SPDX/in-toto/GUAC concepts become core internal state
```

Strength:
interoperability and existing ecosystem.

Risk:
domain logic distorted by generic schemas and high complexity.

### Strategy C — domain core + standards adapters

```text
UpgradePilot typed decision/evidence model
↕ mapping/adapters
CycloneDX / SPDX / in-toto / GitHub / GUAC / deps.dev
```

Strength:
preserves precise reasoning while gaining interoperability.

Risk:
mapping/duplication cost and potential semantic mismatch.

**Strategy C currently appears the strongest research candidate, but this report does not adopt it.**

---

## 15. Specific interoperability experiments worth considering

### Experiment 1 — CycloneDX evidence mapping

Take one current UpgradePilot case and attempt to encode:

- dependency component;
- occurrence;
- evidence technique;
- tool;
- confidence;
- call stack if applicable;
- workflow/formulation;
- claim;
- evidence;
- assessor;
- citation.

Record what maps cleanly and what does not.

### Experiment 2 — SPDX explicit unknown/none semantics

Map several UpgradePilot proposition states to:

- relationship exists;
- `NoneElement`;
- `NoAssertionElement`;
- completeness.

Determine whether the semantics are actually equivalent.

### Experiment 3 — GUAC graph lab

```text
CycloneDX/SPDX input
→ GUAC ingest
→ deps.dev/OSV enrichment
→ GraphQL query
```

Then ask whether a small UpgradePilot evidence subset can be represented/queryable without losing provenance.

### Experiment 4 — GitHub dependency submission comparison

Compare:

- static GitHub dependency detection;
- submitted build-time dependency snapshot;
- UpgradePilot's exact package/environment evidence.

Study producer precedence, correlators, matrix identity, and freshness.

### Experiment 5 — signed UpgradePilot evidence artifact

Generate an UpgradePilot analysis artifact and attach an in-toto/GitHub/Sigstore attestation tied to:

- exact repo;
- exact revision;
- exact workflow/run;
- analysis artifact digest.

Measure audit/replay value.

---

## 16. Learning / exposure opportunities

This report has unusually high career/skill value because these technologies sit directly in software supply-chain security.

### Highest-value hands-on candidates

#### GUAC — **project/lab experiment candidate**

Teaches:

- knowledge graphs;
- GraphQL;
- evidence normalization;
- SBOM ingestion;
- supply-chain ontology;
- Docker/service orchestration;
- demand-driven enrichment.

Suggested exposure:
**HANDS_ON_EXPERIMENTED** target.

#### CycloneDX 1.7 — **very high-priority standards lab**

Teaches:

- SBOM design;
- evidence representation;
- claims/attestations;
- vulnerability exchange;
- reachability evidence;
- process formulation;
- schema validation.

Suggested exposure:
hands-on mapping experiment, possibly later project integration for export.

#### SPDX 3.0.1 — **high-priority standards lab**

Teaches:

- graph relationship semantics;
- explicit unknown/no-assertion handling;
- build provenance;
- profile-based schemas;
- open source compliance/supply-chain modeling.

Suggested exposure:
hands-on modeling experiment.

#### SLSA + in-toto + Sigstore — **very high-priority security experiment**

Teaches:

- build/source provenance;
- attestations;
- cryptographic subject binding;
- DSSE;
- artifact signing/verification;
- CI supply-chain integrity.

Suggested exposure:
real GitHub Actions artifact-attestation experiment.

#### deps.dev — **easy, high-value practical lab**

Teaches:

- dependency graph APIs;
- requirements vs resolution;
- PyPI metadata;
- public graph data;
- package/project identity.

Suggested exposure:
hands-on API experiment soon.

#### ORT — **valuable but heavier**

Teaches:

- SCA pipeline architecture;
- package-manager abstraction;
- policy-as-code;
- SBOM output;
- advisor/scanner composition;
- JVM/Kotlin toolchain exposure.

Suggested exposure:
bounded lab if Tier-1/Track-C comparison benefits from a full SCA pipeline.

### Career-relevance note

A real experiment combining:

```text
deps.dev
+ CycloneDX/SPDX
+ GUAC
+ SLSA/in-toto/Sigstore
```

would provide credible hands-on exposure across:

- dependency intelligence;
- SBOM;
- provenance;
- evidence graphs;
- supply-chain security;
- CI security;
- GraphQL;
- cryptographic attestations.

That aligns strongly with AI/security/platform engineering while still being relevant to UpgradePilot.

---

## 17. What should NOT be copied blindly

1. Do not make a universal knowledge graph the center of UpgradePilot before a concrete query need justifies it.
2. Do not replace domain-specific proposition semantics with generic SBOM relationships merely for standards compliance.
3. Do not interpret a signed attestation as semantic truth.
4. Do not interpret public deps.dev resolution as exact target resolution.
5. Do not treat absence from an SBOM/dependency graph as proven absence unless completeness semantics justify it.
6. Do not expose arbitrary numeric “confidence” unless the meaning/calibration is defined.
7. Do not adopt GUAC as infrastructure merely to gain graph experience; a bounded lab is sufficient until product pressure exists.
8. Do not generate SBOMs/provenance as decorative outputs that no consumer uses.
9. Do not conflate build provenance with runtime behavior or test coverage.
10. Do not make standards interoperability block core product learning/build progress.

---

## 18. Track-C hypotheses

1. UpgradePilot likely benefits from a domain-specific internal evidence model plus standards-aware adapters.
2. CycloneDX 1.7 may be suitable for external evidence/report exchange for some claim/evidence families.
3. SPDX 3.0.1 may supply useful build/relation/no-assertion semantics.
4. in-toto/SLSA/Sigstore could bind UpgradePilot reports to exact revisions/artifacts/workflows.
5. GUAC should be evaluated as a graph architecture comparator before building a bespoke evidence graph.
6. Some deterministic evidence acquisition can be event/graph-driven rather than agent-planned.
7. GitHub dependency submission provides a production precedent for producer precedence, revision binding and runtime-submitted dependency evidence.
8. External package graphs should be treated as contextual/candidate evidence, not target runtime truth.
9. Cryptographic provenance should become a separate trust dimension from semantic evidence authority.
10. If UpgradePilot eventually exposes interoperability, mapping fidelity must be tested proposition-by-proposition rather than assuming standards equivalence.

---

## 19. Sources checked

### deps.dev
- https://deps.dev/
- https://docs.deps.dev/api/v3/

### GUAC
- https://docs.guac.sh/
- https://docs.guac.sh/guac/
- https://docs.guac.sh/guac/guac-ontology/
- https://docs.guac.sh/guac/guac-components/
- https://docs.guac.sh/guac/graphql/
- https://docs.guac.sh/guac/certifier-deps-dev/

### ORT
- https://oss-review-toolkit.org/ort/
- https://oss-review-toolkit.org/ort/docs/intro
- https://oss-review-toolkit.org/ort/docs/tools/analyzer
- https://oss-review-toolkit.org/ort/docs/tools/advisor
- https://oss-review-toolkit.org/ort/docs/tools/evaluator
- https://oss-review-toolkit.org/ort/docs/tools/reporter

### SPDX
- https://spdx.github.io/spdx-spec/v3.0.1/
- https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Classes/Relationship/
- https://spdx.github.io/spdx-spec/v3.0.1/model/Build/Build/
- https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Vocabularies/ProfileIdentifierType/

### CycloneDX
- https://cyclonedx.org/docs/1.7/json/
- https://cyclonedx.org/docs/1.7/proto/

### SLSA
- https://slsa.dev/spec/v1.2/
- https://slsa.dev/spec/v1.2/tracks
- https://slsa.dev/spec/v1.2/provenance
- https://slsa.dev/spec/v1.2/build-track-basics
- https://slsa.dev/spec/v1.2/source-requirements

### in-toto / Sigstore / GitHub attestations
- https://github.com/in-toto/attestation/blob/main/spec/README.md
- https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md
- https://github.com/in-toto/attestation/blob/main/spec/v1/predicate.md
- https://github.com/in-toto/attestation/blob/main/spec/predicates/reference.md
- https://docs.sigstore.dev/quickstart/quickstart-cosign/
- https://docs.sigstore.dev/cosign/verifying/attestation/
- https://docs.github.com/en/actions/concepts/security/artifact-attestations
- https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations
- https://docs.github.com/en/rest/dependency-graph/dependency-submission
- https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/use-dependency-submission-api

---

## 20. Status / next report

**Tier-1 Report 04: COMPLETE.**

Next research family:

> **Tier-1 Report 05 — CI/runtime evidence + program-analysis techniques**

Primary areas:

- actionlint;
- zizmor;
- StepSecurity / Harden-Runner;
- GitHub Actions runtime evidence;
- act/workflow emulation;
- CodeQL;
- Joern;
- CrossHair/angr and bounded symbolic execution where relevant.

Central question:

> how much of UpgradePilot's difficult CI/runtime/environment reasoning can be solved with existing static analyzers, runtime telemetry, program-analysis graphs, workflow emulation, or symbolic execution before we build more custom rules or introduce AI?
