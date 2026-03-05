'''7. Create a Todo list Manager where users can add, view, and remove tasks. Use List for 
storing tasks. '''
tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully.")

    elif choice == 2:
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nTodo List:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    elif choice == 3:
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])
            num = int(input("Enter task number to remove: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print("Removed task:", removed)
            else:
                print("Invalid task number.")

    elif choice == 4:
        print("Exiting Todo Manager.")
        break

    else:
        print("Invalid choice. Try again.")