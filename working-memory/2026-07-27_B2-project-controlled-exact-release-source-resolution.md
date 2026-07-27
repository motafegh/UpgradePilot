# B2 Project-Controlled Exact-Release Source Resolution

**Date:** 2026-07-27  
**Operation:** Select the smallest credible generalizable rule for resolving a project-controlled source that applies to an exact proposed Python package release  
**Starting revision:** `9c01c02f21828e2727e5ae53f5f7eb17fadefb37`  
**Status:** Active investigation

## Objective

Design the upstream-source boundary required by the selected B2 package and upstream evidence plan.

The investigation must determine how UpgradePilot can move from validated PyPI package/version evidence and publisher-supplied project-link candidates to a separately validated source that:

- is associated with and controlled by the package's upstream project;
- applies to the exact proposed version;
- can be acquired through a bounded public read-only operation;
- preserves locator, retrieval or revision context, and explicit uncertainty;
- does not interpret release prose or make a compatibility, safety, or merge recommendation.

## Starting product boundary

Already behavior-validated:

```text
public PR identity
→ exact pinned dependency change
→ exact-head CI authority
→ exact PyPI package/version identity
→ publisher-supplied project-link candidates
```

Not yet established:

```text
project-controlled source
+ exact-release binding
+ bounded upstream content acquisition
```

## Exact design question

> What is the smallest credible and generalizable authority chain that lets UpgradePilot establish that an acquired public source is controlled by the project associated with a PyPI package and applies to the exact proposed version?

## Preliminary claim boundary

The resolver should establish only an acquisition and provenance claim of this form:

> A supported project-link candidate was bound to a project-controlled source, and the acquired source exposes a release record or version marker applying to the exact proposed version.

It must not establish:

- that the release is compatible with the target repository;
- that the release is safe;
- that release prose has a particular semantic meaning;
- that the dependency update should be merged, deferred, or blocked.

## Candidate strategy families to compare

1. **Repository release object** — bind a PyPI source/repository link to a supported repository host, then resolve an exact-version release object.
2. **Repository tag or ref** — bind the project repository and exact version to a tag/ref, preserving that a tag is identity evidence rather than release-note meaning.
3. **Project-controlled changelog or release-note page** — use a PyPI-supplied changelog/documentation candidate and locate an exact-version section under bounded format rules.
4. **Project-controlled repository changelog file** — acquire a changelog file at an exact tag/revision and locate an exact-version section.
5. **Package artifact metadata/content** — inspect whether official distribution artifacts can credibly bind the project and exact release to upstream release material without adding excessive scope.

## Comparison criteria

Each strategy must be evaluated for:

- package-to-project binding strength;
- exact-version binding strength;
- source-control or authority evidence;
- generality across admitted public Python packages;
- deterministic acquisition and validation;
- redirect and locator behavior;
- unavailable, mismatched, unsupported, and ambiguous states;
- security and maintenance burden;
- fit with the current GitHub, PyPI, and shared JSON-contract boundaries;
- minimum controlled tests and one live read-only proof;
- whether it creates a genuinely identical second consumer for PyPI's bounded body-reading mechanics.

## Investigation sequence

1. Inspect the current PyPI evidence object and selected B2 plan.
2. Review official PyPI/Core Metadata semantics for project URLs and release identity.
3. Review official repository-host release/tag semantics for candidate structured sources.
4. Test the control case against candidate strategies without encoding pytest-specific behavior.
5. Compare failure modes and source-authority limits.
6. Recommend one initial supported format and authority rule.
7. Present the proposed boundary, tradeoffs, evidence states, and proof plan to Ali.
8. Implement only after approval.

## Learning-by-building contract

During this investigation:

- explain the difference between discovery metadata, project association, source control, exact-version binding, and semantic interpretation;
- connect each proposed rule to concrete current source objects and future code responsibilities;
- expose assumptions and rejected alternatives rather than presenting only the final choice;
- keep the investigation bounded so architectural learning does not stall B2 momentum;
- do not create code until the authority rule is understood and approved.

## Non-goals

This investigation does not yet:

- implement the upstream resolver;
- integrate PyPI into the CLI;
- interpret release-note prose;
- produce a final maintainer recommendation;
- create a universal source framework, adapter registry, plugin system, or new runtime dependency;
- reorganize the package into subpackages.

## Current classification

**Active.** The evidence claim is bounded, but the first supported source format and authority chain have not yet been selected.
