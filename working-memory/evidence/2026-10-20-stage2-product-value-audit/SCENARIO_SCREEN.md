# Stage-2 S001–S016 product-value readiness screen

**Date:** 2026-10-20  
**Purpose:** lightweight audit screening only; not the execution/results packet of `PRODUCT_VALUE_AND_TRANSPARENT_BASELINE_FEASIBILITY_INVESTIGATION_PLAN.md`  
**Branch basis:** `audit/project-wide-system-audit-2026-10-20`, reconciled against `main@a1c291c6cf9238493eeb666b184192ed178b90f1`

## Proof-class legend

- **historical simulation** — retained manual/AI-assisted simulation evidence; useful development pressure, not current automated product output;
- **baseline artifact** — retained `BASELINE_RESULT.json` under the frozen simulation baseline; does not make the paired historical full investigation a current-product run;
- **current-source projection** — retained reasoning about what current source would do; not a fresh end-to-end run;
- **component candidate** — retained facts appear suitable for a named deterministic product/component responsibility if a current producer can consume them;
- **fresh product** — would require the current normal product path and all of its actual dependencies; not executed by this audit.

All S001–S016 are exposed development material. None is converted into a protected qualification set by this screen.

## Lightweight matrix

| Case | Product-boundary status | Distinct responsibility / value pressure | Retained comparison evidence | Plausible evaluation mode now | Deep-readiness value |
| --- | --- | --- | --- | --- | --- |
| **S001** Pydantic / Soup Sieve | eligible Python public dependency-update development case | upstream Python-support signal + target applicability + CI authority | explicit baseline artifact plus rich historical simulation/raw evidence | historical baseline/full-investigation review; retained-input/component readiness must be checked before any current-product replay claim | **high** — supported positive/target-applicability contrast candidate |
| **S002** Dashboard / HTTPX | eligible Python development case | source/API relation, consumer forwarding, CI relevance | explicit baseline artifact plus rich historical simulation; also heavily exposed in later Investigator work | historical comparison; supplied-evidence semantic development case; current product reachability requires explicit mode | **high** — strong false-reassurance/source-relation pressure but heavily exposed |
| **S003** event-handler-loader / TypeScript | **outside supported Python product boundary** | install/resolution failure attribution and negative-evidence discipline | explicit baseline artifact and historical simulation | historical pressure only; must not count as Python product coverage | **exclude from supported product cohort**; retain as failure-design evidence |
| **S004** glyphsLib / pytest patch | eligible Python development case | baseline-sufficient / stopping control | explicit baseline artifact; historical simulation; heavily exposed in Investigator work | historical baseline control; current-product mode must be separately established | **high as no-added-value control**, not because it is difficult |
| **S005** modelarrayio / pytest | eligible Python development case | coarse favorable baseline versus target/coverage uncertainty | explicit baseline artifact plus historical simulation | historical baseline/full-investigation comparison; retained-input current mode needs checking | **high** — useful miscalibration/coverage contrast |
| **S006** qldebugger / Pydantic validators | eligible Python development pressure | targeted-check design and visible coverage gap | explicit baseline artifact plus targeted-check/oracle/stopping records | manual/historical evaluation; known oracle/exposure limitations prevent treating it as independent qualification | **conditional high** — useful targeted-check pressure if exposure is explicit |
| **S007** BiomedParse / torch CUDA family | eligible Python real Dependabot case | coordinated package-family reasoning, contradiction handling, static evidence stopping/pruning | no retained `BASELINE_RESULT.json`; retained proposition/family/stopping artifacts | historical simulation / deterministic component candidate | **high for stopping and family-state responsibility**, not turnkey baseline benchmark |
| **S008** CARLA / OpenCV | eligible Python real Dependabot case | interpreter support vs wheel availability vs source fallback; proposition-specific CI coverage | no baseline artifact; exact target/upstream/artifact/stopping records | historical simulation / artifact-serviceability component candidate | **high if current artifact producer/consumer is reachable** |
| **S009** CGM / pandas | eligible Python real Dependabot case | repository-purpose/provenance consistency independent of runtime compatibility | no baseline artifact; repository-context/reproducibility/stopping records | historical/manual evidence only unless a current repository-context producer is identified | **medium/high for product thesis breadth**, but current automation reachability is uncertain |
| **S010** podcast-script / NumPy | eligible Python real proposal pressure | multiple independently grounded mechanisms and discovery breadth | no baseline artifact; retained mechanism/discovery/runtime records | historical simulation / possible multi-mechanism component pressure | **high for coverage/discovery responsibility**, not turnkey product comparison |
| **S011** dictare / mlx optional extra | eligible Python real proposal pressure | optional environment formation before CI coverage; package-family context | no baseline artifact; optional-extra/CI-coverage/discovery records | historical simulation / deterministic environment+CI component candidate | **high** — materially distinct CI/environment applicability pressure |
| **S012** freqtrade / scikit-learn | eligible Python real public dependency proposal | persisted-artifact producer-version/history applicability | no baseline artifact; exact persisted-path/upstream-contract/state/stopping records | historical simulation; current product support for artifact-history provenance not established | **high for future history-sensitive applicability**, likely not first runnable comparator |
| **S013** langchain / anyio | eligible Python development case | prior environment formation versus later no-sync exercise; stale/prior state | no baseline artifact; exact command/runtime-state artifacts | historical simulation / deterministic runtime-state component pressure | **high for state-proof correctness**, not current baseline benchmark by default |
| **S014** production-ready-cicd / pip | eligible Python development case | `already satisfied` state truth versus install provenance/fresh installation | no baseline artifact; exact state/proof-boundary records | historical simulation / deterministic command-completion component pressure | **high for proof-boundary regression**, not current baseline benchmark by default |
| **S015** charset-normalizer / pytest marker | eligible Python real Dependabot case | marker-scoped requirement applicability across runtime rows | no baseline artifact; explicit `CURRENT_PRODUCT_PROJECTION.json` says current exact-pin extractor rejects marker-bearing line | **current-source projection + deterministic component pressure**; not fresh product output | **very high** for identifying a concrete current unsupported boundary and future applicability invariant |
| **S016** thumbor / uv scope | eligible Python real Dependabot case | lock membership versus selected-root/environment reachability | no baseline artifact; explicit `CURRENT_PRODUCT_PROJECTION_AND_STOP.json` aligns current decomposition with real positive/negative scopes | **current-source projection + deterministic component pressure**; not fresh product output | **very high** as a current-design transfer/control case |

## Screen-level conclusions

1. The original fixed S001–S006 universe is **not a defensible sole universe for the current product-value decision**. It omits later, materially distinct responsibilities including package-family stopping, artifact path changes, repository provenance, multi-mechanism discovery, optional-environment CI coverage, persisted-state provenance, prior-state formation, command provenance, marker applicability and selected uv scope.
2. Expanding the first pass to S001–S016 does **not** make all sixteen benchmark cases. Only S001–S006 visibly retain the original explicit baseline artifact, and S003 is outside the supported Python product boundary.
3. S007–S014 are primarily historical/manual pressure evidence at this screen. Their usefulness is to select responsibilities and identify candidate deterministic owners unless/until exact comparator inputs and current product routes are established.
4. S015/S016 are unusually valuable to current engineering because they preserve explicit current-source projections; nevertheless those projections are not fresh product executions.
5. A deep cohort must therefore be selected by **distinct responsibility + evidence mode + current producer/consumer reachability**, not scenario chronology or a fixed count.
6. The deep cohort should normally include at least one baseline-sufficient/no-added-value control, one misleading coarse-baseline/false-reassurance case, one explicit unknown/stopping case, and one current deterministic transfer/projection case when their exact retained inputs make the comparison mode honest.
7. Missing baseline/current-product artifacts are readiness findings. This audit does not authorize reconstructing them, reacquiring evidence, or running the product merely to fill the matrix.

## Candidate deep-cohort pressure — not a selection

The screen suggests these *roles* are likely discriminating if exact readiness survives deep inspection:

- **S004** — baseline-sufficient/no-added-value control;
- **S002 or S005** — false reassurance / coarse-baseline miscalibration;
- **S001** — supported upstream/target-applicability information;
- **S015 or S016** — current deterministic source/environment/scope transfer boundary;
- optionally **S008/S011/S012** if a reachable current owner can consume the retained facts without manual oracle injection.

This is not a frozen cohort. The feasibility investigation must still select the smallest cohort whose exact evidence mode can answer the product-value decision.

## Stop

Screening stops here. Deep analysis of every scenario would defeat the purpose of the lightweight first pass and is not justified by this audit.