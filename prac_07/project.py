"""CP1404/CP5632 Practical 07 - Project Class"""

from datetime import datetime


class Project:
    """Stores project details in class."""

    def __init__(self, name="", start_date=0, priority=0, estimate=0, completion=0):
        """Initialise a project."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.estimate = estimate
        self.completion = completion

    def __str__(self):
        """Return details of a project"""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}," \
               f" estimate: ${self.estimate}, completion: {self.completion}%"

    def is_complete(self):
        """Determine if a project is complete."""
        return self.completion >= 100

    def __eq__(self, other):
        return self.name == other.name

    def __ge__(self, other):
        return self.start_date >= other.start_date

    def __lt__(self, other):
        return self.start_date < other.start_date

    def update_priority(self, priority):
        self.priority = priority

    def update_completion(self, completion):
        self.completion = completion
