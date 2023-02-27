"""
File contains responses for the '/hello' endpoint router
"""
from typing import List
from api.schema import APISchema
from .generic import GenericResponses


Schema = APISchema['hello']


class HelloResponses:
    """
    Class contains hello responses
    """

    lookup = {
        "200": {
            "model": Schema.Hello,
            "description": "Hello successfully retrieved",
        },
        **GenericResponses.unauthorized,
        **GenericResponses.not_found,
        **GenericResponses.server_error,
    }

    listed = {
        "200": {
            "model": List[Schema.Hello],
            "description": "HelloList successfully retrieved",
        },
        **GenericResponses.unauthorized,
        **GenericResponses.not_found,
        **GenericResponses.server_error,
    }

    create = {
        "201": {
            "model": Schema.Hello,
            "description": "Hello successfully create",
        },
        **GenericResponses.unauthorized,
        **GenericResponses.not_found,
        **GenericResponses.server_error,
    }

    update = {
        "201": {
            "model": Schema.Hello,
            "description": "Hello successfully updated",
        },
        **GenericResponses.unauthorized,
        **GenericResponses.not_found,
        **GenericResponses.server_error,
    }

    """
    Delete is a special case and requires an additional parameter
    to be set for the specific endpoint controller to remove body/content.
    """
    delete = {
        "204": {
            # 204 No Content
            "description": "Hello successfully deleted"
        },
        **GenericResponses.unauthorized,
        **GenericResponses.not_found,
        **GenericResponses.server_error,
    }
