"""Cp1404 - Practical 04 - Lottery Ticket Generator"""

import random

QUICKPICKS = []
lottery_tickets = int(input("How many quick picks? "))
for i in range(lottery_tickets):
    ticket_i = []
    for j in range(6):
        while len(ticket_i) < 6:
            number = random.randint(1, 45)
            if number not in ticket_i:
                ticket_i.append(number)
            else:
                continue
    QUICKPICKS.append(ticket_i)
for quickpick in QUICKPICKS:
    quickpick.sort()
    for i in quickpick:
        print(f"{i:2}", end=" ")
    print()
