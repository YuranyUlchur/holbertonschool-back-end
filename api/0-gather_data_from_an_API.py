#!/usr/bin/python3
"""
Gather data from an API
"""
import requests


def get_employee_todo_progress(employee_id):
    """
    returns information about his/her TODO list progress.
    """

    """
    Perform GET request to the API to obtain the list of tasks
    """
    todos_response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
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
    employee_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    employee = employee_response.json()

    """Get employee name"""
    employee_name = employee['name']


    print(f'Empleado {employee_name} ha completado tareas {number_of_done_tasks}/{total_number_of_tasks}:')

    """Print title of completed tasks"""
    for task in completed_tasks:
        print('\t', task['title'])


if __name__ == "__main__":
    """Prompts the user for the employee's ID"""
    employee_id = int(input("Ingrese el ID del empleado: "))

    get_employee_todo_progress(employee_id)