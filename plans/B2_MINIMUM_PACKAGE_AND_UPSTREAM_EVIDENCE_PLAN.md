# B2 Minimum Package and Upstream Evidence Plan

**Owner:** Ali Rajabi  
**Parent gate:** [`B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)  
**Parent route:** [`UPGRADEPILOT_90_DAY_PLAN.md`](UPGRADEPILOT_90_DAY_PLAN.md)  
**Applicable generality control:** [`../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md)

## Purpose

Define the bounded product increment that turns a validated dependency identity into the
minimum official package and upstream evidence required for a first B2 decision.

```text
exact package + proposed version
→ official package/version identity
→ bounded release or upstream evidence
→ explicit evidence state and provenance
→ trusted input for a later transparent decision
```

This plan defines scope, sequence, proof, and stop conditions. It does not declare itself
active or record progress. `../MEMORY.md` alone selects it and states continuation.

## Product question

For a supported exact pinned Python dependency update:

> Can UpgradePilot acquire and validate the smallest official public evidence needed to
> confirm the proposed package version and expose the release-specific upstream claim that
> may affect the bounded maintainer action?

For the first supported control case, the material upstream question is whether the official
release source presents the exact proposed version as a drop-in bug-fix release. The
implementation must not encode that answer, package name, version, wording, or URL as product
logic.

## Responsibility horizon

The complete owning responsibility is **official Python package and release evidence
acquisition**, not one pytest page or one phrase.

The accepted method must have a credible path across public Python packages inside the
charter boundary. A package-specific URL, fixture-specific parser, exact phrase table, or
caller-supplied interpretation may be used only as an explicit test fixture or disposable
comparison—not as accepted product behavior.

This increment separates:

1. deterministic package/version identity and source acquisition;
2. release-source availability and provenance;
3. natural-language interpretation of an upstream claim.

Only the first two are automatically admitted by this plan. If natural-language
interpretation requires a consequential method choice, stop for a bounded comparison and
Ali approval before implementation.

## Required evidence states

The increment must preserve at least:

- `available` — official evidence for the exact package/version was acquired and validated;
- `package_not_found_or_inaccessible` — no accessible official package record was established;
- `version_not_found` — the package exists but the exact proposed version was not established;
- `identity_mismatch` — returned package or version identity contradicts the request;
- `source_unavailable` — the package/version exists but the required release-specific source cannot be acquired;
- `malformed_response` — HTTP success did not provide the required trustworthy shape;
- `unsupported_source` — available official material is outside the bounded supported format or authority rule;
- `unresolved_claim` — source text exists but the required release claim has not been interpreted reliably.

Transport failure, malformed successful response, absent evidence, unsupported format, and
unresolved meaning must remain distinct.

## Source-selection decision

Before implementation, compare the smallest credible source strategies.

### Candidate A — PyPI release metadata only

Potential value:

- official package index identity;
- exact version existence;
- release files and upload metadata;
- project URLs supplied by package metadata.

Limitation:

- ordinarily insufficient to establish a release-specific compatibility or drop-in claim.

### Candidate B — PyPI identity plus project-controlled release source

Potential value:

- PyPI establishes package/version identity;
- an official project-controlled release note, changelog, announcement, or tag supplies the
  release-specific claim.

Questions to resolve:

- how the official source is selected without package-specific hardcoding;
- how package metadata and upstream identity are bound;
- which source formats are supported first;
- how redirects, missing pages, and changed content are represented;
- which revision or retrieval time is preserved.

### Candidate C — Package-specific adapter or known URL

Disposition:

- rejected as accepted product behavior;
- permitted only as a fixture, manual oracle, or temporary comparison.

### Selection gate

Select a method only after documenting:

- the exact evidence claim it can establish;
- why the source is official enough for that claim;
- the variable input space it supports;
- failure and ambiguity behavior;
- security, maintenance, and replacement costs;
- the smallest proof that distinguishes it from fixture matching.

Create an ADR only if the selected method is durable and cross-cutting. A routine HTTP
endpoint choice inside an existing acquisition boundary does not require an ADR by default.

## Implementation sequence

### Step 1 — Freeze the trusted input contract

Use the existing proven dependency identity:

```text
normalized package name
raw package spelling
old version
proposed version
source requirements file
repository and exact PR head identity
```

Do not ask the caller to supply package URLs, release conclusions, or the final decision.

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

### Step 3 — Resolve an official release-specific source

Using the selected generalizable source strategy:

- identify the project-controlled source;
- bind it to the package and proposed version as strongly as the source permits;
- acquire read-only public content;
- preserve source locator and retrieval or revision context;
- return unavailable, mismatched, unsupported, or unresolved states instead of guessing.

### Step 4 — Decide whether semantic interpretation is admitted

If the decision requires interpreting release prose:

1. state the exact structured claim required by the transparent decision;
2. compare the simplest credible baseline and alternatives across the owning responsibility;
3. preserve attributed-source authority and grounding;
4. reject phrase enumeration or exact fixture wording as the product method;
5. obtain Ali approval before adding a consequential model or semantic method.

The acquisition increment may stop with `unresolved_claim` if a trustworthy interpretation
method is not yet admitted.

### Step 5 — Integrate without producing the final recommendation

Wire package/upstream evidence into the command path only far enough to expose:

- evidence status;
- exact package and version identity;
- official source and provenance;
- release-specific source availability;
- any trusted structured claim, when separately admitted;
- explicit unresolved or unavailable reasons.

Do not produce the final maintainer recommendation in this plan. That belongs to the later
transparent-decision increment after this evidence boundary is proven.

## Expected source boundaries

Names may change if the responsibility comparison justifies a simpler arrangement, but the
implementation should preserve these boundaries:

```text
package acquisition       official index/package/version identity
upstream acquisition      project-controlled release source
claim interpretation      optional separately admitted semantic transformation
CLI                        execution order and concise presentation
```

Do not place package HTTP parsing, upstream source selection, prose interpretation, and
recommendation policy into one broad CLI function.

## Deterministic proof

Tests must cover the smallest credible set of:

1. exact package/version success;
2. normalized-name variation that preserves identity;
3. exact version absent while the package exists;
4. returned identity mismatch;
5. malformed successful response;
6. ambiguous `404` or inaccessible source;
7. release-specific source unavailable;
8. unsupported source format;
9. no package-specific hardcoded answer;
10. no final recommendation from acquisition evidence alone.

Controlled responses establish deterministic behavior. A separately identified live
read-only run is required to establish live acquisition for one supported case.

## Acceptance evidence

The increment passes only when:

- the source-selection method is accepted;
- exact package/version identity is acquired without fixture hardcoding;
- official release-source availability is represented honestly;
- all required evidence states are tested;
- a safe live supported case succeeds or fails in an accurately classified way;
- the output makes no compatibility, safety, or recommendation claim beyond acquired and
  separately trusted evidence;
- no unapproved runtime dependency, model, service, persistence layer, or target mutation is
  introduced.

## Stop line

Stop this plan when trusted package/version evidence and bounded official release-source
evidence are exposed to the product path.

Do not continue here into:

- final recommendation policy;
- broad natural-language release-note understanding without separate admission;
- advisory or vulnerability analysis;
- repository-wide usage analysis;
- indirect CI expansion unrelated to this evidence question;
- persistence or replay infrastructure;
- B3 source-robustness breadth;
- B4 general decision-support expansion.

## Maintenance

Change this plan only when its responsibility, source-selection decision, evidence states,
proof obligations, or stop line changes. Do not record progress, latest commits, blockers, or
continuation here.