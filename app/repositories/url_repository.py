from sqlalchemy.orm import Session
from app.models.url import URL


def get_by_short_code(
        db:Session,
        short_code:str
):

    return db.query(URL).filter(
        URL.short_code==short_code
    ).first()