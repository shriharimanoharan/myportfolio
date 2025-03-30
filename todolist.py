tasks = []

def show_menu():
    print("\nTo-Do List App")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Exit")

def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task, "done": False})
    print(f"Added: {task}")

def view_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            status = "✓" if task["done"] else " "
            print(f"{i}. [{status}] {task['task']}")

def mark_done():
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a number")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again")