"""CP1404 Practical 06 - Guitars"""

from prac_06.guitar import Guitar


def main():
    """Store guitar details and print results"""
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : {cost:.2f} added.")
        name = input("Name: ")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), "
              f"worth ${guitar.cost:10,.2f} {vintage_string}")


if __name__ == '__main__':
    main()
