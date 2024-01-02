#!/usr/bin/python3
'''
Retrieves and displays TODO list progress for a given employee ID.
'''

if __name__ == '__main__':
    import requests
    import sys

    completed_tasks_count = 0
    completed_task_titles = []
    employee_id = sys.argv[1]

    user_info_url = ('https://jsonplaceholder.typicode.com/users/{}'
            .format(employee_id))
    user_info = requests.get(user_info_url).json()
    employee_name = user_info.get("username")

    todo_url = ('https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(employee_id))
    todo = requests.get(todo_url).json()

    for task in todo:
        if task.get('completed'):
            completed_task_titles.append(task.get('title'))
            completed_tasks_count += 1

    total_tasks_count = len(todo)

    print('Employee {} is done with tasks({}/{}):'.
          format(employee_name, completed_tasks_count, total_tasks_count))
    for title in completed_task_titles:
        print('\t{}'.format(title))
