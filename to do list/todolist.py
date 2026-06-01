# 📌 To-Do List Project

def add_task():
    task = input("Enter a new task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("✅ Task added successfully!")

def view_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

            if not tasks:
                print("No tasks found.")
                return

            print("\n--- Your To-Do List ---")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")

    except FileNotFoundError:
        print("⚠️ No task file found. Add a task first!")

def delete_task():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        view_tasks()
        choice = int(input("\nEnter task number to delete: "))

        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print(f"🗑️ Task '{removed.strip()}' deleted successfully!")
        else:
            print("Invalid task number.")

    except FileNotFoundError:
        print("⚠️ No task file found. Add a task first!")

# 🔁 Main Menu Loop
while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("👋 Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
