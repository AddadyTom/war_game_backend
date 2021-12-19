from pydantic import BaseModel


class Person(BaseModel):
    name: str
    age: int
    country: str
    organization_name: str
    image: bytes
