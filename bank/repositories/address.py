import psycopg2
from psycopg2 import sql
from bank.models.address import Address


class AddressRepository():
    # establish a connection
    connection = psycopg2.connect(
        host="localhost",
        database="capstone",
        user="postgres",
        password="password123",
    )

    connection.set_session(autocommit=True)

    def insert(self, address: Address):
        with self.connection.cursor() as cursor:
            cursor.execute("""
            INSERT INTO Address
            (address, city, state, zipcode)
            VALUES (%(address)s, %(city)s, %(state)s, %(zipcode)s)
            RETURNING ID
            """, {
                'address': address.address,
                'city': address.city,
                'state': address.state,
                'zipcode': address.zipcode

            }
            )
            address.id = cursor.fetchone()[0]
        return address
