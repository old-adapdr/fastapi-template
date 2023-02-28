"""File contains seeder for the 'hello' table"""
from uuid import uuid4

from masoniteorm.seeds import Seeder

from databases.models.hello import HelloModel


class HelloTableSeeder(Seeder):
    """Seeder for the 'hello' table"""

    def run(self):
        """Run the database seeds."""
        HelloModel.create({"uid": uuid4(), "name": "John Doe"})
