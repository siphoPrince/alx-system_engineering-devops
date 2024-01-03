#!/usr/bin/python3
"""
A script that gets the TODO list of a designated employee ID.
"""

import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} employee_number".format(argv[0]))
        exit(1)

    employee_number = int(argv[1])

    baselink = "https://jsonplaceholder.typicode.com"
    employee_url = "{}/users/{}".format(baselink, employee_number)
    tasks_url = "{}/todos?userId={}".format(baselink, employee_number)

    try:
        employee_response = requests.get(employee_url)
        tasks_response = requests.get(tasks_url)
        employee_data = employee_response.json()
        tasks_data = tasks_response.json()

        employee_fullname = employee_data.get("name")
        total_tasks = len(tasks_data)
        completed_tasks = [task for task in tasks_data if task.get("completed")]

        print("Employee {} has completed tasks({}/{}):".format(
            employee_fullname, len(completed_tasks), total_tasks))

        for task in completed_tasks:
            print("\t {}".format(task.get("title")))

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        exit(1)
