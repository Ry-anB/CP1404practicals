"""CP1404/CP5632 Practical 06 - Guitar Class"""

import datetime

CURRENT_DATETIME = datetime.datetime.today()
CURRENT_YEAR = CURRENT_DATETIME.date()
VINTAGE_AGE = 50


class Guitar:
    """Stores Guitar details in class."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return details of a Guitar"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return age of a Guitar"""
        return CURRENT_YEAR.year - self.year

    def is_vintage(self):
        """Determine if a Guitar is vintage."""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Less than - Sort by year"""
        return self.year < other.year
