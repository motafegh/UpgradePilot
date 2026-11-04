"""Explicit supported controls where historical ordinary acquisition is unavailable.

These are new authored fixtures over retained real source, not repaired historical
captures. Prefix identity metadata and package/tag/index observations are authored.
The curated rejection control also declares two minimal authored package reexport
bridges and selects only the earlier starlette sample. That is a labelled source
pressure, not a claim that ordinary acquisition reproduced the old curated input.
"""
from dataclasses import asdict, replace
from datetime import UTC, datetime
from hashlib import sha256
import json
from pathlib import Path

from experiments import api_call_signature_trial as curated
from retained_cases import RetainedCase, read
from upgradepilot.workspace.source_access import RetainedSourceCatalog, RetainedSourceFile


def prefix(target, files):
    path, head = next((path,text) for path,text in files.items() if path.endswith('.txt') and target.normalized_package.lower()+'==' in text.lower())
    proposed = next(line for line in head.splitlines() if line.lower().startswith(target.normalized_package.lower()+'=='))
    old = proposed.replace(target.proposed_version, target.old_version)
    description = "CONTROLLED retained-source qualification; original ordinary prefix not available."
    return dict(identity=dict(repository=target.repository, number=target.pull_number,
        title='Controlled retained-source qualification', state='open', merged=False, author='controlled-fixture',
        base_ref='controlled-base', base_sha=target.base_sha, head_ref='controlled-head', head_sha=target.head_sha, changed_files=1),
        changed_files=[dict(filename=path,status='modified',additions=1,deletions=1,changes=2,patch='-'+old+'\n+'+proposed)],
        dependency=dict(package=target.normalized_package,normalized_package=target.normalized_package,old_version=target.old_version,
            proposed_version=target.proposed_version,source_evidence=[dict(path=path,file_format='exact_requirement',extraction_method='changed_file_patch')],limitations=[]),
        source_contexts=[],
        description=dict(state='retained',text=description,source_url=f'https://api.github.com/repos/{target.repository}/pulls/{target.pull_number}',
            observed_at=datetime.now(UTC).isoformat(),utf8_bytes=len(description.encode()),content_sha256=sha256(description.encode()).hexdigest()))


def controlled_case(name, original, modules, catalog, metadata, authored_sources=()):
    scopes = {s.source_id:s for s in catalog.scopes}
    records = []
    for module in modules:
        if module['role']=='target':
            continue
        scope=scopes[module['source_id']]
        records.append(dict(state='module_examined',request=dict(package=module['package'],version=module['version'],module=module['module']),
            repository=scope.repository,revision=scope.revision,tag_commits={module['version']:scope.revision},
            metadata=dict(package=module['package'],version=module['version'],requirements=[dict(raw=r) for r in metadata.get(module['package'],())])))
    target=catalog.target
    target_files={f.path:f.content for f in catalog.files if (scopes[f.source_id].repository,scopes[f.source_id].revision)==(target.repository,target.head_sha)}
    native=prefix(target,target_files)
    acquisition=dict(native_inputs=native,ordinary_acquisition=dict(changed_package_sources=dict(attempts=records),adapter_exploration=dict(samples=[])),internal_module_requests=[])
    # RetainedCase.native_sources is intentionally not used for these controls:
    # actual clients will construct their own new controlled-observation receipts.
    body=dict(modules=modules,acquisition=acquisition)
    return RetainedCase(name, original.directory, original.hashes, body, catalog), dict(
        name=name,proof='explicit_control_not_historical_admission',original_case=original.name,
        original_hashes=original.hashes,authored_prefix=True,authored_metadata=metadata,authored_sources=list(authored_sources))


def glyphslib_control(original):
    modules=original.body['modules']
    # Original module roles/version identities and all code remain exact. The
    # missing provider metadata/prefix are authored and only qualify a control.
    return controlled_case('controlled-glyphslib-protocol',original,modules,original.catalog,{})


def rejection_control(root):
    evidence=root/'working-memory/evidence'
    index=read(evidence/'2026-10-28-caller-signature-build/inspection.json')
    hashes={n:v['sha256'] for n,v in index['private_saved_files'].items()}
    directory=Path.home()/'.local/share/upgradepilot/caller-signature-evidence/retained-httpx-2026-10-28/attempt-01'
    assert hashes=={n:sha256((directory/n).read_bytes()).hexdigest() for n in hashes}
    body,catalog=curated.open_comparison(directory)
    original=RetainedCase('curated-httpx-rejection',directory,hashes,body,catalog)
    scopes=tuple(s for s in catalog.scopes if s.source_id!='starlette-new')
    files=[f for f in catalog.files if f.source_id!='starlette-new']
    authored=[]
    for source in ('httpx-old','httpx-new'):
        file=RetainedSourceFile(source,'httpx/__init__.py','from ._client import Client\n')
        files.append(file)
        authored.append(dict(source_id=source,path=file.path,sha256=sha256(file.content.encode()).hexdigest(),
                             basis='authored minimal bridge; not retained original file'))
    catalog=RetainedSourceCatalog(scopes,tuple(files),target=catalog.target)
    modules=[]
    from upgradepilot.caller_signature.correspondence import module_name
    for file in files:
        if not file.path.endswith('.py'):
            continue
        sid=file.source_id
        role='target' if sid=='target-proposed' else 'native_old_version' if sid=='httpx-old' else 'native_proposed_version' if sid=='httpx-new' else 'constraint_sample'
        package='httpx' if sid.startswith('httpx-') else 'fastapi' if sid=='fastapi-reference' else 'starlette' if sid=='starlette-old' else ''
        version=catalog.target.old_version if sid=='httpx-old' else catalog.target.proposed_version if sid=='httpx-new' else '0.0.0+fixture' if package else ''
        dependencies=('starlette',) if package=='fastapi' else ('httpx',) if package=='starlette' else ()
        modules.append(dict(source_id=sid,path=file.path,module=module_name(file.path),package=package,version=version,role=role,dependencies=dependencies))
    return controlled_case('controlled-retained-httpx-rejection',original,modules,catalog,{'fastapi':['starlette'],'starlette':['httpx']},authored)
