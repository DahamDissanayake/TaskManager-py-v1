# TaskManager-py-v1
The Personal Task Manager is a Python-based application that manages tasks with simple file handling. It creates a text file to store task data, automatically saving changes during add, view, update, and delete operations. Tasks are loaded from the file at startup, ensuring data is always available across sessions.

# Personal Task Manager

A simple command-line task management application written in Python that allows users to create, view, update, and delete tasks with persistent file storage.

## Author
**Daham Dissanayake**  
*Date: March 26, 2025*

## Features

- **Add Tasks**: Create new tasks with name, description, priority, and due date
- **View Tasks**: Display all tasks in a numbered, formatted list
- **Update Tasks**: Modify existing task details (name, description, priority, or due date)
- **Delete Tasks**: Remove tasks from your list
- **Persistent Storage**: Tasks are automatically saved to and loaded from a file
- **Error Handling**: Robust input validation and error management

## Requirements

- Python 3.x
- No external dependencies required

## Installation

1. Clone or download the `Personal_Task_Manager_file_handling.py` file
2. Ensure Python 3.x is installed on your system
3. Run the application from your terminal or command prompt

## Usage

### Running the Application

```bash
python Personal_Task_Manager_file_handling.py
```

### Menu Options

When you run the application, you'll see the following menu:

```
Task Manager
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Exit
```

### Adding a Task

1. Select option `1` from the main menu
2. Enter the following information:
   - **Task Name**: A brief title for your task
   - **Description**: Detailed description of the task
   - **Priority**: Choose from `high`, `medium`, or `low`
   - **Due Date**: Enter in YYYY-MM-DD format

### Viewing Tasks

Select option `2` to display all your tasks in a formatted list showing:
- Task number
- Name
- Description
- Priority level
- Due date

### Updating a Task

1. Select option `3` from the main menu
2. Enter the task number you want to update (1-based index)
3. Choose which field to update:
   - Name
   - Description
   - Priority
   - Due Date
4. Enter the new value

### Deleting a Task

1. Select option `4` from the main menu
2. Enter the task number you want to delete (1-based index)
3. The task will be permanently removed

## File Structure

```
├── Personal_Task_Manager_file_handling.py  # Main application file
└── tasks.txt                              # Auto-generated task storage file
```

## Data Storage

Tasks are stored in a `tasks.txt` file in the following format:
```
Task Name | Description | Priority | Due Date
```

The file is automatically created when you add your first task and is updated whenever you make changes.

## Error Handling

The application handles various error scenarios:

- **File Not Found**: If the tasks file doesn't exist, the application starts with an empty task list
- **Invalid Task Numbers**: Validates task indices when updating or deleting
- **Invalid Input**: Handles non-numeric input for menu selections and task numbers
- **Priority Validation**: Ensures priority levels are correctly entered

## Example Usage

```
Task Manager
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Exit
Choose an option: 1

Enter task name: Complete Python Project
Enter task description: Finish the personal task manager application
Enter task priority (high/medium/low): high
Enter due date (YYYY-MM-DD): 2025-04-01
Task added successfully!
```

## Limitations

- Tasks are stored in plain text format
- No advanced filtering or sorting options
- Basic date validation (format checking only)
- Single-user application

## Future Enhancements

Potential improvements could include:
- Task completion status tracking
- Advanced date validation and reminders
- Task categories or tags
- Search and filter functionality
- GUI interface
- Task scheduling and notifications

## License

This project is open source and available for educational and personal use.

## Support

For questions or issues, please refer to the code comments or create an issue in the project repository.