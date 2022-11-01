"""CP1404 - Practical 05 - Emails """


def main():
    """Create dictionary of email and names"""
    email_to_name = {}
    user_email = input("Email: ")
    while user_email != "":
        user_name = get_name_from_email(user_email)
        name = email_name_confirmation(user_name)
        if user_email not in email_to_name:
            email_to_name[user_email] = name
        else:
            print("Email already exists")
        user_email = input("Email: ")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """Guess name based on email"""
    first_slice_position = email.rfind("@")
    non_alpha_characters = []
    email_without_domain = email[:first_slice_position]
    name = email_without_domain
    for character in email_without_domain:
        if not character.isalpha():
            non_alpha_characters.append(character)
    for item in non_alpha_characters:
        name = email_without_domain.replace(f"{item}", " ")
    return name


def email_name_confirmation(name):
    """Confirm accurate user name"""
    confirmation = input(f"Is your name {name}? (Y/n) ").lower()
    if len(confirmation) == 0:
        return name
    if confirmation.startswith("y"):
        return name
    name = input("Name: ")
    return name


main()
