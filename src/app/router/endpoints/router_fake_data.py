from fastapi import HTTPException, APIRouter
from fastapi.responses import JSONResponse
from starlette.status import HTTP_503_SERVICE_UNAVAILABLE
from src.app.services.services_fake_data import service_fake_data
from pydantic import BaseModel

class MessageResponse(BaseModel):
    message: str

fake = APIRouter()

@fake.get("/random/name", response_model=MessageResponse)
async def get_random_name():
    try:
        random_name = service_fake_data.get_random_name()
        return MessageResponse(message=random_name)
    except Exception:
        return JSONResponse(
            status_code=HTTP_503_SERVICE_UNAVAILABLE,
            content={"detail": "Serviço indisponível"}
        )

@fake.get("/random/email", response_model=MessageResponse)
async def get_random_email():
    try:
        random_name = service_fake_data.get_random_email()
        return MessageResponse(message=random_name)
    except Exception:
        return JSONResponse(
            status_code=HTTP_503_SERVICE_UNAVAILABLE,
            content={"detail": "Serviço indisponível"}
        )
