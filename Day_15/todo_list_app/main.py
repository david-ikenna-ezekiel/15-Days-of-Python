# Importing the functions from the todo_functions module

import todo_functions as todo

def display_menu():
    print("\nTodo List Application")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Complete a task")
    print("4. Delete a task")
    print("5. Exit")

def handle_choice(choice, tasks):
    if choice == '1':
        todo.display_tasks(tasks)
    elif choice == '2':
        title = input("Enter the task title: ")
        todo.add_task(tasks, title)
    elif choice == '3':
        task_number = int(input("Enter the task number to mark as completed: "))
        todo.complete_task(tasks, task_number)
    elif choice == '4':
        task_number = int(input("Enter the task number to delete: "))
        todo.delete_task(tasks, task_number)
    elif choice == '5':
        todo.save_tasks(tasks)
        print("Goodbye!")
        return False
    else:
        print("Invalid choice. Please select a valid option.")
    return True

# main program loop

if __name__ == "__main__":
    tasks = todo.load_tasks()
    print("Welcome to the Todo List Application!")

    while True:
        display_menu()
        choice = input("Choose an option: ")
        if not handle_choice(choice, tasks):
            break
