# B2 Shared External-Source Foundation Investigation

**Date:** 2026-07-27  
**Operation:** Audit repeated acquisition and validation mechanics before adding another external source  
**Starting revision:** `4520f981d7c7e0ab9f716daab0773643405e1338`  
**Investigation record created:** `2c55c107a8e2a831f5f0b65747e4ba83910adc2e`  
**Status:** Active; bounded design available for approval

## Objective

Determine whether UpgradePilot now has enough repeated external-source behavior to justify a small shared foundation before implementing the project-controlled upstream-source resolver.

The goal is not to generalize every client. The goal is to remove proven repetition while preserving source-specific authority, identity, failure, and evidence semantics.

## Why this investigation exists now

UpgradePilot currently has:

- a shared GitHub REST/JSON foundation used by multiple GitHub clients;
- a separate PyPI exact-release client with its own bounded acquisition and JSON-contract helpers;
- an upcoming upstream-source resolver that may introduce another acquisition boundary.

One GitHub implementation alone did not justify a source-neutral abstraction. Two implemented boundaries plus a third planned boundary create a concrete duplication risk worth investigating before more code is added.

## Question

> What is the smallest shared external-source foundation that removes repeated mechanics without collapsing GitHub, PyPI, and upstream evidence into one generic client or erasing their different authority rules?

## Inventory findings

### Proven repeated mechanics

The current GitHub and PyPI boundaries both implement runtime checks for:

- required nested objects;
- required arrays;
- required non-empty strings;
- required integer and non-negative-integer values;
- rejecting booleans where JSON integers are required.

Both also inject HTTP sessions and timeouts for testing, catch Requests transport exceptions, decode JSON, and distinguish acquisition failure from an untrustworthy successful body.

### Similar-looking behavior that is not yet safely shareable

The HTTP layers are not equivalent:

- GitHub uses authentication and API-version headers; PyPI does not;
- GitHub currently raises `GitHubAcquisitionError` and `GitHubResponseError`; PyPI returns `PackageReleaseProblem` values;
- GitHub assigns GitHub-specific meanings to `404`, `403`, and `429`;
- PyPI performs a second package-level request after a release `404` to distinguish a missing version from an absent or inaccessible package;
- PyPI streams and caps response bodies; GitHub currently decodes successful JSON through its existing client boundary;
- the upcoming upstream source may be HTML, Markdown, raw text, a GitHub release object, or repository content rather than PyPI-shaped JSON.

These differences mean a universal external-source HTTP client would currently erase useful semantics or require a configuration framework larger than the duplicated code.

## Option comparison

### Option A — Keep every source completely separate

**Benefit:** no immediate refactor risk.  
**Cost:** a third source is likely to create another validator family and increase behavioral drift.  
**Disposition:** rejected as the default path because the JSON value-contract duplication is already proven.

### Option B — Extract only source-neutral contract primitives

Create a small module containing pure value validators such as:

- expect a JSON object;
- expect a JSON array;
- expect non-empty text;
- expect an integer while rejecting booleans;
- expect a non-negative integer.

Focused source modules would keep field lookup, source names, errors or result states, identity checks, HTTP classification, and evidence authority. Existing GitHub helpers may remain as compatibility wrappers that delegate to the neutral primitives; PyPI helpers may delegate and translate violations into `malformed_response`.

**Benefit:** removes proven duplication with a narrow testable abstraction while preserving source contracts.  
**Cost:** introduces one small indirection and requires regression tests.  
**Disposition:** recommended first refactor.

### Option C — Introduce a general external-source acquisition client

**Benefit:** could centralize sessions, headers, GET logic, body handling, JSON decoding, errors, and provenance.  
**Cost:** current sources have materially different HTTP, body, error, and authority semantics; the abstraction would require callbacks or configuration before the third source format is selected.  
**Disposition:** rejected for now as premature and momentum-reducing.

## Provisional bounded design

The smallest justified first change is:

```text
source-neutral JSON value contracts
├── GitHub wrappers preserve GitHub exceptions and messages
├── PyPI wrappers preserve PackageReleaseProblem classification
└── future structured sources may reuse the same value rules
```

The shared layer must not own:

- HTTP requests;
- headers or authentication;
- status-code meaning;
- field presence policy or resource-specific missing-field wording;
- package, repository, PR, workflow, release, or upstream identity;
- provenance records;
- public evidence/problem types.

A practical implementation shape is a small `json_contract.py` module with a neutral `JsonContractViolation` and value-level functions. Value-level validation is preferred over a universal `required_field` API because GitHub and PyPI currently preserve missing fields differently.

## Deferred possible extraction

Bounded response-body reading may become the second shared primitive, but only after the upstream source format is chosen. If the upstream client needs the same streamed byte limit and response-closing behavior as PyPI, that exact common behavior can then be extracted with evidence from two consumers.

It should not be forced into GitHub or generalized before that need is concrete.

## Proposed proof

The first refactor should require:

1. direct deterministic tests for every neutral value contract;
2. unchanged GitHub public exception behavior in focused regression tests;
3. unchanged PyPI evidence/problem states in all existing tests;
4. the complete active repository test suite;
5. no new dependency;
6. no CLI, network endpoint, authority, or product-claim change.

## Proposed stable instruction

After implementation is validated, add a concise repository-wide rule:

> Before adding helpers for a new external source, classify each behavior as source-neutral mechanics or source-specific evidence semantics. Reuse shared primitives only when the meaning is identical; keep authority, identity, and failure interpretation in the focused source boundary.

## Non-goals

This investigation does not yet:

- implement the upstream-source resolver;
- integrate PyPI into the CLI;
- interpret release notes;
- redesign all error types;
- create a plugin framework, adapter registry, service layer, or dependency-injection container;
- refactor code merely for stylistic uniformity.

## Learning notes

The key distinction established here is:

```text
same syntax or library call
≠
same responsibility
```

`isinstance(value, Mapping)` has source-neutral meaning. A PyPI release `404` followed by a package lookup has PyPI-specific evidence meaning. The first is a good shared primitive; the second must remain local.

## Current classification

**Design ready for approval; source unchanged.**

The audit found enough real duplication to justify one small JSON-contract extraction. It did not justify a shared HTTP client. Implementation should begin only after Ali accepts this exact boundary, then stop after the refactor and full regression proof so B2 upstream-source work can resume.
