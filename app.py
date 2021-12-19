import uvicorn
from fastapi import FastAPI

from config import CONFIG
from routers.game_router import game_router
from routers.user_router import user_router

app = FastAPI()
app.router.include_router(game_router, prefix='/game')
app.router.include_router(user_router, prefix="/user")

if __name__ == '__main__':
    uvicorn.run(app, host=CONFIG.HOST, port=CONFIG.PORT)
