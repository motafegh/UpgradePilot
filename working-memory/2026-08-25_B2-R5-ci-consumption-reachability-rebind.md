# Working Memory — B2 R5 CI Consumption Reachability Rebind

**Date:** 2026-08-25  
**Status:** IMPLEMENTED TO STATIC/SOURCE-REVIEW DEPTH; LOCAL RUNTIME VALIDATION DEFERRED  
**Execution branch:** `main`  
**Current plan:** `../plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`

## 1. Bounded responsibility

R5 rebinds Cluster-5 static CI consumption to the narrower R4 uv proposition without changing runtime authority or direct-exercise semantics.

The intended chain is now:

```text
static uv command selection
+ dependency-owned selected-root reachability
→ static CI dependency consumption
```

This remains explicitly separate from:

```text
STATIC DEPENDENCY CONSUMPTION
!= STATIC DIRECT EXERCISE
!= RUNTIME COMMAND/JOB AUTHORITY
```

## 2. Pre-R5 pressure

`src/upgradepilot/ci/consumption.py` still imported the legacy broad uv membership type:

```text
UvSelectedEnvironmentMembership
```

and mapped:

```text
member          → supported
not_established → not_established
unresolved      → unresolved
```

That left the CI layer coupled to the pre-R4 proposition/name after the dependency layer had already moved to explicit selected-root reachability.

The old generic adapter also derived `source_path` from `project_file_path` when available and otherwise fell back to the selection observation's `pyproject.toml`. That is not the source of the new uv reachability proposition: R4 is exact-lock-backed and its source is `uv.lock`.

## 3. New CI dependency evidence contract

`src/upgradepilot/ci/consumption.py` now imports:

```text
ProjectSourceEnvironmentMembership
UvSelectedRootReachability
```

through the active composition union:

```text
ProjectEnvironmentDependencyEvidence
```

The public composer now receives:

```text
dependency_evidence=
    ProjectSourceEnvironmentMembership
    | UvSelectedRootReachability
```

rather than a generic `membership=` parameter that blurred two different propositions.

The two paths are mapped explicitly instead of by attribute probing.

## 4. uv selected-root reachability → CI consumption

R5 maps R4 evidence as follows:

```text
UvSelectedRootReachability.state == reachable
→ StaticDependencyConsumptionEvidence.state = supported
→ reason = selected_uv_roots_reach_changed_dependency
→ preserve direct/transitive reachability kind
→ preserve unconditional witness path
→ source_path = uv.lock

UvSelectedRootReachability.state == not_established
→ StaticDependencyConsumptionEvidence.state = not_established
→ reason = selected_uv_root_reachability_not_established
→ only admitted for bound_project scope

UvSelectedRootReachability.state == unresolved
→ StaticDependencyConsumptionEvidence.state = unresolved
→ preserve dependency-owned reason/detail
→ preserve conditional candidate diagnostics when present
→ never promote a conditional candidate to supported consumption
```

The composer also verifies the material declaration relation that R4 evidence carries:

```text
project_root matches
selectors match
```

### Scope guard

R4's `not_established` state is only sound after the complete bounded-project selected-root domain is exhausted. An all-workspace declaration has a larger negative proof obligation.

Therefore R5 rejects composition of:

```text
R4 not_established
+ declaration.package_scope = all_workspace_packages
```

rather than silently strengthening a bounded negative result.

Positive `reachable` remains existential: one sound bound-project witness is still a valid witness when the static declaration also applies to all workspace packages. `unresolved` remains non-positive and cannot strengthen CI proof.

## 5. Conditional diagnostics remain non-proof

R4 can preserve:

```text
conditional_candidate_path
unresolved_conditions
```

when a deterministic structural path reaches the changed package only through unevaluated marker/resolution conditions.

R5 copies those diagnostics only onto an `unresolved` static-consumption result.

It deliberately does not create:

```text
candidate path exists
→ supported consumption
```

because structural candidate existence does not establish condition satisfiability or target applicability.

## 6. Project-source membership remains separate for S011

`ProjectSourceEnvironmentMembership` remains the source-owned proposition for cases such as S011, where the changed dependency belongs to one `pyproject.toml` optional extra/dependency group and the workflow selects another environment.

Its mapping remains separately calibrated:

```text
member          → supported
not_established → not_established
unresolved      → unresolved
source_path     → pyproject.toml
```

This preserves:

```text
lock-backed selected-root reachability
!= project-source affected-environment membership
```

## 7. CI proof split preserved

No R5 production change was made to the runtime/direct-exercise evaluator.

The existing Cluster-5 rule remains:

```text
successful exact-head CI
+ supported static dependency consumption
→ supported_not_correlated
```

A supported static uv consumption says only:

```text
this visible static uv declaration selects an explicit root
with an unconditional exact-lock path to the changed dependency
```

It does not say:

```text
the command executed
the install succeeded
the changed package was directly invoked
the expected lock/version was used at runtime
the changed behavior was exercised
```

## 8. Focused regression updates

Updated:

```text
tests/test_ci_dependency_coverage.py
tests/test_workflow_dependency_evidence.py
```

The focused CI coverage regression now protects:

```text
real S001-shaped `uv sync --all-packages --group docs`
→ supported static consumption
→ transitive witness retained
→ source_path = uv.lock
→ direct exercise still not_established

conditional candidate
→ unresolved consumption
→ candidate path/conditions retained
→ no reachability witness promotion

bound-project no-witness
→ not_established

not_established rebound to all-workspace scope
→ rejected as invalid composition

S011 dev selection vs mlx affected environment
→ not_established
→ source_path = pyproject.toml

runtime failure/no-successful-CI
→ remains separate from supported static consumption

external workflow/revision/step identity
→ remains independently rebound and checked by workflow composition
```

## 9. Changed executable/source-test commits

```text
b72d52e461862ba10a4851b687761c2469237b1f  R5 rebind CI consumption to uv reachability
bdc2672d9b73bdfb67afe95740baf2777b43c5d0  R5 focused CI reachability regressions
0f35860b66608901c665670240eafb4a9ef0bce0  R5 workflow evidence diagnostic alignment
```

Static comparison from the completed R4 record head `6d9ef23f6ef87527c8f29bc17e16905179614e70` through `0f35860b66608901c665670240eafb4a9ef0bce0` shows only:

```text
src/upgradepilot/ci/consumption.py
tests/test_ci_dependency_coverage.py
tests/test_workflow_dependency_evidence.py
```

changed in the executable/test slice.

## 10. Deliberately not changed

R5 does not implement or change:

```text
uv marker evaluation
complete workspace enumeration
complete uv environment interpretation
project/lock currentness
runtime uv invocation or runtime lock/version proof
static↔runtime step correlation
direct package-exercise semantics
S005 mediated tox support
R6 real-case pressure
R7 reconciliation acceptance
```

`uv_membership.py` is no longer the CI consumption contract, but it still temporarily contains legacy reachability projection helpers currently reused by `uv_reachability.py`. Removing/collapsing that remaining internal coupling is a separate cleanup/ownership decision and should not be conflated with this CI rebind.

## 11. Validation state

Per the user's explicit instruction, local runtime validation remains deferred.

Current evidence:

```text
R5 source/consumer ownership trace                 COMPLETE
legacy uv membership import removed from CI       IMPLEMENTED
explicit uv vs project-source mapping              IMPLEMENTED
S001/S011 focused regression updates               IMPLEMENTED
conditional diagnostic non-promotion regression   IMPLEMENTED
all-workspace negative-scope guard regression      IMPLEMENTED
post-write GitHub source inspection                PASS to static/source-review depth
R4→R5 changed-file comparison                      PASS / bounded to intended files
local focused runtime                              DEFERRED
nearest dependency/CI integration runtime          DEFERRED
complete standard suite                            DEFERRED
compileall                                         DEFERRED
```

No runtime PASS is claimed for R3, R4, or R5.

## 12. Learning / handoff

R5's important engineering lesson is a semantic composition boundary:

```text
DEPENDENCY LAYER
what does the selected project/lock evidence establish about the changed package?

        ↓ typed evidence

CI LAYER
what does this exact visible workflow declaration statically consume?

        ↓ separate evidence axis

RUNTIME / DIRECT EXERCISE
what actually ran, succeeded, or directly invoked the package?
```

The next bounded closure is R5 post-implementation learning/ownership using the real S001 and S011 mappings. After that, R6 owns real-case pressure and transfer unless the user explicitly redirects the sequence.
