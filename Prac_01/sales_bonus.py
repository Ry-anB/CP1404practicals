"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""


def main():
    """Calculate sales bonus until user inputs negative value"""
    sales = float(input("Enter sales: $"))
    while sales >= 0:
        if sales >= 1000:
            bonus = .15
        else:
            bonus = .10
        print(f"Your sales of ${sales} earned a bonus of ${sales * bonus}")
        sales = float(input("Enter sales: $"))


def run_tests():
    """Test main function with values"""
    test_values = [[500, [50]], [2000, [300]], [1000, [150]]]
    for value in test_values:
        sales = value[0]
        if sales >= 1000:
            bonus = .15
        else:
            bonus = .10
        print(f"Your sales of ${sales} earned a bonus of ${sales * bonus} "
              f"| Bonus should be {value[1]}")


main()
# run_tests()
