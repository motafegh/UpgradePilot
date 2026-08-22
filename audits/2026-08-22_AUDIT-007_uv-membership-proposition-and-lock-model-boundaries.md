# AUDIT-007 — uv Membership Proposition and Lock-Model Boundaries

**Date:** 2026-08-22  
**Audit type:** bounded architecture / evidence-proposition / implementation-boundary review  
**Inspected UpgradePilot revision:** `476a0626a7e7ba1c4347b5a5aa7276ed5e09f991`  
**Primary real pressure:** S001 — `pydantic/pydantic#13432`, Soup Sieve `2.6 -> 2.8.4`  
**Transfer pressure:** S011 optional-extra activation/coverage; S005 tox/uv-mediated lock consumption  
**Related audits:** AUDIT-004 resolver/currentness boundary; AUDIT-006 internal evidence-type/revalidation boundary  
**Authority:** non-controlling audit evidence. This file records findings and future reassessment requirements; it does not itself change product behavior, authorize a refactor, reopen accepted historical validation, or change live continuation.

## 1. Trigger and question

Plan-02 learning raised a specific design challenge in:

```text
src/upgradepilot/dependency/uv_membership.py
```

The initial question was whether exact `pyproject.toml` evidence is genuinely necessary when exact `uv.lock` already materializes the selected dependency-group/extra roots and dependency graph.

The investigation widened into the more important question:

> What exact proposition should UpgradePilot's uv membership responsibility establish, what evidence is necessary for that proposition, and does the current selection/lock model preserve enough real uv semantics for its positive and negative-ish results to remain sound?

This audit therefore does **not** ask whether the existing code should simply be made shorter. It examines:

- proposition naming and proof strength;
- why `pyproject.toml` is currently mandatory and what it actually contributes;
- project/lock coherence versus lock-backed reachability;
- uv group/default/workspace selection semantics;
- the real S001 `--all-packages --group docs` command;
- positive witness versus `not_established` completeness requirements;
- duplicated `uv.lock` structural interpretation;
- non-package workspace-root dependency groups;
- the possible role of `uv workspace metadata`;
- security/execution constraints;
- the correct reconciliation point before ordinary application integration.

## 2. Current implemented proposition

Current source:

- [`../src/upgradepilot/dependency/uv_membership.py`](../src/upgradepilot/dependency/uv_membership.py)
- [`../src/upgradepilot/dependency/environment_selection.py`](../src/upgradepilot/dependency/environment_selection.py)
- [`../src/upgradepilot/dependency/environment.py`](../src/upgradepilot/dependency/environment.py)

`uv_membership.py` states its bounded responsibility accurately in its module documentation:

```text
exact changed package from uv.lock
+ exact project/lock source at one immutable revision
+ one static uv environment-selection declaration
-> whether the changed package is reachable from explicitly selected group/extra roots
```

Its result is:

```text
member(direct | transitive)
not_established
unresolved
```

with a witness path for positive membership.

The implementation deliberately does **not** establish:

```text
lock freshness/currentness
resolver satisfiability
runtime command execution
installation/environment formation
exact runtime version observation
behavioral exercise
compatibility/safety/action
```

That proof boundary remains sound and should be preserved.

## 3. Real S001 evidence

Authoritative scenario record:

- [`../product-simulation/scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/CASE.md`](../product-simulation/scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/CASE.md)

Frozen S001 identity:

```text
repository: pydantic/pydantic
PR:         #13432
base:       652a61ce4f9d7d76eaada31535807a485ece0e21
head:       aa2dc024d33f61cdef50bf1973ab5adf0a974f5a
change:     soupsieve 2.6 -> 2.8.4
```

GitHub's changed-file listing for the real PR contains only:

```text
uv.lock
```

and the PR patch changes the Soup Sieve package record/version/artifact metadata rather than `pyproject.toml`.

The exact-head CI docs-build command preserved in S001 is:

```text
uv sync --all-packages --group docs
```

See:

- [`../product-simulation/scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/artifacts/raw/ev-008-ci-docs-build.yml`](../product-simulation/scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/artifacts/raw/ev-008-ci-docs-build.yml)

Exact-head `pyproject.toml` provides, among other data:

```text
[project]
name = pydantic

[dependency-groups]
dev = [...]
docs = [..., mkdocs-llmstxt, ...]
...

[tool.uv]
default-groups = ['dev']

[tool.uv.workspace]
members = ['pydantic-core']
```

The lock-backed dependency path retained by the scenario is:

```text
mkdocs-llmstxt
-> beautifulsoup4
-> soupsieve
```

The real S001 positive proposition is therefore naturally pressure-tested by:

```text
static command explicitly selects docs
+
exact lock records a docs root that reaches Soup Sieve
-> positive lock-backed witness
```

The scenario and Cluster-4/5 source/test evidence do **not** by themselves establish complete real-case application integration; Cluster 6 remains the ordinary application/CLI integration point in the selected B2 plan.

## 4. What `pyproject.toml` currently contributes inside membership

Current private project model:

```python
_ParsedProject(
    normalized_name,
    optional_extras,
    dependency_groups,
)
```

`_parse_project(...)` requires a valid `[project].name` and records only the normalized project name plus the **names** of optional extras and dependency groups.

It does not retain or reconcile the dependency contents of those project groups/extras.

Current use of project metadata is therefore principally:

```text
project name
-> help bind one workspace package in uv.lock

project group/extra names
-> cross-check that an explicitly selected name exists in pyproject.toml

project-file path
-> bind declaration project_root to exact project location
```

The actual graph roots are then taken from the bound lock package's:

```text
optional-dependencies
dev-dependencies
```

### Consequence

For the narrow proposition:

> Does one explicitly selected lock-backed group/extra root reach the changed package?

S001 demonstrates that `pyproject.toml` **content** is not inherently required to discover the positive `docs -> ... -> soupsieve` path: the exact lock already materializes the relevant workspace package, group roots, and dependency edges.

However, that does **not** imply that `pyproject.toml` is generally irrelevant to uv semantics. Project configuration can affect defaults, workspace behavior, package identity, and other command semantics. The architecture question is therefore where those facts belong and which proposition needs them.

## 5. Current project cross-check does not establish project/lock currentness

Current membership parsing checks that a selected group/extra name appears in exact `pyproject.toml` and in the bound lock package.

It does **not** establish:

```text
project declaration contents == lock materialization
```

because the dependency contents of the project group/extra are discarded by `_ParsedProject`.

It also does not establish:

```text
uv.lock is current against exact-head project metadata
```

or:

```text
a fresh uv resolver run would leave the lock unchanged
```

That distinction is already correctly recognized by:

- [`2026-08-16_AUDIT-004_uv-lock-resolution-satisfiability-evidence-boundary.md`](2026-08-16_AUDIT-004_uv-lock-resolution-satisfiability-evidence-boundary.md)
- [`../plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md`](../plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md)

AUDIT-004's proof ladder keeps separate:

```text
L1  lock exists/parses
L2  lock current against project metadata
L3  uv lock --check succeeds
L4  target-relevant locked sync succeeds
L5  relevant runtime behavior succeeds
```

Therefore project/lock currentness should not be implied by the current membership cross-check. If currentness/coherence is later selected, it requires its own explicit proposition and proof.

## 6. Real uv selection semantics materially exceed the current selector model

Official uv documentation verified on 2026-08-22:

- https://docs.astral.sh/uv/reference/cli/
- https://docs.astral.sh/uv/concepts/projects/dependencies/
- https://docs.astral.sh/uv/concepts/projects/sync/

Material semantics include:

### 6.1 `--all-packages`

For `uv sync`, `--all-packages` syncs all workspace packages. uv documents that extras or groups supplied through `--extra`, `--group`, or related options are applied to all workspace members.

Real S001 uses exactly:

```text
uv sync --all-packages --group docs
```

### 6.2 default groups

uv includes the `dev` dependency group by default unless project configuration changes the default groups. `tool.uv.default-groups` can replace that default set.

Real S001 explicitly has:

```toml
[tool.uv]
default-groups = ['dev']
```

### 6.3 `--group` versus `--only-group`

`--group docs` includes that group in addition to the project's other admitted/default selection semantics.

`--only-group docs` is materially different: uv documents that it omits the project and its dependencies and implies no default groups.

### 6.4 lock update before sync

uv documents that `uv sync` re-locks the project before syncing unless `--locked` or `--frozen` is provided.

Therefore:

```text
static repository lock membership
!= proof that runtime CI consumed an unchanged exact lock graph
```

This remains a separate currentness/runtime-correlation proposition.

## 7. Current selector/membership abstraction loses material uv command scope

### 7.1 `--all-packages` is not represented

`src/upgradepilot/dependency/environment_selection.py` currently represents:

```text
manager
operation
segment_index
project_root
selectors
```

and recognizes explicit extras/groups, all-extras/all-groups, project path, and bounded negative/targeting flags.

It does not preserve `--all-packages` as a typed selection/workspace-scope fact.

The focused S001-style selection test passes a command containing `--all-packages`, but tests only the explicit group/extra selector result; workspace-wide scope is not retained.

### 7.2 membership binds one workspace package

`src/upgradepilot/dependency/uv_membership.py::_bind_workspace_package(...)` resolves one workspace package by:

```text
normalized project name
+
editable/virtual source path relative to lock root
```

`_selected_roots(...)` then reads selected groups/extras only from that one package.

Thus the real command:

```text
uv sync --all-packages --group docs
```

is represented for membership approximately as:

```text
one bound project package
+
explicit docs roots on that package
```

rather than:

```text
all workspace members
+
docs applied across that workspace scope
```

### 7.3 `mode='only'` is preserved but not used by membership

`DependencyGroupSelector` correctly preserves:

```text
mode = include | only
```

but `_selected_roots(...)` treats both as a request to retrieve the same group roots and does not use the mode to change the broader proposition.

This is acceptable only if the proposition remains narrowly:

```text
explicit selected-group root reachability
```

It is insufficient if the result is interpreted as complete command-selected environment membership.

## 8. Positive witness and `not_established` have asymmetric completeness requirements

This distinction is central.

### Positive result

To establish:

```text
member
```

one sound selected root and one unconditional lock-backed witness path are sufficient.

For S001:

```text
explicit docs selector
+
valid Pydantic docs root
+
mkdocs-llmstxt -> beautifulsoup4 -> soupsieve
-> positive membership witness
```

The existence of additional default/workspace roots does not invalidate that positive witness.

### `not_established`

To establish:

```text
not_established
```

UpgradePilot must have completely traversed **all roots belonging to the proposition being claimed** without finding a witness and without material ambiguity.

If a command is workspace-wide but the model evaluates only one workspace member, a no-witness result cannot safely mean:

```text
membership was not established for the complete real command-selected scope
```

unless all relevant scope was actually represented.

Therefore scope loss is more dangerous for negative-ish results than for one-path positive evidence.

## 9. Proposition choice: do not silently build a complete uv environment interpreter

The investigation identifies two different possible responsibilities.

### Proposition A — explicit-root reachability

```text
one statically explicit uv group/extra selection
+
exact admitted lock graph
-> does an explicit selected root reach the changed package?
```

This is close to what current `uv_membership.py` actually implements.

### Proposition B — complete command-selected uv environment

```text
project/base dependencies
+ default groups/config
+ explicit inclusions/exclusions
+ extras
+ --only-* semantics
+ workspace/member targeting
+ --all-packages
+ package/config/project discovery
+ relevant marker/conflict semantics
-> complete package environment selected by the command
```

This is substantially broader.

### Disposition

The evidence does **not** justify building Proposition B now merely for completeness.

UpgradePilot's selected B2 plan explicitly rejects a universal package-manager/environment framework and asks for the smallest bounded semantics required by real pressure.

S001's current decision-relevant need is satisfied by a strong positive explicit-root witness. A complete uv environment interpreter would introduce complexity far beyond the demonstrated proposition.

The preferred direction is therefore to keep a **narrow explicit-root/reachability responsibility**, but make its naming, inputs, scope, and `not_established` semantics honest about what it exhausts.

## 10. Workspace scope still matters inside the narrow proposition

Avoiding a complete environment interpreter does not mean workspace scope can be ignored.

A future bounded selection declaration may need to preserve enough scope to answer which explicit roots are in the command's admitted domain, conceptually for example:

```text
current project
all workspace packages
specific workspace package
```

Exact type names/design are **not selected by this audit**.

For S001, `--all-packages` should not need a complete uv reimplementation; it may be sufficient to preserve the workspace scope so:

- one valid member's `docs` witness can still establish positive membership immediately;
- a future no-witness result cannot become `not_established` until every in-scope explicit root required by the bounded proposition has been exhausted.

## 11. Duplicate `uv.lock` structural interpretation is a real maintenance risk

Current source contains two independent uv lock parsers with overlapping format knowledge:

```text
src/upgradepilot/dependency/uv_lock.py
src/upgradepilot/dependency/uv_membership.py
```

### `uv_lock.py`

Owns dependency-transition extraction and parses/validates:

```text
schema version
lock revision
package records
package names
versions
workspace local-source shapes
repeated records
canonical comparison structure
```

### `uv_membership.py`

Independently parses/validates:

```text
schema version
lock revision
package records
package names
versions
sources
resolution markers
dependencies
optional dependencies
dev dependencies
edge markers/extras
```

Some duplication is expected because transition comparison and graph reachability need different semantic views. The concern is duplicated **structural format truth**.

### Demonstrated divergence

`uv_lock.py` accepts a versionless package record only when its source is one admitted editable/virtual workspace shape.

`uv_membership.py::_parse_lock_package(...)` accepts `version=None` without imposing the same workspace-source restriction.

The normal current path may still be protected because `UvLockDependencyContext` is produced after earlier transition extraction, but this divergence demonstrates the maintenance risk:

```text
one external format
-> two independently maintained structural admission rules
-> contract drift becomes possible
```

This is not a reason to create a generic dependency-graph framework. It is pressure for the smallest **uv-specific shared structural lock model/parser** that can feed separate transition and reachability responsibilities without duplicating fundamental schema rules.

## 12. `pyproject.toml` should be used only where its proposition requires it

This audit does not recommend deleting project evidence from UpgradePilot.

`pyproject.toml` is essential in other admitted responsibilities, including S011-style source-established optional-extra/dependency-group evidence.

For uv, project metadata/config may be necessary for propositions involving:

```text
project identity not recoverable safely from admitted lock structure
workspace/config discovery
default-groups behavior
complete group/extra declaration semantics
project/lock coherence/currentness
non-lock tool configuration
```

But the current membership use should not require project content merely to repeat facts already materialized in the admitted lock unless that cross-check establishes a separately named, decision-relevant proposition.

Preferred discipline:

```text
lock-backed explicit-root reachability
-> consume only evidence necessary for reachability + sound root/scope binding

project/lock coherence/currentness
-> separate proposition with sufficiently strong reconciliation evidence

pyproject-source membership
-> source-owned project environment responsibility
```

## 13. Non-package workspace-root groups expose another current boundedness limit

Current `_parse_project(...)` requires a valid `[project].name`.

The Python Dependency Groups specification (PEP 735), however, supports dependency groups for development/internal use cases, including projects that are not built for distribution:

- https://packaging.python.org/en/latest/specifications/dependency-groups/

Current uv workspace metadata documentation also models a workspace root that defines dependency groups while not itself being a package.

Therefore a generic statement that current membership supports every valid uv workspace/group shape would be incorrect.

This does **not** require immediate support for non-package roots. The correct action is to make the admitted boundary explicit and add support only when real product pressure justifies it.

## 14. `uv workspace metadata` is relevant but not an automatic product replacement

Official uv documentation verified on 2026-08-22:

- https://docs.astral.sh/uv/reference/internals/metadata/
- https://docs.astral.sh/uv/concepts/preview/

uv now provides:

```text
uv workspace metadata
```

and explicitly advises tools wanting access to information encoded by `uv.lock` to prefer the metadata output because the lockfile format is not a stable interface guaranteed for third-party consumers.

The metadata exposes graph entry points for:

```text
workspace root
workspace members
packages
extras
dependency groups
dependency edges
markers
conflicts/multiple-version structure
```

This aligns closely with UpgradePilot's membership needs.

### Why it should not be adopted automatically

The feature is currently preview/unstable and its schema version is `preview`.

More importantly, UpgradePilot's [`../SECURITY.md`](../SECURITY.md) treats target repository content and dependency tooling as untrusted evidence and does not allow repository/tool execution merely because read-only inspection is authorized.

Executing uv against an investigated repository introduces questions about:

```text
project discovery/config
network/index/cache access
lock/update behavior
build metadata/build backend interaction
credentials/environment inheritance
untrusted execution surface
version-specific uv behavior
```

Therefore:

```text
uv recommends workspace metadata for tooling
!= UpgradePilot is authorized or required to execute it in ordinary analysis
```

### Near-term candidate role

A proportionate future use is as a **developer/experiment validation oracle on controlled fixtures**:

```text
our bounded static lock interpretation
vs
uv's own metadata graph on controlled inputs
```

This can reveal parser/semantic drift without making external command execution part of product runtime.

Any production adoption requires a separately selected, security-reviewed bounded responsibility.

## 15. Relationship to AUDIT-006

AUDIT-006 established:

```text
weak/permissive exact-file evidence type
-> downstream defensive revalidation
```

and recommended strengthening trusted internal evidence contracts before deleting repeated checks.

AUDIT-007 is distinct:

```text
what proposition does uv membership own?
+
what uv command/lock/project semantics does that proposition actually require?
+
where is structural lock knowledge duplicated?
```

A future refactor should coordinate the two audits rather than treating them independently:

```text
AUDIT-006
strengthen exact evidence contracts

AUDIT-007
clarify uv selection/reachability contract and shared lock structure

then
remove only validation/parsing duplication made genuinely redundant
```

Do not use AUDIT-007 as justification to delete current defensive exact-file checks before AUDIT-006's contract issue is resolved.

## 16. Relationship to AUDIT-004

AUDIT-004 remains the owner of the distinct resolver/currentness opportunity.

Keep these propositions separate:

```text
exact static lock-backed reachability
!= lock currentness against project declarations
!= fresh resolver satisfiability
!= sync/install success
!= runtime behavior
```

Current S001 command does not use `--locked` or `--frozen`; official uv semantics say sync normally re-locks before syncing. Therefore static repository membership plus successful CI must not be promoted into an exact runtime-lock-consumption claim without additional evidence.

## 17. Relationship to S011 and S005

### S011

S011 demonstrates a different and legitimate project-source responsibility:

```text
changed dependency established inside [project.optional-dependencies].mlx
+
workflow selects dev rather than mlx
-> affected optional environment consumption not established
```

This supports keeping source-established project membership separate from uv lock graph reachability.

### S005

S005 demonstrates that lock consumption can be mediated through tox plus `uv-venv-lock-runner` rather than a direct `uv sync` command.

Therefore a reusable uv lock graph/reachability model should not be inseparably coupled to one command interpreter. Selection interpretation and lock reachability should remain distinct responsibilities joined through typed evidence.

## 18. Findings

### AUDIT-007-F1 — Current positive S001 explicit-root witness remains technically defensible — GREEN

The real S001 command explicitly selects `docs`, and the admitted lock graph supplies a transitive path from a selected docs root to Soup Sieve.

Additional workspace/default roots do not invalidate one sound positive witness.

Do not discard the accepted Cluster-4/5 historical evidence merely because the broader abstraction needs reconciliation.

### AUDIT-007-F2 — The current type/name is close to a stronger whole-environment claim than the implementation actually proves — YELLOW

`UvSelectedEnvironmentMembership` may be read as membership in the complete environment selected by uv, while the module actually proves reachability from explicit positive group/extra roots only.

Before wider integration, either:

- narrow naming/contract language to explicit-root reachability; or
- strengthen implementation to the larger semantics actually claimed.

The first option is currently preferred because it matches demonstrated product need with lower complexity.

### AUDIT-007-F3 — Mandatory project-content cross-check is not sufficiently justified for narrow lock-backed reachability — YELLOW

For S001, exact lock structure already carries the positive docs roots and dependency graph. Current project parsing contributes name/group/extra namespace corroboration but does not establish full project/lock coherence/currentness.

Do not keep mandatory project acquisition/parsing in the core reachability path merely because the existing implementation already has it. Reassess each project fact against the exact proposition it establishes.

### AUDIT-007-F4 — `--all-packages` scope loss is a material semantic gap — YELLOW / BLOCK BEFORE BROAD INTEGRATION

The real S001 command is workspace-wide, but the current selection declaration drops that scope and membership binds one workspace package.

This does not refute the positive S001 witness, but it can make a no-witness/`not_established` result incomplete for commands whose explicit groups/extras apply across several members.

Preserve enough workspace/package scope before relying on this abstraction broadly in Cluster-6 application integration.

### AUDIT-007-F5 — `include` versus `only` group mode is preserved upstream but not reflected in membership proposition — YELLOW

The current selector records `mode='include'|'only'`, but membership uses only the named group's roots.

If the responsibility is explicitly root reachability, document that this mode does not change the root's own reachability.

If any caller interprets the result as complete environment membership, the current behavior is insufficient.

### AUDIT-007-F6 — project defaults matter to complete environment semantics but should not force a complete interpreter now — GREEN/YELLOW GUARD

S001's `tool.uv.default-groups=['dev']` proves that project metadata can genuinely affect complete `uv sync` selection.

The lesson is not “always parse more pyproject.” It is:

> only claim complete environment semantics when all decision-relevant selection inputs are represented.

The current product need does not justify implementing all of those semantics yet.

### AUDIT-007-F7 — duplicate lock structural parsers create demonstrated drift risk — YELLOW

`uv_lock.py` and `uv_membership.py` independently encode overlapping uv lock schema/package admission rules and already differ on versionless-record validation.

Before more uv responsibilities are added, evaluate a narrow shared uv-specific structural parser/model. Keep transition comparison and reachability as separate semantic consumers.

### AUDIT-007-F8 — current parser does not cover every valid dependency-group/workspace shape — YELLOW / BOUNDEDNESS

Requiring `[project].name` excludes valid dependency-group-only/non-package-root shapes.

This is acceptable only as an explicit admitted boundary. Do not market or internally reason about the implementation as universal uv workspace membership.

### AUDIT-007-F9 — `uv workspace metadata` is a valuable reference/oracle candidate, not yet an ordinary runtime dependency — WATCH

The feature could reduce dependence on unstable lock internals and provides stronger graph entry points, but its preview status plus UpgradePilot's untrusted-execution boundary make immediate product adoption unjustified.

Evaluate it first as controlled comparison evidence if/when a bounded experiment is selected.

### AUDIT-007-F10 — currentness/resolver/runtime questions remain separate and should not be solved by adding more static cross-checks inside membership — GREEN

Keep AUDIT-004's ladder intact. Do not use partial `pyproject.toml` reconciliation as a surrogate for lock-currentness evidence.

### AUDIT-007-F11 — reconciliation should occur before Cluster-6 ordinary application integration — YELLOW / TIMING

Current B2 state has Clusters 0–5 accepted and Cluster 6 not yet integrated through the ordinary application path.

This is the lowest-cost point to reconcile the uv membership contract before it becomes a deeper application/CLI dependency.

This audit does not itself change the selected plan or live continuation; when B2 Cluster 6 is next selected, load this audit before implementation and explicitly disposition these findings.

## 19. Preferred future architecture direction

The smallest currently justified direction is conceptually:

```text
STATIC WORKFLOW COMMAND
        ↓
bounded uv selection interpretation
        ↓
EXPLICIT UV SELECTION DECLARATION
- project/workspace location
- explicit group/extra selectors
- minimum workspace/package scope required by admitted command form
- material include/only mode retained
        │
        │
        ▼
EXACT TRUSTED uv.lock STRUCTURE
        ↓
selected explicit lock roots
        ↓
bounded universal-lock reachability
        ↓
EXPLICIT-ROOT MEMBERSHIP EVIDENCE
member | not_established | unresolved
```

Separately:

```text
PROJECT/LOCK COHERENCE OR CURRENTNESS
exact project/config + exact lock + stronger check
-> separate evidence
```

Separately:

```text
RUNTIME RESOLVER/SYNC OBSERVATION
-> separately authorized evidence
```

And separately:

```text
CI COMPOSITION
static consumption evidence
+ exact-head runtime authority
-> bounded CI coverage
```

This preserves responsibility ownership while avoiding a general package-manager framework.

## 20. Candidate shared uv lock structure — evaluate, do not preselect exact API

A future reconciliation should compare the smallest shape that lets one structural interpretation feed multiple uv consumers, for example conceptually:

```text
RepositoryTextFile(uv.lock)
        ↓
parse/validate one admitted uv lock schema
        ↓
ParsedUvLock
        ├── package/repeated-record structure
        ├── source identity
        ├── dependency edges / marker data needed by membership
        └── raw/canonical semantic structure needed by transition comparison
```

Then:

```text
uv_lock.py
-> owns base/head transition comparison

uv_membership.py (or renamed narrow owner)
-> owns explicit-root reachability
```

Do **not** automatically introduce:

```text
GenericDependencyGraph
PackageManagerGraph
UniversalEnvironment
Validated[T]
GraphFramework
```

A shared primitive is justified only where its semantics are genuinely identical across the two existing uv consumers.

## 21. Recommended pre-Cluster-6 reconciliation sequence

When this audit is explicitly selected for implementation/reconciliation:

1. **Freeze the exact proposition first.**
   - Prefer explicit selected-root reachability unless a real case demonstrates need for complete environment formation semantics.

2. **Inventory real admitted uv command forms from S001 plus active tests.**
   - classify which flags affect explicit root identity, project/workspace scope, defaults, exclusions, and complete-environment semantics;
   - do not implement unneeded flags merely because uv supports them.

3. **Preserve material scope needed for sound positive and `not_established` results.**
   - S001 `--all-packages` is the first concrete pressure.

4. **Decide which `pyproject.toml` facts the narrow proposition actually requires.**
   - retain project/config evidence where it establishes necessary binding/scope;
   - remove it from the core path only after equivalent required identity is safely available elsewhere;
   - do not confuse name corroboration with currentness.

5. **Evaluate a narrow shared uv lock structural model/parser.**
   - reconcile schema/package/source admission;
   - preserve repeated records, universal-lock branches, dependency edges, extras, and markers required by current consumers;
   - do not create a generic graph framework.

6. **Coordinate with AUDIT-006.**
   - strengthen exact-file evidence contracts before deleting defensive source/provenance checks;
   - preserve relational/rebinding checks.

7. **Rework tests by responsibility.**
   - real S001-shaped tests should preserve `--all-packages` scope where that is the admitted command;
   - domain tests should not manufacture provider-integrity failures except when testing a real domain rebinding responsibility;
   - add a multi-member workspace case proving that positive and `not_established` behavior respects scope;
   - preserve universal-lock ambiguity/cycle/bounds tests.

8. **Optionally run a controlled `uv workspace metadata` comparison experiment.**
   - controlled local fixtures only;
   - no target-repository mutation;
   - no automatic production adoption;
   - classify differences between UpgradePilot's static model and uv's own graph output.

9. **Pressure S001, S011, and S005 again.**
   - S001: positive lock-backed docs witness remains available;
   - S011: project-source optional-extra semantics remain separate;
   - S005: lock graph is not coupled to direct `uv sync` only.

10. **Run focused, nearest-integration, and complete deterministic validation.**

11. **Only then enter ordinary Cluster-6 application/CLI integration.**

If reconciliation creates a consequential durable cross-module structural method, record it in the appropriate ADR. Do not create an ADR merely for renaming a result type or extracting one parser helper.

## 22. Required proof for accepting a future reconciliation

Do not accept a refactor because it removes lines or dependencies.

Required evidence should include:

- exact S001 positive witness remains established without package-name hardcoding;
- `--all-packages` scope is represented sufficiently for the admitted proposition;
- a multi-workspace-member no-witness case cannot incorrectly become `not_established` after inspecting only one member;
- direct/transitive witness paths remain explanatory;
- universal-lock marker/fork ambiguity still produces `unresolved` when material;
- cycles and traversal bounds remain safe;
- malformed/unsupported lock structure still degrades explicitly;
- transition extraction retains all current conservative base/head semantics;
- shared structural lock parsing does not weaken either consumer's proof boundary;
- project/lock currentness remains a separate claim;
- S011 `dev != mlx` behavior remains intact;
- S005 remains representable as separate mediated lock-consumption pressure rather than forcing tox support into uv membership;
- exact-file provider/rebinding guarantees remain at least as strong as before;
- focused + nearest integration + complete deterministic suites pass.

## 23. What not to do

Do not respond to this audit by:

```text
removing pyproject.toml everywhere
```

or:

```text
adding every uv flag/default/conflict/workspace rule to one giant interpreter
```

or:

```text
executing uv workspace metadata on untrusted targets by default
```

or:

```text
merging resolver/currentness/runtime evidence into static membership
```

or:

```text
creating a generic package-manager graph framework
```

or:

```text
deleting current provenance checks before AUDIT-006's strong-type issue is resolved
```

The desired result is not maximal modeling and not minimal code. It is:

> **the smallest proposition whose inputs and scope are sufficient for a sound, decision-relevant claim, with each invariant owned once and each stronger claim kept separate.**

## 24. Final disposition

Current assessment:

```text
S001 POSITIVE EXPLICIT-ROOT WITNESS               GREEN
DIRECT / TRANSITIVE WITNESS MODEL                 GREEN
TRI-STATE FAILURE/UNCERTAINTY MODEL                GREEN
UNIVERSAL-LOCK AMBIGUITY CONSERVATISM              GREEN
CYCLE / RESOURCE BOUNDS                            GREEN

WHOLE-ENVIRONMENT-SOUNDING CONTRACT/NAMING         YELLOW
MANDATORY PYPROJECT CONTENT IN NARROW REACHABILITY YELLOW
PROJECT/LOCK CURRENTNESS INSIDE MEMBERSHIP          KEEP SEPARATE
--ALL-PACKAGES WORKSPACE SCOPE PRESERVATION         YELLOW / PRE-INTEGRATION BLOCK
INCLUDE/ONLY COMPLETE-ENVIRONMENT SEMANTICS         YELLOW / BOUNDED CLAIM ONLY
DUPLICATE uv.lock STRUCTURAL PARSING                YELLOW
NON-PACKAGE WORKSPACE-ROOT GROUP SUPPORT            BOUNDED / NOT GENERAL
uv workspace metadata                              WATCH / CONTROLLED EVALUATION CANDIDATE
AUDIT-006 TYPE/REVALIDATION COORDINATION            REQUIRED FOR REFACTOR
```

Preferred continuation when this engineering concern is next selected:

```text
DO NOT rewrite the implementation immediately.

First:
freeze explicit-root reachability as the likely proposition
→ preserve real workspace scope required by admitted commands
→ identify the minimum truly necessary project facts
→ evaluate one shared uv-specific lock structural model
→ coordinate exact-evidence strengthening with AUDIT-006
→ pressure real S001/S011/S005
→ validate
→ only then integrate broadly through Cluster 6
```

The current code is a conservative and useful first bounded implementation, but this investigation does **not** support treating its present interface/inputs as the optimal final architecture. The next improvement should make the proposition more exact, not merely add more checks or remove evidence.