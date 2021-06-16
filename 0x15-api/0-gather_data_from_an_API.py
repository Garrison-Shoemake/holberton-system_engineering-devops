#!/usr/bin/python3
""" gathers data from API """

#notes:
# need to use sys to get input from terminal
# need to look at API provided
## need to find out how to get user information
## name, num of tasks done and not, task titles
## dont forget the tab and space
## look at requests module

import requests
import sys

def get_employee_tasks(employeeId):
    """ gets the task of the employees """
    # variables
    name = ''
    task_list = []
    completed_counter = 0

    #do get requests
    userRes = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(employeeId))
    todosRes = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.format(employeeId))

    # get json from responses
    name = userRes.json().get('name')
    todosJson = todosRes.json()

    # loop tasks
    for task in todosJson:
        if task.get('completed') is True:
            # up counter if completed
            completed_counter += 1
            #save task title to task_list
            task_list.append(task.get('title'))

    #print first line
    print("Employee {} is done with tasks ({}/{}):".format(name, completed_counter, len(todosJson)))
    #loop task_list and print tasks
    for title in task_list:
        print("\t {}".format(title))

    return

if __name__ == "__main__":
    get_employee_tasks(sys.argv[1])
