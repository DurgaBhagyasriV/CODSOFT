tasks = []
def add_newtask():
    newtask = input("Enter a task: ")
    tasks.append(newtask)
    print("Newtask added successfully!")
def view_existingtasks():
    if tasks == []:
        print("There are no tasks in the list.")
    else:
        print("Tasks in the list are:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
def remove_task():
    if tasks == []:
        print("There are no tasks to remove.")
    else:
        view_existingtasks()
        try:
            task_num = int(input("Enter the task number to remove: "))
            if len(task_num) <= len(tasks):
                remove = tasks.pop(task_num)
                print(f"The task that is removed is: {remove}")
            else:
                print(f"The task number {task_num} does not exist.\nPlease enter a valid task number.")
        except ValueError:
            print("Please enter a valid number.")
while True:
    print("\nTo-Do List Options: \n1. Add a Task  \n2. View Tasks  \n3. Remove a Task  \n4. Exit")

    try:
        user_input = input("Please enter your choice: ")
        list_options = int(user_input)

        if list_options == 1:
         add_newtask()
        elif list_options == 2:
         view_existingtasks()
        elif list_options == 3:
         remove_task()
        elif list_options == 4:
         print("exiting list")
         break
        else:
         print("Please enter a valid choice.")

        want_to_continue = input("Do you want to perform any other function? (yes/no): ")
        if want_to_continue.lower() == 'no':
            print("Closing the list....\nThe list is closed.")
            break

    except ValueError:
        print("Please enter a valid option.")