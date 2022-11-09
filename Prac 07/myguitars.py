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


if __name__ == '__main__':
    main()
