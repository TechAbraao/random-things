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
            details_exception = "Error getting e-mail."
            raise HTTPException(HTTP_503_SERVICE_UNAVAILABLE, detail=details_exception)

    @staticmethod
    def get_random_address():
        try:
            raw_address = faker.address()
            lines = raw_address.split('\n')

            if len(lines) < 3:
                raise ValueError("Address format is not as expected.")

            street = lines[0].strip()
            neighborhood = lines[1].strip()
            zip_city_state = lines[2].strip()

            zip_code, rest = zip_city_state.split(' ', 1)
            city, state = rest.rsplit('/', 1)

            return {
                "street": street,
                "neighborhood": neighborhood,
                "zip_code": zip_code,
                "city": city.strip(),
                "state": state.strip()
            }

        except Exception:
            raise HTTPException(
                HTTP_503_SERVICE_UNAVAILABLE,
                detail="Error generating random address."
            )