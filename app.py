import uvicorn
from fastapi import FastAPI

from config import CONFIG
from routers.example_router import example_router

app = FastAPI()
app.router.include_router(example_router, prefix='/example')

if __name__ == '__main__':
    uvicorn.run(app, host=CONFIG.HOST, port=CONFIG.PORT)
