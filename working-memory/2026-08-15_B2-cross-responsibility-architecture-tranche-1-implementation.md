# B2 Cross-Responsibility Architecture — Tranche 1 Implementation Record

**Date:** 2026-08-15  
**Operation:** Phase E / Tranche 1 — static workflow architecture implementation and migration  
**Result classification:** TRANCHE 1 ACCEPTED / STOP-REVIEW CHECKPOINT REACHED  
**Validated product/source baseline:** `92e6ea6cb6dbfad7c50986d95e23de924a9b36c1` on `main`  
**Accepted Tranche-1 revision:** `ef4283db0a7ce3eec75a56ccc5c07354015fd2e3` on `main`

## 1. Purpose and operating mode

Preserve material implementation, debugging, findings, exact validation evidence, and cluster results for Tranche 1 of [`../plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_IMPLEMENTATION_PLAN.md`](../plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_IMPLEMENTATION_PLAN.md).

This is an evidence trail, not the live-state owner. `../MEMORY.md` alone owns current continuation.

Accepted durable architecture remains [`../docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md`](../docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md).

### Learning / source-documentation mode

The user selected learning-by-doing/building and deferred broad mastery/system/data-flow teaching until a meaningful implementation milestone. Tranche-1 acceptance is now that milestone. New/materially modified source should include useful docstrings/comments for responsibility, proof boundaries, invariants, precedence/abstention logic, and non-obvious reasoning without restating syntax; the stable rule is owned by [`../OPERATING_GUIDE.md`](../OPERATING_GUIDE.md).

## 2. Tranche-1 checklist

- [x] **Cluster 0 — synchronize and validate baseline**
- [x] **Cluster 1 — add PyYAML and prove parser dependency boundary**
- [x] **Cluster 2 — implement bounded GitHub Actions static workflow IR**
- [x] **Cluster 3 — implement shared direct-installation declaration observation**
- [x] **Cluster 4 — migrate Target artifact-environment interpretation**
- [x] **Cluster 5 — migrate CI static reading and narrow proof strength**
- [x] **Cluster 6 — reconcile repository-path ownership drift**
- [x] **Cluster 7 — Tranche-1 regression and acceptance gate**
- [x] **Tranche-1 implementation / acceptance complete**
- [ ] **STOP / REVIEW milestone discussion completed**

A checked cluster means its bounded objective and applicable validation were satisfied; code presence alone is insufficient.

## 3. Continuation-critical guards

```text
static declaration != execution != success
consumer unresolved != parser failure
multiple jobs / needs / source order != runtime environment continuity
workflow evidence != complete Target context
direct-install declaration != generic dependency consumption
package invocation/exercise remains CI-specific
static Actions evidence != runtime Actions evidence
Tranche 1 != automatic authorization for Tranche 2
```

## 4. Cluster 0 — green baseline

**Status:** COMPLETED / GREEN BASELINE  
Validated baseline `92e6ea6cb6dbfad7c50986d95e23de924a9b36c1`; complete suite: `403 tests / OK`.

## 5. Cluster 1 — PyYAML dependency/parser boundary

**Status:** COMPLETED / GREEN  
**Validated implementation revision:** `0d2c7f9eba08bd3c80f1b128d5b223b4e10a9667`

PyYAML runtime dependency + private bounded representation-node parsing were established and validated. A stale exact dependency-contract expectation correctly failed after PyYAML was added, then was deliberately updated and revalidated.

## 6. Cluster 2 — bounded static GitHub Actions workflow IR

**Status:** COMPLETED / GREEN  
**Validated implementation revision:** `1e3027f87fa5b187c7d333472fe849aa6a49b049`  
Complete suite: `416 tests / OK`.

The provider-owned typed static IR is independently green before consumer migration.

## 7. Cluster 3 — shared direct-install declaration observation

**Status:** COMPLETED / GREEN  
**Validated implementation revision:** `2980e22994216c069b2f4fb36dc31ea80398367f`  
Complete suite: `425 tests / OK`.

`upgradepilot.dependency` owns direct requirements-install declaration observation with step > job > workflow > repository-root working-directory precedence and `observed | not_observed | unresolved` declaration-strength semantics.

## 8. Cluster 4 — Target migration and proof-strength correction

**Status:** COMPLETED / GREEN  
**Validated implementation revision:** `f40e7348a38966e7e30b462846a4962a116a9e80`  
Complete suite: `430 tests / OK`.

Target now consumes the shared workflow IR + direct-install observer. Static workflow source no longer claims runtime environment formation; active Target evidence uses declaration-strength `observed | not_observed | unresolved` semantics.

## 9. Cluster 5 — CI migration and proof-claim narrowing

**Status:** COMPLETED / GREEN  
**Validated implementation revision:** `10e07b37a72e6d457dfedd6766dfab23e5a27520`  
Complete suite: `434 tests / OK`.

CI now consumes the shared workflow IR and dependency install observer. The strongest active state is `supported_not_correlated`, explicitly preserving the missing static↔runtime command correlation. Static install-before-invocation ordering is checked without claiming runtime execution or success.

## 10. Cluster 6 — repository-path ownership reconciliation

**Status:** COMPLETED / GREEN  
**Validated implementation revision:** `63190a9f9538966a6d3e53d3ae70cda21edbfc8c`  
Complete suite: `435 tests / OK`.

`src/upgradepilot/github/repository.py` no longer owns a second repository-path validator. Source-neutral relative POSIX path structure is owned by `src/upgradepilot/repository_path.py`; GitHub retains provider-specific URL/acquisition/provenance behavior.

The reconciliation intentionally adopted the canonical owner where the duplicate had drifted: no silent outer-whitespace normalization, backslash paths rejected, empty/`.`/`..` components rejected, and exact accepted spelling preserved.

## 11. Cluster 7 — Tranche-1 regression and acceptance gate

**Status:** COMPLETED / GREEN / ACCEPTED  
**Accepted revision:** `ef4283db0a7ce3eec75a56ccc5c07354015fd2e3`

No acceptance-only source/test code was added because the existing focused suites already covered the plan-required obligations. The final gate therefore tested the actual accumulated Tranche-1 implementation rather than introducing new behavior at the acceptance boundary.

### Acceptance coverage

The requested fail-fast gate included:

```text
environment / dependency / import smoke
+
test_github_workflow_definition.py
test_direct_install_declaration.py
test_target_artifact_environment.py
test_workflow_commands.py
test_ci_dependency_exercise.py
test_exact_commit_repository_files.py
test_identity_primitives.py
test_source_topology.py
test_github_actions.py
test_artifact_serviceability.py
test_runtime_dependency_contract.py
test_investigation.py
test_cli.py
test_step7f_end_to_end.py
+
complete active product deterministic suite
+
clean/aligned repository state
```

Because the fail-fast block reached its final acceptance marker, the environment/import smoke and every focused/nearest command completed successfully before the full-suite result.

Complete deterministic suite:

```text
Ran 435 tests in 0.090s
OK
```

Final accepted state:

```text
branch: main
HEAD: ef4283db0a7ce3eec75a56ccc5c07354015fd2e3
origin/main: ef4283db0a7ce3eec75a56ccc5c07354015fd2e3
worktree: clean

TRANCHE 1 ACCEPTANCE COMPLETE
ACCEPTED REVISION: ef4283db0a7ce3eec75a56ccc5c07354015fd2e3
```

### T1-F008 — Tranche 1 satisfies its accepted stop line

The final gate validates the accumulated architecture and migrations together:

```text
RepositoryTextFile
→ bounded PyYAML parser boundary
→ provider-owned static GitHub Actions IR
→ dependency-owned direct-install declaration observation
→ Target consumer with declaration-strength semantics
→ CI consumer with narrowed non-correlated proof semantics
+ source-neutral repository-path ownership
```

The acceptance does **not** strengthen static evidence into runtime command correlation. The following remain intentionally outside Tranche 1:

```text
static↔runtime job/step correlation
runtime log interpretation
matrix runtime-instance mapping
reusable-workflow execution semantics
exact proposed-version runtime witness
universal workflow / shell / dependency tracing
```

## 12. Tranche-1 result and stop line

**TRANCHE 1 IMPLEMENTATION / ACCEPTANCE: COMPLETE.**

The approved stop line has been reached:

- shared static workflow IR implemented and migrated;
- Target static proof semantics corrected;
- CI strongest current proof wording/state narrowed;
- shared dependency direct-install declaration observation implemented;
- repository-path ownership drift reconciled;
- focused/nearest/import/full validation green at one clean aligned accepted revision.

**STOP / REVIEW is mandatory now.** Do not continue automatically into Tranche 2.

The next activity is milestone review/onboarding and an explicit decision about what follows. Tranche 2 remains optional separately reviewed strengthening, not unfinished Tranche-1 work.
