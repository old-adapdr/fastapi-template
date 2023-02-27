"""Module contains and loads routers"""
from importlib import import_module
from typing import List
from pathlib import Path
from fastapi import APIRouter

from config.auto_loader import AutoLoader

ROUTERS: List[APIRouter] = []

# ? Add routers from ROUTERS_LOCATION -> ROUTERS
for router in Path(AutoLoader.routers_location).iterdir():
    if '__' in str(router):
        continue

    ROUTERS.append(
        import_module(f"api.routers.{router.stem}").router
    )
