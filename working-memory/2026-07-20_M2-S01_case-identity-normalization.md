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

- Accepted source implementation: none.
- Accepted tests: none.
- Accepted package layout: none.
- Accepted architecture: none.
- The removed AI-generated scaffold remains historical only and is not an implementation baseline.
- The real case identity is sourced from the completed Career M1 report, not reconstructed from memory.

## Scope and stop line

Authorized during M2-S01:

- one manually created Python dictionary for the real case;
- identity-field validation and text normalization;
- a new normalized dictionary while preserving raw input;
- one valid unit test;
- one malformed or missing `head_sha` test;
- one raw-input non-mutation assertion;
- one Ali-directed behavior change;
- one deliberately observed and diagnosed failure.

Not authorized:

- live GitHub or PyPI acquisition;
- JSON contracts or schema frameworks;
- recommendation policy;
- persistence or databases;
- CLI or public API;
- external runtime or test dependencies;
- CI, containers, cloud, agents, ML, graph, or broader architecture adoption;
- restoration of removed scaffold files.

No source or test file may be created before the pre-code gate passes and the temporary file layout is selected and recorded here.

## Progress against the session plan

### Step 1 — Orient

**Status:** Complete enough to proceed.

Established:

- the single responsibility being built;
- why exact repository, PR, base, and head identity matters;
- what remains outside the session;
- why the previous generated scaffold is not reused.

### Step 2 — Teach and predict

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
- unit tests, assertions, arrange/act/assert, and bounded test claims.

Observed guided reasoning:

- Ali explained that one PR number can contain different changes and therefore commit identity matters.
- Ali recognized that a CI result for an earlier head revision does not automatically support a later revision.
- Ali selected clear error raising rather than silent continuation for malformed identity.
- Ali distinguished the need for case identity from later evidence after clarification.

Not yet demonstrated as one connected model:

- the complete flow from raw identity through normalization, validation, explicit failure, non-mutation, and bounded test evidence.

### Step 3 — Select temporary file layout

**Status:** Not started.

Options still to compare:

1. one root module;
2. a small flat `upgradepilot/` package;
3. a `src/` layout package.

No option is accepted yet. Any selection is temporary for this responsibility and is not a permanent architecture decision.

### Steps 4–9

Not started. No source code, tests, commands, outputs, accepted behavior, or implementation ownership exists yet.

## Instructional correction

The first attempt fragmented the material into repeated micro-questions before a complete mental model had been taught. Ali correctly identified that this damaged momentum and forced guessing.

The corrected rhythm for the rest of the session is:

```text
one meaningful technical chunk
→ connected explanation and example
→ one integrated reasoning, tracing, transfer, or practical task
→ inspect evidence
→ correct the model
→ continue
```

Avoid fill-in-the-blank, forced-choice, and one-question-per-detail assessment when the goal is reasoning capability.

## Durable learning note

A concise review note is stored at:

- `learning/concepts/case-identity-validation-and-normalization.md`

It is a review aid, not evidence of mastery or implementation ownership.

## Assistance and ownership state

- Current work is AI-assisted.
- Ali materially directed the learning pace and assessment correction.
- No implementation is Ali-owned or AI-generated in the active tree.
- Capability depth must not be upgraded until practical implementation, modification, test interpretation, and diagnosis evidence exists.

## Exact next action

1. Close the pre-code gate through one integrated discussion or practical trace of the complete responsibility.
2. Compare the three temporary layout options.
3. Record Ali's selected layout and rationale here.
4. Only then create the valid test first.
