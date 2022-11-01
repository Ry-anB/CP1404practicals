"""CP1404 Practical - 2
Password Program"""

PASSWORD_LENGTH = 10


def main():
    """Check password against parameter and print length of *'s"""
    password = get_password(PASSWORD_LENGTH)
    print_asterisks(password)


def print_asterisks(password):
    """Print *'s the same length as entered password"""
    print("*" * len(password))


def get_password(password_length):
    """Get password meeting minimum length requirements"""
    password = input("Enter Password: ")
    while len(password) < password_length:
        print(f"Password must be {password_length} characters or more")
        password = input("Enter Password: ")
    return password


main()
