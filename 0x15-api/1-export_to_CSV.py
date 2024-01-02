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

    try:
        user_response = requests.get(f"{base_url}/users/{employee_id}")
        user_response.raise_for_status()  # Raise HTTPError for bad responses
        user_data = user_response.json()
        employee_name = user_data.get('name')

        todo_response = requests.get(f"{base_url}/todos?userId={employee_id}")
        todo_response.raise_for_status()  # Raise HTTPError for bad responses
        todo_data = todo_response.json()

        return employee_name, todo_data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        sys.exit(1)
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
        sys.exit(1)

def export_to_csv(employee_id, employee_name, todo_data):
    """
    Export TODO list data to CSV file.
    """
    csv_filename = f"{employee_id}.csv"

    try:
        with open(csv_filename, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["USER_ID", "EMPLOYEE_NAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

            for task in todo_data:
                csv_writer.writerow([employee_id, employee_name, str(task['completed']), task['title']])

        print(f"{csv_filename} created successfully")
    except csv.Error as csv_err:
        print(f"Error occurred while writing to CSV: {csv_err}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    try:
        employee_name, todo_data = get_employee_data(employee_id)
        export_to_csv(employee_id, employee_name, todo_data)
        print(f"{employee_id}.csv: OK")
    except requests.RequestException as e:
        print(f"Error: Unable to fetch data for employee ID {employee_id}. Please check the employee ID and try again.")

