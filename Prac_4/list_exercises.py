"""CP1404 - Practical 04 - Basic list operations"""
NUMBER_OF_PROMPTS = 5


def main():
    """Print information about entered values"""
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
                 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole',
                 'InterpreterInterface', 'StartServer',
                 'bob']
    numbers = []
    for i in range(NUMBER_OF_PROMPTS):
        user_entered_number = int(input(f"Number {i+1}: "))
        numbers.append(user_entered_number)
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")
    user = input("Username: ")
    if is_in_list(usernames, user):
        print("Access granted")
    else:
        print("Access denied")


def is_in_list(data, value):
    """Return True or False to see if value is in data"""
    return value in data


main()
