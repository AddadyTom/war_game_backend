from datetime import datetime
from typing import List

from pydantic import BaseModel


class Character(BaseModel):
    name: str
    description: str
    section: str


class TimeStop(BaseModel):
    time: datetime
    stop_reason: str


class StartingPoint(BaseModel):
    description: str


class Role(BaseModel):
    name: str
    description: str
    section: str


class Resource(BaseModel):
    name: str
    description: str
    section: str


class Game(BaseModel):
    name: str
    sections: List[str]
    game_mode: str
    game_date: datetime
    starting_point: StartingPoint
    start_time: datetime
    end_time: datetime
    time_stops: List[TimeStop]
    characters: List[Character]
    roles: List[Role]
    resources: List[Resource]
    rule_type: str
