# FCI candidate selection and rejection record

Selection date: 2026-10-20. These are exposed development/diagnostic cases, not holdouts or product-acceptance evidence.

## Admitted

| Case | Public PR | Frozen transition | Classification | Why admitted |
| --- | --- | --- | --- | --- |
| FCI001 | `openai/openai-agents-python#5404` | `mcp 2.0.0 -> 2.3.0`; base `64cd5dfc5a1579870dcbed0ea42b27aa84033fee`; head `8549af29bb5d4b061e3beb41b487ceb669cfb5c0` | `qualified_for_current_ci_diagnostic` | Current exact-head Actions evidence has a non-empty runtime step array and an ordinary workflow shape that satisfies the current static/runtime-correlation preconditions. User steps happen to be skipped, which keeps dependency-exercise claims correctly separate from identity correlation. |
| FCI002 | `executablebooks/mdformat-footnote#50` | `tox>=4.61.1 -> tox>=4.64.4`; base `9a174e4cba089f4b117134a220164bdc20f070fe`; head `c4b631da85386c18ad691c9d3d6af35b72e3a9ab` | `qualified_as_unresolved_control` | Python/tox-oriented transition with current rich executed-job steps and provider-unavailable/null steps on skipped jobs. The workflow has unnamed static jobs plus a later matrix; the current owner should first refuse `static_job_name_missing`, while matrix expansion remains a secondary unsupported shape. |
| FCI003 | `PasarGuard/panel#1044` | `fastapi>=0.143.2 -> >=0.143.3`; base `67096b59e80769e84b7a29012da62b8a78a7e273`; head `ffecd3d66aa307590dd41d7cc755dde7a5b5644b` | `qualified_as_unresolved_control` | Current exact-head workflow has five jobs with non-empty runtime steps and no matrix, but the static jobs have no explicit literal `name:` values. This isolates the owner's intentional static-job-name refusal boundary. |

Discovery stops at three admitted cases because the requested responsibilities are covered without adding redundant cases.

## Screened but rejected / not deepened

| Candidate | Decision | Reason |
| --- | --- | --- |
| `microsoft/SPARROW#83` — urllib3 `2.7.0 -> 2.8.0`, head `5aaa315023877c0200943dee5de84ea57f2d7f77` | `rejected` | Exact-head discovery exposed only CodeQL Advanced for the relevant head during screening. It did not add the application-CI/runtime-step responsibility needed by this cohort. |
| `p-e-w/heretic#510` — aiohttp `3.14.3 -> 3.14.4`, head `c5927614f4e2054866785deeca5b5512b2acd389` | `rejected` | Current CI had rich runtime steps, but its matrix-expanded job shape duplicates an unsupported-shape responsibility already represented within FCI002. |
| `aws-samples/sample-agentstorming#3` — urllib3 `2.7.0 -> 2.8.0`, base `e154ec224b32a93f0a21c957ab4b49c06756846c`, head `326e0ca5c93d85138666bdbd4b0721a37d163ee0` | `rejected` | Matrix-shaped CI plus an unrelated npm-audit failure introduced cross-ecosystem noise without a new diagnostic responsibility. |
| `microsoft/agent-framework#9556` — aiohttp `3.14.3 -> 3.14.4` | `not_deepened` | Screened during discovery, then stopped once FCI001–FCI003 covered the required distinct responsibilities. No case was added merely to raise cohort size. |

## Selection discipline

Candidates were not admitted because their desired outcome was known in advance. Admission required an exact frozen PR identity, a current exact-head Actions path, retained source/runtime evidence, and a distinct diagnostic role. Rejection remains recorded so later work can distinguish deliberate cohort boundaries from forgotten candidates.
