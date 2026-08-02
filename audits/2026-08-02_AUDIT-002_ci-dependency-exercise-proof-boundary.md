# AUDIT-002 — CI Dependency-Exercise Proof Boundary

**Audit date:** 2026-08-02  
**Audit type:** implementation correctness / evidence-authority / proportionality audit  
**Trigger:** learning review of the current `DependencyCIExerciseResult` `proven` state, specifically whether successful run/job status plus static workflow-command recognition is sufficient to support the practical interpretation that the changed dependency was successfully installed and exercised  
**Inspected repository baseline:** `c1acf07628f5f8b8ddee2e5dfae6431dbb37d862` (`Close Step 5B and activate Step 5C validation`)  
**Disposition at audit time:** preserve the current implementation; do not change the active route or CI contract during this audit; record concrete proof-boundary risks and a staged strengthening direction for later authorized work  

## 1. Audit question

UpgradePilot currently has a bounded CI dependency-exercise rule:

```text
trusted DependencyVersionChange
+ exact-head WorkflowRun / WorkflowJob evidence
+ exact-revision workflow definition
+ independently established direct requirements path
+ visible supported pip -r installation command
+ visible supported direct changed-package invocation
→ DependencyCIExerciseResult
```

The public states are:

```text
proven
no_successful_ci
unresolved
```

The practical question exposed during learning was:

> When UpgradePilot returns `proven`, what has actually been established by the current evidence chain, and under which workflow/shell conditions could static command presence plus successful job/run status overstate what happened at runtime?

The associated design question is:

> What is the smallest proportionate strengthening that would let UpgradePilot make a materially stronger runtime dependency-exercise claim without becoming a general GitHub Actions YAML interpreter, shell interpreter, or CI log-analysis engine?

This audit distinguishes two possible interpretations of the existing `proven` state:

```text
A. bounded-static interpretation
   "one successful exact-head job/run has a statically recognized direct
    install command and a statically recognized direct package invocation"

B. runtime-success interpretation
   "the qualifying installation actually succeeded and the changed package
    was actually exercised successfully in the relevant runtime environment"
```

The current implementation is deliberately designed around A. Several current detail strings and ordinary human readings of the word `proven`, however, can be understood as B. The findings below focus on that gap.

## 2. Scope

Inspected responsibilities:

```text
exact PR head identity
→ exact-head workflow-run acquisition
→ complete job acquisition for each run
→ optional runtime step-summary acquisition
→ exact workflow-definition acquisition
→ successful job/run classification
→ shallow static workflow-command reading
→ direct requirements installation recognition
→ direct package invocation recognition
→ per-workflow CI dependency-exercise state
→ existential aggregate state
→ CLI presentation
```

Primary source inspected:

```text
src/upgradepilot/github_actions.py
src/upgradepilot/workflow_commands.py
src/upgradepilot/ci_dependency_exercise.py
src/upgradepilot/cli.py
```

Primary tests inspected:

```text
tests/test_github_actions.py
tests/test_workflow_commands.py
tests/test_ci_dependency_exercise.py
tests/test_cli.py
```

Related controlling/stable records inspected:

```text
plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md
audits/README.md
```

### Explicitly outside scope

This audit does not decide or implement:

- a universal GitHub Actions parser;
- a general YAML parser replacement;
- a general POSIX/Bash/PowerShell interpreter;
- arbitrary script, tox, nox, Makefile, task-runner, reusable-workflow, or custom-action tracing;
- broad test-coverage inference;
- dependency compatibility or safety;
- merge/defer/recommendation logic;
- `uv.lock` CI-consumption semantics;
- constraints-file installation semantics;
- current Step 5 upstream-acquisition work;
- a new live project priority.

No source/test change is authorized merely because this audit identifies a risk.

## 3. Controlling and related project records

### `audits/README.md`

The audit area is explicitly non-controlling. An audit may identify defects, risks, simplification opportunities, accepted complexity, or future reassessment questions, but it does not silently alter an implementation contract, plan, ADR, or `MEMORY.md` continuation.

This record therefore preserves the concern for later use without preempting the active B2 Step 5 work.

### `plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`

The plan deliberately excludes broad CI interpretation and defines the first shared CI boundary narrowly.

It states that the existing direct-requirements rule may prove one successful exact-head path through:

```text
visible pip -r <exact path> installation
+
direct changed-package invocation
```

It also explicitly requires:

```text
constraints and uv.lock do not inherit requirements-file semantics
```

and treats broad CI interpretation as outside this plan.

This matters because the correct response to the findings below is **not** automatically to implement a complete CI interpreter. Any strengthening should preserve the original boundedness unless a later plan intentionally expands it.

## 4. Observed implementation

### 4.1 Exact-head execution acquisition

`src/upgradepilot/github_actions.py` acquires:

```text
WorkflowRun
WorkflowJob
WorkflowStep
```

A `WorkflowRun` preserves:

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

A `WorkflowJob` preserves:

```text
job_id
run_id
name
head_sha
status
conclusion
steps: tuple[WorkflowStep, ...] | None
```

A `WorkflowStep` preserves:

```text
number
name
status
conclusion
```

Run items are checked against the frozen PR `head_sha`, and job items are reconnected to both the parent `run_id` and the same frozen head SHA.

This is strong exact-head execution identity. The audit does not challenge that boundary.

### 4.2 Static workflow-command reader

`src/upgradepilot/workflow_commands.py` intentionally implements a shallow text reader rather than a complete YAML or shell parser.

Its supported flow is:

```text
find jobs:
→ identify direct child job keys by indentation
→ require exactly one statically identifiable job
→ extract visible run: commands
→ split visible command chains
→ find supported pip install -r <source file>
→ find supported direct package invocation
→ supported / unresolved
```

Supported package invocation prefixes include direct invocation and selected wrappers such as:

```text
python -m
python3 -m
uv run
poetry run
pipenv run
coverage run -m
```

The module explicitly refuses to infer tox, scripts, aliases, functions, custom actions, or reusable workflows.

This conservative abstention is valuable and should be preserved.

### 4.3 Shell segmentation

`_shell_segments(...)` splits visible command text at:

```text
&&
||
;
newline
```

It intentionally does not preserve or evaluate the semantic relationship represented by those operators.

For example:

```bash
pip install -r requirements-dev.txt || true
```

is split into approximately:

```text
pip install -r requirements-dev.txt
true
```

The installation matcher can then recognize the first segment as qualifying installation syntax while the fact that failure was masked by `|| true` has been discarded.

### 4.4 Dependency-exercise evaluator

`src/upgradepilot/ci_dependency_exercise.py` evaluates each workflow in this order:

```text
completed successful job exists?
  no → no_successful_ci
  yes ↓

workflow run completed-successful?
  no → unresolved
  yes ↓

workflow definition available?
  no → unresolved
  yes ↓

workflow definition revision == run head SHA?
  no → unresolved
  yes ↓

explicit direct requirements installation path available?
  no → unresolved
  yes ↓

workflow_commands reports supported?
  no → unresolved
  yes → proven
```

The evaluator checks job-level and run-level status/conclusion, but it does not use `WorkflowJob.steps` to establish whether the specific static install or exercise step ran and succeeded.

### 4.5 Aggregate rule

The outer evaluator uses an existential rule:

```text
at least one per-workflow result == proven
→ overall proven
```

All per-workflow results remain preserved.

This audit does not challenge that existential aggregation. If the product question remains “does at least one admitted path prove dependency exercise?”, one valid witness is logically sufficient.

The concern is whether an individual workflow currently earns the strength attributed to `proven`.

### 4.6 Current controlled tests

`tests/test_workflow_commands.py` currently protects two simple supported forms:

```text
separate named run steps
one run: | block with installation + invocation
```

`tests/test_ci_dependency_exercise.py` protects:

- successful direct-requirements + direct invocation → `proven`;
- no workflow inputs;
- no completed successful job;
- precedence of no-successful-job over unavailable definition;
- successful job + unavailable definition;
- successful job + non-successful run;
- tox indirection → unresolved;
- multiple jobs → unresolved;
- missing explicit requirements path;
- generic evidence paths not becoming installation proof;
- existential overall proof while retaining weaker workflow results.

No current controlled test found during this audit covers:

```text
continue-on-error
|| true
conditional/skipped install or exercise step
install-after-exercise ordering
matched step runtime failure with successful overall job
runtime proposed-version observation
```

## 5. Baseline conclusion

The current implementation is **not broadly overengineered** and its conservative shape is valuable.

Strong parts that should be preserved include:

```text
exact-head run identity
exact run/job relationship checks
exact workflow-definition revision
explicit direct requirements path
no promotion of generic dependency source paths into CI proof
one-job static boundary
abstention for tox/indirection
transparent per-workflow results
existential aggregate with preserved evidence
```

The audit concern is narrower:

> Whole-job/run success plus static recognition of command text does not always establish that the matched installation succeeded, that the matched exercise actually ran successfully, that installation occurred before exercise, or that the exercised runtime contained the proposed dependency version.

Therefore the current implementation is a credible **bounded static-path recognizer**, but it should not be silently interpreted as full runtime command-success proof.

## 6. Findings

### AUDIT-002-F1 — `proven` currently combines runtime job success with static command presence, not matched-command runtime success

**Classification:** proof-soundness risk / contract-clarity issue  
**Current severity:** medium  
**Recommended disposition:** preserve current behavior for now; before expanding reliance on `proven`, either narrow the public meaning explicitly or strengthen the admitted evidence rule.

Current successful evidence is effectively:

```text
job completed-successful
+ workflow run completed-successful
+ exact workflow text contains qualifying install syntax
+ exact workflow text contains qualifying exercise syntax
→ proven
```

What is not currently established independently is:

```text
this exact install command completed successfully
this exact exercise command completed successfully
```

The difference matters when workflow semantics allow a command to fail or be skipped without making the whole job/run fail.

The implementation remains consistent with the plan's narrow “visible direct rule” wording. The risk appears when `proven` or its detail is interpreted as direct runtime-success evidence.

### AUDIT-002-F2 — `|| true` can mask installation failure while the static reader still recognizes installation evidence

**Classification:** concrete false-positive path under the runtime-success interpretation  
**Current severity:** medium-high for proof strength; no observed public incident recorded  
**Recommended disposition:** treat as a priority hardening case when CI proof is next revised.

Example:

```yaml
jobs:
  test:
    steps:
      - run: pip install -r requirements-dev.txt || true
      - run: pytest tests
```

Possible runtime behavior:

```text
pip install fails
→ || true masks failure
→ workflow continues
→ pytest succeeds from an already-available environment
→ job/run can be successful
```

Current static behavior:

```text
_shell_segments(...)
→ "pip install -r requirements-dev.txt"
→ "true"

install matcher sees first segment
→ qualifying installation command found
```

If the package invocation is also found and the run/job are successful, the current evaluator can reach `proven` even though successful installation was not established.

This is not a reason to implement a full shell parser. It is evidence that the accepted safe grammar must either preserve relevant operator semantics or abstain when matched commands participate in unsupported control flow.

### AUDIT-002-F3 — step-level `continue-on-error` and conditional execution are not interpreted by the static reader

**Classification:** proof-soundness risk  
**Current severity:** medium  
**Recommended disposition:** when hardening, preserve step modifiers in the static representation or conservatively return unresolved when a matched step has unsupported execution modifiers.

Example:

```yaml
- name: Install dependencies
  continue-on-error: true
  run: pip install -r requirements-dev.txt

- name: Test
  run: pytest tests
```

A successful job does not by itself prove the installation succeeded because failure may have been permitted.

Likewise:

```yaml
- name: Install dependencies
  if: some-condition
  run: pip install -r requirements-dev.txt
```

may be skipped depending on runtime context.

The current reader extracts `run:` values but does not model `continue-on-error`, `if`, or the runtime step outcome corresponding to that static step.

`github_actions.py` already preserves runtime step summaries when GitHub supplies them, including step status and conclusion, but `ci_dependency_exercise.py` currently does not consume them for command proof.

### AUDIT-002-F4 — the current reader does not prove install-before-exercise ordering

**Classification:** correctness defect relative to a causal “consume then exercise” interpretation  
**Current severity:** medium-high  
**Recommended disposition:** require a proven ordering relationship in any strengthened rule; add a regression test before changing public proof semantics.

Current installation and invocation discovery are independent searches over the command collection:

```text
first matching install command
first matching exercise command
```

No comparison of their positions is performed.

Therefore a workflow shaped as:

```yaml
jobs:
  test:
    steps:
      - run: pytest tests
      - run: pip install -r requirements-dev.txt
```

contains both recognized facts and can satisfy the static reader even though the qualifying installation occurs after the package invocation.

For a claim that CI “consumed the changed dependency and exercised the changed package,” order is material:

```text
qualifying installation
must precede
qualifying exercise
```

unless another separately admitted rule establishes that the exercised environment already contained the exact changed version.

### AUDIT-002-F5 — runtime `WorkflowStep` evidence is already acquired but is not joined to the matched static commands

**Classification:** evidence-utilization opportunity  
**Current severity:** medium as a missed strengthening opportunity, not a standalone defect  
**Recommended disposition:** investigate bounded static-to-runtime step correlation before considering log parsing or a broad interpreter.

`WorkflowJob.steps` can preserve:

```text
step number
step name
status
conclusion
```

This is richer runtime evidence than whole-job status alone.

A future strengthened rule could aim for:

```text
static install step
↔ exact runtime step summary
→ completed-successful

static exercise step
↔ exact runtime step summary
→ completed-successful
```

However, the join must itself be trustworthy.

Potential complications include:

- GitHub-generated setup/cleanup steps;
- duplicate or omitted step names;
- reusable/custom actions;
- step-number differences between static YAML and runtime representation;
- missing `steps` evidence (`None`);
- dynamically generated behavior.

Therefore the audit does **not** prescribe a naive name-only or ordinal-only join. A later implementation plan should define the smallest unambiguous correlation rule and return `unresolved` when that rule cannot establish identity.

### AUDIT-002-F6 — successful requirements consumption does not independently prove the exact proposed version was the version exercised

**Classification:** claim-strength limitation / future evidence tier  
**Current severity:** medium if `proven` is interpreted as exact-version runtime proof; low under the narrower static-path interpretation  
**Recommended disposition:** keep exact-version runtime observation separate from basic direct-path proof; add it only when evidence is actually available.

Suppose the canonical dependency change is:

```text
pytest 9.0.2 → 9.0.3
```

and the workflow contains:

```text
pip install -r requirements-dev.txt
pytest tests
```

Even after proving both steps executed successfully, a stronger statement such as:

```text
the exercised runtime definitely contained pytest==9.0.3
```

requires additional assumptions or runtime evidence.

Potential complications include:

- environment markers;
- constraints or resolver behavior;
- another installation later in the job;
- uninstall/downgrade/reinstall between the recognized installation and exercise;
- multiple Python environments or interpreter/path changes;
- a package invocation resolved from a different environment than the recognized `pip` command.

A strong exact-version fact is better represented when the runtime itself exposes a version witness, for example an admitted exact package-version output. Arbitrary external repositories will not always provide such evidence, so absence of a version witness must not be silently converted into one.

### AUDIT-002-F7 — same-job membership does not by itself establish environment/interpreter continuity

**Classification:** bounded-model limitation  
**Current severity:** low-medium  
**Recommended disposition:** do not attempt general environment simulation; define only the minimum continuity assumptions admitted by a future stronger rule and abstain outside them.

The current one-job restriction is valuable because installation in job A and invocation in job B clearly do not establish one shared environment.

But one job can still contain environment transitions such as:

```text
virtual-environment activation/deactivation
PATH changes
shell changes
container/tool wrappers
multiple Python interpreters
working-directory-dependent behavior
```

A future rule should not claim complete environment equivalence merely from “same job.”

The proportionate strategy is to define a small supported runtime shape, not to simulate every possible environment mutation.

### AUDIT-002-F8 — job logs can strengthen evidence but are not the best first authority mechanism

**Classification:** future-reassessment item / accepted deferred complexity  
**Current severity:** none  
**Recommended disposition:** prefer structured step evidence and a stricter static grammar first; use logs later as bounded corroboration or for explicitly selected proof cases.

Runtime logs may expose:

- that a command was actually emitted/executed;
- package installation output;
- package version output;
- test invocation output.

But logs introduce their own evidence problems:

- size and acquisition cost;
- retention/availability differences;
- formatting differences by shell/tool/version;
- masked secrets;
- commands that do not echo cleanly;
- output that can be produced by scripts rather than the expected command;
- parsing ambiguity;
- need for exact run/job/attempt correlation.

Making logs the first or only authority would trade one bounded static problem for a broad text-interpretation problem.

### AUDIT-002-F9 — preserving separate proof facts would reduce future overclaim risk

**Classification:** design improvement opportunity  
**Current severity:** low now; increasingly valuable if CI proof grows  
**Recommended disposition:** if the CI evidence model is revised, consider preserving distinct facts rather than adding more hidden meaning to one Boolean-like `proven` state.

A future internal evidence record could preserve facts such as:

```text
successful_exact_head_run
successful_exact_head_job
static_install_command_identified
static_exercise_command_identified
install_precedes_exercise
install_runtime_step_success
exercise_runtime_step_success
proposed_version_observed
```

The product state can then decide which combination is sufficient for a specific claim.

This makes it possible to distinguish, for example:

```text
static direct path established
runtime install/exercise established
exact proposed version observed and exercised
```

without pretending they are identical levels of proof.

This audit does not prescribe public state names or require the current three-state vocabulary to change.

## 7. Strengthening options and tradeoffs

The following are candidate levels, not authorized implementation steps.

### Option A — clarify only the current contract

Keep the current implementation but make its claim explicitly static/bounded.

Example meaning:

```text
proven
= a successful exact-head run/job contains a recognized direct installation path
  and recognized direct package invocation under the current static grammar
```

Advantages:

- no new acquisition or parser complexity;
- preserves existing validated behavior;
- accurately reflects the evidence currently used.

Disadvantage:

- does not solve runtime-success uncertainty;
- callers must not treat the result as per-command runtime proof.

This is the minimum safe response if stronger proof is not yet needed.

### Option B — define a stricter safe static grammar

Instead of attempting to understand arbitrary workflow/shell semantics, explicitly define the shapes allowed to contribute to strong proof.

Potential rules to evaluate:

```text
one statically readable job
one identifiable install step
one identifiable exercise step
install step precedes exercise step
no unsupported failure masking around matched commands
no unsupported conditional execution on matched steps
no continue-on-error on matched steps
no unsupported script/reusable/custom-action indirection
```

The important design principle is:

> Prefer a small whitelist of semantics that UpgradePilot can justify over an ever-growing blacklist of dangerous shell syntax.

Advantages:

- small incremental change;
- catches the concrete `|| true`, ordering, and step-modifier problems;
- remains consistent with current conservative abstention philosophy.

Disadvantages:

- still static;
- may classify more real workflows as unresolved;
- safe grammar must be carefully specified and tested.

### Option C — correlate static matched steps with structured runtime step outcomes

After static identification, require the matching runtime steps to be observed as completed-successful.

Conceptually:

```text
exact static install step
+ unambiguous runtime-step identity
+ completed-successful runtime outcome

exact static exercise step
+ unambiguous runtime-step identity
+ completed-successful runtime outcome

+ correct ordering
→ stronger runtime exercise evidence
```

Advantages:

- uses structured evidence UpgradePilot already acquires;
- materially closes the gap between whole-job success and matched-step success;
- can detect skipped/failed matched steps even when the job remains successful.

Disadvantages:

- requires a defensible static-to-runtime step identity rule;
- runtime step summaries may be absent;
- complex/reusable/generated steps remain outside the bounded rule.

This is the strongest candidate for the **next material CI-proof improvement** after a safe static grammar is defined.

### Option D — add an optional exact-version runtime witness

When the workflow already exposes trustworthy version output, preserve it separately.

Possible future admitted evidence could include carefully bounded forms such as:

```text
python -c using importlib.metadata.version(...)
python -m pip show <exact package>
other explicitly admitted generic version command
```

The output would still need exact runtime/log grounding and package/version parsing.

Advantages:

- supports the stronger claim that the proposed dependency version was actually present;
- makes “changed version exercised” more precise.

Disadvantages:

- many external repositories do not emit such a witness;
- log/output parsing is required;
- package-specific `--version` behavior is not uniform;
- should not become a requirement that forces arbitrary repository mutation.

This should therefore be a stronger optional evidence tier, not silently inferred from ordinary install syntax.

### Option E — bounded job-log corroboration

Acquire exact job logs only when a specific later proof rule justifies them.

Use logs to corroborate or establish facts that structured evidence cannot provide, not as a generic semantic search surface.

Advantages:

- closer to actual runtime behavior;
- may expose version and command output.

Disadvantages:

- expensive and variable;
- broad parsing can become fragile quickly;
- retention and availability must be handled explicitly.

Logs should be considered after Options B/C, not before them.

## 8. Recommended staged direction

This audit recommends a **future staged strengthening**, subject to normal planning/authorization.

### Stage 1 — freeze the intended claim

Before changing code, decide which statement the product actually needs:

```text
Claim A:
"a direct install/exercise path is statically present in successful exact-head CI"

Claim B:
"the matched install and exercise steps actually completed successfully"

Claim C:
"the exact proposed dependency version was present and successfully exercised"
```

Do not let one state name silently move from A to B to C without changing its evidence obligations.

### Stage 2 — harden the current static rule

At minimum, the future proof rule should address:

```text
failure masking
conditional/skipped matched steps
install-before-exercise ordering
```

Prefer conservative unresolved results over broad semantic guessing.

### Stage 3 — use structured runtime steps

Investigate an unambiguous join between static matched steps and `WorkflowStep` runtime evidence.

If the join is ambiguous or the runtime steps are unavailable:

```text
strong runtime proof → unresolved
```

The system may still preserve weaker static evidence separately if the product model supports levels.

### Stage 4 — preserve exact-version runtime evidence when available

Do not invent version observation.

If an exact runtime version witness exists and is admitted, preserve it as a stronger fact. Otherwise retain the narrower consumption/exercise result.

### Stage 5 — add logs only for bounded unresolved gaps

Use exact job logs when a concrete selected proof case requires information unavailable from structured run/job/step evidence.

Avoid creating an unbounded log-search subsystem merely because logs exist.

## 9. Reassessment triggers

Reopen this audit when any of the following becomes true:

1. `DependencyCIExerciseResult.proven` begins influencing compatibility, safety, merge/defer, targeted-check, or maintainer-action logic.
2. A real supported/public workflow contains `continue-on-error`, `|| true`, conditional matched steps, or another failure-masking construct.
3. A real workflow has the recognized exercise before the recognized installation.
4. A real workflow shows job success while a relevant runtime step is failed/skipped.
5. Step-level runtime evidence becomes necessary for a B2/B3 proof obligation.
6. CI results are persisted/replayed and need durable explanation of proof strength.
7. A later plan requires proof that the **exact proposed version**, rather than only the changed dependency source, was exercised.
8. The current static rule produces a known false positive or a public validation case exposes claim ambiguity.
9. Work begins on broader CI coverage/platform semantics.
10. A future architecture change introduces a general evidence-confidence or proof-tier model.

## 10. Proof required if the CI rule is strengthened

A later implementation should preserve existing exact-head and source-authority behavior while adding controlled proof for the new semantics.

Minimum regression/proof cases should include:

### Existing behavior that must remain protected

1. no exact-head workflow inputs → `no_successful_ci`;
2. no completed successful job → `no_successful_ci`;
3. successful job + non-successful run → unresolved;
4. unavailable/mismatched workflow definition → unresolved;
5. no explicit direct requirements path → unresolved;
6. tox/unsupported indirection → unresolved;
7. multiple jobs under the current one-job rule → unresolved;
8. constraints and `uv.lock` do not inherit direct requirements semantics;
9. all per-workflow evidence remains preserved;
10. existential aggregation still requires at least one genuinely admitted proof path.

### New proof-soundness cases

11. `pip install -r requirements-dev.txt || true` cannot establish strong install success;
12. matched install step with `continue-on-error: true` cannot establish strong install success merely from green job status;
13. conditionally skipped install step cannot establish strong install success;
14. conditionally skipped exercise step cannot establish strong exercise success;
15. exercise before installation cannot establish consume-then-exercise proof;
16. failed matched install runtime step + successful job cannot establish strong proof;
17. successful install runtime step + failed/skipped exercise step cannot establish strong proof;
18. both unambiguously matched runtime steps completed-successfully can establish the selected stronger proof level;
19. missing/ambiguous runtime step identity remains unresolved rather than guessed;
20. later dependency mutation between install and exercise is either ruled out by the admitted grammar, explicitly modeled, or causes abstention;
21. an observed runtime version mismatch with `DependencyVersionChange.proposed_version` cannot produce exact-version proof;
22. absence of runtime version observation is not represented as an observed proposed version;
23. exact-head/run/job/attempt identity remains intact when adding any log or step evidence;
24. S004 is re-evaluated through the stronger rule rather than preserved by case-specific exception;
25. the complete deterministic suite remains green.

## 11. What should not be built merely to close this audit

Do not automatically create:

```text
complete GitHub Actions YAML AST + evaluator
complete shell parser/interpreter
full tox/nox/Make/script tracing
arbitrary log semantic extraction
repository-specific CI plugins
hardcoded S004 proof exceptions
```

A stronger proof rule is valuable only if its additional certainty is proportional to its complexity.

The safe fallback remains:

```text
unsupported or ambiguous semantics
→ unresolved
```

## 12. Disposition

Current disposition:

```text
KEEP current bounded implementation
+
DO NOT reinterpret it as universal runtime command proof
+
REASSESS before CI `proven` is used as a stronger decision signal
+
PREFER staged hardening:
  safe static grammar
  → structured runtime step correlation
  → optional exact-version witness
  → bounded logs only if needed
```

No source, tests, plan, ADR, or `MEMORY.md` change is authorized by this audit alone.

The current B2 Step 5 continuation remains unchanged.

## 13. References

### Audit control

- [`README.md`](README.md)
  - defines audits as durable, non-controlling technical review records.

### Dependency/CI plan

- [`../plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](../plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)
  - defines the bounded CI dependency-exercise states;
  - admits the first direct requirements rule;
  - excludes broad CI interpretation;
  - keeps constraints and `uv.lock` consumption separate.

### Current CI source

- [`../src/upgradepilot/ci_dependency_exercise.py`](../src/upgradepilot/ci_dependency_exercise.py)
  - owns `DependencyCIExerciseResult`;
  - checks successful job/run state;
  - delegates static command recognition;
  - aggregates `proven` existentially.

- [`../src/upgradepilot/workflow_commands.py`](../src/upgradepilot/workflow_commands.py)
  - shallowly reads one job and visible `run:` commands;
  - splits common shell separators;
  - recognizes direct pip requirements installation and package invocation;
  - deliberately does not implement full YAML/shell semantics.

- [`../src/upgradepilot/github_actions.py`](../src/upgradepilot/github_actions.py)
  - acquires exact-head runs/jobs;
  - preserves optional step summaries with status/conclusion;
  - does not itself interpret dependency exercise.

- [`../src/upgradepilot/cli.py`](../src/upgradepilot/cli.py)
  - constructs `WorkflowDependencyExerciseInput`;
  - presents the CI dependency-exercise state and matching commands.

### Current controlled tests

- [`../tests/test_ci_dependency_exercise.py`](../tests/test_ci_dependency_exercise.py)
  - protects state meanings, precedence, direct-requirements proof, tox abstention, multiple-job abstention, source-path separation, and existential aggregation.

- [`../tests/test_workflow_commands.py`](../tests/test_workflow_commands.py)
  - protects the two current simple supported command shapes.

- [`../tests/test_github_actions.py`](../tests/test_github_actions.py)
  - protects exact-head run/job acquisition and runtime step-summary parsing.

- [`../tests/test_cli.py`](../tests/test_cli.py)
  - protects public `CI dependency exercise` presentation and current S004/S001-shaped orchestration expectations.

### Related prior audit

- [`2026-08-01_AUDIT-001_exact-pr-file-acquisition-evidence-contract.md`](2026-08-01_AUDIT-001_exact-pr-file-acquisition-evidence-contract.md)
  - demonstrates the same audit discipline: distinguish necessary evidence controls, derivable metadata, proportionality concerns, and future reassessment without silently changing the active product contract.
