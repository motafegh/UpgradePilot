# Temporary Work Package 06 — Snapshot and Consistency Validation

**Status:** Blocked until Work Package 05 passes  
**Sequence:** 6 of 7  
**Primary repository:** `motafegh/UpgradePilot` with one final canonical Career snapshot source  
**Dependency:** Work Packages 01–05  
**Stop boundary:** Complete one intentional snapshot refresh and structural validation before final integration and deletion of temporary plans.

> This package converts the embedded Career files into an explicit point-in-time snapshot and validates the redesigned control system without creating a heavy documentation platform.

## 1. Outcome

After this package:

- the Career snapshot is explicitly point-in-time rather than a continuously synchronized mirror;
- routine session or decision changes no longer trigger snapshot refreshes;
- one reviewed canonical Career commit is selected and copied once;
- snapshot provenance is updated once and content equality is verified;
- high-value consistency checks are performed with low maintenance cost;
- realistic change-amplification scenarios produce small, predictable update sets.

## 2. Files in scope

- `docs/program/SOURCE.md`
- snapshot-related sections of UpgradePilot `AGENTS.md`
- snapshot navigation text in README or related indexes only if necessary
- `docs/program/career/**` for one final refresh after canonical Career modifications are complete
- an optional small validation/snapshot script only if it demonstrably reduces recurring manual work

## 3. Snapshot policy

### Nature

The embedded Career directory is a reviewed point-in-time program context. It is not a live mirror and must not claim continuous canonicality.

### Canonical precedence

When canonical Career access is available, canonical Career files control. The snapshot must state:

- source repository;
- selected source commit;
- refresh date;
- snapshot scope;
- known age or staleness boundary;
- canonical-precedence rule.

### Refresh triggers

Refresh only when one of these occurs:

- milestone transition;
- formal program review;
- material governance change affecting UpgradePilot operation;
- project-local continuation would otherwise be materially wrong;
- explicit manual refresh request.

Do not refresh merely because:

- one test changes;
- one session ends;
- one exact next action changes;
- one implementation sub-gate passes;
- one working-memory entry changes;
- an ADR is accepted but the snapshot is still operationally sufficient.

## 4. One-time refresh procedure

After Work Packages 01–05 are reviewed:

1. Identify the final reviewed canonical Career commit.
2. Confirm the approved snapshot file set.
3. Copy those files once into `docs/program/career/**`.
4. Verify exact content equality for every copied file.
5. Record source commit, file set and verification in `docs/program/SOURCE.md`.
6. Do not create intermediate snapshot commits for earlier canonical refactor steps.

The snapshot update should be one coherent UpgradePilot commit where tooling permits.

## 5. Optional lightweight automation

Add a small script only when it is simpler than the manual process and clearly reusable.

It may:

- copy the approved snapshot set;
- record or accept the source commit;
- compare file hashes or content;
- report missing or extra snapshot files;
- verify source metadata.

It must not:

- create continuous synchronization;
- require complex infrastructure;
- automatically rewrite unrelated files;
- infer semantic truth;
- make product work depend on a documentation platform.

## 6. Bounded consistency checker

A small checker may be created only if it materially reduces future manual review.

Candidate checks:

- broken local Markdown links;
- exact-next-action phrases inside files prohibited from carrying transient state;
- current milestone/session fields inside `AGENTS.md` or durable specifications;
- duplicate or missing requirement IDs;
- missing accepted ADR index entries;
- snapshot metadata and content equality during an intentional refresh;
- prohibited unsupported claims such as `production-ready` or `mastery` without evidence markers.

Limits:

- no semantic governance engine;
- no elaborate schema for ordinary prose;
- no style-policing gate;
- no blocking product work for low-value wording differences.

## 7. Change-amplification validation scenarios

### Scenario A — Accept a future architecture ADR

Expected logical updates:

1. ADR;
2. ADR index;
3. technical specification only if required behavior/status changes;
4. tracker decision-gate result;
5. concise memory update only if continuation materially changes.

Not normally expected:

- README;
- `AGENTS.md`;
- roadmap;
- learning contract;
- original plan/amendment;
- immediate Career snapshot refresh.

Target: normally no more than four or five canonical logical updates.

### Scenario B — One implementation test passes

Expected:

- source/test evidence;
- session evidence;
- tracker only if a gate or capability state materially changes;
- memory only if continuation changes.

No governance, roadmap, README, agent-instruction or snapshot update.

### Scenario C — Exact next action changes inside one milestone

Expected:

- tracker/current execution context;
- concise memory continuation pointer.

No stable-file changes.

### Scenario D — Milestone transition

Higher ceremony is appropriate. Expected updates may include:

- tracker;
- milestone activation metadata;
- project memory;
- coarse README maturity summary where useful;
- one intentional Career snapshot refresh.

### Scenario E — Ali challenges an accepted method

Expected behavior:

- enter bounded decision/exploration mode;
- inspect the ADR and reassessment triggers;
- collect discriminating evidence;
- update ADR/specification only if the decision or requirement actually changes.

### Scenario F — Prerequisite work exceeds 90 minutes

Use the review checkpoint. Continue, narrow, distribute or escalate based on evidence. Do not automatically create a new roadmap.

### Scenario G — Advanced-system opportunity appears

Identify the real question, check prerequisites and core health, compare with the simpler baseline, and authorize selected A1/A2 only when justified. Reject/defer is valid.

## 8. Structural validation checklist

### Authority and responsibility

- [ ] Every controlling file has a clear responsibility boundary.
- [ ] Career tracker is the exact current-state and capability-evidence owner.
- [ ] Technical requirements and implementation decisions are separated.
- [ ] Session evidence is not treated as state authority.

### Transient state

- [ ] Exact next action is absent from stable governance files.
- [ ] Exact current method/session state is absent from `AGENTS.md`.
- [ ] README files do not function as trackers.
- [ ] Plans define gates rather than routine results.

### Learning and ownership

- [ ] Proportional session modes exist.
- [ ] Decision/exploration/execution/tangent modes are distinct.
- [ ] AI-assistance fading is explicit.
- [ ] D3/D4 evidence includes transfer, failure, delayed and reduced-assistance requirements where applicable.
- [ ] Ownership can be evaluated by dimension.

### Technical specification

- [ ] Normative keywords are defined.
- [ ] Requirement IDs are unique.
- [ ] Proof obligations are traceable.
- [ ] Pydantic mechanics primarily remain in ADR-0002.
- [ ] Semantic processing order is explicit.

### Advanced systems

- [ ] All-six A0 orientation remains.
- [ ] A1/A2 selection is evidence-dependent.
- [ ] At least one credible A2 remains targeted.
- [ ] Negative decisions are valid evidence.

### Snapshot

- [ ] Snapshot is explicitly point-in-time.
- [ ] Refresh triggers are bounded.
- [ ] One final canonical Career commit was selected.
- [ ] Mirrored files match the selected canonical content.
- [ ] `SOURCE.md` records the refresh once.

## 9. Out of scope

Do not in this package:

- make further substantive policy changes unless validation reveals a direct contradiction;
- implement product code or tests;
- turn the checker into a permanent governance platform;
- continuously synchronize Career and UpgradePilot;
- delete the temporary plans before final integration review.

## 10. Pass conditions

- [ ] Snapshot policy is point-in-time and canonical precedence is explicit.
- [ ] Refresh triggers exclude routine session and sub-gate changes.
- [ ] One final canonical Career commit was copied once.
- [ ] Snapshot content equality was verified.
- [ ] `SOURCE.md` contains accurate provenance.
- [ ] Any checker added is small, high-value and low-maintenance.
- [ ] All seven change-amplification scenarios produce the expected bounded behavior.
- [ ] No substantive rule was silently changed during synchronization.

## 11. Recommended commit boundaries

Use one or two focused commits:

1. `Define bounded Career snapshot refresh policy`
2. `Refresh and validate final Career program snapshot`

After validation, stop and proceed to Work Package 07.