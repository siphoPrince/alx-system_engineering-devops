#!/usr/bin/python3
'''
printing a todo
'''

import requests
import sys
import json

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

def export_to_json(employee_id, todo_data):
    """
    Export TODO data to JSON file.
    """
    filename = f"{employee_id}.json"
    with open(filename, 'w') as json_file:
        json.dump({employee_id: todo_data}, json_file, indent=2)
    print(f"Data exported to {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    try:
        employee_name, todo_data = get_employee_data(employee_id)
        display_todo_progress(employee_name, todo_data)
        export_to_json(employee_id, todo_data)
    except requests.RequestException as e:
        print(f"Error: {e}")

