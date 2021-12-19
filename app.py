import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from config import CONFIG
from routers.game_router import game_router
from routers.user_router import user_router

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.router.include_router(game_router, prefix='/game')
app.router.include_router(user_router, prefix="/user")

if __name__ == '__main__':
    uvicorn.run(app, host=CONFIG.HOST, port=CONFIG.PORT)
