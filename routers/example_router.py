from fastapi import APIRouter

example_router = APIRouter()


@example_router.get('/')
async def example():
    return
