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

**Next learning/design checkpoint:** inspect the exact `actions/setup-python` → PATH → later bare `pip` chain and determine which edges can be positively established from provider/action semantics and existing UpgradePilot evidence, which require new typed evidence, and which remain unresolved. Then compare bounded venv/PATH activation.

