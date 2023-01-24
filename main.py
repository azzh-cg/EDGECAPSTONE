from actions import *

def main():
    print("Hello! Welcome to MAP Bank! Where we help you map your future!")
    selection = input("Please select an option:\n"
                      "1: Open a new account\n"
                      "2: Retrieve information on all accounts\n"
                      "3: Retrieve information for a specific account\n"
                      "4: Execute a withdrawal from an existing account\n"
                      "5: Execute a deposit to an existing account\n"
                      "6: Close an existing account\n")
    action(selection)


def action(selection):
    switcher = {
        1: createAccount(),
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday'
    }
    return switcher.get(selection, "Invalid day of week")


if __name__ == "__main__":
    main()
