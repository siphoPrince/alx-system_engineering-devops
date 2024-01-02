#!/usr/bin/python3
'''
printing a todo
'''

import json
import requests


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


def export_to_json(data, filename):
    """
    Export data to JSON file.
    """
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=2)
    print(f"Data exported to {filename}")


if __name__ == "__main__":
    all_employee_data = {}

    for employee_id in range(1, 11):  # Assuming there are employees with IDs from 1 to 10
        try:
            employee_name, todo_data = get_employee_data(employee_id)
            all_employee_data[employee_id] = [{"username": employee_name, "task": task['title'], "completed": task['completed']} for task in todo_data]
        except requests.RequestException as e:
            print(f"Error: {e}")

    export_to_json(all_employee_data, "todo_all_employees.json")

