#!/usr/bin/python3
import requests


def get_employee_todo_progress(employee_id):

    todos_response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
    todos = todos_response.json()


    completed_tasks = [todo for todo in todos if todo['completed']]

    number_of_done_tasks = len(completed_tasks)
    total_number_of_tasks = len(todos)

    employee_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    employee = employee_response.json()

    employee_name = employee['name']


    print(f'Empleado {employee_name} ha completado tareas {number_of_done_tasks}/{total_number_of_tasks}:')


    for task in completed_tasks:
        print('\t', task['title'])


if __name__ == "__main__":

    employee_id = int(input("Ingrese el ID del empleado: "))

    get_employee_todo_progress(employee_id)