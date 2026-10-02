# G2 — Real-derived controlled same-workflow job-composition variant (design only)

**Date:** 2026-09-22  
**Form:** Real-derived *controlled* variant; the combined workflow, altered runner declarations, and resulting expected outcomes are **not** facts about public Aruba CI. No code/test/run was executed here.  
**Original host:** [Aruba Device Tracker #83](https://github.com/Jam3s97/Aruba_Device_Tracker/pull/83), exact head `b9630fc176fa7ae5321fab8844ee383587854fed`, changed `requirements.txt` ruff `0.16.5 → 0.16.8`.  
**Related evidence:** [G1 screening](2026-09-22_G1_COMMAND_RUNTIME_REAL_CASE_SCREENING.md), [G2 first screening](2026-09-22_G2_MULTI_JOB_TARGET_FIRST_SCREENING.md), [G2 bounded non-consumer control](2026-09-22_G2_NONCONSUMER_CONTROL_AND_STOP.md).

## 1. Named gap and admission limits

Existing F4 controlled tests prove job-key composition in artificial workflow containers. Real Aruba #83 proves direct changed-source `-r/--requirement` installs in **separate** one-job workflow files, whereas the public aiohttp PR has same-workflow multi-job contexts but an upstream `-c` source-selection gap. No newly screened untouched host was verified to satisfy all gates for a clean exact-source same-workflow positive F4 replay.

**Question:** With *one* workflow containing two explicit static jobs that both directly consume the exact changed requirements source, plus one unrelated job, does the product retain both consuming job identities and each selected job's *own* declared Target context, without borrowing the unrelated job's context or treating runtime matrix rows as static jobs?

The variant is appropriate to isolate the composition mechanism, not to prove the prevalence of the structure in public Dependabot CI or claim public F4 acceptance.

## 2. Frozen real inputs and controlled changes

**Keep frozen:** PR identity, changed source `requirements.txt`, changed package/version transition, and real commands from the two original Aruba workflows:

- original `lint.yml`, static key `ruff`: `python3 -m pip install -r requirements.txt`;
- original `test.yml`, static key `test`: `python3 -m pip install --requirement requirements.txt`, after a pip self-upgrade, followed by a distinct test-requirements install;
- original `validate.yml` has action-based `hassfest` and `hacs` jobs with no visible direct install from the changed requirements source.

**Clearly synthetic intervention:** combine `ruff`, `test`, and one non-consuming validation key (for example `hassfest`) into a *single controlled workflow*. To discriminate Target environment binding, set `ruff` to Windows/Python 3.12 and retain `test` on Ubuntu/Python 3.14; the Windows/Python 3.12 declaration is **invented for the controlled contrast**, not observed Aruba CI. Preserve the key names and changed-source commands and avoid any implicit claims about successful execution on the invented environment.

Minimal controlled workflow *shape* (for investigation fixture design only; not claimed to be a faithful runnable copy):

```yaml
jobs:
  ruff:
    runs-on: windows-latest # SYNTHETIC contrasted declaration
    steps:
      - uses: actions/checkout@v7.0.1
      - uses: actions/setup-python@v7
        with:
          python-version: "3.12" # SYNTHETIC contrasted declaration
      - run: python3 -m pip install -r requirements.txt
  test:
    runs-on: ubuntu-latest # from real test.yml
    steps:
      - uses: actions/checkout@v7.0.1
      - uses: actions/setup-python@v7
        with:
          python-version: "3.14"
      - run: |
          python3 -m pip install --upgrade pip
          python3 -m pip install --requirement requirements.txt
          python3 -m pip install --requirement requirements-test.txt
  hassfest:
    runs-on: ubuntu-latest
    steps:
      - uses: home-assistant/actions/hassfest@a7c616ce81ccda50150bf1595786c71b1883fabb
```

The YAML omits top-level triggers, permissions and full external-action provenance intentionally: it is a controlled static-interpretation fixture sketch, not a command to run CI or a claim of a real artifact. A future executable fixture must define all required surrounding metadata and safety boundaries separately.

## 3. Controlled checks / expected observations

1. **Positive exact-source consumption:** the admitted direct-requirements parser should recognize the same changed `requirements.txt` path in `ruff` (`-r`) and `test` (`--requirement`) separately, retaining `job_key=ruff` and `job_key=test` and the exact synthetic workflow path/revision. The non-consuming `hassfest` action must not acquire source consumption from workflow co-membership or success.
2. **Target composition:** given the exact two supported consumption records, F4 should produce two separate *declared* Target contexts (Windows/Python 3.12 for `ruff`; Ubuntu/Python 3.14 for `test`). Do not collapse by source/workflow alone. No result may silently substitute `hassfest` or use the `test` declarations for `ruff`.
3. **Negative identity mutation:** change a supported consumption record's `job_key` to a nonexistent value while retaining workflow/source/revision; expect an explicit missing-job problem rather than name-based fallback. Change its revision or workflow path; expect cross-identity rejection rather than evidence transfer.
4. **Runtime proof boundary:** do not infer exact actual package version, wheel tags, executed commands, or test/behavioral compatibility from the synthetic declarations. The real Aruba job logs belong to the *original separate workflows* and must not be transplanted as evidence that the recombined/altered fixture ran.
5. **Optional matrix stress (separate controlled variant only):** introduce two Python rows under one static consuming key; expect one static job identity unless an additional explicit runtime-row binding exists. Do not represent two matrix instances as two static consuming jobs.

## 4. Stop and transfer rule

This design is complete when it identifies the changed-versus-frozen inputs, discriminating expected states, exact identity keys, and proof limits. **No new product test/source change or external target run is authorized by this document.** If the main F4 owner wants a deterministic replay, hand off this controlled input set and the already established F4 tests, reconcile against the then-current main, and implement only through that owner's explicitly selected bounded operation.

For Product Simulation, stop the narrow same-workflow `-r` hunt at the documented bounded result; instead prioritize the distinct real-world `aiohttp -c` source-consumption question and G3 package-manager/runtime-state evidence, unless a new untouched clean candidate with genuinely better discriminating evidence appears. This variant remains discovery/evaluation design rather than an accepted product contract.