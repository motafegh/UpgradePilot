"""Invocation limits, physical retries and ordinary-prefix transport composition.

Author-controlled HTTP responses exercise real clients/Requests preparation;
no live provider, credential, target code or model is used. These controls prove
policy accounting and retained receipt integrity, not live source availability.
"""
from dataclasses import asdict
import json
from unittest import TestCase
from unittest.mock import Mock, patch

from upgradepilot.caller_signature.acquisition import AcquisitionPolicy, AcquisitionSession


class StagedTransportTests(TestCase):
    def test_opted_in_pypi_timeout_recovery_retains_both_charged_attempts(self):
        from requests.exceptions import Timeout
        session = AcquisitionSession(policy=self.policy(), retry_pypi_timeouts=True)
        with patch('requests.Session.request', side_effect=[Timeout('authored timeout'), self.response()]) as request:
            self.assertEqual(session.get('https://pypi.org/pypi/control/1.0/json').status_code, 200)
        receipt = asdict(session.acquisition_receipt())
        self.assertEqual(request.call_count, 2)
        self.assertEqual(receipt['provider_requests'], 2)
        self.assertEqual(receipt['retry_policy'], 'pypi-get-timeout-once/1')
        self.assertEqual([r['state'] for r in receipt['requests']], ['failed', 'received'])
        self.assertEqual(receipt['retry_decisions'][0]['after_provider_request'], 1)
        self.assertEqual(receipt['retry_decisions'][0]['retry_provider_request'], 2)
        self.assertEqual(receipt['retry_decisions'][0]['state'], 'dispatched')

    def test_timeout_recovery_has_per_request_and_shared_run_ceiling(self):
        from requests.exceptions import Timeout
        session = AcquisitionSession(policy=self.policy(), retry_pypi_timeouts=True)
        with patch('requests.Session.request', side_effect=Timeout('authored timeout')) as request:
            for i in range(3):
                with self.assertRaises(Timeout):
                    session.get('https://pypi.org/pypi/control/' + str(i) + '/json')
        self.assertEqual(request.call_count, 5)
        self.assertEqual(len(asdict(session.acquisition_receipt())['retry_decisions']), 2)

    def test_timeout_recovery_never_retries_other_failure_classes_or_default_profile(self):
        from requests.exceptions import Timeout
        for case in ('default', 'github', 'status', 'body'):
            with self.subTest(case=case):
                session = AcquisitionSession(policy=self.policy(), retry_pypi_timeouts=case != 'default')
                response = self.response(status=429)
                if case == 'body':
                    response.status_code = 200
                    response.iter_content = Mock(side_effect=Timeout('body timeout'))
                effect = Timeout('header timeout') if case in {'default','github'} else response
                with patch('requests.Session.request', side_effect=effect if isinstance(effect, BaseException) else None,
                           return_value=response) as request:
                    if case == 'status':
                        self.assertEqual(session.get('https://pypi.org/control').status_code, 429)
                    else:
                        with self.assertRaises(Timeout):
                            session.get('https://api.github.com/control' if case == 'github' else 'https://pypi.org/control')
                self.assertEqual(request.call_count, 1)

    def test_timeout_retry_can_be_selected_but_refused_by_existing_provider_or_time_limit(self):
        from requests.exceptions import Timeout
        from upgradepilot.github.api import GitHubAcquisitionError
        for boundary in ('provider', 'time'):
            with self.subTest(boundary=boundary):
                now = [0.0]
                policy = self.policy(github_requests=2, provider_requests=2, source_request_reserve=1)
                session = AcquisitionSession(policy=policy, retry_pypi_timeouts=True, clock=lambda: now[0])
                if boundary == 'provider':
                    with patch('requests.Session.request', return_value=self.response()):
                        session.get('https://pypi.org/prior')
                def timeout(*args, **kwargs):
                    if boundary == 'time': now[0] = 181.0
                    raise Timeout('authored timeout')
                with patch('requests.Session.request', side_effect=timeout) as request, self.assertRaises(GitHubAcquisitionError):
                    session.get('https://pypi.org/control')
                self.assertEqual(request.call_count, 1)
                decision = asdict(session.acquisition_receipt())['retry_decisions'][0]
                self.assertEqual(decision['state'], 'not_dispatched')
                self.assertIsNone(decision['retry_provider_request'])

    """Exercise actual Requests Response handling with an authored HTTP transport."""

    @staticmethod
    def response(body=b'{}', status=200):
        from io import BytesIO
        from requests import Response
        response = Response()
        response.status_code = status
        response.raw = BytesIO(body)
        response.close = Mock(wraps=response.close)
        return response

    @staticmethod
    def policy(**changes):
        from upgradepilot.caller_signature.acquisition import AcquisitionPolicy
        return AcquisitionPolicy(**changes)

    def test_token_does_not_override_local_budget_and_explicit_budget_can_differ(self):
        from upgradepilot.github.api import GitHubAcquisitionError
        observations = []
        for token, policy, expected in ((None, self.policy(), 50), ('synthetic-test-token', self.policy(), 50),
                                        ('synthetic-test-token', self.policy(github_requests=80), 80)):
            session = AcquisitionSession(token=token, policy=policy)
            with patch('requests.Session.request', side_effect=lambda *a, **k: self.response()) as request:
                for _ in range(expected):
                    session.get('https://api.github.com/repos/control/library')
                with self.assertRaises(GitHubAcquisitionError) as raised:
                    session.get('https://api.github.com/repos/control/library')
            self.assertEqual(raised.exception.reason, 'acquisition_request_limit')
            self.assertEqual(request.call_count, expected)
            observations.append((session.auth_mode, session.github_requests))
        self.assertEqual(observations, [('anonymous', 50), ('token-env', 50), ('token-env', 80)])

    def test_reservation_protects_later_stage_without_resetting_shared_counts(self):
        session = AcquisitionSession(policy=self.policy(github_requests=6, source_request_reserve=2))
        with patch('requests.Session.request', side_effect=lambda *a, **k: self.response()) as request:
            with session.stage('target_context', reserve_github=2):
                for _ in range(4):
                    session.get('https://api.github.com/target')
                with self.assertRaises(Exception) as raised:
                    session.get('https://api.github.com/target')
            self.assertEqual(raised.exception.reason, 'acquisition_stage_request_limit')
            self.assertFalse(session.request_limit_reached)
            with session.stage('source_closure'):
                session.get('https://api.github.com/library/old')
                session.get('https://api.github.com/library/new')
        self.assertEqual(request.call_count, 6)
        receipt = asdict(session.acquisition_receipt())
        self.assertEqual([e['stage'] for e in receipt['requests']], ['target_context'] * 4 + ['source_closure'] * 2)
        self.assertEqual(receipt['stops'], ({'stage': 'target_context', 'reason': 'acquisition_stage_request_limit'},))

    def test_pypi_and_error_bodies_count_and_only_explicit_github_token_is_sent(self):
        session = AcquisitionSession(token='synthetic-secret', policy=self.policy(provider_requests=50))
        responses = [self.response(b'{"answer": 1}'), self.response(b'error', 503)]
        with patch('requests.Session.request', side_effect=responses) as request:
            response = session.get('https://api.github.com/control', headers={'Authorization': 'wrong'})
            self.assertEqual(response.json(), {'answer': 1})
            self.assertEqual(b''.join(response.iter_content(2)), b'{"answer": 1}')
            session.get('https://pypi.org/pypi/control/json', headers={'Authorization': 'wrong'})
        self.assertEqual(request.call_args_list[0].kwargs['headers']['Authorization'], 'Bearer synthetic-secret')
        self.assertNotIn('Authorization', request.call_args_list[1].kwargs['headers'])
        self.assertFalse(request.call_args.kwargs['allow_redirects'])
        self.assertEqual(session.provider_requests, 2)
        self.assertEqual(session.github_requests, 1)
        self.assertEqual(session.body_bytes, 18)
        self.assertNotIn('synthetic-secret', json.dumps(asdict(session.acquisition_receipt())))
        anonymous = AcquisitionSession(policy=self.policy())
        with patch('requests.Session.request', return_value=self.response()) as request:
            anonymous.get('https://api.github.com/control', headers={'Authorization': 'wrong'})
        self.assertNotIn('Authorization', request.call_args.kwargs['headers'])

    def test_response_and_aggregate_limits_charge_rejected_bytes_and_close(self):
        for changes, bodies, expected in (
            ({'response_bytes': 4}, [b'12345'], 'acquisition_response_body_limit'),
            ({'aggregate_bytes': 6}, [b'1234', b'5678'], 'acquisition_aggregate_body_limit'),
        ):
            session = AcquisitionSession(policy=self.policy(**changes))
            responses = [self.response(body) for body in bodies]
            with patch('requests.Session.request', side_effect=responses):
                with self.assertRaises(Exception) as raised:
                    for _ in bodies:
                        session.get('https://pypi.org/pypi/control/json')
            self.assertEqual(raised.exception.reason, expected)
            self.assertEqual(session.body_bytes, sum(map(len, bodies)))
            self.assertTrue(all(r.close.called for r in responses))
            self.assertEqual(session.receipts[-1]['state'], 'failed')

    def test_deadline_checks_start_body_and_empty_response_without_real_sleep(self):
        for body in (b'', b'{}'):
            now = [0.0]
            session = AcquisitionSession(policy=self.policy(elapsed_seconds=1), clock=lambda: now[0])
            response = self.response(body)
            def late(*args, **kwargs):
                self.assertEqual(kwargs['timeout'], (1, 1))
                now[0] = 2.0
                return response
            with patch('requests.Session.request', side_effect=late):
                with self.assertRaises(Exception) as raised:
                    session.get('https://api.github.com/control')
            self.assertEqual(raised.exception.reason, 'acquisition_deadline')
            self.assertEqual(session.receipts[0]['state'], 'failed')
            response.close.assert_called_once()
            with patch('requests.Session.request') as transport:
                with self.assertRaises(Exception):
                    session.get('https://pypi.org/pypi/control/json')
                transport.assert_not_called()

    def test_all_provider_limit_transport_failure_and_policy_validation(self):
        from requests.exceptions import ConnectionError
        session = AcquisitionSession(policy=self.policy(github_requests=2, source_request_reserve=1, provider_requests=2))
        with patch('requests.Session.request', side_effect=[ConnectionError('authored outage'), self.response()]):
            with self.assertRaises(ConnectionError):
                session.get('https://pypi.org/pypi/control/json')
            session.get('https://pypi.org/pypi/control/json')
        with patch('requests.Session.request') as transport:
            with self.assertRaises(Exception) as raised:
                session.get('https://api.github.com/control')
            transport.assert_not_called()
        self.assertEqual(raised.exception.reason, 'acquisition_provider_request_limit')
        self.assertEqual(session.github_requests, 0)
        self.assertEqual(session.provider_requests, 2)
        for changes in ({'github_requests': True}, {'elapsed_seconds': float('nan')},
                        {'github_requests': 201}, {'source_request_reserve': 50}):
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                self.policy(**changes)


class NativeTransportCompositionTests(TestCase):
    def test_normal_prefix_and_later_clients_share_charged_prepared_requests(self):
        import base64
        from urllib.parse import urlsplit
        from requests.adapters import BaseAdapter
        from requests.exceptions import Timeout
        from test_github_client import _identity, _pull_request_payload, _changed_file
        from upgradepilot.github.pull_request import GitHubPullRequestClient
        from upgradepilot.github.repository import GitHubRepositoryClient
        from upgradepilot.investigation_inputs import acquire_dependency_inputs
        from upgradepilot.pypi.release import PyPIReleaseClient, PackageReleaseEvidence

        identity = _identity(changed_files=1)
        dispatched = []
        pypi_attempts = 0
        body = b'def send():\n pass\n'

        class Transport(BaseAdapter):
            def send(self, request, **kwargs):
                nonlocal pypi_attempts
                dispatched.append(request)
                path = urlsplit(request.url).path
                if path.endswith('/pulls/1145'):
                    payload = {**_pull_request_payload(identity), 'body': 'Original provider description'}
                elif path.endswith('/pulls/1145/files'):
                    payload = [_changed_file(1, filename='requirements.txt')]
                elif path.endswith('/contents/demo.py'):
                    payload = dict(type='file', path='demo.py', encoding='base64',
                                   content=base64.b64encode(body).decode())
                elif path == '/pypi/pytest/9.0.3/json':
                    pypi_attempts += 1
                    if pypi_attempts == 1:
                        raise Timeout('Controlled pre-response timeout')
                    payload = dict(info=dict(name='pytest', version='9.0.3', project_urls={}), urls=[], last_serial=1)
                else:
                    raise AssertionError('Unexpected physical request: ' + request.url)
                response = StagedTransportTests.response(json.dumps(payload).encode())
                response.request, response.url = request, request.url
                return response

            def close(self):
                pass

        session = AcquisitionSession(policy=AcquisitionPolicy(), token='synthetic-shared-secret',
                                     retry_pypi_timeouts=True, clock=lambda: 0.0)
        session.mount('https://', Transport())
        pull = GitHubPullRequestClient(session=session)
        repository = GitHubRepositoryClient(session=session)
        releases = PyPIReleaseClient(session=session)
        with patch('requests.sessions.get_netrc_auth', return_value=('ambient', 'must-not-be-used')) as ambient:
            with session.stage('dependency_inputs'):
                inputs = acquire_dependency_inputs(identity.repository, identity.number, pull, repository,
                    expected_base=identity.base_sha, expected_head=identity.head_sha)
            prefix = session.acquisition_receipt()
            with session.stage('source_closure'):
                release = releases.get_release('pytest', '9.0.3')
                file = repository.get_exact_commit_text_file(identity.repository, identity.head_sha, 'demo.py')
            ambient.assert_not_called()
        session.finish_acquisition()
        final = session.acquisition_receipt()
        self.assertEqual(inputs.identity, identity)
        self.assertEqual(inputs.description.text, 'Original provider description')
        self.assertEqual((inputs.dependency.old_version, inputs.dependency.proposed_version), ('9.0.2', '9.0.3'))
        self.assertEqual((file.repository, file.revision, file.content), (identity.repository, identity.head_sha, body.decode()))
        self.assertIsInstance(release, PackageReleaseEvidence)
        # The prefix's required identity recheck is charged too. Later source
        # work reuses its exact input rather than acquiring a second PR prefix.
        self.assertEqual((prefix.github_requests, prefix.provider_requests), (3, 3))
        self.assertEqual((final.github_requests, final.provider_requests, len(dispatched)), (4, 6, 6))
        self.assertEqual([x.provider_requests for x in final.requests], list(range(1, 7)))
        self.assertEqual([x.stage for x in final.requests], ['dependency_inputs'] * 3 + ['source_closure'] * 3)
        self.assertEqual([x.state for x in final.requests], ['received'] * 3 + ['failed', 'received', 'received'])
        self.assertEqual((final.retry_decisions[0].after_provider_request, final.retry_decisions[0].retry_provider_request), (4, 5))
        for request in dispatched:
            if urlsplit(request.url).hostname == 'api.github.com':
                self.assertEqual(request.headers['Authorization'], 'Bearer synthetic-shared-secret')
            else:
                self.assertNotIn('Authorization', request.headers)
        self.assertNotIn('synthetic-shared-secret', repr(final))
        self.assertEqual(len(prefix.requests), 3)  # Snapshot did not grow/mutate.
        self.assertEqual(prefix.requests, final.requests[:3])
        self._assert_native_receipt_round_trip(final)

    @staticmethod
    def _assert_native_receipt_round_trip(transport):
        from upgradepilot.caller_signature import source_evidence as se
        from upgradepilot.caller_signature.evidence import AnalysisLimits
        from upgradepilot.caller_signature.source_codec import encode_sources, decode_sources
        # A transport snapshot can survive before a source inventory/catalog is
        # ready; it does not invent admitted text or claim a complete acquisition.
        receipt = se.SourceAcquisitionReceipt(origin='controlled_observation', state='partial',
            observed_at=None, target=None, module_requests=(), samples=(), problems=(),
            omitted_candidates=(), deferred_candidates=(), unexamined_modules=(),
            material_omissions=(), adapter_limitations=(), source_work=None,
            transport=transport, method_files=(), retention_gaps=())
        sources = se.CallerSignatureSources(None, (), AnalysisLimits(), receipt)
        decoded = decode_sources(encode_sources(sources))
        assert decoded == sources
        assert decoded.analysis_input() is None

    def test_product_requires_policy_and_rejects_scope_before_dispatch(self):
        from requests.exceptions import RequestException
        with self.assertRaises(ValueError):
            AcquisitionSession(policy=None)
        with self.assertRaises(TypeError):
            AcquisitionSession()
        session = AcquisitionSession(policy=AcquisitionPolicy())
        with patch('requests.Session.request') as dispatch:
            for method, url in (('POST', 'https://api.github.com/control'),
                ('GET', 'http://api.github.com/control'), ('GET', 'https://token@api.github.com/control'),
                ('GET', 'https://api.github.com:443/control'), ('GET', 'https://other.example/control')):
                with self.subTest(method=method, url=url), self.assertRaises(RequestException):
                    session.request(method, url)
            dispatch.assert_not_called()
        self.assertEqual(session.acquisition_receipt().provider_requests, 0)

    def test_real_requests_preparation_refuses_redirect_without_followup(self):
        from requests.adapters import BaseAdapter
        from upgradepilot.github.api import GitHubApiClient, GitHubAcquisitionError
        dispatched = []

        class Redirect(BaseAdapter):
            def send(self, request, **kwargs):
                dispatched.append(request)
                response = StagedTransportTests.response(b'redirect', 302)
                response.request, response.url = request, request.url
                response.headers['Location'] = 'https://pypi.org/not-admitted-by-redirect'
                return response

            def close(self):
                pass

        session = AcquisitionSession(policy=AcquisitionPolicy(), token='synthetic-secret')
        session.mount('https://', Redirect())
        with self.assertRaises(GitHubAcquisitionError) as raised:
            GitHubApiClient(session=session)._get('https://api.github.com/control', resource='control')
        self.assertEqual(raised.exception.reason, 'http_error')
        self.assertEqual(len(dispatched), 1)
        snapshot = session.acquisition_receipt()
        self.assertEqual((snapshot.provider_requests, snapshot.requests[0].status), (1, 302))
        # Transport receipt says received; the provider still refuses evidence.
        self.assertEqual(snapshot.requests[0].state, 'received')
