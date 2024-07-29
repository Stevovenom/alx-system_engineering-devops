#!/usr/bin/python3

"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

from requests import get
from sys import argv

def fetch_employee_todo_progress(employee_id):
    """
    Fetch and display the TODO list progress of an employee.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    # Fetch employee details
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    user_response = get(user_url)
    todos_response = get(todos_url)

    # Ensure successful API response
    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Error fetching data from the API.")
        return

    user = user_response.json()
    todos = todos_response.json()

    # Extract employee details
    employee_name = user.get("name")
    total_tasks = len(todos)
    done_tasks = [todo for todo in todos if todo.get("completed")]

    # Display employee's TODO list progress
    print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        exit(1)

    try:
        employee_id = int(argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        exit(1)

    fetch_employee_todo_progress(employee_id)
