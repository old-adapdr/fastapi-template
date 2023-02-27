"""File contains the HelloTasks container"""


class HelloTasks:
    """Tasks container for the HelloRouter"""

    @staticmethod
    def create_later(entity: object):
        print(f'hello {entity.name}')
