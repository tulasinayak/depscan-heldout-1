import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from hub.config import settings

_bearer = HTTPBearer()
_jwks = jwt.PyJWKClient(settings.jwks_url, cache_keys=True, lifespan=900)


def current_partner(credentials: HTTPAuthorizationCredentials = Depends(_bearer)) -> dict:
    token = credentials.credentials
    try:
        signing_key = _jwks.get_signing_key_from_jwt(token)
        claims = jwt.decode(token, signing_key.key, algorithms=["RS256"], audience=settings.audience)
    except jwt.PyJWTError as exc:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "invalid token") from exc
    if "partner_id" not in claims:
        raise HTTPException(status.HTTP_403_FORBIDDEN, "not a partner token")
    return claims
