"""Cp1404 - Practical 09 - Silver Service Taxi Class"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):

    def __init__(self, name, fuel, fanciness):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * self.fanciness
        self.flagfall = 4.50

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.flagfall * super().get_fare()

    def __str__(self):
        """Return a string like a Taxi but with fanciness and flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall}"
