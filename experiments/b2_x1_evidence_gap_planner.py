"""Historical import compatibility for the former B2/X1 planner model-boundary module.

Active implementation ownership moved to ``experiments.evidence_gap_planner_model_boundary``.
This narrow re-export exists only so preserved historical experiment/proof utilities can remain
runnable without rewriting their recorded provenance-oriented module names.
"""

from experiments.evidence_gap_planner_model_boundary import *  # noqa: F401,F403
