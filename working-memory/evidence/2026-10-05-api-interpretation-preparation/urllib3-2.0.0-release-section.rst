2.0.0 (2023-04-26)
==================

Read the `v2.0 migration guide <https://urllib3.readthedocs.io/en/latest/v2-migration-guide.html>`__ for help upgrading to the latest version of urllib3.

Removed
-------

* Removed support for Python 2.7, 3.5, and 3.6 (`#883 <https://github.com/urllib3/urllib3/issues/883>`__, `#2336 <https://github.com/urllib3/urllib3/issues/2336>`__).
* Removed fallback on certificate ``commonName`` in ``match_hostname()`` function.
  This behavior was deprecated in May 2000 in RFC 2818. Instead only ``subjectAltName``
  is used to verify the hostname by default. To enable verifying the hostname against
  ``commonName`` use ``SSLContext.hostname_checks_common_name = True`` (`#2113 <https://github.com/urllib3/urllib3/issues/2113>`__).
* Removed support for Python with an ``ssl`` module compiled with LibreSSL, CiscoSSL,
  wolfSSL, and all other OpenSSL alternatives. Python is moving to require OpenSSL with PEP 644 (`#2168 <https://github.com/urllib3/urllib3/issues/2168>`__).
* Removed support for OpenSSL versions earlier than 1.1.1 or that don't have SNI support.
  When an incompatible OpenSSL version is detected an ``ImportError`` is raised (`#2168 <https://github.com/urllib3/urllib3/issues/2168>`__).
* Removed the list of default ciphers for OpenSSL 1.1.1+ and SecureTransport as their own defaults are already secure (`#2082 <https://github.com/urllib3/urllib3/issues/2082>`__).
* Removed ``urllib3.contrib.appengine.AppEngineManager`` and support for Google App Engine Standard Environment (`#2044 <https://github.com/urllib3/urllib3/issues/2044>`__).
* Removed deprecated ``Retry`` options ``method_whitelist``, ``DEFAULT_REDIRECT_HEADERS_BLACKLIST`` (`#2086 <https://github.com/urllib3/urllib3/issues/2086>`__).
* Removed ``urllib3.HTTPResponse.from_httplib`` (`#2648 <https://github.com/urllib3/urllib3/issues/2648>`__).
* Removed default value of ``None`` for the ``request_context`` parameter of ``urllib3.PoolManager.connection_from_pool_key``. This change should have no effect on users as the default value of ``None`` was an invalid option and was never used (`#1897 <https://github.com/urllib3/urllib3/issues/1897>`__).
* Removed the ``urllib3.request`` module. ``urllib3.request.RequestMethods`` has been made a private API.
  This change was made to ensure that ``from urllib3 import request`` imported the top-level ``request()``
  function instead of the ``urllib3.request`` module (`#2269 <https://github.com/urllib3/urllib3/issues/2269>`__).
* Removed support for SSLv3.0 from the ``urllib3.contrib.pyopenssl`` even when support is available from the compiled OpenSSL library (`#2233 <https://github.com/urllib3/urllib3/issues/2233>`__).
* Removed the deprecated ``urllib3.contrib.ntlmpool`` module (`#2339 <https://github.com/urllib3/urllib3/issues/2339>`__).
* Removed ``DEFAULT_CIPHERS``, ``HAS_SNI``, ``USE_DEFAULT_SSLCONTEXT_CIPHERS``, from the private module ``urllib3.util.ssl_`` (`#2168 <https://github.com/urllib3/urllib3/issues/2168>`__).
* Removed ``urllib3.exceptions.SNIMissingWarning`` (`#2168 <https://github.com/urllib3/urllib3/issues/2168>`__).
* Removed the ``_prepare_conn`` method from ``HTTPConnectionPool``. Previously this was only used to call ``HTTPSConnection.set_cert()`` by ``HTTPSConnectionPool`` (`#1985 <https://github.com/urllib3/urllib3/issues/1985>`__).
* Removed ``tls_in_tls_required`` property from ``HTTPSConnection``. This is now determined from the ``scheme`` parameter in ``HTTPConnection.set_tunnel()`` (`#1985 <https://github.com/urllib3/urllib3/issues/1985>`__).

Deprecated
----------

* Deprecated ``HTTPResponse.getheaders()`` and ``HTTPResponse.getheader()`` which will be removed in urllib3 v2.1.0. Instead use ``HTTPResponse.headers`` and ``HTTPResponse.headers.get(name, default)``. (`#1543 <https://github.com/urllib3/urllib3/issues/1543>`__, `#2814 <https://github.com/urllib3/urllib3/issues/2814>`__).
* Deprecated ``urllib3.contrib.pyopenssl`` module which will be removed in urllib3 v2.1.0 (`#2691 <https://github.com/urllib3/urllib3/issues/2691>`__).
* Deprecated ``urllib3.contrib.securetransport`` module which will be removed in urllib3 v2.1.0 (`#2692 <https://github.com/urllib3/urllib3/issues/2692>`__).
* Deprecated ``ssl_version`` option in favor of ``ssl_minimum_version``. ``ssl_version`` will be removed in urllib3 v2.1.0 (`#2110 <https://github.com/urllib3/urllib3/issues/2110>`__).
* Deprecated the ``strict`` parameter as it's not longer needed in Python 3.x. It will be removed in urllib3 v2.1.0 (`#2267 <https://github.com/urllib3/urllib3/issues/2267>`__)
* Deprecated the ``NewConnectionError.pool`` attribute which will be removed in urllib3 v2.1.0 (`#2271 <https://github.com/urllib3/urllib3/issues/2271>`__).
* Deprecated ``format_header_param_html5`` and ``format_header_param`` in favor of ``format_multipart_header_param`` (`#2257 <https://github.com/urllib3/urllib3/issues/2257>`__).
* Deprecated ``RequestField.header_formatter`` parameter which will be removed in urllib3 v2.1.0 (`#2257 <https://github.com/urllib3/urllib3/issues/2257>`__).
* Deprecated ``HTTPSConnection.set_cert()`` method. Instead pass parameters to the ``HTTPSConnection`` constructor (`#1985 <https://github.com/urllib3/urllib3/issues/1985>`__).
* Deprecated ``HTTPConnection.request_chunked()`` method which will be removed in urllib3 v2.1.0. Instead pass ``chunked=True`` to ``HTTPConnection.request()`` (`#1985 <https://github.com/urllib3/urllib3/issues/1985>`__).

Added
-----

* Added top-level ``urllib3.request`` function which uses a preconfigured module-global ``PoolManager`` instance (`#2150 <https://github.com/urllib3/urllib3/issues/2150>`__).
* Added the ``json`` parameter to ``urllib3.request()``, ``PoolManager.request()``, and ``ConnectionPool.request()`` methods to send JSON bodies in requests. Using this parameter will set the header ``Content-Type: application/json`` if ``Content-Type`` isn't already defined.
  Added support for parsing JSON response bodies with ``HTTPResponse.json()`` method (`#2243 <https://github.com/urllib3/urllib3/issues/2243>`__).
* Added type hints to the ``urllib3`` module (`#1897 <https://github.com/urllib3/urllib3/issues/1897>`__).
* Added ``ssl_minimum_version`` and ``ssl_maximum_version`` options which set
  ``SSLContext.minimum_version`` and ``SSLContext.maximum_version`` (`#2110 <https://github.com/urllib3/urllib3/issues/2110>`__).
* Added support for Zstandard (RFC 8878) when ``zstandard`` 1.18.0 or later is installed.
  Added the ``zstd`` extra which installs the ``zstandard`` package (`#1992 <https://github.com/urllib3/urllib3/issues/1992>`__).
* Added ``urllib3.response.BaseHTTPResponse`` class. All future response classes will be subclasses of ``BaseHTTPResponse`` (`#2083 <https://github.com/urllib3/urllib3/issues/2083>`__).
* Added ``FullPoolError`` which is raised when ``PoolManager(block=True)`` and a connection is returned to a full pool (`#2197 <https://github.com/urllib3/urllib3/issues/2197>`__).
* Added ``HTTPHeaderDict`` to the top-level ``urllib3`` namespace (`#2216 <https://github.com/urllib3/urllib3/issues/2216>`__).
* Added support for configuring header merging behavior with HTTPHeaderDict
  When using a ``HTTPHeaderDict`` to provide headers for a request, by default duplicate
  header values will be repeated. But if ``combine=True`` is passed into a call to
  ``HTTPHeaderDict.add``, then the added header value will be merged in with an existing
  value into a comma-separated list (``X-My-Header: foo, bar``) (`#2242 <https://github.com/urllib3/urllib3/issues/2242>`__).
* Added ``NameResolutionError`` exception when a DNS error occurs (`#2305 <https://github.com/urllib3/urllib3/issues/2305>`__).
* Added ``proxy_assert_hostname`` and ``proxy_assert_fingerprint`` kwargs to ``ProxyManager`` (`#2409 <https://github.com/urllib3/urllib3/issues/2409>`__).
* Added a configurable ``backoff_max`` parameter to the ``Retry`` class.
  If a custom ``backoff_max`` is provided to the ``Retry`` class, it
  will replace the ``Retry.DEFAULT_BACKOFF_MAX`` (`#2494 <https://github.com/urllib3/urllib3/issues/2494>`__).
* Added the ``authority`` property to the Url class as per RFC 3986 3.2. This property should be used in place of ``netloc`` for users who want to include the userinfo (auth) component of the URI (`#2520 <https://github.com/urllib3/urllib3/issues/2520>`__).
* Added the ``scheme`` parameter to ``HTTPConnection.set_tunnel`` to configure the scheme of the origin being tunnelled to (`#1985 <https://github.com/urllib3/urllib3/issues/1985>`__).
* Added the ``is_closed``, ``is_connected`` and ``has_connected_to_proxy`` properties to ``HTTPConnection`` (`#1985 <https://github.com/urllib3/urllib3/issues/1985>`__).
* Added optional ``backoff_jitter`` parameter to ``Retry``. (`#2952 <https://github.com/urllib3/urllib3/issues/2952>`__)

Changed
-------

* Changed ``urllib3.response.HTTPResponse.read`` to respect the semantics of ``io.BufferedIOBase`` regardless of compression. Specifically, this method:

  * Only returns an empty bytes object to indicate EOF (that is, the response has been fully consumed).
  * Never returns more bytes than requested.
  * Can issue any number of system calls: zero, one or multiple.

  If you want each ``urllib3.response.HTTPResponse.read`` call to issue a single system call, you need to disable decompression by setting ``decode_content=False`` (`#2128 <https://github.com/urllib3/urllib3/issues/2128>`__).
* Changed ``urllib3.HTTPConnection.getresponse`` to return an instance of ``urllib3.HTTPResponse`` instead of ``http.client.HTTPResponse`` (`#2648 <https://github.com/urllib3/urllib3/issues/2648>`__).
* Changed ``ssl_version`` to instead set the corresponding ``SSLContext.minimum_version``
  and ``SSLContext.maximum_version`` values.  Regardless of ``ssl_version`` passed
  ``SSLContext`` objects are now constructed using ``ssl.PROTOCOL_TLS_CLIENT`` (`#2110 <https://github.com/urllib3/urllib3/issues/2110>`__).
* Changed default ``SSLContext.minimum_version`` to be ``TLSVersion.TLSv1_2`` in line with Python 3.10 (`#2373 <https://github.com/urllib3/urllib3/issues/2373>`__).
* Changed ``ProxyError`` to wrap any connection error (timeout, TLS, DNS) that occurs when connecting to the proxy (`#2482 <https://github.com/urllib3/urllib3/pull/2482>`__).
* Changed ``urllib3.util.create_urllib3_context`` to not override the system cipher suites with
  a default value. The new default will be cipher suites configured by the operating system (`#2168 <https://github.com/urllib3/urllib3/issues/2168>`__).
* Changed ``multipart/form-data`` header parameter formatting matches the WHATWG HTML Standard as of 2021-06-10. Control characters in filenames are no longer percent encoded (`#2257 <https://github.com/urllib3/urllib3/issues/2257>`__).
* Changed the error raised when connecting via HTTPS when the ``ssl`` module isn't available from ``SSLError`` to ``ImportError`` (`#2589 <https://github.com/urllib3/urllib3/issues/2589>`__).
* Changed ``HTTPConnection.request()`` to always use lowercase chunk boundaries when sending requests with ``Transfer-Encoding: chunked`` (`#2515 <https://github.com/urllib3/urllib3/issues/2515>`__).
* Changed ``enforce_content_length`` default to True, preventing silent data loss when reading streamed responses (`#2514 <https://github.com/urllib3/urllib3/issues/2514>`__).
* Changed internal implementation of ``HTTPHeaderDict`` to use ``dict`` instead of ``collections.OrderedDict`` for better performance (`#2080 <https://github.com/urllib3/urllib3/issues/2080>`__).
* Changed the ``urllib3.contrib.pyopenssl`` module to wrap ``OpenSSL.SSL.Error`` with ``ssl.SSLError`` in ``PyOpenSSLContext.load_cert_chain`` (`#2628 <https://github.com/urllib3/urllib3/issues/2628>`__).
* Changed usage of the deprecated ``socket.error`` to ``OSError`` (`#2120 <https://github.com/urllib3/urllib3/issues/2120>`__).
* Changed all parameters in the ``HTTPConnection`` and ``HTTPSConnection`` constructors to be keyword-only except ``host`` and ``port`` (`#1985 <https://github.com/urllib3/urllib3/issues/1985>`__).
* Changed ``HTTPConnection.getresponse()`` to set the socket timeout from ``HTTPConnection.timeout`` value before reading
  data from the socket. This previously was done manually by the ``HTTPConnectionPool`` calling ``HTTPConnection.sock.settimeout(...)`` (`#1985 <https://github.com/urllib3/urllib3/issues/1985>`__).
* Changed the ``_proxy_host`` property to ``_tunnel_host`` in ``HTTPConnectionPool`` to more closely match how the property is used (value in ``HTTPConnection.set_tunnel()``) (`#1985 <https://github.com/urllib3/urllib3/issues/1985>`__).
* Changed name of ``Retry.BACK0FF_MAX`` to be ``Retry.DEFAULT_BACKOFF_MAX``.
* Changed TLS handshakes to use ``SSLContext.check_hostname`` when possible (`#2452 <https://github.com/urllib3/urllib3/pull/2452>`__).
* Changed ``server_hostname`` to behave like other parameters only used by ``HTTPSConnectionPool`` (`#2537 <https://github.com/urllib3/urllib3/pull/2537>`__).
* Changed the default ``blocksize`` to 16KB to match OpenSSL's default read amounts (`#2348 <https://github.com/urllib3/urllib3/pull/2348>`__).
* Changed ``HTTPResponse.read()`` to raise an error when calling with ``decode_content=False`` after using ``decode_content=True`` to prevent data loss (`#2800 <https://github.com/urllib3/urllib3/issues/2800>`__).

Fixed
-----

* Fixed thread-safety issue where accessing a ``PoolManager`` with many distinct origins would cause connection pools to be closed while requests are in progress (`#1252 <https://github.com/urllib3/urllib3/issues/1252>`__).
* Fixed an issue where an ``HTTPConnection`` instance would erroneously reuse the socket read timeout value from reading the previous response instead of a newly configured connect timeout.
  Instead now if ``HTTPConnection.timeout`` is updated before sending the next request the new timeout value will be used (`#2645 <https://github.com/urllib3/urllib3/issues/2645>`__).
* Fixed ``socket.error.errno`` when raised from pyOpenSSL's ``OpenSSL.SSL.SysCallError`` (`#2118 <https://github.com/urllib3/urllib3/issues/2118>`__).
* Fixed the default value of ``HTTPSConnection.socket_options`` to match ``HTTPConnection`` (`#2213 <https://github.com/urllib3/urllib3/issues/2213>`__).
* Fixed a bug where ``headers`` would be modified by the ``remove_headers_on_redirect`` feature (`#2272 <https://github.com/urllib3/urllib3/issues/2272>`__).
* Fixed a reference cycle bug in ``urllib3.util.connection.create_connection()`` (`#2277 <https://github.com/urllib3/urllib3/issues/2277>`__).
* Fixed a socket leak if ``HTTPConnection.connect()`` fails (`#2571 <https://github.com/urllib3/urllib3/pull/2571>`__).
* Fixed ``urllib3.contrib.pyopenssl.WrappedSocket`` and ``urllib3.contrib.securetransport.WrappedSocket`` close methods (`#2970 <https://github.com/urllib3/urllib3/issues/2970>`__)

