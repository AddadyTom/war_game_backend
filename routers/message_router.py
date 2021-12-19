from typing import List

from elasticsearch_dsl import Search
from fastapi import APIRouter, status
from pydantic import BaseModel

from consts.elastic import MESSAGES_INDEX
from models.message import Message
from utils.elastic import elastic_client

message_router = APIRouter()


@message_router.get('/{id_}')
async def get(id_: str):
    elastic_client.get(index=MESSAGES_INDEX, id=id_)


@message_router.get('/')
async def get_by_content(content: str):
    Search(index=MESSAGES_INDEX) \
        .using(elastic_client) \
        .query("match", content=content)


class AuthorsRequest(BaseModel):
    authors: List[str]


@message_router.post('/authors')
async def get_by_authors(request: AuthorsRequest):
    Search(index=MESSAGES_INDEX) \
        .using(elastic_client) \
        .query("terms", author=request.authors)


@message_router.post('/')
async def create_message(message: Message, status_code=status.HTTP_201_CREATED) -> dict:
    elastic_client.index(index=MESSAGES_INDEX, document=message.dict())
    return message.dict()
