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

#deserialize json
#temp_addr = new Address(address, city, street, zipcode)
#temp_cust = new Customer(firstName, lastName, email)
#temp_acc = new Account(openingBalance)

# OPEN AN ACCOUNT
# check if account already exists, and check auto-increment:
def open_account(address: string, city, street, zipcode, firstName, lastName, email, openingBalance: int):  
    with connection.cursor() as cursor:
        cursor.execute("""
            INSERT into Address 
            SET (Address, City, Street, Zipcode)
            VALUES (%(address)s, %(city)s, %(street)s, %(zipcode)s,)
            """)
        connection.commit()
        addressID = cursor.fetchone().Address_ID

        cursor.execute("""
            INSERT into Customer
            SET (first_name, last_name, Address_ID, email)
            VALUES (%(firstName)s, %(lastName)s, %(addressID)s, %(email)s,)
            """)
        connection.commit()
        customerID = cursor.fetchone().Customer_ID

            
        cursor.execute(""" 
            INSERT into Account 
            SET (Customer_ID, current_balance) 
            VALUES (%(customerID)s, %(openingBalance)s);
            """)
        connection.commit()

def retrieve_all_accounts():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM Account
            """)

def retrieve_specific_account(accountNum):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM Account WHERE account_number = %(accountNum)s
            """)

def execute_withdrawal(accountNum, withdrawal):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT current_balance FROM Account WHERE account_number = %(accountNum)s
            """)
        current_balance = cursor.fetchone().current_balance
        if(current_balance >= withdrawal):
            cursor.execute("""
            UPDATE Account 
            SET current_balance 
            VALUES (%(current_balance)s - %(withdrawal)s);
            """)
            connection.commit()

def execute_deposit(accountNum, deposit):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT current_balance FROM Account WHERE account_number = %(accountNum)s
            """)
        current_balance = cursor.fetchone().current_balance
        cursor.execute("""
            UPDATE Account 
            SET current_balance 
            VALUES (%(current_balance)s + %(deposit)s);
            """)
        connection.commit()

def close_account(accountNum:
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT Customer_ID from Account where account_num = %(accountNum)s
            """)
            customerId = cursor.fetchone().Customer_ID

            cursor.execute("""
            DELETE from Account where account_num = %(accountNum)s
            """)
            connection.commit()

            cursor.execute("""
            SELECT Address_ID from Customer where Customer_ID = %(customerId)s
            """)
            addressId = cursor.fetchone().Address_ID

            cursor.execute("""
            DELETE from Customer where Customer_ID = %(customerId)s
            """)
            connection.commit()

            cursor.execute("""
            DELETE from Address where Address_ID = %(addressId)s
            """)
            connection.commit()

    catch (Exception, psycopg2.Error) as error:
        throw Exception("Account you are trying to close does not exist")
