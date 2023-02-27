"""
File contains responses for the '/hello' endpoint router
"""
from typing import List
from api.schema import APISchema
from .generic import Generic


Schema = APISchema['hello']


class Hello:
    """
    Class contains hello responses
    """

    lookup = {
        "200": {
            "model": Schema.Hello,
            "description": "Hello successfully retrieved",
        },
        **Generic.unauthorized,
        **Generic.not_found,
        **Generic.server_error,
    }

    listed = {
        "200": {
            "model": List[Schema.Hello],
            "description": "HelloList successfully retrieved",
        },
        **Generic.unauthorized,
        **Generic.not_found,
        **Generic.server_error,
    }

    create = {
        "201": {
            "model": Schema.Hello,
            "description": "Hello successfully create",
        },
        **Generic.unauthorized,
        **Generic.not_found,
        **Generic.server_error,
    }

    update = {
        "201": {
            "model": Schema.Hello,
            "description": "Hello successfully updated",
        },
        **Generic.unauthorized,
        **Generic.not_found,
        **Generic.server_error,
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
        **Generic.unauthorized,
        **Generic.not_found,
        **Generic.server_error,
    }
