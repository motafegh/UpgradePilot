# Fresh current CI diagnostic cohort acquisition and qualification

Session status: CLOSED after post-closure audit and corrective replay. Primary operation: Build/Implement with Learning-by-Doing.

Accepted scope: Ali's 2026-10-20 instruction to create a new exposed real-world diagnostic cohort under `product-simulation/` using current public GitHub Actions evidence, with immutable offline evidence bundles, qualification/rejection records, a readiness matrix, fresh-process replay proof, and no product-source repair unless separately authorized.

## Closure supersession note

The first same-day closure at `ad3e1bd96e2b5984dea3c96256f40f939676585f` is historically valid as an intermediate state but is **superseded** by this record. A post-closure audit reopened the evidence gate and found additional source-byte fidelity defects plus one inaccurate expected-refusal description. Those defects were repaired additively, replay was rerun, and the cycle is closed again only on the corrected state.

## Cycle and orientation map

A0 — DONE: reconciled live `main` at task start `c381c02a9eb786ed50e972c8eb62764be5bb5dcf`; inspected root governance, local `product-simulation/` governance/specification, current `MEMORY.md`, retained-native-CI/baseline comparison, GitHub Actions acquisition owner, dependency-state owner and YAML↔runtime correlation owner. Predecessor learner-ownership debt remains separate.

A1 — DONE: the motivating historical glyphsLib evidence contained exact-attempt jobs with empty captured `steps`; that limitation did not establish a producer defect and was not repaired by assumption.

A2 — DONE: Ali fixed the diagnostic question, evidence classes, qualification rules, exposure status, proof obligations, stop boundary, non-goals and final deliverables. This cycle owned acquisition/retention/qualification/diagnostic preparation only, not product acceptance/generalization or product-source repair.

B — DONE: established the exposed `FCI` series under `product-simulation/fresh-current-ci-diagnostic-2026-10-20/`; screened current public dependency-update PRs; admitted three distinct cases and recorded rejected/not-deepened candidates. No `src/upgradepilot/` file changed.

Verification gate — DONE after two rounds of repair:

1. Initial Git-object verification found manually reconstructed PR-diff whitespace defects in FCI001 and FCI003. The flawed raw objects remain immutable/non-authoritative; additive `pr.provider-exact.diff` objects are authoritative. FCI002's original diff was exact.
2. Post-closure audit found that the first FCI001 workflow copy and FCI002 workflow/base/head requirements copies had lost their final newline during connector-to-text persistence. Those files were internally self-consistent, so a verifier comparing only retained bytes to retained hashes could pass without proving upstream fidelity. Additive provider-exact source overlays were created whose Git blob identities are **identical to the frozen upstream source blobs**. Earlier copies remain immutable/non-authoritative.

The network-free verifier now checks recorded upstream Git object identity as well as retained byte size/SHA-256/Git identity. Corrected fresh-process replay of a materialized offline mirror passes for all three cases without target-repository API values.

D — DONE: current GitHub exposes non-empty job step summaries in all three selected PR heads for executed jobs, so historical glyphsLib empty-step history is not a universal current-provider condition. One case is a realistic supported correlation shape; two are intentional unresolved controls. No evidence currently establishes an UpgradePilot product defect.

E — DONE / CLOSED on corrected evidence. The three-case cohort is sufficient; discovery stopped rather than padding count. Recommended next responsibility, only if separately selected, is a retained-evidence current-CI diagnostic: FCI001 positive path → FCI002 missing-name/mixed-step refusal → FCI003 missing-name refusal.

C — COMPLETE for this cycle: decisions, failures, repairs, proof/non-proof and handoff are preserved here and in cohort artifacts.

## Current producer-contract facts confirmed during audit

GitHub Actions acquisition:

- exact-head `pull_request` runs are acquired for the frozen PR head;
- jobs are acquired from the exact run-attempt endpoint;
- run ID/head identity is verified;
- `steps=None` is preserved separately from an empty tuple/array.

YAML ↔ runtime correlation:

- revision identity must match;
- reusable-workflow jobs and strategy/matrix jobs are unsupported;
- ordinary jobs require a unique literal explicit static job display name;
- static/runtime job display names must form an exact bijection;
- runtime step identities/order must be available and unambiguous.

Runtime dependency state remains narrower than generic successful CI: the current supported family is direct-requirements/pip and even a positive witness is bounded to exact successful command completion, not fresh-install causality, artifact identity, later use or behavioral compatibility.

## Cohort result

### FCI001 — `openai/openai-agents-python#5404`

- transition: `mcp 2.0.0 -> 2.3.0`
- base: `64cd5dfc5a1579870dcbed0ea42b27aa84033fee`
- head: `8549af29bb5d4b061e3beb41b487ceb669cfb5c0`
- selected run: `39372679381`, attempt `1`, `Release Readiness`
- runtime steps: one non-empty job step array
- current correlation shape: eligible
- runtime dependency state: unsupported/not established; uv/lockfile shape and both user steps skipped
- classification: `qualified_for_current_ci_diagnostic`
- authoritative workflow source: `raw/workflow.provider-exact.yml`, Git blob `fb2110166d4df410cea5f181d0e75a55b92824a4`, identical to frozen upstream source

### FCI002 — `executablebooks/mdformat-footnote#50`

- transition: `tox>=4.61.1 -> tox>=4.64.4`
- base: `9a174e4cba089f4b117134a220164bdc20f070fe`
- head: `c4b631da85386c18ad691c9d3d6af35b72e3a9ab`
- selected run: `36798375619`, attempt `1`, `CI`
- runtime steps: executed jobs non-empty; two skipped publish jobs preserve `steps: null` as `field_absent_or_unavailable`
- current correlation shape: unsupported; **first expected reason is `static_job_name_missing` on `pre-commit`**; later matrix remains independently unsupported as `static_job_strategy_unsupported`
- dependency exercise: not established; observed workflow does not consume `requirements.txt` or invoke tox
- classification: `qualified_as_unresolved_control`
- authoritative workflow source: provider-exact blob `9643a4ea975e7182c548e4bc8e94accb93aa0056`
- authoritative base/head requirements sources: blobs `994653111f7abfd53b8e4e0f932a1696dcf87189` / `b6afd3da9c4d83bbf7c82b2c1e9c7d900c03b790`

### FCI003 — `PasarGuard/panel#1044`

- transition: `fastapi>=0.143.2 -> >=0.143.3`
- base: `67096b59e80769e84b7a29012da62b8a78a7e273`
- head: `ffecd3d66aa307590dd41d7cc755dde7a5b5644b`
- selected run: `39445488948`, attempt `1`, `Test Database Migrations`
- runtime steps: all five job arrays non-empty
- current correlation shape: intentionally unsupported because static jobs lack explicit literal display names
- provider wrinkle: selected run payload exposed an empty `pull_requests` array; exact-head discovery remains frozen by PR head and the missing array relation is not fabricated
- dependency exercise: not established by make-target step summaries
- classification: `qualified_as_unresolved_control`
- retained workflow and base/head `pyproject.toml` files already match frozen upstream Git blobs exactly; manifests now bind those upstream identities explicitly

## Corrected replay result

Separate-process offline replay result after all repairs:

- FCI001: 5 declared artifacts, 1 job, step state `non_empty_array`;
- FCI002: 9 declared artifacts, 13 jobs, step states `field_absent_or_unavailable` + `non_empty_array`;
- FCI003: 7 declared artifacts, 5 jobs, step state `non_empty_array`;
- overall status: `pass`;
- target-repository network/API required during replay: `false`.

A literal fresh `git clone` inside the execution container was unavailable because that container could not resolve GitHub. Replay therefore used a materialized mirror of retained bytes. Durable repository persistence and upstream source fidelity were checked separately via Git object identities. This limitation remains explicit rather than being disguised as a literal-clone proof.

## Capture and retention boundary

The GitHub connector exposes structured provider fields used by the current diagnostic path plus repository source/diff text, but it does not export original HTTP bodies/headers byte-for-byte. Provider API material is therefore a structured provider capture, not an HTTP-wire archive.

Provider/source evidence is kept separate from review/interpretation. Raw published objects are never silently repaired in place; exact replacements are additive and manifests identify which objects are authoritative.

Logs/workflow artifacts were not retained because they are not material to the current declared correlation responsibilities and would add size/security/privacy surface. A later diagnostic needing them must capture that evidence explicitly.

## Repair history

Initial case publication:

- `ecd11a4a424bd1b6cecc8a8c83e9e17370ab88db` — FCI001
- `5e08c7a2623c774121e50deb273a21b20d8570d8` — FCI002
- `862731e031d2f2ca00337bb6668cc8226f07a712` — FCI003

Initial exact diff repairs:

- `73ee8fc7c6182de82ae3b3fcf6549820edb7c62b` — exact FCI001 provider diff
- `e4739be2160dbea87e15aa3c7eef2c62f92516f0` — exact FCI003 provider diff

Post-closure audit and exact-source repair started at:

- `c665fc889759f5b17b08b5fa85702b61e518d05a` — provider-exact FCI001/FCI002 source overlays + correction record
- later manifest/verifier/report commits bind those overlays, correct FCI002 semantics and rerun replay

The repair history is evidence for the process: self-consistent retention hashes are not sufficient to prove byte identity with a frozen upstream source. Source fidelity must be independently bound to the upstream object identity when that proof is available.

## Canonical cohort records

- `product-simulation/fresh-current-ci-diagnostic-2026-10-20/README.md`
- `product-simulation/fresh-current-ci-diagnostic-2026-10-20/CANDIDATE_SELECTION.md`
- `product-simulation/fresh-current-ci-diagnostic-2026-10-20/READINESS_MATRIX.md`
- `product-simulation/fresh-current-ci-diagnostic-2026-10-20/RETENTION_CORRECTIONS.md`
- `product-simulation/fresh-current-ci-diagnostic-2026-10-20/REPLAY_VERIFICATION.md`
- `product-simulation/fresh-current-ci-diagnostic-2026-10-20/FINAL_REPORT.md`
- `product-simulation/fresh-current-ci-diagnostic-2026-10-20/verify_bundle.py`

## Proof / non-proof

Proven:

- exact frozen identities for three recent public Python dependency-update PRs;
- current exact-head workflow/run-attempt/job evidence retained with provenance;
- executed jobs can currently expose non-empty runtime steps;
- provider-unavailable/null skipped-job steps can coexist with rich executed-job steps;
- authoritative workflow/dependency source bytes are bound to frozen upstream Git object identities;
- one current correlation shape satisfies the current owner's static/runtime preconditions;
- FCI002 and FCI003 preserve legitimate unsupported boundaries without guessing;
- retained inputs can be integrity/identity checked and replayed without current target API values.

Not proven:

- product reliability, product acceptance or generalization;
- that successful jobs installed/exercised the updated dependency;
- that FCI001 correlation actually succeeds until the product owner is executed against retained inputs;
- that FCI002/FCI003 return their expected unresolved results until the product owner is executed;
- any `src/upgradepilot/` defect;
- HTTP-wire-perfect GitHub API archival.

UP-SKILL:upgradepilot-build-implement
UP-SKILL:upgradepilot-learning-by-doing
UP-SKILL:upgradepilot-working-memory
