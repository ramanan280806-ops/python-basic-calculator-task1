todo_list = []
def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")
def todo_app():
    while True:
        show_menu()
        choice = input("Enter choice: ")
        if choice == "1":
            task = input("Enter task: ")
            todo_list.append(task)
            print("Task added.")
        elif choice == "2":
            task = input("Enter task to remove: ")
            if task in todo_list:
                todo_list.remove(task)
                print("Task removed.")
            else:
                print("Task not found.")
        elif choice == "3":
            print("\nYour Tasks:")
            for t in todo_list:
                print("-", t)
        elif choice == "4":
            break
        else:
            print("Invalid input")
todo_app()
