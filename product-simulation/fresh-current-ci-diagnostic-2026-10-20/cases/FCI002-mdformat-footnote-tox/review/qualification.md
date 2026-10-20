# FCI002 qualification

Classification: `qualified_as_unresolved_control`.

The exact tox transition is `>=4.61.1` → `>=4.64.4`. GitHub currently exposes non-empty runtime steps for the executed build/pre-commit/test jobs. The two tag-only publishing jobs are skipped and expose `steps: null`, retained explicitly as `field_absent_or_unavailable` rather than being converted to an empty array.

The static workflow contains `strategy.matrix` for the test job and several jobs without explicit static display names. Current correlation must refuse this workflow rather than guess a matrix expansion/bijection. The observed workflow also does not install `requirements.txt` or run tox: successful pytest jobs therefore do not establish that the updated tox requirement was installed or exercised.
