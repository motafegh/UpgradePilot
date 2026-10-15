"""Native capture and historical projections for the evolving investigation Workspace.

Start with ``native_capture.NativeInvestigationCapture`` at the normal orchestration seam.
``checkpoint_revision.CheckpointRevision`` composes that native boundary with optional
``lifecycle_boundary.CapturedLifecycleHistory``. Explicit schema-2 stores retain both;
schema-1 checkpoints stay native-only. Typed lifecycle reconstruction is separate from
encoded storage inspection. ``lifecycle_host.InvestigationWorkspaceHost`` owns present
admission/intent/observation and native-owner feedback on the normal selected-read path;
``material_validity`` owns original-versus-current checks independently of predecessors.
Default in-process publication is volatile; a supplied schema-2 store makes it durable.
``preparation`` reuses the normal dependency/CI input owners without invoking models.
``source_access`` navigates frozen source bytes; ``consumer_access`` delivers bounded
source/native views and attributed citations through this same host. Actual delivery is
retained separately from acquisition, observable use and evaluated support.
This package preserves native owner results; it does not grant evaluation/action authority.
"""
