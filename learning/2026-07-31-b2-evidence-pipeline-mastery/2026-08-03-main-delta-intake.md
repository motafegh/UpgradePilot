# 2026-08-03 Main Delta Intake — Step 5 and CI Proof-Boundary Audit

**Learning package:** `2026-07-31-b2-evidence-pipeline-mastery`  
**Purpose:** Preserve the material production delta imported before continuing implementation-adjacent learning.  
**Learning branch:** `agent/learning-current-implementation`  
**Current synchronized main baseline:** `794f45201a7c6a3c71ecfa7fbf4411467851e5d5`  
**Synchronization merges:** PR #16 and PR #17  
**Authority:** Learning intake only. `MEMORY.md` on `main` remains the sole live-state owner.

## 1. Why this intake exists

The learning branch had been synchronized through the earlier Step 4-era production state, but `main` advanced materially while the CI learning session continued.

The imported delta now includes:

```text
Step 4 target-Python relevance validation
→ Step 5A release-index acquisition/selection
→ Step 5B Git tag-to-commit resolution
→ Step 5C exact immutable changelog-file acquisition/composition
→ Step 5D deterministic authority-composition integration proof
```

and the non-controlling technical audit:

```text
audits/2026-08-02_AUDIT-002_ci-dependency-exercise-proof-boundary.md
```

The correct learning response is **not** to abandon the current CI unit and jump to Step 5. The new code is preserved as later intake while the current source-learning path continues from its exact stopping point.

## 2. Current product truth imported from `main`

At synchronized baseline `794f452...`, `MEMORY.md` states:

- parent-plan Steps 1–4 and Step 5A–5C are behavior-validated;
- Step 5D deterministic integration proof is implemented but awaiting local validation;
- after Step 5D validates, a live S001 upstream-acquisition proof is still required before parent Step 5 closes;
- semantic extraction/model integration, conditional target activation in CLI runtime, and full S001 end-to-end relevance remain outside the current validated boundary.

The last observed complete deterministic validation recorded for Step 5C is:

```text
Ran 310 tests in 0.054s

OK
```

Step 5D adds two controlled integration tests, so 312 is only the derived expected complete count until observed terminal output confirms it.

## 3. New later-learning responsibility: Step 5 authoritative acquisition

The previously generic future-intake slot is now concrete enough to preserve as a later learning sequence.

### Step 5A — complete package release index and crossed-release selection

Product question:

> Given a trusted dependency interval and a complete PyPI project release index, which admitted PEP 440 releases actually satisfy `old < release <= proposed`?

Core concepts later:

- raw registry keys versus parsed PEP 440 meaning;
- complete acquisition versus semantic selection;
- exact proposed raw identity;
- non-PEP-440 keys preserved as ignored/out-of-scope;
- deterministic crossed-release ordering;
- source provenance and retrieval time.

### Step 5B — exact Git tag to immutable commit

Product question:

> Given one explicit accepted version tag, which immutable Git commit does that exact tag identify?

Core concepts later:

- Git reference versus object;
- lightweight versus annotated tags;
- tag peeling;
- nested annotated tags;
- cycle detection and maximum peel depth;
- direct tag-object identity versus final resolved commit identity.

### Step 5C — exact immutable changelog-file evidence

Product question:

> Given the resolved immutable tag commit and one explicit changelog path, can UpgradePilot acquire the exact bounded UTF-8 file and compose it into trusted tagged-changelog evidence without mixing identities?

Core concepts later:

- immutable commit-only repository-file acquisition;
- commit identity versus blob identity;
- requested path versus returned path;
- reported versus decoded bytes;
- retrieval time belonging to the actual file request;
- pure evidence join;
- crucial identity rule:

```text
file_evidence.revision
==
tag_commit.resolved_commit_sha
```

### Step 5D — reuse existing Step 1 authority rather than add another production layer

The new integration test demonstrates the intended chain:

```text
PackageReleaseIndexEvidence
→ select_crossed_release_index(...)
→ CrossedReleaseIndexEvidence

GitHubTagCommitEvidence
+ ExactRepositoryTextFile
→ build_tagged_changelog_evidence(...)
→ TaggedChangelogEvidence

CrossedReleaseIndexEvidence
+ TaggedChangelogEvidence
→ assemble_upstream_interval_authority(...)
→ AuthoritativeUpstreamIntervalEvidence
```

A significant design point for later study is that Step 5D currently adds **tests only**, not a new production wrapper, because `assemble_upstream_interval_authority(...)` already owns the authority-composition responsibility.

The controlled S001-shaped minimum authority path is:

```text
complete crossed-release index
+ exact proposed-tag changelog
+ no GitHub Release bodies
→ authority_basis = tagged_changelog
```

A second integration case proves that individually valid evidence from different dependency intervals must not be joined; it produces `identity_mismatch`.

## 4. AUDIT-002 belongs to the current CI learning path, but after mechanics

The audit created during learning is now present on the synchronized branch:

```text
audits/2026-08-02_AUDIT-002_ci-dependency-exercise-proof-boundary.md
```

It should be used as a **design-review companion to Unit 4**, after the current command reader has been understood mechanically.

The audit does not change current product behavior. It records that the current `proven` rule is a bounded static-command rule combined with successful run/job evidence, not direct runtime proof of every matched command.

Important later review cases include:

```text
pip install -r requirements-dev.txt || true
continue-on-error: true
conditional/skipped steps
exercise appearing before installation
successful job without matched-step runtime correlation
proposed-version identity not observed at runtime
```

The learning goal is not merely to memorize those limitations. Ali should be able to inspect the current reader and explain exactly **why** each case can exceed its proof strength, then compare proportionate strengthening options:

```text
stricter static abstention
→ static-step/runtime-step correlation
→ optional exact-version runtime evidence
→ bounded logs only when justified
```

Do not treat the audit as authorization to implement these changes.

## 5. Current learning position remains unchanged

We remain in the CI learning path, not Step 5.

Already established with guided operational understanding:

- exact Step 7 product question;
- `proven`, `no_successful_ci`, and `unresolved` semantics;
- execution absence versus proof insufficiency;
- precedence/order of evidence checks;
- existential overall proof and preserved per-workflow evidence;
- dependency evidence path versus CI installation evidence;
- `str | None` as an explicit domain state;
- keyword-only `*`;
- `Sequence[...]` as a broad read-oriented ordered collection contract.

The exact source continuation remains:

```python
results = tuple(
    _evaluate_workflow_dependency_exercise(
        dependency,
        workflow_input,
        direct_requirements_install_path=direct_requirements_install_path,
    )
    for workflow_input in workflow_inputs
)
```

Next concepts:

```text
tuple(...)
→ generator expression
→ per-input evaluation
→ immutable aggregate result collection
```

then:

```python
proven = next(
    (result for result in results if result.state == "proven"),
    None,
)
```

which connects Python mechanics directly to the already-understood existential rule.

After the successful path is fully traced, continue into decision aggregation and then the bounded workflow-command reader. Only there should AUDIT-002 become an active design-review exercise.

## 6. Learning-order decision

Current order remains:

```text
Unit 2 — complete proven path and Python mechanics
↓
Unit 3 — decision order / aggregation
↓
Unit 4 — bounded workflow-command reader
   + AUDIT-002 design review after mechanics
↓
Unit 5 — canonical dependency identity
↓
Unit 6 — multi-format dependency coordination
   + AUDIT-001 after exact-file mechanics
↓
Units 7–10 — integration / upstream authority / grounding
↓
Unit 11A — Step 3 packaging method
↓
Unit 11B — Step 4 relevance mapping
↓
Later intake — Step 5A/5B/5C/5D acquisition chain
↓
remaining implementation only as it becomes real
```

This preserves just-in-time learning and avoids replacing the current mental model every time `main` advances.

## 7. Depth statement

This intake does **not** establish user understanding of Step 5A–5D.

Those responsibilities are only mapped for future study.

Current personal learning depth remains concentrated on the CI dependency-exercise responsibility. Product validation and user mastery remain separate claims.