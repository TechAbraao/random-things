from src.app.schemas.base import BaseSchema
from typing import Dict, Any

class MessageResponse(BaseSchema):
    message: str

class MessageResponseEmail(BaseSchema):
    message: Dict[str, Any]
