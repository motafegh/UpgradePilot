"""Native capture and historical projections for the evolving investigation Workspace.

Start with ``native_capture.NativeInvestigationCapture`` at the normal orchestration seam.
``checkpoint_revision.CheckpointRevision`` composes that native boundary with optional
``lifecycle_boundary.CapturedLifecycleHistory``. Explicit schema-2 stores retain both;
schema-1 checkpoints stay native-only. Typed lifecycle reconstruction is separate from
encoded storage inspection. The normal execution host is a subsequent integration.
This package preserves native owner results; it does not grant evaluation/action authority.
"""
