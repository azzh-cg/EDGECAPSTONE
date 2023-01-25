from pydantic import BaseModel

class Address(BaseModel):
    id: int
    address: str
    city: str
    zipcode: str

    def __eq__(self, other):
        return self.id == other.id and self.address == other.address and \
            self.city == other.city and self.zipcode == other.zipCode