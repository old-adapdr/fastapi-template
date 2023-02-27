"""
Module contains and loads routers
"""
from importlib import import_module
from typing import List
from pathlib import Path
from fastapi import APIRouter


ROUTERS_LOCATION = "api/routers"
ROUTERS: List[APIRouter] = []

# ? Add routers from ROUTERS_LOCATION -> ROUTERS
for router in Path(ROUTERS_LOCATION).iterdir():
    if '__' not in str(router):
        ROUTERS.append(
            import_module(f"api.routers.{router.stem}").router
        )
