# Partner Hub

A small FastAPI service for supplier partners:

- `PUT /catalog` replaces a partner's product catalogue from an uploaded XML file
- `GET /catalog` returns the current catalogue
- `POST /contact` accepts a contact form
- `GET /healthz` for the load balancer

Partners authenticate with RS256 bearer tokens issued by the partner identity service; signing keys are fetched
from its JWKS endpoint.

## Configuration

| variable | default |
|---|---|
| `HUB_JWKS_URL` | `https://auth.partner-hub.example/.well-known/jwks.json` |
| `HUB_AUDIENCE` | `partner-hub` |
| `HUB_MAX_CATALOG_ITEMS` | `5000` |

## Run

```bash
pip install -r requirements.txt uvicorn
uvicorn hub.main:app
```

Dependencies are pinned with pip-compile from `requirements.in`.
