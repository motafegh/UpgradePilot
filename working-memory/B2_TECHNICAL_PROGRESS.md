# B2 Technical Evidence — 2026-07-24

**Record type:** Dated technical evidence; non-controlling  
**Behavioral source/test commit:** `bdd178f38ad23e82a93cc5f3505932e5d0ef3b53`

This record preserves what was observed on 2026-07-24. It does not state the live project
position or continuation; those belong only in [`../MEMORY.md`](../MEMORY.md).

## Observed environment

```text
Platform: WSL2 / Linux shell
Repository: ~/projects/UpgradePilot
Python: 3.12
Virtual environment: .venv
Install mode: editable
Network scope: public GitHub REST API, read-only
Authentication used for live run: none
```

## Observed deterministic and live proof

Ali observed:

```text
python3 -m unittest discover -s tests -v
→ 28 deterministic tests passed

python3 -m upgradepilot googlefonts/glyphsLib 1145
→ dependency pytest 9.0.2 → 9.0.3
→ exact head f3cda8a94600e58d27f1bc17c99b7693718b6350
→ 2 exact-head workflow runs
→ overall CI authority: sufficient
```

Observed workflow interpretation:

```text
Regression Tests → sufficient direct install-and-pytest evidence
Test + Deploy → unresolved because multi-job/tox indirection was not traced
overall → sufficient because at least one exact-head workflow proved direct exercise
```

This established that at least one successful exact-head CI path installed the changed
requirements file and directly exercised pytest. It did not establish complete test coverage,
compatibility, upgrade safety, or a maintainer recommendation.

## Source path represented by the proof

```text
PR locator and metadata
→ changed files and exact pinned dependency
→ exact-head Actions runs, jobs, and steps
→ run-specific workflow path
→ workflow text at exact head SHA
→ bounded command evidence
→ CI authority result
```

Responsibility boundaries at the recorded commit:

```text
github_api.py          shared read-only HTTP/JSON trust boundary
github_client.py       PR identity and changed files
github_actions.py      workflow runs, jobs, and step summaries
github_repository.py   exact-head workflow-definition acquisition
workflow_commands.py   bounded jobs/run command reading
ci_authority.py        deterministic authority classification
dependency_change.py   dependency interpretation
cli.py                 execution order and presentation
```

## Recorded first authority rule

The evaluator claimed sufficient authority only when one completed successful exact-head
workflow:

- had one statically identifiable job;
- installed the changed requirements file using pip `-r` or `--requirement`; and
- directly invoked the changed package or Python module.

It preserved unresolved results for indirect tox/script paths, multiple jobs, unavailable
workflow text, richer YAML, and package-command aliases.

## Boundaries of this evidence

- No runtime dependency was added for workflow parsing.
- The command reader was not a complete YAML parser.
- The proof concerned one public PR and one bounded rule.
- Later source or test edits require their own validation evidence.
- This dated record does not select subsequent product work.
