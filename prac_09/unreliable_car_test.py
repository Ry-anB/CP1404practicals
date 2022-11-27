"""CP1404 - Practical 09 - Taxi Test"""
from prac_09.unreliable_car import UnreliableCar
import random


def main():
    """Create and test taxi object"""
    mycar = UnreliableCar("My car", 100, 40)
    if random.uniform(0, 100) < mycar.reliability:
        print(f"You drove {mycar.drive(random.randint(1, 100))}km")
    else:
        print(f"You drove {mycar.drive(0)}km")


main()
