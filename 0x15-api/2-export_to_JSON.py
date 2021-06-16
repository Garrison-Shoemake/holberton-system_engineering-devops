#!/usr/bin/python3
""" exports to JSON """

import json
import requests
import sys

def export_to_json(employeeId):
    """ method to run """

    username = ''
    userDict = {}

    userRes = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(employeeId))
    todosRes = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.format(employeeId))

    username = userRes.json().get('username')
    todosJson = todosRes.json()

    userDict[employeeId] = []

    for task in todosJson:
        taskDict = {}
        taskDict["task"] = task.get('title')
        taskDict["username"] = username
        taskDict["completed"] = task.get('completed')

        userDict[employeeId].append(taskDict)

    with open("{}.json".format(employeeId), 'w') as jsonFile:
        json.dump(userDict, jsonFile)

if __name__ == "__main__":
    export_to_json(sys.argv[1])
