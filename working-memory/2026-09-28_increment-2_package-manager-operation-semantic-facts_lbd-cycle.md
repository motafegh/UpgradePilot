# Increment 2 — Static Package-Manager Operation Declaration and Semantic-Fact Core — Learning-by-Doing Cycle

## Smart Situational Override Rule

This cycle began under the previous single-A/B+C cadence. During its pre-B orientation, the project refined the canonical Learning-by-Doing model to A0 → A1 → A2 → B → Verification → D → E with C continuous across the whole cycle. On resumption, this existing record is retained rather than creating a duplicate cycle record; the new governance is applied from a deliberate A0 re-entry. The Smart Situational Override Rule permits this transition because no Increment-2 Build began. The rule does not create Build authorization or weaken evidence truth.

**Date:** 2026-09-28  
**Cycle status:** ACTIVE — A0 and A1 complete; A2 upcoming-responsibility orientation is current and stops at its pre-B understanding gate  
**Primary operation:** Learning-by-Doing orientation under the already-admitted Runtime Dependency-State Proof plan; Build/Implement is not yet entered  
**Controlling plan:** `plans/RUNTIME_DEPENDENCY_STATE_PROOF_COMPLETION_PLAN.md`  
**R4 implementation sequence:** `working-memory/2026-09-27_runtime-dependency-state-proof-implementation-and-verification-planning.md`  
**Accepted architecture:** `docs/architecture/ADR-0010-package-manager-semantic-facts-and-runtime-dependency-state-composition.md`  
**Live position owner:** `MEMORY.md`

UP-SKILL:upgradepilot-learning-by-doing  
UP-SKILL:upgradepilot-working-memory

## Canonical cycle status

```text
A0 — DONE: current main/owners/source/tests reconciled; existing cycle record reused; living A map seeded
A1 — DONE: Ali confirmed the continuity model; no material continuity gap surfaced
A2 — CURRENT: upcoming responsibility orientation; pre-B understanding gate pending Ali response
B — PENDING
Verification gate — PENDING
D — PENDING
E — PENDING
C — CONTINUOUS: preserve meaningful progression across A0→E
```

## Why no separate new plan

No additional plan is needed. The controlling runtime dependency-state plan already owns the program responsibility, ADR-0010 owns the accepted cross-layer architecture, and the R4 implementation record already defines Increment 2's implementation responsibility, proof cases, pass condition, and next increments.

A second plan would duplicate ownership rather than clarify it. This record therefore owns only the real Increment-2 cycle progression and learning/evidence history.

## Governance refinement interruption and resumption

While this cycle was stopped before Build, Ali and the assistant identified that the old single-A cadence did not model fresh-session reorientation, user continuity onboarding, whole-cycle C preservation, or E handoff cleanly enough. The canonical governance was refined and recorded in `working-memory/2026-09-28_lbd-cycle-governance-refinement.md`.

Resumption rule:

```text
reuse this existing cycle record
→ execute refined A0 current-state reconciliation and seed/update the living A map
→ execute A1 continuity/recent-work onboarding
→ STOP at A1 continuity gate
→ execute A2 upcoming-responsibility orientation using the historical material below as input
→ STOP at A2 pre-B gate
→ only then may B begin when authorized
```

No Increment-2 product source or tests were changed before this governance refinement.
## Refined A0 — current-state reconciliation + cycle initialization — DONE

### Current-state evidence checked

A0 re-read the current canonical/active surfaces needed for Increment 2:

- root `AGENTS.md`, `OPERATING_GUIDE.md`, and the Learning-by-Doing / working-memory Skills after the 2026-09-28 governance refinement and root-context compaction;
- current `MEMORY.md`; 
- `plans/RUNTIME_DEPENDENCY_STATE_PROOF_COMPLETION_PLAN.md`; 
- `working-memory/2026-09-27_runtime-dependency-state-proof-implementation-and-verification-planning.md`; 
- accepted `docs/architecture/ADR-0010-package-manager-semantic-facts-and-runtime-dependency-state-composition.md`; 
- this existing Increment-2 cycle record and the recent governance-refinement/compaction records;
- current source seam: `src/upgradepilot/dependency/pip_command.py`, `direct_install.py`, and `environment_selection.py`; 
- current focused tests: `tests/test_direct_install_declaration.py` and `tests/test_project_environment_selection.py`; 
- recent `main` commit history.

### Freshness / implementation reconciliation

The verified Increment-1 implementation head remains `a47923ee778b0984966bc09b8d01169205d0f7f9`. A compare from that commit to current `main` found **no changes under `src/`, `tests/`, `experiments/`, or `tools/`**. All later changes are governance/planning/working-memory reconciliation rather than product implementation.

Therefore:

```text
Increment 1 implementation truth remains intact
+ Increment 2 still has no product Build
+ current source seam is unchanged
+ no fresh implementation evidence invalidates the selected Increment-2 route
```

### Reconciliation discovered during A0

The controlling runtime-state plan and the active R4 implementation-sequence record still contained several references to the superseded `A → B → C → D → E` / `B+C` cadence. Their **technical responsibilities and proof obligations were still correct**, but their process language conflicted with current governance.

A0 reconciled only that process vocabulary:

- `a512ec1` — aligned `plans/RUNTIME_DEPENDENCY_STATE_PROOF_COMPLETION_PLAN.md` with A0/A1/A2/B/Verification/D/E + continuous C;
- `84edbe0` — aligned the R4 continuation rhythm while preserving Increment-1 historical cadence as history.

No semantic/architecture/build scope was changed by this reconciliation.

### A0 conclusion

No contradiction requires replanning or redirecting Increment 2. The selected responsibility remains:

> parse one package-manager operation occurrence once and expose independent typed semantic resolution for manager environment selection, installation destination, package mutation mode, and direct requirement handling, without runtime claims or universal config reconstruction.

The existing cycle record is reused rather than creating a duplicate record, as already decided during the governance transition.

## Living A-phase orientation / learning map

This map is a living cycle aid, not a second plan. A1 may add/remove items when Ali's continuity gaps become visible.

### A1 — continuity / recent-work onboarding topics

- [x] Reconnect Increment 1's closed result: exact-command successful execution evidence exists, but it does not establish package-manager meaning or resulting package state.
- [x] Reconnect the governance interruption: Increment 2 started orientation but **no Build began**; governance was refined before product work continued.
- [x] Explain what changed since that point: LbD A0/A1/A2 model + continuous C, root governance compaction, and plan/R4 cadence reconciliation only.
- [x] Re-establish current live position: Increment 2 remains selected; technical scope/ADR/plan did not change.
- [x] Reconnect the current source seam: `pip_command.py` recognizes bounded pip prefixes; `direct_install.py` and `environment_selection.py` consume/reinterpret pieces independently.
- [x] Surface any continuity gaps/questions from Ali and record them before A2 — none surfaced at the A1 gate.

### A2 — upcoming responsibility orientation topics (do not execute before A1 gate)

- [ ] Why one dependency-owned package-manager operation declaration should replace repeated prefix interpretation.
- [ ] Invocation identity/forms that matter: bare pip, `python -m pip`, explicit interpreter relation, and pip global `--python` placement.
- [ ] The four independent semantic facts and why they must not collapse into one `valid install` boolean.
- [ ] Shared bounded semantic provenance/problem representation and fail-closed unresolved material values.
- [ ] Command-local decisive semantics first: especially `--dry-run`, target/destination distinctions, and `--no-deps` direct-requirement meaning.
- [ ] Exact Increment-2 pass condition, proof cases, non-goals, and ownership depth.

### A-phase understanding gaps

None are assumed at A0. A1 must discover them from Ali's actual questions/reasoning rather than infer them from prior approval.
## Refined A1 — continuity / recent-work onboarding — DONE

Ali confirmed both continuity propositions:

1. Increment 1 proves successful execution of the exact command occurrence, not resulting package state.
2. Increment 2 has not entered Build; subsequent work before this point was governance/reconciliation while the technical responsibility remained unchanged.

No material A1 understanding gap was identified. The cycle therefore advances to A2 only.
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

## Historical pre-refinement A orientation — input to refined A1/A2

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

## Historical pre-refinement understanding gate — superseded by refined A1/A2 gates

Before B begins, Ali should be able to reason about these two points:

1. Why is a successful exact command from Increment 1 still insufficient to say the proposed dependency became present?
2. Why should “manager environment”, “installation destination”, “mutation mode”, and “direct requirement handling” remain separate facts instead of one combined “pip install is valid” result?

No product source/test Build should begin until this gate is cleared or a justified Smart Situational Override is explicitly recorded.
