from fastapi import APIRouter, status
from models.message import Message
from utils.elastic import elastic_client
from consts.elastic import MESSAGES_INDEX
import uuid

message_router = APIRouter()


@message_router.get('/{id}')
async def get_message():
    return


@message_router.post('/')
async def create_message(message: Message, status_code=status.HTTP_201_CREATED) -> dict:
    elastic_client.create(MESSAGES_INDEX, str(uuid.uuid4()), message.dict())
    return message.dict()
