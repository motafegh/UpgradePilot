# Resolve the source and runtime evidence boundary for RainbowChess redirect

November 28, 2026. Used the repository-audit and working-memory skills at the doing-only cadence. The [development review](2026-11-28_adapter-first-view-development-review.md) selected the [runtime applicability checkpoint](../plans/CALLER_SIGNATURE_NATIVE_ADOPTION_AND_QUALIFICATION_PLAN.md#16-combined-evidence-and-runtime-applicability-design-checkpoint) for one RainbowChess route. The maintainer question is whether the seven recorded fallback comparisons cover the Werkzeug call used on a normal request through the sampled Flask adapter.

## Exact case and alternate source path

RainbowChess PR #58 updates Werkzeug 3.1.7 to 3.1.8. The retained target head `68875f5b75082828447281d891107969ebcec0b1` registers `/newgame` for GET and POST in `main.py`. The handler calls `redirect('/play')` at line 49 if execution reaches its return. The installed report and exact Workspace reopen to the same 50 native comparisons and original source material. Both retain seven adapter paths across the target and abstention.

| Retained source | What it establishes |
| --- | --- |
| `source-18`, `main.py` | An app constructed as `Flask(__name__)` and the registered `/newgame` handler. |
| `source-25`, Flask `app.py` | `Flask` inherits `App` from `sansio.app` and has no local `redirect` override in the captured class. Its WSGI path pushes the request context before full dispatch and calls the selected view function. |
| `source-27` and `source-28`, Flask `ctx.py` and `globals.py` | Request-context push creates or reuses the matching app context. `current_app` is declared as a proxy to that context's `app` attribute. |
| `source-29`, Flask `helpers.py` | The helper delegates to `current_app.redirect` at line 268 if the proxy is truthy. The direct fallback at line 270 is the call in the seven paired witnesses. |
| `source-30`, Flask `sansio/app.py` | The sampled `App.redirect` declaration is at line 893. It calls the imported Werkzeug redirect at line 905 and passes `Response=self.response_class`. |

This source chain supports an app-context path under the sampled WSGI, proxy and inheritance assumptions. Exact Werkzeug proxy implementation text was outside this capture. The source establishes the branch structure and the distinct call site. It leaves the actual running receiver, imports and branch selection open. The difference in the supplied response class still matters to behavior, even where both signatures accept the same argument names.

## Isolate the missing relationship

The native worker analyzed every file in the table. At `helpers.py:268`, it retained `current_app.redirect` with unknown binding and `callable_relationship_unresolved`. It emitted neither a witness for the receiver call nor a witness for the downstream `sansio/app.py:905` call. At the selected `/newgame` root it retained one old and one proposed bound outcome for the direct fallback at `helpers.py:270`. The gap is call correspondence through the context proxy. The required Flask and exact Werkzeug signature texts are already present.

I used the installed local argument checker on explicitly selected native call and signature facts. The retained helper arguments fit `App.redirect` with one receiver assumed. The same check rejects without that assumption. At the downstream `sansio/app.py:905` call, both exact Werkzeug signatures bind and receive `code` and `Response` as named parameters. The two exact Werkzeug module files have identical text under their distinct revisions. These isolated checks establish local argument reception if the named calls reach the given signatures. They leave the ordinary product's correspondence gap and its original report intact.

## Applicability disposition

The retained exact commit points to a complete Git tree with 61 entries and ten workflow paths. The source-only report contains no workflow body, selected CI run, attempt or job, or matching execution trace. Its CI and runtime states remain `not evaluated`. A workflow inventory and declared dependency pin supply no process-level proof for this route. A package installation observation alone would also leave the dispatch question open.

Keep the bounded source-only opt-in and its conditional fallback claim. Defer app-proxy correspondence expansion and new runtime collection for this case. The additional source check finds the same local fit on the alternate call, and the retained evidence shows no decision-changing failure or observed cross-branch difference in argument fit. Reopen the applicability question when an exact-head, target-owned observation can join a representative request to the selected branch, the loaded receiver and the actual Werkzeug callee in the same process. Establish the loaded source identities and link them to the compared files. An observation of the app-context branch would select the alternate call and its own premises. An observation of the fallback with matching loaded source would support applying the existing witness to that execution. A mismatched or incomplete trace leaves it unresolved. Broader behavior and an upgrade-caused difference have separate proof requirements.

The [Product Decision Model](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md) owns applicability. Existing source correspondence owns the unresolved proxy relationship. A future branch observation would belong to target-owned runtime evidence. The command-completion package-state owner and the selected historical CI text reader each have narrower evidence contracts.

## Handoff

Pass this disposition to the [evidence-grounded AI design checkpoint](../plans/UPGRADEPILOT_90_DAY_PLAN.md#evidence-grounded-ai-design-checkpoint). The runtime limitation here is missing evidence. A retained-source explanation comparison could instead test whether an assistant finds and links the existing alternate-branch evidence while preserving the exact limits, against a deterministic report and direct-source baseline. Select a concrete reader task and evaluate whether the comparison is worth running before any inference work.

[Exact source, comparison and reopening receipt](evidence/2026-11-28-rainbowchess-redirect-applicability/verification.json)

`UP-SKILL:upgradepilot-repository-audit` · `UP-SKILL:upgradepilot-working-memory`
