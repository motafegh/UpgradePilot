# G2 — Non-consumer CI control and bounded search outcome

**Date:** 2026-09-22  
**Mode:** Non-controlling Product Simulation research; not an approved numbered scenario or validated F4 end-to-end replay.  
**Companion:** [G2 first screening](2026-09-22_G2_MULTI_JOB_TARGET_FIRST_SCREENING.md).  
**Question:** Does a multi-instance or multi-job successful/failed CI run identify the exact job that consumes the changed dependency source, or can the jobs be unrelated to the dependency proposal?

## C — open-webui/open-webui#26494: changed requirements file, but unrelated matrix jobs

- Real [Dependabot PR #26494](https://github.com/open-webui/open-webui/pull/26494), title `Update pytest requirement from ~=8.4.1 to ~=9.1.1 in /backend`; created 2026-07-01; closed without merge. Head `ed99df86c8cb69e5848592f0af0df2fb0d3d0103`; base `af1c0eee89810fa4c36e3eb7e4eba6de685bd7ca` at the PR metadata snapshot. PR changes exactly `backend/requirements.txt`, line `pytest~=8.4.1` to `pytest~=9.1.1`.
- [Exact-head workflow `.github/workflows/backend.yaml`](https://github.com/open-webui/open-webui/blob/ed99df86c8cb69e5848592f0af0df2fb0d3d0103/.github/workflows/backend.yaml) triggers on backend paths and has **one static job key** `format-check` with a Python-version matrix `['3.11', '3.12']`; declared runner is `ubuntu-latest` in both rows. The `Install formatter` step runs `pip install "ruff>=0.15.5"`, then formatting and Ruff logic checks. It does **not** run `pip install -r backend/requirements.txt`, select a pytest extra, or otherwise visibly consume the exact changed dependency source. The workflow's path filter is a trigger, **not** dependency-source consumption evidence.
- [Head-associated Python CI run `28488568057`](https://github.com/open-webui/open-webui/actions/runs/28488568057) completed failure: runtime `Ruff Format (3.11)` job `84440184038` and `Ruff Format (3.12)` job `84440184064` both had successful `Install formatter`, failed `Verify formatting`, and skipped `Detect logic errors`. Both are instances of static key `format-check`, **not two static jobs**. This inspection did not independently establish whether the run checked out the bare PR head versus a synthetic merge ref; do not transfer that assumption.

### Material distinction

```
changed backend/requirements.txt
+ path-filter-triggered Python CI
+ two runtime matrix job instances
+ formatter installation succeeded
+ formatting failed
!=
pytest 9.1.1 installed/consumed/failed as a dependency update
```

This is a **negative control**, not a positive F4 composition demonstration. Do not transfer failures or successful formatter installation to the updated pytest dependency. Do not treat two matrix executions as two static job keys or fabricate Target contexts that were never supported by exact source-consumption evidence.

## Bounded G2 screening disposition

| Host | What is real and supported | Why not the desired clean positive F4 case? |
| --- | --- | --- |
| [aiohttp#13785](https://github.com/aio-libs/aiohttp/pull/13785) | Several jobs, changing constraints sources, differing declared environments and matrix instances | Exact changed sources enter inspected relevant commands through `-c/--constraint`, upstream of current `-r` direct-source observer. |
| [Aruba#83](https://github.com/Jam3s97/Aruba_Device_Tracker/pull/83) | Exact changed requirements source directly installed by `-r`/`--requirement`; unrelated Validate workflow | Direct consumers are separate one-job workflow files; does not isolate same-workflow F4 handoff. |
| [Open WebUI#26494](https://github.com/open-webui/open-webui/pull/26494) | Exact changed requirements source, two runtime Python-version rows and exact-head workflow/run metadata | Only `format-check` static job; formatter install does not consume the changed source. Closed-without-merge PR and failing checks are not evidence of pytest regression. |
| [MontePy#986](https://github.com/idaholab/MontePy/pull/986) — previously retained for G3 | Several static CI jobs and explicit post-install `pip freeze` state witness | Changes `pyproject.toml` build-system requirements and installs through `pip install .[build]`, not the selected changed `-r` requirements-file shape. It may inform broader project-source consumption, but not the requested clean direct-requirements handoff. |

**Search conclusion at this bounded stop:** No untouched case meeting *all* G2 criteria—same workflow with contrasting **static** jobs, exact changed `-r/--requirement` source, and inspectable relevant runtime jobs—was verified in this screening. This is a property of the **purposefully screened convenience set**, not a claim about how often such CI exists. No new numbered scenario or real-world positive F4 claim is admitted merely to close the search.

**Next useful alternative:** construct a **real-derived controlled variant** from the already frozen Aruba#83 direct-source workflow material, placing contrasting source-consuming/non-consuming jobs into a single controlled workflow. Clearly label the changed workflow as *synthetic/real-derived*, preserve the exact changed `requirements.txt` proposal and expected static job keys, and evaluate the current F4 producer/composition boundary with controlled inputs. This can test our implementation without pretending the modified workflow or its CI run happened in the public target. Approval to implement/run a variant must follow the relevant operation and evidence boundary; Product Simulation may prepare the design without modifying product code or external CI.

**Other high-information route:** The real `aiohttp -c` source-selection gap is a more immediate externally observed product-breadth pressure than collecting further variants of this narrow F4 positive. Hand off to the main owner for explicit design consideration, not automatic scope expansion.

No target repo, CI, main product source/tests/plans/specifications, root `MEMORY.md`, or main working memory was modified.