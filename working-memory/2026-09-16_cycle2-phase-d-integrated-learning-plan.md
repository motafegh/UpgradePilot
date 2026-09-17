# Cycle 2 Phase D Integrated Learning / Ownership Plan — Working Memory

**Date:** 2026-09-17  
**Session status:** CLOSED — remaining deep-dive learning explicitly deferred by Ali  
**Primary responsibility:** Cycle 2 Phase D — integrated post-implementation learning and engineering-ownership check  
**Execution mode:** Learning-Only; no product/source/test mutation occurred during D  
**Previous closure:** [`2026-09-16_cycle2-phase-b-hosted-proof-closure.md`](2026-09-16_cycle2-phase-b-hosted-proof-closure.md)  
**Phase A design record:** [`2026-09-14_static-command-consumer-migration-and-identity.md`](2026-09-14_static-command-consumer-migration-and-identity.md)  
**Phase B engineering record:** [`2026-09-15_cycle2-static-consumer-build.md`](2026-09-15_cycle2-static-consumer-build.md)  
**Cycle 1 closure:** [`2026-09-13_static-workflow-command-three-cycle-implementation.md`](2026-09-13_static-workflow-command-three-cycle-implementation.md)  
**Selected bounded implementation plan:** [`../plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md`](../plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md)  
**Accepted architecture:** [`../docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md`](../docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md)

## 1. Closure decision

Phase D is closed now by explicit user decision. This is **not** a claim that every originally planned D2–D7 exercise was completed.

The closure rule is:

```text
D1 practical ownership demonstrated
+ substantial D2–D6 concepts/source/case coverage already obtained
+ no concrete product/design defect exposed
+ remaining deep-dive checks explicitly postponed
→ close D without fabricating completion
```

The postponed items remain useful learning references and may be reopened later if Cycle 3 or another responsibility exposes a concrete ownership gap.

Current cycle position after reconciliation:

```text
Cycle 1 — CLOSED
Cycle 2 A — COMPLETE
Cycle 2 B — CLOSED / hosted proof green
Cycle 2 C — COMPLETE through progressive preservation
Cycle 2 D — CLOSED with explicit deferred learning
Cycle 2 E — COMPLETE / no demonstrated repair required
Cycle 3 A — NEXT
```

## 2. Ownership actually established during D

Ali reached practical ownership of the central Cycle-1 → Cycle-2 architecture at the level needed to continue engineering work:

```text
GitHub Actions run step
→ effective shell context
→ shell-family Tree-sitter parser
→ parser-neutral StaticCommandAnalysis
→ real StaticCommandOccurrence / typed atoms / structural context
→ canonical StaticCommandLocation
→ dependency / project-environment / package-invocation interpretation
→ one-pass CI composition
→ bounded static ordering
→ explicit runtime non-claim
```

Important retained distinctions:

- one provider-owned command analysis feeds several domain consumers;
- consumers derive domain propositions from shared parser-neutral facts rather than reparsing raw shell text;
- `StaticCommandLocation(source_span, source_order)` identifies a static source occurrence only;
- source order is not runtime order or execution proof;
- the old `segment_index` identity/order/placeholder overload was deliberately removed rather than renamed;
- `observed`, `not_observed` / `not_established`, and `unresolved` are proposition-relative states;
- a sound lower-level observation can remain positive while a stronger composition is unresolved;
- conditional or short-circuit structure does not erase the existence of a real static occurrence;
- static consumption or direct invocation does not prove execution or success;
- parser uncertainty remains conservative and does not fall back to regex/text splitting for positive evidence.

## 3. D1 completion

### D1 — Cycle-2 problem + Phase-A design reconstruction

**Status:** DONE

Practical ownership was demonstrated through changed workflow examples rather than terminology memorization. Ali correctly reasoned about:

- why Cycle 1 established the trusted producer but Cycle 2 still had downstream architectural work;
- one shared analysis per run step;
- domain-specific interpretation by dependency and CI consumers;
- canonical source identity and the danger of fabricated ordinals;
- direct requirements versus changed-package invocation as different propositions;
- `ordered_after | not_after | unresolved` as bounded static composition;
- the difference between individual positive observations and a stronger unresolved relationship;
- runtime execution/success remaining outside Cycle 2.

No D1 repair is required.

## 4. Remaining D blocks — explicit reclassification

The original route contained D2–D7. They are not marked DONE merely because parts were discussed.

| Block | Final D status | What was covered | Deferred remainder |
|---|---|---|---|
| D2 identity + static ordering | DEFERRED after substantial coverage | final `StaticCommandLocation` seam, exact source identity, step/source ordering, path-dependent unresolved behavior, representative ordering tests | additional practical classification drill |
| D3 parser-neutral facts → domain semantics | DEFERRED after substantial coverage | provider/dependency/CI ownership, typed atoms, no textual fallback, material uncertainty, direct requirements/invocation examples | deeper source-by-source proof walk |
| D4 one-analysis composition | DEFERRED after source trace | final one-`WorkflowDefinition` / one job-step traversal / one `StaticCommandAnalysis` per run-step production shape and source-in composition rationale | dedicated ownership exercise |
| D5 S001 + S011 real cases | DEFERRED after real-case trace | S001 Pydantic `uv sync --all-packages --group docs` → transitive `soupsieve` witness; S011 Dictare `.[dev]` versus affected `mlx` extra → membership/consumption not established; dynamic uv-group unresolved contrast | final changed-case answers |
| D6 static/runtime boundary | DEFERRED after repeated coverage | static occurrence/order/consumption/direct exercise kept separate from execution and success | dedicated runtime-boundary drill |
| D7 proof failures + synthesis | DEFERRED | hosted failure records inspected: missed strict-API consumer, stale ordinal fixture, provider-owned dynamic uncertainty, detached identity seam, final 587/587 hosted proof | full debugging classification/synthesis exercise |

This reclassification is deliberate and user-authorized. The deferred items are learning depth, not known product defects.

## 5. Real-case evidence retained

### S001 — Pydantic / soupsieve

The real PR-head command shape:

```text
uv sync --all-packages --group docs
```

was traced through parser-neutral command facts, dependency-owned uv selection, exact-lock reachability, and CI consumption composition. The regression establishes the transitive witness:

```text
mkdocs-llmstxt
→ beautifulsoup4
→ soupsieve
```

The dynamic group variant remains `unresolved`, not absence/not-observed.

### S011 — Dictare / NumPy in `mlx`

The real case establishes that the affected dependency belongs to optional extra `mlx`, while the inspected standard and macOS test workflows install `.[dev]` rather than `.[mlx]`.

The important proposition is:

```text
visible dev selection
+ affected environment mlx
→ selected environment membership not established
```

This is a clean negative/not-established result, not parser uncertainty and not a runtime incompatibility claim.

### S004 — glyphsLib / pytest

S004 was retained as real pressure for the consumption → changed-package exercise proposition: changed development requirements are installed and pytest responsibilities are invoked. The historical case itself predates the current canonical-location implementation, so it was not falsely presented as having been evaluated by the current Cycle-2 ordering code.

## 6. Hosted-proof lessons retained

Phase-B proof history remains the durable detailed owner. The main lessons carried forward are:

1. strict evidence-contract migration must include secondary downstream consumers;
2. stale fixtures can retain removed identity assumptions after product code is clean;
3. the same conservative uncertainty may move to an earlier, more trustworthy owner;
4. unresolved step-level evidence does not automatically earn exact inner-command identity;
5. the single-traversal/source-in architecture is a correctness boundary because detached identity must not be guessed or rebound later;
6. final authoritative hosted proof passed fresh install, `pip check`, focused investigation 15/15, and full deterministic regression 587/587.

## 7. Newly discovered learning item reconciliation

The earlier D-N1 item required integrating enough Cycle-1 producer knowledge to avoid treating Cycle 2 as black-box migration plumbing.

**Final status:** RESOLVED FOR CONTINUATION.

The remaining detailed parser/consumer/test drills are now lookup/deferred learning, not a blocker to Cycle 3 Phase A. If Cycle 3 reasoning exposes a concrete missing prerequisite, reopen only that bounded gap.

## 8. Phase E reconciliation

Phase E asked for repair of demonstrated learning/prerequisite gaps, product/design defects discovered during D, and live-state reconciliation before Cycle 3.

Result:

```text
concrete product/design defect discovered in D → none
demonstrated must-repair prerequisite gap       → none
remaining optional/deep learning                → explicitly deferred
source/test mutation required                   → no
Phase-D record reconciled                       → yes
MEMORY.md reconciliation                        → required with this closure
```

Therefore **Cycle 2 Phase E is COMPLETE with no repair increment**.

## 9. Handoff to Cycle 3

The next responsibility is Cycle 3 Phase A: orient/design the **runtime-strengthening eligibility** boundary already selected by ADR-0009 and the implementation plan.

Starting proposition:

```text
static command occurrence
+ structural/control-flow context
+ effective execution profile
+ exact correlated runtime step evidence
→ is this specific occurrence eligible to be strengthened by step-level runtime success?
```

The known current pressure is that the existing CI runtime classifier works primarily at `(job_key, step_source_index)` granularity. Cycle 3 must prevent a successful enclosing step from automatically strengthening an internal command occurrence whose static structure or execution profile does not justify that inference.

Do not begin implementation before Cycle 3 Phase A establishes the bounded first eligibility rule and proof cases.

## 10. Stop / reopen rule

Do not reopen deferred D2–D7 learning merely to complete a checklist. Reopen a specific item only if:

- Cycle 3 design depends on a concept that is not sufficiently understood;
- a source/test contradiction appears;
- an implementation defect is demonstrated; or
- Ali explicitly chooses to return for deeper learning.

`UP-SKILL:upgradepilot-learning-only`  
`UP-SKILL:upgradepilot-working-memory`