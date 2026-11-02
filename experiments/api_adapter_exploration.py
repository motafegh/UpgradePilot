"""Historical adapter trial imports; product owns exact sources and exploration."""
from upgradepilot.caller_signature.source_acquisition import (
    PackageDependencyMetadata, PackageDependencyMetadataClient as TrialDependencyMetadataClient,
    AdapterModuleSample, AdapterExploration, AdapterDiscoverySeed, PythonModuleSourceRequest,
    ExaminedPythonModule, PythonSourceAcquisitionWork, PythonSourceAcquisitionRun,
    select_exploration_version, AdapterSourceExplorer as ProductAdapterSourceExplorer,
)
from .api_change_source_acquisition import TrialPublicSession


class AdapterSourceExplorer(ProductAdapterSourceExplorer):
    def __init__(self, *, session=None, **providers):
        super().__init__(session=session or TrialPublicSession(), **providers)
