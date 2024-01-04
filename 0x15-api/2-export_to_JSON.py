#!/usr/bin/python3
"""
returns information about his/her TODO list progress and exports it to JSON.
"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}/'.format(user_id)
    todos_url = url + 'todos'
    user = requests.get(url).json()
    todos = requests.get(todos_url).json()

    todo_list = []
    for todo in todos:
        new_dict = {}
        new_dict['task'] = todo.get('title')
        new_dict['completed'] = todo.get('completed')
        new_dict['username'] = user.get('username')
        todo_list.append(new_dict)

    todo_dict = {user.get('id'): todo_list}

    file_name = '{}.json'.format(user.get('id'))

    with open(file_name, mode='w') as outfile:
        json.dump(todo_dict, outfile)
