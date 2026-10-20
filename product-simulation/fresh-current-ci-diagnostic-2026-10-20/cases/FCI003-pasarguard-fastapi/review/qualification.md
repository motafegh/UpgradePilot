# FCI003 qualification

Classification: `qualified_as_unresolved_control`.

The FastAPI transition is frozen at `>=0.143.2` → `>=0.143.3` in `pyproject.toml`, with the matching lockfile transition preserved by the PR diff. The selected migration workflow has five completed jobs and GitHub currently returns non-empty step arrays for all five.

The workflow has no strategy/matrix, but none of its jobs has an explicit literal `name:`. Current correlation intentionally requires the static display name and must return unresolved/unsupported rather than assuming the YAML job key is the runtime display name. The workflow invokes `make setup-test`/`make test`; green jobs do not by themselves prove the exact FastAPI requirement was installed or exercised.
