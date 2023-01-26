from pydantic import BaseModel

class Address(BaseModel):
    id: int
    address: str
    city: str
    zipcode: str