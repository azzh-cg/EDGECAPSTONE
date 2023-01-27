import unittest
from bank.models.address import Address
from bank.models.customer import Customer
from bank.repositories.address import AddressRepository
from bank.repositories.customer import CustomerRepository

class TestCustomerRepository(unittest.TestCase):
    def setUp(self):
        self.customerRepository = CustomerRepository()
        self.addressRepository = AddressRepository()
        

    #def tearDown(self):
     #   self.customerRepository.delete(self.inserted_customer.id)

    def test_insert(self):
        self.inserted_address = self.addressRepository.insert(Address(id=0, address="1234 Lane Rd", city='Los Angeles', state='California', zipcode=90210))
        self.inserted_customer = self.customerRepository.insert(Customer(id=0, first_name = "Jane", last_name="Doe", address = self.inserted_address, email = "janedoe@gmail.com") )
        self.assertEqual("Jane", self.inserted_customer.first_name)

    #def test_delete(self):
        #_address = new Address(id=0, address="1234 Lane Rd", city='Los Angeles', state='California', zipcode=90210)
        #self.inserted_customer = self.customerRepository.insert(Customer(id=0, first_name = "Jane", last_name="Doe", address = _address, email = "janedoe@gmail.com") )
        #self.customerRepository.delete(inserted_customer.id)
        # what to assert?

if __name__ == "__main__":
    unittest.main()