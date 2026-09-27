# depscan-heldout-1 (held-out evaluation repo)

A FastAPI service used as a **held-out** test for depscan: its answers (`expected.yaml`) were written and committed
before depscan was ever run on it, and depscan's logic and prompts were not changed after seeing its results.

| advisory | package | expected | why |
|---|---|---|---|
| CVE-2026-54283 | starlette (via fastapi) | affected | `Form(...)` endpoint → `request.form()` parses urlencoded bodies without limits |
| CVE-2026-54282 | starlette | not affected | the app never reads `request.url` |
| CVE-2026-53540 | python-multipart | not affected | only direct `parse_form()` callers; starlette does not use it |
| CVE-2026-48524 | pyjwt | affected | bearer tokens go to `PyJWKClient.get_signing_key_from_jwt` (unknown kid → refetch) |
| CVE-2026-48523 | pyjwt | not affected | `decode` gets `signing_key.key`, not a `PyJWK` |
| CVE-2026-48526 | pyjwt | not affected | `algorithms=["RS256"]` only |
| CVE-2026-48522 | pyjwt | not affected | JWKS URI from configuration |
| CVE-2026-48525 | pyjwt | not affected | no detached (`b64=false`) JWS |
| CVE-2026-41066 | lxml | affected | uploaded XML into `iterparse()` with default entity resolution |

This directory is skipped by depscan's scanner.
