import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    jwks_url: str
    audience: str
    max_catalog_items: int


settings = Settings(
    jwks_url=os.environ.get("HUB_JWKS_URL", "https://auth.partner-hub.example/.well-known/jwks.json"),
    audience=os.environ.get("HUB_AUDIENCE", "partner-hub"),
    max_catalog_items=int(os.environ.get("HUB_MAX_CATALOG_ITEMS", "5000")),
)
