# Proposal feasibility review — dated evidence and reasoning

**Recorded:** 2026-09-06; review began in the 2026-09-05 conversation.

**Session status:** CLOSED at the bounded assessment boundary.

**Responsibility:** Source-grounded feasibility and priority assessment of the broader proposal.

**Inspected HEAD:** `0137837ac1fbfcfb6d86678ebe706284bdf4468a`.

**Related artifact:** [End-to-End Product and Engineering Proposal](../proposals/2026-09-05_UPGRADEPILOT_END_TO_END_PRODUCT_AND_ENGINEERING_PROPOSAL.md), section 19.

## Starting question and boundary

Ali requested that preliminary feature/tool priorities be checked against actual implementation, environment, and data. The earlier proposal contained case-informed possibilities, not measured feasibility. Balanced AI, backend, and applied ML remains the requested learning emphasis.

The review inspected product source and focused tests, the experiment boundary, package configuration, environment reference, and local corpus inventory. It did not implement features, install packages, invoke a model, acquire live target evidence, execute third-party code, train, publish, or select a replacement implementation route. `MEMORY.md` was consulted for coordination; its R4-B continuation was not changed by this proposal work.

## Source observations that changed the assessment

- `cli.py` accepts repository and PR number, calls the typed application flow, prints evidence, and maps acquisition/input failures to exit codes. It does not expose a final five-action recommendation, durable report export, or a web interface in that flow.
- `investigation.py` integrates exact dependency identity, exact-head CI workflow evidence and consumption, upstream evidence, and conditional Python-support investigation. This provides a useful producer-to-presentation seam.
- `dependency/pyproject.py` already handles one exact optional-extra version-pin change. It expressly rejects broader specifier changes. This is a partial foundation for S011-like context, not general S010 range-broadening support.
- `impact/artifact_serviceability.py` and `target/artifact_environment.py` contain bounded wheel/environment behavior with tests. The inspected normal `investigation.py` does not import/call these capabilities. Internal capability and end-to-end delivery must be assessed separately.
- `impact/python_support.py::select_python_support_drop_investigation` selects one exact target declaration acquisition under defined missing-evidence conditions. It is not a broad check or remedy generator.
- `experiments/b2_x1_evidence_gap_transition.py` preserves bounded state/transition/replay semantics. Experiment semantic replay is not durable product job recovery.
- `experiments/langgraph/evidence_gap_workflow.py::build_evidence_gap_langgraph` builds plan/authorize/investigate/conclude nodes and calls `compile()` without a checkpointer. The graph is an experiment; checkpoint/recovery functionality is not established by this source.

## Local verification

Commands ran through WSL Ubuntu-24.04 using `/home/motafeq/projects/UpgradePilot/.venv/bin/python`, with the repository as Python working directory. On continuation, native execution used an explicit repository working directory because the app-provided cwd was invalid. Git HEAD and the existing proposal-only diff were rechecked and unchanged.

Observed interpreter: Python 3.12.3. Product import resolved to `/home/motafeq/projects/UpgradePilot/src/upgradepilot/__init__.py`.

Observed installed metadata:

| Distribution | Result |
|---|---|
| requests | 2.34.2 |
| packaging | 26.2 |
| PyYAML | 6.0.3 |
| langgraph | not installed in the checked environment |
| hypothesis | not installed in the checked environment |
| opentelemetry-api | not installed in the checked environment |
| libcst | not installed in the checked environment |
| temporalio | not installed in the checked environment |

`pyproject.toml` declares `langgraph==1.2.11` in the experiment dependency group. Missing installation is an executable-proof prerequisite, not a framework rejection. No LangGraph test pass is claimed here.

Point-in-time capacity observations: 20 logical CPUs visible to Python and approximately 729.0 GiB free on the repository filesystem. These are not workload benchmarks or host-wide guarantees. `ENVIRONMENT.md` records an 8 GiB GPU and local inference topology; this review did not refresh GPU availability, measure model latency, or prove concurrent serving capacity.

### Focused product verification

Seven existing deterministic test files were loaded with `unittest.TestLoader().discover('tests', pattern=...)` into one suite:

```text
test_cli.py
test_investigation.py
test_pyproject_optional_extra_change.py
test_r6_project_environment_workflow_integration.py
test_artifact_serviceability.py
test_target_artifact_environment.py
test_python_support_impact.py
```

Observed: **62 tests passed; 0 failures, 0 errors, 0 skips**. Runner reported 0.029 seconds; fixture-test duration is not product performance evidence.

### Focused experiment verification

Three existing files were loaded similarly from `experiments/tests`:

```text
test_b2_x1_evidence_gap_transition.py
test_b2_x1_evidence_gap_planner.py
test_b2_x1_evidence_gap_admission.py
```

Observed: **30 tests passed; 0 failures, 0 errors, 0 skips**. Runner reported 0.003 seconds. These are deterministic experiment checks, not live model or external-acquisition proof.

To reproduce either selection, run from the repository root with the project interpreter, construct a `unittest.TestSuite`, add each matching `TestLoader().discover` result, run `TextTestRunner`, and exit nonzero unless `wasSuccessful()` is true. No new test files were added.

### Corpus inspection

The inventory found 12 `S*/README.md` scenario directories and 120 JSON artifacts under `product-simulation/scenarios`. Artifact count is not independent-example count. `experiments/step6_support_drop_semantic_corpus.json` contains 15 cases and identifies itself as a frozen support-drop semantic oracle. Its cases concern extraction/grounding, including paraphrase and negative/ambiguous controls, not a reviewed set of competing investigations with outcome/cost labels.

The review therefore did not establish a ready training/evaluation dataset for a learned investigation ranker. It also did not establish the absence of every possible relevant record elsewhere. S006's documented prior-oracle exposure and the use of S010–S012 in design prevent treating them as unseen final tests.

## Assessment and stop

The evidence supports prioritizing a bounded evidence/coverage report using existing typed results, then narrow environment/coverage integration. General action synthesis, remediation, report persistence/recovery, and learned ranking require materially different prerequisites. The proposal records those distinctions and a conditional priority comparison.

No product code, tests, dependency configuration, accepted semantics, or live continuation changed. Remaining uncertainties include actual maintainer value, end-to-end latency/cost, training-label feasibility, and broader release-level implementation effort. Those require discriminating investigations; document checks and selected passing tests do not answer them.

## Follow-on report design and publication preparation — 2026-09-06

Ali authorized continuing the bounded report design and committing/pushing this conversation's repository changes. The proposal's section 20 maps report statements to actual producers, chooses an evidence-only CLI-first scope, and identifies information not supplied by the application result. Product implementation remains outside this completed design slice.

Further source inspection sharpened two points: CI `supported_not_correlated` cannot be rendered as runtime dependency exercise, and a retained Python-support investigation selection can describe already-completed work. Also, exceptions handled at the CLI boundary do not supply a completed application result for an evidence report.

Publication preflight fetched `origin/main`, finding unrelated governance work from `0137837` through `8081708`. A safe fast-forward preserved the three local proposal/record changes. The incoming AGENTS/Operating Guide changes concerned supervision routing and were reviewed; product source/tests did not change. The earlier test results remain dated proof at their recorded revision, not claimed as a new run.

Publication scope is exactly the consolidated proposal, its Mature System Horizon navigation link, and this evidence record. No product code, dependencies, accepted specifications, or live position were changed by this work. Final commit/push outcome is reported in the conversation after remote verification rather than predicting a commit hash here.

## Framework-independent acceptance refinement — 2026-09-06

Ali reported that the separate LangGraph workstream had advanced to full S001 testing and authorized proceeding with the independent report design. At `e3416c4`, repository records document native 7/7 and controlled comparison 4/4 proof before the executable naming migration, with post-rename validation/S001 still pending in the saved live record. This supersedes the earlier environment snapshot for feasibility discussion without rewriting its historical measurement.

Sections 20.7–20.9 specify the logical report contract, executable and formative usability acceptance criteria, and an evidence-driven reconciliation checkpoint. They do not require the report to consume graph state or the experiment-owned semantic comparison projection. Product source was unchanged relative to the earlier report-design inspection.

Publication refresh fast-forwarded `e3416c4` to `25d9183` without overlapping these edits. The updated repository evidence records Ali's 58/58 post-rename WSL PASS and a committed S001 smoke harness with diagnostic refinements. The proposal checkpoint now reflects that closed naming proof gate while preserving the unverified S001 outcome. No experiment was rerun or supervised, and no completion claim was inferred from Ali's report of ongoing testing. The untracked `.zsh_history` was left untouched and excluded from publication. Continuing commit/push authorization applies only to this work's proposal and dated evidence edits.

Provenance: `UP-SKILL:upgradepilot-repository-audit`; `UP-SKILL:upgradepilot-planning-design`; `UP-SKILL:upgradepilot-working-memory`.

## S001 checkpoint and first report scope — 2026-09-06

Continued after `e49bf5f`; fetched and fast-forwarded to `a9dca93`. The separately owned real S001 proof is now recorded PASS in [the executable-proof record](2026-09-06_1752_real-s001-langgraph-executable-proof.md). Inspected the smoke success conditions and timing boundary against that record: product target/final equality and expected node path are checked; 6.726 seconds is graph-stream time, not full product latency. No real experiment was rerun. Exact executed checkout revision/raw diagnostic retention remains a reproducibility limit of the inspected record.

Proposal sections 20.9–20.10 now apply the checkpoint and select the first candidate implementation scope: existing CLI presentation of grounded source text, applicability/investigation lifecycle and available workflow identifiers. Source trace: `investigation.py` returns those facts; `cli.py` omits or compresses them; `tests/test_cli.py` patches the investigator rather than exercising normal provider composition. The candidate calls for a pure renderer and a controlled normal-composition check, with no new dependency or report schema.

Reconciled foundation Phase 6/7 and vertical-slice output ownership: report presentation can be independent, while artifact-serviceability integration precedes heterogeneous synthesis design. Kept live `MEMORY.md` and the separate framework value/cost workstream unchanged. No Build was performed in this proposal continuation. Publication is restricted to this record and the consolidated proposal; unrelated `.zsh_history` remains untouched.

Validation: source/evidence reconciliation plus Markdown/local-link, whitespace and governance checks; no product behavior changed and no new runtime test result is claimed.
