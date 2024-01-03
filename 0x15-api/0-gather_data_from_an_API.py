#!/usr/bin/python3
'''
printing a todo
'''

import requests
import sys

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        # Get user data
        user_response = requests.get(user_url)
        user_data = user_response.json()
        employee_name = user_data.get('name')

        # Get TODO list data
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Count completed and total tasks
        total_tasks = len(todos_data)
        completed_tasks = sum(task['completed'] for task in todos_data)

        # Display progress information
        print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")

        # Display completed tasks
        for task in todos_data:
            if task['completed']:
                print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    try:
        employee_id = int(employee_id)
    except ValueError:
        pass  # Do nothing or print a custom message if desired

    get_employee_todo_progress(employee_id)
