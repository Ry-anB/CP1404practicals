"""CP1404 - Practical 2
Score Menu Program"""

MENU = "(G)et Valid Score\n(P)rint Result\n(D)isplay Stars\n(Q)uit"


def main():
    """Get valid score and print results"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_result(score)
            print(result)
        elif choice == "D":
            print_asterisks(score)
        else:
            print("Invalid Choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Finished.")


def get_valid_score():
    """Get valid number between 0 - 100 inclusive"""
    score = int(input("Enter Score: "))
    while score < 0 or score > 100:
        print("Invalid Score- Must be 0 - 100")
        score = int(input("Enter Score: "))
    return score


def determine_result(score):
    """Return result from user score"""
    if score < 0 or score > 100:
        return "Invalid score"
    if score >= 90:
        return "Excellent"
    if score >= 50:
        return "Passable"
    return "Bad"


def print_asterisks(length):
    """Print *'s the same length as parameter"""
    print("*" * length)


main()
