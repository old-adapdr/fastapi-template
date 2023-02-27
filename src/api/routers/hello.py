"""File contains endpoint router for '/hello'"""
from logging import getLogger

from fastapi import APIRouter, Path, Query, status
from fastapi.exceptions import HTTPException
from fastapi.responses import Response

from api.schema import APISchema
from api.responses import APIResponses


# ? Router Configuration
logger = getLogger(__name__)
Responses = APIResponses.get('hello')
Schema = APISchema.get('hello')
router = APIRouter(
    prefix="/api/hello",
    tags=["Hello"],
)


# ? Router endpoints
@router.post(
    path="/",
    operation_id="api.hello.create",
    responses=Responses.create
)
async def create_hello(hello: Schema.Hello):
    """Endpoint is used to create a `Hello` Object"""
    result = Models.Hello.create(
        hello.dict()
    ).fresh()

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.get(
    path="/{hello_id}",
    operation_id="api.hello.lookup",
    responses=Responses.lookup
)
async def lookup_hello(
    hello_id: int = Path(..., description="ID of the Hello Entity to retrieve")
):
    """Endpoint is used to lookup a `Hello` Object"""
    result = Models.Hello.find(hello_id)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.get(
    path="/",
    operation_id="api.hello.listed",
    responses=Responses.listed
)
async def listed_hello(
    limit: int = Query(..., description="Limit # records retrieved"),
    page_nr: int = Query(..., description="First entry of the list"),
):
    """Endpoint is used to listed a `Hello` Object"""

    result = Models.Hello.simple_paginate(limit, page_nr).get()

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.put(
    path="/{hello_id}",
    operation_id="api.hello.update",
    responses=Responses.update
)
async def update_hello(
    hello: Schema.Hello,
    hello_id: str = Path(..., description="ID of the Hello Entity to update"),
):
    """Endpoint is used to update a `Hello` Object"""
    result = Models.Hello.where({"uuid": hello_id}).update(hello.dict()).get()

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return result


@router.delete(
    path="/{hello_id}",
    operation_id="api.hello.delete",
    responses=Responses.delete
)
async def delete_hello(
    hello_id: str = Path(..., description="ID of the Hello Entity to delete"),
):
    """Endpoint is used to delete a `Hello` Object"""
    result = Models.Hello.delete(hello_id)

    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return Response(content=None, status_code=status.HTTP_204_NO_CONTENT)
