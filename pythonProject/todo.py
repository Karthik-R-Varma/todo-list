import json  # Import the json module for file handling


# Function to add a new task
def add_task(task_list, task_description):
    task_id = len(task_list) + 1  # Generate a new task ID
    task = {'id': task_id, 'task': task_description, 'completed': False}  # Create a new task dictionary
    task_list.append(task)  # Add the new task to the task list
    print(f"Task added: {task_description}")


# Function to view all tasks
def view_tasks(task_list):
    if not task_list:  # Check if the task list is empty
        print("No tasks in the list.")
    for task in task_list:  # Iterate through each task in the list
        status = "Completed" if task['completed'] else "Not completed"  # Determine the status of the task
        print(f"{task['id']}. {task['task']} - {status}")  # Print the task details


# Function to mark a task as completed
def mark_task_completed(task_list, task_id):
    for task in task_list:  # Iterate through each task in the list
        if task['id'] == task_id:  # Find the task with the matching ID
            task['completed'] = True  # Mark the task as completed
            print(f"Task {task_id} marked as completed.")
            return
    print(f"Task {task_id} not found.")  # Print an error if the task ID is not found


# Function to delete a task
def delete_task(task_list, task_id):
    for task in task_list:  # Iterate through each task in the list
        if task['id'] == task_id:  # Find the task with the matching ID
            task_list.remove(task)  # Remove the task from the list
            print(f"Task {task_id} deleted.")
            return
    print(f"Task {task_id} not found.")  # Print an error if the task ID is not found


# Function to save tasks to a file
def save_tasks_to_file(task_list, filename):
    with open(filename, 'w') as file:  # Open the file in write mode
        json.dump(task_list, file)  # Write the task list to the file as JSON
    print("Tasks saved to file.")


# Function to load tasks from a file
def load_tasks_from_file(filename):
    try:
        with open(filename, 'r') as file:  # Open the file in read mode
            task_list = json.load(file)  # Load the task list from the file
        print("Tasks loaded from file.")
        return task_list
    except FileNotFoundError:  # Handle the case where the file is not found
        print("No saved tasks found. Starting with an empty list.")
        return []


# Main function to run the application
def main():
    filename = "tasks.json"  # Define the filename for saving/loading tasks
    task_list = load_tasks_from_file(filename)  # Load existing tasks from the file

    while True:
        # Display the menu options
        print("\nTo-Do List Application")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Save and exit")

        choice = input("Choose an option: ")  # Get the user's choice

        if choice == '1':
            task_description = input("Enter task description: ")  # Get the task description from the user
            add_task(task_list, task_description)  # Add the new task
        elif choice == '2':
            view_tasks(task_list)  # View all tasks
        elif choice == '3':
            task_id = int(input("Enter task ID to mark as completed: "))  # Get the task ID to mark as completed
            mark_task_completed(task_list, task_id)  # Mark the task as completed
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))  # Get the task ID to delete
            delete_task(task_list, task_id)  # Delete the task
        elif choice == '5':
            save_tasks_to_file(task_list, filename)  # Save tasks to file and exit
            break  # Exit the loop to end the program
        else:
            print("Invalid option. Please choose again.")  # Handle invalid menu options


# Entry point for the script
if __name__ == "__main__":
    main()  # Call the main function to run the program
