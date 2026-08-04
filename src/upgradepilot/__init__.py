"""UpgradePilot application package.

Internal product code imports precise owning modules such as
``upgradepilot.github.pull_request`` or ``upgradepilot.dependency.change``. The package
root intentionally does not re-export provider clients, evidence records, problem
states, or implementation helpers.

Importing ``upgradepilot`` performs no network activity.
"""

__all__: tuple[str, ...] = ()
