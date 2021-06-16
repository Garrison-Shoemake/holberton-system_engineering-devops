#!/usr/bin/python3
""" prints to CSV format """
import csv
import requests
import sys

def save_tasks_to_csv(employeeId):
    """ function to save to CSV """
    username = ''
    allTasks = []

    userRes = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(employeeId))
    todosRes = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.format(employeeId))

    username = userRes.json().get('username')
    todosJson = todosRes.json()

    for task in todosJson:
        taskRow = []
        taskRow.append(employeeId)
        taskRow.append(username)
        taskRow.append(task.get("completed"))
        taskRow.append(task.get("title"))

        allTasks.append(taskRow)

        with open("{}.csv".format(employeeId), 'w') as csvFile:
                  csvwriter = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
                  csvwriter.writerows(allTasks)

    return

if __name__ == "__main__":
    save_tasks_to_csv(sys.argv[1])



# notes
# a file -> CSV (value,value)
# open and write
#specific file (ID.csv)
#all tasks for users -> 

# to use CSV module
# need to loop all tasks and add them to a list
#open file 
# csvwriter = csv.write(ourfile, quoting=csv.QUOTE_ALL)
# use csvwriter.writerows(taskList)
