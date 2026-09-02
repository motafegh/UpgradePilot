# Group 4A — Dependency Identity, Exact Version Transition, and Release Interval

**Learning-artifact date:** 2026-09-02  
**Source/test evidence horizon:** `main@5c3036cddf88e1eec9bef02e91ae38fcbbe6f534`  
**Landing context:** authored after unrelated `main@7cce5ebc65b3a6120aea9ab63aa452b99b42b64` added an R4-B proposal; that proposal does not change this note's source/test horizon  
**Roadmap responsibility:** Group 4A from `../plans/UPGRADEPILOT_WHOLE_PROJECT_LEARNING_ARTIFACT_ROADMAP_PLAN.md`  
**Artifact role:** frozen reusable learning snapshot; not project-state, implementation, or execution authority  
**Target depth:** **must master** package identity / exact-version / interval distinctions; understand current contracts and failure behavior operationally; keep parser/provider minutiae at lookup depth

This note answers one question:

> **How does UpgradePilot move from several dependency-file observations to one trustworthy package/version transition and then derive the exact release interval that later upstream reasoning is allowed to inspect?**

The key mental model is that UpgradePilot preserves **source identity first**, establishes **cross-source agreement second**, and derives **version semantics only afterward**.

---

## 1. The whole flow

```text
exact admitted dependency sources at PR base/head
        ↓
source-specific parsing/extraction
        ↓
ExtractedDependencyVersionChange | DependencyChangeProblem
        ↓
PR-wide comparison across every admitted result
        ↓
DependencyVersionChange | DependencyChangeProblem
        ↓
preserve raw exact old/proposed version strings
        ↓
PEP 440 parse + semantic comparison
        ↓
ParsedDependencyReleaseInterval | PackagingVersionProblem
        ↓
derive crossed-release interval
        ↓
(old, proposed]
        ↓
exact PyPI release/index evidence + ordered crossed releases
        ↓
later upstream authority / semantic interpretation
```

Do not collapse these into one operation:

```text
package-name normalization
!= source validation
!= dependency-change establishment
!= version parsing
!= release-interval construction
!= upstream semantic interpretation
```

---

## 2. Package identity has two useful forms

File:

```text
src/upgradepilot/package_identity.py
```

The shared function is:

```python
normalize_package_name(package: str) -> str
```

It applies the Python package-index comparison form associated with PEP 503:

```text
case-insensitive
+
runs of -, _, . compare as one hyphen
```

Example:

```text
My_Package   → my-package
my.package   → my-package
MY-package   → my-package
```

### Why normalize?

Different sources may spell the same Python distribution differently. UpgradePilot needs a source-neutral comparison identity so it can ask:

> Do these two dependency records describe the same distribution?

### Why preserve the original spelling too?

Because normalization is a **comparison transformation**, not permission to rewrite source evidence.

The current `DependencyVersionChange` therefore carries both:

```text
package             # one preserved source spelling for presentation
normalized_package  # cross-source comparison identity
```

### Must-master distinction

```text
raw/source package spelling
!=
normalized comparison identity
```

and:

```text
normalize_package_name(...)
!=
prove the package exists
!=
prove the source is trusted
!=
prove a dependency changed
```

Source-specific validators still own source validity.

---

## 3. One parsed file is not yet PR-wide truth

Current shared contract:

```text
src/upgradepilot/dependency/change.py
```

A source-specific dependency parser returns one of:

```python
ExtractedDependencyVersionChange
DependencyChangeProblem
```

The extracted form contains:

```text
package
normalized_package
old_version
proposed_version
source_evidence
```

Its meaning is deliberately narrow:

> **This one admitted source supports this exact transition.**

It does **not** yet mean:

> **The pull request as a whole has one trusted dependency transition.**

Another admitted dependency source may disagree, be malformed, be unavailable, or identify another changed package.

---

## 4. Source provenance is part of the transition evidence

`DependencyChangeSourceEvidence` records the minimal source-specific provenance needed at this boundary:

```text
path
file_format
extraction_method
```

Examples of current admitted file-format vocabulary include:

```text
exact_requirement
uv_lock
pyproject_optional_extra
```

Current extraction-method vocabulary includes:

```text
changed_file_patch
exact_base_head_files
```

This record deliberately does not duplicate every provider field or PR identity field. The exact repository/base/head/file objects are owned by their earlier evidence boundaries.

The important idea is:

```text
transition value
+
where/how that transition was established
```

not just:

```text
"soupsieve changed to 2.8.4"
```

---

## 5. PR-wide comparison is conservative consensus, not winner selection

The integration boundary is:

```python
compare_extracted_dependency_changes(results)
```

Its current logic is intentionally strict:

1. preserve unique provenance from all supplied results;
2. if any admitted result is a `DependencyChangeProblem`, stop rather than ignore it;
3. require at least one extracted transition;
4. require exactly one normalized package identity;
5. require exactly one **exact raw** `(old_version, proposed_version)` pair;
6. only then promote to `DependencyVersionChange`.

Conceptually:

```text
source A → pytest 9.0.2 → 9.0.3
source B → pytest 9.0.2 → 9.0.3
        ↓
agreement
        ↓
trusted PR-wide DependencyVersionChange
```

But:

```text
source A → pytest 9.0.2 → 9.0.3
source B → malformed dependency source
        ↓
DependencyChangeProblem
```

The valid source does not cancel the malformed admitted evidence.

### Why?

Because ignoring a problematic admitted source would turn incomplete or contradictory evidence into unjustifiably strong PR-wide truth.

---

## 6. Canonical package agreement does not mean exact-version normalization

A current test deliberately demonstrates:

```text
source A package = My_Package
source B package = my-package
normalized both = my-package
old = 1.0.0
new = 1.1.0
```

These may agree on one dependency identity and one exact transition.

But versions are different.

At the dependency-change evidence boundary, UpgradePilot requires the same **exact strings**:

```text
old_version
proposed_version
```

It does not first convert them to a semantic version object and then decide the source records agree.

### Core distinction

```text
package identity agreement
uses normalized comparison identity

version transition agreement
uses exact source strings
```

This protects provenance and prevents semantic equivalence from erasing what an external source actually named.

---

## 7. Only after exact transition is established do we apply PEP 440 semantics

File:

```text
src/upgradepilot/dependency/versioning.py
```

Accepted method owner:

```text
docs/architecture/ADR-0005-packaging-version-and-python-line-method.md
```

The implementation uses:

```python
packaging.version.Version
```

for Python package-version semantics.

The sequence matters:

```text
exact raw strings preserved
        ↓
parse semantic Version objects
        ↓
compare / order
```

not:

```text
normalize away raw strings
        ↓
keep only semantic versions
```

`ParsedDependencyReleaseInterval` therefore retains the original interval while also carrying parsed `Version` objects.

---

## 8. Textually different versions can be semantically equivalent

PEP 440 may consider forms such as:

```text
1.0
1.0.0
```

semantically equal.

Current behavior treats an interval whose old/proposed bounds are PEP-440 equivalent as:

```text
equivalent_python_package_versions
```

not a meaningful forward dependency transition.

This gives two simultaneous truths:

```text
raw text: 1.0 != 1.0.0
semantic version identity: Version("1.0") == Version("1.0.0")
```

UpgradePilot needs both facts at different boundaries.

### Why this matters

Raw identity tells us what the source actually said.
Semantic identity tells us whether the transition crosses a meaningful Python package release ordering boundary.

Neither should overwrite the other.

---

## 9. A valid dependency interval must move forward

Current semantic failure cases include:

```text
invalid_python_package_version
equivalent_python_package_versions
dependency_version_not_forward
```

Examples:

```text
old = not-a-version
new = 2.0
→ invalid

old = 1.0
new = 1.0.0
→ semantically equivalent, not a forward change

old = 2.8.4
new = 2.6
→ backwards
```

A prerelease-to-final transition such as:

```text
2.8.4rc1 → 2.8.4
```

is a valid forward PEP 440 transition.

---

## 10. The crossed release interval is `(old, proposed]`

The dependency change:

```text
old_version = 2.6
proposed_version = 2.8.4
```

becomes the upstream release interval:

```text
(2.6, 2.8.4]
```

Meaning:

```text
old release 2.6       → excluded
crossed releases      → included
proposed release 2.8.4 → included
```

If the actual crossed releases are:

```text
2.7
2.8
2.8.3
2.8.4
```

then later upstream reasoning must inspect the material changes introduced anywhere across that sequence, not only the proposed release body.

### Why old-exclusive?

The target already depended on the old release before the proposal. The investigation asks what was crossed when moving **from** that state **to** the proposed state.

### Why proposed-inclusive?

The proposed version itself may introduce a relevant change.

---

## 11. Crossed-release ordering derives semantics but preserves exact raw identities

Current method:

```python
order_crossed_release_versions(...)
```

It parses and orders crossed versions using PEP 440 but returns both:

```text
ordered_raw_versions
ordered_versions
```

Representative rules:

- release at the old bound is outside the interval;
- release below old is outside;
- release above proposed is outside;
- invalid release syntax is explicit;
- PEP-440-equivalent duplicate release identities are rejected;
- the proposed release must appear using its **exact raw identity**.

That last rule is subtle and important.

If the trusted proposed version is:

```text
2.8.4
```

and the crossed-release evidence contains only:

```text
2.8.4.0
```

then even though the two may be PEP-440 equivalent, current behavior reports:

```text
proposed_release_missing
```

### Must-master equation

```text
semantic equivalence
!=
source identity equivalence
```

Semantic comparison can tell us how releases order. It cannot silently replace the exact external identity the PR proposed.

---

## 12. PyPI supplies exact release and release-index evidence, not final upstream meaning

File:

```text
src/upgradepilot/pypi/release.py
```

Two distinct provider responsibilities matter here.

### Exact release lookup

```python
PyPIReleaseClient.get_release(package, version)
```

Produces either:

```python
PackageReleaseEvidence
PackageReleaseProblem
```

Available evidence retains, among other things:

```text
requested_package
normalized_package
requested_version
published_name
published_version
source_url
retrieved_at
last_serial
distribution_files
project_urls
```

Current identity checks require:

```text
normalize(published_name) == requested normalized package
published_version == exact requested_version
```

The exact published version is not replaced by PEP-440 equivalence here.

### Release-index lookup

```python
PyPIReleaseIndexClient.get_release_index(package)
```

returns the published release-version keys plus package/source identity and retrieval metadata.

That index can later be interpreted against `(old, proposed]` to establish the exact crossed releases.

---

## 13. A PyPI 404 is not treated as one undifferentiated failure

For an exact release URL returning 404, the client queries the package-level record to distinguish:

```text
package_not_found_or_inaccessible
```

from:

```text
version_not_found
```

Other current problem states include:

```text
identity_mismatch
malformed_response
acquisition_failed
```

This follows the broader project rule:

```text
missing / unavailable / malformed / conflicting
must not collapse into one generic false result
```

---

## 14. Real S001 mental walkthrough

Historical real-case substrate:

```text
pydantic/pydantic#13432
soupsieve 2.6 → 2.8.4
changed dependency source: uv.lock
```

The frozen Tranche-1 learning note at:

```text
learning/2026-08-15-tranche1-real-case-code-flows/
01_S001_NORMAL_APPLICATION_END_TO_END.md
```

shows the real application path at its own older source snapshot.

For the Group 4 concept, reason about S001 like this:

```text
exact base uv.lock
+
exact head uv.lock
        ↓
source-specific structural comparison
        ↓
ExtractedDependencyVersionChange
        ↓
PR-wide consensus boundary
        ↓
DependencyVersionChange(
    package="soupsieve",
    normalized_package="soupsieve",
    old_version="2.6",
    proposed_version="2.8.4",
)
        ↓
PEP 440 semantic parsing
        ↓
forward interval (2.6, 2.8.4]
        ↓
identify exact crossed upstream releases
```

At this point we still have **not** established:

- what semantic changes occurred in those releases;
- whether a Python support boundary changed;
- whether such a change applies to Pydantic;
- whether CI exercised the dependency;
- whether the PR is safe or should merge.

Those belong to later evidence responsibilities.

---

## 15. Failure behavior is part of the model, not cleanup noise

Useful current states to recognize:

| Boundary | Representative result | Meaning |
|---|---|---|
| source-specific dependency evidence | `malformed_dependency_file` | an admitted source cannot safely support a transition |
| PR-wide comparison | `multiple_dependency_version_changes` | several normalized packages changed; B2 cannot choose one silently |
| PR-wide comparison | `conflicting_dependency_version_changes` | sources disagree on exact transition |
| PEP 440 parse | `invalid_python_package_version` | raw version cannot enter supported semantic comparison |
| PEP 440 comparison | `equivalent_python_package_versions` | raw strings differ but no semantic forward release movement exists |
| PEP 440 comparison | `dependency_version_not_forward` | proposed semantic version is not greater |
| crossed releases | `crossed_release_outside_interval` | supplied release is not in `(old, proposed]` |
| crossed releases | `equivalent_crossed_release_versions` | two raw releases collapse to one semantic version identity |
| crossed releases | `proposed_release_missing` | exact raw proposed release was not present |
| PyPI | `version_not_found` | package exists but exact requested release was not established |
| PyPI | `identity_mismatch` | provider response conflicts with requested package/version identity |

A problem does not automatically mean an internal code defect. Many are expected evidence outcomes that prevent stronger trust.

---

## 16. Proof and non-proof boundaries

The current tests establish behavior for their exercised inputs and contracts. They do not turn the dependency-transition layer into a universal dependency solver.

### Current evidence supports

- shared PEP 503-style package comparison normalization;
- preservation of raw package/version identity;
- conservative PR-wide source reconciliation;
- exact-version agreement before semantic parsing;
- PEP 440 parse/order behavior;
- `(old, proposed]` interval semantics;
- exact raw proposed-release membership;
- explicit PyPI identity/failure states.

### This layer does not by itself prove

```text
dependency role
runtime environment membership
lock reachability
installation in CI
actual import/use
upstream semantic change
target relevance
technical consequence
compatibility
safety
maintainer action
```

This boundary discipline is essential. A precise dependency transition is a prerequisite for later reasoning, not the final reasoning.

---

## 17. Current fact, evidenced rationale, engineering judgment

### Current fact

At the pinned horizon:

- `normalize_package_name(...)` owns source-neutral Python distribution comparison identity;
- source-specific extraction is distinct from PR-wide `DependencyVersionChange` promotion;
- any admitted source problem blocks promotion;
- exact old/proposed strings must agree across dependency sources;
- PEP 440 parsing/ordering happens after exact strings are retained;
- the upstream interval is old-exclusive/proposed-inclusive;
- semantic equivalence does not substitute a different exact raw proposed release identity.

### Evidenced rationale

ADR-0004 records the decision to separate raw/exact source evidence, source-specific extraction, and shared PR-wide comparison so one parser or convenient file cannot become implicit PR-wide authority.

ADR-0005 records the decision to derive Python packaging semantics with `packaging.version.Version` while preserving exact source values.

### Engineering judgment

This layered treatment is slightly more explicit than directly converting every version string into one normalized semantic value, but the extra separation earns traceability and conflict detection that matter for an evidence-backed decision system.

---

## 18. What to master vs what to look up

### Must master / own

Be able to explain:

1. raw package spelling vs normalized package identity;
2. file-level extraction vs PR-wide trusted change;
3. why an admitted malformed/conflicting source cannot be ignored beside a valid one;
4. why exact version strings are preserved before PEP 440 semantics;
5. raw textual inequality vs semantic version equivalence;
6. why `(old, proposed]` is the correct crossed-release interval;
7. why semantic equivalence cannot replace the exact raw proposed release identity;
8. why exact dependency transition does not establish environment use, upstream impact, or safety.

### Understand operationally

- `normalize_package_name(...)`;
- `ExtractedDependencyVersionChange`;
- `DependencyVersionChange`;
- `DependencyChangeProblem`;
- `compare_extracted_dependency_changes(...)`;
- `ParsedDependencyReleaseInterval` / `PackagingVersionProblem`;
- crossed-release ordering;
- `PackageReleaseEvidence` / `PackageReleaseIndexEvidence`.

### Lookup-level

- complete dependency problem-code tuple;
- individual parser implementation details;
- every PyPI JSON field validator;
- exact helper names inside versioning/provider modules;
- all test fixtures.

### Deliberately deferred

- dependency declaration/environment/uv reachability — Group 5;
- target Python/environment evidence — Group 6;
- artifact serviceability — Group 7;
- CI consumption evidence — Group 8;
- impact/applicability/investigation — Group 9.

---

## 19. Fast relearning route

1. Read Sections **1–6** for identity and consensus.
2. Read Sections **7–11** for exact-vs-semantic version reasoning and `(old, proposed]`.
3. Read Section **14** to anchor the concepts in S001.
4. Rehearse:

```text
normalized package identity ≠ rewritten source evidence
file-level extraction ≠ PR-wide truth
exact version identity ≠ semantic version equivalence
(old, proposed] = crossed-release interval
precise transition ≠ target impact
```

5. Inspect current tests only if a failure-state or edge condition is unclear.

---

## 20. Evidence anchors

Accepted method owners:

- [`ADR-0004 — Dependency Version Change Evidence`](../docs/architecture/ADR-0004-dependency-version-change-evidence.md)
- [`ADR-0005 — Packaging Version and Python Line Method`](../docs/architecture/ADR-0005-packaging-version-and-python-line-method.md)

Stable constraints:

- [`UpgradePilot Core Invariants`](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md)

Current source at the pinned horizon:

- `src/upgradepilot/package_identity.py`
- `src/upgradepilot/dependency/change.py`
- `src/upgradepilot/dependency/versioning.py`
- `src/upgradepilot/pypi/release.py`
- `src/upgradepilot/upstream/interval.py`

Current proof surface:

- `tests/test_dependency_change_contracts.py`
- `tests/test_dependency_change_comparison.py`
- `tests/test_packaging_version_method.py`
- `tests/test_upstream_interval.py`

Frozen real-case learning reused by reference rather than copied:

- [`S001 Real-Case Code Flow`](2026-08-15-tranche1-real-case-code-flows/01_S001_NORMAL_APPLICATION_END_TO_END.md)

No bounded Audit was required for this note: the accepted ADRs/specifications and current source/tests agree on the responsibility and method boundaries taught here.
