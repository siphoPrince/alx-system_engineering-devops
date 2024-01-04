#!/usr/bin/python3
<<<<<<< HEAD
"""Retrieve employee TODO list progress from a REST API"""
=======
>>>>>>> edaf382d8bdc65e2da1526a2faf985798b7f469c

import requests
import sys

<<<<<<< HEAD
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
=======
def get_employee_data(employee_id):
    """
    Get employee data and TODO list data from the REST API.
    """
    base_url = "https://jsonplaceholder.typicode.com"

    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    employee_name = user_data.get('name')

    todo_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todo_data = todo_response.json()

    return employee_name, todo_data

def display_todo_progress(employee_name, todo_data):
    """
    Display employee's TODO list progress.
    """
    total_tasks = len(todo_data)
    completed_tasks = sum(task['completed'] for task in todo_data)

    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")

    for task in todo_data:
        if task['completed']:
            print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    try:
        employee_name, todo_data = get_employee_data(employee_id)
        display_todo_progress(employee_name, todo_data)
    except requests.RequestException as e:
        print(f"Error: {e}")
>>>>>>> edaf382d8bdc65e2da1526a2faf985798b7f469c
