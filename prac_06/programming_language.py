"""CP1404/CP5632 Practical 06 - Programming_Language class.
Estimated time: 15mins | 10:30am
Actual time: 20mins
"""


class ProgrammingLanguage:
    """Represent a Programming Language"""

    def __init__(self, name, typing, reflection, year):
        """Initialise information about a Programming Language"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return details from ProgrammingLanguage as a string."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}," \
               f" First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if a Programming language is dynamic."""
        return self.typing == "Dynamic"
