# UpgradePilot Current Memory

**Last updated:** 2026-08-22  
**Authority:** Sole repository owner of live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Non-negotiable implementation-retention rule

**Existing code is evidence to inspect, not authority to preserve.** Current use, passing tests, comments, historical intent, prior effort, or another under-review consumer does not by itself justify keeping a field, check, type, helper, abstraction, metadata value, alias, dependency, or compatibility surface.

For every material mechanism under review:

```text
What current admitted responsibility / proof need / material risk / real compatibility obligation requires it?
→ if independently justified: keep the smallest adequate mechanism
→ if not independently justified: remove or narrow it
```

Do not invent reasons for legacy/current implementation. Do not use circular retention arguments such as “field X must stay because consumer Y uses it” when Y's dependence on X is itself under review. Passing tests protect behavior; they do not prove that the mechanism producing that behavior is architecturally necessary.

This rule is durable in `AGENTS.md`, `OPERATING_GUIDE.md`, and `docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md` (`JUST-001` through `JUST-003`) and is bound explicitly into the active reconciliation plan.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice. X1 remains available only through its evidence-gated admission rule.
- **Current mode:** normal **learning by doing and building** under `OPERATING_GUIDE.md`; the dedicated learning-folder route is paused, not abandoned as project learning.
- **Current implementation responsibility:** [`plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`](plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md).
- **Current plan position:** **R0 COMPLETE; R1 IN PROGRESS — exact-file contract FROZEN, coherent source/test migration NEXT**.
- **Current progressive working record:** [`working-memory/2026-08-22_B2-source-evidence-and-uv-reconciliation-session.md`](working-memory/2026-08-22_B2-source-evidence-and-uv-reconciliation-session.md).
- **Current active audit inputs:** AUDIT-001, AUDIT-006, AUDIT-007, classified in [`audits/active/README.md`](audits/active/README.md); canonical audit files remain directly under `audits/`.
- **Dedicated learning package:** [`learning/2026-08-17-b2-dependency-environment-ci-consumption-mastery/`](learning/2026-08-17-b2-dependency-environment-ci-consumption-mastery/) is **PAUSED at its recorded Plan-02/Chunk-1 state**.
- **Previous dependency-environment/CI plan:** [`plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md`](plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md) is **DEFERRED at the completed Cluster-5 boundary**. Cluster 6 must not start while the reconciliation plan is active.
- **Agentic evaluation:** [`plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md`](plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md) is **DEFERRED** until the reconciliation closes and older continuations are re-reviewed.
- **Current product status:** previously accepted Clusters 0–5 remain historical green evidence; Cluster 6 is not started.
- **Latest product-runtime validation point:** `bfdfd4257574f85cc3a2d094bf46a37ad6373dea` — `508 tests / OK`, `HEAD == origin/main`, clean worktree at that validation point.
- Governance/plan/working-memory commits after that point do not create a newer product-runtime validation point.
- **Tranche 2 static↔runtime correlation:** NOT SELECTED / NOT AUTHORIZED.

## Why the live continuation changed

Learning/review of the B2 implementation exposed concrete design pressure before wider integration:

```text
strong provider acquisition checks
+ weak/permissive RepositoryTextFile contract
→ repeated downstream invariant revalidation

one external uv.lock format
→ duplicated structural parsers
→ demonstrated admission-rule drift

real uv command scope
→ --all-packages dropped from current declaration
→ negative-ish not_established can be stronger than modeled scope

current uv membership name
→ can sound like complete environment membership
while implementation principally proves
→ explicit selected-root reachability
```

The current reconciliation therefore seeks the **smallest sound architecture**, not maximal modeling and not minimum line count.

## Stable proof ladder

```text
dependency transition
!= explicit-root/environment membership evidence
!= static environment selection
!= static dependency consumption
!= resolver satisfiability/currentness
!= runtime execution/success
!= exact-version witness
!= direct package exercise
!= behavioral compatibility/safety/action
```

and:

```text
observation != interpretation != evidence quality != decision
```

remain controlling proof boundaries.

## R0 disposition

R0 completed without product behavior changes and does **not** need to be rerun.

Its validation taxonomy remains an ownership map:

```text
external trust-boundary validation
semantic/domain validation
relational/rebinding validation
repeated internal invariants
impossible-state defense
```

but the R0 inventory is **not a retention list**. An individual current field/check still has to earn retention under `JUST-*`.

Specific R0 correction already absorbed into R1:

- provider blob identity was originally grouped with external validation;
- that classification only said where such a check currently lives;
- it did not establish that UpgradePilot needs blob identity at all;
- R1 therefore reopened the field rather than grandfathering it.

Other frozen R0 findings remain:

- `uv_lock.py` and `uv_membership.py` duplicate material `uv.lock` structural truth and already diverge on versionless-record admission;
- S001 `uv sync --all-packages --group docs` loses `--all-packages` scope in the current typed selection declaration;
- the smallest justified uv proposition is explicit selected-root reachability;
- the accepted S001 positive witness remains `docs → mkdocs-llmstxt → beautifulsoup4 → soupsieve`;
- static dependency consumption, static direct exercise, and exact-head runtime authority remain separate proof classes.

## R1 frozen exact-file contract direction

### 1. One strong successful type

The consumer/construction scan supports one strong `RepositoryTextFile`, not a parallel trusted/exact hierarchy merely for historical/test convenience.

The frozen minimum durable contract is:

```text
RepositoryTextFile
├── repository
├── path
├── revision       # exact immutable Git commit/object identity admitted by this provider path
└── content        # admitted UTF-8 text
```

The type should enforce the internal structural invariants of these facts without silently coercing malformed values. The GitHub provider remains the owner of actual external acquisition; a Python dataclass cannot and need not cryptographically prove that a manually fabricated object came from GitHub.

`UnavailableRepositoryFile` should carry the same required source locator:

```text
repository
path
revision
reason
detail
```

so successful and unavailable exact-source states remain explicit and structurally coherent.

### 2. Validate then discard

The following current GitHub-response details are **not justified as durable `RepositoryTextFile` fields**:

```text
returned_path
reported_byte_count
decoded_byte_count
blob_sha
retrieved_at
```

Current R1 reasoning:

- **returned path:** needed only to prove GitHub returned the exact requested repository path; after equality succeeds, preserving a second path spelling adds no new fact.
- **reported size:** provider metadata is not part of a current product proposition. UpgradePilot can bound the actual decoded bytes directly; a mismatch between two GitHub-supplied representations does not add a necessary domain fact once actual content is safely bounded.
- **decoded byte count:** derivable from the admitted bytes/content when needed and currently propagated mainly to revalidate acquisition consistency downstream.
- **blob SHA:** provider-native content-object identity can be useful for caching/dedup/object lookup in other systems, but no current admitted UpgradePilot proposition requires those capabilities. Exact `repository + immutable revision + path` already identifies the repository file used by the current evidence flow. Current consumer comparisons/copies are migration pressure, not independent justification.
- **retrieval time:** exact repository files are addressed by immutable revision. No current decision, staleness rule, or proof uses their wall-clock fetch time. The project evidence doctrine requires time/revision context where material; for these files the immutable revision is the material temporal/source context. Mutable API evidence may still legitimately own `retrieved_at` separately.

This does **not** weaken necessary acquisition checks. The provider must still validate the untrusted response sufficiently to establish one bounded exact UTF-8 text file:

```text
requested path is admitted
response describes a regular file
returned path == requested path
encoding/content shape is supported
base64 decoding is strict
actual decoded bytes stay within the bound
content decodes as UTF-8
```

Provider `sha`/reported `size` should not remain required response fields merely because the current implementation reads them if the final migration confirms no independent acquisition need.

### 3. Alias direction

Current aliases:

```text
ExactRepositoryTextFile = RepositoryTextFile
ExactRepositoryFileEvidence = RepositoryTextFile | UnavailableRepositoryFile
RepositoryFileEvidence = RepositoryTextFile | UnavailableRepositoryFile
```

are redundant under the frozen one-strong-type direction. R1 implementation should migrate active source/tests to one concrete success type plus one `RepositoryFileEvidence` union unless a real distinct responsibility appears during migration.

### 4. Downstream propagation scheduled for removal

Current-use inspection found no independent reason to preserve the following metadata propagation:

```text
DependencyChangeSourceEvidence
→ base_blob_sha / head_blob_sha
→ base_byte_count / head_byte_count

TargetArtifactEnvironmentEvidence
→ workflow_blob_sha

TargetPythonDeclaration / TargetPythonDeclarationProblem
→ blob_sha

TaggedChangelogEvidence
→ returned_path / blob_sha / reported_byte_count / decoded_byte_count / retrieved_at

CrossedReleaseSourceWindow
→ blob_sha

CLI
→ rendering dependency blob/byte metadata
```

These are migration targets, not retained compatibility requirements.

### 5. Relations that remain independently justified

R1 simplification does **not** erase real joins. Current independently justified examples include:

```text
base/head repository identity belongs to the same dependency comparison
base/head path matches the changed-file path
repository-file revision matches the intended PR base/head or exact tag commit
uv lock path/revision matches the dependency context it is being combined with
static declaration project root matches the project evidence being evaluated
CI consumption matches the retained workflow/job/step/segment proposition
upstream changelog repository/revision matches the resolved upstream tag commit
```

Whether a later R2–R5 redesign narrows one of those relations is decided by that responsibility, not by legacy usage.

## R1 implementation migration surface

The frozen contract now has enough justification to move from design to code.

Primary product source migration surface:

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

`src/upgradepilot/dependency/requirements.py` constructs the same source-independent `DependencyChangeSourceEvidence` but does not depend on the exact-file metadata being removed; it remains regression pressure rather than a required edit unless the shared type change demands one.

Affected developer-tool/experiment/test fixtures must migrate with the product contract rather than forcing compatibility fields back into production.

## Current plan status

```text
✓ R0  re-anchor contracts + freeze behavior
→ R1  strengthen exact repository-file evidence ownership
     ✓ retention rule hardened
     ✓ consumers/construction mapped
     ✓ durable-field necessity pressured
     ✓ minimum contract frozen
     → coherent source + tests/tool migration NEXT
  R2  one bounded uv-specific structural lock model
  R3  preserve minimum real uv command/workspace scope
  R4  narrow uv membership to explicit selected-root reachability
  R5  rebind CI consumption to reconciled evidence
  R6  pressure S001 / S011 / S005 + changed-case workspace transfer
  R7  acceptance + audit disposition + deferred-plan re-review
```

No R1 product-source behavior has been modified yet. The latest product-runtime validation point therefore remains unchanged.

## Continuation-critical guards

- `MEMORY.md` alone owns live continuation.
- The current reconciliation plan is the only active implementation route until its final STOP/REVIEW gate or Ali changes selection.
- Existing implementation/current use/passing tests/history are not retention authority.
- Never justify an upstream field from a downstream consumer whose dependence on that field is itself being reviewed.
- Do not start old Cluster 6, the agentic evaluation, Tranche 2, or a separate source-clarity pass in parallel.
- Preserve necessary GitHub/external trust-boundary validation, but do not preserve provider metadata that proves no required fact.
- Preserve independently necessary relational/rebinding checks.
- Do not introduce generic trust/provenance wrappers, generic dependency graphs, or generic package-manager abstractions without new evidence and explicit admission.
- Do not build a complete uv environment interpreter merely to justify an over-broad name.
- project/lock coherence/currentness and resolver/runtime evidence remain separate propositions.

## Immediate project action

Implement the frozen R1 contract as one coherent migration rather than a compatibility shim:

```text
1. strengthen RepositoryTextFile / UnavailableRepositoryFile construction invariants
2. reduce GitHub exact-file acquisition to necessary response checks + actual-byte bound
3. migrate active source away from exact-file blob/count/path-duplicate/time fields and redundant aliases
4. preserve only independently justified cross-object relations
5. migrate tests/tools/experiments to the new contract; do not keep production compatibility fields for fixture convenience
6. run focused provider + dependency + Target + upstream tests, then nearest integration/full suite when a runnable environment is available
7. record exact validation evidence before marking R1 complete
```

## Learning state

Ali's predictions and design answers are learning inputs, not engineering authority. The AI must lead from admitted responsibilities, source/evidence, proof boundaries, professional technical judgment, and simpler adequate alternatives; it should correct Ali's reasoning when needed and explain why.

A key R1 lesson now established is:

```text
current code uses X
!= product requires X

provider returns X
!= durable evidence needs X

one strong source locator + content
can be better than carrying every provider metadata field forward
```

The dedicated learning-folder route remains paused because the source being learned is under active redesign. Resume, rewrite, or close it only after R7 re-review.