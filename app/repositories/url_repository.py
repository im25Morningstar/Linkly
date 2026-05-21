from sqlalchemy.orm import Session
from app.models.url import URL


def get_by_short_code(
        db:Session,
        short_code:str
):

    return db.query(URL).filter(
        URL.short_code==short_code
    ).first()

def get_user_links(
        db:Session,
        user_id:int
):

    return db.query(
        URL
    ).filter(
        URL.user_id==user_id
    ).all()