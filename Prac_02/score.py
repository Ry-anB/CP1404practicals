"""
CP1404practicals/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    """Print result from user score"""
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)
    random_score = random.randint(1, 100)
    result = determine_result(random_score)
    print(f"Score: {random_score} - {result}")


def determine_result(score):
    """Return result from user score"""
    if score < 0 or score > 100:
        return "Invalid score"
    if score >= 90:
        return "Excellent"
    if score >= 50:
        return "Passable"
    return "Bad"


main()
