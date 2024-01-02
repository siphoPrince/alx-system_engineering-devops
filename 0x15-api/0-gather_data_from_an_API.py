#!/usr/bin/python3
"""Accessing a employee todo lists"""

import requests
import sys

if __name__ == '__main__':
    emp_id = sys.argv[1]

    base_url = "https://jsonplaceholder.typicode.com/users"
    emp_url = base_url + "/" + emp_id

    # Fetch employee details
    emp_resp = requests.get(emp_url)
    emp_name = emp_resp.json().get('name')

    # Fetch employee tasks
    todo_url = emp_url + "/todos"
    todo_resp = requests.get(todo_url)
    tasks = todo_resp.json()

    comp_tasks_count = 0
    comp_tasks_list = []

    # Filter completed tasks
    for t in tasks:
        if t.get('completed'):
            comp_tasks_list.append(t)
            comp_tasks_count += 1

    # Print employee's completed tasks
    print("Employee {} has completed tasks ({}/{}):"
          .format(emp_name, comp_tasks_count, len(tasks)))

    for t in comp_tasks_list:
        print("\t {}".format(t.get('title')))
