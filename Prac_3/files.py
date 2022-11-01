"""CP1404 Practical 3 - Files"""


def main():
    """Run various file reading tasks"""
    write_name_to_file()
    print_name_from_file()
    display_sum_of_x_file_lines(2)
    print_sum_of_all_numbers_in_file()


def write_name_to_file():
    """Task 1: Writes user entered name to a file (name.txt)"""
    name = input("Enter your name: ")
    out_file = open("name.txt", "w")
    print(name, file=out_file)
    out_file.close()


def print_name_from_file():
    """Task 2: Print user's name from file (name.txt)"""
    in_file = open("name.txt", "r")
    print(f"Your name is {in_file.readline()}")
    in_file.close()


def display_sum_of_x_file_lines(number_of_lines):
    """Task 3: Reads x lines of a file and prints the sum of the numbers"""
    total = 0
    in_file = open("numbers.txt", "r")
    try:
        for line in range(number_of_lines):
            total += float(in_file.readline())
    except ValueError:
        pass
    print(f"{total:.0f}")
    in_file.close()


def print_sum_of_all_numbers_in_file():
    """Task 4: Reads all lines of a file and prints the sum of all numbers"""
    total = 0
    in_file = open("numbers.txt", "r")
    for line in in_file:
        try:
            total += float(line)
        except ValueError:
            pass
    print(f"{total:,.2f}")
    in_file.close()


main()
