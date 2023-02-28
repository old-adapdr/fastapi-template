"""
File contains responses for the '/hello' endpoint router
"""
from typing import List
from api.schema import APISchema
from .generic import GenericResponses


Schema = APISchema['hello']
GenericSchema = APISchema['generic']


class HelloResponses:
    """
    Class contains hello responses
    """

    options = {
        "200": {
            "content": None,
            "description": "Hello router options successfully retrieved",
            "headers": {
                "allow": {
                    "description": "Allowed methods for the Hello router",
                    "type": "List[string]"
                }
            }
        },
        **GenericResponses.unauthorized,
        **GenericResponses.not_found,
        **GenericResponses.server_error,
    }
    retrieve = {
        "200": {
            "model": Schema.Hello,
            "description": "Hello successfully retrieved",
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
        **GenericResponses.unauthorized,
        **GenericResponses.not_found,
        **GenericResponses.server_error,
    }
    retrieve_multiple = {
        "200": {
            "model": List[Schema.Hello],
            "description": "Hello successfully retrieved",
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
        **GenericResponses.unauthorized,
        **GenericResponses.not_found,
        **GenericResponses.server_error,
    }

    listed = {
        "200": {
            "model": List[Schema.Hello],
            "description": "HelloList successfully retrieved",
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
        **GenericResponses.unauthorized,
        **GenericResponses.not_found,
        **GenericResponses.server_error,
    }

    create = {
        "201": {
            "model": Schema.Hello,
            "description": "Hello successfully create",
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
        **GenericResponses.unauthorized,
        **GenericResponses.not_found,
        **GenericResponses.server_error,
    }

    update = {
        "201": {
            "model": Schema.Hello,
            "description": "Hello successfully updated",
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
        **GenericResponses.unauthorized,
        **GenericResponses.not_found,
        **GenericResponses.server_error,
    }
    replace = {
        "201": {
            "model": Schema.Hello,
            "description": "Hello successfully replaced",
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
        **GenericResponses.unauthorized,
        **GenericResponses.not_found,
        **GenericResponses.server_error,
    }

    delete = {
        "204": {
            "content": None,
            "description": "Hello successfully deleted",
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
        **GenericResponses.unauthorized,
        **GenericResponses.not_found,
        **GenericResponses.server_error,
    }
