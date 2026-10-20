# FCI002 qualification

Classification: `qualified_as_unresolved_control`.

The exact tox transition is `>=4.61.1` → `>=4.64.4`. GitHub currently exposes non-empty runtime steps for the executed build/pre-commit/test jobs. The two tag-only publishing jobs are skipped and expose `steps: null`, retained explicitly as `field_absent_or_unavailable` rather than being converted to an empty array.

The static workflow contains both jobs without explicit literal display names and a `strategy.matrix` test job. Under the current correlation owner's actual validation order, the first expected refusal is `static_job_name_missing` on the first unnamed `pre-commit` job; the later matrix remains independently unsupported as `static_job_strategy_unsupported`. The correct behavior is therefore to remain unresolved rather than guess either a display name or matrix expansion/bijection.

The observed workflow also does not install `requirements.txt` or run tox. Successful pytest jobs therefore do not establish that the updated tox requirement was installed or exercised.
