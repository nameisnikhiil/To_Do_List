# Simple To-Do List in Python
tasks = []

def show_menu():
    print("\n=== To-Do List ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Quit")

def add_task():
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print(f" Task added: {task}")
    else:
        print(" Task cannot be empty!")

def view_tasks():
    if not tasks:
        print(" No tasks yet!")
    else:
        print("\n Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def remove_task():
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input("\nEnter task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"  Removed: {removed}")
        else:
            print(" Invalid task number!")
    except ValueError:
        print(" Please enter a valid number!")

# Main program loop
print("Welcome to Simple To-Do List! ")
while True:
    show_menu()
    choice = input("\nEnter your choice (1-4): ").strip()
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print(" Goodbye! Have a productive day!")
        break
    else:
        print(" Invalid choice! Please enter 1, 2, 3, or 4.")