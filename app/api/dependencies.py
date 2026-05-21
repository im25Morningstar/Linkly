from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.core.security import decode_token
from app.repositories.user_repository import (
    get_user_by_email
)

oauth2_scheme=OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)


def get_current_user(
        token:str=Depends(
            oauth2_scheme
        ),
        db:Session=Depends(
            get_db
        )
):

    email=decode_token(
        token
    )

    if not email:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    user=get_user_by_email(
        db,
        email
    )

    return user