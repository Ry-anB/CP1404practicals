"""
CP1404practicals/CP5632 - Practical
Broken program to determine score status
"""


def main():
    """Print result from user score"""
    score = float(input("Enter score: "))
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


main()
