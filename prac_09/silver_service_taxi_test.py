"""Cp1404 - Practical 09 - Silver Service Taxi Test"""
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test silver service taxi class"""
    hummer = SilverServiceTaxi("Hummer", 200, 4)
    print(hummer.__str__())
    mytaxi = SilverServiceTaxi("My Taxi", 100, 2)
    mytaxi.drive(18)
    print(mytaxi.__str__())
    print(f"${mytaxi.get_fare()}")


main()
