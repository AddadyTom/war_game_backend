from fastapi import APIRouter, status
from models.game import Game
from utils.elastic import elastic_client
from consts.elastic import GAMES_INDEX
import uuid

game_router = APIRouter()


@game_router.get('/{id}')
async def get_game():
    return


@game_router.post('/')
async def create_game(game: Game, status_code=status.HTTP_201_CREATED) -> dict:
    elastic_client.create(GAMES_INDEX, str(uuid.uuid4()), game.dict())
    return game.dict()
