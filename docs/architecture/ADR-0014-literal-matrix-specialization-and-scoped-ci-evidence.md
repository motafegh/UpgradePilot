# ADR-0014 — Literal matrix specialization and scoped CI evidence

**Status — Accepted architecture and supported-scope direction.** Ali agreed to the proposed architecture and general direction on 2026-11-18, subject to the complete end-to-end implementation and verification requirements in the [implementation and qualification plan](../../plans/LITERAL_MATRIX_CI_EVIDENCE_IMPLEMENTATION_AND_QUALIFICATION_PLAN.md). Method-specific qualification remains an implementation gate. Build starts after the requested plan review.

**Responsibility —** Interpret literal GitHub Actions matrix variants, preserve their source and command identity, and associate supported variants with reported runtime steps.

**Owners —** [Static provider structure](ADR-0008-bounded-static-github-actions-workflow-definition.md), [command analysis](ADR-0009-parser-backed-static-workflow-command-analysis.md), [execution and package-state composition](ADR-0010-package-manager-semantic-facts-and-runtime-dependency-state-composition.md), [native recovery](ADR-0013-versioned-native-reconstruction-and-workspace-checkpoint-storage.md), and [evidence scope](../specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md#9-evidence-identity-scope-and-observation-strength).

## Context

MapProxy's retained workflow declares four Python versions and a singleton Pillow version. Its recorded attempt has four test jobs and four ordinary jobs. The product exposes their reported step outcomes. Dependency reasoning still encounters an unsupported matrix strategy, and the original install script contains a matrix expression that the shell parser cannot interpret directly.

A private source-only probe specialized all four combinations and reused the existing command parser. Each script became analyzable with four commands. The changed requirements install remained the second command and stayed outside existing runtime-strengthening eligibility. The four command locations were identical across combinations. The original script was 112 UTF-8 bytes and the specialized script was 90 bytes. Extending association alone would leave both a command-proof gap and an identity collision. [Design evidence](../../working-memory/2026-11-18_literal-matrix-dependency-evidence_design-cycle.md)

## Decisions and qualification boundaries

### 1. Keep three distinct propositions

| Proposition | Required basis | Permitted interpretation |
| --- | --- | --- |
| Declared variant | Exact workflow and complete admitted literal expansion | These fields follow from this declared combination. |
| Reported runtime correspondence | Exact-attempt provider records and a unique admitted source-to-record match | This interpreted variant corresponds to this reported job and its matched steps under the recorded method. |
| Successful command execution | Correspondence plus reported step outcome and an admitted shell/control-flow rule | This command has the supported execution evidence defined by that rule. |

Installed package state remains composed by its existing owner after those premises are available. A complete list of declared variants does not establish that each was created, executed or successful. The report retains a separate outcome for each variant and each material unresolved premise.

### 2. Add a provider-owned specialization companion

Keep RepositoryTextFile and the base WorkflowDefinition unchanged in meaning. Add bounded matrix expansion and field specialization under the existing GitHub provider responsibility, before shell analysis. Reuse the accepted PyYAML representation-node approach. CI and Target may consume the provider result while retaining their separate interpretation policies.

An expanded job refers to its original YAML job key and source occurrence, its typed matrix coordinates and expansion provenance, and its specialized fields. An ordinary job has an explicit ordinary context. Repeated coordinate rows retain distinct expansion identities. A local expansion ordinal distinguishes declared slots within the same frozen definition, without asserting anything about runtime scheduling order.

The matrix literal reader preserves scalar type and original spelling at the provider boundary. The current BaseLoader-backed scalar IR retains text only, so CI must not infer boolean or numeric identity from that text. The companion can retain the narrow matrix literal metadata without changing every general scalar consumer. The proposed initial scalar contract admits quoted strings, unquoted values unambiguously parsed as strings, core boolean/null spellings, and decimal integers exactly representable in the provider's numeric model. Preserve a quoted number as a string. Fractional/exponential conversion, alternate numeric spellings and object-valued axes require further characterization. Their source remains readable with a precise unsupported reason while that work is outstanding.

GitHub's own workflow-parser reader retains distinct string, number, boolean and null token classes. Its fixtures also demonstrate that a numeric-looking underscored value remains a string. That reference supports preserving type and spelling instead of using Python's default YAML implicit conversions. It is a pinned source reference for the type model, without a claim that it executes the hosted matrix scheduler. [GitHub YAML reader](https://github.com/actions/languageservices/blob/4043eda158e16579cc5fb1b0b07a4bce2a76f0b5/workflow-parser/src/workflows/yaml-object-reader.ts), [scalar fixture](https://github.com/actions/languageservices/blob/4043eda158e16579cc5fb1b0b07a4bce2a76f0b5/workflow-parser/testdata/reader/yaml-schema-exceptions.yml)

Expand the Cartesian product in declared axis order, apply partial-match exclusions, then apply include entries in source order against eligible original combinations. Include may extend an original row without replacing its original axis values, update fields added by an earlier include, or create an additional row. Extra include-created rows do not become original rows for a later include. Include-only matrices are represented directly. Matrix key lookup must account for GitHub's case-insensitive variable names, and case-colliding declarations must remain explicit.

Expansion limits must produce an incomplete/unresolved result before a truncated set can be used as complete. Use the provider's documented maximum and existing bounded-source resource safeguards. Empty declarations, repeated values and duplicate keys receive explicit outcomes. The initial include/exclude comparison class uses homogeneous scalar kinds for each compared property and rejects case-only string collisions across its relevant axis/include/exclude values. Under that admitted class, exact typed matching avoids depending on an unqualified loose-conversion or case-folding behavior. Mixed comparison kinds and other ambiguous equality cases retain an explicit comparison limit. This preserves MapProxy and the documented string-valued include example while leaving the wider comparison contract open for later qualification. [GitHub matrix semantics](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#jobsjob_idstrategymatrix)

### 3. Specialize allowed fields before shell parsing

The first expression subset is direct matrix property access, including a qualified quoted-key index form. Preserve unsupported operators, functions and external contexts as unresolved. Substitute once using the original expression occurrences. A replacement value containing expression-like text must not trigger recursive evaluation.

Specialize only fields whose GitHub schema admits the matrix context and whose meaning the selected consumer needs. Material fields include declared display names, run scripts, runner selection, action inputs, environment values and applicable error-handling settings. Keep unresolved higher-precedence shell or environment declarations visible. Workflow defaults prohibit expressions, and a job-level if is evaluated before matrix expansion, so neither may be treated as an ordinary matrix substitution site. Step conditions retain their condition meaning instead of becoming evidence of execution.

A direct scalar expression and a scalar embedded in text need their respective provider conversion rules. Preserve typed values where the field expects them. Quoted source strings must not be silently treated as numbers. Missing properties or an unqualified conversion remain unresolved for this first method. [Expression semantics](https://docs.github.com/en/actions/reference/workflows-and-actions/expressions), [workflow contexts and conditions](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#jobsjob_idif)

Insert the value as GitHub inserts it. Adding shell escaping would change the script being analyzed. A literal containing a semicolon can introduce another shell command, as the diagnostic demonstrated. Parse the resulting text through the existing command analyzer. The analysis remains inert. [GitHub substitution order](https://docs.github.com/en/actions/concepts/security/script-injections)

### 4. Make generated-text provenance and variant identity explicit

Retain the original step reference, its original command template and digest, the coordinates and specialization method, and the generated script and digest. Preserve replacement ranges and their coordinate sources. Command spans returned by the shell parser refer to the generated script. They must not be presented as byte ranges in the original template.

The full command identity includes the original workflow revision/path/job/step, the variant identity, and the occurrence within the generated script. Equivalent generated text from two distinct variants does not merge their execution contexts.

Carry that identity through consumption and direct-exercise evidence, candidate deduplication, runtime step lookup, command execution, package-state lookup and report/native projections. The existing runtime lookup returns the first matching job key, and existing candidate deduplication omits the variant. Both need migration before a matrix instance reaches them. The package-state consumer currently validates command text against the original step, so it must resolve the retained specialized context instead of comparing generated text to the raw template.

Use one explicit parent context or reference for related evidence where practical. Avoid copying coordinate maps into every scalar fact. Preserve ordinary and historical evidence with an explicit ordinary or legacy context. New codec and method identities must make the changed interpretation visible. Cold recovery restores validated retained values and transformations without performing fresh expansion, shell analysis or provider access.

### 5. Prefer source-defined identity witnesses over guessed default job names

Build candidate correspondences from the complete admitted specialized workflow and the exact captured-attempt jobs. Use an explicit source-defined job name when available, and the existing ordered user-step matcher over specialized step identities. For a job without an explicit name, an otherwise unique ordered-step identity can supply correspondence under the recorded provider-report trust assumption.

MapProxy's explicit Use python step names distinguish the four declared combinations. The probe obtained exactly one candidate per declared job/variant and exactly one job/variant per runtime row across all eight records while withholding runtime job names. That is the proposed sufficient matching class. It reuses the existing step matcher and requires no general graph solver.

Method review separates job association from the completeness of its command-step evidence. A uniquely discriminating source-defined name or ordered step witness may establish the job association while a different step remains absent, failed or skipped. Check the witness against the complete admitted competing job/variant set and other runtime records. Missing discriminators, unsupported competing origins or contradictory witnesses leave the affected association unresolved. The existing complete-step matcher supplies a sufficient fast path, while its workflow-wide early return cannot represent the selected per-variant result contract.

Preserve scoped association and per-step problem records separately. A missing install row receives no success from another row or variant. A skip with no step witnesses can use a separately admitted explicit source-defined name basis. An unnamed matrix skip retains its reported identity and skip outcome with unresolved variant assignment when the remaining evidence cannot establish that assignment.

A label-only guess, positional pairing or an unexplained tie is insufficient. If unsupported siblings could produce competing rows, preserve the unresolved correspondence. Missing and extra jobs, repeated IDs, duplicated witnesses, missing steps and conflicting source-defined names must be represented explicitly. A skipped job without steps may retain an existing independently earned name-based association, but receives no step-based association merely from the skip.

The observed default matrix display format can be retained for the reader and used as a diagnostic. Its undocumented formatting is unnecessary as a positive association premise in MapProxy. The human graph remains optional corroboration. A later case whose combinations share all admitted identity witnesses requires a separately qualified discriminator.

Record the association basis and witness references beside the runtime ID. Source-defined display correspondence uses GitHub's factual reports. It does not independently attest the running interpreter or installed package. The coordinated mutation of all display channels in the earlier diagnostic demonstrates the provider premise the method trusts. It is not evidence that a valid unmodified MapProxy workflow has competing matches, and by itself does not veto all reported-metadata correspondence. Preserve the original diagnostic and this qualification together.

### 6. Treat later sequential commands as a separate method extension

The current accepted rule admits a sole ordinary command and the first ordinary command of a sequential Bash/sh script. Specializing a matrix does not widen that rule.

For the MapProxy script, propose qualifying a later ordinary command when the selected GitHub Bash/sh execution profile establishes fail-fast behavior and the complete parsed script has a supported straight-line structure. The structural classifier must positively rule out early successful termination and changes to error handling before the target. It must account for shell builtins, functions, traps, status lists, pipes, nested/asynchronous control flow, and masked or dynamic behavior. Unsupported structures keep command execution unresolved even if the step reports success.

The probe demonstrated that Bash fail-fast stops after a failing target, while an earlier successful exit or disabled fail-fast can produce a successful script without the required target result. These are concrete defeaters for a broad later-command rule.

Before accepting the extension, characterize the AST-to-structure rule against the existing shell owner and the smallest meaningful defeater set. The proposed positive class should cover MapProxy's sequence of simple package-manager commands. Preserve the existing profile and continue-on-error checks. A failed step alone cannot identify which internal command failed. Keep package-manager and installed-state semantics with their existing owner.

The proposed structural contract requires a clean Bash/sh parse whose significant root statements are ordinary foreground commands. Executable atoms must be statically literal. Reject nested commands/substitutions, status operators, redirections and asynchronous syntax for the initial later-command class. Also reject shell-control builtins and declarations that can terminate, replace or modify the shell, change its environment/working directory or alter error handling. The finite shell language's builtin effects belong to the shell adapter, with an unresolved outcome for an unclassified effect. This is a structural/profile method under the same declared-process assumptions as the existing execution evidence. It adds no executable-path or package-version attestation.

The profile premise also covers material declared startup settings and inherited shell effects, not only script syntax. Method review's self-authored BASH_ENV controls produced successful shell outcomes after an early startup exit or an error trap, without the required target result. A visible startup override or other unresolved material shell effect must therefore block the stronger positive until its effect is established. Retain the boundary between a supported declared execution profile and independent observation of the actual process. Keep any resulting premise gap explicit across both the new and existing execution families.

The parser owns the whole-script structural relation and its blockers. The existing CI strengthening owner combines that relation with an admitted fail-fast Bash/sh profile, and the execution owner combines it with the matched step's factual outcome. Name the new relation separately from the already accepted first-command relation so historical evidence keeps its original meaning. A custom shell profile receives no new positive support. This proposal covers every position in the qualified sequence, preserving all four MapProxy contexts.

### 7. Preserve per-variant outcomes through aggregation and recovery

Associate a consumption and a following exercise only inside the same variant context. Evidence from one Python variant cannot complete a premise in another. Each context retains its own correspondence, observed status and command eligibility.

The existing aggregate's positive state means that admitted supported evidence exists. It must not be relabeled as all-combinations coverage. Present declared, associated and successful combinations with their individual failures and unknowns so a successful sibling cannot hide an incomplete matrix. Preserve reported rows even when semantic association remains unavailable.

Native storage retains the exact source, typed expansion and specialization provenance, correspondence witnesses, and semantic results needed for that view. Qualify cold reconstruction and older ordinary layouts through the existing codec/recovery owners. Saved-report reopening keeps the recorded method and observation horizon.

## Alternatives and trade-offs

| Alternative | Decision rationale |
| --- | --- |
| Specialize only one successful combination | Cannot meet the selected all-four-combination responsibility or reveal contrasting outcomes. |
| Replace the original YAML with generated workflow files or renamed job keys | Loses the actual job/source identity and gives generated spans a misleading original-file meaning. |
| Require an independent runtime coordinate attestation for every metadata-based claim | Adds an evidence requirement beyond reported correspondence. Use it when an interpreter or package-state proposition actually requires that observation. |
| Depend on the human graph immediately | Adds acquisition, markup and recovery qualification while leaving coordinates and multiline proof unresolved. The retained step witnesses discriminate this case. |
| Support a full GitHub expression evaluator and dynamic matrix executor | Adds input, scheduling and execution responsibilities beyond the retained evidence. Keep future admission tied to a concrete missing producer and consumer. |
| Add variant expansion while leaving downstream lookup unchanged | The probe demonstrates colliding command identities and source-span changes. That would risk attributing one job's result to another. |

## Design contract and adoption proof

The design chooses provider-owned specialization, explicit variant scope and source-defined reported correspondence. Its bounded initial contracts are the scalar/comparison class above, the existing ordered-step matcher with complete unique correspondence, and the proposed straight-line Bash/sh relation. The implementation plan should make the following proof obligations explicit.

1. Characterize the literal reader and direct-property syntax with quoted numbers, boolean/null values, homogeneous include/exclude rows and refusal controls for case collisions and mixed comparison kinds.
2. Use an immutable variant-context identity and a separate generated-script record. References carry scope through deduplication, step lookup and command recovery. Ordinary/historical records map explicitly to their prior context, and new codecs retain the association basis and generated-text provenance.
3. Challenge the later-command relation with early exit, fail-fast disabling, traps, sourced/evaluated text, shell context mutation, status masking, nested/asynchronous structures and custom profiles before it can promote MapProxy's second install command.

These are implementation/adoption proof dependencies, with the full four-combination result retained as the consumer. The private prototype is disposable diagnostic code. It establishes feasibility and exposes gaps, while product behavior remains owned by active source and tests.

Review this method if an admitted workflow has indistinguishable variants, unsupported runtime-generated matrix values, material scalar-conversion disagreement, or a real command outside the qualified sequential class. Broader static expansion and stronger runtime association can have different coverage, and their reasons must remain inspectable.

## Consequences and adoption

This proposal adds no dependency or external execution requirement. It extends the provider's optional interpretation responsibility and requires a coordinated identity migration across existing CI and recovery consumers. It retains the base static/runtime separation accepted in ADR-0008.

ADR-0009 and the first command-analysis implementation plan retain their accepted historical scope. The later-command direction above is accepted for qualification under this companion decision. Positive command support requires its structural and adversarial gates to pass. Architectural acceptance does not establish matrix product behavior or successful execution proof.

The [implementation and qualification plan](../../plans/LITERAL_MATRIX_CI_EVIDENCE_IMPLEMENTATION_AND_QUALIFICATION_PLAN.md) owns the dependency order, normal-entry-point proof and final completion gates. The live selection remains in MEMORY.md.
