# UpgradePilot Current Memory

**Last updated:** 2026-08-01  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, selected continuation, and current learning state.

Stable plans, specifications, ADRs, source, tests, and dated working records retain their own responsibilities. They must not mirror or compete with this file for live status.

## Single-live-state rule

`MEMORY.md` is the only repository file allowed to answer questions such as:

- What stage or responsibility is selected now?
- What behavior is currently verified?
- What is blocked or open?
- What is the exact next action?
- What learning depth is currently established?

Other files may record stable rules, position-neutral plans, accepted methods, or dated historical evidence, but they must not act as current trackers.

This file is **replacement state, not append-only history**. When the project advances, remove superseded live statements instead of retaining old expected counts, old blockers, and old continuations beside the new state. Git history and dated evidence preserve history.

Do not create a second current-status file, validation-status tracker, handoff file, or duplicate live register. A separate dated working-memory record is justified only when a material diagnostic or reasoning trail would otherwise be lost; it still must not own current project position.

## Live position

- **Execution branch:** `main`. No separate implementation branch is selected.
- **Route:** B2 — Public PR vertical slice.
- **Selected parent plan:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)
- **Completed Step 1:** upstream interval/source authority.
- **Completed Step 2:** deterministic support-drop claim grounding.
- **Completed Step 3:** standards-based dependency-version and Python-line specifier method.
- **Selected next responsibility:** parent-plan Step 4 — deterministic target-Python relevance with manual trusted inputs.

The Step 4 responsibility is:

```text
GroundedPythonSupportDropClaim
+ TargetPythonDeclaration
+ Step 3 packaging method
→ deterministic target-Python relevance result
```

No dedicated Step 4 implementation plan exists yet. The exact continuation is to freeze the smallest Step 4 domain contract and state mapping before writing implementation code.

## Current validated executable boundary

The executable source/test revision validated locally is:

```text
baacd71e4be93b9d0633edd1fd311f5c45c627d5
```

The user fast-forwarded local `main` to that revision with:

```bash
git pull --ff-only
```

inside the project virtual environment, then observed:

```text
python -m unittest \
  tests.test_upstream_claim \
  tests.test_upstream_claim_edges \
  -v

Ran 24 tests in 0.003s
OK
```

and:

```text
python -m unittest discover -s tests -v

Ran 251 tests in 0.053s
OK
```

This current full-suite result supersedes the former derived expectation of 250 tests. The additional regression test belongs to the Step 2 Python-line quote-token correction introduced on 2026-08-01.

The complete 251-test discovery includes the Step 3 packaging/version/specifier tests and runtime dependency contract, so a second execution of the older focused 54-test command is not required merely to close Step 3.

Repository documentation/state-maintenance commits after `baacd71e...` do not alter the validated executable source/test boundary.

## Behavior now established

### Dependency identity foundation

Admitted requirements/constraints and `uv.lock` evidence can produce one representation-neutral:

```text
DependencyVersionChange
```

or explicit evidence problems. Source evidence and CI-consumption evidence remain separate.

### Step 1 — upstream interval authority

Behavior-valid foundation exists for representing an exact old-exclusive/proposed-inclusive dependency release interval and bounded authoritative upstream source evidence without interpreting prose.

### Step 2 — support-drop grounding

The deterministic trust boundary is behavior-validated:

```text
AuthoritativeUpstreamIntervalEvidence
+ untrusted CandidateUpstreamClaimResult
→ GroundedPythonSupportDropClaim
   or explicit UpstreamSupportDropClaimProblem
```

The 2026-08-01 regression fix is included in the current validated revision:

```text
"Python 3.8."
→ may ground canonical Python line 3.8

"Python 3.8.1"
→ must not ground canonical Python line 3.8
```

The focused Step 2 suite and complete repository suite both passed after that change.

### Step 3 — packaging/version method

`pyproject.toml` admits:

```text
packaging>=26.2,<27
```

and `src/upgradepilot/packaging_method.py` behavior is validated through the complete suite.

Established method responsibilities are:

```text
DependencyReleaseInterval
→ PEP 440 parsed forward interval
   or explicit invalid/equivalent/non-forward problem
```

```text
ParsedDependencyReleaseInterval
+ already selected raw crossed-release identities
→ deterministic ordered crossed releases
   or explicit interval/identity problem
```

```text
canonical Python line X.Y
+ exact requires-python declaration
→ exact stable X.Y.Z witness/non-overlap
   or explicit invalid/unsupported/unsatisfiable problem
```

The Python-line method derives finite candidates from specifier boundaries and uses maintained `SpecifierSet.contains(..., prereleases=False)` rather than arbitrary patch enumeration.

Step 3 remains a pure method layer: it does not acquire upstream or target evidence, map final relevance states, modify CLI orchestration, or make compatibility/safety/action claims.

## Step 3 closure decision

Step 3 is **closed and behavior-validated** at the current executable boundary.

No separate Step 3 validation-status file is required solely to repeat the live pass state. The observed commands and results are summarized here because this file owns current verified behavior. Existing dated Step 3 implementation and earlier validation records remain historical evidence at their stated revisions and do not control present status.

The former continuation to run Step 3 validation and then activate Step 4 is superseded by this current state.

## Exact continuation

Proceed only with parent-plan Step 4:

```text
GroundedPythonSupportDropClaim
+ TargetPythonDeclaration
→ deterministic relevance mapping
```

First freeze the smallest domain contract and tests for at least these parent-plan states:

```text
declared_python_overlap
outside_declared_python_range
target_declaration_unresolved
upstream_claim_unresolved
comparison_unsupported
```

Before implementation, decide explicitly:

1. which Step 3 method problems map to `comparison_unsupported` versus target-declaration unresolved behavior;
2. whether Step 4 accepts only successful trusted input records or the wider result unions and owns unresolved-state mapping;
3. which input identity/provenance checks Step 4 must enforce before invoking the packaging method;
4. the exact result record fields needed to preserve the claim, target evidence, method witness/problem, and bounded relevance state without introducing compatibility or recommendation meaning.

Then use tests-first implementation for the pure deterministic mapping.

## Stop line for the next increment

During Step 4, do **not** proceed into:

- model or Instructor integration;
- upstream release-index or tagged-changelog network acquisition;
- conditional target-Python acquisition;
- CLI orchestration changes;
- S001 end-to-end integration;
- compatibility, safety, merge, defer, targeted-check, or recommendation logic.

Those remain later parent-plan responsibilities.

## Explicitly not established

- a Step 4 relevance result contract or implementation;
- an automated upstream semantic extraction/model path;
- complete crossed-release network acquisition;
- exact tagged-changelog acquisition and tag peeling;
- conditional target-Python activation in CLI orchestration;
- S001 automated `outside_declared_python_range` result;
- compatibility, safety, recommendation, maintainer action, or production readiness;
- user mastery of Steps 1–3.

## Learning state

Product behavior for Steps 1–3 is behavior-validated.

Concepts introduced through Step 3 include:

- source authority versus semantic interpretation;
- candidate output versus trusted grounded evidence;
- exact source-span grounding;
- canonical Python major/minor token boundaries;
- PEP 440 raw versus parsed identity;
- equivalent and non-forward dependency versions;
- crossed-release ordering;
- `SpecifierSet` syntax and contradiction detection;
- exact stable `X.Y.Z` product meaning;
- symbolic boundary candidate derivation;
- witness evidence versus publication evidence;
- valid-but-unsupported specifier semantics.

Current learning depth:

```text
structured explanation exposure
+ plans/ADRs available
+ implementation and tests available
+ Steps 1–3 behavior validated
but
no recorded user-owned end-to-end technical explanation
no independent implementation proof
no formal mastery assessment
not mastered
```

Product validation and learning mastery remain separate claims.

## State-maintenance rule

When route, selected responsibility, verified executable boundary, blocker, learning state, or exact continuation changes:

1. update `MEMORY.md` only for live state;
2. replace obsolete live statements instead of accumulating them;
3. change plans/specifications/ADRs only when their stable responsibility actually changes;
4. create dated working-memory only for material historical evidence or reasoning that deserves preservation, never as another status owner;
5. keep navigation READMEs explicitly non-state-bearing.