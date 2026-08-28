# UpgradePilot Agent Skills Governance Stage 1 Corrections Plan

**Plan status:** Structurally complete; executable repository-wide doctor run deferred to final post-merge local validation  
**Authority:** Non-controlling execution coordination; root `AGENTS.md` and normal responsibility owners remain authoritative.  
**Source proposal:** `proposals/2026-08-27_UPGRADEPILOT_AGENT_SKILLS_AND_GOVERNANCE_EVOLUTION_PROPOSAL.md`

## Lifecycle reconciliation

Stage 1's bounded structural work was completed before the later governance-evolution stages. The repository-wide positive `governance_doctor.py` run that this original plan listed as a Stage-1 pass requirement was subsequently and explicitly deferred until the complete Skills/governance branch is finalized, merged, and pulled locally. No repository-wide executable doctor PASS is claimed by this plan.

The execution/proof text below is preserved as the Stage-1 coordination record. Where it asks for a real-repository doctor PASS, read that item as the final deferred executable validation obligation rather than evidence that Stage 1 is still the live continuation.

## Responsibility

Correct the two objective Agent-Skills governance defects identified during the 2026-08-27 audit and protect the Learning-by-Doing → Learning-Only transition with one discriminating behavioral regression case.

This plan admits only Stage 1 of the proposal. It does not admit the later progressive-disclosure, learning-transfer, routing-evaluation, root-pruning, or new-Skill candidates.

## Entry evidence

The bounded work starts from these observed facts:

- root `AGENTS.md` already admits `upgradepilot-learning-only` as one of the five operation Skills;
- `.agents/skills/upgradepilot-learning-by-doing/SKILL.md` still contains the obsolete fallback text `Until a dedicated Learning-Only Skill is admitted`;
- `tools/agent-governance/governance_doctor.py` checks Skill presence, frontmatter presence, non-empty `name`/`description`, name-directory equality, unique names, and expected operation Skills, but does not yet validate the admitted Agent Skills name grammar/length or description maximum length;
- `tools/agent-governance/learning_only_cases.json` already protects Learning-Only behavior but does not contain a dedicated regression case whose setup begins with Learning-by-Doing active and then explicitly switches to the admitted Learning-Only Skill.

## Allowed modification boundary

This plan may modify only:

- `.agents/skills/upgradepilot-learning-by-doing/SKILL.md`;
- `tools/agent-governance/governance_doctor.py`;
- `tools/agent-governance/learning_only_cases.json`;
- `tools/agent-governance/README.md` when required to keep the doctor's documented objective checks accurate;
- this plan only if execution discovers an ambiguity in its own bounded coordination responsibility.

No product source, product tests, specifications, ADRs, root operation catalog, other operation Skills, learning packages, or live project-state files are in scope.

## Execution sequence

### 1. Correct the Learning-by-Doing transition

Replace the obsolete pre-admission fallback with an explicit transition to the already-admitted Learning-Only procedure.

Required behavior:

```text
explicit request to stop building and just learn
→ product mutation pauses
→ route through .agents/skills/upgradepilot-learning-only/SKILL.md
→ compose applicable root/Operating-Guide/package-local owners
→ do not continue Build merely because Learning-by-Doing was previously active
```

Do not duplicate the full Learning-Only procedure into the Learning-by-Doing Skill.

### 2. Strengthen deterministic Skill frontmatter validation

Extend `governance_doctor.py` with objective checks for every discovered Skill:

- `name` remains required and must match the parent directory;
- `name` length must be at most 64 characters;
- `name` must use lowercase ASCII letters, digits, and single hyphens between non-empty segments, thereby rejecting leading/trailing/consecutive hyphens and other characters;
- `description` remains required and must be at most 1024 characters.

Keep these checks deterministic and local. Do not add fuzzy semantic description-quality scoring, external dependencies, or a hard 500-line Skill-size failure.

### 3. Add one transition regression case

Add one new Learning-Only behavioral case that starts with Learning-by-Doing active and then explicitly asks to stop building and learn only.

The case must require:

- routing to the admitted Learning-Only Skill;
- immediate product-mutation pause;
- preservation of applicable package-local learning ownership;
- no use of the Learning-by-Doing Skill as a fallback replacement for Learning-Only.

Avoid duplicating `LEARN-001`; the new case specifically protects the cross-mode transition and admitted-Skill routing fact.

### 4. Keep developer documentation aligned

Update `tools/agent-governance/README.md` only enough to state that the doctor validates Skill frontmatter name grammar/length and description length in addition to the existing checks.

## Proof obligations

### Final executable repository validation — deferred

The complete governance/Skills system must eventually run:

```bash
python tools/agent-governance/governance_doctor.py
```

That repository-wide executable validation is deliberately deferred until the governance branch is finalized, merged, and pulled locally. Stage 1 therefore makes no repository-wide doctor PASS claim by itself.

### Negative discriminating validation

Using temporary uncommitted Skill fixtures in a local checkout, prove that the updated doctor rejects at least:

1. an invalid Skill name grammar while the name still matches its temporary directory;
2. a Skill name longer than 64 characters;
3. a Skill description longer than 1024 characters.

Temporary fixtures must be removed after the check and must not be committed.

### Structural review

Inspect the final diff and confirm:

- the obsolete Learning-Only fallback is gone;
- the new wording points to the admitted Learning-Only Skill rather than copying its procedure;
- the doctor checks are objective and do not expand into semantic linting;
- the new case is valid under the existing case-bank schema and has a unique ID;
- the README describes implemented doctor behavior accurately.

## Pass condition

Stage 1 is structurally complete when all of the following are established:

- Learning-by-Doing contains no obsolete pre-admission Learning-Only fallback;
- explicit Learning-by-Doing → Learning-Only transition wording routes to the admitted Skill and pauses product mutation;
- the doctor contains deterministic rejection logic for invalid name grammar, overlong names, and overlong descriptions;
- the transition regression case is admitted without schema/ID errors;
- the README describes the implemented doctor behavior accurately;
- no files outside the allowed modification boundary changed during the Stage-1 implementation, apart from the proposal/plan commits already present on the dedicated working branch.

The final repository-wide executable doctor run remains a separate post-merge validation obligation and is not evidence that Stage 1 is still open.

## Stop line

Stage 1's structural work is complete. The following list records the original Stage-1 stop boundary; later stages were subsequently authorized and executed under their own plans, so this list must not be interpreted as current continuation.

At the original Stage-1 boundary, do not begin:

- Build/Audit progressive-disclosure extraction;
- Learning-Only B2-route generalization;
- storage-strength/retrieval additions;
- trigger/routing evaluation runner work;
- root `AGENTS.md` or `OPERATING_GUIDE.md` pruning;
- admission of any sixth Skill.

Those responsibilities required their own later bounded decisions/execution steps.