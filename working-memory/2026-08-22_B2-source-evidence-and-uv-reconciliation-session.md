# Working Memory — B2 Source/Evidence and uv Reconciliation Session

**Date:** 2026-08-22  
**Status:** ACTIVE  
**Execution branch:** `agent/r1-exact-file-contract-migration`  
**Base branch:** `main`  
**Mode:** learning by doing and building  
**Live-state owner:** `../MEMORY.md`

## Session purpose

Learning/review of the B2 dependency-environment/CI implementation exposed concrete design pressure before ordinary Cluster-6 integration:

- exact repository-file provider guarantees are stronger than the nominal internal evidence type;
- downstream modules revalidate provider-owned facts because the type permits weak/manual states;
- `uv_lock.py` and `uv_membership.py` duplicate material `uv.lock` structure and have already drifted;
- the static uv declaration loses S001 `--all-packages` workspace scope;
- current membership terminology can imply more than explicit selected-root reachability proves.

The dedicated learning-folder route is paused. Current work follows normal learning-by-building under `../OPERATING_GUIDE.md` and `../plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`.

## Learning/execution discipline for this session

Ali explicitly requested that implementation remain a learning exercise rather than a bulk AI refactor. The active rhythm is therefore:

```text
one bounded engineering responsibility
→ explain the minimum concept/code needed now
→ Ali predicts/questions/reasons where useful
→ make the bounded source/test change
→ inspect the resulting diff/evidence
→ record what changed and what remains unproven
→ validate before advancing
```

Do not jump across R1 sub-responsibilities merely because the full migration is already mapped.

Ali's reasoning is learning input, not engineering authority. Technical/product/proof requirements decide the implementation; incorrect learner reasoning should be corrected explicitly and constructively.

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

Do not start R2 until R1 is materially complete and validated.

## Non-negotiable retention discipline

> **Existing implementation is evidence to inspect, not authority to preserve.**

Current code, consumers, passing tests, comments, historical design, and prior effort show current behavior and migration pressure. They do not establish that a mechanism is necessary.

Every material mechanism under review must trace to an independent current reason:

```text
admitted product responsibility
or proof/evidence need
or material risk control
or real compatibility/external obligation
```

Do not use circular reasoning such as `X must stay because Y uses X` when Y's dependence on X is itself being reviewed.

This rule is durable in:

- root `../AGENTS.md`;
- `../OPERATING_GUIDE.md`;
- `../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md` as `JUST-001`–`JUST-003`;
- the active reconciliation plan;
- root `../MEMORY.md`.

## R0 — completed ownership/inventory freeze

**Status:** COMPLETE — 2026-08-22  
**Product behavior changed:** no.

R0 classified current checks by responsibility:

```text
A external trust-boundary validation
B semantic/domain validation
C relational/rebinding validation
D repeated internal-invariant validation
E impossible-state defense
```

Important correction: this taxonomy is an ownership map, not a retention list. R0 does not need to be rerun. Each current field/check still has to earn retention under `JUST-*`.

Stable R0 findings:

- external GitHub response handling needs one clear provider owner;
- semantic uv/project structure remains domain-owned;
- independently meaningful cross-object relations remain legitimate even after stronger types;
- duplicate internal checks are R1 candidates only after the owning contract changes;
- manually fabricable impossible states should move toward the construction boundary rather than being defended everywhere;
- `uv_lock.py` and `uv_membership.py` duplicate shared lock structure and differ on versionless-record admission;
- S001 `--all-packages` scope is currently lost;
- the smallest justified uv proposition is explicit selected-root reachability;
- S001 positive witness remains `docs → mkdocs-llmstxt → beautifulsoup4 → soupsieve`;
- static dependency consumption != static direct exercise != exact-head runtime authority.

## R1 design conclusions frozen before implementation

### One strong successful type

Production construction/consumer inspection showed successful production construction is effectively centralized in `GitHubRepositoryClient`; weak/manual construction is concentrated in tests/fixtures.

Decision:

> Strengthen `RepositoryTextFile` itself. Do not introduce a parallel trusted/exact class hierarchy merely to preserve weak fixture construction.

### Validation-owner mental model

```text
VALID EXTERNAL OBJECT?
→ acquisition / trust-boundary validation

VALID RELATION BETWEEN ALREADY-ADMITTED OBJECTS?
→ relational / rebinding validation

VALID DOMAIN MEANING?
→ semantic/domain validation
```

A stronger source type may eliminate repeated acquisition-invariant checks. It does not eliminate real relational or semantic rules.

### Minimum durable exact-file contract

```text
RepositoryTextFile
├── repository
├── path
├── revision
└── content
```

Meaning:

- `repository` — admitted `owner/repository` identity;
- `path` — normalized repository-relative POSIX file path;
- `revision` — canonical exact immutable Git commit/object identity admitted by this provider path;
- `content` — bounded UTF-8 text.

Typed unavailability retains the exact locator plus problem information:

```text
UnavailableRepositoryFile
├── repository
├── path
├── revision
├── reason
└── detail
```

### Fields that did not earn durable exact-file retention

```text
returned_path
reported_byte_count
decoded_byte_count
blob_sha
retrieved_at
```

Reasoning:

- `returned_path` is required to verify the external response matches the requested path, then duplicates the admitted `path` fact.
- decoded/provider byte counts are acquisition mechanics; actual bytes can be bounded without propagating counts.
- `blob_sha` is legitimate Git metadata, but no admitted current UpgradePilot proposition needs separate Git blob identity beyond `repository + immutable revision + path`.
- `retrieved_at` supports no current staleness/decision/proof rule for an immutable commit-addressed file; immutable revision is the relevant source/version context.

Current use or propagation of these fields is migration pressure, not retention proof.

### Redundant aliases scheduled for removal

```text
ExactRepositoryTextFile
ExactRepositoryFileEvidence
```

No distinct responsibility was found for them.

### Independently justified relations that R1 must preserve

```text
base/head repository belong to the same intended dependency comparison
base/head path matches the changed file
source revision matches intended PR base/head or resolved tag commit
uv lock repository/path/revision matches the dependency context being combined
project-root relation remains until R4 decides the exact proposition input
CI workflow/job/step/segment joins remain where required by the retained CI proposition
upstream changelog repository/revision matches the resolved tag commit
```

## R1 migration surface

Primary source pressure:

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

Metadata propagation scheduled to disappear unless later independent evidence proves otherwise:

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
→ dependency blob/byte presentation
```

## Earlier direct-to-main staging attempt and rollback

Two exploratory direct-to-main source edits were made only to pressure the frozen design:

```text
de2ce0bcdea25e607ece4dbf252660e163d1f512
→ staged stronger RepositoryTextFile/provider

1a5ca5a0c4629566ce600f15e63aa8cc1318ac86
→ staged narrowed DependencyChangeSourceEvidence
```

They revealed that the contract fans out too broadly to leave `main` half-migrated without runnable validation. Both files were restored byte-for-byte:

```text
5d40efd867222fd0c3e087bbeba965637c0059fd
→ repository.py restored to blob 68d88e9fb9d19c1850f3df8eb14eb4130af674bb

7ed62d2a577299e0a846c0a358dbe5054e5b6610
→ dependency/change.py restored to blob b87b72d708eea57db93bdd8199b5fddae8cf7a31
```

No product-runtime validation claim was created by those staging/restore commits.

## R1 coherent migration branch

### Branch decision

A temporary branch is justified here by a concrete execution risk rather than generic branch ceremony:

```text
cross-cutting evidence contract migration
+ many active consumers/fixtures
+ no repository GitHub Actions workflow
+ GitHub connector can write but cannot run the user's WSL test suite
→ intermediate migration states should not break main
```

Created:

```text
agent/r1-exact-file-contract-migration
```

from current `main` at merge base:

```text
aa3e3bcb15c0f672fb4aeb4faf6155d58d1b8150
```

Do not add GitHub Actions merely to validate this change; the repository already has a real local WSL validation environment and CI would be a separate capability requiring its own justification.

## R1 Step 1 — repository text construction/acquisition boundary

**Status:** IMPLEMENTED ON MIGRATION BRANCH; LOCAL VALIDATION PENDING.

### Learning concept: construction invariant vs provider truth

A type annotation alone does not make an object valid. A **construction invariant** is a fact every successfully created instance must satisfy.

For `RepositoryTextFile`:

```text
constructor/type responsibility
→ internal structural validity

GitHubRepositoryClient responsibility
→ external GitHub response/acquisition truth
```

Therefore the dataclass can reject malformed repository/path/revision/content states, but it does not claim that a manually created object was cryptographically proven to originate from GitHub.

### Source change

Commit:

```text
709aba4cdab1fd666579f90cbe6a5e974cad8626
```

`src/upgradepilot/github/repository.py` now makes successful evidence structurally require only:

```text
repository
path
revision
content
```

and makes unavailable evidence require:

```text
repository
path
revision
reason
detail
```

`RepositoryTextFile.__post_init__` enforces:

- canonical admitted repository form;
- normalized repository-relative POSIX path;
- canonical lowercase 40/64-hex immutable Git revision;
- `str` content that is UTF-8 representable;
- the same 1,000,000-byte content ceiling.

The old `ExactRepositoryTextFile` and `ExactRepositoryFileEvidence` aliases were removed from this owner because they expressed no distinct contract.

### Provider response rule after Step 1

The provider still checks the facts needed to admit external GitHub text:

```text
requested path is structurally admitted
response type == regular file
returned path == requested path
encoding == base64
content field is text
strict base64 decoding
actual decoded byte bound
UTF-8 decoding
```

It no longer requires or propagates GitHub `sha` or reported `size` merely because those fields were previously present.

### Important safety refinement

Removing provider-reported `size` must not remove the resource bound.

The implementation therefore bounds the compact base64 representation before decode and separately bounds the actual decoded bytes afterward. The safety responsibility is retained while the unnecessary provider-size metadata contract is removed.

### Nearest tests migrated

Commits:

```text
e88b1e21e3b1efd09c226b5ca1512230f6477057
→ tests/test_github_repository.py

74fd3aaede37b15cb2eedbfda41128bc4d81f46c
→ tests/test_exact_commit_repository_files.py
```

The nearest tests now exercise the new proposition rather than old metadata propagation:

- exact repository/path/revision/content result;
- uppercase external commit input normalized before construction;
- movable/malformed revisions rejected before network;
- shared path admission preserved;
- unavailable evidence preserves exact locator;
- returned-path mismatch rejected at acquisition boundary;
- malformed base64 rejected;
- oversized content rejected without relying on provider `size`;
- manually constructed successful evidence rejects noncanonical locator states.

The old test asserting reported-vs-decoded provider byte-count equality was removed because that exact provider metadata relationship is no longer an admitted product or safety requirement.

### Branch diff after Step 1

Compared with `main`:

```text
3 commits ahead
0 behind
3 files changed

src/upgradepilot/github/repository.py
tests/test_exact_commit_repository_files.py
tests/test_github_repository.py
```

No dependency/Target/upstream consumer migration has happened yet.

### Step 1 proof state

**Not yet proven by execution.** The GitHub connector cannot execute the user's local WSL test suite, and this repository has no `.github/workflows` CI.

Required focused local validation before Step 2:

```bash
git fetch origin
git switch agent/r1-exact-file-contract-migration
git pull --ff-only origin agent/r1-exact-file-contract-migration
python -m unittest tests.test_github_repository tests.test_exact_commit_repository_files -v
```

What a green focused run would prove:

- the new exact-file provider/type boundary imports and executes under the project environment;
- its nearest acquisition and construction-invariant tests pass.

What it would **not** prove:

- downstream dependency/uv/Target/upstream consumers are already migrated;
- the full suite is green;
- R1 is complete;
- R2 may start.

## Progressive session log

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

- Promoted “existing code is evidence, not authority” to repository governance, operating method, accepted core invariants, active plan, and root memory.
- Clarified R0 as an inventory/ownership freeze rather than grandfathered retention.

### 2026-08-22 — R1 contract investigation completed

- Selected one strong `RepositoryTextFile` direction.
- Separated identity, acquisition detail, and relational validation.
- Challenged blob/time/byte/path-duplicate propagation against independent product needs.
- Froze `repository + path + revision + content` as minimum durable successful-file evidence.
- Mapped the active consumer/test migration surface.

### 2026-08-22 — direct-to-main staging rolled back

- Used two bounded staging edits to pressure the contract.
- Confirmed piecemeal main migration would create a knowingly inconsistent intermediate tree.
- Restored product source exactly; no validation claim created.

### 2026-08-22 — R1 migration branch / Step 1

- Created `agent/r1-exact-file-contract-migration` from current `main`.
- Implemented the new provider/type construction boundary.
- Preserved actual response/path/base64/UTF-8/resource-bound responsibilities while dropping unearned durable metadata.
- Migrated the two nearest provider tests.
- Diff pressure remains intentionally limited to three files.
- Focused local validation is the next gate.

## Exact next action

Do **not** start dependency/uv consumer migration until Step 1 focused validation is observed.

Next gate:

```text
run focused provider/type tests in WSL
→ if green: record exact result and enter R1 Step 2 (dependency source provenance)
→ if failing: diagnose the smallest revealed model/code gap and repair Step 1 first
```

Latest accepted full product-runtime validation remains the historical `508 tests / OK` point at `bfdfd4257574f85cc3a2d094bf46a37ad6373dea`; nothing on this migration branch supersedes it yet.
