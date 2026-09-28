# Increment 2 — Static Package-Manager Operation Declaration and Semantic-Fact Core — Learning-by-Doing Cycle

## Smart Situational Override Rule

This cycle follows the canonical A/B+C/verification/D/E cadence under the Smart Situational Override Rule from root `AGENTS.md`. Any material deviation must be explicit and reconciled with the correct owner. The rule does not create Build authorization or weaken evidence truth.

**Date:** 2026-09-28  
**Cycle status:** ACTIVE — canonical A orientation established; understanding gate pending  
**Primary operation:** Learning-by-Doing orientation under the already-admitted Runtime Dependency-State Proof plan; Build/Implement is not yet entered  
**Controlling plan:** `plans/RUNTIME_DEPENDENCY_STATE_PROOF_COMPLETION_PLAN.md`  
**R4 implementation sequence:** `working-memory/2026-09-27_runtime-dependency-state-proof-implementation-and-verification-planning.md`  
**Accepted architecture:** `docs/architecture/ADR-0010-package-manager-semantic-facts-and-runtime-dependency-state-composition.md`  
**Live position owner:** `MEMORY.md`

UP-SKILL:upgradepilot-learning-by-doing  
UP-SKILL:upgradepilot-working-memory

## Canonical cycle status

```text
A — ORIENTATION ESTABLISHED / UNDERSTANDING GATE PENDING
B — PENDING
C — PENDING / continuous with B
Verification gate — PENDING
D — PENDING
E — PENDING
```

## Why no separate new plan

No additional plan is needed. The controlling runtime dependency-state plan already owns the program responsibility, ADR-0010 owns the accepted cross-layer architecture, and the R4 implementation record already defines Increment 2's implementation responsibility, proof cases, pass condition, and next increments.

A second plan would duplicate ownership rather than clarify it. This record therefore owns only the real Increment-2 cycle progression and learning/evidence history.

## Cycle responsibility

Move UpgradePilot from repeated narrow package-manager prefix interpretation toward one reusable static package-manager operation declaration that can feed independent package-manager semantic facts.

The intended progression is conceptually:

```text
parser-neutral StaticCommandOccurrence
→ one dependency-owned package-manager operation declaration
→ independent semantic facts
   ├─ manager environment selection
   ├─ installation destination
   ├─ package mutation mode
   └─ direct requirement handling
```

The Increment-2 pass condition remains:

> one exact package-manager occurrence can feed independent typed semantic resolution without runtime claims or universal config reconstruction.

## A — Pre-implementation learning / orientation

### 1. Starting implementation truth

Increment 1 already established the reusable execution boundary:

```text
static/runtime step identity
→ correlated successful user-step execution
→ exact-command structural eligibility
→ exact-command execution evidence
```

That proves a bounded proposition that an exact command occurrence executed successfully. It deliberately does not prove what pip/uv effectively did or what package state resulted.

### 2. Current source seam

#### `src/upgradepilot/dependency/pip_command.py`

The current helper `parsed_pip_install_arguments(...)` recognizes bounded pip install prefixes and returns the remaining typed command atoms.

Current admitted shapes include:

```text
pip install ...
pip3 install ...
python -m pip install ...
python3 -m pip install ...
```

Its current result is essentially:

```text
install arguments | not this shape | materially unresolved prefix
```

It does not preserve a reusable typed operation identity such as invocation form, explicit interpreter relation, pip global-option placement, or semantic facts.

#### `src/upgradepilot/dependency/direct_install.py`

This consumer uses the pip helper and then independently interprets `-r/--requirement` arguments against an already-established repository dependency-source path.

Its proof stops at visible static declaration. It does not establish execution, mutation, installed version, or package state.

#### `src/upgradepilot/dependency/environment_selection.py`

This consumer also uses the pip helper for local-project pip installs while separately interpreting uv command identity and uv-specific selectors/options.

This exposes the architectural pressure directly: package-manager operation identity is partly reconstructed inside different consumers instead of being parsed once into one dependency-owned declaration.

### 3. What Increment 2 is fixing

The problem is not merely “support `--dry-run`.”

If each downstream consumer independently asks:

```text
is this pip?
is it python -m pip?
where is install?
are there pip global options?
which arguments belong to the operation?
```

then package-manager identity and invocation semantics can drift across consumers.

ADR-0010 therefore requires:

> Parse one package-manager operation once.

The package-manager declaration should preserve enough static identity for later semantic resolvers without becoming a universal shell parser or universal pip/uv configuration model.

### 4. The four independent semantic facts

These are deliberately separate because proving one must not accidentally prove the others.

#### Manager environment selection

Question:

> Which Python/package-manager environment does this invocation select or relate to?

Examples of relevant static evidence can include an explicit interpreter form or pip's global `--python` relation.

This is not automatically the same proposition as the final installation destination.

#### Installation destination

Question:

> Where is the package state being written or targeted?

Examples later include explicit destination-changing mechanisms such as target/user/root/prefix-style behavior where admitted.

A command can select one manager/interpreter environment while directing installation somewhere else, so this fact must remain independent.

#### Package mutation mode

Question:

> Does the effective operation actually mutate/synchronize package state, or is it non-mutating?

The decisive first example is explicit `--dry-run`.

```text
exact command executed successfully
+
effective dry-run
≠ package state changed
```

This is why Increment 1 execution evidence alone cannot support the later requirement-state proposition.

#### Direct requirement handling

Question:

> Does the operation still include the exact direct requirement that UpgradePilot is reasoning about?

This must distinguish direct-package treatment from transitive-dependency treatment. For example, pip `--no-deps` suppresses dependency installation; it does not by itself exclude the explicitly requested direct requirement.

### 5. What “independent facts” buys us

Avoid one giant boolean such as:

```text
safe_install = true
```

Instead later composition can reason from explicit propositions:

```text
operation identity known
AND mutation mode supports state change
AND direct requirement is included
AND manager environment is sufficiently established
AND destination is sufficiently established
AND exact command execution is supported
→ candidate command-completion requirement-state witness
```

That final composition belongs to a later increment, not this one.

### 6. Expected Increment-2 Build responsibility after the gate

If the A gate is cleared and Build is explicitly entered, the already-admitted plan expects us to:

1. replace repeated pip-prefix interpretation with one reusable static package-manager operation declaration;
2. preserve command location and invocation form;
3. support the bounded invocation forms required by the accepted first family, including explicit-interpreter/global-option forms as justified;
4. introduce shared semantic-resolution provenance/problem representation;
5. introduce the four independent facts;
6. implement command-local decisive semantics first;
7. preserve dynamic/unsupported material inputs as semantic problems instead of guessing.

Required proof cases already exist in the R4 plan, including bare pip, `python -m pip`, explicit interpreter forms, pip global `--python`, `--dry-run`, destination distinction, `--no-deps`, unresolved material values, and parse-once behavior.

### 7. Explicit non-goals for Increment 2

Increment 2 does **not** yet solve:

- workflow/job/step environment precedence;
- `GITHUB_ENV` propagation;
- setup-python/PATH executable provenance;
- virtual-environment activation provenance;
- ambient `PIP_*` / `UV_*` process variables;
- user/system/project persistent config reconstruction;
- universal pip/uv option coverage;
- resulting package-state proof;
- later package exercise/compatibility;
- maintainer-action permission;
- generic job-log/stdout/artifact acquisition.

Those remain later responsibilities, principally Increment 3 and Increment 4.

### 8. Professional engineering ownership target

**Primary:** code/system understanding — own the boundary between parser-neutral command evidence, one package-manager operation declaration, and downstream semantic facts.

**Secondary:** design/system judgment — understand why operation identity is parsed once while semantic propositions remain independent rather than collapsing into one “effective install” object.

**Required depth:** must own the responsibility/proof boundaries and normal data flow; exact class/function names and full pip/uv option catalogs remain recognize/lookup-level.

## A understanding gate — STOP

Before B begins, Ali should be able to reason about these two points:

1. Why is a successful exact command from Increment 1 still insufficient to say the proposed dependency became present?
2. Why should “manager environment”, “installation destination”, “mutation mode”, and “direct requirement handling” remain separate facts instead of one combined “pip install is valid” result?

No product source/test Build should begin until this gate is cleared or a justified Smart Situational Override is explicitly recorded.
