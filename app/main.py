from fastapi import FastAPI

from app.db.base import Base
from app.db.session import engine

from app.api.routes.url import router
from app.api.routes.auth import router as auth_router


Base.metadata.create_all(
    bind=engine
)

app=FastAPI(
    title="Linkly"
)

app.include_router(
    router,
    tags=["URL"]
)

app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"]
)


@app.get("/")
def home():

    return {
        "message":"Linkly API running"
    }