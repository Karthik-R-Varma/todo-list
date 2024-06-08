# todo-list
This repository consists of code which implements a todo list. It executes, adding a new task, viewing the tasks previously entered, changing the status of tasks to completed, deleting task entries, and saving the changes made.

# To-Do List Application

This is a simple command-line To-Do List application written in Python. The application allows you to add tasks, view tasks, mark tasks as completed, delete tasks, and save/load tasks to/from a file.

## Features

- Add a new task
- View all tasks
- Mark a task as completed
- Delete a task
- Save tasks to a file
- Load tasks from a file

## Requirements

- Python 3.x

## Usage

When you run the application, you will see the following menu:

To-Do List Application

Add task
View tasks
Mark task as completed
Delete task
Save and exit
Choose an option:


### Adding a Task

Select option 1 and enter the task description. The task will be added to the list.

### Viewing Tasks

Select option 2 to view all tasks. You will see the task ID, description, and status (completed or not completed).

### Marking a Task as Completed

Select option 3 and enter the task ID you want to mark as completed.

### Deleting a Task

Select option 4 and enter the task ID you want to delete.

### Saving and Exiting

Select option 5 to save the tasks to a file (`tasks.json`) and exit the application. The next time you run the application, the tasks will be loaded from this file.

## Example

Here's a brief example of how to use the application:

1. Run the application:
    ```sh
    python todo.py
    ```

2. Add a task:
    ```
    1. Add task
    Enter task description: Buy groceries
    Task added: Buy groceries
    ```

3. View tasks:
    ```
    2. View tasks
    1. Buy groceries - Not completed
    ```

4. Mark a task as completed:
    ```
    3. Mark task as completed
    Enter task ID to mark as completed: 1
    Task 1 marked as completed.
    ```

5. Delete a task:
    ```
    4. Delete task
    Enter task ID to delete: 1
    Task 1 deleted.
    ```

6. Save and exit:
    ```
    5. Save and exit
    Tasks saved to file.
    ```


