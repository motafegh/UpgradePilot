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

Final product-source content at this checkpoint is unchanged from the pre-R1 implementation. Two exploratory staging edits were deliberately restored after they demonstrated that the contract migration must be coherent across provider, consumers, fixtures, and validation.

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

### 1. One strong type versus parallel exact type

Ali reasoned that if UpgradePilot consumes `RepositoryTextFile` as successful repository text, the type should be strong from the start.

Production construction/consumer inspection supported that direction:

```text
successful production construction
→ effectively centralized in GitHubRepositoryClient

weak/manual construction
→ concentrated in tests/fixtures
```

Decision:

> Strengthen `RepositoryTextFile` itself. Do not create a second trusted/exact class hierarchy merely to preserve weak fixture construction.

### 2. Validation-owner mental model

```text
VALID EXTERNAL OBJECT?
→ acquisition / trust-boundary validation

VALID RELATION BETWEEN ALREADY-ADMITTED OBJECTS?
→ relational / rebinding validation

VALID DOMAIN MEANING?
→ semantic/domain validation
```

A stronger source type may eliminate repeated acquisition-invariant checks. It does not automatically eliminate a real relationship or domain rule.

### 3. Field-role investigation

Initial exercise separated:

```text
identity
provenance
acquisition-only validation detail
```

Ali correctly identified `returned_path` and duplicate byte-count propagation as validate-and-discard candidates.

The less obvious fields were then challenged against independent product responsibilities rather than accepted from current usage.

### 4. Blob SHA challenge

Ali asked:

> If UpgradePilot already has exact repository + immutable base/head commit SHA + exact path, what does blob SHA actually add to the product?

Technical clarification:

```text
commit SHA
→ identifies a repository revision/snapshot

blob SHA
→ identifies one Git content object
```

Different commits can share a file blob, but that general Git capability does not establish a current UpgradePilot need for blob identity.

No admitted current proposition uses repository-file blob identity for caching, deduplication, object lookup, independent integrity verification, or another separate capability. Exact:

```text
repository + immutable revision + path
```

already locates the repository file used by the current evidence flow.

Current `uv_membership.py` comparison or other blob copies are migration pressure, not independent retention proof.

**R1 decision:** `blob_sha` does not earn durable exact-file retention from current evidence.

### 5. Retrieval-time challenge

`retrieved_at` was initially considered useful because upstream evidence currently carries it. The retention rule required the stronger question:

> Which current decision, staleness rule, or proof needs the wall-clock time at which an immutable commit-addressed repository file was fetched?

No such responsibility was found.

The project evidence doctrine requires material time/revision context. For an exact immutable repository file, the revision is the relevant source/version context. Mutable API evidence may still legitimately retain retrieval time separately.

**R1 decision:** `retrieved_at` does not earn retention on `RepositoryTextFile` or on commit-addressed tagged-changelog evidence merely for symmetry with mutable API evidence.

### 6. Provider size/blob metadata pressure

Current provider reads GitHub `sha` and `size`, validates reported-vs-decoded byte equality, and propagates those values.

Under the retention burden:

- actual decoded byte length is sufficient to enforce the admitted text-size bound;
- GitHub-reported size is not used by a current product proposition;
- equality between two GitHub-supplied representations is not itself a required domain fact once actual bytes are safely bounded;
- GitHub blob SHA is not required to parse/admit exact text and supports no separate current product capability.

The intended provider boundary therefore retains only necessary response checks:

```text
admitted requested path
response type == regular file
returned path == requested path
supported encoding/content shape
strict base64 decode
actual decoded byte bound
UTF-8 decode
```

and does not require provider `sha`/reported `size` merely because the current implementation does.

## R1 frozen minimum contract

```text
RepositoryTextFile
├── repository
├── path
├── revision
└── content
```

Meaning:

- `repository` — admitted `owner/repository` identity;
- `path` — admitted repository-relative POSIX file path;
- `revision` — exact immutable Git revision admitted by the provider path;
- `content` — bounded UTF-8 text after provider validation.

The type should enforce its **internal structural invariants without silent coercion**. Actual GitHub acquisition remains provider-owned; a dataclass is not a cryptographic provenance token.

Typed unavailability remains explicit:

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

Current metadata propagation scheduled to disappear unless new independent evidence appears:

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

Current pressure confirmed:

- `workflow_blob_sha` is only copied into the Target evidence record and has no downstream product consumer;
- changelog blob identity is copied again into `CrossedReleaseSourceWindow` even though repository + resolved commit + path already identifies the exact source;
- dependency blob/byte values are primarily propagated/rendered plus used by one under-review uv rebinding path;
- these are migration obligations, not retention justifications.

### Independently justified relations to preserve through R1

```text
base/head repository belong to the same intended dependency comparison
base/head path matches the changed file
exact source revision matches intended PR base/head or tag commit
uv lock path/revision matches the dependency context being combined
project-root relation remains until R4 decides exact proposition input
CI workflow/job/step/segment joins remain where required by retained CI proposition
upstream changelog repository/revision matches resolved tag commit
```

## R1 implementation rule

Do not introduce a production compatibility shim merely so old tests can continue constructing weak evidence.

The migration must update production consumers and fixtures/tools together:

```text
strong contract first-class in production
+ tests construct valid strong fixtures
+ removed metadata assertions disappear or become boundary-specific tests
+ no legacy InitVar/property/alias retained solely for fixture convenience
```

Because the contract fans out across provider, dependency, Target, upstream, CLI, tools, experiments, and tests, implementation must be a coherent migration rather than leaving `main` conceptually half-old/half-new.

## Executable staging attempt and rollback

### What was tried

After freezing the contract, two direct source edits were staged on `main`:

1. `de2ce0bcdea25e607ece4dbf252660e163d1f512` — strengthened `RepositoryTextFile` and simplified the GitHub provider;
2. `1a5ca5a0c4629566ce600f15e63aa8cc1318ac86` — narrowed `DependencyChangeSourceEvidence`.

Those edits were intentionally **not** treated as accepted implementation evidence.

### What the staging attempt revealed

The contract change touches too many active consumers and fixtures to be safely landed as sequential direct-to-main source commits while this assistant environment has no runnable repository checkout/test runner. The local container also cannot clone GitHub because outbound DNS/network access is unavailable.

Leaving the tree half-migrated would violate the same professional/retention discipline this reconciliation is enforcing.

### Rollback

Both product files were restored byte-for-byte to their pre-R1 content:

```text
5d40efd867222fd0c3e087bbeba965637c0059fd
→ restored src/upgradepilot/github/repository.py
→ content blob returned to 68d88e9fb9d19c1850f3df8eb14eb4130af674bb

7ed62d2a577299e0a846c0a358dbe5054e5b6610
→ restored src/upgradepilot/dependency/change.py
→ content blob returned to b87b72d708eea57db93bdd8199b5fddae8cf7a31
```

Therefore the final product-source content at this checkpoint remains the previously validated implementation. The staging/restore commits are process history only, not a newer product-runtime validation point.

### Implementation-method conclusion

R1 executable work must next be prepared/landed as a **coherent provider + consumer + tests/tools/experiments migration**, followed by runnable focused validation. Do not reintroduce compatibility fields just to make piecemeal migration convenient.

## Session progression log

### 2026-08-22 — governance/session setup

- Paused dedicated learning-folder route.
- Selected normal learning-by-building mode.
- Created reconciliation plan and progressive working memory.
- Deferred old Cluster 6 and agentic evaluation.

### 2026-08-22 — R0 completed

- Inspected exact-file/dependency/uv/CI/Target/upstream responsibilities.
- Classified validation ownership.
- Confirmed duplicated uv structure and concrete parser drift.
- Froze explicit selected-root reachability proposition and S001 witness.
- No product source/tests changed.

### 2026-08-22 — retention discipline hardened

- Promoted “existing code is evidence, not authority” to `AGENTS.md`, `OPERATING_GUIDE.md`, accepted core `JUST-*` invariants, active plan, and root `MEMORY.md`.
- Clarified R0 as inventory/ownership freeze rather than grandfathered retention.
- Preserved learning leadership: Ali predicts/reasons; AI leads/corrects from technical evidence.

### 2026-08-22 — R1 contract investigation completed

- Consumer scan selected one strong `RepositoryTextFile` direction.
- Separated identity, provenance, acquisition detail, and relational validation.
- Challenged current blob/time/byte/path-duplicate propagation against independent product needs.
- Rejected circular “current consumer uses it” retention arguments.
- Froze minimum exact-file contract as `repository + path + revision + content`.
- Mapped active source propagation that must migrate.

### 2026-08-22 — first executable staging rolled back cleanly

- Tried the provider/type and dependency-provenance edits to pressure the frozen design.
- Confirmed the change is cross-cutting enough that piecemeal direct-to-main landing would create a knowingly inconsistent intermediate tree.
- Restored both source files to their original content blobs.
- No new product-runtime validation claim was created.

## Exact next action

Prepare and apply the coherent R1 implementation set:

```text
1. RepositoryTextFile / UnavailableRepositoryFile strong locator invariants
2. necessary-only GitHub file response checks + actual decoded-byte bound
3. dependency source provenance without blob/byte metadata
4. uv membership using retained repository/path/revision relations only
5. Target and upstream evidence/window contract migration
6. redundant exact-alias and CLI metadata cleanup
7. tests/tools/experiments migrated to the strong contract rather than production shims
8. focused provider + dependency + Target + upstream validation
9. nearest integration/full deterministic validation
10. exact revision/result recorded before R1 is marked complete
```

Do not start R2 until that R1 migration is materially complete and validated.