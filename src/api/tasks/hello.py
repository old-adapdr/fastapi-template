"""File contains the HelloTasks container"""
from api.schema.hello import HelloSchema


class HelloTasks:
    """Tasks container for the HelloRouter"""

    @staticmethod
    async def do_after(entity: HelloSchema):
        print(f'hello {entity.name}')
