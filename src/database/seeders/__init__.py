"""
Module contains database seeders
"""
from dataclasses import dataclass

from .hello_table_seeder import HelloTableSeeder


@dataclass
class Seeders:
    """
    Container holding database seeders
    """

    hello = HelloTableSeeder
