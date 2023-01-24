from pydantic import BaseModel
from edgecapstone.models.address import Address

class Customer(BaseModel):
    id: int
    first_name: str
    last_name: str
    address: Address
    email: str

    def __eq__(self, other):
        return self.id == other.id and self.first_name == other.first_name and \
            self.last_name == other.last_name and self.address = other.address and \
            self.email == other.email

