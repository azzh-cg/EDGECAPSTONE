import unittest
from unittest.mock import Mock
from bank.models.address import Address
from bank.models.customer import Customer
from bank.models.account import Account
from bank.repositories.address import AddressRepository
from bank.repositories.account import AccountRepository
from bank.repositories.customer import CustomerRepository
from bank.services.account import AccountService


class TestAccountService(unittest.TestCase):
    def setUp(self):
        self.inserted_address = Address(id=0, address="1234 Lane Rd", city='Los Angeles', state='California', zipcode='90210')
        self.inserted_customer = Customer(id=0, first_name = "Jane", last_name="Doe", address = self.inserted_address, email = "janedoe@gmail.com")
        self.inserted_account = Account(id=0, account_number=0, customer=self.inserted_customer, current_balance=25)
        self.addressRepository = AddressRepository()
        self.customerRepository = CustomerRepository()
        self.accountRepository = AccountRepository()
        self.accountService = AccountService(self.accountRepository, self.addressRepository, self.customerRepository)
    
    def tearDown(self):
        self.accountService.close_account(self.inserted_account)

    def test_add_new_account(self):
        new_acc = self.accountService.add_new(self.inserted_account)
        self.assertEqual(new_acc, self.inserted_account)
        

    def test_get_one_order(self):
        new_acc = self.accountService.add_new(self.inserted_account)
        get_acc = self.accountService.get_one(new_acc.account_number)
        self.assertEqual(get_acc, self.inserted_account)

    def test_get_all_orders(self):
        new_acc = self.accountService.add_new(self.inserted_account)

        address1 = Address(id=1, address="5678 Street Dr", city='Denver', state='Colorado', zipcode=80012)
        customer1 = Customer(id=1, first_name = "John", last_name="Doe", address = address1, email = "johndoe@gmail.com")
        account1 = Account(id=1, account_number=1, customer=customer1, current_balance=80)
        get_accs = self.accountService.get_all("0")
        self.assertEqual(get_accs[0], self.inserted_account)
        self.assertEqual(get_accs[1], account1)

    def test_withdrawal(self):
        new_acc = self.accountService.add_new(self.inserted_account)
        self.accountService.withdrawal(new_acc.account_number, 20)
        updated_acc = self.accountService.get_one(new_acc.account_number)
        self.assertEqual(updated_acc.current_balance, 5)

   #def test_deposit(self):
        # uncomment when this action is implemented
        #new_acc = self.accountService.add_new(self.inserted_account)
        #self.accountService.deposit(new_acc.account_number, 20)
        #updated_acc = self.accountService.get_one(new_acc.account_number)
        #self.assertEqual(updated_acc.current_balance, 45)

if __name__ == "__main__":
    unittest.main()
