##0x15. API
This task covers the concepts in the following areas: <br>
1. Python
2. Scripting
3. Back-end
4. API


Stay Tuned as we work out the solutions of this task to completion.

#Task 0
For this particular task, we need to:<br>

This task requires you to write a Python script that interacts with a REST API to fetch and display information about an employee's TODO list progress. Here’s a detailed breakdown of what this task entails:

1. Objective
Create a Python script that, given an employee ID, retrieves and displays the TODO list progress of that employee using a specific REST API.
<br>
2. Requirements
Modules: You must use either the urllib or requests module to make HTTP requests to the API.<br>
Input Parameter: The script should accept a single integer parameter, which represents the employee ID.<br>
Output Format: The script should display the TODO list progress in a specific format.<br>
3. Output Format
First Line: Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):<br>
i. EMPLOYEE_NAME: The name of the employee.<br>
ii. NUMBER_OF_DONE_TASKS: The number of tasks that the employee has completed.<br>
iii. TOTAL_NUMBER_OF_TASKS: The total number of tasks assigned to the employee.<br>
iv. Subsequent Lines: Titles of the completed tasks, each preceded by a tab character and a space.<br>
