from pydantic import BaseModel
from bank.models.address import Address
from bank.models.customer import Customer

class Account(BaseModel):
    id: int
    account_number: int
    currentBalance: int
