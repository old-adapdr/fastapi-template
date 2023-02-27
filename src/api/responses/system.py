"""
File contains responses for the system endpoint router
"""
from fastapi.responses import HTMLResponse

from .generic import Generic


class System:
    """
    Class contains system responses
    """

    index = {
        "200": {
            "class": HTMLResponse,
            "description": "HTML resource successfully served by the system",
        },
        **Generic.not_found,
        **Generic.server_error,
        **Generic.unauthorized,
    }
