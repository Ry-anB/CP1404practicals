"""
CP1404practicals/CP5632 - Practical
Broken program to determine score status
"""

# Using boundaries instead of checking in range

score = float(input("Enter score: "))
while 0 <= score <= 100:
    if score > 90:
        print("Excellent")
    elif score > 50:
        print("Passable")
    else:
        print("Bad")
    score = float(input("Enter score: "))

# Using range for boundaries

# score = float(input("Enter score: "))
# while score in range(101):
#     if score > 90:
#         print("Excellent")
#     elif score > 50:
#         print("Passable")
#     else:
#         print("Bad")
#     score = float(input("Enter score: "))
