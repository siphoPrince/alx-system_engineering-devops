import requests
import sys

def get_employee_todo_progress(employee_id):
    # API endpoints
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'

    # Get user information
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Failed to retrieve user information. Status code: {user_response.status_code}")
        return

    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Get TODO list for the user
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Failed to retrieve TODO list. Status code: {todos_response.status_code}")
        return

    todos_data = todos_response.json()

    # Calculate progress
    number_of_done_tasks = sum(1 for task in todos_data if task.get('completed'))
    total_number_of_tasks = len(todos_data)

    # Display information
    print(f'Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_number_of_tasks}):')
    for task in todos_data:
        if task.get('completed'):
            print(f'\t{task.get("title")}')

if __name__ == '__main__':
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = sys.argv[1]
        get_employee_todo_progress(employee_id)

