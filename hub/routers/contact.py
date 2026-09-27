from datetime import datetime, timezone

from fastapi import APIRouter, Form

router = APIRouter(tags=["contact"])
_inbox: list[dict] = []


@router.post("/contact", status_code=201)
async def send_message(name: str = Form(..., max_length=120), email: str = Form(..., max_length=254),
                       message: str = Form(..., max_length=4000)):
    _inbox.append({"name": name, "email": email, "message": message,
                   "received": datetime.now(timezone.utc).isoformat()})
    return {"queued": len(_inbox)}
