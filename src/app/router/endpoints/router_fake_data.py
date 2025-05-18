from fastapi import APIRouter
from pydantic import BaseModel
from src.app.services.service_fake_data import service_fake_data

class MessageResponse(BaseModel):
    message: str

fake = APIRouter()

@fake.get("/api/name", response_model=MessageResponse)
async def get_random_name():
    name: str = service_fake_data.get_random_name()
    return {"message": name}

@fake.get("/api/email", response_model=MessageResponse)
async def get_random_email():
    email: str = service_fake_data.get_random_email()
    return {"message": email}

@fake.get("/api/address", response_model=MessageResponse)
async def get_random_address():
    address: str = service_fake_data.get_random_address()
    return {"message": address}
