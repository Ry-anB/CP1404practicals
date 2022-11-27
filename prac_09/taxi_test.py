"""CP1404 - Practical 09 - Taxi Test"""
from prac_09.taxi import Taxi


def main():
    """Create and test taxi object"""
    mytaxi = Taxi("Prius 1", 100)
    mytaxi.drive(40)
    print(f"{mytaxi.__str__()} ${mytaxi.get_fare()}")
    mytaxi.start_fare()
    mytaxi.drive(100)
    print(f"{mytaxi.__str__()} ${mytaxi.get_fare()}")


main()
