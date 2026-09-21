# F6 post-install package-state evidence feasibility — 2026-09-21

**Session status:** INVESTIGATION COMPLETE — read-only Audit + Planning/Design + Learning-by-Doing; joint learning/decision is next. No F6 product implementation is selected or authorized.
**Prior:** F5 target wheel-tag evidence-source feasibility CLOSED; F4 CI-consuming job → Target composition CLOSED.
**Controlling route:** `plans/END_TO_END_PRODUCT_FLOW_LEARNING_AND_EVIDENCE_TO_ACTION_EXECUTION_PLAN.md`; parent synthesis plan and accepted action semantics remain unchanged.
**Audit input:** `audits/2026-09-19_AUDIT-008_current-system-evidence-to-action-readiness.md::AUDIT-008-F6`.

## 1. Exact F6 question

AUDIT-008-F6 correctly records a deliberate current proof boundary:

```text
exact supported static dependency-consumption occurrence
+ exact correlated completed-successful runtime step
→ supported_runtime_correlated

but NOT:
→ exact installed/resolved dependency version
→ wheel/sdist/artifact identity
→ exact target-supported tags
→ behavioral compatibility
```

Current normal dependency-change admission already establishes an **exact proposed version** for supported sources. Conventional requirements/constraints require an exact `package==version` transition; the current pyproject optional-extra rule likewise requires one non-wildcard `==version` transition; uv-lock evidence is exact-version source evidence. Therefore F6 is not currently a generic “which version did this range resolve?” feature.

The decision-critical F6 proposition investigated here is narrower:

> **Was the exact proposed dependency version actually present in the exact relevant CI environment after the dependency-consuming install/sync activity?**

Keep this distinct from how the package was installed, whether a relevant behavior ran, whether another environment works, and what maintainer action is justified.

## 2. Current producer → interpretation boundary

### 2.1 What the product already knows

- `dependency/change.py` owns one exact old → proposed dependency transition across admitted sources.
- `dependency/requirements.py` accepts the current conventional requirements path only for one removed and one added exact pin.
- `dependency/pyproject.py` accepts the current optional-extra path only when both sides use one exact non-wildcard `==version`.
- `ci/consumption.py` / `dependency/direct_install.py` preserve the exact workflow/source/job/step relation for supported dependency consumption.
- `ci/runtime_strengthening.py` can strengthen only admitted structural command shapes, principally a sole ordinary top-level command or the first ordinary top-level sequential Bash/sh command under the admitted execution profiles.
- `ci/dependency_exercise.py` deliberately names the stronger result `supported_runtime_correlated` while explicitly refusing to claim exact installed version, wheel selection, or compatibility.
- `github/actions.py` currently acquires exact-head workflow runs and jobs from the captured run attempt, plus factual step status/conclusion. It does **not** acquire job logs or package-state output.

### 2.2 Why successful correlated consumption is not post-install state

The existing runtime bridge is execution evidence for an exact admitted occurrence, not a durable state witness.

Three concrete defeaters establish that distinction:

1. **pip dry-run**
   ```text
   python -m pip install --dry-run -r requirements.txt
   ```
   Pip documents `--dry-run` as resolving/printing without actually installing. The current direct-install observer recognizes the pip-install + requirements-source relation but does not interpret `--dry-run` as a material negative option. Under an otherwise eligible runtime shape, a successful step can therefore coexist with no resulting installation.

2. **uv non-installing/excluding modes**
   Current project-environment selection admits uv project-environment commands but its material-negative option set does not cover all current uv installation-affecting modes. Official uv semantics include:
   - `uv sync --dry-run`: resolve/report without modifying the project environment;
   - `uv run --no-sync`: avoid syncing the environment;
   - `--no-install-package <name>`: explicitly exclude a package from installation.
   Thus successful runtime-correlated project-environment activity cannot be silently upgraded to “changed dependency is present.”

3. **later state mutation**
   Even a genuine successful install can be followed by:
   ```text
   pip install -r requirements.txt
   pip uninstall -y changed-package
   ```
   in the same successful job/step sequence. Runtime success of the install occurrence proves the install command's bounded execution result, not persistence of package state at a later observation point.

These are not reasons to weaken the accepted static/runtime correlation contract. They prove why F6 is a separate proposition. They also expose a nearby source-traced design question: whether some current “consumption” command profiles (especially dry-run/no-sync/exclusion modes) should later be restricted or more precisely classified. That question is preserved, not silently repaired here.

Official references consulted:
- pip install / dry-run / report: https://pip.pypa.io/en/latest/cli/pip_install/
- uv command reference: https://docs.astral.sh/uv/reference/cli/

## 3. Real public evidence — normal UpgradePilot-shaped positive case

### 3.1 Exact target

**Repository:** `Jam3s97/Aruba_Device_Tracker`  
**PR:** https://github.com/Jam3s97/Aruba_Device_Tracker/pull/83  
**Dependabot package ecosystem:** pip  
**Change:** `requirements.txt`  
**Exact transition:** `ruff==0.16.5 → ruff==0.16.8`  
**Exact PR head:** `b9630fc176fa7ae5321fab8844ee383587854fed`

The patch is exactly within UpgradePilot's current conventional-requirements admission rule.

### 3.2 Exact-head CI

Public exact-head pull-request runs include:

- `Validate` run `35615432444` — success;
- `Test` run `35615432407` — success;
- `Lint` run `35615432558` — success.

The relevant Lint job is job `106384769468`, completed successfully.

Frozen head workflow `.github/workflows/lint.yml` contains:

```yaml
- name: Install requirements
  run: python3 -m pip install -r requirements.txt

- name: Lint
  run: python3 -m ruff check .

- name: Format
  run: python3 -m ruff format . --check
```

The target-owned public job log records, in order:

```text
Collecting ruff==0.16.8 (from -r requirements.txt ...)
Downloading ruff-0.16.8-...manylinux...whl
Installing collected packages: ... ruff ...
Successfully installed ... ruff-0.16.8 ...
Run python3 -m ruff check .
Run python3 -m ruff format . --check
```

This establishes **feasibility** of a stronger target-owned observation in one real case that the current dependency parser can admit.

At careful proof strength:

- the human pip output provides strong evidence that pip reported installing `ruff-0.16.8` in that exact job;
- the later exact steps successfully invoke ruff in the same job;
- this is stronger than current UpgradePilot's run/job/step metadata alone;
- the raw pip text is still a human-oriented log surface rather than a versioned UpgradePilot evidence contract;
- this one case does not establish a general parser or action permission.

## 4. Real public evidence — historical availability limitation

UpgradePilot's existing GitHub Actions tests are anchored to real Dependabot PR:

**Repository:** `googlefonts/glyphsLib`  
**PR:** https://github.com/googlefonts/glyphsLib/pull/1145  
**Change:** `requirements-dev.txt`, `pytest==9.0.2 → pytest==9.0.3`  
**Exact head:** `f3cda8a94600e58d27f1bc17c99b7693718b6350`

Exact-head workflow runs and jobs remain publicly queryable and show successful install/test steps. However, attempts to download job logs for retained job IDs now return HTTP **410 Gone**.

GitHub's documentation states that workflow logs are retained for a bounded period; the documented default is 90 days, with public repositories configurable from 1 to 90 days.

Therefore:

```text
exact workflow/job metadata retained
!= historical package-state/log witness retained
```

A future F6 log producer MUST represent unavailable/expired logs as normal missing evidence, never as package absence, install failure, or negative evidence.

Official reference:
https://docs.github.com/en/rest/actions/workflow-jobs#download-job-logs-for-a-workflow-run
https://docs.github.com/en/organizations/managing-organization-settings/configuring-the-retention-period-for-github-actions-artifacts-and-logs-in-your-organization

## 5. Real public evidence — explicit package-state output exists in normal Python CI

A separate public Python repository demonstrates that target-owned CI can explicitly emit installed-state inventories:

**Repository:** `idaholab/MontePy`

Its public `.github/dependabot.yml` configures Dependabot for the `pip` ecosystem. Current CI `.github/workflows/main.yml` includes `pip freeze` after package installation in build/test jobs.

This proves that explicit package-state output is not a synthetic mechanism. However, the visible recent Python dependency example inspected during this investigation (PR #941, Sphinx range widening) is not itself within UpgradePilot's current exact-pin dependency-change admission rule. Preserve the distinction:

```text
real target-owned package-state source exists
!= current UpgradePilot normal input model reaches every such PR
```

This case is evidence-source feasibility, not end-to-end F6 acceptance.

## 6. Candidate evidence sources compared

| Source | What it can establish | Strengths | Material limits | Investigation disposition |
| --- | --- | --- | --- | --- |
| Exact pin/lock + successful current CI correlation only | command/source relation and bounded execution success | already implemented; durable metadata | dry-run/no-sync/exclusions/later mutation defeat post-state; no direct installed-version observation | **insufficient alone for F6 post-state** |
| Human installer log, e.g. `Successfully installed ...` | installer-reported package/version at that point in job | already exists in many ordinary jobs; real exact positive Aruba case | human-oriented text; quiet/format variation; manager-specific; retention; point-in-time; step-output correlation needed | **feasible, but not preferred as strongest contract** |
| `pip inspect` JSON | installed distributions + environment | stable versioned JSON format (v1); explicit environment-state report | only if target already emits/preserves it; still needs exact job/interpreter/order binding | **strongest generic pip witness when present** |
| `python -c '...importlib.metadata.version(...)'` | installed version for one named distribution in current Python environment | stdlib; minimal; exact one-package discriminator | only if target already emits it; absence/exception/output parsing must be handled; interpreter identity matters | **strong precise one-package witness when present** |
| `pip list --format=json` | installed package/version inventory | structured JSON; common pip surface | target must emit; interpreter/path scope matters | **strong conditional witness** |
| `pip freeze` | installed distribution snapshot-like text | common; real MontePy workflow uses it | text format; not a lockfile or complete semantic environment description | **useful conditional witness** |
| `uv pip list --format json`, `uv pip freeze`, `uv pip show` | uv-selected environment installed-state information | explicit current uv inspection surfaces | environment-selection identity still required | **strong uv-side conditional witness** |
| pip `--report` / Installation Report | what pip installed or *would* install | stable JSON v1; includes package metadata and artifact download info | with `--dry-run` it describes would-install, not final state; target must emit/preserve; point-in-time | **useful installer observation, not automatically post-state** |
| Uploaded workflow artifact containing inventory | preserved target-owned structured/text state file | can be cleaner than whole-log parsing; exact run artifact | only if target creates/uploads it; artifact retention/acquisition/provenance | **strong conditional source if present** |
| Dependency file/lock only | declared/resolved source truth | durable/reproducible | static, not runtime state | **not F6 runtime evidence** |
| UpgradePilot's own recreated environment | proxy/reconstruction | executable by us in theory | not exact historical target authority; third-party execution boundary; can diverge | **not an exact-target F6 witness** |
| Maintainer-performable version query | can directly discriminate missing package-state fact | tiny check such as `importlib.metadata.version` | external target execution/action; only justified if proposition is decision-critical and no better product-owned observation exists | **possible future targeted-check route, not current producer** |

Official package-state references:
- pip inspect stable JSON: https://pip.pypa.io/en/latest/reference/inspect-report/
- pip list JSON: https://pip.pypa.io/en/latest/cli/pip_list/
- Python installed-distribution version: https://docs.python.org/3/library/importlib.metadata.html
- uv environment inspection: https://docs.astral.sh/uv/pip/inspection/
- pip installation report: https://pip.pypa.io/en/latest/reference/installation-report/

## 7. Provenance and temporal requirements for any future F6 evidence

A credible domain fact cannot be merely:

```text
package=ruff
version=0.16.8
```

At minimum it needs identity sufficient to bind the observation to the decision:

```text
target repository
+ exact PR head revision
+ exact workflow run
+ exact run attempt
+ exact job
+ package identity
+ observed version
+ observation source/method
+ observation position/time sufficient for the claim
+ explicit limitations/unavailable state
```

The exact run-attempt/job work already implemented by UpgradePilot is reusable provenance foundation.

### 7.1 Ordering matters

For a bounded **post-install presence** claim:

```text
supported consumption
→ package-state observation
```

must be ordered in the same relevant job/environment.

For a stronger future claim that a subsequent test/exercise used that version:

```text
supported consumption
→ package-state observation
→ relevant exercise
```

is necessary but may still be insufficient if intervening commands can mutate the environment. A general “no mutation occurred” proof is a materially harder responsibility and is **not** selected here.

### 7.2 Environment/interpreter identity matters

`python -m pip`, `pip`, uv-managed environments, user installs, `--target`, multiple Python interpreters, and virtual environments can refer to different package-state scopes. A package-state adapter must preserve the environment/interpreter relationship it actually observes; it must not synthesize sameness from a job name alone.

## 8. Relationship to F5 artifact-serviceability

F5 asked for exact supported wheel tags so UpgradePilot could determine whether old/proposed published wheel availability maps to the exact target environment.

F6 can answer a different and sometimes earlier-sufficient question:

> Did the exact proposed version actually become present in this exact CI environment?

If yes, then for that exact observed environment the narrow proposition “the proposed version cannot be installed/present here” is refuted, regardless of whether pip used a wheel or source distribution.

That does **not** make F5 globally obsolete. Wheel/sdist identity may still matter when the decision specifically concerns:
- loss of a prebuilt path;
- source-build fallback behavior;
- artifact mechanism;
- a different supported environment not represented by the successful CI observation.

Action-relative selection should therefore prefer the earliest sufficient proposition rather than collecting wheel details automatically.

## 9. Relationship to behavioral CI evidence

F6 version presence and existing direct-exercise evidence are different axes:

```text
exact proposed version present
!= affected behavior exercised
```

and:

```text
package invocation/test step succeeded
!= exact proposed version proven present
```

The Aruba case happens to provide both a pip install log naming `ruff-0.16.8` and later successful ruff invocations in one job. That illustrates how the axes can compose when provenance/order are strong enough. It does not create a generic rule that every test step used the observed version.

## 10. Action-relative value

F6 does not itself authorize a maintainer action.

What it can do:

- close or narrow the exact-environment installation-presence uncertainty;
- defeat a same-environment “proposed version did not/could not become present” premise;
- provide stronger version activation for later mechanism-specific reasoning;
- prune some artifact-serviceability uncertainty when exact installation presence is the earliest sufficient fact;
- improve interpretation of later exact exercise evidence when ordering/environment identity are also established;
- expose when a tiny package-state query would be a genuinely discriminating targeted check.

What it cannot do by itself:

- prove behavioral compatibility;
- prove all supported environments;
- prove production/deployment compatibility;
- prove wheel/sdist/source-build mechanism unless separately observed;
- justify merge, block, investigate, defer, or targeted checks without those actions' independent positive conditions.

## 11. Nearby correctness/design findings exposed by F6

These are **not silently selected as implementation work**:

1. Current direct pip consumption observation does not treat `--dry-run` as a material “no installation” modifier.
2. Current uv project-environment selection does not cover all current environment-suppression/exclusion options such as `--dry-run`, `--no-sync`, and `--no-install-package`.
3. The current label `supported_runtime_correlated` remains valid at its documented bounded execution strength, but consumers must not read it as resulting installed-state evidence.
4. If product semantics intend “dependency consumption” to imply stronger environment formation than declaration/execution of the source-consuming command, those command-option gaps should be reviewed at the earliest owning parser/selector rather than patched downstream in F6.
5. Generic job-log ingestion introduces a new untrusted-text acquisition surface, bounded-size/retention/error handling, and provenance requirements. SECURITY.md therefore applies if that route is selected.

## 12. Architecture alternatives preserved for joint decision

No alternative is selected yet.

### Alternative A — strengthen command semantics only; keep F6 absent

Reject/resolve dry-run/no-sync/exclusion shapes earlier and continue using current runtime correlation without claiming post-state.

**Gain:** smallest architecture; no logs.  
**Limit:** still no direct post-install version witness; later mutation and environment-scope ambiguity remain.

### Alternative B — bounded installer-log witness

Acquire exact job logs and recognize one tightly bounded installer-reported package/version observation, initially for an admitted pip shape.

**Gain:** demonstrated normal reachability by Aruba PR #83; no target workflow change.  
**Cost/risk:** human text parsing, bounded retention, log size/format, step attribution, package-manager-specific semantics.

### Alternative C — explicit package-state witness only

Admit explicit state queries such as `pip inspect`, `pip list --format=json`, `pip freeze`, `importlib.metadata.version`, or uv equivalents when target workflows already emit them.

**Gain:** strongest semantic fit; structured sources available.  
**Cost/risk:** lower coverage because many target workflows do not emit them; still usually requires log/artifact acquisition.

### Alternative D — source-neutral F6 evidence contract + staged adapters

Define the domain fact/provenance independently, then admit one or more evidence adapters only when each is proven:
1. explicit structured state output first when available;
2. possibly bounded installer-log evidence as a weaker source class;
3. preserve unavailable/unsupported distinctly.

**Gain:** avoids coupling domain meaning to pip text; allows future uv/other state sources without changing the core fact.  
**Cost:** larger design surface; still must choose a first adapter and prove value.

### Alternative E — no new producer; use a targeted check only when decision-critical

If exact package state is necessary for a specific decision and no admitted read-only witness exists, synthesize a small maintainer-performable check rather than building generic acquisition.

**Gain:** proportional, avoids broad log infrastructure.  
**Limit:** requires targeted-check positive permission and does not help when the fact could have been read automatically from existing public evidence.

## 13. Investigation conclusion

The F6 question survives full investigation:

- **necessity:** current runtime-correlated consumption is intentionally weaker than post-install package state, with concrete pip/uv/later-mutation defeaters;
- **feasibility:** a real, currently supported exact-pin Dependabot case (Aruba PR #83) exposes target-owned exact proposed-version evidence in public job logs and then directly exercises that package;
- **stronger source classes:** stable structured package-state mechanisms exist and real public Python CI can emit explicit inventory;
- **availability limit:** historical logs are not durable; glyphsLib #1145 demonstrates retained run/job metadata with expired logs;
- **architecture is not yet decided:** generic human-log parsing is feasible but not automatically the best baseline;
- **action impact is bounded:** F6 can close an exact-environment installation/version proposition but does not create a maintainer action by itself.

Therefore **F6 full investigation is complete, but F6 Build is NOT selected**.

The next responsibility is joint Learning-by-Doing review with Ali, at medium-sized chunks:
1. current CI proof vs package-state proof;
2. why F6 is genuinely useful and where it stops;
3. real Aruba positive case + historical retention case;
4. evidence-source alternatives and trade-offs;
5. jointly choose whether to build F6, tighten earlier command semantics first, prefer targeted checks, combine approaches, or leave the boundary unchanged.

## 14. Preservation / proof status

No UpgradePilot product source, tests, stable specifications, accepted plans, or target repositories were mutated by this investigation. Only this dated working-memory record and canonical live-memory handoff are eligible for update.

External target evidence was read-only. Public CI/log output is treated as evidence/data, not project authority.

**Procedures:** `UP-SKILL:upgradepilot-repository-audit`; `UP-SKILL:upgradepilot-planning-design`; `UP-SKILL:upgradepilot-learning-by-doing`; `UP-SKILL:upgradepilot-working-memory`; canonical A→B→C→D→E.
