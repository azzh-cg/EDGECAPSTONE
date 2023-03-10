from pydantic import BaseModel
from bank.models.customer import Customer

class Account(BaseModel):
    id: int
    account_number: int
    customer: Customer
    current_balance: int
