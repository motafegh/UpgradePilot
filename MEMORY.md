# UpgradePilot Current Memory

**Last updated:** 2026-09-13  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position

- **Current responsibility:** static shell/direct-install false-positive recognition in CI dependency evidence.
- **Mode:** Learning-by-Doing — A orientation/design. Read-only until the new correction is sufficiently bounded and Build/Implement is explicitly authorized.
- **Selected parent plan:** `plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`.
- **Active working memory:** `working-memory/2026-09-13_static-shell-direct-install-false-positive-recognition.md`.
- **Previous working memory:** `working-memory/2026-09-12_exact-revision-requirements-constraints-evidence-coherence.md`.
- **Repository route:** continue directly on `main` unless Ali later requests otherwise.
- **Framework status:** ordinary-Python / LangGraph / LangChain comparison remains closed; no framework re-entry is justified.

The parent synthesis journey still prioritizes correctness/provenance reinforcement before broader evidence production or non-abstention maintainer-action expansion.

## Previous correctness cycle — exact-revision requirements/constraints provenance — CLOSED A→E

The requirements/constraints route previously could consume a mutable PR-files patch from head B while downstream source context still carried a frozen head A when the changed-file count stayed equal.

The repair is now closed:

```text
frozen PullRequestIdentity A
→ acquire all PR-file pages
→ validate each changed-file contents_url against repository + exact filename + A.head_sha
→ retain complete-count check
→ re-read PR identity, including zero-file snapshots
→ require final base_sha + head_sha + changed_files == A
→ only then return ChangedFile records
```

Primary implementation owner: `src/upgradepilot/github/pull_request.py`.

Validation completed locally on synchronized `main`:

```text
13 focused provider tests green
15 nearby regression tests green
566 full deterministic tests green
```

The admitted claim remains client-side observable snapshot coherence, not transactional/cryptographic linearizability. A theoretical unobservable ABA-style mutation remains outside the proof boundary; exact commit comparison remains a stronger fallback only if future evidence justifies it.

D ownership review also closed. Ali correctly retained the core model: same-count head drift can misattribute evidence; GitHub provenance belongs at the provider boundary; per-file locator binding and final PR reread protect different propositions; green deterministic tests prove only their controlled horizon.

No new correctness gap was exposed inside that responsibility, so E closed it rather than reopening or broadening the mechanism.

## Current correctness cycle — static shell/direct-install false-positive recognition

### Why this is next

The preceding CI static↔runtime correlation work can strengthen static dependency-consumption evidence by establishing that the relevant workflow step completed successfully. A wrong static interpretation can therefore become stronger wrong evidence if the static command observer falsely recognizes dependency installation.

A prior controlled investigation reproduced false positives such as:

```text
pip install wheel # -r requirements-dev.txt
→ observed — false positive

echo "note; pip install -r requirements-dev.txt"
→ observed — false positive
```

The defect is current because `src/upgradepilot/dependency/workflow_context.py` still implements `bounded_shell_segments()` as textual splitting over `&&`, `||`, `;`, and newline without shell quote/comment awareness.

`src/upgradepilot/dependency/direct_install.py` consumes those segments before recognizing pip requirements-file installation. `src/upgradepilot/dependency/environment_selection.py` also consumes the same shared helper for pip/uv project-environment selectors.

Therefore the next A responsibility is **not yet simply “fix direct_install.py.”** A must determine the earliest sufficient owner and smallest sound correction:

```text
shared bounded shell segmentation
vs
narrower observer-owned correction(s)
```

without accidentally claiming complete Bash/POSIX/PowerShell/cmd interpretation.

### Current A questions

A should establish, proportionately:

1. exact false-positive classes inside the admitted repair;
2. earliest sufficient owner;
3. smallest mechanism that distinguishes real separators from quoted/comment payloads sufficiently for current product pressure;
4. existing positive cases that must stay supported;
5. shared-consumer regression pressure;
6. explicit unsupported/non-claim shell shapes.

Likely first source/test owners:

- `src/upgradepilot/dependency/workflow_context.py`
- `src/upgradepilot/dependency/direct_install.py`
- `src/upgradepilot/dependency/environment_selection.py`
- `src/upgradepilot/ci/workflow_commands.py`
- `tests/test_direct_install_declaration.py`
- nearest project-environment/workflow-command tests if the shared helper remains the owner.

## Current Learning-by-Doing cycle

```text
Slice: static shell / direct-install false-positive recognition

A — NEXT / NOT YET DESIGNED
    known failure shape + current source pressure re-anchored

B — NOT STARTED
C — NOT STARTED
D — NOT STARTED
E — NOT STARTED
```

### Cycle granularity preference

Ali's explicit process preference:

> Treat A→B→C→D→E as the real cycle. Do not recursively turn each stage into another elaborate sub-cycle. By default, finish each stage in one or two substantive rounds; use more only when the situation genuinely requires it or Ali explicitly requests smaller sub-steps.

This is a proportionality preference, not permission to skip material reasoning, proof, or state preservation.

## Maintainer-action synthesis baseline retained

The accepted synthesis semantics remain unchanged. The deterministic evaluator is still intentionally abstention-only:

```text
PublicPullRequestInvestigation
→ synthesize_maintainer_action(...)
→ MaintainerActionSynthesis(action="abstain")
```

No merge, targeted-check, investigate, block, or defer permission is implemented yet. Stronger technical evidence does not create action permission by itself.

## Closed CI foundations retained

- exact run/job attempt coherence remains closed and proven;
- bounded static↔runtime correlation remains closed and proven;
- exact-revision requirements/constraints changed-file provenance is now closed and proven.

Do not reopen them without concrete regression evidence.

## Later evidence bottlenecks retained

After static-command correctness is trustworthy, reassess rather than broadening automatically:

1. preserve an already-known CI consuming `job_key` into Target composition;
2. acquire exact runtime dependency-version/artifact evidence only for a precise selected proposition;
3. produce exact target wheel-compatibility evidence through a normal producer;
4. freshly discriminate CI acquisition-failure containment if decision-relevant;
5. broaden matrix/reusable/dynamic-name correlation only under real case/product pressure.

These are not all correctness defects. Conservative unresolved/unsupported behavior remains valid where UpgradePilot cannot safely establish a fact.

## Durable journey

```text
accepted synthesis semantics
+ abstention-only evaluator
+ exact-attempt CI identity
+ bounded static↔runtime correlation
+ exact-revision requirements/constraints provenance
        ↓
CURRENT: static shell/direct-install recognition correctness
        ↓
re-audit / retire corrected trust restrictions
        ↓
select next decision-critical evidence bottleneck
        ↓
re-evaluate non-abstention action reachability
        ↓
admit one action path at a time through normal producer proof
```

## Current stop line

Do not yet:

- modify product source/tests before A is sufficiently resolved and Build is explicitly authorized;
- adopt a full/general shell parser merely because shell syntax is complex;
- claim arbitrary shell-dialect support;
- combine this correction with matrix/reusable-workflow expansion;
- parse job logs or workflow artifacts;
- add exact wheel/version installation semantics;
- redesign Target composition;
- enable a non-abstention maintainer action;
- reopen the closed exact-revision cycle without new failing evidence.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`
