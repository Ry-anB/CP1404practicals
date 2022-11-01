"""CP1404 Practical 06 - Tests for Guitar Class"""

from prac_06.guitar import Guitar


def run_tests():
    """Tests for Guitar class."""
    guitars = [["Gibson L-5 CES", 1922, 16035.40], ["Another Guitar", 2012, 1512.9]]
    guitar = Guitar(guitars[0][0], guitars[0][1], guitars[0][2])
    another_guitar = Guitar(guitars[1][0], guitars[1][1], guitars[1][2])

    print(f"{guitar.name} get_age() - Expected {100}. Got {guitar.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected {10}. Got {another_guitar.get_age()}")
    print()
    print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected {False}. "
          f"Got {another_guitar.is_vintage()}")


if __name__ == '__main__':
    run_tests()
