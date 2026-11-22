# UpgradePilot public portfolio and repository presentation strategy

- **Date:** 2026-11-22
- **Status:** AUDIT + RECOMMENDED DECISION — awaiting owner adoption for changes on `main`
- **Scope:** read-only inspection of GitHub `main` at `90601aa156913ed12afe683f27e15fe64990a185` and aligned WSL checkout; write only to research branch
- **Purpose:** make the existing credible engineering work findable, reproducible and accurately attributable for a potential hiring reviewer, without degrading contributor/agent knowledge or historical audit evidence
- **Related:** [Two-track operating allocation](2026-11-22_upgradepilot-aegislab-two-track-operating-decision.md) and [independent usefulness research](2026-11-22_1911_independent-maintainer-utility-supervision.md)
- **Authority:** `MEMORY.md` on `main` owns live project status; `AGENTS.md`, `docs/README.md`, Charter, security and relevant ADRs control their accepted responsibilities. This document cannot supersede them.

## 1. Audited baseline, with limits

The public GitHub repository `motafegh/UpgradePilot` is accessible and contains 3,627 Git-tracked paths in the local checkout at the inspected commit. Of those, **2,613 under `working-memory/`**, including **2,110 under `working-memory/evidence/`**, plus 340 `product-simulation/`, 128 `experiments/`, 120 `src/`, 118 `tests/`, 100 `plans/`, 92 `learning/`, 22 `docs/`, 24 `audits/`, 15 `proposals/`, 27 `tools/` and three `examples/` files. `working-memory/` occupies approximately 30.36 MB across tracked files; its mix is primarily JSON (923 files), TXT (815), MD (670), with Python, log and captured body artifacts also present. `examples/av-tracer/av-tracer-pr-11.zip` is roughly 2.91 MB and provides a reproducible saved case. These are **engineering/evidence inventories, not a quality score**.

Public GitHub repository metadata observed: description absent, topics empty, homepage absent, no tagged releases in the queried release list, and **no root LICENSE**. `pyproject.toml` has `version = "0.0.0"`, consistent with an in-development package but not a declared release. Only `product-verification.yml` is in GitHub Actions workflows; it is intentionally manually dispatched. The root `README.md` is approximately 24.7 KB; `MEMORY.md` ~210 KB and `OPERATING_GUIDE.md` ~62 KB. The Charter still labels UpgradePilot the primary learning flagship for a July–October 90-day period, whereas on Nov 22 the new recommended portfolio strategy assigns primary learning to AegisLab. **This is a prospective live policy change that needs a deliberate normative owner update, not a historical fact to silently erase.**

Existing strengths:
- README identifies the exact dependency-update maintainer problem, explicitly distinguishes observed evidence from compatibility/safety claims, documents install/CLI/offline report opening, separates source/test/experiment boundaries and clearly discloses substantial AI-assisted implementation. This is a stronger base than many public experimental repos.
- `docs/README.md` has a solid canon-versus-history and decision-promotion map. Accepted semantics, ADRs, current state, plans and raw evidence have distinct owners. Historical evidence can support actual conclusions rather than marketing prose.
- `examples/av-tracer/README.md` has one concrete reproducible source/CI case with a packaged report/workspace and third-party notices; it acknowledges its causal limitations.
- Product technical evidence is meaningful; live product readiness and independent maintainer usefulness remain distinct and must not be inferred from passing tests or exposed F4 reviews.

### Read-only public-content risk survey

A **lightweight heuristic** scanned text in current tracked files, **not Git history, ZIP interiors, binary payloads, runtime environment or third-party licensing obligations**. It found **zero files matching a narrow token-prefix/long credential-assignment/private-key-header pattern**. This is not a security audit or guarantee. It flagged approximately **349 text files with absolute home/Windows-user paths** (mostly `working-memory`) and three with private-range IPv4 address patterns. They may be innocuous or purposeful experiments, but publicly exposed paths/host metadata deserve contextual review. `.gitignore` does not remove already tracked or historical content. Respect third-party source redistribution rights and review every public packet, particularly large captured bodies and ZIPs. Do not print any discovered secrets as part of a later audit; respond to a verified credential leak with revocation and controlled history remedy, not a superficial README change.

## 2. Primary diagnosis

**The repository is not invalid or unprofessional merely because it contains many files.** Its detailed evidence history is both engineering value and an internal continuity asset. But its current public path puts a hiring reviewer near a very long README, a heavy internal governance system and 2,600+ historical evidence paths. This increases navigation burden and may obscure the central product demo and the owner's personally defensible decisions.

The design problem is **two audiences**:
1. **A maintainer/contributor/AI engineering assistant** needs source layout, current authoritative contracts, reproducible evidence, detailed historical research and exact work handoffs.
2. **A hiring reviewer** usually needs a short problem statement, what runs, what proof exists, one or two outcomes, architecture, code, limitations, the human contribution and a concise technical explanation.

**Recommended policy:** keep one public repository and historical Git trace, but create a separate *portfolio front door* that selects and explains verified evidence. Do not mass-delete, bulk-move, rewrite Git history, or create a duplicate stripped-down code repo just to minimize visible file count. A curated view can exist above the full research history.

## 3. Proposed artifact policy — retention and navigation

| Area | Decision recommendation | Hiring view |
| --- | --- | --- |
| `src/upgradepilot/`, `tests/`, `pyproject.toml`, `.github/workflows/` | **Keep in place**, maintain truthful package/test status; selected tests may be linked in case studies. | First-class technical evidence. |
| `README.md` | **Refactor / shorten opening**, keeping working CLI and accurate limitations; move excessive low-level steps into linked usage reference only with anchors/links repaired and tested. | 1–2 minute initial view, then deeper routes. |
| `docs/README.md`, `docs/specifications/`, `docs/architecture/` | **Keep canonical** and link only the few conceptually important ADRs from portfolio. | Deeper architecture review, not required first reading. |
| `working-memory/`, `working-memory/evidence/`, `audits/`, `product-simulation/`, `experiments/`, `learning/` | **Retain historical evidence** by default. Add clear research-history labels/navigation, privacy/rights audit and archive policy. Avoid moving known-file paths. | Opt-in deep provenance and learning trail. |
| `plans/`, `proposals/`, `archive/`, `chronicle/` | Keep selected accepted owners and historical discussions; distinguish accepted/current/superseded/proposed. | Accessible, not the headline. |
| `AGENTS.md`, `OPERATING_GUIDE.md`, `MEMORY.md`, `.agents/`, `ENVIRONMENT.md` | Keep internal contributor/agent routing valid. **Assess** their continuing cost and stale scopes separately; do not refactor this massive authority network for appearance only. | Link once as operating-method detail if relevant, not recruiter entry point. |
| `examples/` | Preserve tested reproducible demos and third-party notices. Create an easier **short guided demo** from one currently supported historical capture (perhaps AV-Tracer or MapProxy) without fake output. | Main inspection path for technical reviewer. |
| Proposed `docs/portfolio/` | Create a small, distinct **portfolio navigation and evidence** area only if the README cannot hold it clearly. No duplicate source or evidence archives. | Case studies, own contribution, technical walkthrough and limits. |

**Avoid adding more documents than necessary.** The likely minimum is a short README opening, one portfolio overview/technical walkthrough and one or two linked case studies. A separate contributions note can be included in the overview instead of another file.

## 4. Recommended hiring-facing narrative

**One-sentence framing:** `UpgradePilot is an AI-assisted, evidence-backed Python dependency-update investigation tool that correlates selected public PR, package and CI observations, preserves what those observations do not prove, and produces an inspectable maintainer report.`

**Explain honestly:** the supported product emits an explained abstention; supported CI command completion does **not** prove that the desired package was installed, imported or behaviorally compatible; the exact target Python/wheel applicability may remain unknown; independent maintainer usefulness/time savings are not established; no production adoption, full autonomous merge decision or finished release claim.

**Three proof stories to consider:**
1. **MapProxy matrix:** distinguish observed successful scoped install commands from unresolved installed-package state, preserve exact job/step/provenance, and show the proposed first-view UX only after it is actually implemented and tested.
2. **ApplyPilot failed install:** distinguish a failed consuming step from successful sibling jobs; a separate declared peer-package conflict does not automatically establish historical CI cause.
3. **AV-Tracer HTTPX:** the old/new `app=` API signature path and exact-job failure evidence support a bounded compatibility hypothesis, but loaded-module identity and counterfactual causation remain unproven. The saved public example can be reopened offline.

**Owner/AI attribution:** continue disclosing heavy AI-assisted architecture/code/tests accurately; support it with a few specific **personally exercised** decisions or independently diagnosed changed cases, linked to dated records where supported. Do not claim manual implementation or individual proficiency over 120 Python modules solely because they exist. Distinguish engineering contribution through requirements, experiments, evidence skepticism, design choices, reviews and actual user-performed diagnosis. Technical competence should be demonstrated through a live/reproducible exercise, not only an AI-written retrospective.

**3–5-minute reviewer route:**
- 30 seconds: problem, audience, narrow capability, non-goals.
- 1 minute: architecture sketch and real supported end-to-end CLI.
- 1–2 minutes: inspect one saved report, finding, proof limit and original source.
- 1 minute: select a test/source responsibility plus the owner's decision/diagnosis story.
- Final: status, limitations, what is being measured next.

The reviewer should not need a configured LM Studio model, public GitHub token, heavy live request, Git history archaeology or a 1,141-line report for first exposure. Use **offline saved source and a truthful concise explanation**. A short recorded demo or small curated screenshots are optional after text-based reproducibility.

## 5. Priority and effort under six hours of personal weekly UpgradePilot time

**P0 — Safety and accuracy (first relevant portfolio pass):**
- Review public packets/ZIP contents and tracked historical data for credentials, personal/host identifiers, unsafe paths, third-party material and redistribution rights. The preliminary heuristic is NOT clearance.
- Confirm the README and package metadata correctly reflect what runs at the current pinned commit and what has not been proven; check license policy and whether any third-party content constrains a chosen license.
- Adjust the Charter's active primary-learning designation **only after** the owner adopts the two-track strategic policy; retain the original July–October decision as historical.
- Do not publicly copy private workspace artifacts to create a showcase without a reviewed release packet.

**P1 — High-impact portfolio entry (one coherent bounded documentation increment):**
- Add a 30-second front page with: problem/user, current implemented behavior, 3 bullet-point core engineering challenges, one deterministic/offline inspection example, honest AI attribution and limitations.
- Add a single `docs/portfolio/README.md` or equivalent with a reader route, architecture diagram or short text path, two or three evidence-backed decisions, links to tests/ADRs and one user-facing limitation. Avoid converting historical logs into marketing.
- Create one 3–5 minute **offline-first walkthrough** from existing verifiable captures; use exact current CLI commands and independent evidence to avoid stale examples.
- Supply repository description/topic tags and an appropriate license/release policy once the owner approves; no automatic version bump, release or license selection.

**P2 — Maintainable ongoing documentation practice:**
- Maintain a small top-level current-capability section and stable links; no need to re-narrate every new commit. `MEMORY.md` continues as operational authority, not public changelog.
- For each material product change, update the relevant canonical owner, the short present-tense capability/limitation claim and demonstration only when materially changed.
- Periodically validate README links, example source IDs, install instructions, CI status and legal notice completeness at the exact documented revision.
- Consider slimming `MEMORY.md` to a concise live position **only if** the existing 210KB owner actually causes retrieval/usability errors; preserve and link the historical content. Agent governance file volume should be solved for operation, not superficial portfolio cosmetics.
- Consider archiving/moving evidence into another repository **only** if a measured size, exposure/rights, acquisition, reviewer or maintenance problem justifies it, with all path links, checksums, repository history and consumer behavior explicitly handled. A repository split does not by itself solve public-history exposure.

## 6. Decision and acceptance gates

Recommend choosing **public presentation + provenance-preserving historical storage** over bulk cleanup. Before implementing, owner should approve the scope of public information, GitHub profile/pinning, license choice and whether any historical documents must remain private. Public Git history complicates retroactive removal; a sensitive-information remedy is a separate controlled, authorized operation.

Success is not "fewer files". A person unfamiliar with the repo should be able to:
1. Understand the product's exact user/problem and truthful implemented status from the first screen.
2. Follow a safe, realistic runnable or offline saved example in a few minutes.
3. Inspect one genuine CI/evidence claim and its significant limit without reading internal worklogs.
4. Find two or three technical choices, their source/tests/evidence, and **accurate AI-assisted human contribution**.
5. Navigate deeper records if motivated, without broken canon/working-memory links.

**Not done by this audit:** no license choice, profile metadata edit, version bump, release, mass file movement, CI/tool execution, historical Git rewrite, claim of personal mastery, full security/third-party rights audit, or update to accepted `main` documentation. Owner should decide whether to turn P0/P1 into a small authorized presentation task after the current CI first-view product increment or as a deliberately chosen replacement.
