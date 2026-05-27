#maya
def main():
    todo_list = []
    done_list = []

    while True:
        print("-" * 40)
        print(f"You have {len(todo_list)} items left to do.")
        if todo_list:
            print("To-Do List:")
            for i, task in enumerate(todo_list):
                print(f"  {i + 1}. {task}")
        if done_list:
            print("Completed Items:")
            for task in done_list:
                print(f"  ✓ {task}")
        print("-" * 40)
        print("Menu Options:")
        print("1. Add an item to the to-do list")
        print("2. Mark an item as Done")
        print("3. Remove an item or Clear the List")
        print("4. Exit the program")
        print("-" * 40)

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            task = input("Enter a task to add: ")c
            if task:
                todo_list.append(task)
                print(f"'{task}' added to the to-do list.")
            else:
                print("Task cannot be blank. Please try again.")

        elif choice == '2':
            if not todo_list:
                print("Your to-do list is empty. Nothing to mark as done.")
                continue

            try:
                item_num = int(input("Enter the number of the item you completed: "))
                if 1 <= item_num <= len(todo_list):
                    completed_task = todo_list.pop(item_num - 1)
                    done_list.append(completed_task)
                    print(f"'{completed_task}' marked as done and moved to completed list.")
                else:
                    print("Invalid item number. Please enter a number from the list.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '3':
            if not todo_list:
                print("Your to-do list is empty. Nothing to remove.")
                continue

            remove_choice = input("Do you want to (R)emove a single item or (C)lear the entire list? (R/C): ").strip().lower()

            if remove_choice == 'r':
                try:
                    item_num = int(input("Enter the number of the item you want to remove: "))
                    if 1 <= item_num <= len(todo_list):
                        removed_task = todo_list.pop(item_num - 1)
                        print(f"'{removed_task}' removed from the to-do list.")
                    else:
                        print("Invalid item number. Please enter a number from the list.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            elif remove_choice == 'c':
                todo_list.clear()
                print("The entire to-do list has been cleared.")
            else:
                print("Invalid choice. Please enter 'R' or 'C'.")

        elif choice == '4':
            print("Exiting the To-Do List application. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

main()
