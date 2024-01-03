#!/usr/bin/python3
'''
printing a todo
'''

import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Fetch employee data using the provided REST API
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        todo_response = requests.get(todo_url)

        user_data = user_response.json()
        todo_data = todo_response.json()

        # Extract relevant information
        employee_name = user_data['name']
        done_tasks = [task['title'] for task in todo_data if task['completed']]
        total_tasks = len(todo_data)
        done_tasks_count = len(done_tasks)

        # Display the output
        print(f"Employee {employee_name} is done with tasks ({done_tasks_count}/{total_tasks}):")
        print(f"{employee_name}: {done_tasks_count}/{total_tasks}")

        for task_title in done_tasks:
            print(f"\t{task_title}")

    except requests.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

