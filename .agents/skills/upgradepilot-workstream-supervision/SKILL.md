---
name: upgradepilot-workstream-supervision
description: Supervise one or more UpgradePilot workstreams being performed, or recently completed but not yet reconciled, by other AI agents. Use when Ali asks to check parallel/other-agent progress, reconstruct what each workstream is doing, verify process/results/evidence against the applicable governance and Skills, understand material developments, detect cross-workstream conflicts, and decide whether to continue, watch, guide, intervene, or reconcile. Read-only by default; it does not itself authorize fixes or agent orchestration.
---

# UpgradePilot Workstream Supervision

Use this Skill as the compact **support/composition procedure** for independently supervising meaningful UpgradePilot work performed by one or more other AI agents/workstreams.

**Skill provenance marker:** `UP-SKILL:upgradepilot-workstream-supervision`

This is **not a sixth primary operation**, not a replacement for Repository-Audit, and not an agent-execution framework.

Root `AGENTS.md` owns authorization, responsibility ownership, operation routing, support/composition boundaries, and context discipline. `OPERATING_GUIDE.md` owns project-wide Learning-by-Doing, proportionality, evidence interpretation, assistance/ownership, and handoff. The exact product/design/plan/source/evidence owners remain authoritative inside their responsibilities. This Skill reconstructs and supervises workstreams by composing those existing surfaces; it does not become a second project-control system.

## Activation and action boundary

Use this Skill when Ali explicitly or clearly asks to:

```text
supervise/check/watch work another AI agent is doing
review ongoing parallel agent work together
catch up on named workstreams and verify they remain on track
reconcile progress/results from several active agents
independently check another agent's process + result + evidence
supervise recently completed other-agent work before relying on it
```

The supervised work may be Build/Implement, Planning/Design, Audit/Review, Learning-by-Doing, Learning-Only, research, proposal writing, governance, testing/debugging, learning-artifact work, or another bounded UpgradePilot responsibility.

Do **not** activate this Skill merely because:

- ordinary work is progressing in the current conversation;
- Ali asks for a one-off repository Audit/Review with no workstream-supervision responsibility;
- Ali asks for general project status without asking to supervise named/identifiable other-agent work;
- several branches/sessions happen to exist;
- another agent could theoretically be used.

Supervision is **read-only by default**. It may identify a problem, recommend an intervention, or draft a precise instruction for the responsible agent. It does not itself authorize repository mutation, external mutation, merge/rebase/cherry-pick, agent dispatch, or scope expansion.

If Ali separately asks this session to perform a correction, route that new action through the applicable authorized primary operation before mutating anything.

## 1. Keep two routes separate

Every supervision session may involve two different procedural questions:

```text
SUPERVISION-SESSION ROUTE
What is this conversation itself authorized to do?

SUPERVISED-WORKSTREAM EXPECTED ROUTE
What operation, support Skills, owners, and boundaries should the other workstream be following?
```

Example:

```text
this session
→ Workstream Supervision + read-only Review/Audit as material

subject workstream
→ Build/Implement + Learning-by-Doing + Working-Memory
```

When you read another Skill solely to determine whether the **subject workstream** followed the expected procedure, treat that file as an **evaluated procedure reference**. That does **not**:

- activate that operation for this supervision session;
- grant its mutation authority;
- require its `UP-SKILL:*` marker in this session merely because it was consulted.

Emit another Skill's provenance marker only when that Skill is actually activated and materially applied to the **current supervision session's own responsibility**.

For example, activate/materially apply Repository-Audit when a checkpoint becomes a substantive cross-owner correctness/necessity/proof evaluation. Merely checking whether a Build agent should have used the Build procedure is not current-session Build.

## 2. Scope the workstreams before inspecting them

Start with the workstreams Ali actually wants supervised.

When several are named, keep them separate first. The unit is the **bounded workstream responsibility**, not the AI session/persona itself.

For each stream, establish only what is needed to identify it:

```text
workstream / responsibility
authorized or expected scope
relevant branch / PR / artifact / plan when applicable
current or recent checkpoint
```

Ali's description is normally enough to choose the relevant streams. Do not inventory every branch, session, working-memory record, or open idea merely because supervision is active.

If the workstream identity is ambiguous, use the repository's plans, current/recent working-memory, branch/commit/PR state, or artifact names to resolve it. Do not pretend to see another agent's private conversation, hidden reasoning, or unexposed tool trace.

## 3. Reconstruct from the smallest sufficient evidence

Use a fresh-session reconstruction pattern:

```text
Ali's workstream description
→ exact governing owner / selected plan when material
→ directly relevant workstream working-memory or handoff
→ actual artifact / branch / commit / PR / source / tests / research output
→ current execution/runtime evidence when the claim requires it
```

`MEMORY.md` is required only when canonical live project continuation materially affects the supervision question. A workstream may be supervised without making it the live project position.

Treat progress notes, handoffs, agent summaries, provenance markers, tickets, and plan status as **claims/context inputs**. Verify material claims against the evidence owner appropriate to that claim.

Useful temporary workstream brief:

```text
Responsibility / allowed scope
Expected operation + support Skills
Canonical owners
Agent-reported state
Observable evidence / verified state
Material unresolved claim or proof gap
Next meaningful checkpoint
Cross-workstream dependency, only if one exists
```

Keep this brief in session context unless working-memory is independently justified. Do not create a new permanent tracker or second live-state owner.

## 4. Map the expected procedure without over-loading context

For each supervised stream, determine proportionately:

```text
what responsibility is actually being performed?
which primary operation should govern that work?
which support/composition Skills are materially expected?
which canonical owners are relevant?
which conditional owners/references should have become material?
what stop/proof/authorization boundary applies?
```

Inspect the exact operation/support Skill when its procedure is material to judging the subject workstream. Do not load every UpgradePilot Skill just to build a complete matrix.

Common examples:

- implementation stream → Build/Implement expected; full Learning-by-Doing when materially applicable; Working-Memory when intentionally maintained;
- planning/design stream → Planning/Design expected;
- standalone mastery stream → Learning-Only expected;
- durable learning-artifact stream → Learning-Artifact support expected, with its primary operation unchanged;
- substantive formal repository evaluation stream → Repository-Audit expected.

A supervised stream may itself have used several procedures. Check only the procedures whose requirements could change the supervision judgment.

## 5. Separate claims from evidence

For every material progress/completion/proof claim, keep distinct:

```text
REPORTED
what the agent / handoff / working-memory says happened

OBSERVED
what current artifacts, commits, tests, outputs, or other direct evidence establish

INFERRED
what reasonably follows from the observed evidence but was not directly established

UNRESOLVED
what remains unverified, stale, conflicting, unavailable, or blocked
```

Do not treat agent identity, confidence, a `UP-SKILL:*` marker, a commit, a passing narrow test, or a written handoff as stronger proof than it actually is.

Absence of evidence is not automatically evidence of failure. State the missing proof and whether it matters before the next material step.

Use the proof owner appropriate to the claim. For example:

- plan/proposal quality → relevant plan/proposal responsibility + source/research evidence;
- product behavior → current source/tests/runtime evidence;
- experiment behavior → experiment source/tests/evidence;
- Learning-Only quality → current teaching route + real source/test anchors + learner-ownership evidence available to the session;
- process compliance → observable artifacts/provenance/working-memory plus explicit uncertainty about unobservable behavior.

## 6. Choose supervision depth proportionately

Use these as conversational depth guides, not repository statuses:

### Light

Use when the responsibility is already understood, the change/checkpoint is small or familiar, evidence is direct, and no material discrepancy or cross-stream pressure appears.

Typical path:

```text
exact checkpoint
→ nearest owner/artifact/evidence
→ concise judgment
```

Do not activate full Repository-Audit merely for ceremony.

### Standard

Use for meaningful progress where Ali needs confidence that scope, expected procedure, result, proof, state preservation, and learning/project direction remain coherent.

Inspect the relevant route + artifact + evidence and explain material findings.

### Deep

Escalate when there is a material:

- owner/specification/ADR/plan conflict;
- architecture or responsibility-placement question;
- correctness/necessity/proof dispute;
- security/trust/environment boundary;
- repeated failed or weak evidence;
- consequential novel mechanism;
- cross-workstream dependency/conflict;
- unexplained deviation from the expected procedure;
- claim that would authorize/justify a consequential next step.

Compose the applicable existing operation/conditional procedure rather than recreating its detailed checklist inside this Skill.

## 7. Select only the supervision lenses that matter

Possible lenses are:

### Authorization and scope

Is the workstream still inside what Ali authorized? Has it silently expanded, crossed a stop line, or mutated an external/other target without authority?

### Expected operation / Skill / owner alignment

Is the stream using the correct procedural route and canonical owners for what it is actually doing? Did a conditional owner become material and get ignored?

### Process / trajectory

Is the work progressing in a sensible order with appropriate evidence, preservation, and stopping behavior? Are assumptions being corrected when evidence changes?

### Artifact-specific quality

Is the produced source, plan, proposal, research, learning artifact, governance change, test result, or other output technically/content-wise sound?

For a deep material judgment, compose the exact existing Audit/Planning/Build/Learning procedure that owns that kind of evaluation rather than inventing a parallel review method here.

### Evidence / proof / claim strength

Does the evidence establish what the agent says it establishes? What remains unproven? Is stale or weak evidence being promoted into a completion claim?

### State / working-memory consistency

When material, does the workstream's working-memory accurately preserve the engineering progression and proof limits? If canonical live project position changed, is `MEMORY.md` consistent with actual state?

Do not inspect/update `MEMORY.md` reflexively for a side workstream whose live-project selection has not changed.

### Learning / ownership

When the supervised responsibility includes Learning-by-Doing or learning, is Ali getting the important mental model, evidence closure, and ownership opportunity at appropriate depth? Do not manufacture a lesson for every checkpoint.

### Proportionality

Is the agent falling into unnecessary investigation, repeated proof, overengineering, underengineering, premature abstraction/framework adoption, excessive ceremony, or review loops that no longer buy useful confidence?

### Cross-workstream reconciliation

Use only when several streams are in scope. Look for real shared pressure such as:

- shared semantic/method owner;
- one stream invalidating another's assumption or evidence;
- order/dependency constraints;
- overlapping or conflicting changes;
- responsibility duplication;
- duplicated investigation;
- working-memory/live-state conflict;
- research/learning conclusion that should materially change another stream.

Parallel timing alone is not a dependency.

## 8. Inspect each stream before inspecting the joins

For several workstreams:

```text
Stream A responsibility → expected route → claims/evidence → current judgment
Stream B responsibility → expected route → claims/evidence → current judgment
...
→ only then inspect material A↔B joins
```

Do not collapse separate streams into one generic status summary or invent one shared plan.

If two streams are tightly coupled enough that independent progress is creating duplication/conflicts, say so. The correct intervention may be serialization, scope clarification, or one shared decision—not more parallel agents.

## 9. Keep Ali oriented without turning supervision into a separate course

Supervision is also an engineering-ownership surface.

For substantive checkpoints, explain the material mechanism, decision, evidence gap, or deviation Ali needs in order to judge the work with you. Use the default Learning-by-Doing method from `OPERATING_GUIDE.md`.

Compose the full Learning-by-Doing Skill only when its fuller orientation/reasoning/evidence/ownership cycle materially improves this supervision responsibility or Ali explicitly requests it.

If Ali explicitly pauses the supervision work to master a topic, route that standalone learning responsibility through Learning-Only. Evaluating another stream's Learning-Only procedure does not itself make this session Learning-Only.

## 10. Produce a supervisory judgment, not a ceremonial score

Use plain findings and evidence first. When a compact decision label helps coordination, use one of:

```text
CONTINUE
CONTINUE / WATCH
GUIDE BEFORE NEXT MATERIAL STEP
INTERVENE NOW
STOP / RECONCILE
```

Interpret them as conversational judgments only:

- **CONTINUE** — no material issue changes the current route;
- **CONTINUE / WATCH** — concern exists but intervening now would be premature; name the next discriminating checkpoint;
- **GUIDE BEFORE NEXT MATERIAL STEP** — the current micro-step may finish, but give exact guidance before crossing a material boundary;
- **INTERVENE NOW** — continuing would compound a material problem; provide the smallest actionable intervention;
- **STOP / RECONCILE** — authorization, owner/architecture, proof, state, or cross-workstream conflict makes further progress irresponsible until resolved.

Do not force a label when ordinary prose is clearer. Do not persist these labels as project enums/status fields.

## 11. Intervene with the smallest exact handoff

When intervention is justified, produce:

```text
finding
→ evidence + uncertainty
→ why it matters before the next material step
→ smallest exact instruction / decision request
```

Prefer sending the correction to the agent/workstream that already owns the responsibility when that avoids unnecessary takeover.

A useful corrective instruction should normally state:

- what must be reconciled or checked;
- the exact owner/evidence boundary involved;
- what not to expand/change;
- the proof or stopping condition for the correction.

Do not dump the entire supervision analysis into the other agent's prompt when a short precise correction is enough.

If Ali asks this session to make the repair, explicitly hand off/transition into the proper authorized operation. Keep:

```text
supervision finding/proof
!=
repair implementation/proof
```

## 12. Preserve supervision progression only when useful

If Ali asks for a working-memory trail, or this supervision responsibility intentionally maintains one, compose `.agents/skills/upgradepilot-working-memory/SKILL.md` and update it at meaningful checkpoints.

Useful preserved material includes:

- workstreams supervised and their evidence horizons;
- material discrepancies or cross-stream dependencies;
- important intervention decisions and why;
- research/architecture/learning conclusions that changed the supervision model;
- what is established vs unresolved;
- next meaningful checkpoint.

Do not log every inspected commit, message, or test rerun.

Do not create/update `MEMORY.md` merely because supervision occurred. Update it separately only when its canonical live-position responsibility actually changed.

## 13. Stop line

A supervision checkpoint is complete when:

- the relevant workstream(s) are identified accurately enough;
- expected routes/owners are clear enough for the judgment;
- material progress claims are reconciled with available evidence;
- the selected supervision depth/lenses are proportional;
- material cross-stream relationships are addressed when applicable;
- Ali is oriented on consequential findings at useful depth;
- the next action/checkpoint or intervention is precise when one is needed;
- proof limits and unavailable visibility are explicit;
- no mutation or agent-control action occurred without separate authorization.

Then stop until new workstream evidence or a new user instruction creates another meaningful checkpoint.

## Anti-patterns

Do not:

- turn Workstream Supervision into a sixth primary operation;
- duplicate the Repository-Audit, Planning, Build, Learning-Only, Learning-by-Doing, Working-Memory, or Learning-Artifact procedures;
- scan all branches, commits, working-memory, plans, Skills, or source for every checkpoint;
- assume another agent's handoff/provenance marker proves its behavior;
- claim access to private reasoning/tool traces you cannot observe;
- emit another operation Skill's provenance solely because you inspected it as the subject stream's expected procedure;
- review every commit/message/micro-step;
- force code-review/test lenses onto plans, proposals, research, or learning work;
- create a permanent workstream tracker or duplicate live-state owner;
- invent dependencies because workstreams are parallel;
- automatically launch/restart/message/merge agents;
- automatically fix findings;
- require multiple reviewer agents for routine supervision;
- continue reviewer/fix loops without a discriminating next check or stopping condition;
- turn Ali's learning into a mandatory quiz at every checkpoint;
- treat more supervision as automatically safer or better.

## Provenance

When this full Skill was materially used and a normal completion/handoff surface exists, emit:

```text
UP-SKILL:upgradepilot-workstream-supervision
```

The marker records claimed activation only; actual routing, inspected evidence, and behavior determine whether the procedure was followed.
