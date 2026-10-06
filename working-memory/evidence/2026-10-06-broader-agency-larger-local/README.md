# Larger local models — capacity diagnosis and reviewed evidence

Recorded 2026-10-06. Local experiment evidence; no product or independent semantic acceptance.

The initial larger-model profile exposed an inadequate ordinary/stage output allowance: Gemma 4 12B passed two fresh interface canaries, then three real-case assignments each stopped at 1024 generated tokens. Each failing response recorded 1021 reasoning tokens and no usable continuation. This is observed output truncation, rather than a completed model-quality comparison.

Ali explicitly stopped the run during the fourth Gemma assignment and requested raising the limits. The worker saved its private receipts and unloaded its own instance. Qwen3.6 35B-A3B was not started. [The interrupted-profile evidence](interrupted-profile.json) preserves three saved trial records, receipt-derived partial facts for the fourth, the interruption and four unstarted Qwen assignments separately.

| Original assignment | Outcome | Calls | Final report |
|---|---|---:|---|
| Gemma HTTPX fixed | Output truncated during stage correction | 4 | None |
| Gemma HTTPX agent | Output truncated during investigation | 5 | None |
| Gemma pytest agent | Output truncated during investigation | 4 | None |
| Gemma pytest fixed | User interrupted first stage after two tool responses | 3 attempts / 2 responses | None |
| Qwen, both cases and arms | Not started | 0 | None |

The complete original receipts total **26 attempts / 25 accounted responses**, including ten successful canary calls. Known totals are **68276 input / 14420 generated / 12594 reasoning tokens**. These are lower bounds because the interrupted outstanding request has unreported usage. Receipt reconciliation includes that attempt rather than recording it as zero cost. The three saved cases and two canaries have complete accounting and measured context fit; reconstructed fourth-assignment facts are not a fabricated formal trial trace.

Useful source clues survive: the HTTPX agent found the actual FastAPI TestClient import/call and unpinned FastAPI declaration; the pytest agent found pytest configuration, the input constraint, direct plugins and a regression command. Neither finished the required investigation. Separately, HTTPX F's pre-truncation stage candidate claimed no major breaking changes and stable standard use after two searches without reading the relevant upstream material; its bare-path citations failed the contract. The later truncation does not erase those unsupported claims, and the claims do not establish that a sufficiently provisioned run would also fail.

Original executable freeze `53f34aae` and exact reused corpus hashes match the preserved published source. Model identity, loaded 16K context, ratio 0.55, private-artifact hashes and individual reviews are in the JSON. [Earlier three-small-model evidence](../2026-10-06-broader-agency-repair/README.md) remains unchanged and is a distinct configuration.

[Protocol section 17.1](../../../plans/BROADER_LLM_AGENCY_COMPARATIVE_EVALUATION_PROTOCOL.md) records Ali's selected separate capacity profile: 8192 ordinary/stage and report output, 131072 total generated/524288 input per trial, 32768 loaded context. The existing TrialLimits object propagates through pilot, canaries, both arms and HTTP output reserves, retaining finalization, correction, accounting, source, tool and validation controls. The source/profile implementation passes 53 focused checks, Ruff/format and CLI-help verification. These controlled checks do not substitute for actual model proof.

Raw source, prompts, candidates, provider reasoning and partial receipts stay private under ignored .tmp. This evidence establishes the interruption and capacity problem, not reliable advice, a model winner, greater product authority or an agency/parameter-count effect. The sole live continuation owner remains [MEMORY.md](../../../MEMORY.md).


## Saved-packet capacity check

Implementation `cdbf9c70` was committed/pushed before inference. An owned Gemma load confirms 32768 context with the same GPU ratio 0.55, strict VRAM cap, KV offload and flash attention. One explicitly selected replay preserves the first truncated HTTPX F stage-correction request's system/user/history/schema. Only the output reserve, owned instance binding and load/context profile differ; no source hint, reference answer or retry is added.

The response completes in **139.498 seconds**, using **4307 input / 1136 generated / 805 reasoning tokens**, with **finish_reason=stop**, no truncation and wire max_tokens=8192. Existing citation syntax and JSON shape pass. The generated response actually exceeds the old 1024 ceiling. This establishes the selected larger allowance, measured context fit, actual accounting and a completed capacity contrast; it is not an independent case outcome or repaired historical trial. The owned contrast instance was unloaded.

Source meaning still fails: `target-base:requirements.txt:L2` is the httpx pin, not proof of standard request usage. `httpx-new:pyproject.toml:L62` is a Changelog URL, not proof that the target's request patterns remain compatible. Relevant upstream removals and the indirect framework path were not read in this retained packet. [Reviewed contrast evidence](capacity-contrast.json) separates actual capacity repair from these unsupported claims. The sole live continuation owner remains MEMORY.md; the new profile is a distinct deployment experiment rather than a causal size/agency comparison.

## First corrected-profile case checkpoint

The two fresh Gemma canaries pass in eight calls. The first corrected-profile HTTPX fixed assignment completes in 1840.258 seconds with **15 calls / 13343 generated tokens including 9859 reasoning**, and no truncated response. All 23 completed canary/case receipts reconcile exactly: 126090 input / 18144 generated / 13607 reasoning tokens. This supports end-to-end capacity/accounting proof; it does not close the remaining seven assignments.

The first case still fails the report reference contract; none of its five stage artifacts is complete. Manual source review also rejects its low-risk/proceed recommendation and stable-primary-tests claim: delivered evidence contains the target pin, scoped literal-search absence and upstream/CI inventories, rather than the relevant release changes, indirect TestClient path or CI capture bodies. The generic indirect-framework condition is a useful lead. [Reviewed first-case checkpoint](capacity-profile-checkpoint.json) preserves these distinct findings.

## User-requested pause checkpoint

Ali requested stopping for a later overnight run. The worker exits at the interrupted Gemma HTTPX agent request, saves final receipts and unloads its own model; anonymous inventory reports no loaded instances. The completed HTTPX fixed result stays unchanged. The interrupted agent attempt has ten calls/nine known responses and nine delivered operations, including actual upstream changelog pages and target consumer-search clues, with no formal final result. One outstanding request has unknown usage. Six other assignments were not started.

[Pause evidence](overnight-pause.json) reconciles the 23 completed checkpoint receipts plus this ten-attempt partial: **33 attempts / 32 accounted responses**, known lower-bound totals **171103 input / 24433 generated / 19575 reasoning tokens**. A later continuation must preserve the interruption and launch a separately labelled fresh attempt for the interrupted case, retain the completed case, and run the six unstarted assignments. The original driver must not be rerun unchanged over existing folders. Scheduling/current continuation remains owned by MEMORY.md.

## Immediate continuation selection, 2026-10-07

Ali requested restarting. [The continuation selection](continuation-selection-2026-10-07.json) retains the completed fixed case and interrupted costs, starts the interrupted Gemma agent case with fresh state, and selects the six unstarted assignments. All seven model/companion/package hashes match prior identities, and the unchanged code/corpus and original evidence hashes pass preflight. Qualification reuse is conditional on identical reloaded Gemma configuration; Qwen receives its fresh checks. This records selection/preflight, not finished outcomes; MEMORY.md owns actual launch state.
