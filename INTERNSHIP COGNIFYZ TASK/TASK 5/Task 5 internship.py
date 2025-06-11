import json
import os

TASK_FILE = "tasks.json"

# 🔁 Always initialize an empty JSON file if not present
def init_file():
    if not os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'w') as f:
            json.dump([], f)
            print("📂 tasks.json created.")

# 📤 Load from JSON file
def load_tasks():
    try:
        with open(TASK_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# 💾 Save to JSON file
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

# 📋 Menu
def display_menu():
    print("\n📋 TASK MANAGER (Persistent Storage)")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

# 👀 View
def view_tasks(tasks):
    if not tasks:
        print("📭 No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['title']} - {task['description']}")

# ➕ Add
def add_task(tasks):
    title = input("Enter title: ").strip()
    if not title:
        print("❌ Title cannot be empty.")
        return
    description = input("Enter description: ").strip()
    if not description:
        print("❌ Description cannot be empty.")
        return
    tasks.append({'title': title, 'description': description})
    save_tasks(tasks)
    print("✅ Task saved to file.")

# 🔁 Update
def update_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        idx = int(input("Task number to update: ")) - 1
        if 0 <= idx < len(tasks):
            new_title = input("New title: ").strip()
            new_desc = input("New description: ").strip()
            if not new_title or not new_desc:
                print("❌ Title or description cannot be empty.")
                return
            tasks[idx]['title'] = new_title
            tasks[idx]['description'] = new_desc
            save_tasks(tasks)
            print("🔁 Task updated.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Enter a valid number.")

# 🗑️ Delete
def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        idx = int(input("Task number to delete: ")) - 1
        if 0 <= idx < len(tasks):
            deleted = tasks.pop(idx)
            save_tasks(tasks)
            print(f"🗑️ Task deleted: {deleted['title']}")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Enter a valid number.")

# 🚀 Main App
def main():
    init_file()
    print("🚀 Task 5: File-Based Task Manager Started")
    while True:
        tasks = load_tasks()
        display_menu()
        choice = input("Select option (1-5): ").strip()
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("👋 Exiting. All tasks saved.")
            break
        else:
            print("❌ Invalid input. Choose from 1 to 5.")

if __name__ == "__main__":
    main()
