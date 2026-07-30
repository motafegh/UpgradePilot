# B2 Minimum Package and Upstream Evidence Plan

**Owner:** Ali Rajabi  
**Parent gate:** [`B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)  
**Parent route:** [`UPGRADEPILOT_90_DAY_PLAN.md`](UPGRADEPILOT_90_DAY_PLAN.md)  
**Dependency input plan:** [`B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)  
**Naming control:** [`../docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md)  
**Generality control:** [`../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md)

## Purpose

Turn one trusted `DependencyVersionChange` into the minimum official Python package and upstream evidence required for a bounded B2 decision.

```text
trusted package + exact raw old/proposed version strings
→ PEP 440 validation for Python package semantics
→ official package/version identity
→ bounded upstream source evidence
→ explicit evidence state and exact source identity
→ trusted input for later relevance and decision work
```

This plan defines scope, sequence, proof, and stop conditions. It does not declare itself active or record progress. `../MEMORY.md` alone selects it and states continuation.

## Product question

For one trusted exact-text dependency version change:

> Can UpgradePilot validate the old and proposed values as Python package versions, acquire the smallest official public evidence needed to confirm the proposed package release, and expose the upstream evidence that may affect a bounded maintainer action?

The implementation must not encode a control-case answer, package name, version, wording, source representation, or URL as product logic.

## Responsibility horizon

The complete responsibility is **official Python package and upstream evidence acquisition**, not one pytest page, one lockfile, one requirements file, or one phrase.

This increment separates:

1. exact dependency-file observation supplied by the dependency version change plan;
2. Python package version validation and ordering under PEP 440;
3. official package/version identity and source acquisition;
4. upstream-source availability and exact identity;
5. natural-language interpretation of an upstream claim.

Only responsibilities 2–4 are automatically admitted here. If natural-language interpretation requires a consequential method choice, stop for a bounded comparison and Ali approval before implementation.

Dependency-file representation explains how the textual transition was proven. It does not change the official package lookup question once the package and version inputs are admitted.

## Trusted input boundary

The plan consumes one trusted `DependencyVersionChange` containing at least:

```text
raw package spelling
normalized package name
exact raw old version string
exact raw proposed version string
exact PR repository/base/head identity
dependency change source evidence
```

The input must not require a requirements-file-specific `source_file` meaning.

Change-evidence paths remain available for traceability, but they do not establish:

- direct or transitive dependency role;
- install command;
- CI consumption;
- target usage;
- compatibility or safety.

No caller may supply package URLs, release conclusions, or the final decision.

## Selected Python version validation boundary

Dependency-file extraction preserves exact text and does not perform PEP 440 validation or ordering.

This plan begins Python package version interpretation before official package release lookup and crossed-version ordering.

Use:

```text
packaging.version.Version
```

for both old and proposed version strings.

The validation result must preserve:

```text
raw old version string
raw proposed version string
parsed old Version
parsed proposed Version
```

where parsing succeeds.

If either raw value cannot be parsed under the selected PEP 440 implementation, return:

```text
invalid_python_package_version
```

This result means:

> A textual dependency version change was established, but at least one value cannot be used as a Python distribution version for package release lookup or ordering.

It must not be rewritten as “no dependency change.”

The package/upstream path must also distinguish:

```text
proposed version later than old version
→ eligible for forward crossed-version work

proposed version equal to old version under PEP 440
→ equivalent_python_package_versions

proposed version earlier than old version
→ dependency_version_not_forward
```

The exact raw strings remain attached even when PEP 440 considers different spellings equivalent. Dependency-file source agreement remains based on exact observed text; PEP 440 normalization must not rewrite source evidence.

The `packaging` runtime dependency, exact bounds, and installation proof remain separately controlled before implementation.

## Required evidence states

The increment must preserve at least:

- `available` — official evidence for the exact package/version was acquired and validated;
- `invalid_python_package_version` — old or proposed text cannot be parsed under the selected PEP 440 method;
- `equivalent_python_package_versions` — raw strings differ but parse to the same PEP 440 version;
- `dependency_version_not_forward` — proposed version orders before the old version;
- `package_not_found_or_inaccessible` — no accessible official package record was established;
- `version_not_found` — the package exists but the exact proposed version was not established;
- `identity_mismatch` — returned package or version identity contradicts the request;
- `source_unavailable` — the package/version exists but required upstream evidence cannot be acquired;
- `malformed_response` — HTTP success did not provide the required trustworthy shape;
- `unsupported_source` — available official material is outside the bounded source or authority rule;
- `unresolved_claim` — source text exists but the required upstream claim has not been interpreted reliably.

Transport failure, invalid version semantics, malformed successful response, absent evidence, unsupported format, and unresolved meaning must remain distinct.

An unsupported or conflicting dependency-change result must not reach this plan as trusted input.

## Accepted source strategy

```text
PyPI exact-release identity
+
separately validated project-controlled upstream source evidence
```

The two sources have different authority and must not be collapsed.

### PyPI role

PyPI release metadata is accepted for:

- official Python distribution identity;
- exact proposed version existence;
- release-file presence and registry source identity;
- publisher-supplied project-link candidates.

PyPI metadata alone is insufficient to establish compatibility, safety, a drop-in claim, or upstream meaning. A PyPI `project_urls` entry is a discovery candidate, not proof that its target is authoritative for the required claim.

### Project-controlled upstream role

A separately validated project-controlled release note, changelog, announcement, or tag must supply upstream evidence. The acquisition rule must establish, as strongly as the supported source permits:

- that the source is controlled by the project associated with the package;
- the package/version or crossed-version interval to which the source applies;
- that acquired content and locator are preserved with retrieval or revision context;
- that missing, redirected, mismatched, unsupported, or ambiguous material remains explicit.

An exact proposed-version release body may be sufficient for some claims. A downstream bounded plan may require complete old-version-exclusive/proposed-version-inclusive evidence when an intermediate release carries the material change.

### Rejected product method

A package-specific URL, known release page, exact dependency representation, exact wording, or caller-supplied conclusion remains rejected as product behavior. Such material may appear only as a controlled fixture, manual oracle, or disposable comparison.

## Implementation sequence

### Step 1 — Validate the trusted dependency input

Require one trusted `DependencyVersionChange`.

Validate:

- normalized and raw package identity;
- non-empty exact raw old and proposed version strings;
- exact PR identity;
- dependency source evidence is available and non-conflicting;
- source representation remains evidence rather than package lookup policy.

Do not reinterpret lockfiles, requirements files, or dependency graphs in this plan.

### Step 2 — Validate Python package versions

Parse both exact raw strings with the selected `packaging.version.Version` dependency.

Preserve raw and parsed forms. Return explicit invalid, equivalent, or non-forward results rather than guessing.

Do not begin official release interval work without a valid forward old/proposed pair.

### Step 3 — Acquire official package/version evidence

Acquire the smallest official package record for the exact proposed version.

Validate:

- requested normalized package identity against returned identity;
- exact proposed version presence;
- required response shape and types;
- bounded response size;
- source URL and retrieval context;
- no silent fallback to a different version.

Return immutable trusted evidence or an explicit bounded evidence state.

### Step 4 — Resolve an official upstream source

Using the selected generalizable source strategy:

- identify the project-controlled source;
- bind it to the package and relevant version or interval as strongly as the source permits;
- acquire read-only public content;
- preserve source locator and retrieval or revision context;
- return unavailable, mismatched, unsupported, conflicting, or unresolved states instead of guessing.

### Step 5 — Decide whether semantic interpretation is admitted

When the decision requires interpreting release prose:

1. state the exact structured claim required by the downstream decision;
2. compare the simplest credible baseline and alternatives across the complete responsibility;
3. preserve attributed-source identity and grounding;
4. reject phrase enumeration or exact fixture wording as the product method;
5. obtain Ali approval before adding a consequential model or semantic method.

The acquisition increment may stop with `unresolved_claim` when a trustworthy interpretation method is not yet admitted.

### Step 6 — Integrate without producing the final recommendation

Expose only:

- dependency evidence status and source identity;
- exact raw and parsed old/proposed version identity;
- official package source and identity;
- upstream-source availability and interval binding where required;
- any separately trusted structured claim;
- explicit invalid, unresolved, conflicting, or unavailable reasons.

Do not produce the final maintainer recommendation in this plan.

## Expected source boundaries

```text
dependency change evidence   exact textual package/version change and source evidence
Python version validation    PEP 440 parsing and ordering
package acquisition          official index/package/version identity
upstream acquisition         project-controlled upstream source
claim interpretation         optional separately admitted semantic transformation
CLI                          execution order and concise presentation
```

Do not place dependency-file parsing, version semantics, package HTTP parsing, upstream source selection, prose interpretation, and recommendation policy into one broad CLI function.

## Deterministic proof

Tests must cover:

1. trusted dependency input from an exact requirements representation;
2. equivalent trusted input from a structured lock representation;
3. valid raw old/proposed PEP 440 versions;
4. invalid old version;
5. invalid proposed version;
6. raw strings that parse to equivalent PEP 440 versions;
7. proposed version earlier than old version;
8. exact package/version success without representation-specific lookup behavior;
9. normalized-name variation preserving identity;
10. exact proposed version absent while the package exists;
11. returned identity mismatch;
12. malformed successful response;
13. ambiguous `404` or inaccessible source;
14. upstream source unavailable;
15. unsupported source format;
16. conflicting or unsupported dependency input cannot reach package acquisition;
17. no package-, representation-, or fixture-specific hardcoded answer;
18. no final recommendation from acquisition evidence alone.

Controlled responses establish deterministic behavior. A separately identified live read-only run is required to establish live acquisition for one supported case.

## Acceptance evidence

The increment passes only when:

- `packaging` admission and exact bounds are accepted and behavior-validated;
- raw and parsed version identities remain distinguishable;
- invalid, equivalent, and non-forward version states are tested;
- trusted dependency inputs from admitted representations reach equivalent package lookup behavior;
- exact package/version identity is acquired without fixture hardcoding;
- official upstream-source availability is represented honestly;
- all required evidence states are tested;
- a safe live supported case succeeds or fails in an accurately classified way;
- output makes no compatibility, safety, or recommendation claim beyond acquired and separately trusted evidence;
- no unapproved model, service, persistence layer, or target mutation is introduced.

## Stop line

Stop this plan when validated Python package version identity, trusted package/release evidence, and bounded official upstream-source evidence are exposed to the product path from one trusted `DependencyVersionChange`.

Do not continue here into:

- dependency-file parsing or extracted-change comparison;
- final recommendation policy;
- broad natural-language release-note understanding without separate admission;
- advisory or vulnerability analysis;
- repository-wide usage analysis;
- indirect CI expansion unrelated to this evidence question;
- persistence or replay infrastructure;
- B3 source-robustness breadth;
- B4 general decision-support expansion.

## Maintenance

Change this plan only when its responsibility, trusted input boundary, Python version method, source-selection decision, evidence states, proof obligations, or stop line changes. Do not record progress, latest commits, blockers, or continuation here.