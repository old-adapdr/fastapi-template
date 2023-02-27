"""
File contains seeder for the 'hello' table
"""
from uuid import uuid4

from masoniteorm.seeds import Seeder

from database.models.hello import Hello


class HelloTableSeeder(Seeder):
    """
    Seeder for the 'hello' table
    """

    def run(self):
        """
        Run the database seeds.
        """
        Hello.create({"uid": uuid4(), "name": "John Doe"})
