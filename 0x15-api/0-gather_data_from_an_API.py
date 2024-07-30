#!/usr/bin/python3
"""For a given employee ID, returns information about
their TODO list progress"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        userId = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    # Fetch user information
    user_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{userId}")
    if user_response.status_code != 200:
        print("Error fetching user data from the API.")
        sys.exit(1)

    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch TODO list
    todos_response = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={userId}")
    if todos_response.status_code != 200:
        print("Error fetching todos data from the API.")
        sys.exit(1)

    todos_data = todos_response.json()
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get('completed')]

    # Display TODO list progress
    print(
        f"Employee {employee_name} is done with tasks({len(completed_tasks)
                                                       }/{total_tasks}): ")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")
