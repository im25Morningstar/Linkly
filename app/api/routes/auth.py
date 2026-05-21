from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.db.session import get_db
from app.schemas.user import (
    UserCreate,
    UserLogin
)

from app.models.user import User

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)

from app.repositories.user_repository import (
    get_user_by_email
)


router=APIRouter()


@router.post("/register")
def register(
        user:UserCreate,
        db:Session=Depends(get_db)
):

    existing=get_user_by_email(
        db,
        user.email
    )

    if existing:

        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    new_user=User(
        email=user.email,
        hashed_password=
        hash_password(
            user.password
        )
    )

    db.add(new_user)

    db.commit()

    return {
        "message":
        "User registered"
    }


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    db_user = get_user_by_email(
        db,
        form_data.username
    )

    if not db_user:

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        form_data.password,
        db_user.hashed_password
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token=create_access_token(
        {"sub": db_user.email}
    )

    return {
        "access_token":token,
        "token_type":"bearer"
    }