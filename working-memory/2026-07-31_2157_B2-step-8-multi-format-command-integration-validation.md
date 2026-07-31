# B2 Step 8 — Multi-format command integration validation

**Recorded:** 2026-07-31 21:57 +03:30  
**Route:** B2 — Public PR vertical slice  
**Step:** 8 — Integrate the multi-format dependency command path  
**Status:** Complete and behavior-validated

## Controlling authority

- Parent dependency-foundation plan: [`../plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](../plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)
- Focused Step 8 plan: [`../plans/B2_STEP_8_MULTI_FORMAT_COMMAND_INTEGRATION_PLAN.md`](../plans/B2_STEP_8_MULTI_FORMAT_COMMAND_INTEGRATION_PLAN.md)
- Architecture: [`../docs/architecture/ADR-0004-dependency-version-change-evidence.md`](../docs/architecture/ADR-0004-dependency-version-change-evidence.md)
- Implementation record: [`2026-07-31_2123_B2-step-8-multi-format-command-integration-implementation.md`](2026-07-31_2123_B2-step-8-multi-format-command-integration-implementation.md)
- Public-case partial validation: [`2026-07-31_2153_B2-step-8-public-cases-partial-validation.md`](2026-07-31_2153_B2-step-8-public-cases-partial-validation.md)

## Validated product boundary

The Step 8 product/test implementation revision remains:

```text
16c74f887d960a5e2dede56d05d7a55c16395a08
```

Later implementation, public-validation, final-validation, and memory commits do not alter that product/test source boundary.

## Deterministic repository validation

The user reported that all required Step 8 tests passed:

```text
focused Step 8 suite: passed
complete deterministic suite: passed
```

The required commands covered:

```text
tests.test_dependency_analysis
tests.test_step8_source_recognition
tests.test_exact_requirement_change
tests.test_cli
tests.test_package_interface
+
complete unittest discovery
```

The exact terminal summary lines and elapsed times were not supplied in the final message, so this record does not invent them. The user explicitly confirmed that all tests passed.

## Installed S001 validation

Observed installed command:

```bash
unset GITHUB_TOKEN
upgradepilot pydantic/pydantic 13432
```

Validated dependency identity:

```text
uv.lock
soupsieve 2.6 → 2.8.4
```

Validated exact evidence:

```text
base revision: 652a61ce4f9d7d76eaada31535807a485ece0e21
base blob: b4a68ab725de337889d50d5374ac0f05db7fb484
base bytes: 606307

head revision: aa2dc024d33f61cdef50bf1973ab5adf0a974f5a
head blob: def33fe05d78ab851ce91a33db5bc55a439873a1
head bytes: 606313
```

Validated downstream continuation:

```text
Target requires-python: >=3.10
CI dependency exercise: unresolved
CI dependency exercise reason: dependency_exercise_not_proven
Published package: soupsieve==2.8.4
Distribution files: 2
Upstream source: unsupported_source
```

The unresolved CI result is correct. The command did not infer `uv.lock` consumption from the dependency-evidence path.

The upstream source problem is an independent downstream boundary caused by the admitted source-candidate rule. It does not invalidate dependency identity, exact provenance, target evidence, CI classification, or package evidence.

## Installed S004 regression validation

Observed installed command:

```bash
unset GITHUB_TOKEN
upgradepilot googlefonts/glyphsLib 1145
```

Validated preservation:

```text
requirements-dev.txt
pytest 9.0.2 → 9.0.3
CI dependency exercise: proven
CI dependency exercise reason: exact_head_dependency_exercised
Published package: pytest==9.0.3
Provenance coverage: 2 of 2 files
Upstream repository: pytest-dev/pytest
Accepted tag: 9.0.3
Claim state: unresolved_claim
```

The direct-requirements proving rule remained based on visible installation of the explicit requirements path and direct invocation of the changed package in successful exact-head CI.

## Step 8 stop-line result

Behavior-validated:

```text
one active multi-format dependency-analysis coordinator
+
requirements and constraints patch extraction
+
modified uv.lock exact base/head acquisition and extraction
+
PR-wide comparison through the shared comparator
+
canonical DependencyVersionChange downstream identity
+
recognized evidence problems cannot be hidden by convenient success
+
requirements-only explicit CI input remains separate
+
constraints and uv.lock do not inherit requirements CI semantics
+
normal installed S001 works through uv.lock
+
installed S004 remains proven
+
focused and complete deterministic tests pass
```

Step 8 is complete and behavior-validated.

## Parent dependency-foundation closure

The parent dependency-version-change evidence plan has reached its bounded stop line.

It established the prerequisite required by the target Python support relevance plan:

```text
materially different admitted dependency representations
→ one representation-neutral DependencyVersionChange
   or one explicit unsupported/ambiguous/multiple/incomplete/conflicting problem
```

The completed foundation includes:

- exact-requirements and constraints source admission;
- exact base/head repository-file acquisition;
- `uv.lock` schema and package-record interpretation;
- PR-wide result comparison;
- canonical downstream migration;
- CI dependency-exercise state migration;
- installed multi-format command integration;
- behavior-validated S004 and S001 controls.

The parent dependency-evidence plan is therefore complete.

## Next authorized plan

Return to:

```text
plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md
```

Its Step 0 prerequisite is now satisfied.

The next bounded step is:

```text
Step 1 — Freeze upstream interval and source authority
```

That work must define and test:

- old-version-exclusive/proposed-version-inclusive interval identity;
- admitted GitHub Release and exact tagged-changelog sources;
- source ordering and provenance;
- unavailable and conflicting source states;
- rejection of arbitrary or model-selected authority.

Do not begin target-range comparison, LLM extraction, conditional CLI orchestration, compatibility, safety, or recommendation logic before those upstream authority contracts are frozen.

## Learning state

Concepts introduced, implemented, and behavior-validated during the dependency foundation include:

- source-specific parsing behind one canonical model;
- orchestration versus interpretation;
- immutable base/head and blob provenance;
- PR-wide evidence reconciliation;
- recognized-problem precedence;
- dependency identity versus CI operational evidence;
- explicit unresolved evidence states;
- localized source-format extension boundaries;
- migration and retirement of temporary compatibility contracts.

Current depth:

```text
structured explanations completed
+ architecture and focused plans reviewed
+ tests written before implementation
+ source implementation reviewed
+ focused and complete deterministic tests reported passing
+ installed S004 and S001 behavior observed
but
no user-owned technical explanation recorded
no independent implementation practice recorded
no formal assessment recorded
not mastered
```

Product validation and learning mastery remain separate claims.
