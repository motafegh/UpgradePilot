# B2 Step 5B — Git Tag-to-Commit Validation Evidence

**Date:** 2026-08-02  
**Role:** Historical validation evidence only. `MEMORY.md` owns live project state.

## Validated responsibility

Step 5B resolves one explicitly supplied Git version tag to one immutable commit:

```text
repository + exact requested tag
→ refs/tags/{tag}
→ lightweight commit target
   or bounded annotated-tag peeling
→ resolved commit SHA
```

The validated implementation boundary is:

```text
783a22c790b0c45487acf3b4d3a4698ba7484a82
```

Later Step 5B working-memory/state commits did not modify that executable boundary.

## Observed local result

The user pulled the current `main` checkout and reported:

```text
Ran 294 tests in 0.064s

OK
```

This is the complete repository discovery result containing the new Step 5B tests and existing release/upstream-source/package-interface regressions.

The exact focused-command summary was not supplied and is not invented. The complete passing suite is sufficient to close the same deterministic behavior, so no redundant focused rerun is required solely for status bookkeeping.

## Behavior established

Validated behavior includes:

- exact `refs/tags/{requested_tag}` identity;
- lightweight tag → direct commit;
- annotated tag → tag-object peeling;
- nested annotated tags;
- explicit peel-depth bound;
- cycle detection;
- unsupported Git object type handling;
- malformed/missing/acquisition failures;
- preserved direct tag object versus final resolved commit identity;
- shared exact tag-reference parsing with `GitHubReleaseClient` without moving release-client responsibility into Step 5B.

## Meaning limit

This validation establishes tag-to-commit identity behavior only. It does not establish:

- a changelog path;
- exact repository-file acquisition at the resolved commit;
- `TaggedChangelogEvidence`;
- Step 1 interval authority from live acquisition;
- semantic support-drop extraction;
- target relevance, compatibility, safety, or recommendation.
