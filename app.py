import uvicorn
from fastapi import FastAPI

from config import CONFIG
from routers.game_router import game_router

app = FastAPI()
app.router.include_router(game_router, prefix='/game')

if __name__ == '__main__':
    uvicorn.run(app, host=CONFIG.HOST, port=CONFIG.PORT)
