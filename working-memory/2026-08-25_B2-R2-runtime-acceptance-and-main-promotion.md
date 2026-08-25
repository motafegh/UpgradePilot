# B2 R2 — runtime acceptance and main promotion

**Date:** 2026-08-25  
**Branch:** `agent/r2-uv-lock-structural-model`  
**R2 base:** `d92e8d263e856c3dde3e6dc5ddcd99ce1f7d0288`  
**State:** R2 ACCEPTED / COMPLETE — ready for non-destructive fast-forward promotion to `main`  
**Authority:** working evidence only; `MEMORY.md` remains the sole live-state owner.

## Accepted responsibility

R2 established one bounded uv-specific owner for shared external `uv.lock` structural truth while retaining separate semantic consumers:

```text
exact uv.lock text
→ dependency/uv_lock_structure.py
   → UvLockStructure
      ├── dependency/uv_lock.py
      │   → base/head dependency-transition semantics
      └── dependency/uv_membership.py
          → explicit-root reachability projection/traversal
```

The accepted shared owner covers only genuinely common structural facts:

- TOML admission;
- exact integer schema-version admission and schema-1 boundary;
- non-negative exact integer revision;
- package-list/table admission;
- package distribution name, normalized name, version, and source admission;
- bounded versionless editable/virtual local-source admission;
- repeated normalized-name record preservation;
- raw package-record preservation for consumer-specific semantics.

It does not own transition comparison, graph/reachability semantics, workspace `--all-packages` scope, resolver/currentness proof, runtime uv behavior, or R4 proposition/naming redesign.

## Drift removed

The previous duplicate structural parsers had two concrete disagreements now removed at the earliest sufficient owner:

```text
versionless package record
old uv_lock.py       → only exact editable/virtual local source admitted
old uv_membership.py → version=None admitted regardless of source
```

and:

```text
TOML version = true
old membership comparison used true == 1 behavior
→ could enter schema-1 path

new shared parser
→ requires type(value) is int
→ boolean is malformed, not schema 1
```

## Runtime evidence

Local project environment on the R2 branch reported:

```text
shared structural regression
.venv/bin/python -m unittest tests/test_uv_lock_structure.py
→ 5 tests / OK

existing uv-focused regression discovery
.venv/bin/python -m unittest discover -s tests -p 'test_uv*.py'
→ user reported green before broadening

complete standard suite
.venv/bin/python -m unittest discover -s tests
→ 507 tests / OK

compile admission
.venv/bin/python -m compileall -q src tests
→ PASS

local worktree after validation
→ clean
```

The focused 5-test regression directly protects shared versionless admission, repeated-record preservation, transition/membership failure mapping, exact-int schema handling, unsupported schema distinction, and invalid untrimmed versions.

## Final ownership / diff review

GitHub comparison from the R2 base to the pre-closure branch head reported:

```text
status: ahead
behind_by: 0
```

Production scope remained bounded to:

```text
src/upgradepilot/dependency/uv_lock.py
src/upgradepilot/dependency/uv_lock_structure.py
src/upgradepilot/dependency/uv_membership.py
```

with focused regression coverage in:

```text
tests/test_uv_lock_structure.py
```

Review found no unexplained structural drift and no accidental implementation of:

- R3 workspace/`--all-packages` semantics;
- R4 reachability proposition/naming redesign;
- a generic dependency graph/package-manager abstraction;
- resolver/currentness/runtime proof.

The large deletion in `uv_lock.py` is intentional removal of duplicate structural parsing, not lost transition semantics. `uv_membership.py` retains only reachability-specific projection and genuine cross-evidence composition checks after shared lock admission.

## Learning closure

The R2 source walkthrough used real S001 evidence to trace:

```text
Pydantic exact base/head uv.lock
→ shared UvLockStructure
→ uv_lock.py
→ soupsieve 2.6 → 2.8.4
→ PR-wide dependency evidence

and separately

head uv.lock + selected docs environment
→ uv_membership.py
→ docs → mkdocs-llmstxt → beautifulsoup4 → soupsieve
→ transitive selected-root membership witness
```

The retained mental model is:

```text
structural parsing
= what an admitted uv.lock structurally says

transition consumer
= what changed between admitted base/head locks

reachability consumer
= whether an explicitly selected root can reach the changed package
```

These are separate propositions and remain separate owners.

## R2 disposition

R2 gate is satisfied:

- shared structural owner implemented;
- demonstrated duplicate-parser drift removed;
- transition and reachability semantic ownership remain independent;
- focused regression green;
- existing uv-focused regression reported green;
- complete standard suite 507 / OK;
- compileall PASS;
- worktree clean;
- final ownership/diff review PASS;
- no R3/R4 scope leakage found.

**Disposition:** `R2 COMPLETE`.

The accepted R2 branch is authorized for a non-force, fast-forward-only promotion to `main` provided GitHub still reports `main` at the R2 base / as an ancestor of the final R2 branch head at promotion time.

After promotion, R3 is the next plan position. R3 must be started as a fresh bounded continuation from synchronized `main`; it is not part of this R2 acceptance.
