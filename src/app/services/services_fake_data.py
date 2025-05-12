from src.app.services import faker
from fastapi import HTTPException
from starlette.status import HTTP_503_SERVICE_UNAVAILABLE


class service_fake_data:
    @staticmethod
    def get_random_name():
        try:
            random_name = faker.name()
            return random_name
        except Exception:
            details_exception = "Error getting name."
            raise HTTPException(HTTP_503_SERVICE_UNAVAILABLE, detail=details_exception)

    @staticmethod
    def get_random_email():
        try:
            random_email = faker.email()
            return random_email
        except Exception:
            details_exception = "Error getting name."
            raise HTTPException(HTTP_503_SERVICE_UNAVAILABLE, detail=details_exception)