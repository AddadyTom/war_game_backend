from pydantic import BaseModel
from typing import List
from models.organization import Organization


class Team(BaseModel):
    organizations: List[Organization]
    color: str
    name: str
    picture: bytes
