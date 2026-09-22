# G1 — Real CI command occurrence / runtime-strengthening screening

**Date:** 2026-09-22  
**Kind:** Non-controlling Product Simulation research evidence; not an accepted numbered scenario, source-code change, or product policy.  
**Question:** For a proposed Python dependency update, when does target-owned CI step success establish successful execution of the *exact changed-dependency-consuming command occurrence*, rather than merely success of its containing step?

## Evidence and admission rules

- Preserve the distinction between **proposal-relevant dependency-source selection**, **static command location/control flow**, **owning step success**, **observed command result in retained logs**, and **post-install package state**. They answer different questions.
- A run associated with a PR head may check out the synthetic PR **merge ref**, not the head tree. Record this where visible; do not silently say the executed checkout equals the bare PR head.
- Do not invent a successful source/command relation simply because a dependency is installed elsewhere in the job.
- This is a deliberately selected small set, not a prevalence sample.

## C1 — Sole command, exact changed requirements source (ordinary positive control)

**PR:** [Jam3s97/Aruba_Device_Tracker#83](https://github.com/Jam3s97/Aruba_Device_Tracker/pull/83); Dependabot ruff `0.16.5 → 0.16.8`; PR head `b9630fc176fa7ae5321fab8844ee383587854fed`.

**Exact changed source:** `requirements.txt`, changed `ruff==0.16.5` to `ruff==0.16.8`. **Exact-head workflow definition:** [`.github/workflows/lint.yml`](https://github.com/Jam3s97/Aruba_Device_Tracker/blob/b9630fc176fa7ae5321fab8844ee383587854fed/.github/workflows/lint.yml); job key `ruff`, step `Install requirements`, sole `run: python3 -m pip install -r requirements.txt`; following steps invoke `python3 -m ruff check .` and `python3 -m ruff format . --check`.

**Runtime reference:** [Lint run `35615432558`](https://github.com/Jam3s97/Aruba_Device_Tracker/actions/runs/35615432558), associated with the PR head; job `106384769468` succeeded and the install log reported `ruff-0.16.8`. The step/command is an ordinary sole top-level invocation under the visible Linux GitHub shell wrapper. Verify checkout SHA separately if using this as exact executed-tree truth: GitHub PR workflows commonly check out a synthetic merge ref.

**Proves:** The exact changed file is directly named in an ordinary sole install declaration; a successful exact owning step is a realistic positive runtime-strengthening shape. Installer output separately identifies `ruff-0.16.8` for the install operation.

**Does not prove:** Later independent package-state inspection, exercised ruff behavior specific to the changed version, compatibility/safety, or that the run's checked-out commit equals the bare PR head.

## C2 — Later sequential command: actual install visible in logs, not justified by step success alone

**Same PR/head:** Aruba #83 / `b9630fc176fa7ae5321fab8844ee383587854fed`. **Exact-head workflow definition:** [`.github/workflows/test.yml`](https://github.com/Jam3s97/Aruba_Device_Tracker/blob/b9630fc176fa7ae5321fab8844ee383587854fed/.github/workflows/test.yml); job key `test`, step `Install dependencies`:

```bash
python3 -m pip install --upgrade pip
python3 -m pip install --requirement requirements.txt
python3 -m pip install --requirement requirements-test.txt
```

**Runtime reference:** [Test run `35615432407`](https://github.com/Jam3s97/Aruba_Device_Tracker/actions/runs/35615432407), job `106384768608`, step 4 success. The retained job log displays GitHub `shell: /usr/bin/bash -e {0}`, then `Collecting ruff==0.16.8 (from -r requirements.txt (line 4))`, `Successfully installed ... ruff-0.16.8 ...`, the later requirements-test install, and 29 passing tests. The checkout log explicitly identifies the synthetic merge commit `f077fda4d5bde656d293d7ec4f09bbf67a780e57`, incorporating PR head `b9630fc...`, **not** a bare-head checkout.

**Proves:** This second ordinary top-level sequential command *did run* in this observed merge-ref execution; its own installer output shows the changed ruff version. The owning step succeeded.

**Does not prove:** The current **bounded step-success-only rule** should strengthen an arbitrary later sequential occurrence. Without command-level output or additional established ordering/control-flow proof, a successful containing step is a weaker input than this retained log. Do not transport the log's stronger observation into a generic step-only rule. The tests are not ruff-version-specific exercise evidence.

**Discrimination against C1:** C1 is the sole-command admitted shape. C2 is an observed successful command beyond the currently admitted sole/first bound; it pressures *proof availability versus policy conservatism*, not a claim that the existing policy is incorrect.

## C3 — First sequential command, but exact changed source enters as pip constraint

**PR:** [aio-libs/aiohttp#13785](https://github.com/aio-libs/aiohttp/pull/13785); Dependabot multidict `6.8.0 → 6.9.0`; PR head `406547435e65e067dac070336799af4691716956`. Changed `requirements/base.txt` contains `multidict==6.8.0 → multidict==6.9.0`. [Exact-head `requirements/base.in`](https://github.com/aio-libs/aiohttp/blob/406547435e65e067dac070336799af4691716956/requirements/base.in) includes `-r runtime-deps.in`; that [runtime source](https://github.com/aio-libs/aiohttp/blob/406547435e65e067dac070336799af4691716956/requirements/runtime-deps.in) declares `multidict >=4.5, <7.0`.

**Exact-head workflow definition:** [`.github/workflows/ci-cd.yml`](https://github.com/aio-libs/aiohttp/blob/406547435e65e067dac070336799af4691716956/.github/workflows/ci-cd.yml), static job key `lint-from-sdist`, displayed job name `Lint / sdist`, step `Run slotscheck`:

```bash
# Some extra requirements are needed to ensure all modules
# can be scanned by slotscheck.
pip install -r requirements/base.in -c requirements/base.txt
slotscheck -v -m aiohttp
```

**Runtime reference:** [CI run `35717414006`](https://github.com/aio-libs/aiohttp/actions/runs/35717414006), job `106712962153`, successful `Run slotscheck` step; the job log shows the command and `slotscheck` returning `All OK!`. In an earlier step of that job, `python -m pip install "${SDIST_PATH}" -c requirements/runtime-deps.txt` reports `Successfully installed ... multidict-6.9.0 ...`; the later slotscheck step's pip invocation installed `Brotli-1.2.0 gunicorn-26.2.0`, not a newly installed multidict. Do not attribute that earlier installed multidict to the later slotscheck command.

**Two separate findings:**

1. The `Run slotscheck` install is the first ordinary top-level Bash command after comments, followed by another command. Structurally it is a realistic first-sequential positive case *if* the exact static dependency consumption had been established.
2. The changed source is `requirements/base.txt`, named by `-c/--constraint`, not `-r/--requirement`. Current `src/upgradepilot/dependency/direct_install.py::_requirement_paths_from_atoms` only matches `-r/--requirement` for direct-requirements source identity. This is a concrete **source-selection gap upstream of runtime strengthening** for the selected `base.txt` relationship. Other changed files/commands in the same PR require independent source-by-source accounting; do not claim CI globally fails or that the product necessarily produces a particular final output without an end-to-end run.

**Does not prove:** Generic `pip -c` support would be safe for every constraint-file shape, exact installed-state persistence after later mutations, independent package-state inspection, target-wheel compatibility, or that this run's executed checkout is bare PR head.

## Screened out — Black #5421 is not a relevant changed-dependency consumption example

[psf/black#5421](https://github.com/psf/black/pull/5421), head `532e33f6695c8f44cedc423bcf60f8635526f3ef`, changes `pyproject.toml` optional `width-table` extra from `wcwidth==0.2.14` to `wcwidth==0.8.4`. Its [exact-head `diff_shades.yml`](https://github.com/psf/black/blob/532e33f6695c8f44cedc423bcf60f8635526f3ef/.github/workflows/diff_shades.yml) has a later `python -m pip install .` command after a matrix-derived setup command. The [run `35568964172`](https://github.com/psf/black/actions/runs/35568964172) and job `106236415404` succeeded and reported a Black install, but that default-project install does **not** select the `width-table` extra. Its runtime checkout also involves PR merge/rebase operations. Therefore it cannot establish changed-`wcwidth` consumption or a G1 changed-dependency runtime outcome. Retain only as a **rejected screening control** showing why command execution alone is insufficient without proposal-relevant source selection.

## G1 synthesis / candidate status

- A small discriminating set is available: **sole direct-source positive** (Aruba lint), **later sequential command with stronger separate log evidence** (Aruba test), and **first sequential shape blocked by a predecessor `-c` source-selection gap** (aiohttp).
- The public cases do **not** justify replacing the current bounded step-level strengthening rule with a broad assumption that all internal commands succeeded.
- The first proposed substantial Product Simulation case is **aiohttp#13785, in candidate status only**. Admission question: is the exact changed constraints file a first-class dependency-source consumption input, and can the command/runtime owner receive a faithfully selected source occurrence without overclaiming what `-c` does? Existing historical Product Simulation corpus and current controlled tests do not establish this exact real source-binding pathway.
- Framework gates: **Q/G/C** above; **E** exact PR/source/workflow/job/run and log available; **S** read-only public target; **N** a negative result preserves conservative unresolved instead of inventing consumption; **L** no universal `-c` semantics, runtime state, or safety claim; **T** stop when a bounded direct constraints relationship and its counterexamples/limits can be distinguished; **F** untouched real public case.
- No numbered scenario, source-code change, test, governing decision, PR comment, target rerun, or merge was made. The main owner should decide whether to take up the `-c` source-consumption gap and what evidence its proof contract requires.
