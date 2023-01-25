import psycopg2
from psycopg2 import sql

class CustomerRepository():
    # establish a connection
    connection = psycopg2.connect(
        host="localhost",
        database="psycopgtest",
        user="postgres",
        password="Password123",
    )

    connection.set_session(autocommit=True)



    def insert(self, customer: Customer):
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT into Customer
                SET (first_name, last_name, Address_ID, email)
                VALUES (%(firstName)s, %(lastName)s, %(addressID)s, %(email)s,)
                """),{
                    'firstName': customer.firstName,
                    'lastName': customer.lastName,
                    'addressID': customer.address.id,
                    'email': customer.email
                }
            connection.commit()
            customer.id = cursor.fetchone()[0]
        return customer