# B2 Minimum Package and Upstream Evidence Plan

**Owner:** Ali Rajabi  
**Parent gate:** [`B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)  
**Parent route:** [`UPGRADEPILOT_90_DAY_PLAN.md`](UPGRADEPILOT_90_DAY_PLAN.md)  
**Applicable generality control:** [`../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md)

## Purpose

Define the bounded product increment that turns a trusted canonical dependency-version change into the minimum official package and upstream evidence required for a first B2 decision.

```text
canonical package + old version + proposed version
→ official package/version identity
→ bounded release or upstream evidence
→ explicit evidence state and provenance
→ trusted input for a later transparent decision
```

This plan defines scope, sequence, proof, and stop conditions. It does not declare itself active or record progress. `../MEMORY.md` alone selects it and states continuation.

## Product question

For one trusted canonical exact-version Python dependency update:

> Can UpgradePilot acquire and validate the smallest official public evidence needed to confirm the proposed package version and expose the upstream evidence that may affect a bounded maintainer action?

The implementation must not encode a control-case answer, package name, version, wording, source representation, or URL as product logic.

## Responsibility horizon

The complete owning responsibility is **official Python package and upstream evidence acquisition**, not one pytest page, one lockfile, one requirements file, or one phrase.

The accepted method must have a credible path across public Python packages inside the charter boundary. A package-specific URL, fixture-specific parser, exact phrase table, caller-supplied interpretation, or dependency-source-specific downstream contract may be used only as an explicit test fixture or disposable comparison—not as accepted product behavior.

This increment separates:

1. trusted canonical dependency identity supplied by the dependency-change foundation;
2. deterministic package/version identity and source acquisition;
3. upstream-source availability and provenance;
4. natural-language interpretation of an upstream claim.

Only the second and third are automatically admitted by this plan. If natural-language interpretation requires a consequential method choice, stop for a bounded comparison and Ali approval before implementation.

The dependency representation establishes how the transition was proven. It does not change the official package lookup question once the canonical package/version identity is trusted.

## Trusted input boundary

The plan consumes a representation-neutral dependency result containing at least:

```text
raw package spelling
normalized package name
old version
proposed version
exact PR repository/base/head identity
dependency-change evidence provenance
```

The input must not require a requirements-file-specific `source_file` meaning.

Change-evidence paths are preserved for traceability, but they do not establish:

- direct or transitive dependency role;
- install command;
- CI consumption;
- target usage;
- compatibility or safety.

No caller may supply package URLs, release conclusions, or the final decision.

## Required evidence states

The increment must preserve at least:

- `available` — official evidence for the exact package/version was acquired and validated;
- `package_not_found_or_inaccessible` — no accessible official package record was established;
- `version_not_found` — the package exists but the exact proposed version was not established;
- `identity_mismatch` — returned package or version identity contradicts the request;
- `source_unavailable` — the package/version exists but the required upstream source cannot be acquired;
- `malformed_response` — HTTP success did not provide the required trustworthy shape;
- `unsupported_source` — available official material is outside the bounded supported format or authority rule;
- `unresolved_claim` — source text exists but the required release claim has not been interpreted reliably.

Transport failure, malformed successful response, absent evidence, unsupported format, and unresolved meaning must remain distinct.

An unsupported or conflicting dependency-change result must not reach this plan as trusted input.

## Accepted source strategy

The accepted product-level strategy is:

```text
PyPI exact-release identity
+ separately validated project-controlled upstream source evidence
```

The two sources have different authority and must not be collapsed.

### PyPI role

PyPI release metadata is accepted for:

- official Python distribution identity;
- exact proposed version existence;
- release-file presence and registry provenance;
- publisher-supplied project-link candidates.

PyPI metadata alone is insufficient to establish compatibility, safety, a drop-in claim, or upstream meaning. A PyPI `project_urls` entry is a discovery candidate, not proof that its target is authoritative for the required claim.

### Project-controlled upstream role

A separately validated project-controlled release note, changelog, announcement, or tag must supply upstream evidence. The resolver must establish, as strongly as the supported source permits:

- that the source is controlled by the project associated with the package;
- the package/version or crossed-version interval to which the source applies;
- that acquired content and locator are preserved with retrieval or revision context;
- that missing, redirected, mismatched, unsupported, or ambiguous material remains explicit.

The initial supported source format may be narrow, but its selection and binding rule must be generalizable across the admitted public Python-package domain rather than encoded for one package.

An exact proposed-version release body may be sufficient for some claims. A downstream bounded plan may require complete old-version-exclusive/proposed-version-inclusive change evidence when an intermediate release can carry the material change.

### Rejected product method

A package-specific URL, adapter, known release page, exact dependency representation, or exact wording remains rejected as accepted runtime behavior. Such material may appear only as a controlled fixture, manual oracle, or disposable comparison.

### Decision rationale and proof gate

The strategy is accepted because it separates registry identity from upstream authority, keeps package/version validation deterministic, and leaves semantic interpretation outside the acquisition boundary until separately admitted.

Any concrete upstream resolver must still document and prove:

- the exact evidence claim it can establish;
- why the selected source is official enough for that claim;
- the variable input space it supports;
- failure and ambiguity behavior;
- security, maintenance, and replacement costs;
- the smallest proof that distinguishes it from fixture matching.

Create an ADR only if the selected resolver method is durable and cross-cutting. A routine HTTP endpoint choice inside an existing acquisition boundary does not require an ADR by default.

## Implementation sequence

### Step 1 — Validate the canonical dependency input

Require one trusted representation-neutral dependency transition.

Validate:

- normalized and raw package identity;
- non-empty exact old and proposed versions;
- versions differ;
- exact PR identity is preserved;
- dependency evidence is available and non-conflicting;
- source representation provenance is retained without controlling package lookup semantics.

Do not reinterpret lockfiles, requirements files, or dependency graphs in this plan.

### Step 2 — Add official package/version acquisition

Acquire the smallest official package record for the exact proposed version.

Validate:

- requested normalized package identity against returned identity;
- exact proposed version presence;
- required response shape and types;
- bounded response size;
- source URL and retrieval context;
- no silent fallback to a different version.

Return immutable trusted evidence or an explicit bounded evidence state.

### Step 3 — Resolve an official upstream source

Using the selected generalizable source strategy:

- identify the project-controlled source;
- bind it to the package and relevant version or interval as strongly as the source permits;
- acquire read-only public content;
- preserve source locator and retrieval or revision context;
- return unavailable, mismatched, unsupported, conflicting, or unresolved states instead of guessing.

### Step 4 — Decide whether semantic interpretation is admitted

If the decision requires interpreting release prose:

1. state the exact structured claim required by the transparent decision;
2. compare the simplest credible baseline and alternatives across the owning responsibility;
3. preserve attributed-source authority and grounding;
4. reject phrase enumeration or exact fixture wording as the product method;
5. obtain Ali approval before adding a consequential model or semantic method.

The acquisition increment may stop with `unresolved_claim` if a trustworthy interpretation method is not yet admitted.

### Step 5 — Integrate without producing the final recommendation

Wire package/upstream evidence into the command path only far enough to expose:

- dependency evidence status and provenance;
- exact package and old/proposed version identity;
- official package source and provenance;
- upstream-source availability and interval binding where required;
- any trusted structured claim, when separately admitted;
- explicit unresolved, conflicting, or unavailable reasons.

Do not produce the final maintainer recommendation in this plan. That belongs to the later transparent-decision increment after this evidence boundary is proven.

## Expected source boundaries

Names may change if the responsibility comparison justifies a simpler arrangement, but the implementation should preserve these boundaries:

```text
dependency-change foundation  canonical package/version identity and representation provenance
package acquisition           official index/package/version identity
upstream acquisition          project-controlled upstream source
claim interpretation          optional separately admitted semantic transformation
CLI                           execution order and concise presentation
```

Do not place dependency representation parsing, package HTTP parsing, upstream source selection, prose interpretation, and recommendation policy into one broad CLI function.

## Deterministic proof

Tests must cover the smallest credible set of:

1. canonical dependency input from an exact-pin representation;
2. equivalent canonical dependency input from a structured lock representation;
3. exact package/version success for both without representation-specific lookup behavior;
4. normalized-name variation that preserves identity;
5. exact version absent while the package exists;
6. returned identity mismatch;
7. malformed successful response;
8. ambiguous `404` or inaccessible source;
9. upstream source unavailable;
10. unsupported source format;
11. conflicting or unsupported dependency input cannot reach package acquisition as trusted identity;
12. no package-, representation-, or fixture-specific hardcoded answer;
13. no final recommendation from acquisition evidence alone.

Controlled responses establish deterministic behavior. A separately identified live read-only run is required to establish live acquisition for one supported case.

## Acceptance evidence

The increment passes only when:

- the source-selection method is accepted;
- trusted canonical dependency inputs from admitted representations reach equivalent package lookup behavior;
- exact package/version identity is acquired without fixture hardcoding;
- official upstream-source availability is represented honestly;
- all required evidence states are tested;
- a safe live supported case succeeds or fails in an accurately classified way;
- the output makes no compatibility, safety, or recommendation claim beyond acquired and separately trusted evidence;
- no unapproved runtime dependency, model, service, persistence layer, or target mutation is introduced.

## Stop line

Stop this plan when trusted package/version evidence and bounded official upstream-source evidence are exposed to the product path from one canonical dependency input contract.

Do not continue here into:

- dependency representation parsing or reconciliation;
- final recommendation policy;
- broad natural-language release-note understanding without separate admission;
- advisory or vulnerability analysis;
- repository-wide usage analysis;
- indirect CI expansion unrelated to this evidence question;
- persistence or replay infrastructure;
- B3 source-robustness breadth;
- B4 general decision-support expansion.

## Maintenance

Change this plan only when its responsibility, trusted input contract, source-selection decision, evidence states, proof obligations, or stop line changes. Do not record progress, latest commits, blockers, or continuation here.
