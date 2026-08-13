# B2 Target-Environment Evidence Review Addendum

**Date:** 2026-08-13  
**Type:** Dated evidence-design working memory  
**Live-state authority:** `../MEMORY.md` only  
**Extends:** `2026-08-13_B2-product-simulation-review-summary.md`

## Purpose

Preserve the reasoning that follows from the targeted `product-simulation/` review before any further target-environment implementation.

The current product gap is:

```text
exact repository-owned observations
→ interpreted environment facts
→ sufficient / partial / conflicting evidence judgment
→ exact wheel compatibility only when justified
→ artifact applicability
```

The review did not accept a new runtime schema. It identified design requirements and open choices.

## Main findings

### 1. Required facts come from the owned proposition

The evidence path remains:

```text
owned technical claim
→ wheel-serviceability semantics
→ required target facts
→ evidence capable of establishing those facts
```

Do not begin from a generic repository-file checklist and manufacture a claim from whatever is found.

### 2. Environment evidence is proposition-specific

A source can be strong for one claim and weak for another.

S008 demonstrates this directly:

- the Dockerfile establishes Python-3.6 repository context;
- it does not prove that OpenCV is installed through that container;
- installation documentation establishes a different full-requirements path;
- CI installs requirements on Ubuntu but does not prove Python-3.6 artifact-selection coverage.

Evidence therefore needs scope, not only a value.

### 3. Partial evidence must remain partial

Buildtest/urllib3 C203 proves an externally managed HPC environment path but does not establish the exact historical native SSL implementation/version needed for the upstream boundary.

The correct state remains:

```text
environment pathway established
+ relevant upstream requirement established
+ exact activation unresolved
```

The target-environment path must therefore be able to preserve known and unknown dimensions without guessing a complete wheel tag set.

### 4. Multiple target environments must preserve identity

S005 and other matrix evidence show that one repository can legitimately exercise multiple environments.

Do not flatten:

```text
Environment A → tags A
Environment B → tags B
```

into one repository-wide tag union if that destroys which compatibility facts belong to which environment.

A union can incorrectly hide that one particular old environment lost its prebuilt path merely because a different environment can use a new wheel.

The current `TargetWheelCompatibilityEvidence` should therefore be treated only as evidence for one already-established environment, not a repository-wide aggregate.

### 5. Different scopes are not automatically conflicts

Docker, CI, installation docs, package metadata, and deployment/runtime evidence may describe different paths.

Before classifying evidence as conflicting, preserve enough identity to ask whether the observations refer to:

```text
same repository/revision
same environment/path
same dependency identity
same proposition
```

Different-scope evidence may remain separately true.

### 6. Environment formation can require more than Python + OS

S007 adds real pressure from CUDA family, local/build-version identity, package-index choice, coordinated package versions, and documented installation intent.

This does not justify a universal environment object. It does reject the assumption that `python_version + os` is always sufficient.

Required dimensions remain mechanism- and proposition-relative.

### 7. CI relevance is environment-branch specific

Across S005/S006/S008:

```text
CI exists
!= relevant CI

package installs
!= exact changed identity exercised

same dependency exercised
!= implicated environment/artifact branch exercised
```

Any future CI-derived environment evidence must retain enough runner/interpreter/dependency identity for the claim being made.

### 8. Static evidence can justify stopping

S004/S007/S008 show that deeper execution is not automatically better.

For S008, source-build execution would answer a different proposition from binary artifact availability.

Once the owned proposition is resolved, deeper environment reconstruction/build execution must not activate automatically.

## Pressure on current Increment 2

The existing artifact applicability evaluator can remain a bounded downstream consumer:

```text
one exact established environment
+ complete supported Tag set for that environment
→ old/new compatible-wheel evaluation
```

But real acquisition should not jump directly from arbitrary raw repository files into that contract.

The design direction now worth debating is:

```text
raw exact repository evidence
→ scoped provenance-carrying environment facts
→ proposition-relative sufficiency check
    ├─ sufficient → exact wheel-compatibility evidence
    └─ insufficient/conflicted → explicit unresolved/problem
→ artifact applicability evaluator
```

This is evidence pressure for an intermediate responsibility, not yet an accepted class/module/schema.

## Requirements for the next design decision

Any first implementation should be evaluated against:

1. exact repository/revision provenance;
2. evidence scope;
3. partial known/unknown facts;
4. per-environment identity;
5. disciplined evidence composition;
6. same-scope conflict handling;
7. proposition-relative sufficiency;
8. honest unresolved state;
9. stopping once the owned question is resolved.

## Still deliberately open

Do not treat the following as decided yet:

- first evidence family to implement;
- exact intermediate data structure;
- Docker/container vs CI vs another first acquisition source;
- derivation rules from partial facts to exact `packaging.tags.Tag` compatibility;
- breadth of multi-environment support in the first slice;
- final genuine-conflict handling;
- any universal environment reconstruction architecture.

## Current path

```text
keep current downstream artifact applicability boundary
→ discuss the smallest explicit environment-fact responsibility
→ choose one real evidence shape for the first bounded implementation
→ test it against S008 + C203 + multi-environment pressure
→ implement acquisition/interpretation without universal claims
→ derive exact compatibility only when justified
→ otherwise preserve unresolved/problem
→ later compare the completed second loop with Python support for earned abstraction
```

No new simulation case is currently justified solely to rediscover broad evidence shapes already represented in the corpus.
