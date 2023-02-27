"""
File contains migration to create `hello` table.
"""

from masoniteorm.migrations import Migration


class CreateHelloTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("hello") as table:
            table.uuid("uuid").primary()
            table.string("name")

            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("hello")
