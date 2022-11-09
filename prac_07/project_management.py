"""" CP1404 Practical 07 - Project Management """

import datetime
from Prac_07

MENU = "- (L)oad Projects\n- (S)ave Projects\n- (D)isplay Projects\n- (F)ilter Projects by Date" \
       "\n- (A)dd New Project\n- (U)pdate Project\n- (Q)uit"


def main():
    in_file = open('projects.txt', 'r')
    # File format is: Name  Start Date	Priority	Cost Estimate	Completion Percentage
    # Separated by \t
    in_file.readline()
    for line in in_file:
        parts = line.strip().split('\t')
        project = Project(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()
    print(MENU)
    choice = input(">>> ").upper()





main()