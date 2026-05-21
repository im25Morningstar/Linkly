from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey
)

from datetime import datetime
from app.db.base import Base

class URL(Base):

    __tablename__="urls"

    id=Column(Integer,primary_key=True,index=True)

    original_url=Column(
        String,
        nullable=False
    )

    short_code=Column(
        String,
        unique=True,
        index=True,
        nullable=False
    )

    user_id=Column(
        Integer,
        ForeignKey("users.id")
    )

    click_count=Column(
        Integer,
        default=0
    )

    created_at=Column(
        DateTime,
        default=datetime.utcnow
    )