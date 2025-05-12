from fastapi import FastAPI
from src.app.router.endpoints.router_fake_data import fake as routes_fake_data

def create_app(title: str, version: str) -> FastAPI:
    app = FastAPI(title=title, version=version)
    app.include_router(router=routes_fake_data)

    return app