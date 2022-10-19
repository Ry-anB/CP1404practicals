"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

SHORT_TO_LONG_STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales",
                             "NT": "Northern Territory", "WA": "Western Australia",
                             "ACT": "Australian Capital Territory", "VIC": "Victoria",
                             "TAS": "Tasmania"}
print(SHORT_TO_LONG_STATE_NAMES)
for state in SHORT_TO_LONG_STATE_NAMES:
    print(f"{state:3} is {SHORT_TO_LONG_STATE_NAMES[state]}")
state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(f"{state_code} is {SHORT_TO_LONG_STATE_NAMES[state_code]}")
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
