#!/usr/bin/python3
'''
For a given employee ID, returns information about his/her
TODO list progress in CSV format.
'''
import csv
import requests
import sys

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

    print(f"Employee {employee_name} is done with tasks({completed_tasks:02}/{total_tasks:02}):")

    for task in todo_data:
        if task['completed']:
            print(f"\t{task['title']}")

def export_to_csv(employee_id, employee_name, todo_data):
    """
    Export TODO list data to CSV file.
    """
    csv_filename = f"{employee_id}.csv"

    with open(csv_filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todo_data:
            csv_writer.writerow([employee_id, employee_name, str(task['completed']), task['title']])

    print(f"{csv_filename} created successfully")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    try:
        employee_name, todo_data = get_employee_data(employee_id)
        display_todo_progress(employee_name, todo_data)
        export_to_csv(employee_id, employee_name, todo_data)
        print(f"sylvain@ubuntu$ cat {employee_id}.csv")
    except requests.RequestException as e:
        print(f"Error: {e}")
