# Case Identity, Validation, and Normalization

**Related session:** M2-S01  
**Current depth:** Taught and partly reasoned with guidance; not yet demonstrated through accepted implementation  
**Purpose:** Concise review note for the concepts required by UpgradePilot's first automated responsibility

## 1. Case identity

Case identity answers:

> Which exact dependency-update proposal and repository snapshot are we analysing?

For M2-S01, the record contains:

```text
repository
pr_number
base_sha
head_sha
dependency
old_version
new_version
changed_files
```

The fields have different roles:

- `repository` and `pr_number` locate the pull-request workflow object;
- `base_sha` and `head_sha` identify the exact before-and-after Git snapshots;
- dependency, version, and changed-file fields describe the update inside that snapshot.

A PR can receive new commits while keeping the same number. Therefore a CI result or conclusion for one head SHA must not automatically be attached to another head SHA.

## 2. Identity, evidence, and recommendation are separate responsibilities

They may live inside one larger case structure, but they answer different questions:

```text
case identity
→ what exact case is this?

release and repository evidence
→ what was observed about it?

CI evidence
→ what checks ran for which revision?

recommendation
→ what action follows from the available evidence?
```

Keeping these boundaries prevents real evidence from being associated with the wrong snapshot and allows recommendations to change when evidence changes.

## 3. Raw and normalized input

**Raw input** preserves exactly what the caller supplied.

**Normalized input** is a predictable representation produced by declared transformations, such as trimming surrounding whitespace.

Example:

```text
raw:        "  soupsieve  "
normalized: "soupsieve"
```

Normalization must not guess missing facts, expand unknown SHAs, change versions, or invent file paths.

## 4. Validation versus normalization

```text
messy but acceptable representation
→ normalize

invalid structure or meaning
→ reject
```

Examples:

- surrounding whitespace can be trimmed;
- a non-positive PR number is invalid;
- a full base or head SHA must be exactly 40 hexadecimal characters for this session;
- dependency and version values must be non-empty;
- old and new versions must differ;
- `changed_files` must contain at least one non-empty path.

A malformed value is not an outlier. It is invalid input because it fails a required rule.

## 5. Deterministic, non-mutating transformation

The intended data flow is:

```text
raw dictionary
→ verify keys and types
→ normalize supported text
→ validate semantic rules
→ construct a new dictionary and new changed-files list
→ return normalized result
```

The original input remains unchanged.

This supports:

- provenance: preserve what entered the system;
- debugging: compare before and after;
- safer data flow: other code does not observe silent mutation;
- reproducibility: the same raw input can be transformed again.

A deterministic function gives the same output for the same input and rules. It should not depend on time, network state, randomness, or hidden mutable state.

## 6. Explicit failure

Invalid identity should raise a clear error rather than return an empty result or guess a repair.

For M2-S01, `ValueError` communicates that a supplied value is unacceptable for the responsibility.

A useful error identifies:

- the invalid field;
- the expected rule;
- enough public-safe case context to locate the problem.

Example meaning:

```text
head_sha is invalid:
expected exactly 40 hexadecimal characters
```

This validates only visible format. It does not prove that the commit exists remotely.

## 7. Python mechanics used by this responsibility

- **Dictionary:** maps required field names to values.
- **List:** stores one or more changed-file paths in order.
- **Function:** receives the raw dictionary and returns the normalized dictionary.
- **Parameter:** the function's input name.
- **Return value:** the separate normalized result.
- **Local variable:** an intermediate value used for clear validation and transformation.
- **Module:** one `.py` file containing the function.
- **Package:** a directory of related importable modules; not automatically required for one function.
- **Type hint:** documents expected types for people and tools; normal Python does not enforce every hint automatically.
- **Exception:** a structured signal that normal execution cannot continue.

## 8. Tests and their claim boundary

The session requires:

- one valid real-case test;
- one malformed or missing `head_sha` test;
- one assertion that raw input remains unchanged.

A valid test can support that the tested input produces the expected normalized result and preserves raw input.

An invalid test can support that the selected malformed SHA is rejected with the expected error behavior.

These tests do not prove:

- every possible invalid case is covered;
- the function is universally correct;
- GitHub evidence is accurate;
- the complete UpgradePilot product works;
- the code is production-ready.

## 9. Current boundary

This note records the mental model required before implementation. It does not record:

- an accepted file layout;
- accepted source code;
- passed tests;
- independent Python or testing capability;
- permanent architecture.

Those must be established through the active M2-S01 working record, observed execution, Ali-directed modification, and failure diagnosis.

## Related files

- `../../docs/program/career/plans/UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md`
- `../../working-memory/2026-07-20_M2-S01_case-identity-normalization.md`
- `../../MEMORY.md`
