from pydantic import BaseModel
from datetime import datetime


class Message(BaseModel):
    author: str
    time: datetime
    content: str
