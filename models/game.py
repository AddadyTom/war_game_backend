from pydantic import BaseModel
from typing import List
from models.team import Team


class Game(BaseModel):
    teams: List[Team]
    name: str
    id: str
