#!/usr/bin/python3
"""Retrieve employee TODO list progress from a REST API"""

import requests
import sys

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/users"
    employee_url = f"{base_url}/{employee_id}"

    # Get employee details
    employee_response = requests.get(employee_url)
    employee_name = employee_response.json().get('name')

    # Get employee tasks
    todo_url = f"{employee_url}/todos"
    todo_response = requests.get(todo_url)
    tasks = todo_response.json()

    completed_tasks_count = 0
    completed_tasks_list = []

    # Filter completed tasks
    for task in tasks:
        if task.get('completed'):
            completed_tasks_list.append(task)
            completed_tasks_count += 1

    total_tasks_count = len(tasks)

    # Print employee's completed tasks progress
    print(f"Employee {employee_name} is done with tasks({completed_tasks_count}/{total_tasks_count}):")

    for task in completed_tasks_list:
        print(f"\t {task.get('title')}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id_input = sys.argv[1]

    try:
        employee_id = int(employee_id_input)
    except ValueError:
        print("Please provide a valid integer for the employee ID.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
