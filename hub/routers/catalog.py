from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from hub.auth import current_partner
from hub.catalog import read_items
from hub.config import settings

router = APIRouter(prefix="/catalog", tags=["catalog"])
_catalogs: dict[str, list[dict]] = {}


@router.put("", status_code=202)
async def replace_catalog(upload: UploadFile = File(...), partner: dict = Depends(current_partner)):
    if upload.content_type not in ("application/xml", "text/xml"):
        raise HTTPException(415, "catalog must be XML")
    items = read_items(upload.file, settings.max_catalog_items)
    _catalogs[partner["partner_id"]] = items
    return {"items": len(items)}


@router.get("")
async def get_catalog(partner: dict = Depends(current_partner)):
    return _catalogs.get(partner["partner_id"], [])
