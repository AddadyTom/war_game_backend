from fastapi import APIRouter, status
from models.team import Team
from utils.elastic import elastic_client
from consts.elastic import TEAMS_INDEX
import uuid

message_router = APIRouter()


@message_router.get('/{id}')
async def get_team():
    return


@message_router.post('/')
async def create_message(team: Team, status_code=status.HTTP_201_CREATED) -> dict:
    elastic_client.create(TEAMS_INDEX, str(uuid.uuid4()), team.dict())
    return team.dict()
