"""Declared-source association, metadata and native module receipt production.

Provider controls are authored observations, never live availability or installed
namespace proof. Native receipts must retain actual successful premises and
honest partial failures without changing the qualified source/question cache.
"""
import json
from dataclasses import replace
from datetime import UTC, datetime
from unittest import TestCase
from unittest.mock import Mock

from upgradepilot.caller_signature.source_acquisition import (
    AcquisitionProblem, DeclaredSourceAssociation, PublisherProvenanceInspection,
    PublisherProvenanceInspector, associate_declared_source,
    AdapterSourceExplorer, PythonModuleSourceRequest, ExaminedPythonModule,
    PackageDependencyMetadata, PackageDependencyMetadataClient as TrialDependencyMetadataClient,
    select_exploration_version,
)
from upgradepilot.caller_signature.source_evidence import SourceDependencyDeclaration as DependencyDeclaration
from upgradepilot.pypi.release import (PackageReleaseEvidence, PackageReleaseIndexEvidence,
    ProjectUrlCandidate)

NOW = datetime(2026, 10, 4, tzinfo=UTC)
SHA = "a" * 40

def release(version="2.0", links=None):
    return PackageReleaseEvidence(
        "demo",
        "demo",
        version,
        "demo",
        version,
        "https://pypi.org/pypi/demo/" + version + "/json",
        NOW,
        1,
        (),
        tuple(
            links
            if links is not None
            else [ProjectUrlCandidate("Source Code", "https://github.com/owner/demo")]
        ),
    )

def absent(state="source_unavailable"):
    return PublisherProvenanceInspection(state, "provider reason")

class AssociationTests(TestCase):
    def test_explicit_declaration_retains_ignored_links_and_absence(self):
        item = release(
            links=[
                ProjectUrlCandidate("Source Code", "https://github.com/owner/demo.git"),
                ProjectUrlCandidate("Homepage", "https://example.com"),
            ]
        )
        result = associate_declared_source(item, absent())
        self.assertIsInstance(result, DeclaredSourceAssociation)
        self.assertEqual(result.repository, "owner/demo")
        self.assertEqual(result.ignored_links, (item.project_urls[1],))
        self.assertEqual(result.provenance.state, "source_unavailable")

    def test_adverse_provenance_never_falls_back(self):
        for state in [
            "identity_mismatch",
            "ambiguous_source",
            "malformed_response",
            "acquisition_failed",
            "unsupported_source",
        ]:
            with self.subTest(state=state):
                result = associate_declared_source(release(), absent(state))
                self.assertEqual(result.reason, state)
                self.assertEqual(result.evidence.state, state)

    def test_homepage_and_unsafe_declarations_do_not_enable_examination(self):
        cases = [
            ("Homepage", "https://github.com/owner/demo"),
            ("Source", "http://github.com/owner/demo"),
            ("Source", "https://token@github.com/owner/demo"),
            ("Source", "https://github.com/owner/demo/tree/main"),
            ("Source", "https://127.0.0.1/owner/demo"),
            ("Source", "https://github.com/owner/demo?x=1"),
        ]
        for label, url in cases:
            with self.subTest(url=url):
                self.assertIsInstance(
                    associate_declared_source(
                        release(links=[ProjectUrlCandidate(label, url)]), absent()
                    ),
                    AcquisitionProblem,
                )

    def test_conflicting_declarations_retained(self):
        result = associate_declared_source(
            release(
                links=[
                    ProjectUrlCandidate("Source", "https://github.com/a/b"),
                    ProjectUrlCandidate("Repository", "https://github.com/c/d"),
                ]
            ),
            absent(),
        )
        self.assertEqual(result.reason, "conflicting_declarations")
        self.assertEqual(len(result.evidence[0]), 2)

class PublisherInspectionTests(TestCase):
    def test_publisher_inspection_is_independent_of_homepage_labels(self):
        from upgradepilot.caller_signature.source_acquisition import (
            PublisherProvenanceInspector,
        )
        from upgradepilot.pypi.provenance import FileProvenanceProblem
        from upgradepilot.pypi.release import DistributionFile

        item = replace(
            release(
                links=[
                    ProjectUrlCandidate("Source", "https://github.com/owner/demo"),
                    ProjectUrlCandidate("Homepage", "https://example.org"),
                ]
            ),
            distribution_files=(
                DistributionFile(
                    "demo.whl",
                    "https://files.pythonhosted.org/demo.whl",
                    "a" * 64,
                    "bdist_wheel",
                ),
            ),
        )
        client = Mock()
        client.get_file_provenance.return_value = FileProvenanceProblem(
            "provenance_unavailable",
            "demo",
            "2.0",
            "demo.whl",
            "https://pypi.org/integrity/demo/2.0/demo.whl/provenance",
            "absent",
        )
        inspected = PublisherProvenanceInspector(client=client).resolve(item)
        result = associate_declared_source(item, inspected)
        self.assertIsInstance(result, DeclaredSourceAssociation)
        self.assertEqual(result.ignored_links[0].label, "Homepage")
        self.assertEqual(len(inspected.records), 1)

    def test_mixed_conflicting_and_malformed_publisher_evidence_blocks(self):
        from upgradepilot.caller_signature.source_acquisition import (
            PublisherProvenanceInspector,
        )
        from upgradepilot.pypi.provenance import (
            FileProvenanceEvidence,
            PublisherIdentity,
        )
        from upgradepilot.pypi.release import DistributionFile

        item = replace(
            release(),
            distribution_files=(
                DistributionFile(
                    "demo.whl",
                    "https://files.pythonhosted.org/demo.whl",
                    "a" * 64,
                    "bdist_wheel",
                ),
            ),
        )
        for publishers in (
            (PublisherIdentity("GitHub", "wrong/repo", None),),
            (
                PublisherIdentity("GitHub", "owner/demo", None),
                PublisherIdentity("other", None, None),
            ),
            (PublisherIdentity("GitHub", None, None),),
        ):
            with self.subTest(publishers=publishers):
                client = Mock()
                client.get_file_provenance.return_value = FileProvenanceEvidence(
                    "demo",
                    "2.0",
                    "demo.whl",
                    "a" * 64,
                    "https://pypi.org/integrity/demo/2.0/demo.whl/provenance",
                    NOW,
                    1,
                    1,
                    publishers,
                )
                inspected = PublisherProvenanceInspector(client=client).resolve(item)
                self.assertIsInstance(
                    associate_declared_source(item, inspected), AcquisitionProblem
                )

def declaration(package, source="requirements.txt", specifier=">=1", marker=None):
    return DependencyDeclaration(
        source,
        "L1",
        package + specifier,
        package,
        specifier,
        (),
        marker,
        "requirements",
    )

def index(package, versions=("1.0", "2.0")):
    return PackageReleaseIndexEvidence(
        package,
        package,
        package,
        "https://pypi.org/pypi/" + package + "/json",
        NOW,
        1,
        versions,
    )

class SamplingTests(TestCase):
    def test_latest_stable_constraint_is_sampling_not_resolved_version(self):
        result = select_exploration_version(
            index("bridge", ("1.0", "1.5", "2.0rc1", "2.0")),
            declaration("bridge", specifier="<2"),
        )
        self.assertEqual(result, "1.5")
        result = select_exploration_version(
            index("bridge", ("2", "2.0")), declaration("bridge")
        )
        self.assertIsInstance(result, AcquisitionProblem)

class MetadataTests(TestCase):
    def client(self, info):
        session = Mock()
        response = Mock()
        response.status_code = 200
        response.headers = {}
        response.iter_content.return_value = [json.dumps({"info": info}).encode()]
        session.get.return_value = response
        return TrialDependencyMetadataClient(session=session)

    def test_conditions_and_extra_markers_remain_unresolved_declarations(self):
        result = self.client(
            {
                "name": "bridge",
                "version": "2.0",
                "requires_dist": [
                    'mediator>=2; python_version < "3.12"',
                    'vendor[fast]; extra == "standard"',
                ],
            }
        ).acquire("bridge", "2.0")
        self.assertEqual(result.requirements[0].marker, 'python_version < "3.12"')
        self.assertEqual(result.requirements[1].extras, ("fast",))
        self.assertEqual(result.requirements[1].marker, 'extra == "standard"')

    def test_wrong_identity_bad_array_and_direct_url_do_not_become_relations(self):
        cases = [
            {"name": "another", "version": "2.0", "requires_dist": []},
            {"name": "bridge", "version": "2.0", "requires_dist": "vendor"},
        ]
        for info in cases:
            self.assertIsInstance(
                self.client(info).acquire("bridge", "2.0"), AcquisitionProblem
            )
        result = self.client(
            {
                "name": "bridge",
                "version": "2.0",
                "requires_dist": ["vendor @ https://token@example.org/file.whl"],
            }
        ).acquire("bridge", "2.0")
        self.assertFalse(result.requirements)
        self.assertEqual(result.gaps[0].reason, "direct_url_not_followed")


class NativeModuleReceiptTests(TestCase):
    def owner(self):
        from upgradepilot.caller_signature.acquisition import AcquisitionPolicy, AcquisitionSession
        from upgradepilot.github.repository import RepositoryInventory, RepositoryInventoryEntry, RepositoryTextFile
        from upgradepilot.github.tag import GitHubTagCommitEvidence
        session = AcquisitionSession(policy=AcquisitionPolicy())
        releases, metadata, tags, inventory, files = (Mock() for _ in range(5))
        releases.get_release.side_effect = lambda package, version: release(version)
        metadata.acquire.side_effect = lambda package, version: PackageDependencyMetadata(
            package, version, 'https://pypi.org/pypi/' + package + '/' + version + '/json', (), ())
        tags.resolve_tag_to_commit.side_effect = lambda repo, tag: GitHubTagCommitEvidence(
            repo, tag, 'refs/tags/' + tag, 'commit', ('c' if tag.lstrip('v') == '1.0' else 'd') * 40,
            ('c' if tag.lstrip('v') == '1.0' else 'd') * 40, (), NOW)
        inventory.acquire.side_effect = lambda repo, sha: RepositoryInventory(repo, sha, 'e' * 40,
            (RepositoryInventoryEntry('demo/api.py', 'blob', '100644'),), False)
        files.get_exact_commit_text_file.side_effect = lambda repo, sha, path: RepositoryTextFile(
            repo, path, sha, 'def send(*, option=None):\n pass\n')
        return AdapterSourceExplorer(session=session, releases=releases, metadata=metadata,
            tags=tags, inventory=inventory, files=files)

    def question(self, version='1.0', basis='native_old_version'):
        return PythonModuleSourceRequest('demo', version, 'demo.api', basis)

    def retained(self, run, *receipts):
        from upgradepilot.caller_signature import source_evidence as se
        from upgradepilot.caller_signature.evidence import AnalysisLimits
        from upgradepilot.caller_signature.source_codec import encode_sources, decode_sources
        receipt = se.SourceAcquisitionReceipt('controlled_observation', 'partial', NOW, None,
            tuple(receipts), (), (), (), (), (), (), (), run.work, None, (), ('transport_receipt_unavailable',))
        sources = se.CallerSignatureSources(None, (), AnalysisLimits(), receipt)
        restored = decode_sources(encode_sources(sources))
        self.assertEqual(restored, sources)
        self.assertIsNone(restored.analysis_input())
        return restored

    def test_exact_native_receipts_preserve_full_premises_and_cached_question_basis(self):
        owner = self.owner()
        run = owner.source_run()
        old, old_receipt = run.examine_with_receipt(self.question())
        new, new_receipt = run.examine_with_receipt(self.question('2.0', 'native_proposed_version'))
        again, again_receipt = run.examine_with_receipt(self.question(basis='explicit_version'))
        self.assertEqual((old_receipt.request.version_basis, new_receipt.request.version_basis,
                          again_receipt.request.version_basis), ('old_dependency', 'proposed_dependency', 'explicit_version'))
        self.assertEqual(old_receipt.association, old.association)
        self.assertEqual(new_receipt.tags, new.tags)
        self.assertEqual(old_receipt.metadata, old.metadata)
        self.assertEqual(old_receipt.state, 'module_examined')
        self.assertEqual(old_receipt.provenance_state, 'source_unavailable')
        self.assertFalse(old_receipt.retention_gaps)
        self.assertIs(old.file, again.file)
        self.assertEqual((owner.releases.get_release.call_count, owner.tags.resolve_tag_to_commit.call_count,
            owner.inventory.acquire.call_count, owner.files.get_exact_commit_text_file.call_count), (2, 4, 2, 2))
        self.assertEqual(run.work.module_attempts, 2)
        self.retained(run, old_receipt, new_receipt, again_receipt)

    def test_failed_file_keeps_prior_actual_premises_without_admitting_text_or_retry(self):
        from upgradepilot.github.api import GitHubAcquisitionError
        owner = self.owner()
        owner.files.get_exact_commit_text_file.side_effect = GitHubAcquisitionError('authored outage', reason='transport_error')
        run = owner.source_run()
        outcome, receipt = run.examine_with_receipt(self.question())
        before = run.release_observations
        again, repeated = run.examine_with_receipt(self.question())
        self.assertIsInstance(outcome, AcquisitionProblem)
        self.assertIs(again, outcome)
        self.assertEqual(repeated, receipt)
        self.assertEqual(owner.files.get_exact_commit_text_file.call_count, 1)
        self.assertEqual((receipt.state, receipt.problem.reason), ('unavailable', 'transport_error'))
        self.assertIsNotNone(receipt.association)
        self.assertIsNotNone(receipt.metadata)
        self.assertEqual(len(receipt.tags), 2)
        self.assertEqual((receipt.repository, receipt.revision, receipt.path), ('owner/demo', 'c' * 40, 'demo/api.py'))
        self.assertIsNone(receipt.sha256)
        self.assertIsNone(receipt.utf8_bytes)
        self.assertEqual(before, run.release_observations)
        self.retained(run, receipt)

    def test_metadata_failure_preserves_release_association_and_caches_refusal(self):
        owner = self.owner()
        owner.metadata.acquire.side_effect = None
        owner.metadata.acquire.return_value = AcquisitionProblem('adapter_metadata', 'identity_mismatch', 'Controlled wrong version')
        run = owner.source_run()
        outcome, receipt = run.examine_with_receipt(self.question())
        snapshot = run.release_observations
        run.examine_with_receipt(self.question())
        self.assertEqual(receipt.problem.reason, 'identity_mismatch')
        self.assertIsNotNone(snapshot[0].release)
        self.assertIsNotNone(receipt.association)
        self.assertIsNone(receipt.metadata)
        owner.tags.resolve_tag_to_commit.assert_not_called()
        owner.files.get_exact_commit_text_file.assert_not_called()
        self.assertEqual(owner.metadata.acquire.call_count, 1)
        self.retained(run, receipt)

    def test_adverse_publisher_is_preserved_live_and_partial_retention_gap_is_explicit(self):
        owner = self.owner()
        owner.provenance = Mock()
        owner.provenance.resolve.return_value = PublisherProvenanceInspection('identity_mismatch', 'Controlled conflict', 'other/repository')
        run = owner.source_run()
        outcome, receipt = run.examine_with_receipt(self.question())
        progress = run.release_observations[0]
        self.assertEqual(progress.publisher.repository, 'other/repository')
        self.assertEqual(progress.problem.reason, 'identity_mismatch')
        self.assertIsNone(receipt.association)
        self.assertEqual(receipt.problem.reason, 'identity_mismatch')
        self.assertIn('publisher_observation_available_in_run_only', receipt.retention_gaps)
        owner.metadata.acquire.assert_not_called()
        owner.files.get_exact_commit_text_file.assert_not_called()
        self.retained(run, receipt)

    def test_source_byte_refusal_retains_observed_size_without_inventing_a_hash(self):
        owner = self.owner()
        run = owner.source_run(max_bytes=1)
        outcome, receipt = run.examine_with_receipt(self.question())
        self.assertEqual((receipt.state, receipt.problem.reason), ('refused', 'source_text_limit'))
        self.assertGreater(receipt.utf8_bytes, 1)
        self.assertIsNone(receipt.sha256)
        self.assertEqual(run.work.source_bytes, 0)
        run.examine_with_receipt(self.question())
        self.assertEqual(owner.files.get_exact_commit_text_file.call_count, 1)
        self.retained(run, receipt)


class NativeSourceClientCompositionTests(TestCase):
    def test_normal_profile_reaches_forwarding_after_earlier_unrelated_samples(self):
        """Two sample chains exercise the ordinary allocation, without case/path selectors.

        The first chain does not reach the changed dependency. The second does,
        through two adapter hops. A two-candidate default silently loses the
        supported native pair even though all global/source budgets can admit it.
        """
        import base64
        from contextlib import redirect_stdout
        from hashlib import sha256
        from io import BytesIO, StringIO
        from pathlib import Path
        from tempfile import TemporaryDirectory
        from urllib.parse import parse_qs, urlsplit
        from requests import Response
        from requests.adapters import BaseAdapter
        from test_github_client import _identity, _pull_request_payload, _changed_file
        from upgradepilot.caller_signature.acquisition import AcquisitionSession
        from upgradepilot.cli import main
        from upgradepilot.report_file import read_report
        from unittest.mock import patch

        identity = _identity(repository="owner/target", changed_files=1, head_sha="a"*40, base_sha="b"*40)
        versions = {("vendor", "1.0"): "c"*40, ("vendor", "2.0"): "d"*40,
                    ("toolkit", "1.0"): "e"*40, ("relay", "1.0"): "f"*40}
        contents = {
            ("owner/target", "a"*40): {"requirements.txt": "vendor==2.0\ntoolkit\n",
                "app.py": "from toolkit.assets import Resource\nfrom toolkit.client import send\nResource()\nsend(option=1)\n"},
            ("owner/vendor", "c"*40): {"vendor/api.py": "def send(*, option=None):\n pass\n"},
            ("owner/vendor", "d"*40): {"vendor/api.py": "def send(*, replacement=None):\n pass\n"},
            ("owner/toolkit", "e"*40): {"toolkit/assets.py": "from relay.assets import Resource\n",
                                       "toolkit/client.py": "from relay.client import send\n"},
            ("owner/relay", "f"*40): {"relay/assets.py": "class Resource:\n pass\n",
                                     "relay/client.py": "from vendor.api import send\n"},
        }
        trees = {key: sha256(repr(key).encode()).hexdigest()[:40] for key in contents}
        requests = []
        class Transport(BaseAdapter):
            def send(self, request, **kwargs):
                requests.append(request)
                parsed = urlsplit(request.url)
                path = parsed.path
                if path == "/repos/owner/target/pulls/1145":
                    payload = dict(_pull_request_payload(identity), body="Controlled adapter allocation.")
                elif path == "/repos/owner/target/pulls/1145/files":
                    payload = [dict(_changed_file(1, repository=identity.repository, head_sha=identity.head_sha, filename="requirements.txt"), patch="-vendor==1.0\n+vendor==2.0")]
                elif parsed.hostname == "pypi.org":
                    bits = path.strip('/').split('/')
                    package = bits[1]
                    if len(bits) == 3:
                        payload = dict(info=dict(name=package), releases={"1.0": []}, last_serial=1)
                    else:
                        version = bits[2]
                        assert (package, version) in versions
                        requirements = {"toolkit": ["relay"], "relay": ["vendor"]}.get(package, [])
                        payload = dict(info=dict(name=package, version=version, requires_dist=requirements,
                            project_urls={"Source": "https://github.com/owner/"+package}), urls=[], last_serial=1)
                else:
                    repo = '/'.join(path.split('/')[2:4])
                    suffix = '/'.join(path.split('/')[4:])
                    if suffix.startswith('git/ref/tags/'):
                        tag = suffix.removeprefix('git/ref/tags/')
                        revision = versions[repo.split('/')[-1], tag.removeprefix('v')]
                        payload = dict(ref='refs/tags/'+tag, object=dict(type='commit', sha=revision))
                    elif suffix.startswith('git/commits/'):
                        revision = suffix.rsplit('/',1)[-1]
                        payload = dict(sha=revision, tree=dict(sha=trees[repo,revision]))
                    elif suffix.startswith('git/trees/'):
                        tree = suffix.rsplit('/',1)[-1]
                        key = next(key for key,value in trees.items() if key[0]==repo and value==tree)
                        payload = dict(sha=tree, truncated=False, tree=[dict(path=p,type='blob',mode='100644') for p in sorted(contents[key])])
                    else:
                        assert suffix.startswith('contents/')
                        filename = suffix.removeprefix('contents/')
                        revision = parse_qs(parsed.query)['ref'][0]
                        content = contents[repo,revision][filename]
                        payload = dict(type='file',path=filename,encoding='base64',content=base64.b64encode(content.encode()).decode())
                response = Response()
                response.status_code, response.raw = 200, BytesIO(json.dumps(payload).encode())
                response.request, response.url = request, request.url
                return response
            def close(self):
                pass
        def controlled_session(**kwargs):
            session = AcquisitionSession(**kwargs)
            session.mount('https://', Transport())
            return session
        with TemporaryDirectory(prefix='upgradepilot-adapter-allocation-') as tmp:
            path = Path(tmp)/'report.json'
            output = StringIO()
            with patch('upgradepilot.cli.AcquisitionSession', side_effect=controlled_session), patch('socket.socket.connect', side_effect=AssertionError('No live provider')), redirect_stdout(output):
                code = main([identity.repository,str(identity.number),'--evidence-profile','caller-signature','--save-report',str(path)])
            self.assertEqual(code,0,(output.getvalue(),[r.url for r in requests]))
            report = read_report(path)
        native = [a for a in report.assessments if any(f.name=='role' and f.value in {'old_dependency','proposed_dependency'} for f in a.facts)]
        self.assertEqual({a.state for a in native},{'bound','rejected'})
        self.assertEqual(len({f.value for a in native for f in a.facts if f.name=='root_call_id'}),1)
        self.assertLessEqual(len(requests),100)
        self.assertLessEqual(sum(urlsplit(r.url).hostname=='api.github.com' for r in requests),50)
        self.assertEqual(sum('/pulls/1145' in r.url for r in requests),3)

    def controlled_transport(self, *, proposed_missing=False, forwarded=False, target_object_id_length=40):
        import base64
        from urllib.parse import parse_qs, urlsplit
        from requests import Response
        from requests.adapters import BaseAdapter
        from io import BytesIO
        from test_github_client import _identity, _pull_request_payload, _changed_file
        from upgradepilot.caller_signature.acquisition import AcquisitionPolicy, AcquisitionSession

        head, base = 'a' * target_object_id_length, 'b' * target_object_id_length
        identity = _identity(repository='owner/target', changed_files=1, head_sha=head, base_sha=base)
        trees = {head: 'e' * target_object_id_length, 'c' * 40: 'f' * 40, 'd' * 40: '1' * 40}
        dispatched = []

        class Transport(BaseAdapter):
            def send(self, request, **kwargs):
                dispatched.append(request)
                parsed = urlsplit(request.url)
                path = parsed.path
                if path == '/repos/owner/target/pulls/1145':
                    payload = {**_pull_request_payload(identity), 'body': 'Controlled demo update'}
                elif path == '/repos/owner/target/pulls/1145/files':
                    changed = _changed_file(1, repository=identity.repository, head_sha=head, filename='requirements.txt')
                    payload = [{**changed, 'patch': '-demo==1.0\n+demo==2.0'}]
                elif parsed.hostname == 'pypi.org' and path in {'/pypi/demo/1.0/json', '/pypi/demo/2.0/json'}:
                    version = path.split('/')[-2]
                    payload = dict(info=dict(name='demo', version=version, requires_dist=[],
                        project_urls={'Source': 'https://github.com/owner/demo'}), urls=[], last_serial=1)
                elif '/git/ref/tags/' in path:
                    tag = path.rsplit('/', 1)[-1]
                    revision = ('c' if tag.lstrip('v') == '1.0' else 'd') * 40
                    payload = dict(ref='refs/tags/' + tag, object=dict(type='commit', sha=revision))
                elif '/git/commits/' in path:
                    revision = path.rsplit('/', 1)[-1]
                    payload = dict(sha=revision, tree=dict(sha=trees[revision]))
                elif '/git/trees/' in path:
                    tree = path.rsplit('/', 1)[-1]
                    paths = ('app.py', 'requirements.txt') if tree == trees[head] else ('demo/api.py',)
                    if forwarded and tree != trees[head]:
                        paths += ('demo/_core.py',)
                    payload = dict(sha=tree, truncated=False,
                        tree=[dict(path=p, type='blob', mode='100644') for p in paths])
                elif '/contents/' in path:
                    file_path = path.split('/contents/', 1)[1]
                    revision = parse_qs(parsed.query)['ref'][0]
                    if file_path == 'requirements.txt':
                        content = 'demo==2.0\n'
                        assert revision == head
                    elif file_path == 'app.py':
                        content = 'from demo.api import send\nsend(option=1)\n'
                        assert revision == head
                    elif forwarded and file_path == 'demo/_core.py':
                        assert revision in {'c' * 40, 'd' * 40}
                        keyword = 'option' if revision == 'c' * 40 else 'replacement'
                        content = f'def send(*, {keyword}=None):\n pass\n'
                    else:
                        assert file_path == 'demo/api.py' and revision in {'c' * 40, 'd' * 40}
                        content = 'def send(*, option=None):\n pass\n'
                        if forwarded:
                            content = 'from ._core import send\n'
                    payload = dict(type='file', path=file_path, encoding='base64',
                        content=base64.b64encode(content.encode()).decode())
                else:
                    raise AssertionError('Unexpected hidden request: ' + request.url)
                response = Response()
                response.status_code = 404 if (
                    proposed_missing and '/contents/demo/api.py' in path
                    and parse_qs(parsed.query).get('ref') == ['d' * 40]
                ) else 200
                response.raw = BytesIO(json.dumps(payload).encode())
                response.request, response.url = request, request.url
                return response

            def close(self):
                pass

        session = AcquisitionSession(policy=AcquisitionPolicy(), clock=lambda: 0.0)
        session.mount('https://', Transport())
        return identity, session, dispatched

    def test_actual_clients_share_prefix_target_and_exact_version_acquisition(self):
        from unittest.mock import patch
        from upgradepilot.github.pull_request import GitHubPullRequestClient
        from upgradepilot.github.repository import GitHubRepositoryClient
        from upgradepilot.investigation_inputs import acquire_dependency_inputs
        from upgradepilot.target.source_context import TargetSourceAcquirer

        identity, session, dispatched = self.controlled_transport()
        base, head = identity.base_sha, identity.head_sha
        with patch('socket.socket.connect', side_effect=AssertionError('No live provider')):
            with session.stage('dependency_inputs'):
                inputs = acquire_dependency_inputs(identity.repository, identity.number,
                    GitHubPullRequestClient(session=session), GitHubRepositoryClient(session=session),
                    expected_base=base, expected_head=head)
            with session.stage('target_context', reserve_github=session.policy.source_request_reserve):
                context = TargetSourceAcquirer(session=session).acquire(inputs.identity.repository,
                    inputs.identity.head_sha, changed_paths=tuple(f.filename for f in inputs.changed_files),
                    max_file_attempts=session.policy.target_file_attempts)
            owner = AdapterSourceExplorer(session=session)
            run = owner.source_run()
            with session.stage('source_closure'):
                old, old_receipt = run.examine_with_receipt(PythonModuleSourceRequest('demo', inputs.dependency.old_version,
                    context.candidates[0].imported_module, 'native_old_version', context.references[0]))
                new, new_receipt = run.examine_with_receipt(PythonModuleSourceRequest('demo', inputs.dependency.proposed_version,
                    context.candidates[0].imported_module, 'native_proposed_version', context.references[0]))
        self.assertIs(owner.session, session)
        self.assertEqual((inputs.identity.base_sha, inputs.identity.head_sha), (base, head))
        self.assertEqual([f.path for f in context.files], ['requirements.txt', 'app.py'])
        self.assertEqual((old.file.revision, new.file.revision), ('c' * 40, 'd' * 40))
        self.assertEqual((old_receipt.request.version_basis, new_receipt.request.version_basis), ('old_dependency', 'proposed_dependency'))
        self.assertIs(old_receipt.request.origin, context.references[0])
        transport = session.acquisition_receipt()
        self.assertEqual((transport.github_requests, transport.provider_requests, len(dispatched)), (17, 21, 21))
        self.assertEqual([x.provider_requests for x in transport.requests], list(range(1, 22)))
        self.assertEqual([x.stage for x in transport.requests], ['dependency_inputs'] * 3 + ['target_context'] * 4 + ['source_closure'] * 14)
        self.assertEqual(sum('/pulls/1145' in r.path for r in transport.requests), 3)

    def test_application_publishes_partial_source_progress_before_analysis(self):
        import subprocess
        import sys
        from dataclasses import asdict
        from tempfile import TemporaryDirectory
        from pathlib import Path
        from unittest.mock import patch
        from upgradepilot.investigation import investigate_caller_signature_progress
        from upgradepilot.workspace.checkpoint_store import CheckpointStore
        from upgradepilot.workspace.lifecycle_host import InvestigationWorkspaceHost
        from upgradepilot.workspace.native_projection import reconstruct_caller_signature_projection

        identity, session, dispatched = self.controlled_transport(proposed_missing=True)
        with TemporaryDirectory() as tmp:
            store = CheckpointStore.create(Path(tmp) / 'store', schema_version=2)
            host = InvestigationWorkspaceHost(store=store, lineage_id='source-progress')
            source_revisions = []

            def fail_after_source_publication(analysis_input):
                saved = store.read_revision(
                    host.lineage_id, host.current.revision_id,
                    expected_target=analysis_input.catalog.target,
                ).revision
                source_revisions.append(saved)
                projection = reconstruct_caller_signature_projection(
                    saved.boundary, expected_target=analysis_input.catalog.target,
                )
                self.assertEqual(projection.sources.catalog, analysis_input.catalog)
                self.assertIsNone(projection.comparison)
                raise RuntimeError('controlled analysis interruption')

            with (patch('socket.socket.connect', side_effect=AssertionError('No live provider')),
                  patch('upgradepilot.investigation.run_source_analysis', side_effect=fail_after_source_publication)):
                with self.assertRaisesRegex(RuntimeError, 'controlled analysis interruption'):
                    investigate_caller_signature_progress(
                        identity.repository, identity.number, session=session, workspace_host=host,
                        expected_base=identity.base_sha, expected_head=identity.head_sha,
                    )
            self.assertEqual(len(source_revisions), 1)
            target = source_revisions[0].boundary.target
            reopened = CheckpointStore.open(store.directory, read_only=True)
            restored = reopened.read_revision(host.lineage_id, host.current.revision_id, expected_target=target)
            result = reconstruct_caller_signature_projection(restored.revision.boundary, expected_target=target)
            self.assertEqual((target.repository, target.pull_number, target.base_sha, target.head_sha),
                             (identity.repository, identity.number, identity.base_sha, identity.head_sha))
            self.assertIsNone(result.comparison)
            self.assertEqual(result.sources.acquisition.state, 'partial')
            old, proposed = result.sources.acquisition.module_requests
            self.assertEqual((old.request.version_basis, old.state), ('old_dependency', 'module_examined'))
            self.assertEqual((proposed.request.version_basis, proposed.state), ('proposed_dependency', 'unavailable'))
            self.assertEqual((proposed.repository, proposed.revision, proposed.path),
                             ('owner/demo', 'd' * 40, 'demo/api.py'))
            self.assertIsNone(proposed.sha256)
            self.assertIsNone(proposed.utf8_bytes)
            self.assertEqual({m.role for m in result.sources.modules}, {'target_repository', 'old_dependency'})
            ledger = result.sources.acquisition.transport
            self.assertEqual((ledger.github_requests, ledger.provider_requests, len(dispatched)), (17, 21, 21))
            self.assertEqual(sum('/pulls/1145' in event.path for event in ledger.requests), 3)
            script = '''
import json, sys
from pathlib import Path
from unittest.mock import patch
from upgradepilot.workspace.checkpoint_store import CheckpointStore
from upgradepilot.workspace.native_boundary import ExactInvestigationTarget
from upgradepilot.workspace.native_projection import reconstruct_caller_signature_projection

target = ExactInvestigationTarget(**json.loads(sys.argv[3]))
with (patch('socket.socket.connect', side_effect=AssertionError('No provider access')),
      patch('ast.parse', side_effect=AssertionError('No source parsing')),
      patch('upgradepilot.caller_signature.worker.run_source_analysis',
            side_effect=AssertionError('No analysis execution'))):
    store = CheckpointStore.open(Path(sys.argv[1]), read_only=True)
    revision = store.read_revision('source-progress', sys.argv[2], expected_target=target).revision
    result = reconstruct_caller_signature_projection(revision.boundary, expected_target=target)
    print(json.dumps([len(result.sources.catalog.files), result.sources.acquisition.state,
                      result.sources.acquisition.module_requests[1].state, result.comparison is None]))
'''
            child = subprocess.run(
                [sys.executable, '-c', script, str(store.directory), host.current.revision_id,
                 json.dumps(asdict(target))], capture_output=True, text=True, timeout=20,
            )
            self.assertEqual(child.returncode, 0, child.stderr)
            self.assertEqual(json.loads(child.stdout), [3, 'partial', 'unavailable', True])

    def test_failed_source_publication_preserves_earlier_progress_and_stops_work(self):
        from tempfile import TemporaryDirectory
        from pathlib import Path
        from unittest.mock import patch
        from upgradepilot.investigation import investigate_caller_signature_progress
        from upgradepilot.workspace.checkpoint_store import CheckpointStore
        from upgradepilot.workspace.lifecycle_host import InvestigationWorkspaceHost
        from upgradepilot.workspace.native_projection import reconstruct_caller_signature_projection

        identity, session, dispatched = self.controlled_transport()
        with TemporaryDirectory() as tmp:
            store = CheckpointStore.create(Path(tmp) / 'store', schema_version=2)
            host = InvestigationWorkspaceHost(store=store, lineage_id='source-progress')
            publish = store.publish

            def fail_library_checkpoint(revision):
                result = reconstruct_caller_signature_projection(
                    revision.boundary, expected_target=revision.boundary.target,
                )
                if result.sources and result.sources.acquisition.module_requests:
                    raise OSError('controlled source checkpoint write failure')
                return publish(revision)

            with (patch('socket.socket.connect', side_effect=AssertionError('No live provider')),
                  patch('upgradepilot.investigation.run_source_analysis') as worker,
                  patch.object(store, 'publish', side_effect=fail_library_checkpoint)):
                with self.assertRaisesRegex(OSError, 'controlled source checkpoint write failure'):
                    investigate_caller_signature_progress(
                        identity.repository, identity.number, session=session, workspace_host=host,
                    )
            worker.assert_not_called()
            self.assertFalse(any('/pypi/demo/2.0/json' in request.url for request in dispatched))
            current = host.current
            result = reconstruct_caller_signature_projection(
                store.read_revision(host.lineage_id, current.revision_id,
                                    expected_target=current.boundary.target).revision.boundary,
                expected_target=current.boundary.target,
            )
            self.assertEqual({file.path for file in result.sources.catalog.files}, {'requirements.txt', 'app.py'})
            self.assertEqual(result.sources.acquisition.module_requests, ())
            self.assertIsNone(result.comparison)

    def test_application_analyzes_the_published_exact_version_pair(self):
        from pathlib import Path
        from unittest.mock import patch
        from upgradepilot.caller_signature import worker
        from upgradepilot.investigation import investigate_caller_signature_progress
        from upgradepilot.workspace.lifecycle_host import InvestigationWorkspaceHost
        from upgradepilot.workspace.native_projection import reconstruct_caller_signature_projection

        identity, session, dispatched = self.controlled_transport(forwarded=True)
        host = InvestigationWorkspaceHost()
        with patch('socket.socket.connect', side_effect=AssertionError('No live provider')):
            revision = investigate_caller_signature_progress(
                identity.repository, identity.number, session=session, workspace_host=host,
            )
        result = reconstruct_caller_signature_projection(
            revision.boundary, expected_target=revision.boundary.target,
        )
        self.assertEqual(result.sources.acquisition.state, 'complete')
        self.assertEqual(result.comparison.state, 'completed', result.comparison.problem_detail)
        self.assertEqual(Path(result.comparison.worker_module_origin), Path(worker.__file__).resolve())
        self.assertEqual({(candidate.callee_role.role, candidate.callee_role.path, candidate.comparison.outcome)
                          for candidate in result.comparison.result.candidates},
                         {('old_dependency', 'demo/_core.py', 'bound'),
                          ('proposed_dependency', 'demo/_core.py', 'rejected')})
        self.assertEqual({m.role for m in result.sources.modules},
                         {'target_repository', 'old_dependency', 'proposed_dependency'})
        self.assertEqual(len(dispatched), 23)
