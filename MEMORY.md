# UpgradePilot Current Memory

**Last updated:** 2026-07-30 16:31 +03:30  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, and exact continuation.

Stable route definitions, specifications, ADRs, source, tests, plans, and dated evidence retain their own responsibilities. This file records only the current position required to continue.

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Controlling route:** [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md)
- **B2 gate:** [`plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)
- **Selected bounded plan:** [`plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)
- **Accepted architecture:** [`docs/architecture/ADR-0004-dependency-version-change-evidence.md`](docs/architecture/ADR-0004-dependency-version-change-evidence.md)
- **Downstream package/upstream plan:** [`plans/B2_MINIMUM_PACKAGE_AND_UPSTREAM_EVIDENCE_PLAN.md`](plans/B2_MINIMUM_PACKAGE_AND_UPSTREAM_EVIDENCE_PLAN.md)
- **Downstream Python relevance plan:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)
- **Naming control:** [`docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md`](docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md)
- **Latest decision evidence:** [`working-memory/2026-07-30_1631_B2-dependency-evidence-design-closure.md`](working-memory/2026-07-30_1631_B2-dependency-evidence-design-closure.md)
- **Previous decision evidence:** [`working-memory/2026-07-30_1550_B2-version-and-ci-evidence-cluster-3.md`](working-memory/2026-07-30_1550_B2-version-and-ci-evidence-cluster-3.md)
- **Latest relevant non-memory revision:** `42a78d2cb1b3fef5a1eae7e14d5e7b279faaf552`.

Use local `HHMM` after the date for additional same-day working-memory records. Existing files are not renamed merely to retrofit the convention.

## Current phase

The dependency-version-change **design phase is closed**.

Decision Clusters 1–3 were progressively discussed and approved. Ali explicitly stated that he did not understand the final acquisition and duplicate-record details, delegated the remaining engineering decisions, and asked to learn the material during implementation.

ADR-0004 therefore authorizes the selected implementation method. It does not establish Ali's understanding, mastery, or ability to reproduce it.

The selected plan no longer has unresolved architecture gates. Product implementation may begin only through its ordered build sequence.

## Behavior-validated product boundary

The latest behavior-validated product revision remains:

```text
75e1b5c55844c2e7b6f9f64d6ae1bd76c2dabd15
```

At that revision Ali ran:

```text
Ran 72 tests
OK
```

One installed public read-only S004 command preserved the existing evidence chain.

Current implemented behavior reaches:

```text
public repository + Dependabot PR
→ exact PR identity and complete changed files
→ one supported same-file package==version transition
→ exact-head target declaration evidence
→ exact-head workflow/job/step evidence
→ current bounded CI classification
→ exact PyPI package/version/file identity
→ matching upstream repository and release evidence
→ concise CLI evidence report
→ unresolved_claim
```

The current source still uses names such as:

```text
PinnedDependencyChange
CIAuthorityResult
```

Those names and behaviors remain runtime truth until replaced through implementation and tests.

## Why the selected plan is required

S004 uses:

```text
requirements-dev.txt
pytest 9.0.2 → 9.0.3
```

S001 uses:

```text
pydantic/pydantic PR 13432
uv.lock
soupsieve 2.6 → 2.8.4
```

The current exact-requirement parser cannot establish S001's structured lockfile transition. Dependency identity must be corrected before further Python-support relevance work.

S001 remains the intended downstream relevance case:

```text
upstream: Drop support for Python 3.8.
target: requires-python >=3.10
expected bounded relevance: outside_declared_python_range
```

That relevance result is not implemented or behavior-validated.

## Accepted dependency evidence architecture

The selected flow is:

```text
admitted dependency file
→ clearly named source-specific extraction
→ ExtractedDependencyVersionChange or DependencyChangeEvidenceProblem

all extracted changes and recognized source problems
→ compare_extracted_dependency_changes
→ DependencyVersionChange or explicit problem
```

B2 supports exactly one package version transition.

The trusted record preserves:

```text
package
normalized package
exact raw old version
exact raw proposed version
all supporting DependencyFileEvidence
limitations
```

It does not imply dependency role, CI consumption, compatibility, safety, or maintainer action.

## Admitted dependency files

First formats:

1. conventional exact `package==version` requirements and constraints files;
2. modified same-path files whose basename is exactly `uv.lock`.

Requirements/constraints paths may be nested. Path eligibility does not establish installation, CI consumption, role, compatibility, or safety.

The first `uv.lock` boundary requires:

```text
GitHub status: modified
basename: uv.lock
same complete path at base and head
both exact files available
schema version: 1
revision: non-negative integer
parser: Python 3.12 tomllib
```

Added, deleted, renamed, unsupported-schema, and changed duplicate-resolution cases remain explicit non-success states.

## Exact file acquisition decision

Use GitHub's Contents endpoint at only the immutable PR base or head SHA.

Keep:

```text
1,000,000 decoded-byte maximum
```

Require:

- non-negative GitHub-reported size;
- early rejection above the bound;
- valid Base64;
- decoded byte count equal to reported size;
- decoded byte count within the bound;
- valid UTF-8;
- exact path, revision, blob, and byte evidence.

Do not add a blob/raw fallback in B2.

Measured S001 files:

```text
base revision: 652a61ce4f9d7d76eaada31535807a485ece0e21
base blob:     b4a68ab725de337889d50d5374ac0f05db7fb484
base bytes:    606,307

head revision: aa2dc024d33f61cdef50bf1973ab5adf0a974f5a
head blob:     def33fe05d78ab851ce91a33db5bc55a439873a1
head bytes:    606,313
```

Both fit the existing boundary. The head is six bytes larger.

## `uv.lock` duplicate-record decision

Group package records by normalized package name.

For repeated-name groups:

```text
remove only top-level sdist and wheels
retain every other parsed field
preserve internal list order
compare records as unordered multisets
```

```text
unchanged duplicate group
→ does not block another clear version transition

changed duplicate group
→ ambiguous_uv_lock_package_records
```

Do not pair duplicate records by position or implement uv resolver semantics.

S001 contains real unchanged duplicate-name groups, including marker-separated `numpy` and `pyodide-build` records. Soup Sieve remains a single unambiguous record in each exact file.

## Version and CI boundaries

Dependency extraction preserves exact raw version text and performs no PEP 440 ordering.

Downstream package/upstream work later owns:

```text
packaging.version.Version
invalid_python_package_version
equivalent_python_package_versions
dependency_version_not_forward
```

`packaging` has not yet been admitted or installed.

Future CI result:

```text
DependencyCIExerciseResult
proven / no_successful_ci / unresolved
```

Exact requirements may use the existing direct `pip -r` plus direct package invocation rule. Constraints and `uv.lock` do not inherit requirements-file install semantics. Unresolved CI does not erase dependency identity and must not appear as green evidence.

## Selected implementation names

```text
DependencyVersionChange
ExtractedDependencyVersionChange
DependencyFileEvidence
DependencyChangeEvidenceProblem
compare_extracted_dependency_changes

is_exact_requirement_file
extract_exact_requirement_changes

is_modified_uv_lock_file
extract_uv_lock_changes

ExactRepositoryTextFile
get_pull_request_base_file
get_pull_request_head_file

DependencyCIExerciseResult
evaluate_dependency_ci_exercise
```

Public labels:

```text
Dependency change
Dependency evidence
CI dependency exercise
```

## Learning boundary

Architecture acceptance is not learning evidence.

During implementation, each new concept must be taught at the point of use:

```text
record/function/rule
→ full term and practical meaning
→ why the name fits
→ input and output
→ mechanism at the current required depth
→ smallest proving test
→ user review before the next conceptual unit
```

Progress tracking must distinguish introduction, partial understanding, tested use, and deeper technical understanding. It must not mark the architecture mastered because AI wrote code or Ali approved the ADR.

## Exact continuation

Begin **Step 1 only** of the selected plan:

```text
freeze and test shared dependency-change records and problem states
```

The first implementation session must:

1. inspect the current `dependency_change.py` and directly coupled tests/callers;
2. teach what the existing `PinnedDependencyChange` and unsupported result currently do;
3. define the smallest new immutable records:
   - `DependencyFileEvidence`;
   - `ExtractedDependencyVersionChange`;
   - `DependencyVersionChange`;
   - `DependencyChangeEvidenceProblem`;
4. define the initial explicit problem vocabulary without implementing file parsers;
5. write focused contract tests first or alongside the records;
6. preserve current behavior until later migration steps;
7. run the focused tests and complete deterministic suite;
8. record evidence and update this file.

Do not begin exact-requirement extraction migration, generic base/head acquisition, `uv.lock` parsing, CI migration, PEP 440 work, or public S001 execution during Step 1 unless the selected plan is explicitly advanced after proof.

## Not established

- the accepted architecture implemented in product source;
- any new shared record or problem type in runtime code;
- path eligibility enforcement;
- constraints-file product behavior;
- generic exact PR base/head file acquisition;
- reported/decoded byte-size validation;
- `uv.lock` parsing;
- duplicate-group comparison;
- S001 dependency identity through the product;
- `DependencyCIExerciseResult` runtime behavior;
- `packaging` admission or PEP 440 runtime validation;
- crossed-version upstream acquisition;
- reliable Python support-drop extraction;
- target/upstream relevance comparison;
- compatibility, safety, maintainer action, or production readiness;
- Ali-owned understanding or mastery of the accepted architecture.

## Relevant revisions

```text
Behavior-validated product:
75e1b5c55844c2e7b6f9f64d6ae1bd76c2dabd15

ADR-0004 accepted:
a305753462cbf4bb0f30739ea9a91567cb2ec931

Selected plan closed and build-authorized:
3c6df2e1a62c125030a29ff016eb88259fa960d8

Architecture register updated:
4dfd0208b774744d51c4bde245d17a181556fd2a

Design closure evidence:
42a78d2cb1b3fef5a1eae7e14d5e7b279faaf552
```

## State-maintenance rule

When route, selected plan, verified behavior, blocker, or exact continuation changes, update this file only. Change another file only when its stable responsibility or dated evidence changes.