# B2 Step 7F — Release-Index Client Integration Defect

**Date:** 2026-08-05  
**Status:** Fixed in product/test wiring; WSL validation and live rerun pending

## Observed normal-path failure

After the provenance-backed `Homepage` repository-association correction, the selected normal CLI proof was rerun:

```bash
time env -u GITHUB_TOKEN python -m upgradepilot pydantic/pydantic 13432
```

The application failed before release-index acquisition completed:

```text
AttributeError: 'PyPIReleaseClient' object has no attribute 'get_release_index'
```

The traceback identified `src/upgradepilot/investigation.py` as calling `get_release_index(...)` on the exact-release client.

## Root cause

`src/upgradepilot/pypi/release.py` intentionally has two separate concrete acquisition responsibilities:

```text
PyPIReleaseClient
→ get_release(package, version)

PyPIReleaseIndexClient
→ get_release_index(package)
```

Step 7E orchestration incorrectly reused `PyPIReleaseClient` for both operations. Existing application/Step 7F tests used one unrestricted `Mock`, so the mock accepted both method names and hid the concrete-client mismatch.

## Correction

`investigate_public_pull_request(...)` now accepts/creates a separate `PyPIReleaseIndexClient` and routes package-wide release-index acquisition only through it.

The focused application and Step 7F controlled tests now use:

```text
Mock(spec=PyPIReleaseClient)
Mock(spec=PyPIReleaseIndexClient)
```

as separate injected dependencies. This makes a future cross-responsibility method call fail deterministically instead of being silently accepted by a generic mock.

## Claim boundary

This correction changes orchestration ownership only. It does not change:

- package/version identity rules;
- crossed-release selection semantics;
- upstream repository authority;
- changelog authority;
- semantic model behavior;
- target-Python relevance;
- compatibility, safety, or recommendation policy.

## Required validation

Run focused application/Step 7F tests and the complete product regression, then rerun the selected normal-path S001 CLI proof. If the live path stops again, preserve the next exact boundary rather than bypassing it.
