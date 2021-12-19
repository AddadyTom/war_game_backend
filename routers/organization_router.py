from fastapi import APIRouter, status
from models.organization import Organization
from utils.elastic import elastic_client
from consts.elastic import ORGANIZATIONS_INDEX
import uuid

message_router = APIRouter()


@message_router.get('/{id}')
async def get_organization():
    return


@message_router.post('/')
async def create_organization(organization: Organization, status_code=status.HTTP_201_CREATED) -> dict:
    elastic_client.create(ORGANIZATIONS_INDEX, str(uuid.uuid4()), organization.dict())
    return organization.dict()
