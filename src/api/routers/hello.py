"""File contains endpoint router for '/hello'"""
from logging import getLogger
from uuid import UUID

from fastapi import APIRouter, Path, Query, status, Depends, BackgroundTasks
from fastapi.exceptions import HTTPException
from fastapi.responses import Response


from api.schema import APISchema
from api.responses import APIResponses
from api.services import APIServices
from api.tasks import APITasks


# ? Router Configuration
logger = getLogger(__name__)
router = APIRouter(
    prefix="/api/hello",
    tags=["Hello CRUD"],
)

# ? Router Components
Responses = APIResponses.get('hello')
Schema = APISchema.get('hello')


# ? Router Endpoints
@router.post(
    path="/",
    operation_id="api.hello.create",
    responses=Responses.create
)
async def create_hello_message(
    hello: Schema.Hello,
    service=Depends(APIServices.get("hello")),
    background=BackgroundTasks
):
    """Endpoint is used to create a `Hello` message object"""
    result = service.create(hello)
    background.add_task(APITasks.get("hello").create_later, entity=hello)

    if not result:
        raise HTTPException(status.HTTP_400_BAD_REQUEST)

    return result


@router.get(
    path="/{uuid}",
    operation_id="api.hello.retrieve",
    responses=Responses.lookup
)
async def retrieve_hello_message(
    uuid: UUID = Path(..., description="ID of the Hello Entity to retrieve"),
    service=Depends(APIServices.get("hello"))
):
    """Endpoint is used to retrieve a `Hello` message object"""
    result = service.retrieve(uuid)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.put(
    path="/{uuid}",
    operation_id="api.hello.update",
    responses=Responses.update
)
async def update_hello_message(
    hello: Schema.Hello,
    uuid: str = Path(..., description="ID of the Hello Entity to update"),
    service=Depends(APIServices.get("hello"))
):
    """Endpoint is used to update a `Hello` message object"""
    result = service.update(uuid, hello)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.delete(
    path="/{uuid}",
    operation_id="api.hello.delete",
    responses=Responses.delete
)
async def delete_hello_message(
    uuid: str = Path(..., description="ID of the Hello Entity to delete"),
    service=Depends(APIServices.get("hello"))
):
    """Endpoint is used to delete a `Hello` message object"""
    result = service.delete(uuid)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return Response(content=None, status_code=status.HTTP_204_NO_CONTENT)
