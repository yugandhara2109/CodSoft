tasks = [
    {"id": 1, "title": "Buy groceries", "status": "Pending", "due_date": "2025-01-15"},
    {"id": 2, "title": "Finish project", "status": "Completed", "due_date": "2025-01-10"}
]
def add_task(title, due_date):
    task = {"id": len(tasks) + 1, "title": title, "status": "Pending", "due_date": due_date}
    tasks.append(task)

def update_task(task_id, new_title=None, new_status=None):
    for task in tasks:
        if task["id"] == task_id:
            if new_title:
                task["title"] = new_title
            if new_status:
                task["status"] = new_status
            break

def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]

def display_tasks():
    for task in tasks:
        print(f"ID: {task['id']}, Title: {task['title']}, Status: {task['status']}, Due: {task['due_date']}")
def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. View All Tasks")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            title = input("Enter task title: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(title, due_date)
        elif choice == "2":
            task_id = int(input("Enter task ID to update: "))
            new_title = input("Enter new task title (leave blank to keep current): ")
            new_status = input("Enter new status (Pending/Completed): ")
            update_task(task_id, new_title, new_status)
        elif choice == "3":
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == "4":
            display_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

import json

def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

tasks = load_tasks()



