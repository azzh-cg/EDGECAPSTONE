from multiprocessing import connection
from re import T
import psycopg2
from psycopg2 import sql
from bank.models.account import Account

# Actions:

# deserialize json
# temp_addr = new Address(address, city, street, zipcode)
# temp_cust = new Customer(firstName, lastName, email)
# temp_acc = new Account(openingBalance)


class AccountRepository():
    # establish a connection
    connection = psycopg2.connect(
        host="localhost",
        database="capstone",
        user="postgres",
        password="password123",
    )
    connection.set_session(autocommit=True)

    def insert(self, account: Account):
        with self.connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO Account (account_number, customer_ID, current_balance)
                VALUES (%(account_number)s, %(customer_id)s, %(current_balance)s)
                RETURNING ID;
                """, {
                'account_number': account.account_number,
                'customer_id': account.customer.id,
                'current_balance': account.current_balance
            })
            account.id = cursor.fetchone()[0]
            return account

    def delete(self, id):
        with self.connection.cursor() as cursor:
            cursor.execute("""
                    DELETE FROM Account WHERE ID=%(id)s
                    """, {
                'id': id
            }
            )

    # def retrieve_all_accounts():
    #     with connection.cursor() as cursor:
    #         cursor.execute("""
    #         SELECT * FROM Account
    #         """)

    # def retrieve_specific_account(accountNum):
    #     with connection.cursor() as cursor:
    #         cursor.execute("""
    #         SELECT * FROM Account WHERE account_number = %(accountNum)s
    #         """)

    # def execute_withdrawal(accountNum, withdrawal):
    #     with connection.cursor() as cursor:
    #         cursor.execute("""
    #         SELECT current_balance FROM Account WHERE account_number = %(accountNum)s
    #         """)
    #     current_balance = cursor.fetchone().current_balance
    #     if (current_balance >= withdrawal):
    #         cursor.execute("""
    #         UPDATE Account
    #         SET current_balance
    #         VALUES (%(current_balance)s - %(withdrawal)s);
    #         """)
    #         connection.commit()

    # def execute_deposit(accountNum, deposit):
    #     with connection.cursor() as cursor:
    #         cursor.execute("""
    #         SELECT current_balance FROM Account WHERE account_number = %(accountNum)s
    #         """)
    #     current_balance = cursor.fetchone().current_balance
    #     cursor.execute("""
    #         UPDATE Account
    #         SET current_balance
    #         VALUES (%(current_balance)s + %(deposit)s);
    #         """)
    #     connection.commit()

    # def close_account(accountNum):
    #     try:
    #         with connection.cursor() as cursor:
    #             cursor.execute("""
    #         SELECT Customer_ID from Account where account_num = %(accountNum)s
    #         """)
    #         customerId = cursor.fetchone().Customer_ID

    #         cursor.execute("""
    #         DELETE from Account where account_num = %(accountNum)s
    #         """)
    #         connection.commit()

    #         cursor.execute("""
    #         SELECT Address_ID from Customer where Customer_ID = %(customerId)s
    #         """)
    #         addressId = cursor.fetchone().Address_ID

    #         cursor.execute("""
    #         DELETE from Customer where Customer_ID = %(customerId)s
    #         """)
    #         connection.commit()

    #         cursor.execute("""
    #         DELETE from Address where Address_ID = %(addressId)s
    #         """)
    #         connection.commit()
    #     except (Exception, psycopg2.Error) as error:
    #         raise Exception("Account you are trying to close does not exist")
