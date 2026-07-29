# B2 Dependency Version Change Evidence — Naming Correction and Decision Cluster 1

**Local timestamp:** 2026-07-29 22:13 +03:30  
**Route:** B2 — Public PR vertical slice  
**Selected responsibility:** Establish one trusted dependency version change from supported dependency files  
**Result:** First architecture cluster approved; project-wide naming clarity rule added; no product source or tests changed

## Why this record exists

During the first architecture discussion, Ali identified that several technically valid project terms were difficult to recall or map quickly to their actual function.

Examples included:

```text
canonical contract
provenance
PinnedDependencyChange
ExactPinDependencyInterpreter
interpreter
reconciler
```

The problem was not lack of effort or beginner status. The names imposed unnecessary project-specific decoding. A learning-by-building flagship should reduce that cognitive cost where clearer domain language exists.

## Naming decision

Ali directed UpgradePilot to establish a project-wide rule that names and titles should bring their closest practical meaning and function to mind with minimal extra explanation.

Created the accepted controlling specification:

```text
docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md
```

Commit:

```text
06caa57eb91a228cd60d6cef2a2c34a0d4211bc7
```

The rule requires:

- concrete responsibility-revealing names;
- action-plus-object function names;
- fact-revealing data type names;
- one primary term per concept;
- avoidance of broad labels when a clearer name exists;
- plain-language treatment of specialist terms;
- a recall test before ADR, source, CLI, or contract names are frozen;
- active-file correction without rewriting historical records merely for stylistic consistency.

## Clear dependency evidence vocabulary

Preferred vocabulary for this responsibility:

```text
DependencyVersionChange
→ trusted record that one package changed from one exact version to another

ExtractedDependencyVersionChange
→ possible change extracted from one supported dependency file

DependencyChangeSourceEvidence
→ exact file, revision, blob, and extraction method supporting the change

extract_exact_requirement_changes
→ read exact package==version patch changes

extract_uv_lock_changes
→ compare exact base/head uv.lock package records

compare_extracted_dependency_changes
→ check whether extracted changes agree, conflict, or contain several package changes
```

Avoid using these as the primary new names where the clearer wording above works:

```text
canonical contract
interpreter
reconciler
provenance
foundation
```

Standard technical terms may still be taught when useful, but they must not become opaque project vocabulary.

## Plan naming correction

Created the clearer active plan:

```text
plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md
```

Commit:

```text
a95caa35e7483fca3c566e66247d99a1226ee460
```

The title states the exact responsibility: evidence that one dependency version changed.

The former path was converted into a non-controlling pointer so historical links remain usable:

```text
plans/B2_DEPENDENCY_CHANGE_INTERPRETATION_FOUNDATION_PLAN.md
```

Pointer commit:

```text
1ac9d66d1209ce9faa746b8f44221672c9118f25
```

## Decision cluster 1 approved

Ali approved the first connected architecture cluster.

### 1. Trusted downstream record

Use one representation-independent:

```text
DependencyVersionChange
```

It contains the trusted package identity, exact old/proposed version strings, and supporting source evidence.

It does not imply dependency role, target usage, CI consumption, compatibility, safety, or maintainer action.

### 2. Source-specific extraction and comparison

Use:

```text
supported dependency file
→ clearly named extraction function
→ ExtractedDependencyVersionChange or source problem

all extracted changes and recognized source problems
→ compare_extracted_dependency_changes
→ DependencyVersionChange or explicit problem
```

Do not use a giant multi-format parser or case-specific CLI branches.

### 3. Exactly-one B2 boundary

B2 supports exactly one dependency version change.

Several package changes produce:

```text
multiple_dependency_version_changes
```

No title, order, package familiarity, or other heuristic may choose one.

### 4. Equivalent extracted changes

Same normalized package, exact raw old version, and exact raw proposed version:

```text
→ one DependencyVersionChange
→ all supporting source evidence attached
```

Agreement does not create stronger claims about role, CI, compatibility, or safety.

### 5. Conflicting extracted changes

Different package/version transitions produce:

```text
conflicting_dependency_version_changes
```

No file-format priority silently chooses one answer.

### 6. Recognized malformed or incomplete evidence

A changed file recognized as a supported dependency format cannot be ignored merely because another file produces a convenient change.

```text
one valid extracted change
+
one recognized malformed, unavailable, incomplete, or too-large supported dependency file
→ no trusted DependencyVersionChange
```

This conservative rule prevents hidden or contradictory dependency changes from reaching downstream evidence stages.

## Historical and active naming boundary

Do not mass-rewrite dated historical records or validated source merely to modernize vocabulary.

Apply the naming rule to:

- the selected plan;
- the future ADR;
- new or changed source and tests;
- public CLI output;
- active controlling documents when their meaning or references are touched.

The existing `PinnedDependencyChange` source type remains actual validated behavior until the approved refactor replaces it through tests. Documentation must distinguish the existing implementation name from the future shared record name.

## No implementation performed

No product source, tests, runtime dependency, CLI behavior, or target repository was changed.

No ADR was created because the remaining dependency-file, identity, CI, acquisition, and final source-name choices are not yet resolved.

## Next coherent discussion

Proceed to the supported dependency-file rules:

1. which exact requirement and constraint paths are eligible;
2. why arbitrary changed-file scanning is risky;
3. how nested conventional paths should be handled;
4. `uv.lock` duplicate package identities and modified-file boundary.

Do not reopen Decision Cluster 1 unless later evidence exposes a concrete contradiction.