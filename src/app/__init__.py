from fastapi import FastAPI
from src.app.router.endpoints.router_fake_data import fake as routes_fake_data
from fastapi.staticfiles import StaticFiles
import os
from src.app.router.endpoints.router_root import root as routes_root

def create_app(title: str, version: str) -> FastAPI:
    app = FastAPI(title=title, version=version)

    app.include_router(router=routes_fake_data)
    app.include_router(router=routes_root)
    app.mount("/static", StaticFiles(directory=os.path.join(os.path.dirname(__file__), "static")), name="static")

    return app