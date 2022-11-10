"""CP1404 Practical 07 - Guitar File Reader"""
from prac_06.guitar import Guitar


def main():
    """Reads information from a file and stores it as an object"""
    guitars = []
    in_file = open('guitars.csv', 'r')
    # File format is: Name,Year,Cost
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()
    guitars.sort()
    for guitar in guitars:
        print(guitar)

    choice = input("Would you like to add new guitars? Y/N: ").upper()
    while choice == "Y":
        name = input("Name: ")
        year = input("Year: ")
        cost = input("Cost: ")
        guitars.append(Guitar(name, int(year), float(cost)))
        choice = input("Would you like to add new guitars? Y/N: ").upper()
    out_file = open('guitars.csv', 'w')
    for guitar in guitars:
        print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)
    out_file.close()


if __name__ == '__main__':
    main()
