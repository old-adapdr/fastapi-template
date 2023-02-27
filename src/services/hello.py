"""File contains the HelloService class."""
from database.models import Models


class HelloService:
    """Service class for the HelloController."""

    def __init__(self):
        pass

    def create(self, data: dict):
        result = Models.Hello.create(
            data.dict()
        ).fresh()

        return result

    def get(self, uuid: str):
        result = Models.Hello.find(uuid)

        return result

    def update(self, uuid: str, data: dict):
        result = Models.Hello.where({"uuid": uuid}).update(data.dict()).get()

        return result

    def delete(self, uuid: str):
        result = Models.Hello.delete(uuid)

        return result
