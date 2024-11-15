import json
import os

# Add a new task
def add_task(tasks, title):
    tasks.append({"title": title, "completed": False})
    print(f"Task '{title}' added.")

# Load tasks from a file
def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            return json.load(file)
    return []

# Save tasks to a file
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

# Display the tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks, 1):
            status = "✓" if task['completed'] else "✗"
            print(f"{index}. {task['title']} [{status}]")

# Complete a task
def complete_task(tasks, task_number):
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]['completed'] = True
        print(f"Task {task_number} marked as completed.")
    else:
        print("Invalid task number.")

# Delete a task
def delete_task(tasks, task_number):
    if 0 < task_number <= len(tasks):
        task = tasks.pop(task_number - 1)
        print(f"Task '{task['title']}' deleted.")
    else:
        print("Invalid task number.")
