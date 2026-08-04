"""Compatibility import for the GitHub provider API foundation.

New product code imports ``upgradepilot.github.api``. This flat path remains only until
all historical tests/tools have migrated during the source-structure reconciliation.
"""

from .github.api import *  # noqa: F401,F403
