"""Compatibility import for bounded workflow-command interpretation.

New product code imports ``upgradepilot.ci.workflow_commands``. This flat path remains
only while historical tests and tools migrate during source-structure reconciliation.
"""

from .ci.workflow_commands import *  # noqa: F401,F403
