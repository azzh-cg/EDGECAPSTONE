import uvicorn
from fastapi import FastAPI
from bank.repositories.account import AccountRepository
from bank.repositories.address import AddressRepository
from bank.repositories.customer import CustomerRepository
from bank.services.account import AccountService
from bank.models.account import Account
from typing import List
app = FastAPI()
account_repository = AccountRepository()
address_repository = AddressRepository()
customer_repository = CustomerRepository()
account_service = AccountService(account_repository, address_repository, customer_repository)


@app.get('/api/accounts')
async def retrieve_accounts():
    responses = account_service.get_all()
    return responses

@app.get('/api/account/{account_number}')
async def retrieve_account_by_num(account_number):
   responses = account_service.get_account(account_number)
   return responses

@app.post("/account/")
async def create_account(account:Account):
    return account_service.add_new(account)

@app.post("/account/withdrawal")
async def withdrawal(account:Account, withdrawal_amt):
    return account_service.withdrawal(account, withdrawal_amt)



# if __name__ == "__main__":
#     uvicorn.run("app:app", host="127.0.0.1", port=8080, reload=True,
#                 timeout_keep_alive=3600, workers=10)


# import uvicorn
# from fastapi import FastAPI

# app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


#  # at last, the bottom of the file/module
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=5049)

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=5049, reload=True,
                timeout_keep_alive=3600, workers=10)