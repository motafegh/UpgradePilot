# Cross-profile real-PR qualification plan review

Reviewed November 12, 2026, at `296a9a4d`, synchronized with GitHub `main`. The [execution plan](../plans/CROSS_PROFILE_REAL_PR_END_TO_END_QUALIFICATION_EXECUTION_PLAN.md) is the review target. The [live position](../MEMORY.md), public CLI, capture tool, upstream model and report paths, historical receipts, and published AV-Tracer example supply the checks. This is a bounded review of a selected plan following Ali's review of the routes and model-activation boundary. It reuses that continuity and records findings here. The execution cycle retains its own A0/A1/A2 and authorization gates.

## Disposition

Keep the three routes and the order of work. Resolve the operational controls and tighten the acceptance checks before launching a live case. OpenCV tests the ordinary artifact route. Soup Sieve is an appropriate candidate for a fresh ordinary run that reaches the model if upstream prerequisites still hold. AV-Tracer supplies historical live evidence and a current offline reader check. The plan correctly preserves partial outcomes, defers a fourth PR and randomized sampling, and leaves target execution, broad usefulness and action permission outside the claim.

## Findings

### 1. Choose and prove the controls that govern each live invocation

Sections 4 and 8 propose hard request, byte and elapsed ceilings but defer choosing the enforcing mechanism. The ordinary [CLI](../src/upgradepilot/cli.py) exposes neither the proposed per-run acquisition limits nor a model-off option. An LM Studio event receipt can observe a request after it occurs. The existing [source-capture diagnostic](../tools/capture_report_sources.py) enforces GET/body limits, forbids POST and calls the application directly. It cannot supply either ordinary CLI proof or model-enabled capture unchanged. Q1's “0 expected” plus a later activation finding is insufficient if Q1 is admitted as zero-inference. Q2 needs invocation attribution as well as a count of requests the server received.

Freeze one invocation method and show, with controlled inputs before live work, which limits it actually enforces. Enforce zero admitted model POSTs for Q1 if zero inference is the agreed scope. For Q2, attribute the single admitted POST to the specific invocation and record attempt, response, timing and available usage. At the request boundary enforce the allowed host and method for each physical dispatch, including redirects. The [extractor](../src/upgradepilot/upstream/support_drop_extractor.py) disables ambient proxy inheritance, but its installed Requests session follows redirects by default. A loopback starting URL alone does not establish loopback-only traffic. A child deadline bounds the caller's lifetime. If it fires while inference is pending, record server completion or cancellation only when observed. Mark unsupported measurements unknown and distinguish soft observation limits from enforced scope. One narrow controlled launcher or observer is sufficient if it preserves the ordinary CLI path. No generic proxy or product framework is required by this finding.

### 2. Decide whether the normal-run freeze is an admission gate or a comparison check

Section 2 correctly notes that the ordinary CLI lacks `--expected-base` and `--expected-head`, but §6 describes head drift as an input stop. The ordinary route reads the PR again and can continue through upstream acquisition and model invocation before a saved-report comparison discovers drift. The existing GET-only diagnostic also compares identity after report projection. A read-only preflight and post-run match are valid evidence for an observed comparison. They do not constrain what the intervening run may investigate.

If Q2 authorization is tied to the exact frozen revision, bind the first real PR observation to that identity before downstream work or at least before model dispatch. The existing [input owner](../src/upgradepilot/investigation_inputs.py) shows the earlier check used by the opt-in profiles. If the owner instead admits one investigation of the named PR as it exists when acquired, record that scope explicitly and classify drifted results as ineligible for the frozen comparison. Preserve any resulting request, cost and artifact under the identity actually observed.

### 3. Split model dispatch, response handling and grounded-result acceptance

Section 5 allows a grounded, unresolved or rejected result to meet Q2's conditional proof. That is reasonable for invocation and outcome-handling coverage. Section 7's phrase “actually observed and qualified” can also be read as qualifying successful extraction and downstream grounding. The [upstream owner](../src/upgradepilot/upstream/support_drop.py) may stop at source-window construction before any POST. The adapter can yield unresolved results on transport, status or output parsing failures. A valid provider response can still produce a candidate the deterministic validator cannot ground. Correct rejection is evidence that a guard works.

Score upstream eligibility, actual request dispatch, usable provider response, deterministic grounding and target evaluation separately. A refused dispatch, a dispatched request with provider failure, a correctly rejected candidate and a grounded finding each prove different things. Require a source-verified grounded result and completed target evaluation for the stronger positive Q2 claim. Keep the historical Soup Sieve result as a comparison anchor. A rejection earns diagnosis of the first observed reason, which may be a correct validator decision rather than a validator defect.

### 4. Name the primary evidence that can actually be inspected

Q2 step 5 could imply that the report can show both the upstream quote and original target declaration offline. The [current report projector](../src/upgradepilot/report_projection.py) gives the target declaration a fact and exact locator but supplies no original text. I reproduced exit `7` for `--show-source source-29` on the historical successful Soup Sieve report. The tagged changelog and grounded quote are retained in that report. The target fact can be read offline, and the actual declaration needs an independently obtained exact-head file or a separately retained primary body.

Write the per-case proof rule before execution. For OpenCV, identify the release inventories that support the wheel-tag and source-distribution facts. For Soup Sieve, name the exact tagged source and target declaration. Prefer evidence from the same invocation when verifying what it consumed. A supplemental source-packet capture or later read is a separate observation. It can independently corroborate a result under matching identity and scope, with any temporal differences recorded. Preserve reference-only refusal as the expected behavior when original text was not saved.

### 5. Initialize the execution cycle record during A0

Plan §3 currently says to create the execution working-memory record “when activating B.” The [canonical cycle](../AGENTS.md) creates that record in A0, before the onboarding gates, with C active across the progression. Create or continue the single record there and preserve the existing A1/A2 stops. The previous AV-Tracer ownership gap can be resolved or explicitly carried as pending as the plan already permits.

## Checks and remaining uncertainty

- Verified all 10 local plan link targets. The current source, product tests and package manifest have no tracked changes since the combined AV-Tracer implementation at `42020f17`.
- Passed 31 focused CLI, semantic adapter and controlled end-to-end tests, plus 9 source-capture tests. Both published AV-Tracer reports and their selected source excerpts reopened in fresh guarded processes after archive checksum validation. This supplies current reader compatibility for Q3 and leaves its live proof at the earlier horizon.
- The corrected LM Studio endpoint, model key, 180-second configured timeout, 1,024 completion-token setting and 4,096-character source-window limit match current source. Live PR availability, actual model readiness and prospective request coverage remain preflight questions. This review performed no new target acquisition or model inference.
- Use one private run card per fresh case, or one manifest with one section per case, to close Findings 1–4. At publication, apply the existing [artifact rule](../docs/README.md#publishing-project-artifacts) to decide whether a reviewed exact report or archive is useful alongside the receipt. Keep reviewed originals locally.

`UP-SKILL:upgradepilot-repository-audit`
