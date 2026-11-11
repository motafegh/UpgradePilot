# AV-Tracer — public-safe saved-report review packet

**Scope:** Curated, attributed extract of the *actual saved UpgradePilot report*, plus a source/citation index. This is **not** the complete saved JSON/text report, a native Workspace snapshot, a replayable acquisition, a target-runtime test, or a substitute for the owner-only capture.

**Purpose:** Give a GitHub-only maintainer/reviewer the exact report opening and the critical retained source-level evidence needed to review the HTTPX compatibility concern. The [complete qualification receipt](qualification.json) and the [read-only maintainer review](../../2026-11-11_av-tracer-maintainer-report-review_lbd-cycle.md) are complementary; this packet deliberately preserves the difference between *actual product output* and *reviewer interpretation*.

## Source artifact identity and integrity

| Field | Observed value |
| --- | --- |
| Target | [ivaronkun-Ahey/AV-Tracer PR #11](https://github.com/ivaronkun-Ahey/AV-Tracer/pull/11) |
| Exact base | `527a004918c0f825e97c3583404242605fd58ec2` |
| Exact head | `25e7205f39103456e7efbc4e9f503f3debc7b5d8` |
| Dependency change | `httpx 0.25.2 → 0.28.1` |
| Saved report ID | `99a373c2-98d0-43ee-8a4b-2e7c449e82ba` |
| Report generated | `2026-11-11T13:32:42.617144+00:00` |
| Recorded generator / renderer | `3 / 4` |
| Workspace report revision | `80a58d494a8c46009aab8dc72b94b447` |
| Original saved `report.json` SHA-256 | `85fd07790ebb0e44eecda9b1f6688251e1d0dec7dc2d340dc66beb9105d69bd3` |
| Original retained text rendering | 5,602 lines; 252,212 bytes (observed local inspection) |
| Evidence classification | Exposed development case, conditional source-level analysis |

The file digest was checked locally against the recorded [public qualification](qualification.json); the exact original source-bearing file was reopened offline. The full report and Workspace remain under the user's owner-only local `$HOME/.local/share/upgradepilot/av-tracer-exact-allocation-2026-11-11.v6SbOe/` capture, **outside Git**. A future user or runner without that private capture cannot verify byte-exact report recovery from this packet alone.

## What the product actually showed first

The following lines are a **literal, selected extract** of the original saved report's `Review at a glance` section (header and unrelated sections omitted; no new conclusion inserted):

```text
Review at a glance
Update: httpx 0.25.2 -> 0.28.1

Caller and signature fit (conditional source evidence)
Target call: source-28 L6 TestClient
Compared call: source-29 L399 super().__init__
Old 0.25.2: arguments fit
Proposed 0.28.1: arguments rejected
Applies under the recorded source and dispatch assumptions. See witness conditions below.
Open: What installed version, import binding and runtime dispatch make these conditional witnesses applicable?
CI dependency coverage: not evaluated
Runtime dependency state: not evaluated
```

This original opening **does not name the rejected parameter**. That fact is recoverable later from the detailed witness, not from this opening. The product's actual maintainer action was **`abstain`** with no non-abstention permission admitted. An abstention is not a compatibility or safety verdict.

## Selected detailed facts retained in the report

These are selected **report fields**, not copied full upstream files. The line positions identify where the field appeared in the saved 5,602-line text rendering; they are *not* original-source line numbers.

| Report field | Saved text position | Meaning and source |
| --- | ---: | --- |
| Proposed witness: `rejected`, `httpx==0.28.1` | ~2,423–2,430 | `source-29` caller → `source-31` constructor |
| `Keyword reception: app: not_received` | 3,715 | Proposed HTTPX constructor does not receive `app` as a named parameter |
| `Local violation: unexpected_keyword: app` | 3,721 | Exact rejected keyword; conditional source-level result |
| Old witness: `bound`, `httpx==0.25.2` | ~3,739–3,747 | Same source caller → `source-36` constructor |
| `Keyword reception: app: named_parameter` | 5,046 | Old HTTPX constructor accepts the named argument |

For both old and proposed versions, the other observed forwarded keywords `base_url`, `headers`, `transport`, `follow_redirects`, and `cookies` were classified as accepted named parameters under the sampled source assumptions. These records establish a **candidate static signature comparison**, not that a specific CI environment loaded those versions or reached that callable.

## Exact source identity and inspection links

| Saved ID | Captured role and original-source locator | Original SHA-256 |
| --- | --- | --- |
| `source-28` | [AV-Tracer head: `backend/tests/test_app.py:6`](https://github.com/ivaronkun-Ahey/AV-Tracer/blob/25e7205f39103456e7efbc4e9f503f3debc7b5d8/backend/tests/test_app.py#L6), module-level `TestClient(app)` | `d261340d34a4aac1e9fa942385aabaa729d12ad865dd9380a99c52e9c24c4d40` |
| `source-16` | [FastAPI 0.104.1: `fastapi/testclient.py:1`](https://github.com/fastapi/fastapi/blob/7e5afe2cb9bf1fa30c04a4dd393ea397a46db29b/fastapi/testclient.py#L1), re-export of Starlette `TestClient` | `9c1bda0265fae9895d45e24d6573ce935b1fba8d90ea1b3c6cebc86827a9e8b4` |
| `source-29` | [Starlette 0.27.0: `starlette/testclient.py:399`](https://github.com/Kludex/starlette/blob/0c4b68ac4e179a788e38bac28f299dcad0f36e99/starlette/testclient.py#L399), sampled `super().__init__(app=...)` forwarding | `3349230dd87260809182440c138f745c18ddfc6dd31aa2871688578cc1f20676` |
| `source-36` | [HTTPX 0.25.2: `httpx/_client.py:620`](https://github.com/encode/httpx/blob/cc206cf2dad42600479962ac1daaa44675cfaf56/httpx/_client.py#L620), old `Client.__init__` includes `app` | `6bfda818e4b0fed70879aac8397c476aa80c8266314b266d4d38e72eff60ce2f` |
| `source-31` | [HTTPX 0.28.1: `httpx/_client.py:639`](https://github.com/encode/httpx/blob/26d48e0634e6ee9cdc0533996db289ce4b430177/httpx/_client.py#L639), proposed `Client.__init__` omits `app` | `c43f941baefe58c91e96d00039e1868fe719d91453026d7db1647194563bff8d` |

The source IDs are **report-local**, not global stable identifiers; the linked upstream GitHub content is external and was captured at the listed exact revisions. Source locators and hashes are retained here rather than full third-party file copies.

## Limits, omissions, and the necessary next observation

- Caller/signature source acquisition was **partial**, with 24 retained files, 33 material omissions and 57 analysis gaps. The analysis completed its bounded work; it did **not** establish exhaustive impact coverage.
- FastAPI and Starlette 0.104.1 / 0.27.0 are **sampled source versions**. The actual installed packages, module file identities, import bindings, effective `super()` resolution and execution of this path are **not established**.
- The source-only profile explicitly **did not evaluate CI coverage or runtime dependency state**. A historical failed CI step is separate evidence and its cause is unverified.
- A specific discriminating observation would pair the **exact-head backend pytest traceback** (if already available) with installed/loaded version/file information for the actual job. An absent traceback stays absent; a source mismatch alone cannot be elevated to an observed CI error.
- The existing action synthesizer returned `abstain`; neither the saved report nor this extract authorizes merging, blocking, approving or modifying the PR.

## Recovery and publication boundary

On the original authorized device with the owner-only capture, the normal **offline** source-opening route is:

```bash
PYTHONPATH=src .venv/bin/upgradepilot --open-report /path/to/private/report.json --show-source source-29
```

Use the saved report's exact source IDs. The command reads the local capture without live source acquisition. This GitHub packet cannot service `--open-report` or `--open-workspace`: it is **review evidence, not a replacement saved artifact**. Do not fabricate missing source bodies or treat link availability as a verified installed runtime.

**Privacy and retention choice:** The public repo retains this report-derived selected view, source identities, digests, normal-product outcomes and limitations. The raw `report.json` (~3 MB), the complete text render (~247 KB) containing substantial copied source, the SQLite Workspace (~10 MB), its sidecars and other unreviewed captured bodies remain in private local storage. Publish any later full captures only after separate content, license, privacy and security review; never mass-add the local data directory to Git.
