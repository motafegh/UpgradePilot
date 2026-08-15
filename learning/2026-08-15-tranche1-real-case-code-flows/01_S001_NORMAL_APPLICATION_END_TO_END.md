# S001 Real-Case Code Flow — Pydantic / Soup Sieve 2.6 → 2.8.4

**Learning snapshot date:** 2026-08-15  
**UpgradePilot source/test snapshot:** `ef4283db0a7ce3eec75a56ccc5c07354015fd2e3`  
**Depth target:** implementation-adjacent understanding of the current normal application path  
**Case:** `pydantic/pydantic#13432`  
**Frozen target base:** `652a61ce4f9d7d76eaada31535807a485ece0e21`  
**Frozen target head:** `aa2dc024d33f61cdef50bf1973ab5adf0a974f5a`  
**Dependency transition:** `soupsieve 2.6 → 2.8.4`

This is a reusable learning snapshot, not a live project tracker and not a new product claim. The source/test commit above is the code baseline taught here. The real case evidence is preserved under:

- [`../../product-simulation/scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/CASE.md`](../../product-simulation/scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/CASE.md)
- [`../../working-memory/2026-08-05_B2-step-7f-normal-path-live-s001-proof.md`](../../working-memory/2026-08-05_B2-step-7f-normal-path-live-s001-proof.md)

The August 5 live proof ran an earlier source revision. Where Tranche-1 later changed CI vocabulary/semantics, this note teaches the accepted `ef4283db...` source and labels the older observed result separately.

---

## 1. What this case is for

S001 is our best **normal application-orchestration** learning case because the real public PR has already passed through the ordinary CLI/application path and reached the upstream semantic + target relevance machinery.

The learning question is not:

> “Was this PR safe?”

The learning question is:

> **How does one real dependency-update proposal become typed evidence objects, branch into independent investigations, and eventually produce bounded conclusions through the actual UpgradePilot functions?**

The mental model to master is:

```text
public PR locator
    ↓
CLI interface
    ↓
application orchestrator
    ↓
exact PR identity + changed files
    ↓
canonical dependency transition
    ↓
┌──────────────── CI branch ────────────────┐
│ exact-head runs/jobs + workflow files     │
│ → bounded CI support result               │
└───────────────────────────────────────────┘
    +
┌──────── package/upstream branch ──────────┐
│ exact release → upstream repo → interval  │
│ → tagged changelog → support-drop claim   │
└───────────────────────────────────────────┘
    ↓ if a grounded claim justifies it
impact candidate / unresolved applicability
    ↓
selected exact target investigation
    ↓
exact-head target Python declaration
    ↓
target relevance
    ↓
reevaluated impact applicability
    ↓
PublicPullRequestInvestigation
    ↓
CLI rendering
```

The branches are deliberately not forced into one synthetic “confidence” value.

---

# Part A — First know the real input

## 2. Frozen S001 identity

The real proposal is:

```text
repository:       pydantic/pydantic
PR:               13432
base SHA:         652a61ce4f9d7d76eaada31535807a485ece0e21
head SHA:         aa2dc024d33f61cdef50bf1973ab5adf0a974f5a
changed file:     uv.lock
dependency:       soupsieve
old version:      2.6
proposed version: 2.8.4
```

The first major engineering principle is already visible:

```text
"Pydantic main"
!=
"the exact Pydantic state proposed by PR #13432"
```

A branch moves. A commit SHA is immutable. UpgradePilot tries to bind later evidence to the frozen PR head/base rather than silently reading whatever the repository looks like today.

### MUST MASTER

**Identity is part of evidence.**

A file, workflow result, target declaration, changelog, or package fact is useful only when we can say what repository/package/revision it belongs to.

---

# Part B — CLI → application boundary

## 3. Entry point: `src/upgradepilot/cli.py`

Normal invocation:

```bash
python -m upgradepilot pydantic/pydantic 13432
```

The important function is:

```python
main(argv)
```

Its responsibility is intentionally narrow:

```text
parse arguments
take GITHUB_TOKEN from environment
call application orchestration
map boundary failures to exit codes
render typed results
```

It calls:

```python
investigate_public_pull_request(
    "pydantic/pydantic",
    13432,
    token=...,
)
```

### Why this separation matters

`cli.py` should not become the product brain.

```text
CLI = interface/presentation boundary
investigation.py = application sequencing boundary
```

If UpgradePilot later has an API, GUI, service, or another interface, those should reuse the application/domain logic rather than copy the investigation into presentation code.

### Read at the snapshot

```bash
git show ef4283db0a7ce3eec75a56ccc5c07354015fd2e3:src/upgradepilot/cli.py
```

---

# Part C — Application orchestration begins

## 4. `investigate_public_pull_request(...)`

File:

```text
src/upgradepilot/investigation.py
```

This is the central application-level sequencing function for the current B2 public-PR slice.

It first constructs or receives provider clients:

```text
GitHubPullRequestClient
GitHubActionsClient
GitHubRepositoryClient
PyPIReleaseClient
PyPIReleaseIndexClient
UpstreamRepositoryResolver
GitHubTagCommitClient
GitHubChangelogPathClient
support-drop evaluator
```

This is orchestration, not a universal abstraction. Each provider/domain still owns its own facts and semantics.

The result container is:

```python
PublicPullRequestInvestigation
```

Think of it as a typed bundle of the independently produced branch results—not as proof that every field must be available.

---

# Part D — Freeze PR authority

## 5. `GitHubPullRequestClient.get_pull_request(...)`

Conceptual transformation:

```text
"pydantic/pydantic", 13432
        ↓
PullRequestIdentity
```

The identity carries the proposal coordinates that downstream work relies on, including the exact base/head revisions.

Then:

```python
changed_files = pull_client.get_changed_files(pull_request)
```

For S001 the material changed-file record is:

```text
uv.lock (modified)
```

### Why both identity and changed files are needed

The PR title is not enough.

A title may say “Bump soupsieve,” but the product must inspect the actual admitted dependency source and establish a canonical transition from repository evidence.

---

# Part E — Canonical dependency change from `uv.lock`

## 6. `analyze_dependency_change(...)`

File:

```text
src/upgradepilot/dependency/analysis.py
```

Call from `investigation.py`:

```python
analysis_result = analyze_dependency_change(
    pull_request,
    changed_files,
    repository_client,
)
```

This is a PR-wide dependency-evidence integration boundary.

For an admitted `uv.lock` file it does **not** trust the patch alone. It requests complete exact files:

```python
repository_client.get_pull_request_base_file(...)
repository_client.get_pull_request_head_file(...)
```

Those become strong `RepositoryTextFile` evidence objects with exact revision/file provenance.

Then `dependency/uv_lock.py` performs:

```text
exact base uv.lock
+
exact head uv.lock
    ↓
TOML parse
    ↓
conservative package-record comparison
    ↓
ExtractedDependencyVersionChange
```

The PR-wide comparison then produces the canonical:

```python
DependencyVersionChange(
    package="soupsieve",
    normalized_package="soupsieve",
    old_version="2.6",
    proposed_version="2.8.4",
    ...
)
```

### The key output wrapper

`analyze_dependency_change(...)` returns:

```python
DependencyChangeAnalysis(
    dependency=...,
    direct_requirements_install_path=...,
)
```

For **S001**, the transition came from `uv.lock`, not an admitted direct requirements file. Therefore:

```text
dependency = soupsieve 2.6 → 2.8.4
direct_requirements_install_path = None
```

This detail becomes very important in the CI branch.

### MUST MASTER

```text
canonical dependency identity
!=
direct CI installation path
```

We know what dependency changed. We do **not** automatically know a direct `requirements*.txt` file that a workflow installs.

---

# Part F — The application splits into independent evidence branches

Once `dependency_result` is a `DependencyVersionChange`, `investigation.py` activates multiple downstream responsibilities.

Do not imagine this as one linear confidence score.

```text
DependencyVersionChange
   ├── CI branch
   └── package/upstream/impact/target branch
```

A failure or unresolved result in one branch does not automatically erase evidence from the other branch.

That was visible in the real S001 live proof: the CI exercise remained unresolved while the package/upstream/target-Python path still reached a grounded relevance conclusion.

---

# Part G — CI runtime acquisition

## 7. Runtime evidence: `github/actions.py`

`investigation.py` calls:

```python
workflow_runs = actions_client.get_exact_head_workflow_runs(pull_request)
```

This provider queries GitHub Actions with the frozen PR head SHA.

It produces:

```python
WorkflowRun
```

with factual runtime fields such as:

```text
run_id
workflow_id
name
event
head_sha
status
conclusion
run_attempt
```

For every run:

```python
actions_client.get_workflow_jobs(pull_request, run)
```

produces `WorkflowJob` records and, when available, `WorkflowStep` summaries.

### Runtime evidence means runtime facts

For example:

```text
run status = completed
run conclusion = success
job conclusion = success
```

This is stronger than static YAML for the proposition “did this run/job succeed?”

But it still does not automatically answer:

```text
which exact static run declaration corresponds to which runtime step?
which dependency version was actually imported?
was the changed dependency’s behavior exercised?
```

That is why static and runtime evidence remain separate contracts.

---

# Part H — Exact workflow source acquisition

## 8. `GitHubRepositoryClient.get_exact_head_workflow_file(...)`

For each exact-head runtime run, the application also acquires the workflow definition associated with that run.

Conceptually:

```text
WorkflowRun
+ frozen PullRequestIdentity
    ↓
workflow-run metadata path reconciliation
    ↓
RepositoryTextFile
```

`RepositoryTextFile` is crucial because it binds:

```text
repository
requested/returned path
revision
blob SHA
byte counts
UTF-8 content
retrieval time
```

The provider is responsible for exact acquisition/provenance—not CI meaning.

---

# Part I — Current Tranche-1 CI semantics on S001

## 9. `WorkflowDependencyExerciseInput`

For each workflow the application builds:

```python
WorkflowDependencyExerciseInput(
    run=run,
    jobs=jobs,
    definition=exact_workflow_file,
)
```

Then:

```python
evaluate_dependency_ci_exercise(
    dependency_result,
    exercise_inputs,
    direct_requirements_install_path=direct_requirements_install_path,
)
```

File:

```text
src/upgradepilot/ci/dependency_exercise.py
```

### The decisive S001 input

Remember:

```text
direct_requirements_install_path = None
```

The current CI rule deliberately refuses to turn generic lockfile evidence into a direct installation declaration.

For an otherwise successful workflow, `_evaluate_workflow_dependency_exercise(...)` therefore stops at:

```text
reason = direct_requirements_install_path_unavailable
state  = unresolved
```

The aggregate remains unresolved when successful CI exists but no admitted bounded dependency-exercise path is established.

### Historical live observation vs current source wording

The August 5 live S001 proof, on earlier source, observed an unresolved CI result with the older reason/vocabulary `dependency_exercise_not_proven`.

Tranche 1 later corrected the active proof language. The strongest positive state is now:

```text
supported_not_correlated
```

and unresolved remains the correct family when the admitted static dependency path cannot be established.

**Do not rewrite the historical live proof.** Learn the current semantics from the accepted snapshot source.

---

# Part J — Where the new workflow IR fits

## 10. Provider-owned static workflow structure

File:

```text
src/upgradepilot/github/workflow_definition.py
```

Entry point:

```python
parse_workflow_definition(source: RepositoryTextFile)
```

The pipeline is:

```text
RepositoryTextFile.content
    ↓
PyYAML BaseLoader representation nodes
    ↓
bounded graph/depth traversal
    ↓
typed GitHub Actions static IR
```

Key provider types include:

```text
WorkflowDefinition
StepsJobDefinition
ReusableWorkflowJobDefinition
RunStepDefinition
UsesStepDefinition
JobProblem
StepProblem
StaticScalarValue / StaticSequenceValue / StaticMappingValue
RunDefaults
```

### A real S001 workflow pressure

The exact S001 `ci.yml` head contains many jobs, including:

```text
docs-build
test
test-mypy
test-plugin
coverage jobs
core jobs
...
```

The real `docs-build` job declares roughly:

```yaml
runs-on: ubuntu-latest
...
- uses: astral-sh/setup-uv@...
  with:
    python-version: '3.12'
- name: Install dependencies
  run: uv sync --all-packages --group docs
- run: uv run python -c 'import docs.plugins.main'
- run: PYTHONPATH=... uv run mkdocs build
```

The shared provider IR is intentionally capable of preserving the **multi-job structure** rather than calling it malformed.

But the current CI consumer `inspect_workflow_commands(...)` intentionally admits only **one statically readable local job**, because Tranche 1 did not implement static↔runtime job correlation or cross-job environment reasoning.

Therefore:

```text
provider can parse many jobs
!=
CI consumer may safely choose one
```

This is one of the most important Tranche-1 lessons.

### Why S001 does not currently reach this parser inside the CI evaluator

Because the earlier guard already sees:

```text
direct_requirements_install_path = None
```

So current `dependency_exercise.py` does not call `inspect_workflow_commands(...)` for that successful workflow.

The IR is still real, tested product infrastructure; it simply is not needed to justify a stronger S001 CI proposition under the current bounded rule.

---

# Part K — Shared direct-install observer

## 11. `dependency/direct_install.py`

Reusable entry point:

```python
observe_direct_installation_declaration(...)
```

It recognizes a deliberately bounded family such as:

```text
pip install -r requirements.txt
python -m pip install --requirement requirements-dev.txt
```

and resolves requirement paths against working-directory precedence:

```text
step working-directory
> job defaults.run.working-directory
> workflow defaults.run.working-directory
> repository root
```

It returns:

```text
observed
not_observed
unresolved
```

Its proof strength stops at:

```text
static declaration
```

not:

```text
execution
success
exact proposed version installed
package exercised
```

### Why it cannot establish the S001 docs environment

S001’s relevant docs workflow uses:

```text
uv sync --all-packages --group docs
```

The current shared direct-install primitive does **not** implement generic uv group resolution or dependency graph tracing.

The historical manual simulation could inspect the lock/manifest relationship and conclude more about that docs environment. The automated Tranche-1 primitive intentionally does not generalize that far.

### MUST MASTER

**Manual discovery evidence can be stronger/different than the currently automated product rule.**

That is not a contradiction if the claim scopes are recorded honestly.

---

# Part L — Package evidence

## 12. PyPI exact release

After the independent CI branch, `investigation.py` executes:

```python
package_client.get_release(
    dependency_result.package,
    dependency_result.proposed_version,
)
```

For S001:

```text
soupsieve == 2.8.4
```

The resulting `PackageReleaseEvidence` is package/distribution authority, not target compatibility authority.

The prior live S001 proof observed:

```text
published package: soupsieve==2.8.4
distribution files: 2
```

---

# Part M — Upstream repository identity

## 13. `UpstreamRepositoryResolver.resolve(...)`

The application next tries to establish the trusted upstream repository associated with the exact published release.

For S001 the prior live proof established:

```text
facelessuser/soupsieve
```

with PyPI provenance coverage for the release files.

Mental model:

```text
package name
!=
trusted GitHub repository identity
```

The relationship must be established from admitted package metadata/provenance rather than guessed from a search result.

---

# Part N — Old-exclusive / proposed-inclusive release interval

## 14. `release_interval_from_dependency_change(...)`

From:

```text
2.6 → 2.8.4
```

UpgradePilot constructs the semantic interval question:

```text
what accepted upstream releases were crossed after 2.6 and through 2.8.4?
```

Then:

```python
release_index_client.get_release_index("soupsieve")
select_crossed_release_index(...)
```

The live S001 proof established:

```text
2.7
2.8
2.8.1
2.8.2
2.8.3
2.8.4
```

This is much better than reading only the proposed release’s latest notes, because a dependency jump can cross multiple releases carrying materially different changes.

---

# Part O — Exact proposed tag and changelog authority

## 15. Tag resolution

`investigation.py` calls its bounded helper:

```python
_resolve_proposed_version_tag(...)
```

It admits two canonical spellings:

```text
2.8.4
v2.8.4
```

It does not perform arbitrary fuzzy tag guessing.

If a tag is established, the application calls:

```python
changelog_client.discover(repository, resolved_commit_sha)
```

then acquires the changelog as an exact `RepositoryTextFile` at that immutable upstream commit.

---

# Part P — Build authoritative interval evidence

## 16. `build_tagged_changelog_evidence(...)`

The exact tag + changelog source is combined with the release interval.

Then:

```python
assemble_upstream_interval_authority(...)
```

can produce:

```python
AuthoritativeUpstreamIntervalEvidence
```

The live S001 proof recorded:

```text
authority basis: tagged_changelog
```

This object is the bounded semantic source window supplied to the semantic extraction responsibility.

---

# Part Q — LLM candidate extraction is not authority

## 17. `evaluate_support_drop_runtime(...)`

The active support-drop path uses the bounded upstream authority and the local semantic extractor.

The important architecture is:

```text
trusted exact source window
    ↓
LLM candidate extraction
    ↓
deterministic source reconstruction / validation
    ↓
GroundedPythonSupportDropClaim
```

For S001 the live proof observed:

```text
Python line dropped: 3.8
introduced in release: 2.8
```

### MUST MASTER

The model does **not** own:

```text
package identity
repository identity
release ordering
source authority
exact source coordinates
target relevance
compatibility
maintainer action
```

It proposes semantic candidates inside a bounded evidence window. Deterministic code admits or rejects them.

---

# Part R — Impact candidate before target evidence

## 18. `build_python_support_drop_impact_candidate(...)`

Once a grounded support-drop claim exists, UpgradePilot can formulate a mechanism-specific candidate:

```text
Soup Sieve dropped Python 3.8 support
→ could matter to Pydantic if Pydantic still targets Python 3.8
```

This is a candidate, not yet a conclusion.

Then:

```python
evaluate_python_support_drop_impact(impact_candidate)
```

without target evidence initially returns an unresolved applicability assessment.

This is intentional:

```text
upstream changed
!=
target affected
```

---

# Part S — Investigation selection

## 19. `select_python_support_drop_investigation(...)`

The unresolved candidate tells the planner what missing target proposition would discriminate the case.

For this mechanism, the bounded selected target is the exact target Python declaration:

```text
pyproject.toml @ exact PR head
```

Before acquisition, `investigation.py` checks that the selected repository/revision still equal the frozen PR identity.

That invariant prevents the investigation selector from silently wandering to another repository or moving revision.

---

# Part T — Exact target declaration

## 20. `interpret_target_python_declaration(...)`

The application executes:

```python
repository_client.get_exact_head_text_file(
    pull_request,
    "pyproject.toml",
)
```

Then:

```python
interpret_target_python_declaration(...)
```

The live S001 proof observed:

```text
path: pyproject.toml
revision: aa2dc024d33f61cdef50bf1973ab5adf0a974f5a
requires-python: >=3.10
```

This is Target evidence tied to the exact proposed head—not an assumption based on the project’s current documentation.

---

# Part U — Target relevance

## 21. `evaluate_target_python_relevance(...)`

Inputs:

```text
GroundedPythonSupportDropClaim: Python 3.8 dropped
TargetPythonDeclaration: requires-python >=3.10
```

Output observed in the live S001 proof:

```text
outside_declared_python_range
```

Meaning, under the accepted bounded method, the target’s declared Python range does not include the dropped 3.8 line.

It does **not** mean:

```text
whole dependency update is safe
all upstream changes are irrelevant
CI is sufficient
merge is automatically authorized
```

It answers one proposition only:

> Does this particular upstream Python-support-drop candidate overlap the target’s declared Python support?

---

# Part V — Reevaluate the impact candidate

## 22. `evaluate_python_support_drop_impact(...)` again

The same candidate is evaluated again, now with acquired target relevance evidence.

Conceptual flow:

```text
candidate
+
target relevance
    ↓
refined applicability
```

For the Python-3.8 mechanism, this supports a non-applicability conclusion for that mechanism under the target declaration.

This is an example of the canonical product-decision pattern:

```text
candidate
→ unresolved proposition
→ selected investigation
→ new evidence
→ reevaluate candidate
```

---

# Part W — Final application object and rendering

## 23. `PublicPullRequestInvestigation`

The orchestrator returns one typed application result carrying heterogeneous branch evidence:

```text
pull_request
changed_files
dependency_result
direct_requirements_install_path
workflow_evidence
ci_exercise_result
package_result
upstream_repository_result
release_index_result
crossed_release_result
tag_commit_result
changelog_path_result
tagged_changelog_result
upstream_interval_result
upstream_support_drop_result
target_python_result
target_python_relevance_result
pre-investigation impact
selected investigation
post-investigation impact
```

Some fields may be `None` or problem results. That is expected.

The CLI then renders the evidence without becoming the owner of its meaning.

---

# Part X — S001 object ledger

Use this table while studying source.

| Stage | Important type/object | What it represents | What it does NOT prove |
|---|---|---|---|
| PR acquisition | `PullRequestIdentity` | exact proposal identity | dependency semantics |
| changed files | `ChangedFile` | repository mutation record | canonical dependency transition |
| exact source | `RepositoryTextFile` | immutable text + provenance | semantic meaning |
| dependency | `DependencyVersionChange` | canonical package/version transition | target impact |
| dependency analysis | `DependencyChangeAnalysis` | transition + optional direct install source | CI execution |
| runtime CI | `WorkflowRun` / `WorkflowJob` | GitHub runtime facts | static command mapping |
| workflow input | `WorkflowDependencyExerciseInput` | one runtime/static evidence bundle | correlation |
| CI result | `DependencyCIExerciseResult` | current bounded CI support state | compatibility/safety |
| package release | `PackageReleaseEvidence` | exact published release/artifacts | target relevance |
| upstream repo | `UpstreamRepositoryEvidence` | established repository identity | every upstream claim true |
| interval | `AuthoritativeUpstreamIntervalEvidence` | bounded crossed-release semantic authority | target effect |
| support-drop | `GroundedPythonSupportDropClaim` | admitted upstream mechanism claim | target applicability |
| target Python | `TargetPythonDeclaration` | exact target declared Python range | runtime environment |
| target relevance | `TargetPythonRelevanceResult` | overlap/non-overlap proposition | whole-PR recommendation |
| application | `PublicPullRequestInvestigation` | heterogeneous result bundle | one universal verdict |

---

# Part Y — Tranche-1 workflow architecture side-lab using the same real case

The normal S001 application path currently does not use the shared static workflow parser after `direct_requirements_install_path=None` causes the CI evaluator to abstain early. We should still use the exact S001 workflow as a separate architecture lab because it demonstrates why the new IR exists.

## 24. Exact real source

At S001 head:

```text
pydantic/pydantic
.github/workflows/ci.yml
aa2dc024d33f61cdef50bf1973ab5adf0a974f5a
```

It is a large multi-job workflow containing matrix jobs, `needs`, `uses` steps, `run` steps, dynamic expressions, and the `docs-build` job.

## 25. Provider interpretation

```python
parse_workflow_definition(repository_text_file)
```

should conceptually preserve:

```text
WorkflowDefinition
  jobs[0..N]
    source order
    job key
    runs-on structure
    needs
    strategy/matrix fragment
    steps in source order
    run/uses distinction
    dynamic-expression flags
```

It does not execute the workflow.

## 26. Consumer limitation

If `inspect_workflow_commands(...)` were asked to interpret the whole S001 `ci.yml`, its current one-job boundary would return unresolved because multiple jobs are present.

That is not parser failure.

```text
provider successfully read structure
+
consumer lacks a trustworthy job-selection/correlation rule
→ consumer unresolved
```

This is the exact mental model Tranche 1 was designed to enforce.

---

# Part Z — What historical S001 manual simulation knew that current automation does not

The manual product-simulation investigation established additional case-specific facts, including:

```text
Soup Sieve was documentation tooling
Pydantic docs-build used the docs dependency group
mkdocs build exercised the documentation pipeline
historical manual evidence supported a bounded merge-after-review recommendation
```

The current product path does **not** automatically reproduce every one of those manual joins.

In particular:

```text
uv.lock change
+
uv sync --group docs
```

is not currently translated by the generic direct-install primitive into a direct dependency installation proof.

Do not “fix” this mentally by pretending the code knows what the manual case knew.

### Engineering lesson

```text
real discovery case
→ exposes useful evidence relationship
→ product may later automate a bounded reusable subset
```

Product simulation is pressure/discovery evidence, not an executable oracle.

---

# 27. Seven S001 rules you MUST remember

1. **Freeze identity first.** Exact base/head SHAs are part of the evidence chain.
2. **Dependency identity is canonicalized once.** Downstream branches consume `DependencyVersionChange`.
3. **A lockfile transition does not automatically provide a direct CI installation path.**
4. **Runtime CI evidence and static workflow evidence are separate proof families.**
5. **CI unresolved does not block independent upstream/target investigation.**
6. **Upstream change is only a candidate until target relevance is investigated.**
7. **One mechanism becoming non-applicable does not equal a whole-PR safety or merge verdict.**

---

# 28. Common wrong explanations

### Wrong

> “CI passed, so Soup Sieve 2.8.4 was tested.”

Correct:

> Successful exact-head CI existed, but the current automated rule did not establish a bounded direct dependency-exercise path for this `uv.lock` transition.

### Wrong

> “Soup Sieve dropped Python 3.8, therefore Pydantic is affected.”

Correct:

> The support drop created an impact candidate. Exact-head Pydantic metadata declared `>=3.10`, so that particular support-drop mechanism was outside the target’s declared range.

### Wrong

> “The LLM discovered the truth.”

Correct:

> The LLM extracted candidates from a bounded authoritative source window; deterministic reconstruction/validation admitted the grounded claim.

### Wrong

> “The workflow parser failed because Pydantic has many jobs.”

Correct:

> The provider IR can preserve many jobs. The current CI consumer intentionally abstains because it lacks static↔runtime job correlation and safe job selection for this proposition.

---

# 29. Source-reading order

Study these files in this order:

```text
1. src/upgradepilot/cli.py
2. src/upgradepilot/investigation.py
3. src/upgradepilot/dependency/analysis.py
4. src/upgradepilot/dependency/uv_lock.py
5. src/upgradepilot/github/repository.py
6. src/upgradepilot/github/actions.py
7. src/upgradepilot/ci/dependency_exercise.py
8. src/upgradepilot/github/workflow_definition.py
9. src/upgradepilot/dependency/direct_install.py
10. src/upgradepilot/ci/workflow_commands.py
11. src/upgradepilot/pypi/release.py
12. src/upgradepilot/upstream/repository.py
13. src/upgradepilot/upstream/interval.py
14. src/upgradepilot/upstream/interval_evidence.py
15. src/upgradepilot/upstream/support_drop.py
16. src/upgradepilot/impact/python_support.py
17. src/upgradepilot/target/python.py
18. src/upgradepilot/target/relevance.py
```

Do not read all lines equally. Follow the functions named in this note.

---

# 30. Study checkpoints

Do not look at the answers until you can explain each from memory.

### Checkpoint A — identity

Why do we need both a PR locator and immutable base/head SHAs?

### Checkpoint B — dependency extraction

Why does S001 produce a trusted dependency transition but `direct_requirements_install_path=None`?

### Checkpoint C — proof classes

What does `WorkflowRun(conclusion="success")` prove that static YAML cannot? What does it still not prove?

### Checkpoint D — independence

Why can the upstream/target relevance path continue when CI dependency exercise is unresolved?

### Checkpoint E — candidate semantics

Why is “Python 3.8 support dropped” not itself a Pydantic impact conclusion?

### Checkpoint F — IR vs consumer

Why can `parse_workflow_definition(...)` successfully represent S001 `ci.yml` while `inspect_workflow_commands(...)` still abstains?

### Checkpoint G — LLM boundary

What does the model propose, and what does deterministic code retain authority over?

---

# 31. Mastery exercise for chat

When studying this with the assistant, trace **one concrete value at a time**.

Recommended sequence:

```text
"pydantic/pydantic", 13432
→ PullRequestIdentity.head_sha
→ ChangedFile("uv.lock")
→ RepositoryTextFile base/head uv.lock
→ DependencyVersionChange(soupsieve, 2.6, 2.8.4)
→ direct_requirements_install_path=None
→ exact-head WorkflowRun/WorkflowJob evidence
→ CI unresolved boundary
→ PackageReleaseEvidence(soupsieve 2.8.4)
→ UpstreamRepositoryEvidence(facelessuser/soupsieve)
→ crossed releases
→ tagged changelog authority
→ GroundedPythonSupportDropClaim(3.8, introduced 2.8)
→ unresolved impact candidate
→ target investigation selection
→ TargetPythonDeclaration(>=3.10)
→ outside_declared_python_range
→ reevaluated impact
```

For every arrow, ask four questions:

```text
1. Which function owns this transformation?
2. What exact input type/data enters?
3. What output type/data leaves?
4. What stronger claim is still NOT justified?
```

If you can answer those four questions across the chain, you understand S001 at the level this snapshot is designed to teach.

---

# 32. Final one-screen model

```text
CLI
 │
 ▼
investigate_public_pull_request
 │
 ├─ PR identity + changed files
 │       ↓
 │   exact base/head uv.lock
 │       ↓
 │   soupsieve 2.6 → 2.8.4
 │
 ├─ CI branch
 │   exact-head runtime runs/jobs
 │   + exact workflow files
 │   + no admitted direct requirements path
 │       ↓
 │   unresolved dependency exercise
 │
 └─ upstream/target branch
     PyPI 2.8.4
       ↓
     facelessuser/soupsieve
       ↓
     crossed releases 2.7 ... 2.8.4
       ↓
     exact tagged changelog
       ↓
     grounded Python-3.8 support-drop claim
       ↓
     impact candidate initially unresolved
       ↓
     exact Pydantic head pyproject.toml
       ↓
     requires-python >=3.10
       ↓
     support-drop mechanism outside declared target range

RETURN: heterogeneous PublicPullRequestInvestigation
NOT: universal safety/merge verdict
```

That is the S001 mental model to own before moving to S011.