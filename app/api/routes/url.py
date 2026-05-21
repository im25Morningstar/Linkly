from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from app.schemas.url import URLCreate
from app.db.session import get_db
from app.models.url import URL
from app.services.url_service import generate_short_code

from app.api.dependencies import get_current_user
from app.models.user import User
router=APIRouter()


@router.post("/shorten")
def create_url(
    url:URLCreate,
    db:Session=Depends(get_db),
    current_user:User=Depends(
        get_current_user
    )
):

    code=generate_short_code(
        db
    )

    new_url=URL(
        original_url=url.original_url,
        short_code=code,
        user_id=current_user.id
    )

    db.add(
        new_url
    )

    db.commit()

    db.refresh(
        new_url
    )

    return {
        "short_url":
        f"http://localhost:8000/{code}"
    }

from fastapi.responses import RedirectResponse
from fastapi import HTTPException
from app.repositories.url_repository import (
    get_by_short_code
)


@router.get("/{short_code}")
def redirect_url(
    short_code:str,
    db:Session=Depends(get_db)
):

    url=get_by_short_code(
        db,
        short_code
    )

    if not url:
        raise HTTPException(
            status_code=404,
            detail="URL not found"
        )

    return RedirectResponse(
        url.original_url
    )