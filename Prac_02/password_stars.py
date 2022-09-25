"""CP1404 Practical - 2
Password Program"""

PASSWORD_LENGTH = 10
password = input("Enter Password: ")
while len(password) < PASSWORD_LENGTH:
    print(f"Password must be {PASSWORD_LENGTH} characters or more")
    password = input("Enter Password: ")
print("*" * len(password))
