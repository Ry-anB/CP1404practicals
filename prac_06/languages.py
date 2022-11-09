"""CP1404/CP5632 Practical 06 - Client code to use the Programming Language class."""

from prac_06.programming_language import ProgrammingLanguage


def main():
    """Display information from ProgrammingLanguage class"""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)
    print()
    languages = [python, ruby, visual_basic]
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
