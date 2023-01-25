
from bank.models.account import Account
from bank.repositories.account import AccountRepository



class AccountService():
    def __init__(self, account_repository: AccountRepository, address_repository : AddressRepository, customer_repository : CustomerRepository):
        self.account_repository = account_repository
        self.address_repository = address_repository
        self.customer_repository = customer_repository

    def add_new(self, account: Account):
        self.inserted_address = self.address_repository.insert(account.customer.address)
        account.customer.address = self.inserted_address
        self.inserted_customer = self.customer_repository.insert(account.customer)
        account.customer = self.inserted_customer
        self.inserted_account = self.account_repository(account.customer)
        return self.inserted_account

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