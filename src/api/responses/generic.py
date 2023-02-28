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
            "headers": {
                "content-length": {
                    "description": "Content Length",
                    "type": "int"
                },
                "date": {
                    "description": "Response Date",
                    "type": "Datetime"
                },
                "server": {
                    "description": "API Server",
                    "type": "string"
                }
            }
        }
    }

    # 300s
    redirect = {
        "308": {
            "description": "Redirects from index to /docs",
            "headers": {
                "Location": {
                    "description": "Content Length",
                    "type": "int"
                },
                "content-length": {
                    "description": "Content Length",
                    "type": "int"
                },
                "date": {
                    "description": "Response Date",
                    "type": "Datetime"
                },
                "server": {
                    "description": "API Server",
                    "type": "string"
                }
            }
        }
    }

    # 400s
    unauthorized = {
        "401": {
            "model": List[Message],
            "description": "Unauthorized to view requested resource",
            "headers": {
                "content-length": {
                    "description": "Content Length",
                    "type": "int"
                },
                "date": {
                    "description": "Response Date",
                    "type": "Datetime"
                },
                "server": {
                    "description": "API Server",
                    "type": "string"
                }
            }
        }
    }
    not_found = {
        "404": {
            "model": List[Message],
            "description": "Could not find requested resource",
            "headers": {
                "content-length": {
                    "description": "Content Length",
                    "type": "int"
                },
                "date": {
                    "description": "Response Date",
                    "type": "Datetime"
                },
                "server": {
                    "description": "API Server",
                    "type": "string"
                }
            }
        },
    }
    conflict = {
        "409": {
            "model": List[Message],
            "descriptions": "The requested resource already exists!",
            "headers": {
                "content-length": {
                    "description": "Content Length",
                    "type": "int"
                },
                "date": {
                    "description": "Response Date",
                    "type": "Datetime"
                },
                "server": {
                    "description": "API Server",
                    "type": "string"
                }
            }
        }
    }
    unprocessable = {
        "422": {
            "model": List[Message],
            "descriptions": "Server could not process entity",
            "headers": {
                "content-length": {
                    "description": "Content Length",
                    "type": "int"
                },
                "date": {
                    "description": "Response Date",
                    "type": "Datetime"
                },
                "server": {
                    "description": "API Server",
                    "type": "string"
                }
            }
        }
    }

    # 500s
    server_error = {
        "500": {
            "model": List[Message],
            "description": "Server could not process request",
            "headers": {
                "content-length": {
                    "description": "Content Length",
                    "type": "int"
                },
                "date": {
                    "description": "Response Date",
                    "type": "Datetime"
                },
                "server": {
                    "description": "API Server",
                    "type": "string"
                }
            }
        },
    }
