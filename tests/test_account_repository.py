import unittest
from bank.models.address import Address
from bank.models.customer import Customer
from bank.models.account import Account
from bank.repositories.address import AddressRepository
from bank.repositories.account import AccountRepository
from bank.repositories.customer import CustomerRepository

class TestAccountRepository(unittest.TestCase):
    inserted_address = Address(id=0, address="", city="", state="", zipcode="")
    inserted_customer = Customer(id=0, first_name="", last_name="", address=inserted_address, email="")
    inserted_account = Account(id=0, account_number=0, customer=inserted_customer, current_balance=0)
    def setUp(self):
        self.addressRepository = AddressRepository()
        self.customerRepository = CustomerRepository()
        self.accountRepository = AccountRepository()
        

    def tearDown(self):
        self.accountRepository.delete(self.inserted_account.id)
        self.customerRepository.delete(self.inserted_customer.id)
        self.addressRepository.delete(self.inserted_address.id)

    def test_insert(self):
        self.inserted_address = self.addressRepository.insert(Address(id=0, address="1234 Lane Rd", city='Los Angeles', state='California', zipcode='90210'))
        self.inserted_customer = self.customerRepository.insert(Customer(id=0, first_name = "Jane", last_name="Doe", address = self.inserted_address, email = "janedoe@gmail.com") )
        self.inserted_account = self.accountRepository.insert(Account(id=0, account_number=0, customer=self.inserted_customer, current_balance=25))
        self.assertEqual(25, self.inserted_account.current_balance)

    #def test_delete(self):
        #_address = new Address(id=0, address="1234 Lane Rd", city='Los Angeles', state='California', zipcode=90210)
        #self.inserted_customer = self.customerRepository.insert(Customer(id=0, first_name = "Jane", last_name="Doe", address = _address, email = "janedoe@gmail.com") )
        #self.customerRepository.delete(inserted_customer.id)
        # what to assert?

if __name__ == "__main__":
    unittest.main()