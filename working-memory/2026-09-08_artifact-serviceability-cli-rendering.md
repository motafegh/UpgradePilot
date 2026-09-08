# Artifact Serviceability CLI Rendering — Working Memory

**Date:** 2026-09-08  
**Session status:** ACTIVE — Slice-4 A/B complete at source/test structural-evidence boundary; C preservation in progress; executable validation deferred  
**Primary responsibility/mode:** Build/Implement + Learning-by-Doing  
**Related plan:** [`../plans/ARTIFACT_SERVICEABILITY_PUBLIC_INVESTIGATION_INTEGRATION_PLAN.md`](../plans/ARTIFACT_SERVICEABILITY_PUBLIC_INVESTIGATION_INTEGRATION_PLAN.md)  
**Previous:** [`2026-09-07_2149_target-artifact-environment-composition.md`](2026-09-07_2149_target-artifact-environment-composition.md)

## Slice 4 A–E status

```text
A — DONE
    Pre-implementation orientation inspected the actual CLI owner and focused CLI tests.
    Ali confirmed that this slice is terminal/CLI presentation only. The adopted boundary is
    a balanced evidence summary: render meaningful artifact states, provenance, limitations,
    and proof strength without dumping full wheel-tag inventories or manufacturing an overall
    maintainer recommendation.

B — DONE WITH DEFERRED EXECUTABLE PROOF
    CLI rendering and focused presentation tests were implemented and committed. The source
    and test diffs were inspected and an isolated compare confirms Slice-4 B changed only
    src/upgradepilot/cli.py and tests/test_cli.py. Local WSL execution remains unavailable by
    user constraint; the latest source/test commit has no remote statuses, so no PASS claim
    exists.

C — IN PROGRESS
    This record preserves the presentation decisions, implementation/test evidence, and proof
    debt. MEMORY.md still needs reconciliation to this live position.

D — PENDING
    Post-implementation learning should trace how the CLI distinguishes not-evaluated,
    no-candidate, evidence-problem, established candidate, Target evidence/problem, and
    applicability state without changing domain semantics.

E — PENDING
    Repair any presentation-model gaps from D and orient Slice 5 only after D closes.
```

## A — adopted presentation boundary

Slice 4 is explicitly a presentation responsibility:

```text
PublicPullRequestInvestigation typed state
→ CLI rendering
→ human-readable terminal evidence
```

It does not reacquire providers, rerun orchestration, infer new artifact semantics, or change applicability.

The selected terminal boundary is:

- show old-package artifact evidence state;
- distinguish artifact candidate `not evaluated`, `not observed`, `evidence problem`, and `established`;
- for a real candidate, show counts of removed/added wheel-tag capabilities rather than dumping raw tags;
- show proposed source-distribution availability without implying source-build success;
- show each selected dependency-source ↔ Target environment association with workflow/revision provenance;
- show Target evidence facts or explicit Target problems and limitations;
- show current artifact applicability state/detail separately from Target environment evidence;
- show exact target wheel-compatibility evidence as not established/problem/available according to its typed owner;
- do not print an overall maintainer recommendation.

The CLI is allowed to render future `established_applicable` or `established_not_applicable` assessment values if the domain later earns them, but the current application path remains unresolved because no exact target wheel-compatibility evidence is admitted.

## B — CLI source implementation

Commit `49b69e50ac81a8c8ce006958af0d9bc60264d3b8` (`feat: render artifact serviceability evidence`) changed only `src/upgradepilot/cli.py`.

The supported dependency path now calls `_print_artifact_serviceability(result)` after package/upstream-repository evidence and before upstream semantic/Python-support presentation.

The new rendering separates states as follows:

```text
old package artifact evidence
├── not evaluated
├── provider problem state + detail
└── available + exact old package/version + distribution-file count

artifact candidate
├── evidence problem → problem/release/file/detail
├── None + both exact releases available → not observed
├── None without complete release prerequisites → not evaluated
└── real candidate → established + removed/added capability counts + sdist availability

Target artifact environments
├── candidate inactive/problem/no-candidate → not activated
├── candidate exists but no admitted association → not established from selected CI relationships
└── one or more associations
    ├── Target problem → exact workflow/revision/job/detail
    └── Target evidence → workflow/revision/job/runner/Python/install declaration/limitations

artifact applicability
├── not evaluated
└── typed applicability state + detail
    └── exact target wheel compatibility
        ├── not established
        ├── typed problem + source/detail
        └── available + source + supported-tag count
```

The CLI intentionally prints wheel-tag capability **counts**, not raw tag inventories. Static Target `exact_wheel_compatibility_state` remains visible as `unresolved` and is not rebound into the stronger `TargetWheelCompatibilityEvidence` contract.

The dependency-problem terminal path was also extended with explicit artifact downstream stops so a user does not confuse absence of artifact lines with successful evaluation.

## B — focused CLI tests

Commit `b810b33996cdc863593b471195e84f3e12344729` (`test: protect artifact serviceability CLI rendering`) changed only `tests/test_cli.py`.

The CLI tests remain presentation-oriented: they patch `investigate_public_pull_request` and supply constructed typed `PublicPullRequestInvestigation` values rather than rerunning providers/application orchestration.

Added/updated cases protect:

1. **Existing supported result with artifact branch inactive**
   - prints artifact state as not evaluated/not activated rather than silently omitting it.

2. **Established artifact candidate + Target evidence**
   - old package evidence is visible;
   - candidate is established;
   - removed/added tag capability counts are visible;
   - proposed sdist availability is visible;
   - Target source/workflow/job/runner/Python/install declaration are visible;
   - static exact wheel compatibility remains unresolved;
   - artifact applicability remains unresolved;
   - exact target wheel compatibility is explicitly not established;
   - raw `cp39-...` tag text is not dumped;
   - no maintainer recommendation label is manufactured.

3. **Target ambiguity/problem**
   - `ambiguous_target_job_selection` and detail are rendered while applicability remains unresolved.

4. **Artifact evidence problem**
   - evidence problem is distinct from no-candidate and blocks Target/applicability presentation appropriately.

5. **Completed comparison with no candidate**
   - `not observed` is shown only when both old/proposed release evidence values exist, preserving the distinction from inactive/provider-blocked composition.

6. **Unsupported dependency**
   - all artifact downstream responsibilities are explicitly shown as not evaluated/not activated.

Existing input/acquisition/response exit-policy tests remain intact.

## Structural evidence / proof boundary

An isolated compare from pre-Slice-4 live-state commit `a2876bc2f32b9bb4e3d78a919cc6227f18fc4c1f` to `b810b33996cdc863593b471195e84f3e12344729` shows exactly:

```text
src/upgradepilot/cli.py

tests/test_cli.py
```

No orchestration/domain/Target/CI source was changed in Slice 4 B.

Available evidence establishes:

```text
CLI owner/tests inspected
+
presentation boundary selected
+
CLI source committed
+
focused presentation tests committed
+
isolated two-file diff inspected
+
latest commit has no remote status
```

It does **not** establish:

```text
Python syntax/import execution
focused CLI tests PASS
investigation regression PASS
package/interface regression PASS
full deterministic suite PASS
```

Local WSL execution is still deferred by user constraint. This remains proof debt, not passing evidence.

## Immediate continuation

Complete C by reconciling `MEMORY.md`, then perform Slice-4 D — post-implementation learning/ownership from the actual CLI branches and test cases. Do not begin Slice 5 final proof until Slice-4 D/E is closed unless Ali explicitly redirects.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-working-memory`
