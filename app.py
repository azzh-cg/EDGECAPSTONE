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

# add actions here