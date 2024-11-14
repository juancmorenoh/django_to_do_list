# Task Management Application

This is a simple Django-based task management application that allows users to create, view, update, and delete tasks. Users can also mark tasks as completed and reset the entire task list.

## Features

- **Add Task**: Create a new task with a title, description, and completion status.
- **View Task List**: Display a list of all tasks, with options to mark tasks as completed.
- **Task Detail View**: View details of a specific task.
- **Delete Task**: Delete an individual task.
- **Reset Task List**: Delete all tasks to reset the task list.

## Project Structure

- `models.py`: Contains the `Task` model, which represents a task with fields for `title`, `description`, `completed` status, and `created_at` timestamp.
- `forms.py`: Contains the `TaskForm`, a Django form based on the `Task` model.
- `views.py`: Handles user requests and responses, providing views for adding, viewing, deleting, and resetting tasks.
- `templates/`: Contains HTML templates for each page, such as the task list, add task, detail task, delete task, and reset confirmation.