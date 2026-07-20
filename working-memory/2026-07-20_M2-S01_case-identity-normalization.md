# M2-S01 Working Memory — Case-Identity Normalization

**Date:** 2026-07-20  
**Session:** M2-S01  
**Status:** Active  
**Route / milestone:** R2 / M2 — First automated vertical slice  
**Mode:** Green  
**Focused minutes:** Not recorded

## Authorized objective

Given manually supplied identity fields for `pydantic/pydantic#13432`, validate and normalize them into one deterministic Python record without mutating the raw input.

This record follows the controlling plan at:

- `docs/program/career/plans/UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md`

## Starting repository state

At session activation:

- accepted source implementation: none;
- accepted tests: none;
- accepted package layout: none;
- accepted architecture: none;
- the removed AI-generated scaffold and retained proposal files were not implementation baselines;
- the real case identity was sourced from the completed Career M1 report, not reconstructed from memory.

The starting state is preserved here as history. The source-layout decision recorded below changed the accepted design state but created no implementation.

## Scope and stop line

Authorized during M2-S01:

- one manually created Python dictionary for the real case;
- identity-field validation and text normalization;
- a new normalized dictionary while preserving raw input;
- the accepted minimum source/package boundary required by the controlling plan;
- one valid unit test;
- one malformed or missing `head_sha` test;
- one raw-input non-mutation assertion;
- one Ali-directed behavior change;
- one deliberately observed and diagnosed failure.

Not authorized:

- live GitHub or PyPI acquisition;
- JSON contracts or schema frameworks;
- recommendation policy or report generation;
- persistence or databases;
- CLI or public API;
- external runtime or test dependencies;
- CI, containers, cloud, agents, ML, graph, or broader architecture adoption;
- speculative source subpackages or layered directories;
- restoration of removed scaffold files.

No package metadata, source, or test file may be created before the integrated behavior gate passes.

## Progress against the session plan

### Step 1 — Orient

**Status:** Complete enough to proceed.

Established:

- the single responsibility being built;
- why exact repository, PR, base, and head identity matters;
- what remains outside the session;
- why the previous generated scaffold and architecture are not reused.

### Step 2 — Teach and close the behavior gate

**Status:** In progress; teaching substantially completed, integrated gate still open.

Concepts introduced at the depth required before implementation:

- case identity and exact PR snapshots;
- repository/PR identity versus base/head revisions;
- evidence association with the correct snapshot;
- raw versus normalized input;
- normalization versus validation;
- deterministic transformation;
- explicit invalid-input failure and `ValueError`;
- dictionaries and lists;
- functions, parameters, return values, and local variables;
- mutation, shallow copying, and constructing independent output data;
- modules, packages, imports, and basic type hints;
- unit tests, assertions, arrange/act/assert, and bounded test claims;
- repository versus distribution package versus import package;
- `src` layout and the purpose of editable installation;
- import-path verification rather than assuming source-tree appearance proves installation correctness.

Observed guided reasoning:

- Ali explained that one PR number can contain different changes and therefore commit identity matters.
- Ali recognized that a CI result for an earlier head revision does not automatically support a later revision.
- Ali selected clear error raising rather than silent continuation for malformed identity.
- Ali distinguished the need for case identity from later evidence after clarification.
- Ali recognized that the uppercase repository name does not need to become the Python import name.
- Ali challenged repeated-name and temporary-layout explanations until the project-wide source/package boundary was treated as a real professional decision.

Not yet demonstrated as one connected model:

- the complete flow from raw identity through normalization, validation, explicit failure, non-mutation, and bounded test evidence.

### Step 3 — Select and record the initial source layout

**Status:** Complete as a design decision; implementation unproven.

#### Problem identified

The original plan framed the choice as a temporary layout for one small function. Ali correctly challenged that framing because the first accepted source files may become the foundation of the full UpgradePilot codebase.

The design review therefore considered:

- production-oriented Python project structure;
- repository/product naming versus Python import naming;
- long-term module growth;
- import namespace clarity;
- installed-package behavior;
- avoiding speculative internal architecture;
- preserving the learning-by-building method.

#### Accepted decision

```text
UpgradePilot/                  # repository and product workspace
├── pyproject.toml             # minimum metadata; not created yet
├── src/
│   └── upgradepilot/          # import package; not created yet
│       ├── __init__.py
│       └── case_identity.py
└── tests/
    └── test_case_identity.py
```

Naming:

- product/repository: `UpgradePilot`;
- distribution: `upgradepilot`;
- import package: `upgradepilot`;
- first module: `upgradepilot.case_identity`.

Decision record:

- `docs/architecture/ADR-0001-initial-python-source-layout.md`

#### Alternatives rejected

- rename the repository to lowercase — no import or architecture benefit;
- place generic modules directly under `src/` — no project namespace;
- use a root-level module — weak long-term project baseline;
- use a flat root package — workable, but weaker installed-package boundary;
- invent another import package name — unnecessary conceptual translation;
- pre-create domain/application/adapters/services directories — speculative architecture.

#### Boundary

The decision accepts a source/package boundary, not a complete internal architecture.

No `pyproject.toml`, `src/`, package, source, or test file was created during this design step.

#### Reassessment triggers

Revisit only when observed evidence shows an import, packaging, distribution, interface, or module-cohesion limitation.

### Steps 4–10

Not started.

No package metadata, installation command, import output, source code, tests, accepted behavior, or implementation ownership exists yet.

## Instructional correction

The first teaching attempt fragmented the material into repeated micro-questions before a complete mental model had been taught. Ali correctly identified that this damaged momentum and forced guessing.

The corrected rhythm is:

```text
one meaningful technical chunk
→ connected explanation and example
→ one integrated reasoning, tracing, transfer, or practical task
→ inspect evidence
→ correct the model
→ continue
```

Avoid fill-in-the-blank, forced-choice, and one-question-per-detail assessment when the goal is reasoning capability.

The source-layout discussion revealed a second correction:

> A “temporary” implementation choice must still be evaluated against the likely growth of the real project when it creates the first accepted source boundary.

This does not mean designing the full future architecture. It means distinguishing a durable foundational boundary from speculative internal layers.

## Durable learning material

Current learning note:

- `learning/concepts/case-identity-validation-and-normalization.md`

Accepted source-layout rationale:

- `docs/architecture/ADR-0001-initial-python-source-layout.md`

The learning note is a review aid. The ADR records an accepted project decision. Neither proves practical mastery or implementation ownership.

## Assistance and ownership state

- Current work is AI-assisted.
- Ali materially directed the learning pace and integrated-assessment correction.
- The technical source-layout recommendation and decision-document drafting were substantially AI-generated.
- Ali challenged the initial framing, required a production-grade project-wide assessment, explicitly accepted the recommendation, and directed repository-wide alignment.
- The source-layout decision is therefore Ali-directed.
- No package creation, installation, import verification, implementation, test execution, or debugging is Ali-owned yet.
- Capability depth must not be upgraded until practical execution, modification, test interpretation, and diagnosis evidence exists.

## Exact next action

1. Close the integrated behavior gate through one connected explanation of the complete case-identity responsibility.
2. Review ADR-0001 only to confirm understanding of the accepted source boundary; do not reopen it as a preference poll without new evidence.
3. Create only `pyproject.toml` and `src/upgradepilot/__init__.py`.
4. Run editable installation and verify that `import upgradepilot` resolves from `src/upgradepilot/`.
5. Write `tests/test_case_identity.py` first and observe the expected failure.
6. Only then create `src/upgradepilot/case_identity.py` and implement the smallest passing behavior.