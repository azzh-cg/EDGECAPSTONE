import psycopg2
from psycopg2 import sql

class AddressRepository():
    # establish a connection
    connection = psycopg2.connect(
        host="localhost",
        database="psycopgtest",
        user="postgres",
        password="Password123",
    )

    connection.set_session(autocommit=True)



    def insert(self, address: Address):
        with connection.cursor() as cursor:
            cursor.execute("""
            INSERT into Address
            SET (Address, City, Street, Zipcode)
            VALUES (%(address)s, %(city)s, %(street)s, %(zipcode)s,)
            RETURNING ID
            """),{
                'address': address.address,
                'city': address.city,
                'street': address.street,
                'zipcode': address.zipcode

            }
            address.id = cursor.fetchone()[0]
        return address