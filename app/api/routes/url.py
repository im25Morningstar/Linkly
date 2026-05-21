from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from app.schemas.url import URLCreate
from app.db.session import get_db
from app.models.url import URL
from app.services.url_service import generate_short_code

from app.api.dependencies import get_current_user
from app.models.user import User
from app.repositories.url_repository import (
    get_user_links
)

from fastapi.responses import RedirectResponse
from fastapi import HTTPException
from app.repositories.url_repository import (
    get_by_short_code
)


router=APIRouter()

@router.post("/shorten")
def create_url(
    url:URLCreate,
    db:Session=Depends(get_db),
    current_user:User=Depends(
        get_current_user
    )
):

    code=(
        url.custom_alias
        if url.custom_alias
        else generate_short_code(db)
    )

    existing=get_by_short_code(
        db,
        code
    )

    if existing:

        raise HTTPException(
            status_code=400,
            detail="Alias already exists"
        )

    new_url=URL(
        original_url=url.original_url,
        short_code=code,
        user_id=current_user.id,
        expires_at=url.expires_at
    )

    db.add(new_url)

    db.commit()

    db.refresh(new_url)

    return {
        "short_url":
        f"http://localhost:8000/{code}"
    }



@router.get("/my-links")
def my_links(
    current_user:User=Depends(
        get_current_user
    ),
    db:Session=Depends(
        get_db
    )
):

    links=get_user_links(
        db,
        current_user.id
    )

    result=[]

    for link in links:

        result.append(
            {
                "original_url":
                link.original_url,

                "short_code":
                link.short_code,

                "click_count":
                link.click_count
            }
        )

    return {
        "total_links":
        len(result),

        "links":
        result
    }

from datetime import datetime


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

    if (
        url.expires_at
        and
        datetime.utcnow()
        > url.expires_at
    ):

        raise HTTPException(
            status_code=400,
            detail="Link expired"
        )

    url.click_count += 1

    db.commit()

    return RedirectResponse(
        url.original_url
    )

