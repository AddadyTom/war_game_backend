from elasticsearch_dsl import Search, Q
from fastapi import APIRouter

from consts.elastic import USERS_INDEX
from models.user import User
from utils.elastic import elastic_client

user_router = APIRouter()


@user_router.post('/auth')
async def authorize(user: User):
    return bool(Search(index=USERS_INDEX)
                .using(elastic_client)
                .query('bool', filter=[Q("term", username=user.username) & Q("term", password=user.password)])
                .execute().hits.hits)
