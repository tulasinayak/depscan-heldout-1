from fastapi import FastAPI

from hub.routers import catalog, contact

app = FastAPI(title="Partner Hub", version="0.4.0")
app.include_router(catalog.router)
app.include_router(contact.router)


@app.get("/healthz")
async def healthz():
    return {"status": "ok"}
