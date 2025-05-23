from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from starlette.status import HTTP_503_SERVICE_UNAVAILABLE
from src.app.services.service_fake_data import service_fake_data
import time

class MessageResponse(BaseModel):
    message: str

class MessageResponseEmail(BaseModel):
    message: dict

fake = APIRouter()

@fake.get("/api/name", response_model=MessageResponse)
async def get_random_name():
    try:
        time.sleep(5)
        name: str = service_fake_data.get_random_name()
        return {"message": name}
    except Exception as error:
        raise HTTPException(
            status_code=HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Error generating name: {str(error)}"
        )

@fake.get("/api/email", response_model=MessageResponse)
async def get_random_email():
    try:
        email: str = service_fake_data.get_random_email()
        return {"message": email}
    except Exception as error:
        raise HTTPException(
            status_code=HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Error generating email: {str(error)}"
        )

@fake.get("/api/address", response_model=MessageResponseEmail)
async def get_random_address():
    try:
        address: dict = service_fake_data.get_random_address()
        return {"message": address}
    except Exception as error:
        raise HTTPException(
            status_code=HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Error generating address: {str(error)}"
        )
