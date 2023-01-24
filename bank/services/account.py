
from bank.models.account import Account
from bank.repositories.account import AccountRepository


class AccountService():
    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    def add_new(self, account: Account):
        address = self.address_respository.get_by_id(account.address.id)
        account.customer.address = address
        customer = self.customer_respository.get_by_id(account.address.id)
        account.customer = customer
        return self.account_repository.insert(account)

    def get_one(self, account_number):
        account = self.account_repository.get_by_number(account_number)
        return account

    def get_all(self):
        return self.account_repository.get_all()

    def withdrawal(self, account_number):
        return self.account_repository.execute_withdrawal(account_number)

    def deposit(self, account_number):
        return self.account_repository.execute_deposit(account_number)
    
    def close_account(self, account_number):
        return self.account_repository.close_account(account_number)