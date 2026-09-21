# Cycle 1 — Runtime dependency-state semantic proof — 2026-09-21

**Status:** ACTIVE — Cycle 1 ready to begin at Phase A.  
**Master plan:** `plans/RUNTIME_DEPENDENCY_STATE_PROOF_COMPLETION_PLAN.md`  
**Investigation evidence:** `working-memory/2026-09-21_f6-post-install-package-state-feasibility.md`  
**Operation:** Learning-by-Doing composed with the applicable primary operation for each phase. Planning/Design controls Phase A until a Build decision is explicitly selected.

## Cycle responsibility

Establish whether UpgradePilot can truthfully derive:

```text
exact proposed dependency version
+ semantically eligible dependency-consuming command
+ exact successful runtime correlation
→ proposed version satisfied/present at the admitted command-completion boundary
```

without adding a new runtime package-state/log producer unless the evidence proves that one is necessary.

Cycle 1 combines two closely coupled master-plan layers:

1. install-command semantic eligibility;
2. command-success → dependency-state proof contract.

## Entry state

The full F6 investigation is complete.

Verified source facts entering this cycle:

- Tree-sitter already preserves shell structure and literal command arguments;
- `pip install --dry-run -r requirements.txt` can currently retain the same direct requirements-source declaration as an ordinary install because `--dry-run` is not yet interpreted at the dependency semantic layer;
- short-circuit, conditional, pipeline, asynchronous and related shapes are shell-structure concerns already represented by the parser-backed provider;
- current runtime correlation establishes bounded successful execution, not resulting package state;
- generic job-log/package-state acquisition is not selected.

## Phase A — orientation and semantic classification — READY

Goal: understand and classify only the pip/uv command semantics reachable through today's admitted product paths.

Actions:

1. trace current pip/uv option handling from parsed command atoms into dependency-consumption/project-environment evidence;
2. enumerate the materially relevant options for current supported command shapes;
3. classify each as:
   - positive/compatible with stronger state inference;
   - non-installing/excluding/retargeting;
   - ambiguous/dynamic/unsupported;
4. compare the classification with current focused tests and real supported scenarios;
5. identify the earliest correct semantic owner.

**Phase A output:** a source-backed semantic eligibility table/model and owner decision sufficient to enter Phase B.

**Phase A stop line:** no product implementation.

## Phase B — bounded design and implementation — PENDING

Activate only after Phase A resolves the semantic owner and smallest trustworthy rule.

Expected responsibility:

- define the minimum semantic/proof contract;
- decide whether existing result types are sufficient;
- implement only the earliest required owners and focused tests once Build is authorized;
- preserve existing declaration evidence rather than overloading it with claims it does not own.

No generic log ingestion or explicit package-state producer belongs here.

## Phase C — preservation and proof state — PENDING

Preserve:

- exact source/test changes;
- focused test results;
- integration state;
- proof debt/unavailable execution;
- what the implementation establishes and does not establish.

Update `MEMORY.md` only when the live position materially changes.

## Phase D — verification and ownership — PENDING

Verify proportionately:

- positive eligible command case;
- non-installing/retargeted close defeater;
- dynamic/unsupported case;
- exact static → runtime identity relation;
- normal application integration;
- broader regression when implementation exists;
- live/public case only when required by the claim.

Learning/ownership focus:

```text
shell syntax/structure
→ provider/Tree-sitter responsibility

package-manager option meaning
→ dependency semantic responsibility

runtime success
→ CI/runtime evidence responsibility

dependency state
→ composed stronger proof
```

## Phase E — cycle closure and next-cycle decision — PENDING

Close Cycle 1 from actual evidence.

Decision:

```text
Cycle 1 sufficient
→ close runtime dependency-state proof at this bounded path
→ do NOT create Cycle 2
→ return to parent evidence-to-action plan

Cycle 1 insufficient for a real decision-critical normal case
+ explicit target-owned evidence is justified
→ append/select conditional Cycle 2 in the master plan
→ create a new active Cycle 2 working-memory record
```

Do not create Cycle 2 merely for completeness.

## Cycle pass condition

One bounded normal command family has a precise, source-backed proof path from exact dependency source through semantic eligibility and exact successful runtime correlation to proposed-version presence/satisfaction at the admitted command-completion boundary, while close defeaters remain explicit.

## Current handoff

Start **Phase A**. The first task is the source-backed pip/uv semantic classification. No Build/Implement action has yet been selected.

**Procedural provenance:** `UP-SKILL:upgradepilot-planning-design`; `UP-SKILL:upgradepilot-learning-by-doing`; `UP-SKILL:upgradepilot-working-memory`.
