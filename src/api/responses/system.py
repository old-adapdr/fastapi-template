"""
File contains responses for the system endpoint router
"""
from fastapi.responses import HTMLResponse

from .generic import GenericResponses


class SystemResponses:
    """
    Class contains system responses
    """

    index = {
        "200": {
            "class": HTMLResponse,
            "description": "HTML resource successfully served by the system",
        },
        **GenericResponses.not_found,
        **GenericResponses.server_error,
        **GenericResponses.unauthorized,
    }
