# ADR-0014 milestone 5 — Qualified later-command execution

The prepared CI path assessed the exact Soup Sieve requirements command in all seven applicable MapProxy jobs. Run 43457921398, attempt 1, belongs to PR 1559 at head `ac01b8901935bfc16a0195277b4aec1c43275897`. The genuine retained attempt contains eight jobs and 79 reported steps. Every job associated to its own declared context. The controlled lifecycle contrasts below are separate observations derived from that frozen input.

| Context | Reported job ID | Requirements command basis | Command execution |
| --- | ---: | --- | --- |
| Python 3.12, Pillow 13.0.0 | 131996881880 | Second command in reported install step 6 | Supported |
| Python 3.13, Pillow 13.0.0 | 131996881564 | Second command in reported install step 6 | Supported |
| Python 3.14, Pillow 13.0.0 | 131996881411 | Second command in reported install step 6 | Supported |
| Python 3.15, Pillow 13.0.0 | 131996881633 | Second command in reported install step 6 | Supported |
| Coverage | 131996881258 | Second command in reported install step 6 | Supported |
| Doc | 131996881440 | No Soup Sieve requirements command | No candidate |
| Lint | 131996881382 | Sole command in reported install step 4 | Supported |
| Typechecking | 131996881059 | Sole command in reported install step 4 | Supported |

The five later assessments identify `pip install -r requirements-tests.txt` at source order 1, bytes `[14, 51)`. The four specialized test scripts have the same digest and offsets. Their job and script identities keep the results separate. The exact-head YAML and specialized script provenance are retained. The four test and coverage jobs separately report successful test steps. Specific Soup Sieve behavior remains unobserved. Every installed-package state remains unresolved with `manager_environment_needs_lower_source_evidence`.

## Declared shell method

The parser inspects the complete Bash/sh script. The later relation requires ordinary foreground root commands with bare literal executable names and supported literal arguments. Shell-control builtins, assignments, dynamic atoms, nesting, substitutions, operators, pipes, redirection and asynchronous syntax prevent the new relation. Existing sole and first relations retain their structural meaning. Their shared runtime profile now withholds a positive when a visible startup input can bypass execution.

| Declared profile | Selected wrapper |
| --- | --- |
| Non-Windows default | `bash -e {0}`, with `sh -e {0}` fallback |
| Explicit Bash | `bash --noprofile --norc -eo pipefail {0}` |
| Explicit sh and container default | `sh -e {0}` |

The startup check inspects the effective workflow/job/step declarations for BASH_ENV, ENV, SHELLOPTS, BASHOPTS, BASH_COMPAT, exported Bash functions and dynamic-loader overrides. Ambiguous declared values, potentially material container env or options, and visible references to GITHUB_ENV in earlier run steps can block stronger support. A GITHUB_ENV reference alone does not establish a write. The guard conservatively leaves its effect unresolved. Runner/image internals, inherited environment, action effects and the actual shell executable remain outside this observation. All seven genuine candidates have the non-Windows default declaration with no visible blocker. The execution owner then requires the matching step’s unmasked completed-success outcome.

The 32 self-authored local shell controls exercised all three launch templates. They measured return status and target markers. Early `exit 0`, successful `exec`, startup exit, an ERR trap before the target and `SHELLOPTS=noexec` produced a success status without the target marker. Disabling `errexit` in the script let the successful tail hide the target’s exit 23. An exported function replaced an executable invocation with a different successful result. The product adversaries also cover custom wrappers, dynamic and true `continue-on-error`, source/eval, redirected or masked syntax and a sibling’s contradictory step being substituted into another context. [GitHub shell profile reference](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#jobsjob_idstepsshell)

## Lifecycle controls

- In the default matrix fail-fast contrast, one variant has a failed install step and an explicitly skipped test step. Its reported step failure supplies no exact inner-command result. A sibling cancelled after starting has no install witness. The queued sibling is unstarted at observation with no unique variant assignment, and the omitted sibling has no runtime row. All required package-state claims remain unresolved.
- The cancelled-after-install contrast retains the admissible preceding completed-success install step for that same context. The command keeps its independently supported result. The cancelled job and its unresolved package state retain their own classifications.
- The explicit job-skip contrast retains GitHub’s skipped job row with no steps and unresolved variant correspondence. The applicable command remains unresolved. The other variants and ordinary jobs keep their own observations. [GitHub matrix fail-fast reference](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#jobsjob_idstrategyfail-fast)

## Persistence and verification

Coverage v6 and runtime dependency-state v3 retain the separate command result beside package state. CI inputs remain v2 for the prepared workflow. Four new SQLite revisions reopened with equal material digests in a fresh, network-disabled process with producer, parser and evaluator re-entry blocked. Seven older native captures also reopened, including the milestone 3 and 4 codecs. Those older captures keep their earlier command evidence; opening them does not derive the new relation.

The installed console entry replayed all 16 frozen provider responses through the current public path and reopened the saved report. Its substantive baseline digest matched, and all nine historical reports reopened with identical rendered digests. This was a parity check on the existing normal path. The scoped results above used the prepared product component. Public orchestration, report row delivery and normally captured scoped recovery are milestone 6. Final installed end-to-end acceptance is milestone 7.

The wheel matched all 120 checkout Python modules and passed dependency consistency validation. The final installed run passed **1,181 product tests**, **104 focused tests** and **25 affected consumer tests**. The experiment architecture check passed.

[Machine-readable verification receipt](VALIDATION.json)
