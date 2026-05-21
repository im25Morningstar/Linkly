from fastapi import FastAPI

from app.db.base import Base
from app.db.session import engine

from app.api.routes.url import router


Base.metadata.create_all(
    bind=engine
)


app=FastAPI(
    title="URL Shortener API"
)

app.include_router(
    router,
    prefix="/url",
    tags=["URL"]
)


@app.get("/")
def home():

    return {
        "message":"API running"
    }