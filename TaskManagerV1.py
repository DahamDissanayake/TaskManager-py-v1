# Author: Daham Dissanayake
# Date: 26/03/2025
# Use: Personal Task Manager with File Handling

#------------------------------------------------------------------------------

# File to store tasks
# This file will store tasks persistently between program runs
task_file = "tasks.txt"

# List to store tasks in memory
tasks = []

# Function to load tasks from file
def load_tasks_from_file():
    """Loads tasks from the file into the tasks list."""
    global tasks  # Using the global tasks list
    try:
        with open(task_file, "r") as file:
            for line in file:
                task_details = line.strip().split(" | ")  # Splitting task details stored in the file
                if len(task_details) == 4:  # Ensuring the correct format
                    tasks.append(task_details)  # Adding to the list
    except FileNotFoundError:
        # If file does not exist, no tasks are loaded
        # This handles requirement #5 - File Not Found scenario
        pass  

# Function to save tasks to file
def save_tasks_to_file():
    """Saves all tasks from the tasks list into the file."""
    with open(task_file, "w") as file:
        for task in tasks:
            file.write(" | ".join(task) + "\n")  # Writing each task in a formatted manner

# Function to add a task
def add_task():
    """Allows the user to input a new task and adds it to the list."""
    # Handle requirement #1 - Valid Input
    task_name = input("Enter task name: ")  # Getting task name from user
    description = input("Enter task description: ")  # Getting task description


    priority = input("Enter task priority (high/medium/low): ")  # Getting priority level1
    due_date = input("Enter due date (YYYY-MM-DD): ")  # Getting due date
    

    tasks.append([task_name, description, priority, due_date])  # Adding task to list
    save_tasks_to_file()  # Saving tasks to file for persistence - handles requirement #6
    print("Task added successfully!\n")

# Function to view all tasks
def view_tasks():
    """Displays all tasks in the tasks list."""
    if not tasks:
        print("No tasks available!\n")  # Message if no tasks exist
        return
    
    # Handle requirement #2 - Viewing With Multiple Tasks
    print("\nTasks List:")
    for index, task in enumerate(tasks, start=1):  # Looping through tasks with numbering
        print(f"Task {index}:")
        print(f" Name: {task[0]}")
        print(f" Description: {task[1]}")
        print(f" Priority: {task[2]}")
        print(f" Due Date: {task[3]}\n")

# Function to update a task
def update_task():
    """Allows the user to update a specific task."""
    if not tasks:
        print("No tasks available to update!\n")
        return
    
    try:
        task_index = int(input("Enter task number to update (1-based index): ")) - 1  # Get task number
        # Handle requirement #3 - Invalid Task Number
        if task_index not in range(len(tasks)):
            print("Invalid task number!\n")
            return
        
        print("\nSelect the field to update:")
        print("1. Name")
        print("2. Description")
        print("3. Priority")
        print("4. Due Date")
        
        criteria = input("Enter the corresponding number: ")  # Get field to update
        
        fields = ["Name", "Description", "Priority", "Due Date"]
        if criteria in ['1', '2', '3', '4']:
            modified_value = input(f"Enter the new {fields[int(criteria)-1]}: ")
            tasks[task_index][int(criteria)-1] = modified_value  # Update task
            save_tasks_to_file()  # Save updated tasks
            print("Task updated successfully!\n")
        else:
            print("Invalid option.\n")
    except ValueError:
        print("Invalid input! Please enter a number.\n")

# Function to delete a task
def delete_task():
    """Allows the user to delete a task."""
    if not tasks:
        print("No tasks available to delete!\n")
        return
    
    try:
        task_index = int(input("Enter task number to delete (1-based index): ")) - 1  # Get task number
        # Handle requirement #3 - Invalid Task Number
        if task_index not in range(len(tasks)):
            print("Invalid task number!\n")
            return
        
        # Handle requirement #4 - Valid Task Deletion
        del tasks[task_index]  # Remove task from list
        save_tasks_to_file()  # Save updated task list
        print("Task deleted successfully!\n")
    except ValueError:
        print("Invalid input! Please enter a number.\n")

# Main execution starts here
if __name__ == "__main__":
    load_tasks_from_file()  # Load existing tasks before showing menu
    
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option: ")  # Get user choice
        
        if choice == '1':
            add_task()  # Call function to add task
        elif choice == '2':
            view_tasks()  # Call function to view tasks
        elif choice == '3':
            update_task()  # Call function to update task
        elif choice == '4':
            delete_task()  # Call function to delete task
        elif choice == '5':
            print("Exiting Task Manager!")
            break  # Exit loop and program
        else:
            print("Invalid choice! Please try again!\n")  # Handle invalid input