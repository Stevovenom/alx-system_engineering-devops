#!/usr/bin/python3

import requests
import sys

def fetch_employee_todo_progress(employee_id):
    # fetch teh employee details
    user_url = f"http://jsonplacejolder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    user_response =  request.get(user_url)
    todos_response = request.get(todo_url)

    #ensure successful API response
    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Error fetching data from teh API.")

        user =  user_response.json()
        todos = todos_response.json()

        #extract the employee details
        employee_name = user.get("name")
        total_tasks = len(todos)
        done_tasks = [todo for todo in todos if todo.get("completed")]

        #display the employees todo list progress
        print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{total_tasks}):")

        for task in done_tasks:
            print(f"\t {task.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

        try:
            employee_id = int(sys.argv[1])
        except ValueError:
            print("Employee ID must be an integer.")
            sys.exit(1)

        fetch_employee_todo_progress(employee_id)
