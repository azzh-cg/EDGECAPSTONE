import unittest
from bank.models.address import Address
from bank.repositories.address import AddressRepository

class TestAddressRepository(unittest.TestCase):
    def setUp(self):
        self.addressRepository = AddressRepository()
        

    def tearDown(self):
        self.addressRepository.delete(self.inserted_address.id)

    def test_insert(self):
        self.inserted_address = self.addressRepository.insert(Address(id=0, address="1234 Lane Rd", city='Los Angeles', state='California', zipcode=90210))
        self.assertEqual("1234 Lane Rd", self.inserted_address.address)

    #def test_delete(self):
        #self.inserted_address = self.addressRepository.insert(Address(id=0, address="1234 Lane Rd", city='Los Angeles', state='California', zipcode=90210 ))
        #self.addressRepository.delete(self.inserted_address.id)
        #what to assert?
        #self.assertTrue()
    
    if __name__ == "__main__":
        unittest.main()
    