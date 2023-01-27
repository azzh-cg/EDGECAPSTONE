from pydantic import BaseModel
from bank.models.address import Address

class Customer(BaseModel):
    id: int
    first_name: str
    last_name: str
    address: Address
    email: str


