# Ranked adapter transfer qualification on LAFS

November 27, 2026. Applied the repository-audit and working-memory skills and used the requested doing-only cadence. The [machine-readable receipt](evidence/2026-11-27-ranked-adapter-transfer-lafs/verification.json) records the method, fixed inputs, comparison and offline verification. This follows the [Python-ranked adapter build](2026-11-27_ranked-python-adapter-sampling-build.md).

## Selection and proof

The eligibility screen fixed the candidate order and selection criteria before examining any comparison output. The first candidate, [LAFS PR #29](https://github.com/ggeerraarrdd/lafs/pull/29), qualified after six anonymous GitHub reads. It changes Werkzeug from 3.1.3 to 3.1.6 in `requirements.txt`. The exact head `78f6c1230c41659a9456a055465afb9ef65613e8` pins Flask at 3.1.1. Job `build` in `.github/workflows/api.yml` declares Python 3.13 at line 13 and installs this requirements file at line 15. The app imports Flask at line 33 and constructs it at line 49. The case and measurement criteria were frozen before the normal CLI runs. The eligibility screen allowed a fixed adapter and accepted a lexical entry point. That made it suitable for testing the rank-to-source join on a different framework and limited its ability to establish a changed selection or a complete path.

The installed wheel from `e87e8ac1` ran the caller-signature profile three times against the same base and head. A private acquisition shim saved bounded anonymous GitHub and PyPI responses at first use and supplied identical bodies to later modes for matching method, URL, query and media type. Each mode charged every response through the product's normal acquisition ledger. The limits were 50 GitHub requests, 100 provider requests, 8 MiB per body, 32 MiB total and 180 seconds, with a 24-request GitHub reserve, 16 target-file attempts and four adapter-candidate attempts. The comparison dispatched 43 HTTPS GETs in total, 38 to GitHub and five to PyPI, returning 699,695 decoded bytes. These counts exclude screening and connectivity controls. A separate direct PyPI connectivity probe used the proposed Werkzeug release URL. Its body was discarded and was absent from the comparison pool. Raw bodies, saved reports, request records and Workspace files are retained privately.

| Mode | Flask sample | Python evidence | GitHub / provider charges | Decoded bytes |
| --- | --- | --- | ---: | ---: |
| Unscoped | 3.1.1 | No Python selection | 38 / 43 | 675,574 |
| Annotation-only | 3.1.1 | Published file metadata overlaps the selected Python 3.13 line | 39 / 44 | 677,452 |
| Ranked | 3.1.1 | A non-yanked Flask wheel matched the Simple Index and the exact release by filename, digest and Python requirement | 39 / 44 | 644,791 |

The ranked mode checked one allowed Flask version and retained its source. `flask-3.1.1-py3-none-any.whl` declares `Requires-Python: >=3.9`, which overlaps the declared line at 3.13.0. Its digest matched in both PyPI records. The ranked run used one Simple Index request in place of the package-wide release lookup. In this case it had the same request count as annotation-only and charged 32,661 fewer decoded bytes. The sample and byte difference describe this case.

## Source result and boundary

All three modes retained the same modules and canonical analysis input, with 27 target roots and 92 identical bound witness assessments. Of those, 76 terminated in target source and 16 in Flask 3.1.1. For example, `app/app.py:49` resolves through Flask's package re-export at `src/flask/__init__.py:6` to `Flask.__init__` at `src/flask/app.py:226`. The reports retain Werkzeug imports in that Flask module, including `werkzeug.datastructures.Headers` at line 15.

The product's adapter explorer queues an external continuation from imports in the sampled entry module. This case's entry module forwards the observed symbol through a relative import. Source closure subsequently retains `flask.app` and its external imports. It does not feed those imports back into the earlier acquisition of exact changed-package pairs. All 13 module acquisition receipts were for Flask. There were zero deferred candidates for a Werkzeug pair, zero old/proposed Werkzeug source requests and zero paired Werkzeug witnesses. Nine source material omissions carry `closure_read_budget`, and the analysis has three unexamined retained units. The provider ledgers show zero acquisition stops. The report action was abstain in each mode.

**Disposition.** The exact-release file join, retained adapter source and saved report recovery transferred to an independently selected fixed Flask adapter. The run did not exercise a version selection change. It exposed a source traversal boundary before the changed Werkzeug dependency. Neither practical compatibility, actual installed state, CI execution nor maintainer usefulness was evaluated.

## Verification and implication

All three saved reports and their exact confirmed Workspace revisions reopened through the installed CLI in an isolated network namespace. The ranked report also opened the retained Simple Index fingerprint. A fresh offline ranked invocation read all 44 charged responses from the frozen pool, made zero network requests, and reproduced the request sequence, byte charges, rank decision and full analysis result. The receipts distinguish new report and Workspace identities from matching analysis. Product code was inspected to explain the acquisition boundary. It was not changed in this qualification.

For another test of rank-driven selection, pre-screen for a ranged adapter declaration and an external continuation already supported by the acquisition method. Freeze that case before inspecting which candidates rank highest. A broader feature for following relative forwarding into an external dependency has a separate proof obligation. LAFS is an observed example for that decision if additional representative cases show the gap materially affects coverage.
