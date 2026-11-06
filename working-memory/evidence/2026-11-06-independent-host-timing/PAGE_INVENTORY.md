# Actual contents of the60 retained HTTPX pages

Post-delivery inspection of the measured run. Every interval is zero-based with an exclusive end. A page may contain the middle of a JSON string/object; candidate labels below are navigation aids, not independent findings. Full text remains private and in the retained source/Workspace.

`bound` means recorded local argument reception under that candidate's premises. It does not mean the package was installed, the path executed, behavior tested or the upgrade compatible. `constraint_sample` identifies sampled source, not an observed target installation. The two old and two proposed HTTPX witnesses are source-path alternatives for one root, not four runtime executions.

The record is 1,669,418 ASCII characters/bytes; this task delivered its first245,760 characters. The candidate array occupies [3825, 241694) (237,869 characters). Page1 also contains the analysis envelope, whole-file admission and profile/version fields. Page60 contains the end of candidates, codec/catalog fields and the beginning of discovery gaps. Most unit/fact tables occur later and were not paged by this task.

## Candidate key

| Candidate | Pages touched | Root expression | Role/package/version | Recorded callee path | Local outcome |
|---|---|---|---|---|---|
| C1 | 1–4 | `StaticFiles(directory=STATIC_DIRECTORY)` | constraint_sample / starlette / 1.10.0 | `starlette/staticfiles.py` | bound |
| C2 | 4–7 | `TestClient(app)` | constraint_sample / starlette / 1.10.0 | `starlette/testclient.py` | bound |
| C3 | 7–10 | `TestClient(app)` | constraint_sample / starlette / 1.10.0 | `starlette/testclient.py` | bound |
| C4 | 10–13 | `TestClient(app)` | constraint_sample / starlette / 1.10.0 | `starlette/testclient.py` | bound |
| C5 | 13–18 | `TestClient(app)` | constraint_sample / starlette / 1.10.0 | `starlette/testclient.py` | bound |
| C6 | 18–28 | `TestClient(app)` | proposed_dependency / httpx / 0.28.1 | `httpx/_client.py` | bound |
| C7 | 28–38 | `TestClient(app)` | proposed_dependency / httpx / 0.28.1 | `httpx/_client.py` | bound |
| C8 | 38–48 | `TestClient(app)` | old_dependency / httpx / 0.27.2 | `httpx/_client.py` | bound |
| C9 | 48–58 | `TestClient(app)` | old_dependency / httpx / 0.27.2 | `httpx/_client.py` | bound |
| C10 | 58–59 | `get_token()` | target_repository / target / head | `app/utils.py` | bound |
| C11 | 59–59 | `get_token()` | target_repository / target / head | `app/utils.py` | bound |
| C12 | 59–60 | `get_token()` | target_repository / target / head | `app/utils.py` | bound |

Step expression JSON strings occupy 204,242 characters across these candidates. Counting each identical source-unit/span/operation/expression tuple once gives 86,002; repeated tuples account for 118,240 characters. These are wire-size observations, not a decision to delete native evidence. Several expressions contain full class/function bodies, which explains long runs of pages within one candidate. Source-step IDs/roles/premises and original retained files still matter.

## Every page

| Page | Character interval | Actual overlapping content |
|---|---|---|
| 1 | [0, 4096) | original analysis envelope/header; result.admission; result.analysis_profile; result.binding_version; C1 constraint_sample starlette 1.10.0: callee_role |
| 2 | [4096, 8192) | C1 constraint_sample starlette 1.10.0: callee_role, candidate_id, comparison, premises, root_call_id, steps; text fragments: call (StaticFiles(directory=STATIC_DIRECTORY)), import_origin (from fastapi.staticfiles import StaticFiles), reexport (from starlette.staticfiles import StaticFiles as StaticFiles), class_declaration (class StaticFiles:) |
| 3 | [8192, 12288) | C1 constraint_sample starlette 1.10.0: steps; text fragments: class_declaration (class StaticFiles:) |
| 4 | [12288, 16384) | C1 constraint_sample starlette 1.10.0: steps; text fragments: class_declaration (class StaticFiles:), initializer (def __init__(); C2 constraint_sample starlette 1.10.0: callee_role, candidate_id, comparison, premises |
| 5 | [16384, 20480) | C2 constraint_sample starlette 1.10.0: premises, root_call_id, steps; text fragments: call (TestClient(app)), import_origin (from fastapi.testclient import TestClient), reexport (from starlette.testclient import TestClient as TestClient), class_declaration (class TestClient(httpx.Client):) |
| 6 | [20480, 24576) | C2 constraint_sample starlette 1.10.0: steps; text fragments: class_declaration (class TestClient(httpx.Client):) |
| 7 | [24576, 28672) | C2 constraint_sample starlette 1.10.0: steps; text fragments: initializer (def __init__(); C3 constraint_sample starlette 1.10.0: callee_role, candidate_id, comparison, premises, root_call_id, steps; text fragments: call (TestClient(app)), import_origin (from fastapi.testclient import TestClient), reexport (from starlette.testclient import TestClient as TestClient), class_declaration (class TestClient(httpx.Client):) |
| 8 | [28672, 32768) | C3 constraint_sample starlette 1.10.0: steps; text fragments: class_declaration (class TestClient(httpx.Client):) |
| 9 | [32768, 36864) | C3 constraint_sample starlette 1.10.0: steps; text fragments: class_declaration (class TestClient(httpx.Client):), initializer (def __init__() |
| 10 | [36864, 40960) | C3 constraint_sample starlette 1.10.0: steps; text fragments: initializer (def __init__(), call (_is_asgi3(app)), declaration (def _is_asgi3(app: ASGI2App \| ASGI3App) -> TypeGuard[ASGI3App]:); C4 constraint_sample starlette 1.10.0: callee_role, candidate_id, comparison, premises, root_call_id, steps; text fragments: call (TestClient(app)), import_origin (from fastapi.testclient import TestClient), reexport (from starlette.testclient import TestClient as TestClient), class_declaration (class TestClient(httpx.Client):) |
| 11 | [40960, 45056) | C4 constraint_sample starlette 1.10.0: steps; text fragments: class_declaration (class TestClient(httpx.Client):) |
| 12 | [45056, 49152) | C4 constraint_sample starlette 1.10.0: steps; text fragments: class_declaration (class TestClient(httpx.Client):), initializer (def __init__(), call (_WrapASGI2(app)) |
| 13 | [49152, 53248) | C4 constraint_sample starlette 1.10.0: steps; text fragments: class_declaration (class _WrapASGI2:), initializer (def __init__(self, app: ASGI2App) -> None:); C5 constraint_sample starlette 1.10.0: callee_role, candidate_id, comparison, premises, root_call_id, steps; text fragments: call (TestClient(app)), import_origin (from fastapi.testclient import TestClient), reexport (from starlette.testclient import TestClient as TestClient), class_declaration (class TestClient(httpx.Client):) |
| 14 | [53248, 57344) | C5 constraint_sample starlette 1.10.0: steps; text fragments: class_declaration (class TestClient(httpx.Client):) |
| 15 | [57344, 61440) | C5 constraint_sample starlette 1.10.0: steps; text fragments: class_declaration (class TestClient(httpx.Client):), initializer (def __init__(), call (_TestClientTransport() |
| 16 | [61440, 65536) | C5 constraint_sample starlette 1.10.0: steps; text fragments: call (_TestClientTransport(), class_declaration (class _TestClientTransport(httpx.BaseTransport):) |
| 17 | [65536, 69632) | C5 constraint_sample starlette 1.10.0: steps; text fragments: class_declaration (class _TestClientTransport(httpx.BaseTransport):) |
| 18 | [69632, 73728) | C5 constraint_sample starlette 1.10.0: steps; text fragments: class_declaration (class _TestClientTransport(httpx.BaseTransport):), initializer (def __init__(); C6 proposed_dependency httpx 0.28.1: callee_role, candidate_id, comparison |
| 19 | [73728, 77824) | C6 proposed_dependency httpx 0.28.1: comparison, premises, root_call_id, steps; text fragments: call (TestClient(app)), import_origin (from fastapi.testclient import TestClient), reexport (from starlette.testclient import TestClient as TestClient), class_declaration (class TestClient(httpx.Client):) |
| 20 | [77824, 81920) | C6 proposed_dependency httpx 0.28.1: steps; text fragments: class_declaration (class TestClient(httpx.Client):) |
| 21 | [81920, 86016) | C6 proposed_dependency httpx 0.28.1: steps; text fragments: class_declaration (class TestClient(httpx.Client):), initializer (def __init__(), call (super().__init__(), declared_base (httpx.Client), reexport (import httpx), reexport (from ._api import *), reexport (from ._client import Client), class_declaration (class Client(BaseClient):) |
| 22 | [86016, 90112) | C6 proposed_dependency httpx 0.28.1: steps; text fragments: class_declaration (class Client(BaseClient):) |
| 23 | [90112, 94208) | C6 proposed_dependency httpx 0.28.1: steps; text fragments: class_declaration (class Client(BaseClient):) |
| 24 | [94208, 98304) | C6 proposed_dependency httpx 0.28.1: steps; text fragments: class_declaration (class Client(BaseClient):) |
| 25 | [98304, 102400) | C6 proposed_dependency httpx 0.28.1: steps; text fragments: class_declaration (class Client(BaseClient):) |
| 26 | [102400, 106496) | C6 proposed_dependency httpx 0.28.1: steps; text fragments: class_declaration (class Client(BaseClient):) |
| 27 | [106496, 110592) | C6 proposed_dependency httpx 0.28.1: steps; text fragments: class_declaration (class Client(BaseClient):), initializer (def __init__() |
| 28 | [110592, 114688) | C6 proposed_dependency httpx 0.28.1: steps; text fragments: initializer (def __init__(); C7 proposed_dependency httpx 0.28.1: callee_role, candidate_id, comparison, premises, root_call_id, steps; text fragments: call (TestClient(app)) |
| 29 | [114688, 118784) | C7 proposed_dependency httpx 0.28.1: steps; text fragments: import_origin (from fastapi.testclient import TestClient), reexport (from starlette.testclient import TestClient as TestClient), class_declaration (class TestClient(httpx.Client):) |
| 30 | [118784, 122880) | C7 proposed_dependency httpx 0.28.1: steps; text fragments: class_declaration (class TestClient(httpx.Client):), initializer (def __init__() |
| 31 | [122880, 126976) | C7 proposed_dependency httpx 0.28.1: steps; text fragments: initializer (def __init__(), call (super().__init__(), declared_base (httpx.Client), reexport (import httpx), reexport (from ._client import *), class_declaration (class Client(BaseClient):) |
| 32 | [126976, 131072) | C7 proposed_dependency httpx 0.28.1: steps; text fragments: class_declaration (class Client(BaseClient):) |
| 33 | [131072, 135168) | C7 proposed_dependency httpx 0.28.1: steps; text fragments: class_declaration (class Client(BaseClient):) |
| 34 | [135168, 139264) | C7 proposed_dependency httpx 0.28.1: steps; text fragments: class_declaration (class Client(BaseClient):) |
| 35 | [139264, 143360) | C7 proposed_dependency httpx 0.28.1: steps; text fragments: class_declaration (class Client(BaseClient):) |
| 36 | [143360, 147456) | C7 proposed_dependency httpx 0.28.1: steps; text fragments: class_declaration (class Client(BaseClient):) |
| 37 | [147456, 151552) | C7 proposed_dependency httpx 0.28.1: steps; text fragments: class_declaration (class Client(BaseClient):), initializer (def __init__() |
| 38 | [151552, 155648) | C7 proposed_dependency httpx 0.28.1: steps; text fragments: initializer (def __init__(); C8 old_dependency httpx 0.27.2: callee_role, candidate_id, comparison, premises, root_call_id, steps; text fragments: call (TestClient(app)), import_origin (from fastapi.testclient import TestClient), reexport (from starlette.testclient import TestClient as TestClient), class_declaration (class TestClient(httpx.Client):) |
| 39 | [155648, 159744) | C8 old_dependency httpx 0.27.2: steps; text fragments: class_declaration (class TestClient(httpx.Client):) |
| 40 | [159744, 163840) | C8 old_dependency httpx 0.27.2: steps; text fragments: class_declaration (class TestClient(httpx.Client):), initializer (def __init__(), call (super().__init__() |
| 41 | [163840, 167936) | C8 old_dependency httpx 0.27.2: steps; text fragments: call (super().__init__(), declared_base (httpx.Client), reexport (import httpx), reexport (from ._api import *), reexport (from ._client import Client), class_declaration (class Client(BaseClient):) |
| 42 | [167936, 172032) | C8 old_dependency httpx 0.27.2: steps; text fragments: class_declaration (class Client(BaseClient):) |
| 43 | [172032, 176128) | C8 old_dependency httpx 0.27.2: steps; text fragments: class_declaration (class Client(BaseClient):) |
| 44 | [176128, 180224) | C8 old_dependency httpx 0.27.2: steps; text fragments: class_declaration (class Client(BaseClient):) |
| 45 | [180224, 184320) | C8 old_dependency httpx 0.27.2: steps; text fragments: class_declaration (class Client(BaseClient):) |
| 46 | [184320, 188416) | C8 old_dependency httpx 0.27.2: steps; text fragments: class_declaration (class Client(BaseClient):) |
| 47 | [188416, 192512) | C8 old_dependency httpx 0.27.2: steps; text fragments: class_declaration (class Client(BaseClient):), initializer (def __init__() |
| 48 | [192512, 196608) | C8 old_dependency httpx 0.27.2: steps; text fragments: initializer (def __init__(); C9 old_dependency httpx 0.27.2: callee_role, candidate_id, comparison, premises, root_call_id, steps; text fragments: call (TestClient(app)), import_origin (from fastapi.testclient import TestClient), reexport (from starlette.testclient import TestClient as TestClient), class_declaration (class TestClient(httpx.Client):) |
| 49 | [196608, 200704) | C9 old_dependency httpx 0.27.2: steps; text fragments: class_declaration (class TestClient(httpx.Client):) |
| 50 | [200704, 204800) | C9 old_dependency httpx 0.27.2: steps; text fragments: class_declaration (class TestClient(httpx.Client):), initializer (def __init__() |
| 51 | [204800, 208896) | C9 old_dependency httpx 0.27.2: steps; text fragments: initializer (def __init__(), call (super().__init__(), declared_base (httpx.Client), reexport (import httpx), reexport (from ._client import *), class_declaration (class Client(BaseClient):) |
| 52 | [208896, 212992) | C9 old_dependency httpx 0.27.2: steps; text fragments: class_declaration (class Client(BaseClient):) |
| 53 | [212992, 217088) | C9 old_dependency httpx 0.27.2: steps; text fragments: class_declaration (class Client(BaseClient):) |
| 54 | [217088, 221184) | C9 old_dependency httpx 0.27.2: steps; text fragments: class_declaration (class Client(BaseClient):) |
| 55 | [221184, 225280) | C9 old_dependency httpx 0.27.2: steps; text fragments: class_declaration (class Client(BaseClient):) |
| 56 | [225280, 229376) | C9 old_dependency httpx 0.27.2: steps; text fragments: class_declaration (class Client(BaseClient):) |
| 57 | [229376, 233472) | C9 old_dependency httpx 0.27.2: steps; text fragments: class_declaration (class Client(BaseClient):), initializer (def __init__() |
| 58 | [233472, 237568) | C9 old_dependency httpx 0.27.2: steps; text fragments: initializer (def __init__(); C10 target_repository  : callee_role, candidate_id, comparison, premises, root_call_id, steps; text fragments: call (get_token()), import_origin (from app.utils import get_token), declaration (def get_token():) |
| 59 | [237568, 241664) | C10 target_repository  : steps; C11 target_repository  : callee_role, candidate_id, comparison, premises, root_call_id, steps; text fragments: call (get_token()), import_origin (from app.utils import get_token), declaration (def get_token():); C12 target_repository  : callee_role, candidate_id, comparison, premises, root_call_id, steps; text fragments: call (get_token()), import_origin (from app.utils import get_token), declaration (def get_token():) |
| 60 | [241664, 245760) | result.catalog_id; result.checker_version; result.correspondence_version; result.format; result.gaps; C12 target_repository  : steps |

The [machine-readable inventory](page-inventory.json) also contains actual delivery IDs/digests and precise source-expression spans. This is inspection metadata; it does not extend the delivery or establish runtime compatibility.
