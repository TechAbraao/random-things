from fastapi import APIRouter, HTTPException
from src.app.schemas.response import MessageResponse, MessageResponseEmail
from starlette.status import HTTP_503_SERVICE_UNAVAILABLE
from src.app.services.service_fake_data import service_fake_data
import asyncio

fake = APIRouter()

@fake.get("/api/name", response_model=MessageResponse)
async def get_random_name():
    try:
        await asyncio.sleep(3)
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
        await asyncio.sleep(3)
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
        await asyncio.sleep(3)
        address: dict = service_fake_data.get_random_address()
        return {"message": address}
    except Exception as error:
        raise HTTPException(
            status_code=HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Error generating address: {str(error)}"
        )
