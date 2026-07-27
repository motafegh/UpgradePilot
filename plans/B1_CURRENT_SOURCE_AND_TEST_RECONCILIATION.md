# B1 Pre-Reset Source and Test Reconciliation — 2026-07-23

**Historical result:** Completed inspection; source disposition superseded by the accepted clean reset  
**Reset decision:** [`../docs/architecture/ADR-0003-clean-slate-b2-source-reset.md`](../docs/architecture/ADR-0003-clean-slate-b2-source-reset.md)  
**Archive:** [`../archive/2026-07-23_PRE_B2_M2_IMPLEMENTATION.md`](../archive/2026-07-23_PRE_B2_M2_IMPLEMENTATION.md)

This record preserves what B1 learned on 2026-07-23 from inspecting the pre-reset
implementation. It is historical evidence, not a live state, implementation plan, or
continuation owner. Read [`../MEMORY.md`](../MEMORY.md) for the project position.

## Inspection result before reset

Connector-backed inspection found an M2-era path:

```text
manual case mapping
→ strict case identity
→ manually assembled evidence
→ optional local-LLM extraction and input-risk experiments
→ mechanical grounding
→ one Python-support decision rule
→ targeted checks or abstention
```

The implementation contained useful concepts—strict identity, immutable contracts, explicit
missing evidence, traceable reasons, limitations, abstention, and separation of untrusted
model output—but it did not implement the accepted S001–S005 runtime.

It lacked, among other responsibilities:

- a real public PR locator and acquisition path;
- stable run identity and operation history;
- complete provenance and degraded evidence states;
- distinct observations, interpretations, and findings;
- transparent baseline versus full decision;
- conditional activation and non-activation;
- same-action, action-change, early-stop, and degraded-evidence flows;
- synchronized machine and human reports;
- follow-up, rerun, supersession, and changed-boundary transitions;
- review, ownership, and whole-run validation.

The detailed original source state remains recoverable at:

```text
e7425dcfc20f093ac10c9a903f1c4ae50a8b2638
```

## Ali's controlling corrections

After reviewing the reconciliation, Ali directed the project not to assume or evolve the
previous source because inherited AI-generated modules and tests could confuse learning and
silently constrain the new product boundary.

That instruction superseded the preliminary recommendation to evolve selected old modules.
Ali also rejected a replay-first implementation sequence because it began from prepared
fixtures and internal lifecycle terminology rather than the real product workflow.

The accepted historical consequence was:

> Build from a thin real public PR-to-decision vertical slice. Begin with a public repository
> and Dependabot PR locator, acquire minimum required public evidence read-only, freeze the
> exact proposal, evaluate it, and produce a bounded recommendation or abstention. Captured
> responses may support deterministic tests and replay, but replay is not the primary product
> interface.

Archived implementation may be consulted only for a named comparison, never as an automatic
code baseline.

## Clean-reset result observed on 2026-07-23

The reset left a minimal package boundary and removed the M2 runtime, tests, scripts, generated
outputs, and inherited runtime dependencies from active paths. The old implementation was
preserved in immutable history and the archive manifest.

Observed structural checks at the reset revision:

- root package metadata parsed;
- package marker compiled;
- isolated source-path import succeeded;
- no clean-checkout or editable-install proof was claimed at that point;
- no live acquisition or product-test behavior was claimed at that point.

These observations describe the dated reset revision only. Later behavior must be established
from later source, tests, commands, outputs, and environment evidence.

## Durable non-reuse gate

The reconciliation established that later work must preserve these rules:

- archived modules are not imported;
- archived tests are not copied or counted;
- previous class names and file boundaries have no presumption of survival;
- every dependency is justified again;
- the product accepts a real public PR locator rather than only a prepared fixture;
- a known PR or expected result is not hardcoded;
- captured expected decisions are not consumed by product logic;
- similarities to archived behavior come from accepted requirements, not convenience.

This file has no handoff or next-action authority.