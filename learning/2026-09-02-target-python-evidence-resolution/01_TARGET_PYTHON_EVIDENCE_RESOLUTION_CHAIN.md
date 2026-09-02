# Target Python Evidence Resolution Chain — Learning Note

**Snapshot date:** 2026-09-02  
**Evidence horizon:** current `main` source/tests inspected immediately before this artifact was authored; this note is a learning snapshot, not live project authority.  
**Learning depth target:** implementation-adjacent understanding of the exact target-Python evidence responsibility, with central authority/evidence boundaries at ownership level and incidental library/syntax details kept operational or lookup-level.  
**Primary real case:** S001 — `pydantic/pydantic#13432`, `soupsieve 2.6 → 2.8.4`.

This note teaches one coherent product-owned responsibility:

```text
exact immutable target repository file
→ interpret the target Python declaration
→ evaluate whether the dropped Python line intersects that declaration
→ update the Python-support applicability assessment
```

It is deliberately narrower than the older S001 end-to-end learning snapshot. It focuses on the evidence-resolution chain that the current R4-A4 experiment reuses after deterministic action admission.

---

## 1. Why this responsibility matters

A dependency update may cross an upstream Python-support drop, but that does not establish that the target project is affected.

UpgradePilot needs another bounded proposition:

> Does the exact target revision declare a Python installation range that includes the dropped Python line?

For S001 the relevant question is approximately:

```text
Soup Sieve 2.8 drops Python 3.8 support
+
Pydantic PR #13432 proposes Soup Sieve 2.6 → 2.8.4
+
what does the exact PR head declare in [project].requires-python?
```

The product therefore uses a sequence of owners rather than one large function:

```text
GitHubRepositoryClient.get_exact_commit_text_file(...)
        ↓
RepositoryTextFile | UnavailableRepositoryFile
        ↓
interpret_target_python_declaration(...)
        ↓
TargetPythonDeclaration | TargetPythonDeclarationProblem
        ↓
evaluate_target_python_relevance(...)
        ↓
PythonLineSpecifierEvaluation | PythonLineSpecifierProblem
        ↓
TargetPythonRelevanceResult
        ↓
evaluate_python_support_drop_impact(...)
        ↓
PythonSupportDropImpactAssessment
```

The key engineering idea is that each layer establishes a different proposition. A later layer consumes earlier trusted results instead of redoing their work.

---

## 2. Responsibility map

### 2.1 `upgradepilot.github.repository`

Main role in this chain:

```text
repository + immutable commit SHA + repository-relative path
→ bounded exact repository text evidence
```

The important method is:

```python
GitHubRepositoryClient.get_exact_commit_text_file(...)
```

It owns provider-facing acquisition and admission of one exact file. A successful result is:

```text
RepositoryTextFile
    repository
    path
    revision
    content
```

An exact file that is absent or inaccessible through the admitted `not_found_or_inaccessible` condition becomes:

```text
UnavailableRepositoryFile
```

That distinction is important later: an unavailable exact file is still a valid typed repository-evidence result. It is not automatically the same thing as an operational transport failure.

### 2.2 `upgradepilot.target.python`

Main role:

```text
exact repository-file evidence
→ meaning of [project].requires-python
```

The public interpreter is:

```python
interpret_target_python_declaration(...)
```

Its valid semantic result family is:

```text
TargetPythonDeclaration
OR
TargetPythonDeclarationProblem
```

It does not decide applicability, compatibility, or whether the dependency update should be accepted.

### 2.3 `upgradepilot.target.python_specifier`

Main role:

```text
one dropped Python X.Y line
+
target requires-python specifier
→ whether at least one stable X.Y.Z version is admitted
```

The public method is:

```python
evaluate_python_line_specifier(...)
```

This is the bounded PEP 440 comparison method used by target relevance. It returns either an evaluation or an explicit method problem.

### 2.4 `upgradepilot.target.relevance`

Main role:

```text
grounded upstream support-drop claim
+
target Python evidence
→ bounded target relevance
```

The public function is:

```python
evaluate_target_python_relevance(...)
```

Its result answers only whether the dropped Python line intersects the target project's exact-head declared Python range under the accepted deterministic method.

It does **not** mean:

```text
compatibility
safety
merge readiness
maintainer recommendation
```

### 2.5 `upgradepilot.impact.python_support`

Main role in this chain:

```text
PythonSupportDropImpactCandidate
+
TargetPythonRelevanceResult
→ updated proposition/applicability state
```

The relevant function is:

```python
evaluate_python_support_drop_impact(...)
```

Before exact target evidence exists, the candidate can remain explicitly unresolved. After target relevance exists, the assessment is recalculated using the new evidence.

---

## 3. The real S001 flow

S001 is the best concrete anchor because this exact target-evidence question is already part of its real product path.

Known case identity:

```text
repository: pydantic/pydantic
PR: 13432
dependency: soupsieve
old version: 2.6
proposed version: 2.8.4
upstream dropped Python line: 3.8
```

Before target acquisition, the Python-support candidate can contain:

```text
upstream_python_support_drop_crossed
→ established

exact_target_python_declaration_established
→ unresolved

declared_python_range_intersects_dropped_line
→ unresolved
```

That state justifies the existing bounded investigation:

```text
acquire_exact_target_python_declaration
```

The deterministic action points to the exact target repository, immutable revision, and `pyproject.toml` path. Once that action is admitted, the execution/evidence chain is:

```text
exact S001 head revision + pyproject.toml
→ RepositoryTextFile / UnavailableRepositoryFile
→ TargetPythonDeclaration / TargetPythonDeclarationProblem
→ TargetPythonRelevanceResult
→ updated PythonSupportDropImpactAssessment
```

The important boundary is:

> The planner may select the investigation ID, but these product owners determine what evidence was actually acquired and what that evidence means.

---

## 4. Step 1 — exact immutable repository evidence

### Mental model

Do not ask:

> What does `pydantic/main` say now?

Ask:

> What did the exact immutable revision proposed by this PR contain at `pyproject.toml`?

This is why `get_exact_commit_text_file(...)` requires a canonical immutable Git commit SHA rather than a movable branch name.

The repository boundary also validates the provider response before creating trusted internal evidence. Examples include:

```text
requested path must be repository-relative and normalized
returned object must be a regular file
returned path must match the requested path
content encoding must be base64
content must decode successfully
text must be UTF-8
text size is bounded
```

Provider-only response details used to admit the result are intentionally not all preserved downstream. The durable successful evidence contract stays small.

### MUST MASTER

```text
identity is part of evidence
```

The repository, immutable revision, and path are not incidental metadata. They define which source the evidence came from.

### Operational vs semantic outcome

A useful distinction:

```text
GitHub says exact file is not found/inaccessible
→ repository owner converts this admitted condition to UnavailableRepositoryFile
→ valid semantic evidence continues downstream

transport timeout / untrusted response shape / other acquisition failure
→ no valid RepositoryFileEvidence exists
→ operational failure at the acquisition boundary
```

That distinction becomes central in R4-A4 state-transition semantics.

---

## 5. Step 2 — interpret only the admitted target declaration

`interpret_target_python_declaration(...)` intentionally reads only:

```toml
[project]
requires-python = "..."
```

It does not try to infer Python support from every possible project file or tool-specific field.

Its admitted source role is also narrow: the evidence path must be `pyproject.toml`.

### Successful result

```text
TargetPythonDeclaration
    state = "available"
    path
    revision
    requires_python
```

### Explicit problem states

```text
file_unavailable
malformed_toml
project_table_absent
requires_python_absent
invalid_requires_python
```

These are not all the same problem.

For example:

```text
requires_python_absent
```

means the exact file was successfully acquired and parsed, but the declaration was not present.

Whereas:

```text
file_unavailable
```

means the exact admitted source file could not be established.

### MUST MASTER

```text
problem result != exception by default
```

A typed domain/evidence problem is often a legitimate semantic result. It lets later logic preserve exactly why a proposition remains unresolved.

---

## 6. Step 3 — bounded PEP 440 Python-line comparison

Suppose the upstream claim says:

```text
Python 3.8 support was dropped
```

and target evidence says:

```toml
requires-python = ">=3.10"
```

The question is not whether the text contains `3.8`. The method asks:

> Does this PEP 440 specifier admit at least one stable Python `3.8.Z` version?

`evaluate_python_line_specifier(...)` uses `packaging.specifiers.SpecifierSet` and `packaging.version.Version` to evaluate this bounded proposition.

It constructs the selected line interval approximately as:

```text
Python 3.8 line
→ lower = 3.8.0
→ upper = 3.9.0
```

Then it derives a finite set of meaningful candidate stable versions from the specifier boundaries and asks whether one is admitted.

### Evaluation result

A successful method result records useful proof details:

```text
normalized_requires_python
line_lower_bound
line_upper_bound
candidate_versions_checked
witness_version | None
contains_stable_release
```

When overlap exists, the witness is especially useful because the result can point to one exact stable `X.Y.Z` version admitted by the target declaration.

### Method problems remain explicit

Examples:

```text
invalid_python_line
invalid_requires_python_specifier
unsupported_requires_python_specifier
unsatisfiable_requires_python_specifier
```

The method does not silently guess when the declaration falls outside its accepted comparison capability.

### Required depth

**Understand operationally:**

- PEP 440 is the Python version-specifier standard used here.
- `SpecifierSet` parses/evaluates the target constraint.
- `Version` provides normalized comparable Python-version values.
- a stable witness proves overlap under this method.

**Lookup-level for now:**

- `packaging` implementation internals;
- every PEP 440 edge case not exercised by this responsibility;
- regex-engine internals;
- deep iterator/collection implementation details.

---

## 7. Step 4 — convert method evidence into target relevance

`evaluate_target_python_relevance(...)` combines the grounded upstream result with target evidence.

### Main states

```text
declared_python_overlap
outside_declared_python_range
target_declaration_unresolved
upstream_claim_unresolved
comparison_unsupported
```

These states preserve why the proposition resolved or did not resolve.

### Important branches

#### Grounded upstream claim + valid declaration + overlap

```text
specifier method finds stable witness
→ declared_python_overlap
```

#### Grounded upstream claim + valid declaration + no overlap

```text
no admitted stable X.Y.Z witness
→ outside_declared_python_range
```

#### Target declaration problem

```text
TargetPythonDeclarationProblem
→ target_declaration_unresolved
```

#### Comparison method cannot support the declaration

```text
PythonLineSpecifierProblem(state="unsupported_requires_python_specifier")
→ comparison_unsupported
```

This is materially different from saying the target is outside the affected range.

### MUST MASTER

```text
relevance != recommendation
```

This layer answers one proposition about declared Python-range intersection. It intentionally stops there.

---

## 8. Step 5 — update the Python-support impact assessment

`PythonSupportDropImpactCandidate` already holds the grounded mechanism candidate and target identity.

Before target evidence:

```text
target_relevance = None
→ target declaration proposition unresolved
→ activation proposition unresolved
→ candidate applicability unresolved
```

Once `TargetPythonRelevanceResult` exists, `evaluate_python_support_drop_impact(...)` rebuilds the relevant proposition assessments.

### Example: overlap

```text
target relevance = declared_python_overlap
→ exact target declaration established
→ declared range intersection established
→ candidate applicability can become established
```

### Example: non-overlap

```text
target relevance = outside_declared_python_range
→ exact target declaration established
→ activation proposition refuted
```

### Example: target evidence problem

```text
target relevance = target_declaration_unresolved
→ target declaration proposition remains unresolved
→ activation remains unresolved
```

Crucially, the exact acquisition is not automatically selected forever. Once target relevance/evidence exists—even when it is a typed target problem—the current mechanism-specific selector does not simply repeat the same immutable investigation.

That is why A4 can treat a valid `TargetPythonDeclarationProblem` as a semantically consumed action.

---

## 9. Three boundaries that are easy to confuse

### Boundary A — acquisition truth

Owned by repository acquisition:

```text
Did we obtain trustworthy exact-file evidence for repository/revision/path?
```

### Boundary B — target declaration meaning

Owned by `target.python`:

```text
What does the admitted pyproject.toml establish about [project].requires-python?
```

### Boundary C — relevance/applicability

Owned by `target.relevance` + `impact.python_support`:

```text
Does the grounded dropped Python line intersect the target declaration?
What does that do to the candidate's bounded applicability propositions?
```

Do not collapse these into one generic "validation" step.

---

## 10. Why the chain is separated this way

### CURRENT FACT

The current product code uses distinct provider, target interpretation, deterministic specifier, relevance, and impact owners.

### EVIDENCED RATIONALE

The surrounding source/tests and current A4 design consistently preserve separate authority boundaries:

```text
provider acquisition
!=
domain interpretation
!=
relevance comparison
!=
impact proposition state
```

This allows later consumers to reuse already-established facts without becoming duplicate owners.

### ENGINEERING JUDGMENT

For the current responsibility, this separation is proportionate. Each layer has a concrete independent proposition and focused tests. Combining them into one broad target-check function would make failure meaning and proof ownership less clear.

The current one-action investigation selector remains deliberately mechanism-specific. There is not yet evidence for a generic executor/rule-engine abstraction.

---

## 11. Focused proof anchors

The most useful tests for relearning are:

### `tests/test_exact_commit_repository_files.py`

Protects:

```text
immutable commit acquisition
minimum durable text contract
rejection of movable/malformed revisions
path admission
provider response trust checks
bounded text semantics
```

### `tests/test_target_python.py`

Protects:

```text
available requires-python declaration
file unavailable
malformed TOML
missing [project]
missing requires-python
invalid requires-python
wrong source path rejection
```

### `tests/test_python_line_specifier_method.py`

Protects the accepted stable Python-line comparison method and its explicit problem states.

### `tests/test_target_python_relevance.py`

Especially useful cases:

```text
S001-shaped Python 3.8 + >=3.10
→ outside_declared_python_range

overlap case
→ exact stable witness preserved

target declaration problems
→ target_declaration_unresolved
```

### `tests/test_python_support_impact.py`

Especially useful cases:

```text
pre-acquisition state is explicitly unresolved
→ exact target declaration investigation selected

typed target problem after acquisition
→ same exact acquisition not selected again

overlap/non-overlap
→ applicability propositions update accordingly
```

### Proof limit

These focused tests establish their deterministic contracts. They do not by themselves prove:

```text
all public repositories can be acquired successfully
all possible PEP 440 declarations are supported by the bounded method
compatibility or safety of a dependency update
maintainer intent
production reliability
planner semantic quality
```

---

## 12. Connection to the current R4-A4 experiment

The current R4-A4 transition seam intentionally does **not** duplicate this product logic.

After A2 has already admitted the action, A4 executes:

```text
AdmittedInvestigationAction
→ GitHubRepositoryClient.get_exact_commit_text_file(...)
→ interpret_target_python_declaration(...)
→ evaluate_target_python_relevance(...)
→ evaluate_python_support_drop_impact(...)
→ next EvidenceGapInvestigationState
```

This is why understanding the product-owned chain first is useful before studying A4.

A4 adds a different responsibility around it:

```text
when execution begins
→ budget semantics
→ semantic consumption vs operational failure
→ immutable state replacement
→ transition trace
→ deterministic replay
```

At this snapshot, A4 source/tests have been implemented but focused runtime execution and real S001 A4 execution remain pending. Therefore this note treats A4 only as the current consumer of the already-existing product chain; it does not teach A4 as proven behavior.

---

## 13. Concepts and required depth

### MUST MASTER / OWN

```text
immutable source identity as part of evidence
provider evidence vs domain interpretation
valid typed problem result vs operational failure
one responsibility/authority owner per proposition
unresolved vs refuted vs unsupported
relevance is narrower than compatibility/safety/recommendation
evidence-driven proposition update
```

### UNDERSTAND OPERATIONALLY

```text
RepositoryTextFile / UnavailableRepositoryFile
TargetPythonDeclaration / TargetPythonDeclarationProblem
TargetPythonRelevanceResult
PythonSupportDropImpactAssessment
PEP 440 specifier evaluation
stable witness idea
frozen dataclasses and typed result unions used to preserve state clearly
```

### RECOGNIZE / LOOKUP-LEVEL

```text
base64 decoding internals
urllib quoting details
regex internals
packaging library internals
all possible PEP 440 corner cases
Python dataclass implementation internals
```

### DEFERRED DELIBERATELY

```text
generic investigation/executor registry
rule engine
general multi-action planner machinery
durable workflow persistence/event sourcing
```

Reopen those only when a real later responsibility demonstrates the need.

---

## 14. Fast relearning route

When returning to this topic later, do this:

```text
1. Recall the chain:
   exact file → declaration → specifier comparison → relevance → impact state

2. Open:
   src/upgradepilot/target/python.py
   src/upgradepilot/target/relevance.py
   src/upgradepilot/impact/python_support.py

3. Trace S001-shaped values:
   Python 3.8 drop + target requires-python >=3.10

4. Inspect proof anchors:
   tests/test_target_python_relevance.py
   tests/test_python_support_impact.py

5. If acquisition/failure semantics matter, reopen:
   src/upgradepilot/github/repository.py
   tests/test_exact_commit_repository_files.py

6. If the exact PEP 440 method matters, reopen:
   src/upgradepilot/target/python_specifier.py
   tests/test_python_line_specifier_method.py
```

You should then be able to explain why a valid target-problem result can consume an exact investigation while a transport failure cannot establish semantic target evidence.

---

## 15. Ownership / transfer questions

1. Why is reading `main` weaker evidence than reading the exact PR-head commit for this responsibility?
2. Why is `TargetPythonDeclarationProblem(state="requires_python_absent")` a valid semantic result rather than an acquisition exception?
3. What proposition does `evaluate_python_line_specifier(...)` establish, and what does it deliberately not establish?
4. Why must `comparison_unsupported` remain different from `outside_declared_python_range`?
5. If the exact target file was acquired successfully but contained no `requires-python`, should the same immutable acquisition be immediately selected again? Why?
6. Which layer owns the statement that the target's declared Python range overlaps the upstream-dropped line?
7. Why can A4 reuse this whole chain without becoming a second owner of target-Python semantics?

---

## 16. Source and evidence anchors

Primary source:

```text
src/upgradepilot/github/repository.py
src/upgradepilot/target/python.py
src/upgradepilot/target/python_specifier.py
src/upgradepilot/target/relevance.py
src/upgradepilot/impact/python_support.py
```

Focused tests:

```text
tests/test_exact_commit_repository_files.py
tests/test_target_python.py
tests/test_python_line_specifier_method.py
tests/test_target_python_relevance.py
tests/test_python_support_impact.py
```

Current R4 continuity:

```text
plans/B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md
plans/B2_X1_R4_LBD_LEARNING_DEPTH_AND_REENTRY_MAP.md
working-memory/2026-09-01_B2-X1-R4A4-pre-implementation-design-and-lbd-entry.md
working-memory/2026-09-01_2055_B2-X1-R4-real-flow-proof-and-live-A3.md
```

Related historical learning snapshot:

```text
learning/2026-08-15-tranche1-real-case-code-flows/01_S001_NORMAL_APPLICATION_END_TO_END.md
```

Do not silently update that older frozen snapshot to match this note. It remains evidence of the earlier learning horizon.
