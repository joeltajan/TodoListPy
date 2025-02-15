tasks = []

def show_tasks():
    if not tasks:
        print("No tasks added.")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def delete_task():
    show_tasks()
    try:
        idx = int(input("Enter task number to delete: ")) - 1
        removed = tasks.pop(idx)
        print(f"Task '{removed}' removed.")
    except (IndexError, ValueError):
        print("Invalid task number.")

while True:
    print("\nTo-Do List Menu")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
