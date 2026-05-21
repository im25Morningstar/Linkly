from passlib.context import CryptContext
from jose import jwt
from datetime import datetime,timedelta
from dotenv import load_dotenv
import os
from jose import JWTError

load_dotenv()

SECRET_KEY=os.getenv("SECRET_KEY")
ALGORITHM=os.getenv("ALGORITHM")

pwd_context=CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(
        password:str
):

    return pwd_context.hash(
        password
    )


def verify_password(
        plain_password:str,
        hashed_password:str
):

    return pwd_context.verify(
        plain_password,
        hashed_password
    )


def create_access_token(
        data:dict
):

    payload=data.copy()

    expire=(
        datetime.utcnow()
        +
        timedelta(minutes=30)
    )

    payload.update(
        {"exp":expire}
    )

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

def decode_token(
        token:str
):

    try:

        payload=jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload.get("sub")

    except JWTError:

        return None