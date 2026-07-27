# B2 Shared External-Source Foundation Investigation

**Date:** 2026-07-27  
**Operation:** Audit repeated acquisition and validation mechanics before adding another external source  
**Starting revision:** `4520f981d7c7e0ab9f716daab0773643405e1338`  
**Status:** Active investigation

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

## Initial observed overlap

Potentially shared mechanics:

- request timeout handling;
- bounded response-body acquisition and response closing;
- JSON decoding and top-level shape checks;
- required JSON field/type validation;
- retrieval time and source-locator preservation;
- test injection for HTTP sessions and clocks.

Known source-specific behavior that must not be generalized accidentally:

- GitHub authentication, API-version headers, pagination, and HTTP classification;
- PyPI release-versus-package `404` classification and exact package/version identity;
- future project-control, redirect, release-specificity, and upstream-source authority rules;
- public result and exception contracts owned by each focused source boundary.

## Investigation sequence

1. Inventory repeated mechanics across `github_api.py` and `pypi_client.py`.
2. Separate exact duplication from merely similar-looking code.
3. Identify which behavior the upcoming upstream source is likely to need.
4. Compare three choices:
   - keep clients separate;
   - extract only source-neutral validators and body-reading primitives;
   - introduce a broader shared acquisition client.
5. Evaluate change cost, regression risk, test impact, readability, and future extension pressure.
6. Present the smallest justified design to Ali before changing source architecture.
7. Implement only after the boundary is understood and accepted.

## Decision criteria

A shared layer is justified only when it:

- serves at least two current source boundaries and a credible near-term third use;
- has identical semantics at the shared level;
- leaves source authority and domain identity checks in focused clients;
- reduces code and behavioral drift rather than adding indirection;
- remains easy to explain and test in the learning-by-doing workflow;
- does not become a universal framework or delay B2 momentum unnecessarily.

## Non-goals

This investigation does not yet:

- implement the upstream-source resolver;
- integrate PyPI into the CLI;
- interpret release notes;
- redesign all error types;
- create a plugin framework, adapter registry, service layer, or dependency-injection container;
- refactor code merely for stylistic uniformity.

## Working method and learning contract

During the investigation:

- preserve concrete examples from current source files;
- explain what is genuinely common and what only looks common;
- keep architectural choices connected to product evidence responsibilities;
- prefer one small refactor with clear tests over a broad cleanup;
- record rejected approaches when they clarify the final design;
- stop the investigation once a bounded decision is available so B2 implementation can continue.

## Current classification

**Active.** The need is credible, but no shared abstraction has been approved or implemented yet.
