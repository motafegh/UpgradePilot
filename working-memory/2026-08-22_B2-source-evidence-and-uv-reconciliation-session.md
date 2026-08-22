# Working Memory — B2 Source/Evidence and uv Reconciliation Session

**Date:** 2026-08-22  
**Status:** ACTIVE  
**Branch:** `main`  
**Mode:** learning by doing and building  
**Live-state owner:** `../MEMORY.md`

## Why this session exists

Learning/review of the B2 dependency-environment/CI implementation exposed concrete design pressure before ordinary Cluster-6 integration:

- exact repository-file provider guarantees are stronger than the nominal internal evidence type;
- downstream modules revalidate provider-owned facts because the type permits weak/manual states;
- `uv_lock.py` and `uv_membership.py` duplicate material `uv.lock` structure and have already drifted;
- the static uv declaration loses S001 `--all-packages` workspace scope;
- current membership terminology can imply more than explicit selected-root reachability proves.

The dedicated learning-folder route is therefore paused and project work is proceeding through normal learning-by-building under `../OPERATING_GUIDE.md` and `../plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`.

## Plan progression

```text
✓ R0  re-anchor contracts + freeze behavior
→ R1  strengthen exact repository-file evidence ownership — IN PROGRESS
  R2  one bounded uv-specific structural lock model
  R3  preserve minimum real uv command/workspace scope
  R4  narrow uv membership to explicit selected-root reachability
  R5  rebind CI consumption to reconciled evidence
  R6  pressure S001 / S011 / S005 + changed-case workspace transfer
  R7  acceptance + audit disposition + deferred-plan re-review
```

No R1 product-source behavior has been modified yet.

## Non-negotiable retention discipline

Ali explicitly rejected implementation-preserving rationalization. The project rule is now:

> **Existing implementation is evidence to inspect, not authority to preserve.**

Current code, consumers, passing tests, comments, historical design, and prior effort show current behavior and migration pressure. They do **not** establish that a mechanism is necessary.

Every material mechanism under review must trace to a current independent reason:

```text
admitted product responsibility
or proof/evidence need
or material risk control
or real compatibility/external obligation
```

Do not use circular reasoning such as:

```text
X must stay because Y uses X
```

when Y's dependence on X is itself being reviewed.

This rule has been promoted to:

- root `../AGENTS.md`;
- `../OPERATING_GUIDE.md`;
- `../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md` as `JUST-001`–`JUST-003`;
- the active reconciliation plan;
- root `../MEMORY.md`.

Ali's predictions/answers remain learning inputs. AI leads from technical/professional evidence and corrects learner reasoning when needed.

## R0 — completed ownership/inventory freeze

**Status:** COMPLETE — 2026-08-22  
**Product behavior changed:** no.

### Source surface inspected

```text
src/upgradepilot/github/repository.py
src/upgradepilot/dependency/change.py
src/upgradepilot/dependency/uv_lock.py
src/upgradepilot/dependency/pyproject.py
src/upgradepilot/dependency/environment.py
src/upgradepilot/dependency/environment_selection.py
src/upgradepilot/dependency/environment_membership.py
src/upgradepilot/dependency/uv_membership.py
src/upgradepilot/ci/consumption.py
src/upgradepilot/ci/workflow_commands.py
src/upgradepilot/ci/dependency_exercise.py
src/upgradepilot/target/artifact_environment.py
src/upgradepilot/upstream/interval_evidence.py
```

Representative focused tests were also identified across provider, dependency, uv reachability, workflow/CI, Target, and upstream evidence.

### R0 taxonomy

R0 classified current checks by responsibility:

```text
A external trust-boundary validation
B semantic/domain validation
C relational/rebinding validation
D repeated internal-invariant validation
E impossible-state defense
```

**Important correction:** the taxonomy is an ownership map, not a retention list. R0 does not need to be rerun. Individual fields/checks still have to earn retention under `JUST-*`.

### Stable R0 findings

- external GitHub response handling needs one clear provider owner;
- semantic uv/project structure remains domain-owned;
- independently meaningful cross-object relations remain legitimate even after stronger types;
- duplicate internal checks are R1 candidates only after the owning contract changes;
- manually fabricable impossible states should move toward the construction boundary rather than being defended everywhere;
- `uv_lock.py` and `uv_membership.py` duplicate shared lock structure and differ on versionless-record admission;
- S001 `--all-packages` scope is currently lost;
- the smallest justified uv proposition is explicit selected-root reachability;
- S001 positive witness remains:

```text
docs
→ mkdocs-llmstxt
→ beautifulsoup4
→ soupsieve
```

- static dependency consumption != static direct exercise != exact-head runtime authority.

## R1 — investigation and design record

### Step 1 — one strong type versus parallel exact type

Ali initially reasoned that if UpgradePilot consumes `RepositoryTextFile` as successful repository text, the type should be strong from the start.

Production construction/consumer inspection supported that direction:

```text
successful production construction
→ effectively centralized in GitHubRepositoryClient

weak/manual construction
→ concentrated in tests/fixtures
```

Decision direction:

> Strengthen `RepositoryTextFile` itself. Do not create a second trusted/exact class hierarchy merely to preserve weak fixture construction.

### Step 2 — validation owner mental model

The learning distinction established during R0/R1 is:

```text
VALID EXTERNAL OBJECT?
→ acquisition / trust-boundary validation

VALID RELATION BETWEEN ALREADY-ADMITTED OBJECTS?
→ relational / rebinding validation

VALID DOMAIN MEANING?
→ semantic/domain validation
```

A stronger source type may eliminate repeated acquisition-invariant checks. It does not automatically eliminate a real relationship or domain rule.

### Step 3 — field-role exercise

Initial classification exercise:

```text
returned_path        → acquisition detail
reported/decoded size→ acquisition detail
retrieved_at         → initially considered durable provenance
blob_sha             → initially considered durable content identity
```

Ali correctly identified returned-path and duplicate byte-count propagation as validate-and-discard candidates.

The conversation then deliberately challenged the less obvious fields rather than accepting current usage as justification.

### Step 4 — blob SHA challenge and correction

Ali asked the key question:

> If UpgradePilot already has exact repository + immutable base/head commit SHA + exact path, what does blob SHA actually add to the product?

This exposed an earlier circular argument: current `uv_membership.py` compares the lock blob SHA, but that current comparison does not prove the field is necessary.

Technical clarification learned:

```text
commit SHA
→ identifies a repository revision/snapshot

blob SHA
→ identifies one Git content object
```

Different commits can share the same file blob, but that general Git capability still does not establish a current UpgradePilot need for blob identity.

Current admitted UpgradePilot propositions do not use blob identity for caching, deduplication, object lookup, independent integrity verification, or another distinct capability. Exact:

```text
repository + immutable revision + path
```

already locates the repository file used by the current evidence flow.

**R1 decision:** `blob_sha` does not earn durable exact-file retention from current evidence.

### Step 5 — retrieval-time challenge and correction

`retrieved_at` was initially considered useful because upstream evidence currently carries it. The new retention rule required a stronger question:

> Which current decision, staleness rule, or proof actually needs the wall-clock time at which an immutable commit-addressed repository file was fetched?

No such responsibility was found.

The project evidence doctrine requires source identity plus material time/revision context. For an exact immutable repository file, the revision is the material source-time/version context. Mutable API evidence can legitimately retain retrieval time separately; that does not justify forcing it onto every exact repository file.

**R1 decision:** `retrieved_at` does not earn retention on `RepositoryTextFile` or on downstream tagged-changelog evidence merely because other mutable upstream API records carry timestamps.

### Step 6 — provider size/blob metadata pressure

Current provider reads GitHub `sha` and `size`, validates reported-vs-decoded byte equality, then propagates those values.

Under the retention burden:

- the actual decoded byte length is enough to enforce the admitted text-size bound;
- GitHub-reported size is not used by a current product proposition;
- equality between two GitHub-supplied representations is not itself a required domain fact once the actual bytes are safely bounded;
- GitHub blob SHA is not required to parse/admit exact text and currently supports no separate product capability.

The provider should therefore retain only necessary external-response checks:

```text
admitted requested path
response type == regular file
returned path == requested path
supported encoding/content shape
strict base64 decode
actual decoded byte bound
UTF-8 decode
```

and should not require provider `sha`/`size` merely because the current implementation does.

## R1 frozen minimum contract

The design/necessity phase is now complete enough to freeze this target before code migration:

```text
RepositoryTextFile
├── repository
├── path
├── revision
└── content
```

Meaning:

- `repository` — admitted `owner/repository` source identity;
- `path` — admitted repository-relative POSIX file path;
- `revision` — exact immutable Git revision admitted by the provider path;
- `content` — bounded UTF-8 text returned after provider validation.

The type should enforce its **internal structural invariants without silent coercion**. Actual GitHub acquisition remains provider-owned; a dataclass is not a cryptographic provenance token.

Typed unavailability remains explicit and should use the same source locator:

```text
UnavailableRepositoryFile
├── repository
├── path
├── revision
├── reason
└── detail
```

### Fields scheduled to disappear from durable exact-file evidence

```text
returned_path
reported_byte_count
decoded_byte_count
blob_sha
retrieved_at
```

### Redundant aliases scheduled for removal

```text
ExactRepositoryTextFile
ExactRepositoryFileEvidence
```

unless implementation pressure reveals a real distinct responsibility. Current evidence does not.

## R1 downstream migration map

Primary product source affected:

```text
src/upgradepilot/github/repository.py
src/upgradepilot/dependency/change.py
src/upgradepilot/dependency/uv_lock.py
src/upgradepilot/dependency/pyproject.py
src/upgradepilot/dependency/uv_membership.py
src/upgradepilot/target/python.py
src/upgradepilot/target/artifact_environment.py
src/upgradepilot/upstream/interval_evidence.py
src/upgradepilot/upstream/interval.py
src/upgradepilot/upstream/changelog.py
src/upgradepilot/cli.py
```

Current propagation scheduled to disappear unless new independent evidence appears during implementation:

```text
DependencyChangeSourceEvidence
→ base_blob_sha / head_blob_sha
→ base_byte_count / head_byte_count

TargetPythonDeclaration / problem
→ blob_sha

TargetArtifactEnvironmentEvidence
→ workflow_blob_sha

TaggedChangelogEvidence
→ returned_path / blob_sha / reported_byte_count / decoded_byte_count / retrieved_at

CrossedReleaseSourceWindow
→ blob_sha

CLI
→ blob/byte presentation copied from dependency evidence
```

Current production-use pressure confirmed that:

- `workflow_blob_sha` is only copied into the Target evidence record and has no downstream product consumer;
- changelog blob identity is copied again into `CrossedReleaseSourceWindow` even though repository + resolved commit + path already identifies the exact source;
- dependency blob/byte values are primarily propagated/rendered plus used by one under-review uv rebinding path;
- these are migration obligations, not retention justifications.

### Independently justified relations to preserve through R1

```text
base/head repository belong to the same intended dependency comparison
base/head path matches the changed file
exact source revision matches the intended PR base/head or tag commit
uv lock path/revision matches the dependency context being combined
project-root relation remains until R4 decides the exact proposition input
CI workflow/job/step/segment joins remain where required by the retained CI proposition
upstream changelog repository/revision matches the resolved tag commit
```

The exact shape of later R2–R5 relations remains for those steps to decide.

## R1 implementation rule

Do not introduce a production compatibility shim merely so old tests can continue constructing weak evidence.

The migration must update production consumers and fixtures/tools together:

```text
strong contract first-class in production
+ tests construct valid strong fixtures
+ removed metadata assertions disappear or become boundary-specific tests
+ no legacy InitVar/property/alias retained solely for fixture convenience
```

Because the contract fans out across provider, dependency, Target, upstream, CLI, tools, experiments, and tests, implementation should be a coherent migration rather than leaving `main` conceptually half-old/half-new.

## Session progression log

### 2026-08-22 — governance/session setup

- Paused the dedicated learning-folder route.
- Selected normal learning-by-building mode.
- Created fresh reconciliation plan and progressive working memory.
- Deferred old Cluster 6 and the agentic evaluation.

### 2026-08-22 — R0 completed

- Inspected exact-file/dependency/uv/CI/Target/upstream responsibilities.
- Classified validation ownership.
- Confirmed duplicated uv structure and concrete parser drift.
- Froze explicit selected-root reachability proposition and S001 witness.
- No product source/tests changed.

### 2026-08-22 — retention discipline hardened

- Promoted “existing code is evidence, not authority” to `AGENTS.md`, `OPERATING_GUIDE.md`, accepted core `JUST-*` invariants, the active plan, and root `MEMORY.md`.
- Clarified R0 as inventory/ownership freeze rather than grandfathered retention.
- Preserved learning leadership: Ali predicts/reasons; AI leads/corrects from technical evidence.

### 2026-08-22 — R1 contract investigation completed

- Consumer scan selected one strong `RepositoryTextFile` direction.
- Separated identity, provenance, acquisition detail, and relational validation.
- Challenged current blob/time/byte/path-duplicate propagation against independent product needs.
- Rejected circular “current consumer uses it” retention arguments.
- Froze minimum exact-file contract as `repository + path + revision + content`.
- Mapped active source propagation that must migrate.
- No product source/tests changed yet; latest runtime proof therefore remains the previously accepted 508-test point.

## Exact next action

Enter the R1 implementation substep:

```text
1. strengthen RepositoryTextFile and UnavailableRepositoryFile invariants
2. simplify GitHub exact-file response admission to necessary fields/checks
3. migrate dependency exact-source provenance away from blob/byte metadata
4. migrate uv membership to retained repository/path/revision relations only
5. migrate Target and upstream evidence/window contracts
6. remove redundant exact aliases and CLI metadata rendering
7. migrate tests/tools/experiments instead of adding compatibility shims
8. run focused and nearest integration validation when execution is available
9. record exact revision/result before declaring R1 complete
```

Do not start R2 until the R1 source/test migration is materially complete and reviewed.