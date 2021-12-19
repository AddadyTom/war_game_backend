from fastapi import APIRouter, status

from consts.elastic import GAMES_INDEX
from models.game import Game
from utils.elastic import elastic_client

game_router = APIRouter()


@game_router.get('/{id}')
async def get(id: str):
    elastic_client.get(index=GAMES_INDEX, id=id)


@game_router.get('/')
async def get_by_name(name: str):
    Search(index=GAMES_INDEX) \
        .using(elastic_client) \
        .query("match", name=name)


@game_router.post('/')
async def create_game(game: Game, status_code=status.HTTP_201_CREATED) -> dict:
    elastic_client.create(GAMES_INDEX, str(uuid.uuid4()), game.dict())
    return game.dict()
