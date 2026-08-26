# Working Memory — B2 R7 Findings Register

**Date:** 2026-08-26  
**Status:** ACTIVE DURING R7; FINDINGS ACCUMULATE UNTIL FINAL REMOTE DISPOSITION  
**Execution branch:** `main`  
**Parent R7 record:** `2026-08-26_B2-R7-acceptance-cleanup-and-baseline-closure.md`

## 1. Purpose

This register collects bounded R7 edges, bugs, design pressure, proof risks, and cleanup candidates discovered while the remote R7 review progresses.

The purpose is to avoid two bad extremes:

```text
find one edge
→ patch immediately
→ churn architecture before the full R7 picture is visible
```

and:

```text
find one edge
→ mention it in chat
→ lose the reasoning/evidence before final closure
```

Normal rule:

```text
observe finding
→ establish exact current behavior from source/tests/real evidence
→ classify risk
→ record cause + consequence + possible repair shape + regression pressure
→ continue R7 when non-blocking
→ disposition all queued findings together before the final remote candidate is frozen
```

A finding may interrupt the current R7 slice immediately only when evidence establishes a hard blocker such as:

- false positive/support;
- proof strengthening or uncertainty erasure;
- authority/provenance conflation;
- broken normal production route;
- contradiction with an admitted current real case or controlling specification;
- corruption/loss that makes later R7 evidence unreliable.

Conservative under-reporting, unselected edge behavior, naming/retention pressure, and possible future capability gaps are normally queued rather than patched immediately unless later R7 evidence raises their severity.

Before R7.8 freezes the final remote candidate, every queued finding must receive one explicit disposition:

```text
FIX IN R7
ACCEPT AS KNOWN BOUNDED LIMITATION
SCHEDULE FOLLOW-UP WITH OWNER/TRIGGER
REJECT / NOT REQUIRED BY CURRENT PRODUCT RESPONSIBILITY
```

If a queued finding is promoted to `FIX IN R7`, implement it remotely in the owning R7 cleanup slice, add the smallest discriminating regression pressure, then include the resulting code/test revision in the final R7.9 local validation bundle.

---

## F-001 — Mixed safe + unresolved shell segments collapse to one unresolved R3 step

**Discovered:** R7.1 remote focused source/test audit  
**Current disposition:** QUEUED — NO IMPLEMENTATION YET  
**Current blocker:** NO  
**Risk class:** conservative under-reporting / granularity loss  
**Owning area if later fixed:** R3 project-environment selection contract, then R6 consumption of that contract

### A. Exact current cause

R3 already parses one GitHub Actions `run:` block into bounded shell segments. For each segment it separately gathers:

```text
parsed declarations
+
unresolved details
```

However, `ProjectEnvironmentSelectionObservation` has one **step-level** `state` for the entire `RunStepDefinition`.

Current producer shape in `environment_selection.py` is effectively:

```text
for each shell segment:
    parse segment
    append safe declaration(s)
    append unresolved detail(s)

if ANY unresolved detail exists:
    overall observation.state = unresolved
    retain declarations, but the step as a whole is unresolved
```

So R3 has segment indices on declarations, but uncertainty is aggregated at the run-step level.

R6 then consumes the aggregate R3 state. Current `derive_project_environment_consumptions(...)` does:

```text
R3 not_observed
→ continue

R3 unresolved
→ preserve one unresolved CI-consumption item
→ continue

R3 observed
→ evaluate each declaration through R4/project-source membership → R5
```

Therefore, when the overall step is `unresolved`, any otherwise safe retained declarations in that same step are not evaluated through R4/R5.

### B. Example

```yaml
- run: |
    uv sync --group docs
    uv sync --group "${{ matrix.group }}"
```

R3 can conceptually identify:

```text
segment 0
uv sync --group docs
→ readable literal docs declaration

segment 1
uv sync --group "${{ matrix.group }}"
→ dynamic selector
→ unresolved
```

But the final R3 observation is step-scoped:

```text
observation.state = unresolved
```

R6 therefore preserves unresolved evidence for that run step and does not evaluate the retained `docs` declaration through R4/R5.

The same limitation is independent of ordering. Reversing the two segments does not solve it.

### C. What this can lose

If the safe segment independently reaches the changed package, the current system may under-report that positive static fact:

```text
safe docs segment
→ could establish R4 reachability
→ could establish R5 supported static consumption

but another unresolved segment in the same run step
→ whole R3 observation unresolved
→ supported fact is not derived
```

Separate GitHub Actions `run:` steps are not affected; R6 still iterates later run steps/jobs/workflows independently.

### D. Why this is not currently a proof-strengthening bug

Current failure direction is conservative:

```text
possible independently supported evidence
→ unresolved
```

not:

```text
uncertain evidence
→ supported
```

and not:

```text
uncertain evidence
→ not_established
```

So the edge can lose useful positive evidence, but it does not currently manufacture false confidence.

No current admitted R6 real case reviewed in R7.1 establishes that mixed safe+unresolved segments in the same `run:` block must be supported now.

### E. Why R6 must not simply process every retained declaration in an unresolved observation

A retained declaration is not automatically independently safe.

Example:

```bash
uv sync --all-extras --no-extra mlx
```

R3 can retain the positive `--all-extras` fact while marking the same segment unresolved because the negative selector is outside the bounded positive-selection rule.

Blindly sending every declaration from every unresolved observation through R4/R5 could therefore manufacture support from a **tainted declaration in the same segment**.

So a downstream R6 workaround such as:

```text
if unresolved but declarations exist:
    evaluate declarations anyway
```

is not accepted as a safe fix shape.

### F. Suggested repair direction if final R7 disposition selects FIX

Preserve the granularity R3 already parses.

Smallest likely design direction:

```text
ProjectEnvironmentSelectionObservation
└── segment observations
    ├── segment_index
    ├── state = observed | not_observed | unresolved
    ├── reason/detail
    └── declarations owned by that segment
```

Then R6 can consume each segment independently:

```text
segment observed
→ its declarations enter R4/project-source membership → R5

segment unresolved
→ preserve unresolved CI-consumption evidence for that segment

segment not_observed
→ no project-environment contribution
```

The existing aggregate step-level state could remain temporarily as a summary/compatibility surface and be dispositioned later by the normal retention review rather than removed automatically.

This direction keeps semantic ownership in R3. R6 should not guess which declarations inside an unresolved step are safe.

### G. Suggested regression fixtures if implemented

#### Fixture 1 — safe segment before unresolved segment

```yaml
- run: |
    uv sync --group docs
    uv sync --group "${{ matrix.group }}"
```

Expected bounded result:

```text
segment 0 → supported or other R4/R5 result based on docs reachability
segment 1 → unresolved
both evidence items preserved
```

#### Fixture 2 — unresolved segment before safe segment

```yaml
- run: |
    uv sync --group "${{ matrix.group }}"
    uv sync --group docs
```

Expected result must be equivalent in evidence meaning to Fixture 1. Ordering must not determine whether the independently readable segment is evaluated.

#### Fixture 3 — one tainted segment must remain unresolved only

```yaml
- run: uv sync --all-extras --no-extra mlx
```

Expected:

```text
unresolved
NO supported consumption manufactured from retained --all-extras declaration
```

This protects against the unsafe shortcut of evaluating declarations merely because they exist inside an unresolved observation.

#### Fixture 4 — separate run steps remain independent

```yaml
steps:
  - run: uv sync --group "${{ matrix.group }}"
  - run: uv sync --group docs
```

Expected:

```text
step 0 → unresolved
step 1 → independently evaluated through R4/R5
```

This fixture protects the already-intended cross-step independence while the segment-level design is changed.

### H. End-of-R7 decision questions

Before R7.8 candidate freeze, decide F-001 against the full findings set:

1. Did later R7 real-case evidence reveal an admitted workflow that requires mixed-segment preservation?
2. Does any later finding show this granularity mismatch participates in a stronger proof/authority defect?
3. Can the segment-result contract be added without broad shell-interpreter or uv-semantics expansion?
4. Is the implementation/test cost justified for the current product responsibility, or should the limitation remain explicit and trigger-based?
5. If deferred, which future real-evidence/product trigger reopens it?

Until that disposition, **do not implement F-001 merely because the repair direction is understood**.

---

## Future finding template

Use the next stable ID (`F-002`, `F-003`, ...).

```text
Finding ID / title
Discovered at R7 slice
Current disposition
Blocker? yes/no
Risk class
Owning area

Exact evidence/current behavior
Root cause
User/product/proof consequence
Why it is or is not a blocker
Possible repair direction (not authorization)
Suggested discriminating regression/real-case fixtures
Dependencies/interaction with earlier findings
Questions for final R7 disposition
```

Do not duplicate the same root cause into multiple findings merely because it appears through different callers; extend the existing finding when the new evidence is the same underlying issue.