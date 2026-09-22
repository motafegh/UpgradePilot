# S015 Post-Case Synthesis — Environment-Marker Applicability Before State Proof

**Date:** 2026-09-22
**Status:** Completed bounded synthesis; non-controlling Product Simulation evidence
**Scenario:** `scenarios/S015-charset-normalizer-marker-scoped-pytest/README.md`

## 1. Result

S015 establishes a real dependency-update boundary that sits upstream of B5:

`changed dependency source consumed` is insufficient unless the exact changed requirement is applicable to the selected runtime environment.

In the observed charset-normalizer matrix, the same exact requirements command succeeds under Python 3.9 while explicitly ignoring the proposed Python-3.8-only pytest requirement. Under Python 3.8, that requirement applies and causes installation failure.

## 2. Current-product consequence

Current UpgradePilot does not accidentally overclaim this case today because `requirements.py` rejects marker-decorated exact pins. The whole-line exact-pin regex accepts bare `package==version` only.

Therefore the current projection is:

`marker-scoped exact transition → unsupported source format → no normal exact DependencyVersionChange → B5 not reached`.

This is conservative and safe, but it is also a real supported-surface limitation rather than a hypothetical edge.

## 3. Future invariant if marker support is added

Marker parsing must not be implemented as only `strip marker, keep package/version`.

The marker is part of the proposition's applicability:

`package/version + marker + selected runtime environment → applicable requirement or non-applicable requirement`.

Only an applicable exact requirement may participate in the B5 source/environment premise for that runtime.

## 4. Matrix consequence

S015 also sharpens the G2/F4 matrix issue:

`static job key = tests` does not by itself identify one universal dependency proposition.

The same static job expands into rows where different requirements from the same source file apply. Therefore an eventual marker-aware state proof may need runtime/matrix-instance environment evidence, or it must remain unresolved when the required marker variables are not bound.

This does not require one product object per matrix row by definition; it does require the proof to avoid pretending the rows are equivalent.

## 5. B5 consequence

S015 validates P2 as an independent premise:

`exact source/environment relation` must establish not just that the file was named by the command, but that the exact changed requirement is active in that environment.

The Python 3.9 row proves why:

- file consumed: yes;
- command succeeded: yes;
- changed pytest 9.0.3 requirement active: no;
- therefore pytest 9.0.3 state proof from this row: no.

## 6. B5 asymmetry consequence

The Python 3.8 row fails on the applicable requirement. This blocks the command-derived positive state proposition.

It does not prove:

- pytest 9.0.3 was absent before command start;
- pytest was absent;
- another environment could not satisfy it;
- a negative package-state proposition.

This directly supports main's asymmetric rule: missing/failed positive command proof remains unresolved rather than becoming package absence.

## 7. Engineering-priority reality check

Unlike some synthetic B4 conflict shapes, marker-scoped requirements are plainly real in public Python dependency files and here occur in an untouched Dependabot proposal with an actual multi-version CI matrix.

That gives marker applicability stronger empirical priority than currently unobserved same-variable multi-write collision cases.

However, S015 alone does not establish how common marker-bearing Dependabot updates are. It establishes one high-consequence real instance and a concrete current limitation.

## 8. Main-thread handoff

Useful handoff:

1. Keep B5 P2 explicit; do not collapse it into file identity.
2. Record marker-bearing exact requirements as a real future source-support question.
3. If admitted, preserve marker provenance and evaluate applicability against justified environment evidence.
4. Do not let successful sibling matrix rows prove a marker-scoped version for another row.
5. Preserve command failure as unresolved state, not absence.

No source implementation is authorized by this scenario.

## 9. Stop

S015 is complete at the current depth. Reopen for marker-support design, matrix-instance environment proof, or implementation transfer only.