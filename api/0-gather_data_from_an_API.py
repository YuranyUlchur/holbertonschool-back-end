#!/usr/bin/python3
"""
Gather data from an API
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    returns information about his/her TODO list progress.
    """

    """
    Perform GET request to the API to obtain the list of tasks
    """
    link = (f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
    todos_response = requests.get(link)
    todos = todos_response.json()

    """
    Filter completed tasks
    """
    completed_tasks = [todo for todo in todos if todo['completed']]

    """
    Counts number of completed tasks and total number of tasks
    """
    number_of_done_tasks = len(completed_tasks)
    total_number_of_tasks = len(todos)

    """
    obtain employee information
    """
    link2 = (f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    employee_response = requests.get(link2)
    employee = employee_response.json()

    """Get employee name"""
    employee_name = employee['name']

    print("Employee {} is done with tasks({}\{}):".format(employee_name, number_of_done_tasks, total_number_of_tasks))

    """Print title of completed tasks"""
    for task in completed_tasks:
        print('\t', task['title'])


if __name__ == "__main__":
    """Prompts the user for the employee's ID"""
    employee_id = (int(sys.argv[1]))

    get_employee_todo_progress(employee_id)
