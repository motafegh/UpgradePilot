# G2 — Multi-job consumption to exact Target context: first real screening

**Date:** 2026-09-22  
**Kind:** Non-controlling Product Simulation research; **not** a validated F4 end-to-end replay or an approved numbered scenario.  
**Question:** When a real dependency-update PR has several CI jobs/environments, what evidence identifies the correct static consuming job(s), and what can Target infer from each selected job without borrowing context from a different job or matrix row?

## Candidate A — aio-libs/aiohttp#13785: useful multi-job pressure, upstream source gap

**Exact PR:** [aiohttp#13785](https://github.com/aio-libs/aiohttp/pull/13785), Dependabot `multidict 6.8.0 → 6.9.0`; head `406547435e65e067dac070336799af4691716956`. Changed sources include `requirements/base.txt`, `requirements/runtime-deps.txt`, and `requirements/test.txt`; their exact diff includes the same `multidict` pin transition. Preserve source-by-source relations; the ten changed files do not imply that every job consumes every source.

[Exact-head `.github/workflows/ci-cd.yml`](https://github.com/aio-libs/aiohttp/blob/406547435e65e067dac070336799af4691716956/.github/workflows/ci-cd.yml) has, among others:

| Static job key | Declared environment and direct workflow commands | Changed-source relation and limit |
| --- | --- | --- |
| `lint-from-sdist` (`Lint / sdist`) | `ubuntu-latest`; setup Python `3.11`; `python -m pip install "${SDIST_PATH}" -c requirements/runtime-deps.txt`; later `pip install -r requirements/base.in -c requirements/base.txt` | Both `runtime-deps.txt` and `base.txt` were changed; they enter as **constraints**, not `-r` requirement paths. The later command is first sequential in its own step but does not newly install multidict in that step. |
| `test` (`Test`, matrix-expanded) | `runs-on: ${{ matrix.os }}-latest`; `setup-uv` Python `${{ matrix.pyver }}`; `uv pip install ... -r requirements/${{ env.DEPENDENCY_GROUP }}.in -c requirements/${{ env.DEPENDENCY_GROUP }}.txt`; `uv pip install -e .`; tests | `requirements/test.txt` / `test-ft.txt` are changed sources selected through `-c` under the matrix. Static job key is **`test`**, while actual executions have different OS/Python/no-extensions rows. Do not infer a single target Python/OS from the static job key alone. |
| Other jobs (`build-pure-python-dists`, docs/lint, wheel builds, etc.) | Different setup/install paths and environments | Their presence/success is not itself evidence that they consume the particular selected changed source or provide the selected job's Target environment. |

**Runtime reference:** [CI run `35717414006`](https://github.com/aio-libs/aiohttp/actions/runs/35717414006), associated with this PR head, finished successfully. The `Lint / sdist` job `106712962153` completed successfully; its sdist install logged `multidict-6.9.0`. The run also includes separate successful `Test` executions with names such as `Test (3.11, ubuntu, false)` and `Test (3.14, ubuntu, false)`; matrix display names are runtime instances, **not** different static job keys. Do not equate run-associated head SHA with executed bare-head checkout without verifying the checkout ref.

**Discriminating finding:** A real PR simultaneously changes several exact constraint-source paths and runs distinct static jobs/matrix environments. An F4-like handoff must select job identity from *proven changed-source consumption*, preserve independent consuming job keys, and leave matrix-dependent Target properties unresolved unless a particular row/compatible witness is bound. This case currently **cannot validate F4's positive direct-requirements path in isolation**: current `direct_install.py` identifies exact `-r/--requirement` source paths, whereas these changed `*.txt` sources enter the inspected relevant commands as `-c/--constraint`. The source-selection gap precedes job-to-Target composition; do not hide it by picking `lint-from-sdist` or `test` by their names.

**Limits:** This screening has not executed UpgradePilot end-to-end on #13785 and does not claim its actual reported Target result. Other independent consumption mechanisms, nested requirement resolution, build isolation, or matrix row mapping must be separately proved before stronger conclusions.

## Candidate B — Aruba#83: cross-workflow control, not same-workflow multi-job proof

[Aruba#83](https://github.com/Jam3s97/Aruba_Device_Tracker/pull/83), head `b9630fc176fa7ae5321fab8844ee383587854fed`, changes `requirements.txt` ruff `0.16.5 → 0.16.8`.

- [Exact-head `lint.yml`](https://github.com/Jam3s97/Aruba_Device_Tracker/blob/b9630fc176fa7ae5321fab8844ee383587854fed/.github/workflows/lint.yml): static job `ruff`, direct `-r requirements.txt`; [Lint run `35615432558`](https://github.com/Jam3s97/Aruba_Device_Tracker/actions/runs/35615432558) succeeds.
- [Exact-head `test.yml`](https://github.com/Jam3s97/Aruba_Device_Tracker/blob/b9630fc176fa7ae5321fab8844ee383587854fed/.github/workflows/test.yml): static job `test`, direct `--requirement requirements.txt`, followed by test-requirements install; [Test run `35615432407`](https://github.com/Jam3s97/Aruba_Device_Tracker/actions/runs/35615432407) succeeds.
- [Exact-head `validate.yml`](https://github.com/Jam3s97/Aruba_Device_Tracker/blob/b9630fc176fa7ae5321fab8844ee383587854fed/.github/workflows/validate.yml): jobs `hassfest`, `hacs` invoke separate actions and do **not** visibly declare direct installation from the changed `requirements.txt`; [Validate run `35615432444`](https://github.com/Jam3s97/Aruba_Device_Tracker/actions/runs/35615432444) succeeds.

**Discrimination:** A successful unrelated validation workflow must not supply changed-source consumption or Target evidence for `ruff`/`test`. This is **cross-workflow identity** pressure and a straightforward direct-source control, not proof of the same-workflow multi-job `job_key` composition that F4 implemented. Its Test CI checkout is a synthetic PR merge ref; that distinction was preserved in the G1 screening.

## G2 current conclusion and next gate

1. Do **not** promote either host as a clean public end-to-end demonstration that the current F4 implementation correctly selects one of several **same-workflow** supported direct-requirements consuming jobs. aiohttp is confounded by the real upstream `-c` gap; Aruba's directly consuming jobs are in separate workflow files.
2. The exact `-c` gap remains a useful main-workstream handoff/candidate; do not implement from this research branch.
3. Continue **bounded search for one clean PR with one changed directly installed `-r/--requirement` source and one workflow containing at least two jobs with differing declared Target contexts, where at least one job consumes the exact changed source**. Prefer one consuming and one non-consuming job, or two distinct consumers, with exact head workflow and inspectable runtime job data. Stop after one complete discriminating case plus an ordinary control; do not accumulate lookalikes.
4. Keep three identities distinct: *static job key*, *runtime matrix job instance*, *exact changed dependency source*. If matrix-derived Python/OS is unresolved at the static job layer, do not silently choose a runtime row as the universal Target environment.

No product source, tests, governing plans, root/main memory, target repository, or external CI run was modified.