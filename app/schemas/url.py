from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class URLCreate(BaseModel):

    original_url:str

    custom_alias:Optional[str]=None

    expires_at:Optional[datetime]=None


class URLResponse(BaseModel):

    short_url:str