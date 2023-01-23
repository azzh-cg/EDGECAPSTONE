import psycopg2
from psycopg2 import sql


# establish a connection
conn = psycopg2.connect(
    host="localhost",
    database="psycopgtest",
    user="postgres",
    password="Password123",
)

connection.set_session(autocommit=True)

# Actions:

# OPEN AN ACCOUNT
# check if account already exists, and check auto-increment:
def open_account(address: string, city, street, zipcode, firstName, lastName, email, openingBalance: int) -> bool:
    with connection.cursor() as cursor:
        cursor.execute("""
            INSERT into Address 
            
            SELECT AddressID from Address order by AddressID desc limit 1


            INSERT into Customer

            SELECT CustomerID from Customer where 
            
            
            INSERT into Account 
            SET (AccountNumber, CustomerID, CurrentBalance) 
            VALUES (%(accountNum)s, %(customerID)s, %(openingBalance)s);
            
            """)

            

        

    admin, = result
    return admin