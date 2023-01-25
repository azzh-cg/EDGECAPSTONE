import unittest
from unittest.mock import Mock
from bank.models.address import Address
from bank.models.customer import Customer
from bank.models.account import Account
from bank.repositories.address import AddressRepository
from bank.repositories.account import AccountRepository
from bank.repositories.customer import CustomerRepository
from bank.services.account import AccountService


class TestOrderService(unittest.TestCase):
    def setUp(self):
        self.address = Address(id=0, address="1234 Lane Rd", city='Los Angeles', state='California', zipcode=90210)
        self.customer = Customer(id=0, first_name = "Jane", last_name="Doe", address = inserted_address, email = "janedoe@gmail.com")
        self.addressRepository = Mock()
        self.customerRepository = Mock()
        self.accountRepository = Mock()
        self.accountService = AccountService(self.accountRepository, self.addressRepository, self.customerRepository)

    def test_add_new_order(self):
        #self.product_repository.get_by_id = Mock(return_value=self.product)
        #self.orderRepository.insert = Mock(return_value=self.order)
        #new_order = self.orderService.add_new(self.order)
        #self.assertEqual(new_order, self.order)

    def test_get_one_order(self):
        #self.orderRepository.get_by_number = Mock(return_value=self.order)
        #get_order = self.orderService.get_one("000")
        #self.assertEqual(get_order, self.order)


    if __name__ == "__main__":
        unittest.main()
