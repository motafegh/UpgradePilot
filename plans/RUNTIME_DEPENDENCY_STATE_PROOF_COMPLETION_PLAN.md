# Runtime Dependency-State Proof Completion Plan

**Status:** admitted bounded planning/execution plan; live selection remains owned by `../MEMORY.md`  
**Responsibility:** determine and implement the smallest trustworthy path by which UpgradePilot may establish that the exact proposed dependency version is present in the exact relevant CI environment, while preserving the distinction between command execution, resulting package state, later behavior/exercise, artifact mechanism, and maintainer-action permission  
**Parent execution owner:** [End-to-End Product Flow Learning and Evidence-to-Action Execution Plan](END_TO_END_PRODUCT_FLOW_LEARNING_AND_EVIDENCE_TO_ACTION_EXECUTION_PLAN.md)  
**Audit provenance:** [AUDIT-008 — F6](../audits/2026-09-19_AUDIT-008_current-system-evidence-to-action-readiness.md)  
**Primary investigation evidence:** [2026-09-21 runtime dependency-state investigation](../working-memory/2026-09-21_f6-post-install-package-state-feasibility.md)  
**Method:** Planning/Design + Learning-by-Doing; Build/Implement only after the applicable child responsibility is understood and explicitly selected

## 1. Responsibility and bounded outcome

The audit originally described F6 broadly as missing exact runtime installed dependency/artifact identity. Investigation narrowed the useful product responsibility.

The core proposition is:

> **The exact proposed dependency version is present in the exact selected dependency-consuming CI environment at the observation boundary justified by the evidence.**

This plan does **not** assume that a new log parser or package-state producer is always necessary. The first responsibility is to determine whether the existing exact dependency source + parsed command semantics + successful runtime correlation already prove the proposition for a bounded class of commands.

Only when that proof is insufficient should stronger target-owned package-state evidence be considered.

The plan deliberately separates four claims:

```text
exact dependency version is proposed
→ exact dependency-consuming command executed successfully
→ exact proposed version is present in that environment
→ relevant behavior exercised successfully
→ maintainer action positively justified
```

Each arrow requires its own admitted evidence. No later claim is inherited automatically.

## 2. Entry evidence and current implementation truth

The following evidence motivates this plan:

- current dependency-change admission already establishes exact old/proposed versions for supported normal sources;
- Tree-sitter-backed workflow command analysis preserves executable, literal/dynamic arguments, source position, structural context, and bounded whole-step relation;
- current pip parsing preserves install arguments after the `pip install` / `python -m pip install` prefix;
- current direct-requirements observation can establish the exact dependency source path used by the parsed install command;
- current runtime strengthening can bind an admitted static occurrence to an exact completed-successful GitHub step;
- current runtime correlation explicitly does **not** claim resulting installed version/package state;
- investigation verified that commands such as `pip install --dry-run -r requirements.txt` can currently retain the same direct-requirements declaration result as an ordinary install because `--dry-run` is syntactically preserved but not yet interpreted as installation-state semantics;
- current uv project-environment selection already interprets some material negative/targeting flags, proving that package-manager-specific semantic filtering belongs above Tree-sitter rather than inside shell syntax parsing;
- public Dependabot PR `Jam3s97/Aruba_Device_Tracker#83` demonstrates that target-owned runtime evidence can expose the exact proposed version when needed;
- historical `googlefonts/glyphsLib#1145` demonstrates that job logs can expire while run/job metadata remains, so log availability cannot be assumed;
- explicit package-state sources such as `pip inspect`, `pip list --format=json`, `pip freeze`, `importlib.metadata.version(...)`, and uv inspection outputs exist but should be added only if the proposition cannot be established more simply.

The dated investigation record owns the detailed source traces, real-case evidence, alternatives, and external reference links. This plan coordinates execution; it does not duplicate that investigation.

## 3. Stable owners and non-owners

Reference rather than re-specify:

- `PROJECT_CHARTER.md` — product mission and maintainer-facing outcome family;
- accepted decision/synthesis specifications — action permission and uncertainty semantics;
- ADR-0009 / parser-backed command analysis — accepted shell-command parsing method;
- `src/upgradepilot/github/workflow_command_analysis.py` — current parser-neutral shell syntax/structure evidence;
- `src/upgradepilot/dependency/pip_command.py` — current pip-install prefix/argument recognition;
- `src/upgradepilot/dependency/direct_install.py` — current requirements-source declaration observation;
- `src/upgradepilot/dependency/environment_selection.py` — current pip/uv project-environment semantic interpretation;
- `src/upgradepilot/ci/runtime_strengthening.py` and `ci/dependency_exercise.py` — current static-to-runtime correlation and proof boundary;
- `MEMORY.md` — sole live-position owner.

This plan must not turn Tree-sitter into a pip/uv semantic engine. Shell grammar owns syntax/structure; dependency/package-manager interpretation owns command meaning.

## 4. Program cycle discipline

This program uses the parent plan's canonical **A → B → C → D → E** Learning-by-Doing rhythm, but groups work into medium-sized engineering cycles so execution does not collapse into disconnected micro-steps or one oversized program pass.

Cycle policy:

```text
select one complete engineering responsibility
→ append that cycle to this master plan
→ execute its A → B → C → D → E progression in one active working-memory record
→ close the cycle from actual evidence
→ decide whether another cycle is genuinely required
```

Rules:

- this master plan owns the durable cycle structure, responsibility, entry condition, pass condition, stop line, and dependency between cycles;
- the active working-memory record owns the actual A/B/C/D/E progression, discoveries, implementation/proof evidence, learning checks, corrections, and cycle handoff;
- `MEMORY.md` alone owns which cycle/phase is live;
- do **not** pre-create speculative later cycles;
- append a later cycle only when the previous cycle's evidence demonstrates that its responsibility is necessary;
- one cycle may contain several closely coupled master-plan layers when splitting them would create artificial micro-cycles;
- a cycle must not silently absorb a materially different responsibility merely to avoid opening a justified next cycle.

### Cycle 1 — runtime dependency-state semantic proof

**Responsibility:** establish whether UpgradePilot can truthfully derive the bounded dependency-state proposition from existing exact dependency-source evidence + package-manager command semantics + exact successful runtime correlation, without requiring a new runtime-state/log producer.

Cycle 1 intentionally combines two tightly coupled layers:

```text
install-command semantic eligibility
+
command-success → dependency-state proof contract
```

Its phases follow the parent A → B → C → D → E rhythm:

```text
A — orient and classify current pip/uv semantic cases
B — select/design and, once authorized, implement the smallest semantic/proof change
C — preserve exact implementation/evidence/proof state
D — verify focused/integration/real-case evidence and transfer ownership
E — close the cycle and decide whether explicit runtime-state evidence is still necessary
```

**Cycle 1 pass condition:** one bounded positive command family has a precise, source-backed proof contract from exact dependency source through exact successful runtime execution to proposed-version presence/satisfaction at the admitted command-completion boundary, with material non-installing/retargeted/dynamic cases remaining distinguishable.

**Cycle 1 stop line:** do not add job-log or explicit package-state acquisition merely because such evidence exists. If command semantics cannot establish the proposition for a decision-critical normal case, close Cycle 1 at its honest boundary and consider the conditional next cycle.

### Conditional Cycle 2 — explicit target-owned runtime-state evidence

Cycle 2 is **not selected or active** by this plan revision.

Append/select it only if Cycle 1 establishes all of the following:

1. command semantics + exact runtime correlation are insufficient for a real normal case;
2. the unresolved package-state fact remains decision-critical under the parent evidence-to-action route;
3. an admitted target-owned evidence source can discriminate that fact proportionately.

If selected, Cycle 2 would own the smallest justified explicit package-state evidence path, preferring structured/targeted state evidence over generic human-log parsing.

If Cycle 1 is sufficient, **do not create Cycle 2**. Return to the parent evidence-to-action plan for the next action-relative responsibility.

### After runtime dependency-state proof

Behavior/exercise composition and maintainer-action integration remain important downstream responsibilities, but they are **not predeclared cycles of this program**. After the runtime dependency-state responsibility closes, return to the parent plan and select the next responsibility from actual evidence rather than assuming this program owns all downstream work.

## 5. Ordered responsibility layers

### Install-command semantic eligibility

Determine which currently admitted pip and uv command shapes positively support the stronger inference:

```text
exact source + exact proposed version
+ eligible install/environment command
+ exact successful runtime correlation
→ proposed version satisfied/present at command completion
```

Work includes:

1. enumerate only the pip/uv options reachable through current supported command shapes;
2. classify options as:
   - compatible with stronger installation-state inference;
   - materially non-installing/excluding/retargeting;
   - ambiguous/dynamic/unsupported;
3. verify current source/tests against that classification;
4. decide the earliest correct owner for each semantic restriction;
5. add no broader option catalog than current product pressure requires.

Initial discriminators include, but are not limited to, `--dry-run`, uv `--no-sync`, package exclusions/retargeting, and current already-handled negative/targeting selectors.

**Pass condition:** UpgradePilot can distinguish an ordinary admitted install/environment-forming command from a materially non-installing or retargeted command without changing the Tree-sitter responsibility.

**Stop line:** if the stronger inference still depends on unobserved runtime state even for a carefully bounded command class, do not force the inference; continue to the next layer.

### Command-success → dependency-state proof contract

Once semantic eligibility is understood, define the minimum evidence composition required for the stronger state claim.

The design must state exactly:

- which source establishes the proposed version;
- which command occurrence establishes consumption;
- which semantic eligibility result permits the inference;
- which exact run/attempt/job/step establishes successful execution;
- what temporal boundary the claim means (for example, satisfied/present at successful command completion);
- what later mutation it does **not** rule out.

Prefer reuse/composition of existing evidence types when sufficient. Introduce a new result type only if the proposition cannot be expressed safely with current types.

**Pass condition:** one precise proof contract exists for the admitted positive command family, with explicit negative/unresolved close defeaters.

**Stop line:** do not silently upgrade the claim to “present for the rest of the job,” “behavior exercised,” or “compatible.”

### Explicit target-owned package-state evidence fallback

Activate only for cases where command semantics + successful runtime correlation cannot establish the required dependency-state proposition and the fact remains decision-critical.

Evidence preference:

```text
explicit structured package-state output
→ explicit targeted package-version output
→ bounded inventory text
→ bounded human installer-log observation
```

Examples include `pip inspect`, `pip list --format=json`, `importlib.metadata.version(...)`, `pip freeze`, uv inspection outputs, and only then tightly bounded installer log interpretation.

Any source adapter must preserve exact repository/head/run-attempt/job/environment provenance and represent expired/unavailable evidence distinctly.

**Pass condition:** at least one fallback source is justified by real product pressure and has a bounded trust/provenance/error contract, or the plan records that no fallback producer is currently justified.

**Stop line:** no generic job-log ingestion subsystem merely because logs are available.

### Downstream handoff: behavior/exercise evidence

If dependency-state proof is produced, trace how it composes with existing package invocation/test/exercise evidence.

The composition must preserve:

```text
version present
!=
affected behavior exercised
```

and must account for ordering/environment identity where a later exercise is claimed to have used the observed version.

**Pass condition:** downstream consumers can distinguish package-state proof from behavior/exercise proof without inventing compatibility.

### Parent-plan re-entry: action-relative integration and end-to-end proof

Only after the dependency-state proposition is trustworthy should it be composed into the evidence-to-action path.

Validate:

- positive and negative semantic cases;
- dynamic/unsupported/retargeted cases;
- exact identity mismatch;
- real normal-path integration;
- broader deterministic regression;
- one bounded public Dependabot case when the claim requires live proof.

**Pass condition:** the selected runtime dependency-state capability changes a real action-relevant uncertainty or demonstrably strengthens a selected normal producer path without overstating action permission.

**Stop line:** if the capability does not materially change decision reachability or correctness after proof, close it as a bounded evidence improvement and return to the parent action-relative comparison rather than inventing more F6 scope.

## 6. Child working-memory rule

Each material layer should be executed through one active dated working-memory slice rather than expanding this master plan with session state.

A child record should contain only:

```text
master-plan link
→ exact layer/responsibility
→ current source/evidence orientation
→ small ordered actions
→ reasoning/learning checkpoints
→ proof/stop condition
→ resulting handoff
```

When the layer closes, preserve its result and open a new child record only if the responsibility materially changes.

The completed 2026-09-21 investigation record remains evidence/provenance and should not be reused as the active implementation log.

## 7. Proof discipline

For every layer, preserve:

```text
observation
→ provenance/context
→ interpretation
→ remaining uncertainty
→ bounded conclusion
```

Key non-proofs:

- parsed argument visibility is not package-manager semantic meaning;
- direct requirements declaration is not execution;
- successful runtime correlation is not automatically resulting package state;
- package state at one boundary is not persistence after later mutation;
- package state is not affected-behavior exercise;
- behavior exercise is not broad compatibility;
- none of these facts alone grants a maintainer action.

## 8. Allowed modification boundary

When Build is later authorized for a child slice, modifications may include only the earliest owners required by that selected responsibility, their focused tests, normal application composition, and directly necessary documentation/plan-memory handoff.

Likely current owners include:

- `src/upgradepilot/dependency/pip_command.py`;
- `src/upgradepilot/dependency/direct_install.py`;
- `src/upgradepilot/dependency/environment_selection.py`;
- CI composition modules only if a stronger proof contract requires them;
- GitHub acquisition only if an explicit fallback source is actually selected.

Do not modify stable action semantics, target repositories, or unrelated evidence producers under this plan without a separately surfaced design need.

## 9. Prohibited scope

This plan does not authorize:

- generic CI log ingestion by default;
- reconstruction of target package state in UpgradePilot's own runtime;
- deriving wheel/sdist identity or target wheel tags unless separately required;
- claiming package-state persistence beyond the evidence boundary;
- broad package-manager support beyond currently admitted pip/uv pressure;
- changing maintainer-action meanings;
- adding agentic orchestration;
- automatic target mutation or execution;
- implementing every AUDIT-008 finding as a queue.

## 10. Completion condition

This plan is complete when either:

1. UpgradePilot has one proven, bounded runtime dependency-state proof path for the selected normal command family, with explicit close defeaters and correct integration; optional fallback evidence exists only where justified; **or**
2. investigation/build evidence proves that the stronger state proposition is not worth implementing under current action reachability, and the responsibility is closed with a precise proof boundary.

Completion does not require artifact provenance, universal environment coverage, behavioral compatibility, or non-abstention action permission unless a later selected responsibility independently requires them.

**Procedural provenance:** `UP-SKILL:upgradepilot-planning-design`; `UP-SKILL:upgradepilot-learning-by-doing`.
