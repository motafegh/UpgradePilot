# UpgradePilot Current Memory

**Last updated:** 2026-07-30 17:01 +03:30  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, and exact continuation.

Stable route definitions, specifications, ADRs, source, tests, plans, and dated evidence retain their own responsibilities. This file records only the current position needed to continue.

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Controlling route:** [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md)
- **B2 gate:** [`plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)
- **Selected plan:** [`plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)
- **Accepted architecture:** [`docs/architecture/ADR-0004-dependency-version-change-evidence.md`](docs/architecture/ADR-0004-dependency-version-change-evidence.md)
- **Implementation evidence:** [`working-memory/2026-07-30_1644_B2-step-1-dependency-contracts-partial-proof.md`](working-memory/2026-07-30_1644_B2-step-1-dependency-contracts-partial-proof.md)
- **Learning correction:** [`working-memory/2026-07-30_1701_B2-learning-record-correction.md`](working-memory/2026-07-30_1701_B2-learning-record-correction.md)
- **Latest relevant non-memory revision:** `ddfef91f5773da9b6aa772d02d560b5214ad4ba3`.

## Current phase

The dependency-version-change design phase is closed.

Implementation has begun through **Step 1 only**:

```text
freeze and test shared dependency-change records and problem states
```

Current Step 1 state:

```text
source records and focused tests committed
but
repository tests not executed
and
technical teaching not yet begun properly
```

Do not begin Step 2.

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

The Step 1 commits do not yet extend this behavior-validated boundary.

The current runtime still uses:

```text
ChangedFile[]
→ extract_pinned_dependency_change
→ PinnedDependencyChange or UnsupportedDependencyChange
```

`PinnedDependencyChange.source_file` still combines the file where the change was observed with the requirements file expected by the current CI rule. The legacy parser, CLI, CI evaluator, workflow-command reader, and output labels remain runtime truth.

## Step 1 implementation present

The following additive contracts are committed in `src/upgradepilot/dependency_change.py`:

```text
DependencyFileEvidence
ExtractedDependencyVersionChange
DependencyVersionChange
DependencyChangeEvidenceProblem
DependencyChangeExtractionResult
DependencyChangeComparisonResult
```

Focused tests are committed in:

```text
tests/test_dependency_change_contracts.py
```

Package-level exports were added without migrating existing runtime callers.

Relevant implementation revisions:

```text
81717384f7351dd018c2ba7c3a2bfc7db970dc63
Add shared records and vocabulary

d9bf3c6c9317ecaee9a03c842e92d75a902d0394
Add focused contract tests

e8447a9c8330e67df5bbcdd3ba832ad53a5cf745
Expose package-level contracts

121d70530c97a80cca83c648670c71d874a66930
Use case-neutral contract fixtures
```

No new parser produces the new records yet.

## Corrected learning state

The previous memory version incorrectly described these concepts as introduced during the implementation session:

```text
dataclass
frozen dataclass
slots
tuple immutability
union-style result handling
extracted versus trusted dependency evidence
stable problem vocabulary
```

That claim is withdrawn.

What actually occurred was brief implementation narration by the assistant. There was no structured lesson, code walkthrough, exercise, comprehension question, user explanation, or demonstrated reasoning.

Correct learning state:

```text
concept names briefly mentioned by the assistant
but
not taught properly
not practiced by Ali
not assessed
not mastered
```

Do not count generated code, assistant commentary, architecture approval, or test execution as user learning evidence.

## Proof state

Completed:

- repository source and direct-caller inspection;
- additive source implementation;
- focused test definition;
- package export update;
- case-neutral fixture review;
- local Python 3.13 smoke check of equivalent record mechanics.

Not completed:

- committed focused contract tests;
- existing dependency-change tests;
- complete deterministic suite;
- Python 3.12 repository execution;
- installed command validation after Step 1;
- structured teaching of the new contracts;
- Ali-owned explanation of any new concept.

The local smoke check is not repository behavior validation and is not learning evidence.

## Exact continuation

Remain in **Step 1**.

The next session must begin with a real teaching unit before requesting test execution:

```text
existing PinnedDependencyChange
→ what a record/value object is
→ @dataclass
→ generated constructor and equality
→ frozen=True
→ slots=True
→ inspect the actual source and one existing test
→ ask Ali to explain the current meaning
```

Then continue one concept at a time:

1. compare list and tuple behavior using `source_evidence`;
2. teach success-or-problem union results and caller type narrowing;
3. distinguish `ExtractedDependencyVersionChange` from trusted `DependencyVersionChange` through a concrete two-file example;
4. read the focused tests with Ali;
5. assess only the depth actually demonstrated.

After the teaching review, run in a real repository checkout:

```bash
python --version
python -m unittest tests.test_dependency_change_contracts -v
python -m unittest tests.test_dependency_change -v
python -m unittest discover -s tests -v
```

Only after teaching at introductory depth and all required tests pass may Step 1 be recorded as behavior-validated and Step 2 considered.

## Not established

- Step 1 behavior validation;
- Ali's understanding of dataclasses, frozen records, slots, tuples, or union results;
- any new parser using the shared contracts;
- `compare_extracted_dependency_changes` implementation;
- path eligibility enforcement;
- constraints-file product behavior;
- generic exact PR base/head acquisition;
- reported/decoded byte-size validation;
- `uv.lock` parsing;
- duplicate-group comparison;
- S001 dependency identity through the product;
- `DependencyCIExerciseResult` runtime behavior;
- `packaging` admission or PEP 440 runtime validation;
- Python-support relevance;
- compatibility, safety, maintainer action, or production readiness.

## State-maintenance rule

When route, selected plan, verified behavior, blocker, learning state, or exact continuation changes, update this file only. Change another file only when its stable responsibility or dated evidence changes.