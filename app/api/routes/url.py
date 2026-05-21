from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from app.schemas.url import URLCreate
from app.db.session import get_db
from app.models.url import URL
from app.services.url_service import generate_short_code


router=APIRouter()


@router.post("/create")
def create_url(
    url:URLCreate,
    db:Session=Depends(get_db)
):

    code=generate_short_code()

    new_url=URL(
        original_url=url.original_url,
        short_code=code
    )

    db.add(new_url)

    db.commit()

    db.refresh(new_url)

    return {
        "short_url":
        f"http://localhost:8000/{code}"
    }