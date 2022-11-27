"""
CP1404/CP5632 Practical
Unreliable Car class
"""
from prac_09.car import Car


class UnreliableCar(Car):
    """Version of car that includes reliability"""

    def __init__(self, name, fuel, reliability):
        """Initialise an Unreliable Car instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability
