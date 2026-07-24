# 06 — Design Reasoning and Tradeoffs

## SMART objective

Within 30–40 minutes, defend the major current design choices, identify their costs, and explain what evidence would justify replacing each one.

## Reasoning standard

A design choice is not good merely because it is common, modern, or sophisticated.

For UpgradePilot, ask:

1. Which responsibility does this choice serve?
2. What is the simplest credible baseline?
3. Which failure or risk does it control?
4. What cost does it add?
5. How reversible is it?
6. What observable evidence would justify a more complex alternative?

## Choice 1 — Requests as the HTTP client

### Why chosen

The current slice needs synchronous public GitHub `GET` requests with:

- headers;
- query parameters;
- timeouts;
- response status;
- JSON decoding;
- injectable session for tests.

Requests provides this with low conceptual overhead.

### Cost

- synchronous only;
- retry policy is not automatic;
- another runtime dependency;
- future high-concurrency acquisition may need reconsideration.

### Why not async now

The current command processes one PR and a bounded number of API calls. Async architecture would add control-flow and testing complexity without observed throughput need.

### Revisit when

- many PRs must be processed concurrently;
- latency becomes a measured blocker;
- rate-limit-aware scheduling requires a different transport model.

## Choice 2 — Shared `github_api.py`

### Why chosen

PR, Actions, and repository-content clients need consistent handling for:

- timeouts;
- HTTP errors;
- invalid JSON;
- top-level response shapes;
- common headers.

Duplicating these rules would create inconsistent failure meanings.

### Cost

A shared base class can become a dumping ground if domain-specific logic is added.

### Control

Keep the module unaware of Pull Requests, workflows, dependencies, and authority.

### Revisit when

If resource clients require materially different transport policies, use composition or separate transports rather than forcing every behavior into one inheritance tree.

## Choice 3 — Separate acquisition from interpretation

### Why chosen

These are different questions:

```text
Can we obtain and validate the evidence?
What does that evidence mean under current product rules?
```

Examples:

- `github_client.py` validates changed-file records;
- `dependency_change.py` interprets patches;
- `github_actions.py` validates run/job facts;
- `ci_authority.py` interprets authority.

### Benefits

- deterministic interpretation tests require no network;
- failures retain precise categories;
- unsupported evidence is not confused with malformed responses;
- later interpretation rules can evolve without rewriting HTTP code.

### Cost

More modules and handoff records.

### Why cost is justified

The boundaries correspond to distinct product claims and failure modes, not artificial layering.

## Choice 4 — Immutable dataclasses

### Why chosen

Validated records should be stable after construction.

They provide:

- explicit fields;
- readable repr/equality for tests;
- fixed handoff contract;
- reduced accidental mutation.

### Why not Pydantic now

Runtime helper validation is currently small and explicit. Adding Pydantic would introduce:

- dependency and version surface;
- a second validation model to learn;
- migration and configuration choices;
- possible confusion between external schemas and internal domain invariants.

### Revisit when

- many nested schemas produce repeated validators;
- serialization contracts become public and stable;
- error aggregation or schema generation becomes a real requirement.

## Choice 5 — Explicit result objects instead of broad exceptions

### Why chosen

Unsupported and unresolved evidence are normal product outcomes.

Examples:

- unsupported dependency syntax;
- successful CI with tox indirection;
- unavailable workflow definition.

Throwing exceptions for these states would imply system malfunction.

### Cost

Callers must handle multiple result variants.

### Why the cost is valuable

The type contract forces the caller to preserve abstention instead of assuming success.

## Choice 6 — Exact SHA binding

### Why chosen

Branch names and PR state can change. Evidence must refer to the same proposal revision.

### Cost

More identity checks and exact-revision file requests.

### Why non-negotiable

Without this, the product could combine evidence from different revisions and produce a false conclusion. This is a product-integrity rule, not optional hardening.

## Choice 7 — Count reconciliation and bounded pagination

### Why chosen

Partial evidence can look internally valid while omitting a conflicting item.

### Cost

More API requests and refusal of very large cases.

### Current policy

Acquire completely within explicit limits or stop. Do not silently use partial sets.

### Revisit when

Large repositories become a supported target and a trustworthy streaming or partial-evidence policy is explicitly designed.

## Choice 8 — Shallow workflow reader instead of PyYAML

### Why chosen

The first authority rule only needs to recognize a narrow workflow shape:

- `jobs:`;
- ordinary job mappings;
- `run:` commands;
- pip requirements;
- direct invocation.

A small reader makes the supported grammar and limitations visible.

### Costs and risks

- YAML has complex syntax;
- a shallow reader may reject valid forms;
- maintaining ad hoc parsing can become unsafe if support expands.

### Why it is acceptable now

The parser fails closed: richer or ambiguous forms become unresolved rather than guessed.

### Revisit when

- unresolved YAML forms materially block the product;
- support expands beyond a small explicit grammar;
- tests show the shallow approach becoming fragile.

At that point, compare PyYAML, ruamel.yaml, GitHub's resolved job data, and other alternatives. Do not add a dependency only because YAML exists.

## Choice 9 — One-job direct authority rule

### Why chosen

Installation and execution in the same statically identifiable job provide a clear environment relationship.

### Why not combine jobs

Separate jobs may use separate machines, environments, caches, and artifacts. Combining commands would require proof of data/environment linkage.

### Cost

Some real CI remains unresolved.

### Why that is correct

False negatives in supported coverage are preferable to false authority claims in this stage. Unresolved is an honest state.

## Choice 10 — Do not trace tox when it is not a blocker

### Why chosen

S004 already has one sufficient direct workflow. Tracing tox would not change the current existential authority result.

### Principle

```text
Do not expand interpretation merely to eliminate every unresolved detail.
Expand when unresolved evidence blocks a required decision or reveals a material risk.
```

### Benefit

Prevents scope growth and keeps learning tied to real product need.

## Choice 11 — CLI first, no service/database yet

### Why chosen

The current product question can be exercised end to end through one command. A service, queue, database, or UI would not strengthen the core evidence logic.

### Revisit when

- persistent evidence history becomes required;
- multiple users or scheduled processing are admitted;
- replay and evaluation need durable storage;
- API consumers require a stable service boundary.

## Tradeoff exercise

For each proposal, decide “admit now,” “defer,” or “reject for current slice.”

1. Add PyYAML to parse every workflow accurately.
2. Add ten retries for every HTTP failure.
3. Add a database to save S004 output.
4. Add exact-head SHA validation to workflow-file retrieval.
5. Add tox tracing solely to make every workflow sufficient.
6. Add a new result state when evidence is valid but not understood.

Expected:

1. defer until richer YAML is a material blocker;
2. reject as stated; retry policy requires reason, limits, and status awareness;
3. defer; no persistence responsibility yet;
4. admit; identity integrity requires it;
5. defer; current overall authority is already sufficient;
6. admit when needed; unresolved already serves this role.

## What you must master

- simplest credible baseline reasoning;
- why complexity needs evidence;
- why false authority is worse than unresolved evidence;
- which decisions are reversible and which protect correctness;
- what signal should trigger reconsideration.

## Completion evidence

This file is mastered when you can defend each current choice without saying only “it is simpler,” and can name the evidence that would justify a different choice.