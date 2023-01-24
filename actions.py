from sre_parse import State


def createAccount():
    print("Please enter the following information...")
    fName = input("First Name: ")
    lName = input("Last Name: ")
    email = input("Email: ")
    print("Please enter the following address information...")
    address = input("Address: ")
    city = input("City: ")
    state = input("State: ")
    zipcode = input("Zipcode: ")