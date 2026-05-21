import random
import string

from sqlalchemy.orm import Session
from app.repositories.url_repository import (
    get_by_short_code
)


def generate_short_code(
        db:Session,
        length=6
):

    characters=(
        string.ascii_letters
        +
        string.digits
    )

    while True:

        code=''.join(
            random.choice(characters)
            for _ in range(length)
        )

        existing=get_by_short_code(
            db,
            code
        )

        if not existing:
            return code