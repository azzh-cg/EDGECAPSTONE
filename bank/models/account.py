from pydantic import BaseModel
from bank.models.address import Address
from bank.models.customer import Customer

class Account(BaseModel):
    id: int
    account_number: int
    currentBalance: int

    def __eq__(self, other):
        return self.id == other.id and self.account_number == other.account_number and \
        self.current_balance = other.current_balance