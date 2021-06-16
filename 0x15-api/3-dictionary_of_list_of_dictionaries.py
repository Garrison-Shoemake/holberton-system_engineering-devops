#!/usr/bin/python3
""" dictionary of list of dictionaries """

import json
import requests

def export_all():
    """ exports all things ever """
    users_and_tasks = {}

    user_json = requests.get('https://jsonplaceholder.typicode.com/users/').json()
    todos_json = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    user_info = {}
    for user in user_json:
        user_info[user['id']] = user['username']

    for task in todos_json:
        if users_and_tasks.get(task['userId'], False) is False:
            users_and_tasks[task['userId']] = []
        task_dict = {}
        task_dict['username'] = user_info[task['userId']]
        task_dict['task'] = task['title']
        task_dict['completed'] = task['completed']

        users_and_tasks[task['userId']].append(task_dict)

    with open("todo_all_employees.json", 'w') as jsonFile:
        json.dump(users_and_tasks, jsonFile)


if __name__ == "__main__":
    export_all()

# need all users -> make dict id:username
# get all todos
# loop the todos
# if userID in task not in the dict: add it with value of empty list
# create new task dict
# append task dict to specific user's list
# put it in the file! 
