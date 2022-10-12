"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Print data from lists to show teacher & number of students for subjects"""
    datasets = get_data()
    for data in datasets:
        print(f"{data[0]} is taught by {data[1]} and has {data[2]} students")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    datasets = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        datasets.append(parts)
    input_file.close()
    return datasets


main()
