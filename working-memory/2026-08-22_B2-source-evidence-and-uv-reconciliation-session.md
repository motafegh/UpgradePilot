# Working Memory — B2 Source/Evidence and uv Reconciliation Session

**Date:** 2026-08-22  
**Status:** ACTIVE  
**Branch:** `main`  
**Mode:** learning by doing and building  
**Live-state owner:** `../MEMORY.md`

## Why this session exists

The project was in the middle of the dedicated learning route under:

```text
learning/2026-08-17-b2-dependency-environment-ci-consumption-mastery/
```

While learning the implemented B2 dependency-environment/CI path, Ali identified concrete design and implementation concerns: duplicated validation, potentially over-strong naming/propositions, repeated `uv.lock` structural interpretation, incomplete preservation of real uv workspace scope, and places where complexity may be compensating for weak internal contracts rather than product responsibility.

Those concerns were preserved in repository audits. A fresh review on 2026-08-22 validated that several findings are real enough to reconcile **before** ordinary Cluster-6 application integration or a new agentic product experiment.

This session therefore pauses the dedicated learning-folder progression and returns UpgradePilot to its normal project mode:

> **learning by doing and building**

Learning is not abandoned. Understanding, prediction, implementation, testing, and explanation happen inside each bounded engineering step under `OPERATING_GUIDE.md` and the source-clarity contract.

## Current session decision

Until this reconciliation closes:

1. the dedicated learning folder is paused;
2. the previously active B2 dependency-environment/CI continuation is deferred at the completed Cluster-5 boundary;
3. the bounded agentic-orchestration evaluation is deferred;
4. current engineering work is `../plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`;
5. after that plan closes, older deferred plans must be re-reviewed against the modified source/architecture before any becomes active again.

No previous accepted implementation evidence is erased merely because its architecture is being refined. In particular, the accepted S001 positive explicit-root witness and Cluster-0–5 validation history remain historical evidence unless later implementation/testing refutes them.

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

No product-source behavior has been modified yet in R1.

## Audit lifecycle

Lifecycle indexes:

- `../audits/active/README.md`
- `../audits/deferred/README.md`
- `../audits/absorbed/README.md`

Canonical audit files remain directly under `../audits/` so their existing relative references stay valid.

### Active

- `../audits/2026-08-01_AUDIT-001_exact-pr-file-acquisition-evidence-contract.md`
- `../audits/2026-08-21_AUDIT-006_internal-evidence-type-strength-and-revalidation-boundaries.md`
- `../audits/2026-08-22_AUDIT-007_uv-membership-proposition-and-lock-model-boundaries.md`

### Deferred

- `../audits/2026-08-16_AUDIT-004_uv-lock-resolution-satisfiability-evidence-boundary.md`
- `../audits/2026-08-21_AUDIT-005_product-ai-agentic-orchestration-sequencing.md`

### Absorbed

- `../audits/2026-08-02_AUDIT-002_ci-dependency-exercise-proof-boundary.md`
- `../audits/2026-08-10_AUDIT-003_post-conversation-c-product-decision-model.md`

## Stable project guards

The reconciliation must preserve:

```text
exact dependency transition
!= explicit-root reachability/environment evidence
!= static CI consumption
!= resolver/currentness
!= runtime execution/success
!= exact-version runtime witness
!= behavioral compatibility/safety/action
```

and:

```text
observation != interpretation != evidence quality != decision
```

Do not introduce generic trust wrappers, generic dependency graphs, universal package-manager abstractions, a complete uv environment interpreter, or target-repository execution merely to simplify code.

### Non-negotiable implementation-retention rule

This session must actively resist **legacy implementation bias**:

```text
existing code / field / check / consumer / test / comment / historical intent
→ evidence about what the system currently does and what migration may affect
!= evidence that the mechanism is necessary
```

Every material mechanism touched by this reconciliation must earn retention from a current independent reason:

- admitted product responsibility;
- proof/evidence requirement;
- material security/reliability risk control;
- real compatibility or external obligation.

Do not invent a rationale after seeing current code. Do not say “X should stay because Y uses it” when Y's dependence on X is also under review. Passing tests protect current behavior but do not prove the architecture/mechanism is necessary. If a simpler mechanism preserves all independently justified responsibilities and proof limits, prefer it.

This rule is now durable in root `AGENTS.md`, the accepted core invariant specification (`JUST-001` through `JUST-003`), the active plan, and root `MEMORY.md`.

### Learning leadership rule

Ali's predictions, answers, and design instincts are part of the learning loop, not acceptance authority. The AI must lead from actual technical/professional requirements, evidence, proof boundaries, and proportionality; it must correct Ali when needed and explain the correction rather than shaping architecture around a learner answer.

## R0 — contract/source freeze

**Status:** COMPLETE — 2026-08-22  
**R0 purpose:** inspect/classify/freeze only; no production source behavior change.

### Inspected primary source surface

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
```

Representative materially different exact-file consumers inspected for R1 pressure:

```text
src/upgradepilot/target/artifact_environment.py
src/upgradepilot/upstream/interval_evidence.py
```

### Baseline test/change surface frozen

Focused/nearest tests that must guide the reconciliation include:

```text
tests/test_github_repository.py
tests/test_uv_lock_change.py
tests/test_uv_lock_versionless_records.py
tests/test_project_environment_selection.py
tests/test_project_source_environment_membership.py
tests/test_uv_selected_environment_membership.py
tests/test_uv_membership_universal_lock_boundary.py
tests/test_workflow_dependency_evidence.py
tests/test_ci_dependency_coverage.py
tests/test_target_artifact_environment.py
tests/test_upstream_interval.py
```

Nearest broader integration surfaces remain `tests/test_dependency_analysis.py`, `tests/test_investigation.py`, and the existing end-to-end regression set when implementation reaches the appropriate gate.

### R0 validation taxonomy

R0's taxonomy remains useful as an **ownership map**, but the new retention rule changes how its “KEEP” language must be read. A category can be necessary while an individual current check inside that category is still unnecessary. R0 therefore does not need to be rerun, but no specific field/check receives grandfathered retention from the R0 inventory.

#### A — external trust-boundary validation: responsibility category stays

The GitHub acquisition boundary must validate the untrusted response enough to establish the exact admitted repository text file. Current checks include:

```text
repository-relative path admission
GitHub response type
requested path == returned path
provider blob identity presence
reported size type/bound
base64 structure/decoding
reported bytes == decoded bytes
actual decoded-size bound
UTF-8 decoding
```

Path/type/encoding/size/content checks have direct acquisition roles. **Provider blob identity is reopened in R1:** being returned by GitHub and currently validated does not itself prove UpgradePilot needs it. If no current acquisition/product/proof responsibility requires it, its strictness/propagation should be removed rather than justified after the fact.

#### B — semantic/domain validation: responsibility category stays

Examples:

```text
changed path really is uv.lock / pyproject.toml
supported uv.lock schema/revision
package-record/name/version/source admission
optional/dev dependency edge shapes
marker/repeated-record ambiguity
pyproject table/environment semantics
```

A stronger exact-file type does not replace required domain semantics. But each specific semantic rule still has to support the exact selected proposition; current parser behavior alone is not enough.

#### C — relational/rebinding validation: responsibility category stays

Current examples include:

```text
base/head evidence belongs to the changed-file path
base/head sources belong to the intended dependency comparison
lock evidence matches UvLockDependencyContext repository/revision/source evidence
static declaration project root matches the evidence being evaluated
CI external consumption matches normalized package
CI consumption matches workflow path/revision/job/step/segment/command
upstream changelog file belongs to the resolved repository/tag commit
```

Relational validation remains a real class of responsibility, but **each relation must remain independently necessary after its participating evidence contracts are simplified**. A relation is not retained just because a current consumer compares two values.

#### D — repeated internal-invariant validation: R1 candidates

The normal `GitHubRepositoryClient` establishes facts that are then repeatedly checked by dependency/target/upstream consumers because `RepositoryTextFile` permits weaker/manual construction. Confirmed examples include:

```text
returned_path == path
blob identity is populated
reported/decoded counts are populated/non-negative/equal
retrieval timestamp is populated where a consumer expects provider-produced evidence
content has already survived UTF-8 decoding
```

`uv_lock.py` and `pyproject.py` repeat nearly the same path/blob/byte defensive block. `uv_membership.py` repeats it again for project/lock evidence. `target/artifact_environment.py` and `upstream/interval_evidence.py` demonstrate that the issue is genuinely cross-responsibility rather than one dependency-file quirk.

These checks are **not authorized for deletion merely because they repeat**. R1 first decides which underlying facts belong in the retained contract at all; then it strengthens the owner and removes only downstream checks that no longer establish an independently necessary relation or semantic fact.

#### E — impossible-state defense: move toward construction boundary, preserve only real relations

The current type allows manually fabricated values such as:

```text
same claimed repository + revision + path
but different claimed blob/content identity
```

Normal correct immutable acquisition should not allow mutually inconsistent representations of one exact repository/revision/path. R1 should make provider-owned impossible states hard/unrepresentable at construction, while avoiding downstream defenses against states that only weak manual construction can create.

### Exact-file contract finding frozen for R1

Current architecture has a real mismatch:

```text
GitHubRepositoryClient
→ strongly validates exact file

but

RepositoryTextFile
→ repository/returned_path/counts/time can be absent
→ ExactRepositoryTextFile is only an alias
→ downstream cannot trust the nominal type alone
```

Several higher-level tests directly construct weak `RepositoryTextFile(path, revision, blob_sha, content)` objects. Test convenience is migration pressure, not production-contract authority.

### Duplicated uv.lock structural truth frozen for R2

Both `uv_lock.py` and `uv_membership.py` currently parse/validate overlapping external lock structure:

```text
TOML document
schema version
lock revision
package array
package names
package versions
package source identity
repeated package records
```

`uv_membership.py` additionally needs graph-specific structure:

```text
resolution markers
dependencies
optional dependencies
dev dependencies
edge version/source discriminators
edge markers
activated extras
```

The demonstrated drift is real:

```text
uv_lock.py
missing package version
→ allowed only for exact editable/virtual workspace-source shape

uv_membership.py
missing package version
→ currently allowed without the same source restriction
```

R2 therefore has a justified target: one **uv-specific structural lock parser/model** for genuinely shared format truth, with transition comparison and reachability remaining separate semantic consumers. R2 must still justify each shared structural fact from actual consumer propositions rather than copy the union of both existing parsers.

### uv selection scope gap frozen for R3

`ProjectEnvironmentSelectionDeclaration` currently preserves:

```text
manager
operation
segment_index
project_root
selectors
```

but no workspace/package scope.

The existing S001-shaped test uses:

```text
uv sync --all-packages --group docs --all-extras
```

and asserts only the group/extra selectors. `--all-packages` disappears from the typed declaration.

This is a material scope loss for no-witness reasoning. It does not invalidate one sound positive S001 path, but it can make `not_established` stronger than the set of workspace roots actually inspected.

### Exact uv proposition frozen for R2–R4

The smallest justified product proposition is now frozen as:

> Given a changed package established from an exact admitted `uv.lock`, a statically explicit positive uv group/extra selector with enough admitted project/workspace scope, and the exact admitted lock structure, determine whether **an in-scope explicitly selected root has a deterministic unconditional lock-backed path to the changed package**.

Result semantics:

```text
member
→ one sound in-scope explicit selected root/path is sufficient

not_established
→ all roots in the proposition's represented scope were exhausted with no witness and no material ambiguity

unresolved
→ scope, marker/fork/edge identity, source structure, or traversal safety prevents that conclusion
```

This proposition intentionally does **not** establish complete uv environment formation, default-group semantics, lock currentness, resolver success, command execution, sync/install success, or runtime behavior.

Current S001 positive witness remains the regression anchor:

```text
docs
→ mkdocs-llmstxt
→ beautifulsoup4
→ soupsieve
```

### `pyproject.toml` status after R0

R0 does **not** decide to remove project evidence.

Current uv membership uses project content for:

```text
[project].name
→ bind one workspace package by name + source path

group/extra names
→ cross-check explicit selector namespace

project file path
→ bind declaration project_root
```

These are current uses, not retention proof. R4 must decide which facts the frozen explicit-root proposition genuinely requires after R1/R2/R3 provide stronger identity/structure/scope.

### Cluster-5 CI contract frozen

The reconciliation must preserve the current proof split:

```text
STATIC DEPENDENCY CONSUMPTION
!= STATIC DIRECT EXERCISE
!= EXACT-HEAD RUNTIME AUTHORITY
```

and the strongest accepted result remains:

```text
successful exact-head CI
+ supported static dependency consumption
→ supported_not_correlated
```

The current workflow/package/job/step/segment checks are pressure evidence. R5 must retain only the joins required to establish the retained CI proposition.

### R0 gate disposition

R0 gate remains satisfied:

- exact change surface identified;
- baseline test surface identified;
- validation ownership categories classified;
- duplicated uv structure identified with a concrete divergence;
- exact uv proposition frozen;
- accepted S001 witness preserved;
- no product-source behavior changed.

No R0 re-execution is required. The only correction is interpretive: **inventory/classification does not grant retention**. R1+ applies the explicit retention burden to each concrete mechanism.

The latest product-runtime validation point is still:

```text
bfdfd4257574f85cc3a2d094bf46a37ad6373dea
508 tests / OK
```

Governance/plan/working-memory edits do not create a newer product-runtime validation point.

## R1 — exact repository-file evidence ownership

**Status:** IN PROGRESS — 2026-08-22  
**Current activity:** consumer- and proposition-driven contract design before the first production source edit.

### Successful-construction/consumer scan

The current scan supports strengthening the existing `RepositoryTextFile` rather than introducing a parallel trusted/exact class hierarchy:

```text
production successful RepositoryTextFile construction
→ effectively centralized in GitHubRepositoryClient

weak/manual RepositoryTextFile construction
→ concentrated in tests/fixtures
```

This makes test convenience a migration concern, not a reason to keep the production contract weak.

Current working direction:

> `RepositoryTextFile` itself should represent one successfully acquired, strongly admitted repository text file.

A separate strong `ExactRepositoryTextFile` type is not currently justified merely to preserve weak test construction. The historical `ExactRepositoryTextFile = RepositoryTextFile` alias must be reassessed after the concrete contract is frozen.

### Field-role learning/design result

The R1 investigation distinguishes three concepts:

```text
IDENTITY
→ what exact repository source is this?

PROVENANCE
→ where/when did this evidence come from?

ACQUISITION / VALIDATION DETAIL
→ what temporary external-response facts were checked to admit it?
```

Current field status is intentionally **not** a keep-list:

```text
strongly justified candidates so far
→ repository
→ path
→ exact immutable revision
→ content

acquisition/validation detail; leading validate-and-discard candidates
→ returned_path
→ reported_byte_count
→ decoded_byte_count

plausible durable provenance; still place at narrowest justified layer
→ retrieved_at

reopened / not yet justified as durable contract fact
→ blob_sha
```

Reasoning so far:

- `returned_path` is valuable while proving GitHub returned exactly the requested path. After equality succeeds, carrying both path spellings gives downstream code two fields for one established fact.
- reported/decoded byte counts are valuable at the GitHub trust boundary for size and contradiction checks. Their duplicated propagation is not currently tied to a dependency/CI proposition; decoded size is derivable from admitted UTF-8 content if a later count is genuinely needed.
- `retrieved_at` is not file identity. It has a plausible independent provenance reason because UpgradePilot's evidence doctrine preserves time/revision context and upstream changelog evidence records when evidence was acquired. R1 still must decide whether retrieval time belongs on every `RepositoryTextFile` or a narrower evidence layer.
- `blob_sha` is provider-native Git content-object identity, but current use/propagation is **not sufficient justification**. Exact `repository + immutable revision + path` already identifies the file location in the repository snapshot. R1 must identify a real current product/proof need that requires blob identity beyond that tuple. If none exists, current blob fields/rebinding/tests should migrate away rather than being used to justify themselves.

Ali correctly challenged the earlier circular argument “keep blob SHA because `uv_membership.py` currently compares it.” The engineering correction is now explicit: current consumption tells us what migration is affected; it does not tell us the dependency is necessary.

No field has been removed from production yet. The minimum contract is not frozen until the remaining provenance/identity questions are pressured against actual responsibilities.

## Session progression log

### 2026-08-22 — Governance/session setup

- Paused the dedicated learning-folder route and selected normal learning-by-building mode.
- Created this progressive working memory and the fresh reconciliation plan.
- Organized audit lifecycle indexes.
- Deferred old Cluster 6 and the agentic evaluation until R7 re-review.
- No product source/tests changed.

### 2026-08-22 — R0 completed

- Inspected the exact-file, dependency, uv-selection/reachability, CI composition, target, upstream, and representative test boundaries.
- Confirmed AUDIT-006's type-strength issue is real and cross-responsibility.
- Confirmed AUDIT-007's parser duplication, scope loss, and over-broad membership naming/proposition pressure.
- Classified validation ownership categories, duplicated uv structure, and the explicit selected-root proposition.
- Preserved S001 as a positive regression anchor.
- No product source/tests changed.

### 2026-08-22 — R1 consumer/field investigation started

- Consumer scan favored strengthening `RepositoryTextFile` itself over introducing a second strong exact-file type merely for fixture compatibility.
- Separated durable identity, durable provenance, and acquisition-only validation detail.
- `returned_path` and duplicate byte-count propagation lean toward validate-and-discard.
- `retrieved_at` has a plausible independent provenance role but still needs narrow placement review.
- No product source/tests changed yet.

### 2026-08-22 — implementation-retention discipline hardened

- Ali explicitly rejected implementation-preserving reasoning that invents purposes for existing code.
- Promoted the rule to root `AGENTS.md` and the accepted core invariant specification as `JUST-001`/`JUST-002`/`JUST-003`.
- Bound the same rule into the active reconciliation plan and root `MEMORY.md`.
- Clarified R0 without reopening it: ownership categories remain valid, but individual mechanisms do not receive grandfathered retention.
- Reopened `blob_sha` necessity instead of treating its current provider validation/consumer use as proof that it belongs in the durable exact-file contract.
- Preserved the learning-role boundary: Ali reasons/predicts; AI leads and corrects from technical evidence and professional necessity.
- No product source/tests changed.

## Exact next action

Continue R1 contract freeze before implementation:

```text
1. pressure blob_sha against exact current product/proof responsibilities
   - ask what fact it adds beyond repository + immutable revision + path
   - do not use current consumer dependence as justification

2. pressure retrieved_at placement
   - confirm the evidence-doctrine requirement
   - decide whether it belongs on RepositoryTextFile or a narrower acquisition/provenance record

3. freeze the minimum strong RepositoryTextFile fields/invariants

4. map aliases, downstream checks, propagated source-evidence fields, and tests that must migrate

5. make the first bounded production source change only after the contract is justified
```

Do not remove or retain a downstream check merely because of its current form. First identify whether the fact/relation it protects remains independently necessary under the new contract.