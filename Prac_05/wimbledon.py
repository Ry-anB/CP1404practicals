"""CP1404 - Practical 05 - Wimbledon"""

FILENAME = "wimbledon.csv"


def main():
    """Extract wimbledon data and print champion and country results"""
    wimbledon_datasets = get_data(FILENAME)
    champion_to_count, countries = process_file_data(wimbledon_datasets)
    display_data(champion_to_count, countries)


def process_file_data(datasets):
    """Create dictionary from list of file data"""
    champion_to_count = {}
    countries = set()
    champion_index = 2
    country_index = 1
    for data in datasets:
        countries.add(data[country_index])
        try:
            champion_to_count[data[champion_index]] += 1
        except KeyError:
            champion_to_count[data[champion_index]] = 1
    return champion_to_count, countries


def get_data(filename):
    """Get data from file"""
    datasets = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            datasets.append(parts)
    return datasets


def display_data(champion_to_count, countries):
    """Print formatted data from data file"""
    print("Wimbledon Champions: ")
    for name, count in champion_to_count.items():
        print(name, count)
    print()
    print(f"These {len(countries)} countries have won Wimbledon: ")
    print(", ".join(sorted(countries)))


main()
