import json

FILE_PATH = "To Do List Manager/todo.json"

def main():
    tasks = load_task()

    while True:
        print()
        print("To Do List Manager: ")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        print()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_task(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("GOODBYE!!")
            break
        else:
            print("Invalid choice. Please try again.")

def load_task():
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except:
        return {"tasks": []}

def save_tasks(tasks):
    try:
        with open(FILE_PATH, "w") as file:
            json.dump(tasks, file)
    except:
        print("Couldn't save!!!")

def add_task(tasks):
    description = input("Enter the description of the task: ").strip()
    if description:
        tasks["tasks"].append({"description": description, "complete": False})
        save_tasks(tasks)
        print("Task added.\n")
    else:
        print("Please provide a description.")

def view_task(tasks):
    print()
    task_list = tasks["tasks"]
    if len(task_list) == 0:
        print("No task to Display")
    else:
        print("Your To Do list: ")
        for idx, task in enumerate(task_list):
            status = "[Completed]" if task["complete"] else "[Pending]"
            print(f"{idx + 1}. {task['description']} | {status}")

def complete_task(tasks):
    view_task(tasks)
    try:
        task_num = int(input("Enter the task number to mark as complete: ").strip())
        if 1 <= task_num <= len(tasks["tasks"]):
            tasks["tasks"][task_num - 1]["complete"] = True
            save_tasks(tasks)
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except:
        print("Enter a valid number.")

def delete_task(tasks):
    view_task(tasks)
    try:
        task_num = int(input("Enter the task number to delete: ").strip())
        if 1 <= task_num <= len(tasks["tasks"]):
            del tasks["tasks"][task_num - 1]
            save_tasks(tasks)
            print("Task deleted.")
        else:
            print("Invalid task number.")
    except:
        print("Enter a valid number.")

main()