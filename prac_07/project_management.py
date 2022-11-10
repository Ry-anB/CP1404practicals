"""" CP1404 Practical 07 - Project Management
 Estimated time: 2hrs
 Total time: 8.5hrs (Unfinished)
 """

import datetime
from prac_07.project import Project

# Project accepts arguments as (name="", start_date=0, priority=0, estimate=0, completion=0)

MENU = "- (L)oad Projects\n- (S)ave Projects\n- (D)isplay Projects\n- (F)ilter Projects by Date" \
       "\n- (A)dd New Project\n- (U)pdate Project\n- (Q)uit"


def main():
    """Project Management"""
    projects = []
    load_data_from_file("projects.txt", projects)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            load_data_from_file("projects.txt", projects)
            projects.sort()
        elif choice == "S":
            save_data_to_file("projects.txt", projects)
        elif choice == "D":
            display_projects_by_completion(projects)
        elif choice == "F":
            filter_by_date(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        print(MENU)
        choice = input(">>> ").upper()


def format_date(date):
    """Return date input to format as dd/mm/yyyy - accepts date as yyyy/mm/dd"""
    project_start_date = date.split("/")
    start_date_as_datetime = \
        datetime.date(int(project_start_date[2]), int(project_start_date[1]), int(project_start_date[0]))
    formatted_date = datetime.date.strftime(start_date_as_datetime, "%d/%m/%Y")
    return formatted_date


def load_data_from_file(file, data):
    """Loads data from project file"""
    in_file = open(file, 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split('\t')
        project_start_date = format_date(parts[1])
        project = Project(parts[0], project_start_date, int(parts[2]), float(parts[3]), int(parts[4]))
        if project not in data:
            data.append(project)
    in_file.close()


def save_data_to_file(file, data):
    """Prints data to an output file"""
    out_file = open(file, "w")
    for project in data:
        print(f"{project.name}\t{project.start_date}\t{project.priority}\t"
              f"{project.estimate}\t{project.completion}", file=out_file)
    out_file.close()


def display_projects_by_completion(projects):
    """Prints projects separated by completed/incomplete"""
    print("Incomplete projects:")
    for project in projects:
        if not project.is_complete():
            print(f"\t{project}")
    print("Completed projects:")
    for project in projects:
        if project.is_complete():
            print(f"\t{project}")


def filter_by_date(projects):
    """Shows projects that start after a certain date"""
    date_input = input("Show projects that start after date (dd/mm/yyyy): ")
    formatted_date = format_date(date_input)
    for project in projects:
        if project.start_date >= formatted_date:
            print(project)


def add_project(projects):
    """Adds a project to the list"""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    formatted_date = format_date(start_date)
    priority = int(input("Priority: "))
    estimate = float(input("Estimate: "))
    completion = int(input("Percent Complete: "))
    project = Project(name, formatted_date, priority, estimate, completion)
    if project not in projects:
        projects.append(project)


def update_project(projects):
    """Updates completion or priority of projects"""
    for project in projects:
        print(f"{projects.index(project)} {project}")
    index_choice = int(input("Project choice: "))
    selected_project = projects[index_choice]
    print(selected_project)


main()
