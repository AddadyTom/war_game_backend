from fastapi import APIRouter, status

from consts.elastic import GAMES_INDEX
from models.game import Game
from utils.elastic import elastic_client

game_router = APIRouter()


@game_router.post('/')
async def create_game(game: Game, status_code=status.HTTP_201_CREATED) -> dict:
    res = elastic_client.index(index=GAMES_INDEX, document=game.dict())
    return res['_id']
