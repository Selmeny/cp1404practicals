"""
CP1404/CP5632 - Practical
Get a password with minimum length and display asterisks
"""

MINIMUM_LENGTH = 6

def main():
    password = get_password()
    print_asterisk(password)

def get_password():
    """
    Get password from user. Show warning is password length is invalid.

    :return: password
    """
    password = input(f"Enter you password with minimum length of {MINIMUM_LENGTH} characters: ")

    while len(password) < 6:
        print("Password is invalid")
        password = input(f"Enter you password with minimum length of {MINIMUM_LENGTH} characters: ")

    return password

def print_asterisk(password):
    """
    Calculate password length. Use that to print same amount of asteriks.

    :param password: Password string whose length sets how many asterisk are printed.
    :return: None.
    """
    print("*" * len(password))

main()


