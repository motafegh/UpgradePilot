# Verify source routes and screen a contrasting ranked adapter case

November 27, 2026. Applied the repository-audit and working-memory skills and used the requested doing-only cadence. The [previous screen](2026-11-27_ranged-adapter-transfer-screening.md) found no ranged adapter in the changed manifest. This pass allowed a separate eligible declaration and started by verifying source routes. The [verification receipt](evidence/2026-11-27-source-first-adapter-transfer/verification.json) retains the frozen criteria, exact source identities, all candidate dispositions, and the isolated route results.

## Verify the source routes

The installed wheel from `e87e8ac1` parsed four exact tagged adapter modules with visible imports of the prospective changed dependency. The source orientation used known tags independent of any rank or comparison outcome. A network-isolated replay supplied those exact upstream files and their matching source dependency literals to the adapter explorer at the adapter-sample boundary. Synthetic target calls supplied the starting bindings. The current explorer deferred the changed module, and the same origin lookup used by the normal product identified which module the pair stage would request at both exact versions. The replay measured question selection at this boundary. It did not look up package releases or acquire paired library files.

| Adapter module and target symbol | First changed module selected by the explorer |
| --- | --- |
| Requests 2.32.5 `requests.adapters.HTTPAdapter` | `urllib3.exceptions` |
| Boto3 1.35.0 `boto3.session.Session` | `botocore.session` |
| Starlette 0.41.3 `starlette.testclient.TestClient` | `httpx` |
| Requests 2.32.5 `requests.certs.where` | `certifi` |

For Requests, the first admitted changed-package import is `urllib3.exceptions`. The same file imports `urllib3.poolmanager.PoolManager` later and calls it in `init_poolmanager`. The production loop defers the first matching module and ends that exploration pass. The replay returned two matching exception import origins on one line. The product composer deduplicates module questions before issuing exact version requests. This illustrates a boundary in the selection order. A paired module request alone cannot establish that the call examined is relevant to the target root. [Exact Requests source](https://github.com/psf/requests/blob/b25c87d7cb8d6a18a37fa12442b5f883f9e41741/src/requests/adapters.py#L225-L241) · [Adapter exploration](../src/upgradepilot/caller_signature/source_acquisition.py) · [Exact pair composition](../src/upgradepilot/caller_signature/source_progress.py)

## Screen public PRs

Five bounded public code-search queries returned no usable candidates. One emitted a timeout diagnostic. I fell back to PR searches seeded by the verified module families and public repository references, then applied the same exact-head admission criteria. The queue excluded all 40 PRs from the previous screen and the existing LAFS and Dashboard API proof targets. A final same-criteria supplement used the remaining three diff slots for the Starlette to HTTPX route. Discovery and eligibility used anonymous reads. The replay dispatched no network requests.

I inspected 18 public diffs. The installed extractor recognized five supported single-pin changes. The head-inventory checks inspected all six eligible requirements or PEP 621 manifests within those targets' normal 16-attempt horizon. One target pinned the suspected adapter at Requests 2.32.5. Four lacked a matching Starlette declaration in the inspected manifests. All five stopped at the declaration check. The bounded screen used 11 upstream orientation reads, 14 discovery requests, 18 public diff reads and 16 exact-head eligibility requests. The receipt excludes separate endpoint connectivity controls.

## Disposition

No public case met the criteria, so the three-mode comparison remains open. The isolated producer result verifies four distinct routes to changed-module questions. Positive evidence that ranking improves a paired witness on a contrasting ordinary PR remains open. The earlier Dashboard ranking and LAFS fixed-choice results retain their original scope.

The next useful decision is whether acquisition should follow a relevant source path into a changed module when the needed import appears after a relative re-export or after a less relevant external import. Use the preserved LAFS path and Requests orientation to design a bounded diagnostic under the existing source limits. Require a trace from the target call to the particular changed-dependency call before treating an extra acquired module as useful. Keep the public transfer trial open for a case with demonstrated eligibility.
