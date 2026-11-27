# Design and test the adapter source path diagnostic

November 27, 2026. Applied the planning-design and working-memory skills and used the requested doing-only cadence. The [bounded diagnostic plan](../plans/CALLER_SIGNATURE_NATIVE_ADOPTION_AND_QUALIFICATION_PLAN.md#changed-module-selection-from-a-target-call-through-an-adapter) records the acquisition experiment and proof criteria. The [verification receipt](evidence/2026-11-27-adapter-source-path-diagnostic/verification.json) retains exact input and output identities, file roles, cost, conditional witnesses and unresolved calls.

## Test whether source availability is the limiting step

The [LAFS report](2026-11-27_ranked-adapter-transfer-lafs.md) reached Flask without acquiring Werkzeug. The [Requests route control](2026-11-27_source-first-adapter-transfer.md) queued `urllib3.exceptions` before the module used by pool setup. I froze those cases and the comparison identities before the worker replay. The evidence question was whether supplying the relevant source alone would allow the installed worker to produce a pair for the same target root and the same adapter call.

The check used the installed `e87e8ac1` worker and its normal input and output codec. I acquired only the exact tagged paths specified for the diagnostic. Ten anonymous read requests returned 151,128 decoded bytes, including tag information and six complete module bodies. For LAFS I reused its actual target and retained Flask sources. The Requests controls used exact tagged Requests and urllib3 bytes with synthetic target calls. The worker ran in isolated network namespaces and every result decoded against its original input. The supplied files are controlled diagnostic inputs. They do not establish that the normal source provider would acquire those files under its full release-association contract.

| Offline input | Files | Witnesses | Old/proposed pairs |
| --- | ---: | ---: | ---: |
| Saved LAFS, replayed with matching input digest | 28 | 92 | 0 |
| LAFS with both tagged `werkzeug.utils` files supplied | 30 | 100 | 4 |
| Requests constructor with both `urllib3.exceptions` files | 4 | 1 | 0 |
| Requests constructor with both `urllib3.poolmanager` files added | 6 | 1 | 0 |
| Explicit synthetic `HTTPAdapter.init_poolmanager` entry | 6 | 0 | 0 |
| Synthetic `PoolManager` call through Requests' imported symbol | 6 | 2 | 1 |

All four LAFS roots are in `app/blueprints/main/routes.py`, at lines 79, 128, 141 and 182. Flask's package re-export reaches `flask.helpers.redirect`, whose direct fallback at line 263 passes `code` and `Response` to Werkzeug. Both exact Werkzeug signatures bind those keywords by name. The result retains the conditions on Flask selection, the import and execution reaching that fallback. `current_app.redirect` remains unresolved. [Werkzeug 3.1.3](https://github.com/pallets/werkzeug/blob/6389612fd1ee1bd93579eed5026e8fd471d04abd/src/werkzeug/utils.py#L242) · [Werkzeug 3.1.6](https://github.com/pallets/werkzeug/blob/04da1b5221b7a7b57e82246e4b5741d37a6b2e56/src/werkzeug/utils.py#L235)

Requests still stopped at `self.init_poolmanager` even with the two relevant module files admitted. The more explicit synthetic class method call also remained unresolved. The synthetic direct import through `requests.adapters` matched both `PoolManager.__init__` signatures, which confirms the available material was sufficient for a supported route. This excludes acquisition alone as a sufficient change for the constructor path. [Exact Requests source](https://github.com/psf/requests/blob/b25c87d7cb8d6a18a37fa12442b5f883f9e41741/src/requests/adapters.py#L173-L242)

## Fit the useful LAFS pair into the source allocation

The normal ranked LAFS run charged 39 GitHub and 44 total provider requests, but all 12 library-module attempts were already used. After seeing the four pairs, I ran a separate allocation control. I removed the last two distinct successful Flask modules in the original receipt order, `flask.sansio.blueprints` and `flask.sansio.scaffold`. With their two slots reserved, the first-pass replay still produced all 92 original witnesses. The run that used the slots for the two Werkzeug files had 28 files in total and preserved all 92 original witnesses plus eight new version-specific witnesses for the four pairs. This measures the effect of replacing material on this capture. Actual provider costs for the exact-release pair remain to be measured with the normal clients.

A local selection sketch then read the current worker's retained candidates, unresolved calls and import traces. Whole-file import scanning yielded ten distinct Werkzeug module names in the retained Flask source. Restricting the hint to unresolved calls inside a target-reached adapter declaration with matching recorded import evidence selected one module, `werkzeug.utils`, linked to all four redirect roots. The sketch returned the same answer with the two module slots reserved. It is development evidence from a case with a known answer. The current gap records omit a root identity, so the diagnostic uses the enclosing declaration as a hypothesis and relies on the final paired comparison as proof.

## Decision

Use LAFS for a bounded acquisition diagnostic with the existing provider route and original shared limits. The experiment should establish whether a selector can derive the module from retained facts and acquire both exact releases after reserving two module attempts, with visible coverage trade-offs and partial outcomes. This addresses a demonstrated source acquisition gap. Requests supplies a distinct negative control and a separate receiver-method correspondence question. No public ranking comparison ran and qualifying a fresh ordinary transfer case remains open.
