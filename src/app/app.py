from fastapi import Request
from werkzeug.exceptions import ServiceUnavailable
from ... import create_app

app = create_app("First project", "1.0.0")

@app.get("/")
async def root():
    try:
        return {"message": "Welcome to my first project in FastAPI!"}
    except Exception:
        return ServiceUnavailable()

@app.get("/users/random")
async def random_user():
    pass
