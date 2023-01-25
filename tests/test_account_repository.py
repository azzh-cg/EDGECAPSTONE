from pydantic import BaseModel
from bank.models.address import Address
from bank.models.customer import Customer
from bank.models.account import Account
from bank.repositories.account import AccountRepository

class TestCustomerRepository(unittest.TestCase):
    def setUp(self):
        self.customerRepository = CustomerRepository()
        

    def tearDown(self):
        self.customerRepository.delete(self.inserted_address.id)

    def test_insert(self):
        self.inserted_address = self.addressRepository.insert(Address(id=0, address="1234 Lane Rd", city='Los Angeles', state='California', zipcode=90210))
        self.inserted_customer = self.customerRepository.insert(Customer(id=0, first_name = "Jane", last_name="Doe", address = inserted_address, email = "janedoe@gmail.com") )
        self.inserted_account = self.accountRepository.insert(Account(id=0, account_number=0, customer=inserted_customer, current_balance=25))
        self.assertEqual("25", self.inserted_account.current_balance)

    def test_delete(self):
        #_address = new Address(id=0, address="1234 Lane Rd", city='Los Angeles', state='California', zipcode=90210)
        #self.inserted_customer = self.customerRepository.insert(Customer(id=0, first_name = "Jane", last_name="Doe", address = _address, email = "janedoe@gmail.com") )
        #self.customerRepository.delete(inserted_customer.id)
        # what to assert?

    if __name__ == "__main__":
    unittest.main()