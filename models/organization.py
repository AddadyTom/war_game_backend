from pydantic import BaseModel
from models.person import Person
from typing import List


class Organization(BaseModel):
    address: str
    country: str
    flag: bytes
    persons: List[Person]
