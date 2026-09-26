# Effective package-manager semantics system design — 2026-09-24

Status: ACTIVE — design/reconciliation before Build  
Operation: Planning/Design + Learning-by-Doing  
Current intent: determine the proper and smartest coherent system UpgradePilot should build for effective package-manager semantics and runtime dependency-state proof.

## Naming and retrieval convention for this active responsibility

**Use expressive subject names first in discussions, working memory, plans, learning checkpoints, and handoffs.** Preserve existing historical identifiers only in parentheses when they are needed to locate older files or checkpoints; never rely on bare `R2`, `B4`, `B5`, `Route A`, or `Route B` to carry meaning. Expand unfamiliar terms at first meaningful use. Existing filenames and old historical text are not renamed retroactively.

- **Effective Package-Manager Semantics — Supported Subsystem Boundary Design (R2):** the *current* design review: which package-manager command, environment, configuration, provenance, and direct-observation relationships the coherent first supported system should own.
- **Evidence Source, Type, and Data-Flow Design (R3):** concrete representation and cross-module flow *after* the subsystem boundary is reviewed.
- **Command-Derived Requirement-State Proof (historical Route A):** positively established effective pip/uv semantics plus exact runtime success, supporting the exact proposed requirement at command completion under the accepted proof contract.
- **Direct Target-Owned Package-State Observation (historical Route B):** independently observed package/version state in an identified target environment at an identified observation time; it does not prove how the package got there.
- **Proposition-Relative Effective-Semantics and Fail-Closed Resolution Contract (historical B4):** resolve each required semantic dimension as non-defeating, defeating, or unresolved for the exact claim.
- **Requirement-Satisfied-at-Command-Completion Proof Contract (historical B5):** the positive command-derived proof requirements and their time-bound claim limit.
- **Rejected Partial-Implementation Routes (historical B6):** the previously rejected narrow implementations, *not* a rejection of the coherent subsystem.

These are readable aliases for existing historical checkpoints and candidate routes, not new or expanded product semantics or architecture approval. See `working-memory/2026-09-24_runtime-state-reconciled-design-baseline.md` for the references to the original owners.

## Why this working memory exists

Previous Runtime Dependency-State Proof Cycle 1 correctly rejected a narrow partial implementation that would only classify visible command-local cases such as `--dry-run` or `--no-sync`.

That result should not be interpreted as:

```text
simple implementation is insufficient
→ defer the responsibility
```

The current responsibility is instead:

```text
simple implementation is insufficient
→ use the investigation results to identify the proper system boundary
→ design the coherent evidence/proof subsystem that solves the real problem
→ build it when the design and proof contract are sound
```

The goal is not artificial minimality. The goal is the proper and smartest architecture for the real UpgradePilot product responsibility, while still avoiding unrelated universal infrastructure.

## Prior investigation records

Primary evidence and design records:

- `working-memory/2026-09-21_f6-post-install-package-state-feasibility.md`
  - established the exact **Post-Install Package-State Feasibility** proposition (historical F6);
  - separated runtime correlation from package state;
  - identified real pip/uv counterexamples;
  - compared target-owned runtime-state evidence sources;
  - established real public feasibility and retention limits.

- `working-memory/2026-09-21_runtime-install-command-semantic-eligibility.md`
  - previous Runtime Install Command Semantic Eligibility — Cycle 1 learning/build loop;
  - established the package-manager semantic families;
  - accepted **Command-Local Semantic Eligibility** (historical B1);
  - accepted **Evidence Ownership and Composition Split** (historical B2);
  - accepted **Bounded pip/uv Semantic Surface** (historical B3);
  - accepted **Proposition-Relative Effective-Semantics and Fail-Closed Resolution Contract** (historical B4);
  - accepted **Requirement-Satisfied-at-Command-Completion Proof Contract** (historical B5);
  - **Rejected Partial-Implementation Routes** (historical B6) rejected only the insufficient partial implementation routes.

- `working-memory/2026-09-22_b4-environment-evidence-data-flow-learning.md`
  - developed environment provenance/propagation/override reasoning;
  - distinguished declared values from executed writes and received process values;
  - explored `GITHUB_ENV`, step-local env, shell-local overrides, and precedence;
  - accepted proposition-first / demand-driven backward proof as the preferred reasoning strategy.

- `plans/RUNTIME_DEPENDENCY_STATE_PROOF_COMPLETION_PLAN.md`
  - owns the durable runtime dependency-state responsibility and proof boundaries.

- `working-memory/2026-09-24_runtime-package-state-decision-criticality.md`
  - parent action-relative investigation;
  - currently paused while this earlier runtime-state responsibility is reconsidered at the proper architecture level.

## Compact durable findings from previous investigation

### 1. Existing runtime correlation is intentionally weaker than package-state proof

```text
exact dependency source/version
+ exact dependency-consuming command
+ exact successful runtime correlation
!=
exact proposed version present in the relevant runtime environment
```

### 2. The problem is broader than visible flags

Material semantic families already identified include:

```text
non-mutating / no-sync behavior
package exclusion / selection narrowing
environment retargeting
overlay / version override
ambient environment/configuration
precedence and propagation
later state mutation
```

Representative examples include:

```text
pip --dry-run
PIP_DRY_RUN
uv --dry-run
uv run --no-sync
UV_NO_SYNC
--no-install-package
--target / --user / --prefix / --root
uv --with conflicting version
workflow/job/step env
GITHUB_ENV
pip/uv configuration
```

### 3. Command-local semantics and effective semantics are different responsibilities

Accepted distinction:

```text
command-local semantic eligibility
!=
effective package-manager semantics
!=
runtime package state
```

A visible decisive command-local defeater can be established positively.

Absence of a visible defeater does not prove effective semantics are safe/non-defeating.

### 4. Effective semantics are proposition-relative and dimension-based

Accepted **Proposition-Relative Effective-Semantics and Fail-Closed Resolution Contract** (historical B4):

```text
exact occurrence
+ exact state-proof proposition
+ one material semantic dimension
→ resolved_non_defeating
  | resolved_defeating
  | unresolved
```

Aggregation:

```text
any required dimension defeating
→ occurrence cannot serve as the state-producing witness

no defeating + at least one required unresolved
→ effective semantics unresolved

all required dimensions resolved non-defeating
→ effective-semantics gate may close
```

### 5. Preferred proof strategy is demand-driven / backward

Accepted reasoning direction:

```text
exact semantic proposition
→ nearest trustworthy process-level evidence
→ shell-local evidence if needed
→ step-local environment if needed
→ GITHUB_ENV/job/workflow/config provenance only as needed
→ unresolved if a necessary material edge cannot be established
```

The system should not reconstruct irrelevant upstream history when a stronger nearer witness already decides the semantic dimension.

### 6. Ownership split is already clear

```text
GitHub/workflow + shell evidence
→ provenance, scope, ordering, propagation, process-value relationship

dependency/package-manager semantics
→ interpretation of pip/uv meaning

CI/state-proof composition
→ whether those typed facts satisfy the stronger dependency-state proof
```

Do not move pip/uv semantics into Tree-sitter or generic CI runtime code.

### 7. Accepted positive state-proof contract

The accepted **Requirement-Satisfied-at-Command-Completion Proof Contract** (historical B5) has this general shape:

```text
P1 exact dependency identity
P2 exact source/environment relation
P3 exact static consumption occurrence
P4 command-local semantics admitted
P5 effective semantics resolved non-defeating
P6 exact runtime-success proof
P7 package-manager operation guarantee
→ exact proposed requirement satisfied at command completion
```

The claim stops at that boundary.

It does not establish:

```text
fresh installation by this command
artifact identity
later persistence
later exercise used the same state
behavioral compatibility
maintainer-action permission
```

### 8. What the Rejected Partial-Implementation Routes checkpoint actually rejected

The **Rejected Partial-Implementation Routes** checkpoint (historical B6) rejected:

```text
only visible command-local flag classification
only workflow/job/step env parsing
synthetic/rare explicit families built merely to satisfy the plan
```

because those routes did not close the real normal effective-semantics problem.

The checkpoint did not prove that a coherent effective-semantics subsystem is undesirable.

The current reconsideration is therefore legitimate:

```text
partial implementation insufficient
→ investigate/design the proper complete bounded subsystem
```

## Current goal

Design the proper and smartest coherent effective package-manager semantics subsystem that UpgradePilot should actually build.

The design should be:

```text
useful for real normal UpgradePilot cases
architecturally coherent
evidence/provenance preserving
fail-closed where truth cannot be established
manager-aware for pip/uv
compatible with current static-consumption and runtime-correlation architecture
capable of composing into the requirement-satisfied-at-command-completion proof contract
extensible to explicit target-owned state evidence when semantic proof cannot close
```

It should not be constrained merely because a narrower implementation is easier.

It also should not become unrelated universal infrastructure such as a full GitHub Actions emulator, complete shell interpreter, or arbitrary operating-system environment simulator unless real evidence later proves such scope is required.

## Next design question

The next question is:

> What should the first proper and smart supported effective-semantics boundary contain so that it solves the real normal pip/uv problem coherently, and what should intentionally remain unresolved outside that boundary?

We should answer this by comparing real evidence sources and relationships already discovered, including:

```text
command-local options
shell-local assignments/exports
workflow/job/step env
proven GITHUB_ENV writes and propagation
package-manager environment variables
observable pip/uv configuration
retargeting/environment identity
manager-specific precedence
runtime-success identity
optional explicit target-owned state witnesses
```

The result of this design step should be a coherent subsystem boundary and implementation sequence, not another isolated rule list.

## Current state — expressive progress names

```text
Prior Investigation Reconstruction (R1): DONE
Effective Package-Manager Semantics — Supported Subsystem Boundary Design (R2): IN REVIEW
Evidence Source, Type, and Data-Flow Design (R3): PENDING
Implementation and Proof-Sequence Planning (R4): PENDING
Build Authorization and Implementation (R5): PENDING
Real-Case and Regression Verification (R6): PENDING
Return to Parent Evidence-to-Action Integration (R7): PENDING
```

## Guardrails

- do not optimize for artificial minimality;
- do not implement isolated flag rules as the end solution;
- preserve uncertainty when required evidence is missing;
- use real product pressure and real supported cases;
- preserve current owner boundaries;
- do not weaken the effective-semantics and command-completion proof standards merely to make implementation easier;
- do not turn the subsystem into universal CI/shell/environment emulation without evidence;
- build the proper system once its boundary is understood well enough to justify implementation.

## Effective Package-Manager Semantics — Supported Subsystem Boundary Design checkpoint (historical R2)

Status: CANDIDATE — source/docs-backed design checkpoint; not yet final architecture selection and no Build authorization.

### Fresh current-source facts

Current source preserves the existing owner split well:

- `github/workflow_command_analysis.py` preserves parser-neutral command occurrences, literal/dynamic executable/argument atoms, shell structure, source order, and bounded whole-step relations. It does not currently expose a typed shell-environment mutation/assignment model.
- `github/workflow_definition.py` currently preserves run defaults/jobs/steps but does not preserve workflow/job/step `env:` mappings.
- `dependency/environment_selection.py` already interprets selected pip/uv project/environment semantics and some uv material negative/targeting options.
- `ci/workflow_commands.py` is already the normal shared traversal/composition seam where parsed command analysis and dependency semantics meet.
- `ci/runtime_strengthening.py` correctly owns structural eligibility for binding an exact static occurrence to successful runtime-step evidence. It does not own pip/uv semantics.

These facts support extension of the existing ownership chain rather than a parallel environment architecture.

### Fresh external semantic facts

Authoritative current documentation reconfirms:

```text
pip:
command line > environment variables > configuration files

uv:
command line > environment variables > persistent configuration

GitHub Actions env:
step > job > workflow while the scope executes

GITHUB_ENV:
a positively executed write becomes available to subsequent steps
in the same job, not to the writing step
```

Pip materially supports environment/config equivalents for command options including `PIP_DRY_RUN`, `PIP_TARGET`, `PIP_USER`, `PIP_ROOT`, `PIP_PREFIX`, plus global/user/site/`PIP_CONFIG_FILE` configuration.

Uv materially supports `UV_NO_SYNC`, `UV_PROJECT_ENVIRONMENT`, persistent project/user/system config, `--no-config`, and command-local sync/exclusion/targeting behavior.

### Candidate architecture: two complementary proof routes

Do not force static/effective-semantics reconstruction to solve every normal case.

```text
COMMAND-DERIVED REQUIREMENT-STATE PROOF (historical Route A)

exact dependency/source/environment proposition
→ command-local pip/uv semantic observations
→ effective semantic dimension resolution
→ exact runtime-success proof
→ requirement-satisfied-at-command-completion proposition

DIRECT TARGET-OWNED PACKAGE-STATE OBSERVATION (historical Route B)

exact target/run/job/environment identity
→ direct package-state observation
→ exact proposed-version state proposition
```

Both routes may feed the same downstream package-state proposition while retaining source/provenance and proof-strength differences.

A direct state witness does not retroactively prove the command semantics; it provides an independent state-proof route.

### Candidate effective-semantics evidence boundary

The system should own the following real evidence families where they can be positively established:

#### 1. Command/process-local package-manager semantics

Interpret package-manager-specific options while structured command atoms are available.

Material dimensions include:

```text
mutation/synchronization
changed-package inclusion/exclusion
target environment/location
version overlay/override
configuration-loading mode
selected project/group/extra scope where relevant
```

Representative inputs:

```text
pip --dry-run
pip --target / --user / --root / --prefix / --python
pip --isolated
uv --dry-run
uv run --no-sync
uv --no-install-package / --only-install-package
uv group/project selectors
uv --with conflicting package version
uv --no-config / --config-file
```

The semantic surface is proposition-relative, not an exhaustive option catalog.

#### 2. Declarative GitHub environment

Extend the provider workflow IR to preserve workflow/job/step `env:` with exact scope/provenance and explicit literal/dynamic/unresolved values.

Use GitHub's specificity rule:

```text
step env > job env > workflow env
```

Only values relevant to a material semantic dimension need interpretation by pip/uv.

#### 3. Bounded same-job GITHUB_ENV propagation

Support positively proven simple `GITHUB_ENV` writes only when exact occurrence execution, literal name/value, destination semantics, same-job ordering, and propagation are established.

Do not infer a write merely from source visibility or enclosing-step success.

Multiple writes are ordered evidence:

```text
latest positively established applicable update
→ inherited baseline for subsequent step
```

An execution-unresolved later write keeps that dimension unresolved rather than falling back to an earlier value.

#### 4. Shell/process-local overrides

The architecture should support process-near shell overrides because they can dominate inherited environment and terminate backward proof early.

Current parser IR does not yet expose a typed shell-assignment model, so this requires a deliberate provider/shell evidence extension rather than reparsing raw strings downstream.

Candidate bounded shapes include direct literal process-local assignment and simple ordered literal export/assignment under admitted shell/runtime relations.

Dynamic shell mutation, arbitrary wrapper behavior, command substitution, sourced scripts, and opaque shell state remain unresolved until separately justified.

#### 5. Observable package-manager configuration

Model only configuration whose content, applicability, and precedence are positively observable.

Examples:

```text
pip PIP_CONFIG_FILE when exact referenced content is available
pip --isolated / explicit neutralization of lower-priority sources
uv project uv.toml / [tool.uv] when exact repository file and applicability are established
uv --config-file when exact file is available
uv --no-config
```

Unknown runner/user/system configuration remains unresolved when it can materially affect a dimension and has not been made irrelevant by a higher-precedence established value.

Do not fabricate absence of user/system configuration.

#### 6. Environment/destination identity

Retargeting is a relationship problem, not a blacklist.

```text
target location/environment
+ exact selected/relevant runtime environment
+ positive relation
→ same environment for the proposition?
```

If the relation is not established, the state-proof dimension remains unresolved.

### Demand-driven resolution rule

For each material semantic dimension:

```text
closest decisive command/process evidence
→ shell-local evidence if needed
→ step env if needed
→ proven GITHUB_ENV/job/workflow inheritance if needed
→ observable manager config if needed
→ external/ambient source only if it remains material
→ unresolved when a necessary edge cannot be established
```

A higher-precedence decisive value makes lower-precedence unknowns irrelevant for that dimension.

Do not require complete environment reconstruction.

### Direct target-owned state evidence boundary

When **Command-Derived Requirement-State Proof** remains unresolved, **Direct Target-Owned Package-State Observation** may establish the package-state proposition independently.

Preferred source classes remain:

```text
structured installed-state output
→ targeted package-version output
→ bounded inventory output
→ bounded installer-state observation/log
```

Examples:

```text
pip inspect
importlib.metadata.version(...)
pip list --format=json
pip freeze
uv environment inspection
bounded installer output when stronger state sources are unavailable
```

The evidence must preserve repository/head/run-attempt/job/environment/observation provenance and unavailable/expired state.

### Intentionally unresolved in the candidate first proper system

The following should not be guessed or universally simulated:

```text
arbitrary preceding third-party action environment mutation
arbitrary sourced shell scripts
dynamic expressions whose effective value cannot be resolved
arbitrary wrapper/nested process mutation
unknown runner-host environment
unknown pip global/user/site config when still material
unknown uv user/system config when still material
cross-job environment propagation unless separately explicit
reusable/composite-action internals not positively modeled
general persistence from command completion to arbitrary later step
```

These remain explicit `unresolved` states unless a nearer decisive witness or direct package-state observation makes them irrelevant to the proposition.

### Candidate system shape

```text
Workflow / shell evidence
    ↓
Effective environment facts with provenance
    ↓
Package-manager semantic interpreter
    ↓
Per-dimension effective semantic results
    ↓
Proposition-relative effective-semantics resolution
    ↓
┌──────────────────────────────────────────┐
│ Command-Derived Requirement-State Proof  │
│ resolved effective semantics             │
│ + exact runtime success                  │
└────────────────────┬─────────────────────┘
                     ↓
 requirement satisfied at command completion

OR

┌──────────────────────────────────────────┐
│ Direct Target-Owned Package-State        │
│ Observation                              │
└────────────────────┬─────────────────────┘
                     ↓
 exact observed package-state proposition
```

This architecture preserves the accepted proposition-relative effective-semantics and command-completion proof contracts while avoiding both bad extremes:

```text
isolated flag rules
vs.
universal runner/environment reconstruction
```

### Supported Subsystem Boundary Design — open review question

Before selecting this boundary, Ali should understand and challenge three core choices:

1. why effective semantics should be resolved per material dimension instead of one whole-environment boolean;
2. why higher-precedence/nearer evidence can terminate backward proof without reconstructing every upstream source;
3. why a direct package-state witness should be a parallel proof route rather than being treated as proof that command semantics were safe.

If these survive review, **Effective Package-Manager Semantics — Supported Subsystem Boundary Design** may be refined/closed and **Evidence Source, Type, and Data-Flow Design** may design the concrete source/type/data-flow architecture.

Sources checked for this checkpoint include current official pip configuration/install documentation, current uv configuration/project/CLI documentation, and current GitHub Actions workflow/env documentation.

UP-SKILL:upgradepilot-planning-design
UP-SKILL:upgradepilot-learning-by-doing
UP-SKILL:upgradepilot-working-memory

## September 24 — agreed evidence-first sequencing and action-synthesis boundary

**Status: AGREED project sequencing for the current subsystem-boundary journey; not a new Charter outcome, stable action semantic, architecture approval, or Build authorization.**

- **Decision:** Defer expanding or redesigning the maintainer-action evaluator while the selected trustworthy evidence/proof capability is designed, built, and verified. Keep the existing explained-abstention evaluator operational; do not infer non-abstention permission from the current limited producer set.
- **Essential qualification:** Do **not** defer *action-relative evaluation*. Periodically test which exact evidence facts are decision-critical to a specific bounded maintainer action, which remain unresolved, and whether a proposed evidence subsystem offers genuine product value. The evidence system is not an unlimited prerequisite project that must be fully complete before any later action work.
- **Future option review:** The Charter's current outcome family and the accepted synthesis specification remain controlling now. Once sufficiently representative real evidence and product understanding exist, review the action categories, their meanings, and their proof requirements through the proper product/semantic owners. A possible future revision is not an authorization or a conclusion that the existing categories must change.
- **Immediate continuation:** Resume the existing **Effective Package-Manager Semantics — Supported Subsystem Boundary Design** review of candidate **Command-Derived Requirement-State Proof** and **Direct Target-Owned Package-State Observation** against realistic pip/uv evidence, actual source ownership, the established effective-semantics and command-completion claim limits, and action-relative value. Preserve candidate-versus-accepted distinctions, then design evidence source/types/data flow only after the subsystem boundary is reviewed; reconcile the runtime-state master-plan sequence before Build if the selected architecture changes its admitted route.

**Learning-by-Doing checkpoint:** Product sequencing and downstream consumer boundary oriented; agreed sequencing decision preserved; working-memory update recorded; next: resume with a concrete subsystem-boundary proof-route example and review the learner's explanation before final design selection.

References: `PROJECT_CHARTER.md`; `docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md`; `plans/END_TO_END_PRODUCT_FLOW_LEARNING_AND_EVIDENCE_TO_ACTION_EXECUTION_PLAN.md`; `plans/RUNTIME_DEPENDENCY_STATE_PROOF_COMPLETION_PLAN.md`; `working-memory/2026-09-24_runtime-state-reconciled-design-baseline.md`.

## September 24 — state-witness scope and reuse learning clarification

See `working-memory/2026-09-24_r2_state-witness-scope-checkpoint.md` for the short reasoning checkpoint and provenance. An already sufficient **Command-Derived Requirement-State Proof** witness supports only its own package/environment/time-bounded claim; later commands or **Direct Target-Owned Package-State Observation** are not redundant mandatory gates. A later-time presence or actual test-use claim needs the additional relevant environment, continuity, and consumption evidence. Investigate only material intervening relations, and leave unproven persistence unresolved.

**Current discussion subject:** review how both candidate state-proof routes preserve what/where/when and what additional relations, if any, are needed when a downstream claim crosses a later environment/time/use boundary. This is still subsystem-boundary review, not approval of concrete data types or implementation.

## September 26 — analysis-depth and R2 closure discipline

**Status: AGREED process/design discipline for the active Supported Subsystem Boundary Design; not a new product requirement, fixed case quota, or Build authorization.**

The recent detailed investigations are justified because they have changed proof correctness, supported-case eligibility, or responsibility placement. They must not become an open-ended attempt to reconstruct every shell, runner, Python, pip, uv, action, or environment possibility.

Use this escalation test before opening another detailed investigation:

```text
Can the answer materially change
  1. correctness of the selected normal proof,
  2. the supported subsystem boundary,
  3. architectural / producer-consumer ownership,
  4. or a decision-critical product capability?
        |
        +-- yes -> investigate proportionately
        |
        +-- no  -> preserve unsupported/unresolved/deferred and move on
```

The controlling Cycle-1 completion target is deliberately bounded: establish **one trustworthy normal command family** from source/semantic/runtime evidence to a package-state proposition at the admitted observation boundary, with material non-installing, retargeted, dynamic, or otherwise close defeaters distinguished. Universal environment coverage is not required.

The compact decision register now owns the finite, non-quota **R2 closure map**. It gives a stable zoom-out path while individual learning-by-doing investigations zoom in:

```text
setup-python / PATH / bare pip
→ bounded venv / bare pip
→ remaining normal interpreter and manager-target families
→ supported effective operation/config semantics
→ Route A positive command-derived state proof
→ Route B / later-use scope decision
→ R2 supported-boundary classification and closure
→ R3 evidence source/type/data-flow design
```

A checkpoint may collapse or disappear when earlier evidence makes it unnecessary. Do not manufacture work to complete the list mechanically. Conversely, do not expand a checkpoint into every conceivable edge case merely because one exists.

## September 26 — bare `pip` normal-case environment-identity clarification

**Status: AGREED supported-boundary direction; concrete producer/types and Build remain open.**

- A literal `pip install ...` / `pip3 install ...` is **not automatically unresolved** and should not be rejected as a command family merely because no `python -m` prefix is present.
- The unresolved proposition, when evidence is insufficient, is the **relationship between the effective bare executable and the Python/package environment it manages**.
- Positive environment identity may be established through a bounded, provenance-preserving relation such as an admitted `actions/setup-python` selection that establishes the later same-job PATH/executable relation, an admitted virtual-environment/PATH selection, or another explicitly supported mechanism.
- Explicit interpreter invocation (`python -m pip` or a supported explicit interpreter path), explicit manager retargeting (`pip --python <env>`), and bare-executable resolution are distinct evidence families with different proof obligations.
- `actions/setup-python` is a high-value normal case, not a universal prerequisite. Real workflows without it may still be resolvable through other positive environment-selection evidence; ambient bare `pip` with no established relation remains reasoned unresolved.
- Directional GitHub code search on 2026-09-26 showed `pip install` and `actions/setup-python` co-occur very frequently in public workflow files, while a substantial set of `pip install` workflow matches do not contain `setup-python`. These search counts are discovery evidence only (file matches, not unique repositories or proof of same-job ordering) and must not be converted into a product probability or trust shortcut.

- **Normal-vs-edge qualification:** `update-environment: false` is a legitimate action configuration but should not dominate first-boundary design. It prevents this action from supplying the usual PATH-selection relation, so a later bare `pip` must be resolved from some other positive source or remain unresolved. This defeats only that proof edge. Do not infer that the action failed, that no `pip` exists, or that bare `pip` is unsupported. A workflow intentionally disabling environment updates will commonly need an explicit selected-interpreter/output relationship if it wants to use the configured Python deterministically.

- **Current runtime-correlation reuse and gap:** `ci/workflow_runtime_correlation.py` already treats both `RunStepDefinition` and `UsesStepDefinition` as correlatable user steps and preserves the matched runtime step status/conclusion. That is the correct existing owner to reuse for positive `setup-python` execution evidence. However, the current bounded correlation requires every static user step to have a unique literal explicit `name:` and rejects strategy/matrix jobs. Official GitHub `setup-python` examples include ordinary unnamed `uses:` steps, so named-step-only correlation is too narrow to define the first normal `setup-python` support boundary. This is a current implementation/evidence-identity gap, not authorization to weaken correlation or guess default runtime names. The supported design must decide a provider-accurate identity relation for ordinary unnamed action steps before Build.

- **Provider-accurate unnamed-step runtime identity evidence (2026-09-26):** current GitHub runner source `ActionRunner.GenerateDisplayName` deterministically derives an unnamed repository-action display name from its repository/path/ref and an unnamed script-step display name from its `run:` script; `FormatStepName` trims leading whitespace, keeps the first line, and applies the runner's normal run prefix. Two public runtime observations matched that contract: an unnamed pinned `actions/setup-python@<ref>` appeared as `Run actions/setup-python@<same-ref>`, and ordinary unnamed `run:` commands appeared as `Run <command>` (multiline scripts used the first line). Therefore the current explicit-`name:`-only correlation is narrower than provider semantics. Candidate direction: extend provider-owned static/runtime correlation with provider-accurate derived display identities for admitted literal unnamed steps, still requiring uniqueness/order/runtime match and failing closed for dynamic/ambiguous names; do not use raw source position alone as proof. Matrix/job-expansion correlation remains a separate limitation and is not solved by step-name derivation.

- **Generic correlated-step success can be reused for action effects (source/docs-backed candidate, 2026-09-26):** GitHub applies step-level `continue-on-error` to both `run:` and `uses:` steps, and the final step `conclusion` is post-`continue-on-error`; a failed continued step may therefore expose `conclusion=success` while its pre-masking outcome is failure. UpgradePilot's existing dependency runtime-strengthening consumer already protects this interpretation for `RunStepDefinition` by requiring `continue-on-error` absent/positively false before treating completed+success as positive execution support. `UsesStepDefinition` already preserves the same static field and workflow runtime correlation already preserves its runtime status/conclusion. Candidate direction: factor/reuse one provider/CI-owned correlated-step-success assessment for both step kinds, then let action-specific semantic producers consume that fact. Do not create setup-python-specific runtime-success logic.
- **Normal `setup-python` PATH-effect premise (source-backed candidate, 2026-09-26):** for the first strong case, positively establish that the action actually has a non-empty selected-version source (for example a supported literal `python-version`), effective `update-environment=true` (the current action contract defaults it to true), and successful unmasked action execution. Current `actions/setup-python` implementation then routes the selected CPython/PyPy/GraalPy finder through `core.addPath` for its interpreter/tool directories; GitHub's `GITHUB_PATH` contract prepends added directories for subsequent actions in the same job. If no version input/file resolves, setup-python may simply use the Python already in PATH and perform no new PATH selection, so the presence/success of the action alone is insufficient. Exact Python version need not be demanded when the proposition only needs the relation to the action-selected environment, but positive evidence that a path-producing selection occurred is required.

- **Intervening PATH/executable-selection reasoning (source-backed candidate, 2026-09-26):** do not treat the mere presence of an intervening step as a reason to abandon the `setup-python`→bare-`pip` relation. Start at the exact bare `pip` process and walk backward only through positively material executable/PATH selectors. A simple admitted intervening command with no PATH/executable effect is irrelevant to this proposition. Conversely, a closer shell-local PATH assignment, virtual-environment activation, proven `GITHUB_PATH` addition, or another positively modeled PATH-producing action may supersede an earlier selector. Arbitrary opaque third-party actions are not presumed to mutate PATH, but if their material PATH effect cannot be positively excluded or modeled for the needed claim, the executable-identity relation may remain unresolved rather than guessed.
- **Ordered `GITHUB_PATH` behavior (runner-source evidence, 2026-09-26):** GitHub runner `AddPathFileCommand` accumulates path-file entries into the job's prepend-path state, and handlers construct the effective PATH by prepending that accumulated state for subsequent steps. The runner removes duplicate matching entries and re-adds later writes so newer proven PATH additions take precedence over older matching/earlier selections. This supports the demand-driven rule that a closer positively established PATH producer can dominate an older `setup-python` selector for executable-resolution reasoning. Preserve the older fact as provenance; do not claim the newer path actually contains `pip` unless separately established.
- **Step-local `env: PATH` versus accumulated `GITHUB_PATH` is now provider-resolved for the normal script-step case (2026-09-26):** GitHub runner evaluates job/workflow environment into `Global.EnvironmentVariables`, merges step `env` into the step environment, then `ScriptHandler.AddPrependPathToEnvironment` constructs the launched script PATH by prepending the accumulated `Global.PrependPath` state above that environment PATH baseline. Therefore a literal step-level `env: PATH: ...` does **not by itself erase** previously accumulated `setup-python`/`GITHUB_PATH` entries; those prepend entries remain earlier in the launched script PATH. A shell-local PATH assignment/export executed inside the script occurs later and can still supersede executable selection for the exact `pip` process. Keep this rule bounded to the admitted normal GitHub script-step/provider path; container/custom execution shapes require their own evidence if later activated.
- **Current UpgradePilot representation gap exposed by that rule:** `src/upgradepilot/github/workflow_definition.py` currently does not preserve workflow-, job-, or step-level `env:` mappings in `WorkflowDefinition`, `StepsJobDefinition`, `RunStepDefinition`, or `UsesStepDefinition`; the parser's material-field sets omit `env`. The provider semantics are therefore understood, but current product evidence cannot yet express those declarative environment facts through this bounded IR. This is an evidence-source/type responsibility to carry into R3 if the selected supported boundary requires declarative env resolution; do not patch the parser during R2 merely because the gap is visible.

## September 26 — first Command-Derived Requirement-State Proof contract

**Status: AGREED first bounded positive Route-A family for R2 closure; concrete evidence types/implementation remain R3/R4+ and no Build is authorized.**

Select a deliberately normal pip family rather than a special target-directory case.

### Positive family

```text
exact repository requirement:
    <distribution>==<proposed-version>

exact admitted pip install occurrence:
    python -m pip install -r <that requirements source>
    OR equivalent supported explicit/resolved interpreter form

+ exact source/path applicability
+ effective normal direct-requirement handling
+ effective dry-run = false
+ positively resolved manager Python environment
+ positively resolved normal installation scheme for that environment
  (no unresolved effective target/user/root/prefix retargeting)
+ exact unmasked successful runtime execution
→ exact proposed requirement is satisfied in that resolved environment
  at command completion
```

The requirements-file variant is intentionally first because current pip `--only-deps` cannot be combined with `--requirement`; therefore a positively successful exact `-r` command cannot simultaneously have that incompatible effective mode. `--no-deps` does not defeat satisfaction of the directly listed requirement.

### Why starting state does not require a universal inventory here

For the normal environment install scheme and an exact direct requirement `name==version`, the proof proposition is **requirement satisfaction at command completion**, not fresh-write causality.

- if the exact version is already satisfied in the selected environment, pip may succeed without installing anything new and the proposition is already true;
- if a different installed version does not satisfy the exact requirement, normal pip resolution/install semantics may replace/downgrade as necessary to satisfy the command or fail;
- exact command success therefore supports the bounded satisfaction proposition once the effective command/source/environment/destination premises above are established.

Do **not** transfer this no-inventory simplification to pip `--target`: target-directory replacement semantics are different and may require `--upgrade` or starting-target evidence.

### Claim limit

This Route-A witness establishes only:

> the exact proposed direct requirement is satisfied in the positively resolved package environment **at completion of the exact successful pip command**.

It does **not** establish:

- that this command freshly installed or changed the package;
- which wheel/sdist artifact was selected unless separately evidenced;
- that the whole environment is dependency-consistent;
- package persistence after later mutations;
- that a later test/process used this environment or exact version;
- behavioral compatibility or successful imports;
- maintainer-action permission.

### Close defeaters / unresolved cases

Leave Route A unresolved or defeated for this first family when any material premise is not established, including:

- effective dry-run enabled or unresolved;
- exact requirements source/path or exact proposed pin not established/applicable;
- manager environment or normal destination scheme unresolved;
- effective `target`, `user`, `root`, `prefix`, or another material retargeting scheme not covered by this family;
- exact pip occurrence execution not positively correlated/successful without masking;
- unsupported/dynamic invocation shape or package-manager semantics.

A direct target-owned package-state observation remains an independent proof route and may still answer its own claim when Route A is unavailable.

## September 26 — effective operation/configuration precedence boundary

**Status: AGREED R2 checkpoint-4 semantic boundary; exact evidence producers/types remain R3/R4+ and no Build is authorized.**

For each package-manager semantic dimension needed by the exact claim, resolve the **effective value** with one common demand-driven precedence model. Do not reconstruct unrelated settings.

### Shared top-level precedence

Both current pip and uv documentation establish the same high-level priority:

```text
explicit command-line value
        >
effective process environment value
        >
applicable persistent configuration
        >
manager default
```

Stop for that semantic dimension as soon as a higher-priority source conclusively resolves it. Preserve the winning source/provenance. Continue downward only when the higher source is absent, explicitly non-decisive, or unresolved.

Manager-specific persistent-config ordering remains an adapter detail:

- pip: command-specific config section > global section; files are combined global → user → site → `PIP_CONFIG_FILE` (later overrides earlier); `PIP_CONFIG_FILE=os.devnull` disables config loading. `--isolated` ignores environment variables and user configuration, but is **not** equivalent to disabling every possible config source.
- uv: project config > user config > system config; `uv.toml` in a directory overrides `[tool.uv]` in that directory's `pyproject.toml`; `[tool.uv.pip]` overrides corresponding top-level settings for the pip interface. Environment variables override persistent config and CLI overrides both. `--no-config` disables persistent config discovery; `--config-file` replaces discovered persistent config.

### Proof-critical dimensions only

For the first supported package-state proof, resolve only these dimensions when material:

1. **Does this exact command handle/write the proposed direct requirement?**
   - pip/uv `--dry-run` decisively defeats command-derived installation/state production while preserving command execution facts.
   - current pip `--only-deps` is claim-relative: for a direct command-line requirement it excludes the user-supplied requirement itself, so that direct requirement cannot be proven installed by the command. For the common `-r/--requirement` family pip currently rejects combining `--only-deps` with `--requirement`; therefore an exact successful requirements-file command rules out that effective incompatible combination rather than requiring a separate universal `only-deps=false` proof.
   - `--no-deps` does not defeat satisfaction of the directly supplied requirement itself; it matters only if the selected proposition depends on transitive dependency installation.

2. **Which Python environment does the manager target?**
   - pip: launcher relation unless superseded by effective `--python` / `PIP_PYTHON`.
   - uv: effective `--python`, `--system`, or supported default environment discovery; config/environment forms use the same precedence rule.

3. **Where are package files installed?**
   - direct target/scheme selectors such as pip/uv `target`, pip `user`, pip `root`, pip/uv `prefix`, or manager-environment default scheme.
   - installation-scheme modifiers are not automatically equivalent to Python-environment identity.

4. **What starting-state/update premise is needed for the selected destination?**
   - resolve only when the selected Route-A family needs it. In particular, pip `--target` does not replace existing target contents by default; `--upgrade` changes that behavior. Exact starting-target/update requirements belong to the Route-A proof contract rather than a universal config sweep.
   - reinstall/ignore-installed/exact-sync style options are not universal gates for direct exact-requirement satisfaction; include them only when the chosen proof family or pre-state makes them material.

### Default inference rule

**Absence of a visible CLI flag is not evidence of a manager default.** A manager default may be claimed only after every higher-precedence source that could materially change that dimension is positively resolved as absent, disabled, or non-overriding.

Consequently:

- decisive CLI evidence can stop before environment/config inspection for that dimension;
- decisive process-environment evidence can stop before persistent config;
- repository-visible/config-explicit evidence can resolve a persistent setting when its manager-specific precedence is established;
- if a necessary lower source is ambient/unobservable and no higher source decides the dimension, the effective value remains reasoned unresolved. Do not invent “ambient safe.”

This means a plain normal-looking pip command may remain Route-A-unresolved for a material dimension such as dry-run or destination when environment/config provenance is unavailable. That is a truthful proof limit, not a reason to build a general runner/config emulator during R2. A later direct target-owned state witness remains an independent route.

### Current UpgradePilot capability gap

Current source has parser-backed CLI occurrence evidence and working-directory resolution, but it does not yet preserve declarative workflow/job/step `env:`, interpret `GITHUB_ENV` propagation, parse pip persistent config, or interpret uv persistent config for effective package-manager semantics. These are explicit R3 evidence-source/type/data-flow responsibilities **only for sources admitted by this boundary**.

Do not solve ambient user/system configuration universally. Prefer nearest decisive evidence; add bounded source adapters only when the selected normal proof actually requires them.

## September 26 — interpreter / manager-target family comparison

**Status: SOURCE/DOCS-BACKED CANDIDATE MODEL for R2 checkpoint 3; supported family selection still under review and no Build authorization.**

Use three distinct semantic dimensions instead of treating “the Python environment” as one field:

```text
launcher / executor identity
        ↓
manager-selected Python environment
        ↓
final installation destination / scheme
```

A stronger fact at one dimension does not automatically settle the next. This model explains both pip and uv without forcing them into identical command semantics.

### pip families

- **`python -m pip install ...`**: strongly binds the pip launcher to the exact invoking Python process. In the absence of an effective `--python` manager retarget and installation retargeters, the natural manager environment is that Python installation/environment. The launcher relation alone does not defeat `--target`, `--user`, `--prefix`, `--root`, or equivalent effective configuration.
- **Explicit interpreter path, e.g. `.venv/bin/python -m pip install ...`**: same relation as above, but with stronger static interpreter/environment identity because the executable path itself is explicit. Current `pip_command.py` does not recognize this normal prefix because it admits only literal `python` / `python3`.
- **`pip --python <python-or-venv> install ...` / `python -m pip --python <env> install ...`**: pip's current contract says it manages the specified interpreter/venv exactly as if pip had been invoked from that environment. Therefore the launcher and managed environment must remain distinct. For the manager-environment proposition, an explicit effective `--python` can make the launcher's own Python environment irrelevant. Current `pip_command.py` does not recognize the canonical global-option-before-command form because it expects `install` immediately after `pip`.
- **`--target <dir>`**: explicit direct installation directory. Current pip docs state packages are installed into that directory and existing files/folders are not replaced by default; `--upgrade` is required to replace existing target contents. This is therefore a strong destination selector but still needs material starting-target conditions for an exact final-state proof. A target directory is not automatically a Python environment or later import path.
- **`--user`**: selects Python's user installation scheme, not one fixed literal directory. `PYTHONUSERBASE` can change the base, default virtual environments can reject user installs because user site is not visible, and already-satisfied globally visible packages can make pip succeed without a fresh user-site write. Because this form is common in real workflows, it should be recognized as a material retargeting family, but it is a poor first direct-destination proof unless the needed user-scheme/environment premises are positively established.
- **`--prefix <dir>`**: selects a prefix under which lib/bin/top-level scheme directories are placed. pip explicitly warns that installed scripts/resources may still reference the interpreter running pip rather than an interpreter under the prefix and recommends `--python` when the intent is to manage another environment. Treat prefix as an installation-scheme selector, not proof of a target Python environment.
- **Default/no retargeter**: requires the next effective-operation/configuration checkpoint to prove that no higher-precedence CLI/environment/config value changes the manager environment or destination; absence of a visible CLI flag is not enough.

Directional GitHub workflow-file search on 2026-09-26 indicates `--user` has materially more visible CI pressure than canonical `pip --python`, while `--target` also appears in real workflows. These are discovery/file-match counts only, not unique-repository prevalence probabilities.

### uv pip families

uv is not a Python-launched package manager by default, so its executable identity must not be equated with its target Python environment.

- **default `uv pip install ...`**: uv requires a virtual environment by default and searches, in documented order, an active `VIRTUAL_ENV`, active `CONDA_PREFIX`, then a `.venv` in the current directory or nearest parent. This environment-discovery chain is manager-specific evidence, not pip PATH semantics.
- **`uv pip install --python <python-or-env> ...`**: explicit manager environment; uv documents that packages are installed into the environment linked to that interpreter/path. This is a high-value explicit positive selector.
- **`uv pip install --system ...`**: explicitly skips virtual-environment discovery and selects system Python from PATH. It is CI-oriented and materially common; it still requires positive system-executable resolution if an exact concrete Python identity is needed.
- **`uv pip install --target <dir> ...`**: installs packages at the top level of the given directory and does not require an existing Python environment; Python is needed for resolution/build compatibility, not as the installation environment. This cleanly demonstrates why manager-selected interpreter and final destination are independent dimensions.
- **`uv pip install --prefix <dir> ...`**: installs under lib/bin/top-level folders of the prefix and, like pip, warns that scripts/artifacts reference the installing interpreter rather than an interpreter under that prefix.
- **No `--user` equivalent**: uv explicitly does not support pip's user installation scheme.

Directional GitHub workflow-file search on 2026-09-26 found substantial `uv pip install` pressure, with `--system` and `--python` both materially represented; `--target` and especially `--prefix` were much less common. These counts guide priority only and are not semantic evidence.

### Current UpgradePilot ownership / gaps

- `dependency/pip_command.py` recognizes bare `pip/pip3 install` and literal `python/python3 -m pip install`, but not explicit interpreter paths or pip global options such as `--python` before `install`.
- existing pip direct-install consumers can preserve later install arguments such as `--target`/`--user`/`--prefix`, but no current producer interprets those arguments into effective manager-environment/destination evidence.
- `dependency/environment_selection.py` already owns bounded uv **project-selection** semantics for `uv sync` / `uv run`; it does not interpret `uv pip install`. uv lock/reachability owners also already exist. Therefore the missing work is specifically effective runtime package-manager semantics, not a new general uv subsystem.
- the already-existing claim-relative precedence/evidence architecture should own these dimensions; do not create one bespoke resolver for every option or manager.

**Checkpoint-3 selection — AGREED boundary:** first positive environment/destination families are (1) pip `python -m pip` and supported explicit-interpreter `-m pip`; (2) positively resolved bare pip; (3) pip explicit `--python` as a manager-environment selector; (4) pip explicit `--target` as a direct destination selector; (5) uv explicit `--python`; (6) uv `--system`; (7) positively established default uv virtual-environment discovery; and (8) uv explicit `--target`. Recognize `pip --user` as a material, common scheme selector but do not grant it a simple positive final-state contract until user-scheme and starting-state premises are closed. Recognize pip/uv `--prefix` as explicit scheme selectors but defer positive first-boundary proof unless product evidence activates them. Recognize pip `--root` / `PIP_ROOT` as a material destination-root modifier/defeater even though real workflow pressure is lower; it must block an unqualified default-destination inference when effective, but it is not a first positive family. Other resolver/build-only flags remain outside this checkpoint unless they change the selected package-state proposition.

This closes R2 checkpoint 3 at the semantic-boundary level. Concrete parser/producer/type support for explicit interpreter paths, pip global `--python`, uv pip semantics, and destination selectors remains R3/R4+ work.

## September 26 — bounded venv activation and sequential runtime-proof expansion

**Status: AGREED supported-boundary direction; exact evidence/type schema and Build remain pending.**

The current first-sequential-command runtime-strengthening rule remains a sound conservative baseline, but real normal GitHub workflows demonstrate that it is too narrow for the selected venv → bare-`pip` environment-identity case. Public workflow examples include both multiline `python -m venv .venv → source .venv/bin/activate → pip install ...` sequences and `source .venv/bin/activate && pip install ...` forms. Directional GitHub code search also shows thousands of workflow-file matches containing venv activation with pip installation; these counts are discovery evidence, not unique-repository prevalence statistics.

Do **not** replace the current rule with “successful step means every sequential command executed.” That is unsound: an earlier successful control-transfer command such as `exit 0` can terminate the shell before a later command while the step still succeeds. GitHub's admitted Bash/sh wrappers do provide fail-fast behavior (`bash -e -o pipefail` / `sh -e`), but fail-fast alone proves neither later-command reachability nor absence of successful shell termination/replacement.

**Bounded expansion direction:** permit later-command runtime support only through an explicitly admitted **sequential reachability composition**. A predecessor may advance the proof to the next command only when its semantics positively establish that, on successful execution, it:

1. returns control to the same containing shell rather than terminating/replacing it;
2. preserves the execution assumptions needed for the next inference (notably the admitted fail-fast context unless a different positive rule applies);
3. has any material environment effect represented explicitly; and
4. is itself positively reached/successful from the existing runtime/sequence evidence.

This is a small semantic contract, not a general shell simulator. Unknown commands, `exit`/`exec`/unmodeled sourced scripts, dynamic control flow, opaque shell-option mutation, and unsupported structures remain unresolved rather than being guessed.

**First venv positive candidate:** for admitted Bash/sh sequencing, a successful standard `python -m venv <env>` command without effective `--without-pip` gives a source-backed basis that the created environment contains its Python and bootstrapped pip; the standard generated `<env>/bin/activate` script prepends that environment's bin directory to PATH and returns control to the same shell. If that exact activation is then positively reached before a later bare `pip`, with no closer material executable/PATH mutation, the bare `pip` identity can be resolved to the venv. A pre-existing or arbitrary activation script does not inherit this guarantee merely from its filename.

The same principle may support a positive `source <known-standard-activate> && pip install ...` form: the `&&` syntax encodes conditional reachability, but the predecessor still needs the same positive fall-through/effect semantics. Do not globally reclassify all short-circuit structures as runtime-safe.

**Current product gap:** UpgradePilot has parser-backed ordered command occurrences and structural context, but no existing `python -m venv` / activation semantic producer and no generic sequential fall-through contract. The gap is therefore real and correctly belongs to later evidence/type/data-flow and implementation design if this R2 boundary is selected; no code change is authorized during R2.

### Bounded venv family — refined positive/negative premises

**Strong same-step candidate (normal CPython/Bash-sh case):**

```text
python -m venv <literal-env>
→ source <same-env>/bin/activate
→ bare pip install ...
```

Admit this path only when all material premises are positively established:

- admitted GitHub Bash/sh execution profile with the existing unmasked successful runtime-step correlation;
- parser-backed ordinary top-level ordering with no unsupported conditional/loop/background/control-transfer structure on the relevant path;
- literal/supported CPython `python -m venv <env>` creation command using the normal creation path (first supported family excludes `--upgrade` and dynamic/custom venv builders);
- no effective `--without-pip`: current CPython CLI defaults to bootstrapping pip, and successful creation runs `ensurepip --upgrade --default-pip`;
- the activation path resolves to the same created environment; successful normal creation also installs the standard activation script;
- the successful venv-creation command is an admitted fall-through predecessor, so the activation command is reached in the same shell;
- the standard generated activation script is the sourced file; it sets `VIRTUAL_ENV`, prepends `<env>/bin` (or provider-equivalent scripts directory) to PATH, clears prior command hashing with `hash -r`, does not disable the admitted fail-fast mode, and returns control to the containing shell;
- no closer material PATH/executable selector occurs between activation and the target bare `pip`;
- the later bare `pip` is positively reached through the bounded sequential-reachability chain and remains in an admitted ordinary structure.

Under those premises, bare-`pip` executable/environment identity may be resolved to the created venv. Step success may then support the later pip command only through this admitted reachability chain; it is not evidence that all commands in the script executed.

**Separate-step candidate:** GitHub documents that steps in one job execute on the same runner and share workspace/filesystem state, while each `run:` step starts a fresh process/shell. Therefore a successful venv-creation step may supply filesystem provenance to an immediately following activation/install step when the effective working-directory/path relation is positively the same. Environment activation itself never carries across steps; the later step must activate again. For the first boundary, prefer adjacent creation→activation/install steps (or otherwise require explicit continuity evidence) so arbitrary intervening mutation of the venv directory is not silently ignored. Current source already has `dependency/workflow_context.py::resolve_effective_working_directory`, which applies the bounded static precedence `step > job > workflow > repository root` and fails closed on dynamic/higher-precedence declarations. The remaining separate-step venv gap is therefore not static working-directory resolution itself; it is composing that static path identity with runtime filesystem continuity/non-mutation across the creation and activation/install steps. Exact continuity evidence/type design remains R3 work.

**Close defeaters / unresolved cases for the first family:**

- `--without-pip` defeats the inference that venv creation established a venv-owned bare `pip`; it does not prove no pip file exists in a pre-existing target or prove which earlier PATH entry will win;
- `--upgrade` is excluded from the first activation-provenance family because CPython's upgrade path does not reinstall the standard activation scripts in the same way; support may be added only if real pressure justifies it;
- dynamic/mismatched environment paths, different effective working directories, arbitrary pre-existing activation files, non-CPython/custom venv builders, unsupported shells, opaque shell-option/control-flow mutation, or an unresolved closer PATH selector remain reasoned unresolved;
- an arbitrary `source <path>/activate` occurrence does not prove the file is the standard script or that that environment owns a pip executable;
- arbitrary intervening steps between creation and activation are not presumed destructive, but continuity is not positively established merely from their presence; first-boundary support may require adjacency or explicit non-mutation evidence.

**Short-circuit form:** a sole/appropriately bounded `source <known-standard-activate> && pip install ...` may be admitted through the same fall-through predecessor contract. Do not globally remove `short_circuit` from the ineligible set: successful shell termination/replacement or more complex AND/OR lists can still make later-command execution unproven.


**Next learning/design checkpoint:** close the exact positive/negative premises of the bounded venv family—same-step versus separate-step creation, matching environment path, `--without-pip`, standard/generated activation provenance, closer PATH mutation, and the minimum runtime correlation needed—then decide whether the venv checkpoint is complete enough to move to the remaining normal interpreter / manager-target families.

