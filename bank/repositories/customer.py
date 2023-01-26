import psycopg2
from psycopg2 import sql
from bank.models.customer import Customer


class CustomerRepository():
    # establish a connection
    connection = psycopg2.connect(
        host="localhost",
        database="capstone",
        user="postgres",
        password="password123",
    )

    connection.set_session(autocommit=True)

    def insert(self, customer: Customer):
        with self.connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO Customer
                (first_name, last_name, Address_ID, email)
                VALUES (%(first_name)s, %(last_name)s, %(address_id)s, %(email)s,)
                """, {
                'first_name': customer.first_name,
                'last_name': customer.last_name,
                'address_id': customer.address.id,
                'email': customer.email
            }
            )
            customer.id = cursor.fetchone()[0]
        return customer

    def delete(self, id):
        with self.connection.cursor() as cursor:
            cursor.execute("""
                    DELETE FROM Customer WHERE ID=%(id)s
                    """, {
                'id': id
            }
            )
