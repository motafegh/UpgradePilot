# `uv.lock` Structural Admission, Version Transition, and Selected-Root Reachability

**Learning-artifact date:** 2026-09-07  
**Source/test evidence horizon:** `main@a6587bf2c4756702f1cb6506e60925652ce22c2e`  
**Roadmap coordination:** **Dependency declarations, environments, and `uv.lock` reachability** in `../../plans/UPGRADEPILOT_WHOLE_PROJECT_LEARNING_ARTIFACT_ROADMAP_PLAN.md`  
**Artifact role:** current frozen learning snapshot completing the `uv.lock` half of this roadmap group; it supersedes no historical learning file and preserves the important architecture evolution from earlier uv/environment reasoning  
**Target depth:** **must master / own** structural-owner vs consumer semantics, exact base/head transition evidence, explicit selected-root reachability, conditional/unresolved reasoning, and proof boundaries; understand TOML, graph traversal, witness paths, normalized package identity, and marker conditions operationally; keep uv-format breadth and exact API syntax lookup-assisted

This note answers three connected questions:

> **What facts does UpgradePilot admit once from the external `uv.lock` format so different consumers do not drift?**

> **How does one consumer derive an exact package-version transition from base/head lock evidence?**

> **How does another consumer determine whether that changed package is reachable from an explicitly selected uv environment root without claiming full environment formation?**

The current mental model is:

```text
exact uv.lock text
→ shared structural admission
→ UvLockStructure

                    ┌→ base/head transition consumer
UvLockStructure ────┤   → exact DependencyVersionChange
                    │
                    └→ selected-root reachability consumer
                        → reachable / not_established / unresolved
```

The critical ownership rule is:

> **Share external-format admission, not every downstream semantic interpretation.**

---

## 1. Why `uv.lock` needed a dedicated architecture

A universal lock contains much more information than:

```text
package name + version
```

It can contain:

```text
many package records
repeated records for one normalized package
local editable/virtual workspace packages
registry packages
source identity
normal dependencies
optional dependencies
dev dependency groups
activated extras
edge markers
resolution markers
artifact-download metadata
```

Two UpgradePilot responsibilities need some of that same external structure but ask different questions:

```text
TRANSITION QUESTION
What package version changed across exact base/head locks?

REACHABILITY QUESTION
From an explicitly selected project/group/extra root in the exact head lock,
is the changed package statically reachable?
```

If each consumer independently invented its own rules for what a valid package record means, they could disagree about basic lock facts before their semantic questions even began.

That pressure produced the current shared structural owner.

---

## 2. Shared structural owner: `uv_lock_structure.py`

Current owner:

```text
src/upgradepilot/dependency/uv_lock_structure.py
```

Public entry:

```python
parse_uv_lock_structure(content)
```

Current success result:

```text
UvLockStructure
├── schema_version
├── revision
├── packages: tuple[UvLockPackageRecord, ...]
└── by_name: normalized package → all matching records
```

Each package record preserves:

```text
index
package source spelling
normalized_package
version | None
source
record_data  # complete admitted TOML table
```

### What this owner admits

It owns shared external-format facts needed by both current consumers:

```text
TOML parseability
supported uv.lock schema version
non-negative lock revision
package field is an array of tables
valid distribution names
normalized package identity
valid textual package versions
narrow admitted meaning of versionless local editable/virtual records
preservation of repeated package records
complete raw record table for consumer-specific projection
```

### What it deliberately does not establish

```text
a dependency changed
which repeated resolution branch corresponds across revisions
selected environment roots
reachability
marker satisfiability
lock currentness
resolver correctness
installation
runtime behavior
compatibility
```

That is the key boundary.

---

## 3. One semantic parser owner does not mean one global parse object

An important current-code detail is easy to state incorrectly.

The architecture has **one owner of shared structural semantics**:

```text
parse_uv_lock_structure(...)
```

But the current consumers invoke that owner when they need to admit their exact lock inputs:

```text
uv_lock.py
→ parses exact base structure
→ parses exact head structure

uv_reachability.py
→ parses exact selected head lock structure
```

So the current principle is not:

```text
parse once in the whole application and pass one permanent object everywhere
```

It is:

```text
one canonical structural admission implementation
→ no duplicated independent TOML/package-record admission rules
```

This distinction matters when learning architecture:

> **Single semantic ownership and single runtime invocation are different concepts.**

The important thing is that transition and reachability cannot silently disagree about whether a versionless record, schema version, distribution name, or repeated package record is structurally admissible.

---

## 4. Why `record_data` is preserved

The shared structural record stores core common fields explicitly but also preserves the complete TOML record as:

```text
record_data
```

Why not parse every possible uv field in the shared layer?

Because current consumers need different additional semantics.

The transition consumer cares about things such as:

```text
source stability
resolution-marker context
non-artifact structural equality
```

The reachability consumer cares about:

```text
dependencies
optional-dependencies
dev-dependencies
edge marker/version/source discriminators
activated extras
resolution markers
```

If all those consumer semantics were pushed into one “universal dependency graph model,” the shared layer would begin owning meanings that only one responsibility actually needs.

Current design instead uses:

```text
small common admitted core
+ preserved source record
→ consumer-specific projection
```

That is a useful general architecture pattern for external formats.

---

## 5. Repeated package records: preserve ambiguity rather than invent identity

`UvLockStructure.by_name` stores **all** records for a normalized package.

It does not assume:

```text
first base record ↔ first head record
second base record ↔ second head record
```

because list position is not automatically semantic branch identity in a universal lock.

This matters later:

- the transition consumer may compare a complete repeated group as an order-independent multiset when it is unchanged;
- if a repeated group changes, it can abstain rather than pair branches heuristically;
- the reachability consumer requires discriminators when an edge could resolve to several repeated records.

### Core lesson

```text
preserve multiplicity at the structural boundary
→ let a semantic consumer decide whether it has enough identity to proceed
```

Do not erase ambiguity early just to make downstream code simpler.

---

## 6. Versionless workspace records: one shared interpretation

The shared parser admits `version=None` only for a narrow local source shape:

```text
source = { editable = "..." }
```

or:

```text
source = { virtual = "..." }
```

A registry package with no textual version is rejected structurally.

This is important because both semantic consumers need to agree on what versionlessness means.

Before the shared owner existed, separate consumers could drift on this basic interpretation.

Current invariant:

```text
version=None
→ admitted local editable/virtual structural record

not

version=None
→ unknown arbitrary package version
```

The focused structural test deliberately checks that an invalid versionless registry record is rejected once and then surfaces consistently as a problem for both transition and reachability paths.

---

## 7. Transition consumer: exact base/head package-version semantics

Current owner:

```text
src/upgradepilot/dependency/uv_lock.py
```

Public semantic entry:

```python
extract_uv_lock_changes(base_file, head_file)
```

Normal flow:

```text
admitted modified uv.lock ChangedFile
→ exact base RepositoryFileEvidence
→ exact head RepositoryFileEvidence
→ shared structural admission for each side
→ compare admitted package groups
→ ExtractedDependencyVersionChange
   OR typed DependencyChangeProblem
```

### Proof boundary

A successful result proves approximately:

> One exact textual package-version transition exists between these admitted base/head lock files under the current conservative comparison rule.

It does not prove:

```text
selected-root reachability
environment membership
CI installation/exercise
resolver currentness
runtime behavior
upgrade safety
```

---

## 8. Conservative transition comparison

The transition consumer compares all normalized package names appearing across the two structures.

For unique records, it checks that the semantic branch context has not changed unexpectedly.

Examples of unsupported structural change include:

```text
package added or removed
source changed
resolution-marker context changed
versionless local record changed materially
same version but non-artifact structure changed
```

The first transition rule wants a clean version transition, not an arbitrary lock rewrite.

### Artifact-download churn is treated separately

The transition comparison excludes only:

```text
sdist
wheels
```

from canonical non-version structural comparison.

Why?

Artifact metadata may legitimately change while the package/dependency semantic identity relevant to this transition question remains the same.

The narrow lesson is:

> **Ignore differences only when the consumer's accepted responsibility has evidence that those fields are irrelevant. Do not create a generic “ignore noisy fields” rule.**

---

## 9. Exactly one dependency version transition

The current dependency-analysis responsibility expects one trustworthy changed dependency.

Therefore the uv transition consumer stops on cases such as:

```text
no version transition
multiple package version transitions
package added/removed
ambiguous changed repeated records
unsupported structural change
malformed or unsupported lock structure
```

This is abstention by design.

A large lockfile is not treated as permission to guess which difference “probably” corresponds to the upgrade under investigation.

---

## 10. From uv transition to `UvLockDependencyContext`

Once PR-wide dependency analysis accepts the uv-derived transition, it translates the source provenance into:

```text
UvLockDependencyContext
```

The context binds:

```text
repository
head revision
normalized changed package
exact uv.lock source evidence
```

This gives reachability the exact package/source identity it needs without giving it the transition consumer's internal comparison machinery.

Architecture:

```text
uv transition extraction
→ generic DependencyVersionChange + source provenance
→ UvLockDependencyContext
→ later reachability reasoning
```

The reachability consumer does not need to recompute the version change.

---

## 11. Environment selection arrives from a different evidence owner

Reachability also requires an independently observed static project environment declaration from:

```text
src/upgradepilot/dependency/environment_selection.py
```

Example:

```bash
uv sync --group docs
```

may yield a declaration like:

```text
manager = uv
operation = sync
project_root = ...
selectors = (DependencyGroupSelector("docs"),)
package_scope = bound_project
```

This declaration proves visible static selection—not lock reachability and not execution.

Reachability begins only after combining:

```text
changed package/source context
+
static uv selection declaration
+
exact lock evidence
```

---

## 12. Selected-root reachability owner

Current owner:

```text
src/upgradepilot/dependency/uv_reachability.py
```

Public function:

```python
evaluate_uv_selected_root_reachability(
    context,
    declaration,
    *,
    lock_file,
)
```

Current result states are intentionally small:

```text
reachable
not_established
unresolved
```

with additional explanation fields such as:

```text
reason
detail
normalized_package
project_root
selectors
reachability_kind
witness_root
witness_path
conditional_candidate_path
unresolved_conditions
```

---

## 13. Why the proposition is “selected-root reachability,” not “environment membership”

The current implementation deliberately narrowed the claim to what exact lock structure and explicit selectors can establish safely.

It asks:

> **Is the changed package reachable from one explicitly selected lock root under the bounded static graph model?**

It does not claim complete uv environment formation.

Why this narrower proposition?

Because full environment formation could require additional knowledge about:

```text
uv default groups/configuration
workspace discovery beyond the bound package
marker evaluation against a concrete target environment
resolver satisfiability
lock currentness
actual command execution
```

The current code does not own all of those facts.

This is an important product-design move:

```text
broad desired question
→ inspect actual evidence capability
→ narrow to the strongest proposition the implementation can prove honestly
```

---

## 14. Reachability-specific projection from the shared structure

The shared `UvLockStructure` does not pre-build one universal graph.

Instead, `uv_reachability.py` projects the fields it needs from admitted records into private reachability structures:

```text
_ReachabilityPackage
_ReachabilityEdge
_ReachabilityLock
```

It validates reachability-specific fields such as:

```text
resolution markers
dependencies
optional-dependencies
dev-dependencies
edge version/source discriminators
edge markers
activated extras
```

This is not duplication of structural admission.

The shared parser already established:

```text
record is an admitted package record
package identity is valid
version/source core shape is admitted
```

The reachability projection establishes only the extra fields whose meaning is required for graph traversal.

---

## 15. Binding the selected project root

A uv declaration is bound to a project root.

The reachability owner relates that root to an editable/virtual local package in the lock.

Example:

```text
project_root = services/api
lock contains local package source = { editable = "services/api" }
→ bind that package as the selected project package
```

The current design deliberately avoids using a project-name cross-check as proof of lock currentness.

The material relation for this bounded proposition is the exact project-root path to the local lock package's source path.

### Why this is stronger than “take every workspace root”

Earlier environment reasoning was tempted toward broad workspace-root inference.

The current design requires an explicit selected project/root relation instead of assuming:

```text
package exists somewhere in workspace
→ therefore it belongs to the selected environment
```

This is a major architecture correction worth retaining.

---

## 16. Selected roots: groups and extras

Once the bound local project package is known, selectors resolve to explicit graph roots from that package's lock record.

Examples:

```text
DependencyGroupSelector("docs")
→ package.dev-dependencies["docs"]

OptionalExtraSelector("email")
→ package.optional-dependencies["email"]

AllDependencyGroupsSelector()
→ all represented dev-dependency groups in that bound lock package

AllOptionalExtrasSelector()
→ all represented optional extras in that bound lock package
```

Notice the evidence owner:

> For this reachability proposition, the selected roots are taken from the **exact lock record**, not re-derived from `pyproject.toml`.

The project-source declaration and lock-backed reachability responsibilities remain separate.

---

## 17. Breadth-first search and witness paths

The current traversal uses a queue based on:

```python
collections.deque
```

and performs bounded graph traversal from the selected roots.

Conceptually:

```text
selected roots
→ visit nearest dependencies
→ resolve each edge to a safe lock package record
→ carry activated extras and unresolved conditions
→ stop when changed package is reached
```

A successful result records a witness path.

Real-case-shaped example:

```text
mkdocs-llmstxt
→ beautifulsoup4
→ soupsieve
```

Result:

```text
state = reachable
reachability_kind = transitive
witness_root = mkdocs-llmstxt
witness_path = (mkdocs-llmstxt, beautifulsoup4, soupsieve)
```

A direct root can produce:

```text
witness_path = (soupsieve,)
reachability_kind = direct
```

### Why witness paths matter

A boolean `True` would throw away the reason.

The path provides:

```text
explainability
focused test evidence
future debugging information
input for later CI/proof reasoning
```

while still remaining only static lock-backed evidence.

---

## 18. Edge discriminators and repeated records

If a normalized package has several lock records, an edge may need enough information to select one safely.

Possible discriminating fields include:

```text
version
source
```

If the edge does not establish which repeated record it refers to, the current reachability result remains unresolved rather than selecting by list position.

This carries forward the structural-owner principle:

```text
structural layer preserves repeated records
→ reachability consumer demands enough edge identity
→ ambiguity remains explicit
```

---

## 19. Activated dependency extras

An edge may activate extras on an intermediate dependency.

The current traversal carries those activated extras so optional dependencies of the reached package can become part of the path.

Example shape:

```text
docs root
→ mkdocs-material[imaging]
→ optional dependency beautifulsoup4
→ soupsieve
```

This is a useful reminder that graph reachability is not always just:

```text
follow package.dependencies
```

The environment selection and edge semantics can change which outgoing edges are relevant.

---

## 20. Marker/resolution conditions: diagnostic path, not false certainty

The current reachability model does **not** evaluate arbitrary uv/PEP environment markers against a concrete target runtime here.

If a structural path exists only through conditions such as:

```text
python_version >= '3.12'
```

it can preserve:

```text
conditional_candidate_path
unresolved_conditions
```

while returning:

```text
state = unresolved
```

not:

```text
state = reachable
```

Example:

```text
mkdocs-llmstxt
→ beautifulsoup4
→ soupsieve
```

with a marker on the final edge can become a diagnostic candidate path, but it is not promoted to unconditional reachability.

### Even contradictory-looking markers stay diagnostic

The current module does not claim that collected conditions are mutually satisfiable.

Therefore a path containing conditions like:

```text
python_version < '3.12'
python_version >= '3.12'
```

remains unresolved diagnostic evidence rather than being interpreted as a valid reachable environment.

Central lesson:

> **Preserve a useful candidate explanation without upgrading its epistemic strength.**

---

## 21. `reachable`, `not_established`, and `unresolved`

These states have different evidence strength.

### `reachable`

At least one selected root has one unconditional deterministically resolved lock-backed path to the changed package.

### `not_established`

The bounded root domain represented by this result was exhaustively traversed and no witness was found.

This is not a repository-wide or runtime absence claim.

### `unresolved`

Available evidence cannot safely establish either result.

Examples:

```text
lock unavailable or identity mismatch
unsupported/invalid lock structure
selected root cannot bind safely
selector missing from bound lock package
repeated-record ambiguity
conditional/marker-only candidate
resource bound reached
all-workspace scope cannot be fully exhausted
```

### Why `not_established` is stronger than `unresolved`

```text
not_established
→ the modeled bounded domain was exhausted

unresolved
→ the modeled domain/evidence was incomplete or ambiguous
```

That difference should survive later aggregation rather than being flattened into `False`.

---

## 22. `all_workspace_packages`: positive witness vs incomplete negative proof

The current selector model can preserve an explicit uv package scope:

```text
bound_project
all_workspace_packages
```

For an all-workspace declaration, one sound positive witness from the currently bound package is still useful:

```text
reachable path found
→ reachable
```

But absence of a witness from the currently bound package does not establish absence across every workspace package if complete workspace-member discovery is not owned here.

So the result remains:

```text
unresolved
reason = workspace scope not exhausted
```

This is another strong evidence rule:

> **Positive existential proof and negative exhaustive proof often require different amounts of evidence.**

---

## 23. Cycle safety and bounded traversal

Dependency graphs can contain cycles.

The traversal maintains visited-state information and bounded limits rather than recursively following edges forever.

Current code also defines explicit resource bounds for:

```text
maximum visited states
maximum path depth
```

If safe exhaustive reasoning cannot continue within the admitted bound, the result should remain unresolved rather than silently truncating and claiming no path.

The general lesson is:

```text
bounded algorithmic safety
must preserve epistemic honesty
```

A resource cutoff is not evidence of dependency absence.

---

## 24. Real UpgradePilot anchor: pydantic dependency-update shape

A representative real shape already used throughout UpgradePilot is:

```text
pydantic/pydantic dependency update
soupsieve 2.6 → 2.8.4
```

The selected uv documentation group can expose a lock-backed transitive witness shaped like:

```text
docs group
→ mkdocs-llmstxt
→ beautifulsoup4
→ soupsieve
```

The focused reachability test deliberately proves that this path can be established from the exact lock **without requiring `pyproject.toml` as an input to the reachability function**.

Why is that useful?

Because the responsibilities are separated:

```text
workflow observer
→ what uv group/extra was explicitly selected

lock owner/reachability
→ what the exact lock says is reachable from that selected root

project-source evidence
→ separate responsibility when needed
```

No layer has to pretend it owns every environment fact.

---

## 25. The historical architecture correction

The older August learning material captured an earlier uv/environment mental model in which lock membership, workspace/root interpretation, and environment reasoning were more tightly mixed.

As the project encountered richer universal-lock and selected-environment pressure, that became too weak.

The current progression is better summarized as:

```text
earlier broad uv membership/root inference
→ pressure from repeated records, workspace packages, markers, source identity, and different consumers
→ shared structural admission owner
→ source-specific transition consumer
→ explicit static environment selector
→ exact selected project-root binding
→ reachability-specific graph projection
→ witness / not-established / unresolved result
```

A particularly important correction is:

```text
all packages/workspace roots inferred broadly
!=
explicit selected-root evidence
```

The project now asks what exact root/scope the workflow declaration establishes and what the exact lock can prove from that root.

### Another important correction

Do not summarize the final architecture as “both consumers share one giant parsed dependency graph.”

They share **structural admission**, while consumer-specific semantics stay independent:

```text
transition
→ base/head change semantics

reachability
→ root/edge/traversal semantics
```

That avoids two opposite failures:

```text
duplicate basic parser truth
→ semantic drift

over-centralize every consumer meaning
→ giant ambiguous abstraction
```

---

## 26. Tests that protect the current architecture

### Shared structure

```text
tests/test_uv_lock_structure.py
```

Protects examples including:

```text
versionless local workspace record admission
repeated record preservation
invalid versionless registry record rejection
shared consumer agreement on that rejection
bool schema version not treated as integer 1
unsupported schema versions
invalid textual versions
```

A subtle Python lesson appears here:

```python
isinstance(True, int)  # True
```

so the structural parser uses exact type checks for integer schema/revision fields to avoid TOML `true` being admitted accidentally as integer `1`.

### Transition semantics

```text
tests/test_uv_lock_change.py
tests/test_uv_lock_versionless_records.py
```

Protect the exact base/head transition contract, repeated-record ambiguity, versionless behavior, unsupported structural changes, and the one-change rule.

### Selected-root reachability

```text
tests/test_uv_selected_root_reachability.py
tests/test_uv_package_scope.py
```

Protect scenarios including:

```text
real S001-shaped transitive witness
direct witness
no witness after complete bound-project traversal
all-workspace negative result remains unresolved
project-root binding to nested local package
missing selector remains unresolved
all groups / all extras roots from lock
activated dependency extras
repeated-record edge ambiguity
cycle safety
marker-only conditional candidates
resolution-marker candidates
source/revision/path mismatch
unavailable exact lock
```

### Proof/non-proof

These tests are strong executable specifications of intended behavior, but this learning-authoring session did not run them and therefore does not claim a fresh aggregate PASS result.

Even when green, they do not prove:

```text
all uv formats/versions
complete uv resolver semantics
actual command execution
lock currentness
installed runtime package versions
behavioral compatibility
upgrade safety
```

---

## 27. Important technical mechanisms

### Must understand operationally

**TOML / `tomllib`**  
The lock is parsed as TOML, then admitted into a narrower product-specific structural model.

**package normalization**  
Graph identity and comparison use normalized distribution names while preserving source spelling for explanation.

**mapping/list preservation**  
Repeated package records are preserved instead of collapsed prematurely.

**consumer projection**  
One admitted source record can be projected differently by transition and reachability consumers without duplicating the common admission rules.

**graph nodes and edges**  
Packages are nodes; selected dependency relations are directed edges used by bounded reachability.

**breadth-first search**  
A queue explores paths from selected roots and naturally yields a short witness when one is found.

**`collections.deque`**  
Efficient queue structure used for traversal. Exact method syntax is lookup-level; queue-based traversal is the learning target.

**cycle/visited-state handling**  
Needed so dependency cycles do not create infinite traversal or false reachability.

**marker/resolution conditions**  
Preserved as unresolved conditions rather than treated as automatically true.

### Lookup/deferred

```text
complete uv lock-file specification
all uv CLI/config semantics
full marker satisfiability solver
resolver algorithm internals
advanced graph-algorithm theory
performance tuning beyond current bounded limits
```

Learn those only when a real UpgradePilot responsibility requires them.

---

## 28. Current facts, rationale, judgment, and future triggers

### Current implementation fact

UpgradePilot has one shared bounded `uv.lock` structural admission owner. The transition consumer uses it for exact base/head version-change semantics; the reachability consumer uses it plus reachability-specific projection for explicit selected-root graph reasoning.

### Evidenced rationale

Current source docstrings, focused tests, the reconciliation design, and the historical learning snapshots all support the split: basic external lock facts should not drift across consumers, while transition and reachability remain distinct semantic responsibilities.

### Engineering judgment

The current design is a strong middle ground:

```text
shared enough
→ one structural truth

not over-shared
→ no generic all-purpose dependency graph/domain model
```

Its cost is repeated consumer adaptation and more explicit types. That cost is preferable to hidden semantic coupling while the consumers truly ask different questions.

### Re-entry triggers

Revisit the architecture when real evidence requires:

```text
new uv schema versions
additional repeated-record/fork identity semantics
actual marker evaluation against a target environment
complete workspace-member discovery
full uv default environment/config formation
resolver/currentness proof
runtime installation evidence
another consumer needing the same currently-private graph fields
```

If several consumers independently need exactly the same additional field semantics, that is evidence to move those semantics toward the shared structural layer. Do not move them there preemptively.

---

## 29. Fast relearning route

Use this sequence:

```text
1. Recall: shared structural truth != transition semantics != reachability semantics.
2. Open uv_lock_structure.py and inspect UvLockStructure / UvLockPackageRecord.
3. Explain why repeated records and versionless local records are preserved/admitted there.
4. Open uv_lock.py and trace exact base/head structure → one transition.
5. Open environment_selection.py and recall how an explicit uv group/extra/root is established.
6. Open uv_reachability.py and trace selected root → graph traversal → witness/unresolved result.
7. Read the S001-shaped reachability test and one marker/repeated-record test.
8. State exactly what a reachable witness does and does not prove.
```

---

## 30. Ownership / transfer questions

Without this note, explain:

1. Why should transition and reachability share structural admission but not necessarily one complete graph model?
2. Why does `UvLockStructure.by_name` preserve repeated records instead of choosing one?
3. What exact meaning does `version=None` have after structural admission?
4. Why can a changed repeated package group force transition abstention?
5. Why does the reachability function not need `pyproject.toml` content for its current proposition?
6. What is the difference between `reachable`, `not_established`, and `unresolved`?
7. Why can an all-workspace scope produce a sound positive witness but still fail to justify a negative conclusion?
8. Why is a marker-conditioned path preserved diagnostically instead of promoted to `reachable`?
9. If an edge points to a package name that has two lock records and provides no version/source discriminator, why is list position not enough?
10. Why is “one shared structural parser owner” different from “the application parses the lock exactly once globally”?

Transfer exercise:

> Imagine a future third consumer needs package license metadata from `uv.lock`, while transition and reachability do not. Where should license interpretation start: in the shared structural core, or in the third consumer? Explain what repeated cross-consumer evidence would justify moving it into shared admission later.

---

## 31. Source and evidence anchors

Current evidence horizon:

```text
main@a6587bf2c4756702f1cb6506e60925652ce22c2e
```

Primary current source:

```text
src/upgradepilot/dependency/uv_lock_structure.py
src/upgradepilot/dependency/uv_lock.py
src/upgradepilot/dependency/uv_reachability.py
src/upgradepilot/dependency/environment.py
src/upgradepilot/dependency/environment_selection.py
src/upgradepilot/dependency/analysis.py
```

Focused tests:

```text
tests/test_uv_lock_structure.py
tests/test_uv_lock_change.py
tests/test_uv_lock_versionless_records.py
tests/test_uv_selected_root_reachability.py
tests/test_uv_package_scope.py
```

Historical/reconciliation evidence:

```text
learning/2026-08-17-Cluster1-5-B2 Dependency Environment and CI Consumption Evidence.md
learning/2026-08-17-b2-dependency-environment-ci-consumption-mastery/
plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md
```

Exact historical filenames are retained above only as provenance. Current concepts and navigation use semantic responsibility names.

This file is a frozen learning snapshot. It does not control the live project position, authorize product changes, or claim more proof than the cited current source/tests provide.

`UP-SKILL:upgradepilot-learning-artifact`
