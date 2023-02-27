"""
File contains generic and shared responses
"""
from typing import List
from api.schema.generic import Message


class GenericResponses:
    """
    Class contains generic and shared responses
    """

    # 200s
    success = {
        "200": {
            "model": List[Message],
            "description": "Successfully processed operation",
        }
    }

    # 300s
    redirect = {"308": {"description": "Redirects from index to /docs"}}

    # 400s
    unauthorized = {
        "401": {
            "model": List[Message],
            "description": "Unauthorized to view requested resource",
        }
    }
    not_found = {
        "404": {
            "model": List[Message],
            "description": "Could not find requested resource",
        },
    }
    conflict = {
        "409": {
            "model": List[Message],
            "descriptions": "The requested resource already exists!",
        }
    }
    unprocessable = {
        "422": {
            "model": List[Message],
            "descriptions": "Server could not process entity",
        }
    }

    # 500s
    server_error = {
        "500": {
            "model": List[Message],
            "description": "Server could not process request",
        },
    }
