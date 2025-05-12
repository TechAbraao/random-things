from fastapi import FastAPI

def create_app(title: str, version: str) -> FastAPI:
    app = FastAPI(
        title=title,
        version=version
    )
    return app