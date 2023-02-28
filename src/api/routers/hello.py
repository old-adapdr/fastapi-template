"""File contains endpoint router for '/hello'"""
from logging import getLogger
from uuid import UUID

from fastapi import APIRouter, Path, Query, status, Depends, BackgroundTasks, Response
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


@router.options(
    path="/",
    operation_id="api.hello.options",
    responses=Responses.options
)
async def hello_options(
    service=Depends(APIServices.get("hello"))
):
    """Endpoint is used to find options for the `Hello` router"""
    result = service.options()
    print(result)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return Response(headers={"allow": str(result)})


@router.post(
    path="/",
    operation_id="api.hello.create",
    responses=Responses.create
)
async def create_hello_message(
    hello: Schema.Hello,
    background: BackgroundTasks,
    service=Depends(APIServices.get("hello"))
):
    """Endpoint is used to create a `Hello` entity"""
    result = service.create(hello)

    # ? Is executed after the router has returned a response
    background.add_task(APITasks.get("hello").do_after, entity="hello")

    if not result:
        raise HTTPException(status.HTTP_400_BAD_REQUEST)

    return result


@router.get(
    path="/",
    operation_id="api.hello.retrieve-multiple",
    responses=Responses.retrieve_multiple
)
async def retrieve_mulltiple(
    name: str = Query(None, description="Name of the Hello Entity to retrieve"),
    page_nr: int = Query(1, description="Page number to retrieve"),
    limit: int = Query(10, description="Number of items to retrieve"),
    service=Depends(APIServices.get("hello"))
):
    """Endpoint is used to retrieve a list of `Hello` entities"""

    result = service.retrieve_multiple(name=name, limit=limit, page_nr=page_nr)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.get(
    path="/{uuid}",
    operation_id="api.hello.retrieve",
    responses=Responses.retrieve
)
async def retrieve_hello_message(
    uuid: UUID = Path(None, description="Unique Identifier for the Hello Entity to retrieve"),
    service=Depends(APIServices.get("hello"))
):
    """Endpoint is used to retrieve a `Hello` entity"""

    result = service.retrieve(uuid)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.put(
    path="/{uuid}",
    operation_id="api.hello.replace",
    responses=Responses.replace
)
async def replace_hello_message(
    hello: Schema.Hello,
    uuid: str = Path(..., description="Unique Identifier for the Hello Entity to update"),
    service=Depends(APIServices.get("hello"))
):
    """Endpoint is used to replace a `Hello` entity"""
    result = service.replace(uuid, hello)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.patch(
    path="/{uuid}",
    operation_id="api.hello.update",
    responses=Responses.update
)
async def update_hello_message(
    hello: Schema.Hello,
    uuid: str = Path(..., description="Unique Identifier for the Hello Entity to update"),
    service=Depends(APIServices.get("hello"))
):
    """Endpoint is used to update a `Hello` entity"""
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
    uuid: str = Path(..., description="Unique Identifier for the Hello Entity to delete"),
    service=Depends(APIServices.get("hello"))
):
    """Endpoint is used to delete a `Hello` entity"""
    result = service.delete(uuid)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return Response(content=None, status_code=status.HTTP_204_NO_CONTENT)
