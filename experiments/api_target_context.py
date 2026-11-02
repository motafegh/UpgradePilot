"""Historical target trial imports; product source acquisition owns behavior.

Trial defaults stay here. Native callers must provide their shared invocation
session, and native provider inventories do not depend on trial result types.
"""
from upgradepilot.github.repository import (
    RepositoryInventoryEntry as InventoryEntry, RepositoryInventory as TargetInventory,
    GitHubRepositoryInventoryClient, RepositoryInventoryProblem,
)
from upgradepilot.caller_signature.source_evidence import (
    AcquisitionProblem, SourceDependencyDeclaration as DependencyDeclaration,
    SourceImportCandidate as ImportDependencyCandidate, SourceContextGap as ContextGap,
)
from upgradepilot.caller_signature.bindings import ImportFact, ReferenceFact
from upgradepilot.target.source_context import (
    TargetSourceContext as TargetContext, TargetSourceAcquirer,
    source_id, extract_python_facts, extract_dependency_declarations, file_sha256,
)
from .api_change_source_acquisition import TrialPublicSession


class TrialRepositoryInventoryClient(GitHubRepositoryInventoryClient):
    def acquire(self, repository, revision):
        result = super().acquire(repository, revision)
        if isinstance(result, RepositoryInventoryProblem):
            return AcquisitionProblem("inventory", result.reason, result.detail, result.status_code)
        return result


class TargetContextAcquirer(TargetSourceAcquirer):
    def __init__(self, *, session=None, inventory=None, files=None):
        super().__init__(session=session or TrialPublicSession(), inventory=inventory, files=files)
