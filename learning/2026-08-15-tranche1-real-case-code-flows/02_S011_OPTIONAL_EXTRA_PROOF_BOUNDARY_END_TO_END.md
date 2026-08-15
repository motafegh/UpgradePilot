# S011 Real-Case Code Flow — Dictare / MLX Optional Extra / NumPy 1.26.4 → 2.4.6

**Learning snapshot date:** 2026-08-15  
**UpgradePilot source/test snapshot:** `ef4283db0a7ce3eec75a56ccc5c07354015fd2e3`  
**Depth target:** implementation-adjacent understanding of the Tranche-1 workflow-evidence architecture, consumer abstention, and current application gap  
**Case:** `dragfly/dictare#34`  
**Frozen target base:** `9921be73b4a55ba54b7b1f46ba424ada0d38aaa7`  
**Frozen target head:** `62d65da86f902d4b54a9d87e9ced5ff2e1f61e55`  
**Changed dependency:** `[project.optional-dependencies].mlx` → `numpy==1.26.4` → `numpy==2.4.6`

This is a reusable educational snapshot. It does not select future implementation and does not claim that the current normal application path fully automates S011. The real simulation evidence is preserved under:

- [`../../product-simulation/scenarios/S011-dictare-mlx-optional-extra-ci-coverage/README.md`](../../product-simulation/scenarios/S011-dictare-mlx-optional-extra-ci-coverage/README.md)
- [`../../product-simulation/scenarios/S011-dictare-mlx-optional-extra-ci-coverage/artifacts/CASE_IDENTITY_AND_OPTIONAL_EXTRA.json`](../../product-simulation/scenarios/S011-dictare-mlx-optional-extra-ci-coverage/artifacts/CASE_IDENTITY_AND_OPTIONAL_EXTRA.json)
- [`../../product-simulation/scenarios/S011-dictare-mlx-optional-extra-ci-coverage/artifacts/OPTIONAL_ACTIVATION_PATH.json`](../../product-simulation/scenarios/S011-dictare-mlx-optional-extra-ci-coverage/artifacts/OPTIONAL_ACTIVATION_PATH.json)
- [`../../product-simulation/scenarios/S011-dictare-mlx-optional-extra-ci-coverage/artifacts/CI_COVERAGE_BOUNDARY.json`](../../product-simulation/scenarios/S011-dictare-mlx-optional-extra-ci-coverage/artifacts/CI_COVERAGE_BOUNDARY.json)

---

# 1. Why S011 is the second case

S001 teaches the normal currently wired application orchestration.

S011 teaches the opposite skill that an evidence-driven system needs just as much:

> **Knowing exactly where the source is readable but the current product cannot justify the stronger conclusion.**

The real simulation question was:

> Can a dependency update inside a real platform-specific optional extra be target-relevant while ordinary test workflows remain non-discriminating because they never install the affected extra?

The manual simulation established:

```text
real optional mlx dependency family
+
real Apple-Silicon MLX runtime activation path
+
normal Ubuntu workflow installs .[dev]
+
macOS workflow installs .[dev]
+
neither installs .[mlx]
    ↓
those inspected workflows do not establish compatibility of the changed NumPy pin
inside the MLX optional environment
```

The learning challenge is to map that real-world truth onto **what the current accepted UpgradePilot source can and cannot automate**.

---

# 2. The single most important distinction

There are three layers here:

```text
A. Real repository facts
B. Product-simulation manual interpretation
C. Current product automation
```

Do not collapse them.

For S011:

```text
A. Real files clearly contain an mlx optional extra and workflows.

B. Manual simulation established the optional activation and bounded CI non-coverage
   from multiple exact target/config/workflow files.

C. Current UpgradePilot does NOT yet parse pyproject optional-extra version changes
   as a canonical DependencyVersionChange, and its shared direct-install observer
   does NOT understand editable extras such as pip install -e .[mlx].
```

This is not a failure of the Tranche-1 workflow architecture. It is a boundary of the **current admitted dependency/consumer semantics**.

---

# Part A — Real case identity

## 3. Frozen proposal

```text
repository:       dragfly/dictare
PR:               34
base SHA:         9921be73b4a55ba54b7b1f46ba424ada0d38aaa7
head SHA:         62d65da86f902d4b54a9d87e9ced5ff2e1f61e55
source file:      pyproject.toml
optional group:   mlx
package:          numpy
old version:      1.26.4
proposed version: 2.4.6
```

At the frozen base, `pyproject.toml` has:

```toml
[project.optional-dependencies]
mlx = [
    ...
    "scipy==1.16.3",
    "numba==0.61.0",
    "numpy==1.26.4",
    "torch==2.0.1",
    ...
]
```

At the frozen head the relevant line is:

```toml
"numpy==2.4.6"
```

The file comments explicitly describe this as a coordinated Apple-Silicon stack whose versions are deliberately pinned together.

---

# Part B — Real activation chain before we touch UpgradePilot code

## 4. Optional environment is not dead metadata

The simulation established the real activation shape:

```text
install optional mlx dependency family
    ↓
run on macOS arm64 / Apple Silicon
    ↓
mlx_whisper discoverable
    ↓
hardware acceleration enabled
    ↓
engine factory selects MLXWhisperEngine
    ↓
MLX runtime imports/uses mlx.core + mlx_whisper + numpy
```

The target repository also documents the installation command:

```text
uv sync --python 3.11 --extra mlx
```

So the changed NumPy pin belongs to a real conditional runtime environment.

### MUST MASTER

```text
optional
!=
irrelevant
```

Optional means activation is conditional. It does not mean the path is fake or unimportant.

---

# Part C — Real workflow definitions

## 5. Normal workflow: `.github/workflows/ci.yml`

At the frozen target revision the workflow has **two jobs**:

```text
test
typecheck
```

Both use:

```yaml
runs-on: ubuntu-latest
```

Both configure Python 3.11 using:

```yaml
uses: actions/setup-python@v5
with:
  python-version: "3.11"
```

The test job installs:

```yaml
- name: Install deps
  run: pip install -e ".[dev]"
```

and runs:

```yaml
xvfb-run pytest tests/ -v -m '' --cov=dictare ...
```

The typecheck job also installs only:

```text
pip install -e ".[dev]"
```

There is no `.[mlx]` installation in these jobs.

---

## 6. Dedicated macOS workflow: `.github/workflows/ci-macos.yml`

This workflow has one job:

```text
test-macos
```

with:

```yaml
runs-on: macos-latest
```

The setup/install block is:

```yaml
- name: Set up Python and install deps
  run: |
    uv venv --python 3.11 --seed .venv
    echo "VIRTUAL_ENV=$PWD/.venv" >> $GITHUB_ENV
    echo "$PWD/.venv/bin" >> $GITHUB_PATH
    .venv/bin/pip install -e ".[dev]"
```

Then:

```yaml
- name: Run CoreAudio tests
  run: pytest tests/ -v -m macos
```

Again, the inspected workflow does not install `.[mlx]`.

### Critical mental model

```text
macOS runner
!=
MLX environment
```

And even:

```text
Apple-Silicon-compatible platform
!=
mlx optional family installed
!=
MLX engine selected
!=
NumPy path exercised
```

There is an activation chain, not one magic platform label.

---

# Part D — What the simulation could establish manually

## 7. Manual evidence result

From the exact `pyproject.toml`, target activation files, README, and two relevant workflow definitions, the simulation established:

```text
workflow context exists
+
macOS workflow exists
+
normal test jobs exist
!=
affected optional mlx environment formed
```

This is a **static evidence conclusion about the inspected definitions**.

It is not based on guessing from a green check.

It also does not claim every workflow in the repository omits `mlx`; the scenario deliberately bounded its coverage question to the two relevant test workflows.

---

# Part E — Now trace the current normal application

## 8. What happens if S011 enters `investigate_public_pull_request(...)`?

Current source snapshot:

```text
src/upgradepilot/investigation.py
src/upgradepilot/dependency/analysis.py
src/upgradepilot/dependency/change.py
```

The application begins normally:

```text
repository + PR number
→ PullRequestIdentity
→ complete ChangedFile records
→ analyze_dependency_change(...)
```

But current dependency analysis only admits:

```text
exact requirement files
uv.lock
```

It does not yet parse `[project.optional-dependencies]` changes from `pyproject.toml`.

Therefore the S011 `pyproject.toml` change does not produce an extracted dependency transition.

`compare_extracted_dependency_changes(...)` receives no admitted extraction and returns:

```text
DependencyChangeProblem
reason = no_supported_dependency_file
```

### Consequence in `investigation.py`

The main downstream block is guarded by:

```python
if isinstance(dependency_result, DependencyVersionChange):
    ...
```

S011 does not cross that gate under the accepted snapshot source.

So the normal application returns without activating:

```text
exact-head workflow acquisition
CI dependency exercise
PyPI release branch
upstream semantic branch
target Python branch
```

### This behavior is source-derived, not a recorded live S011 run

We have not claimed that the current accepted revision was live-executed against S011. This is the deterministic control-flow consequence of the frozen S011 changed-file shape and the accepted dependency-analysis code.

### MUST MASTER

```text
current product cannot automate this case end-to-end
!=
the case is invalid
!=
the workflow parser cannot read the workflows
```

The application stops because the **dependency-source admission boundary** has not yet learned this pyproject optional-extra change.

---

# Part F — Why Tranche 1 still matters enormously for S011

The new Tranche-1 architecture lets us take the **workflow evidence responsibility itself** and study it independently of the application’s current dependency-source gap.

This is not bypassing product truth. It is inspecting the real reusable responsibility that now exists:

```text
RepositoryTextFile
→ parse_workflow_definition(...)
→ typed static provider IR
→ Target or CI consumer interpretation
```

That is the correct end-to-end boundary for this S011 learning lab.

---

# Part G — Provider acquisition

## 9. `GitHubRepositoryClient` → `RepositoryTextFile`

File:

```text
src/upgradepilot/github/repository.py
```

For learning, imagine the frozen exact workflow content has been acquired as:

```python
RepositoryTextFile(
    repository="dragfly/dictare",
    path=".github/workflows/ci.yml",
    returned_path=".github/workflows/ci.yml",
    revision="9921be73...",
    blob_sha=...,
    reported_byte_count=...,
    decoded_byte_count=...,
    content=...,
    retrieved_at=...,
)
```

The provider’s responsibility is:

```text
exact file identity
exact revision
bounded text acquisition
returned-path agreement
blob/byte/encoding/UTF-8 provenance
```

It does not know what “MLX coverage” means.

---

# Part H — Shared GitHub Actions IR

## 10. `parse_workflow_definition(...)`

File:

```text
src/upgradepilot/github/workflow_definition.py
```

The parser boundary is:

```text
workflow text
→ PyYAML BaseLoader representation nodes
→ bounded node graph validation
→ provider-owned typed IR
```

The IR is not a generic YAML AST. It preserves the GitHub Actions structure needed by our consumers.

### `ci.yml` expected structural representation

The provider can represent:

```text
WorkflowDefinition
├── job 0: StepsJobDefinition(key="test")
│   ├── runs_on = StaticScalarValue("ubuntu-latest")
│   └── ordered steps
│       ├── UsesStepDefinition(actions/checkout@v6)
│       ├── UsesStepDefinition(actions/setup-python@v5)
│       ├── RunStepDefinition(sudo apt-get ...)
│       ├── RunStepDefinition(pip install -e ".[dev]")
│       ├── RunStepDefinition(ruff ...)
│       ├── RunStepDefinition(bandit ...)
│       └── RunStepDefinition(xvfb-run pytest ...)
│
└── job 1: StepsJobDefinition(key="typecheck")
    ├── runs_on = StaticScalarValue("ubuntu-latest")
    └── ordered uses/run steps
```

The provider successfully seeing both jobs is a **success**, not an ambiguity error.

### `ci-macos.yml` expected structure

```text
WorkflowDefinition
└── job 0: StepsJobDefinition(key="test-macos")
    ├── runs_on = StaticScalarValue("macos-latest")
    └── steps
        ├── UsesStepDefinition(actions/checkout@v6)
        ├── UsesStepDefinition(astral-sh/setup-uv@v4)
        ├── RunStepDefinition(multiline venv + pip install .[dev])
        └── RunStepDefinition(pytest ... -m macos)
```

### MUST MASTER

```text
provider IR answers: "what structure is declared?"
consumer answers:    "what does that structure establish for my proposition?"
```

Those are different responsibilities.

---

# Part I — Target consumer on the normal `ci.yml`

## 11. `interpret_target_artifact_environment(...)`

File:

```text
src/upgradepilot/target/artifact_environment.py
```

This consumer starts by calling:

```python
parse_workflow_definition(evidence)
```

Then it calls its own bounded selector:

```python
_select_target_job(...)
```

Current rule:

```text
exactly one job required
```

But S011 `ci.yml` contains:

```text
test
typecheck
```

Therefore the Target consumer returns:

```text
TargetArtifactEnvironmentProblem
state = ambiguous_target_job_selection
```

### Important

The correct explanation is **not**:

> “The workflow is unreadable.”

The correct explanation is:

> “The provider read the workflow structure, but this Target proposition currently lacks a safe job-selection rule.”

This is the core provider-vs-consumer distinction.

---

# Part J — Target consumer on `ci-macos.yml`

## 12. One-job case reaches deeper

`ci-macos.yml` contains one local steps job, so `_select_target_job(...)` can safely return:

```text
StepsJobDefinition(key="test-macos")
```

Now the Target consumer evaluates its own bounded facts.

### Runner

`runs-on` is one literal scalar:

```text
macos-latest
```

So `_interpret_runner(...)` can produce:

```python
TargetArtifactEnvironmentFact(
    value="macos-latest",
    source="runs-on declaration at line ...",
)
```

What does this prove?

```text
static workflow declares macos-latest
```

What does it not prove?

```text
specific hardware architecture
actual runtime host properties
MLX installed
MLX engine selected
```

---

## 13. Python version interpretation

The current Target interpreter specifically understands a literal:

```text
actions/setup-python@...
with:
  python-version: ...
```

But `ci-macos.yml` uses:

```text
astral-sh/setup-uv@v4
```

and then declares inside shell text:

```text
uv venv --python 3.11 --seed .venv
```

The current Target interpreter does **not** parse that shell command as setup-python evidence.

Therefore:

```text
python_version = None
limitation includes setup_python_version_not_observed
```

Again:

```text
fact present in human-readable shell text
!=
current bounded consumer has admitted that evidence form
```

This is intentional evidence discipline.

---

# Part K — Shared direct-install observer on S011

## 14. `observe_direct_installation_declaration(...)`

File:

```text
src/upgradepilot/dependency/direct_install.py
```

This shared primitive currently recognizes direct **requirements-file** forms such as:

```text
pip install -r requirements.txt
python -m pip install --requirement requirements-dev.txt
```

It does not implement generic packaging semantics for:

```text
pip install -e .[dev]
pip install -e .[mlx]
uv sync --extra mlx
pyproject optional-group resolution
```

### Apply it to the real S011 macOS install block

The run text includes:

```text
.venv/bin/pip install -e ".[dev]"
```

That is outside the currently admitted direct-requirements-file rule.

So, even if the consumer is passed `dependency_source_file="pyproject.toml"`, the shared observer cannot say:

```text
"I understand that .[dev] resolves this pyproject dependency source but excludes mlx."
```

It simply does not observe an admitted matching direct requirements-file declaration.

The Target consumer therefore reaches:

```text
dependency_installation_declaration = not_observed
installation_declaration_source = None
limitations += changed_dependency_installation_declaration_not_observed
```

### This is weaker than the manual S011 conclusion

Manual simulation established:

```text
.[dev] does not install .[mlx]
```

Current automated direct-install primitive establishes only:

```text
no admitted direct requirements-file declaration for the supplied source was observed
```

Do not upgrade the automated result to the manual semantic claim.

### MUST MASTER

```text
not_observed
!=
proved absent
```

Especially when the consumer’s admitted grammar is intentionally narrow.

---

# Part L — Exact wheel compatibility stays unresolved

## 15. Target result proof strength

`TargetArtifactEnvironmentEvidence` contains:

```text
exact_wheel_compatibility_state = unresolved
```

This is correct even when we know:

```text
runner = macos-latest
```

because broad runner labels do not establish exact Python ABI/platform wheel tags.

The chain would require independently established exact target tags before artifact compatibility can be proven.

So:

```text
macos-latest
!=
exact wheel compatibility environment
```

---

# Part M — CI static consumer on S011 `ci.yml`

## 16. `inspect_workflow_commands(...)`

File:

```text
src/upgradepilot/ci/workflow_commands.py
```

This consumer also calls:

```python
parse_workflow_definition(...)
```

Current CI selection rule requires one static local job because Tranche 1 deliberately did not implement static↔runtime job correlation.

S011 normal `ci.yml` has two jobs.

So CI static interpretation returns:

```text
WorkflowCommandEvidence
status = unresolved
reason = multiple_or_zero_workflow_jobs
job_count = 2
```

Again:

```text
provider structural success
+
consumer selection limitation
→ unresolved
```

not parser failure.

---

# Part N — CI static consumer on S011 `ci-macos.yml`

## 17. One job, but still no admitted dependency path

The static CI consumer can select `test-macos` because there is only one job.

Then it searches each `RunStepDefinition` for two things:

```text
A. admitted direct installation from supplied dependency-source path
B. later direct invocation of changed package
```

For a hypothetical S011 call with:

```text
source_file = pyproject.toml
package = numpy
```

current rules find neither:

- `.venv/bin/pip install -e ".[dev]"` is not an admitted `pip install -r ...` dependency-source declaration;
- `pytest ...` is not a direct invocation of the `numpy` package.

So the bounded result is:

```text
status = unresolved
reason = static_dependency_path_incomplete
```

This does not mean the workflow cannot transitively import NumPy. It means the current **direct invocation** rule does not establish that proposition.

---

# Part O — Why we do not force `evaluate_dependency_ci_exercise(...)` here

## 18. CI exercise evaluator needs a canonical dependency

`evaluate_dependency_ci_exercise(...)` expects:

```python
DependencyVersionChange
```

But the normal S011 application path did not establish one because pyproject optional-extra extraction is not currently admitted.

We should not construct a fake canonical dependency object just to make the pipeline look complete in a learning note.

That would teach the wrong engineering habit.

Correct learning boundary:

```text
normal app
→ stops at dependency-source admission

standalone workflow evidence lab
→ can still teach provider IR + consumer boundaries from exact real files
```

---

# Part P — S011 object/result ledger

| Layer | Current object/result | What it can establish for S011 | What remains outside it |
|---|---|---|---|
| PR/change discovery | `PullRequestIdentity`, `ChangedFile` | exact PR and changed `pyproject.toml` | canonical optional-extra dependency change |
| dependency analysis | `DependencyChangeProblem(no_supported_dependency_file)` | current source boundary is explicit | NumPy transition automation |
| exact workflow source | `RepositoryTextFile` | exact YAML provenance | workflow meaning |
| provider parser | `WorkflowDefinition` | jobs/steps/runners/uses/run structure | Target/CI conclusion |
| Target on `ci.yml` | `ambiguous_target_job_selection` | provider-readable but no safe job selector | exact Target environment |
| Target on macOS workflow | partial `TargetArtifactEnvironmentEvidence` | literal macOS runner; missing/limited facts | Apple-Silicon identity, MLX formation, wheel tags |
| direct-install observer | `not_observed` under current grammar | no admitted direct requirements-file match | semantic `. [dev]` vs `.[mlx]` comparison |
| CI static on `ci.yml` | `multiple_or_zero_workflow_jobs` | current CI cannot select/correlate one job | cross-job/runtime mapping |
| CI static on macOS | `static_dependency_path_incomplete` | no admitted direct install→numpy invocation path | transitive test imports/behavior |
| simulation evidence | manual bounded non-coverage | inspected workflows omit `mlx` extra | actual NumPy 2.4.6 behavioral compatibility |

---

# Part Q — The proof ladder shown by S011

S011 gives us an excellent concrete proof ladder:

```text
pyproject declares mlx optional group
    ↓
workflow declares macos-latest
    ↓
workflow declares install .[dev]
    ↓
workflow may run successfully
```

None of those, individually or automatically together, proves:

```text
mlx extra installed
Apple-Silicon arm64 runner
mlx_whisper discoverable
MLX engine selected
changed NumPy used
changed NumPy behavior compatible
```

Each stronger proposition needs evidence of its own.

### MUST MASTER

```text
configuration context
!=
environment formation
!=
activation
!=
exercise
!=
success of affected behavior
```

This is exactly why Cluster 4 replaced runtime-sounding Target environment-formation language with declaration-strength semantics.

---

# Part R — `observed`, `not_observed`, `unresolved`

## 19. Learn these as evidence states, not English synonyms

### `observed`

An admitted static form was actually found.

Example under current direct-install rule:

```text
pip install -r requirements.txt
```

### `not_observed`

Within the bounded admitted interpretation, a matching declaration was not found.

It does **not** automatically mean the relationship is absent in reality.

S011 is a perfect example because `. [dev]` / `.[mlx]` semantics are outside the direct-requirements observer.

### `unresolved`

Potentially relevant evidence exists but cannot be safely interpreted, or the consumer lacks a trustworthy selection rule.

Examples:

```text
multiple jobs for a one-job consumer
dynamic working-directory
reusable workflow outside current expansion boundary
```

---

# Part S — The provider/consumer architecture in one picture

## 20. S011 normal workflow

```text
real .github/workflows/ci.yml
        ↓
RepositoryTextFile
        ↓
parse_workflow_definition
        ↓
WorkflowDefinition
  ├─ test
  └─ typecheck
        ↓
   ┌──────────────┬───────────────┐
   ▼              ▼
Target consumer   CI consumer
needs 1 job       needs 1 job
   ↓              ↓
ambiguous         unresolved
selection         multiple jobs
```

The important success is that both consumers receive **the same provider-owned structure**.

Before Tranche 1, Target and CI had separate shallow YAML readers. Now structural understanding has one provider owner, while each consumer preserves its own proof limitations.

---

# Part T — S011 macOS workflow in one picture

## 21. Deeper one-job trace

```text
ci-macos.yml
    ↓
RepositoryTextFile
    ↓
parse_workflow_definition
    ↓
WorkflowDefinition
    ↓
StepsJobDefinition("test-macos")
    │
    ├─ runs-on = "macos-latest"
    │      ↓
    │   Target runner fact observed
    │
    ├─ setup uses setup-uv, not setup-python
    │      ↓
    │   Target Python fact not observed by current rule
    │
    ├─ run block contains .venv/bin/pip install -e ".[dev]"
    │      ↓
    │   direct requirements-file observer: not_observed
    │
    └─ pytest -m macos
           ↓
        not a direct numpy invocation

Result:
partial static evidence + explicit limitations
NOT "MLX environment formed"
```

---

# Part U — Why S011 matters to future architecture thinking

S011 reveals several **real gaps**, but this note does not select them for implementation.

The case pressures at least these distinct responsibilities:

```text
1. dependency-source extraction from pyproject optional groups
2. optional dependency-family identity / activation semantics
3. editable-extra install declaration interpretation
4. proposition-specific job selection/correlation
5. platform/hardware evidence beyond broad runner labels
6. runtime affected-path exercise evidence
```

They must not be collapsed into one “make CI smarter” feature.

Each is a different proposition/owner.

### Example of bad design

```text
build generic workflow/environment/dependency tracer
```

### Better design discipline

```text
select one decision-relevant missing proposition
→ identify exact evidence needed
→ add smallest bounded responsibility
→ preserve unresolved elsewhere
```

---

# Part V — What Tranche 1 solved vs what S011 still exposes

## 22. Solved by Tranche 1

```text
✓ one provider-owned GitHub Actions static structure
✓ proper YAML parsing boundary
✓ multiple jobs preserved structurally
✓ dynamic/literal values distinguished
✓ run/uses steps preserved
✓ Target and CI no longer duplicate YAML parsers
✓ direct requirements-file declaration observation shared
✓ static declaration no longer mislabeled runtime formation
✓ CI strongest proof narrowed to supported_not_correlated
✓ consumer limitation separated from parser failure
```

## 23. Not solved by Tranche 1

```text
✗ pyproject optional-extra dependency-change extraction
✗ semantic parsing of pip install -e .[extra]
✗ uv extra/group resolution as general install evidence
✗ arbitrary dependency consumption tracing
✗ multi-job static↔runtime correlation
✗ cross-job environment continuity
✗ exact Apple-Silicon runner identity
✗ MLX runtime activation proof
✗ NumPy 2.4.6 behavioral compatibility
```

This separation is intentional and healthy.

---

# Part W — Common wrong explanations

### Wrong

> “The macOS CI workflow means the MLX stack was tested.”

Correct:

> The workflow declares `macos-latest` and installs `.[dev]`. The real optional MLX environment requires additional installation/platform/runtime activation conditions that were not established by that workflow definition.

### Wrong

> “Target parser failed on `ci.yml`.”

Correct:

> The provider IR read the two-job workflow. The Target consumer abstained because its current proposition-specific selector requires one job.

### Wrong

> “`not_observed` means `mlx` definitely was not installed.”

Correct:

> In the current direct-install primitive, `not_observed` only means no admitted direct requirements-file declaration matched. The stronger `. [dev]` vs `.[mlx]` semantic conclusion came from manual simulation evidence, not this primitive.

### Wrong

> “S011 proves NumPy 2.4.6 breaks Dictare.”

Correct:

> S011 proves the changed NumPy pin belongs to a real optional environment and that the two inspected test workflow definitions do not establish coverage of that optional environment. Behavioral compatibility was not tested.

### Wrong

> “Since current app stops at `no_supported_dependency_file`, Tranche 1 is irrelevant to S011.”

Correct:

> The normal application dependency boundary stops early, but the newly built workflow-evidence architecture directly addresses the structural/claim problems S011 exposed and can be studied independently against the exact workflow files.

---

# Part X — Seven S011 rules you MUST remember

1. **Optional does not mean irrelevant.** Activation is conditional.
2. **A platform label is only one proposition in an environment-activation chain.**
3. **Provider structural readability and consumer interpretability are separate.**
4. **Multiple jobs are valid provider evidence; one-job consumers may still abstain.**
5. **`not_observed` is bounded to the observer’s admitted grammar.**
6. **Static workflow success/structure does not prove the affected optional environment formed or ran.**
7. **A product gap should remain explicit rather than being patched mentally with manual knowledge.**

---

# Part Y — Source-reading order

For this case, study:

```text
1. src/upgradepilot/dependency/analysis.py
2. src/upgradepilot/dependency/change.py
3. src/upgradepilot/github/repository.py
4. src/upgradepilot/github/workflow_definition.py
5. src/upgradepilot/dependency/direct_install.py
6. src/upgradepilot/target/artifact_environment.py
7. src/upgradepilot/ci/workflow_commands.py
8. src/upgradepilot/ci/dependency_exercise.py
9. src/upgradepilot/investigation.py
```

And compare them with the real frozen target sources:

```text
dragfly/dictare @ 9921be73...
pyproject.toml
.github/workflows/ci.yml
.github/workflows/ci-macos.yml
```

Plus the simulation activation artifacts linked at the top of this file.

---

# Part Z — Study checkpoints

## Checkpoint A — application boundary

Why does the current normal S011 application stop before acquiring CI workflow evidence?

Expected concept:

```text
pyproject optional-extra version changes are not yet admitted by dependency analysis
```

## Checkpoint B — provider success

What exact objects should `parse_workflow_definition(...)` produce conceptually for the two jobs in `ci.yml`?

## Checkpoint C — Target abstention

Why is `ambiguous_target_job_selection` a Target problem rather than a YAML parser problem?

## Checkpoint D — macOS semantics

What does literal `macos-latest` establish, and what hardware/environment propositions remain open?

## Checkpoint E — install semantics

Why can manual S011 evidence say “the workflow installs `.[dev]`, not `.[mlx]`” while the current `observe_direct_installation_declaration(...)` only returns a weaker `not_observed` relationship?

## Checkpoint F — CI invocation

Why does running pytest not equal a direct invocation of NumPy under the current CI command rule?

## Checkpoint G — proof ladder

Write the activation chain from optional-group declaration to affected behavior exercise, and mark where each current product responsibility stops.

---

# 24. Mastery exercise for chat

When we study this together, trace these exact values:

```text
"dragfly/dictare", 34
→ ChangedFile(pyproject.toml)
→ no_supported_dependency_file in current dependency analysis

SEPARATE WORKFLOW LAB:

ci.yml exact RepositoryTextFile
→ WorkflowDefinition(jobs = test, typecheck)
→ Target ambiguous_target_job_selection
→ CI multiple_or_zero_workflow_jobs

ci-macos.yml exact RepositoryTextFile
→ WorkflowDefinition(job = test-macos)
→ runner fact = macos-latest
→ setup-python fact not observed
→ direct requirements install not observed
→ exact wheel compatibility unresolved

MANUAL SIMULATION JOIN:

pyproject [mlx] includes numpy pin
+ README says uv sync --extra mlx
+ runtime activation requires Apple Silicon + MLX availability + engine selection
+ inspected workflows install only .[dev]
→ inspected test workflows do not establish affected MLX environment coverage
```

At each arrow ask:

```text
1. Which owner/function produced this?
2. Is this provider fact, consumer interpretation, or manual simulation evidence?
3. What exact proposition does it establish?
4. What tempting stronger statement must we refuse?
```

---

# 25. Final one-screen S011 model

```text
REAL PROPOSAL
pyproject.toml: mlx numpy 1.26.4 → 2.4.6
        │
        ├──────── CURRENT NORMAL APP ────────┐
        │                                    │
        │ analyze_dependency_change          │
        │ only admits requirements/uv.lock   │
        │        ↓                           │
        │ no_supported_dependency_file       │
        │        ↓                           │
        │ normal downstream app stops        │
        │                                    │
        └────────────────────────────────────┘

SEPARATE ACCEPTED TRANCHE-1 WORKFLOW RESPONSIBILITY

exact workflow file
        ↓
RepositoryTextFile
        ↓
parse_workflow_definition
        ↓
typed GitHub Actions IR
        │
        ├─ ci.yml: 2 valid jobs
        │      ├─ Target: ambiguous job selection
        │      └─ CI: multiple-job unresolved
        │
        └─ ci-macos.yml: 1 job
               ├─ runner = macos-latest observed
               ├─ Python setup not admitted by current Target rule
               ├─ .venv/bin/pip install -e .[dev]
               │      ↓
               │   no admitted direct -r dependency-source observation
               └─ pytest is not direct numpy invocation

MANUAL S011 DISCOVERY EVIDENCE

real mlx optional group
+ real Apple-Silicon activation path
+ inspected workflows install only .[dev]
        ↓
those workflows do not establish MLX optional-environment coverage

NOT ESTABLISHED:
NumPy 2.4.6 incompatibility
MLX runtime failure
whole-repository CI absence
safe/unsafe recommendation
```

If you can clearly explain why all three sections coexist without contradiction, you have understood the central Tranche-1 evidence architecture.